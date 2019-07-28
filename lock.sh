#!/usr/bin/env bash

scrot /tmp/screen_locked.png
convert /tmp/screen_locked.png -scale 10% -scale 1000% /tmp/blured_screen_locked.png
playerctl pause
~/scripts/auto_xrandr_daemon.py stop
i3lock -i /tmp/blured_screen_locked.png --ignore-empty-password -n; ~/scripts/auto_xrandr_daemon.py start
