#!/usr/bin/env sh

set -u

topic=$1

shift

curl cht.sh/$topic/$(echo $@ | sed "s/ /+/g")
