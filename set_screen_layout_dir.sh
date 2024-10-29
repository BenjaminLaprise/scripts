#!/usr/bin/env bash

screen_layout_dir="$HOME/.screenlayout"

current_screens_hash=$(xrandr --verbose | md5sum | awk '{print $1}')

if [ ! -f "$screen_layout_dir/$current_screens_hash.sh" ]; then
    touch "$screen_layout_dir/$current_screens_hash.sh"
    echo "#!/bin/sh" > "$screen_layout_dir/$current_screens_hash.sh"
fi

ln -sf "$screen_layout_dir/$current_screens_hash.sh" "$screen_layout_dir/current.sh"
echo "Linked $current_screens_hash.sh to current.sh"
