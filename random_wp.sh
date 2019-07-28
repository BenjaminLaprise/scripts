#!/usr/bin/env bash

image_directory="$HOME/Images/wallpapers"

wallpaper=$(ls $image_directory | sort -R | head -n 1)

nitrogen --set-scaled --head=$1 $image_directory/$wallpaper
