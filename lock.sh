#!/usr/bin/env bash

scrot /tmp/screen_locked.png
convert /tmp/screen_locked.png -scale 10% -scale 1000% /tmp/screen_locked2.png
xdotool mousemove 0 0 && xdotool mousemove 100 100
playerctl pause
./auto_xrandr_daemon.py stop
i3lock -i /tmp/screen_locked2.png --ignore-empty-password -n;
./auto_xrandr_daemon.py start
