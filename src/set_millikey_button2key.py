#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import sys

import serial
import os
import json

# Device index to update key mapping. If only one Millikey is connect,
# DEVICE_INDEX must be 0.
DEVICE_INDEX = 0

# Button ID to update ( 1 - num_buttons )
BUTTON_ID = 1

# Key label to map to. a == 'A', 1 == '1', etc.
KEY_NAME = '2'

# Save changes to device eeprom.
# If False, button mapping will revert to default
# when device is unplugged and reconnected.
SAVE_CHANGES = True

def get_serial_ports():
    """
    Return a list of serial ports that are currently available and connectable.
    """
    available = []
    if os.name == 'nt':
        for i in range(1, 256):
            try:
                sport = 'COM' + str(i)
                s = serial.Serial(sport, baudrate=128000)
                available.append(sport)
                s.close()
            except (serial.SerialException, ValueError):
                pass
    else:  # Mac / Linux
        from serial.tools import list_ports
        available = [port[0] for port in list_ports.comports()]
    return available


def get_millikey_devices():
    """
    Return information about any attached MilliKey devices.
    Each detected MilliKey will be represented as a dict containing
    the current device state and settings.
    """
    devices = []
    available = get_serial_ports()
    for p in available:
        try:
            mkey_sport = serial.Serial(p, baudrate=128000, timeout=0.1)
            mkey_sport.write(b"GET CONFIG\n")
            rx_data = mkey_sport.readline()
            if rx_data:
                rx_data = rx_data.strip()
                try:
                    mkconf = json.loads(rx_data)
                    mkconf['port'] = p
                    if mkconf['model_name'] != 'USB2TTL8':
                        devices.append(mkconf)
                except Exception:
                    raise RuntimeError("ERROR: {}".format(rx_data))
            mkey_sport.close()
        except Exception:
            pass
    return devices


if __name__ == "__main__":
    # Get connected MilliKeys
    millikeys = get_millikey_devices()

    # Check that device was found
    if not millikeys:
        print("Error: No MilliKey Devices detected.")
        sys.exit()
    elif len(millikeys) < DEVICE_INDEX+1:
        print("Error: Update requested for device index %d, but only %d devices where found." % (DEVICE_INDEX,
                                                                                                 len(millikeys)))
        sys.exit()
    else:
        millikey = millikeys[DEVICE_INDEX]
        print()
        print("Updating MilliKey Device:")
        print("\tName:\t\t\t{}".format(millikey.get('name')))
        print("\tSerial Port:\t{}".format(millikey.get('port')))
        print("\tSerial Number:\t{}".format(millikey.get('product_serial')))
        print()

    # Open serial connection to DEVICE_INDEX Millikey found
    sport = serial.Serial(millikeys[DEVICE_INDEX].get('port'), baudrate=128000, timeout=0.1)

    # Update MilliKey Button -> Key mappings
    print("Updating button %d mapping to use key '%s'" % (BUTTON_ID, KEY_NAME))
    cmd_str = "SET B2K %d %s\n" % (BUTTON_ID, KEY_NAME)
    sport.write(cmd_str.encode())
    r = sport.readline()
    print(r)

    if SAVE_CHANGES:
        # Save button mapping change to eeprom
        sport.write(b"SAVE_CONFIG\n")
        r = sport.readline()
        print(r)

    sport.close()