#!/bin/bash
if [ $(xrandr | grep "*" | wc -l) -eq 2 ]; then
    xrandr --output DP-4 --auto --output HDMI-0 --off
else
    xrandr --output DP-4 --auto --output HDMI-0 --auto --right-of DP-4
fi
~/.fehbg
~/.config/polybar/launch.sh restart
