# May need to automate the following and add to bootup process.
# the remote_id is an identifier for which button box we will modify
# the key mapping of.  Can using xinput to list devices, but we do have
# 2 button boxes.  Not sure if the remote_id is stable across reboots, so
# that we can reliably hardcode it here.
#remote_id=$(
#    xinput list |
#    sed -n 's/.*GASIA.*id=\([0-9]*\).*keyboard.*/\1/p'
#)
remote_id=9
[ "$remote_id" ] || exit

# remap the following keys, only for one of the millikey
# button boxes
# key AE01 -> 2

mkdir -p /tmp/xkb/symbols
# This is a name for the file, it could be anything you
# want. For us, we'll name it "custom". This is important
# later.
#
# The KP_* come from /usr/include/X11/keysymdef.h
# Also note the name, "remote" is there in the stanza
# definition.
cat >/tmp/xkb/symbols/custom <<\EOF

xkb_symbols "remote" {
    key <AE01>  { [ 2, at ] };
};
EOF

# (1) We list our current definition
# (2) Modify it to have a keyboard mapping using the name
#     we used above, in this case it's the "remote" definition
#     described in the file named "custom" which we specify in
#     this world as "custom(remote)".
# (3) Now we take that as input back into our definition of the
#     keyboard. This includes the file we just made, read in last,
#     so as to override any prior definitions.  Importantly we 
#     need to include the directory of the place we placed the file
#     to be considered when reading things in.
#
# Also notice that we aren't including exactly the 
# directory we specified above. In this case, it will be looking
# for a directory structure similar to /usr/share/X11/xkb
# 
# What we provided was a "symbols" file. That's why above we put
# the file into a "symbols" directory, which is not being included
# below.
setxkbmap -device $remote_id -print \
 | sed 's/\(xkb_symbols.*\)"/\1+custom(remote)"/' \
 | xkbcomp -I/tmp/xkb -i $remote_id -synch - $DISPLAY 2>/dev/null
