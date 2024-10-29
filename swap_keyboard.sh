#!/usr/bin/env bash

# Get current keyboard layout
layout=$(setxkbmap -query | grep layout | awk '{print $2}')

# If current layout is us, switch to french canadien, else switch to us
if [ $layout == "us" ]; then
    setxkbmap ca
else
    setxkbmap us
fi
layout=$(setxkbmap -query | grep layout | awk '{print $2}')
echo $layout > $HOME/.config/i3status/keyboard_layout
