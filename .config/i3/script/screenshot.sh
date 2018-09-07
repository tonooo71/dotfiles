#!/bin/bash

mkdir -p ~/Pictures/Screenshot
import -window root ~/Pictures/Screenshot/screenshot`date "+%y%m%d%H%M"`.jpg
notify-send "Screenshot has been saved"
