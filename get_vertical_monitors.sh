#!/usr/bin/env bash

xrandr --listmonitors | grep " 1080" | cut -c 2 | xargs
