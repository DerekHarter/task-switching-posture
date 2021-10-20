# Ubuntu 20.04 Bootstrap

The `bootstrap-ubuntu-20.04.sh` shell script contains the current procedure we use to set
up PsychoPy, Python and other needed packages for this experiment.  You can try running it
as is, these commands need to be run as root:

```
$ sudo ./bootstrap-ubuntu-20.04.sh
```

but you may need to run the commands by hand to check and test configuration.

# MilliKey key box configuration

The script `configure-millikey-button-box.sh` can be used to reconfigure
the key that is produced when the button is pressed on our MilliKey
button boxes.  The script is hard coded with a device remote_id, so
the correct id needs to be determined.  Our MilliKey button boxes
are configured by default to generate a `1` key on a button press.  But
we need to map one of the boxes to another key.  So in this script we
map one of the boxes to generate a `2` key.  This script may need to be
added to system bootup, to ensure that keys are mapped if machine gets
rebooted.  To run the script, as root, do the following

```
$ sudo ./configure-millikey-button-box.sh
```

Some other useful commands to check the MilliKey button box configuration

- lsusb : List all usb devices, the MilliKey button boxes should show up on the list.
- xinput list : also lists connected devices including the button box.  The id from this 
  list is the remote_id needed in the configuration script, I believe.
- setxkbmap --device 9 -print : Display keyboard mapping information about a device
- xev : Shows X events, including keyboard and mouse events.  Useful to check if configuration
  is correctly mapping key presses, though since we set the MilliKey device to generate 1
  and 2, and also simply open a terminal or editor and see if that is the key being
  generated.
