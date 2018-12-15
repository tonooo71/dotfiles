#!/bin/bash
if xrandr | grep "HDMI1 connected"; then
    if xrandr | grep "DP2 connected"; then
        if xrandr | grep "1600x900.*\*"; then
            xrandr --output eDP1 --off --output HDMI1 --auto --above eDP1 --output DP2 --auto --right-of HDMI1
        else
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --auto --above eDP1 --output DP2 --auto --right-of HDMI1
        fi
    else
        if xrandr | grep "1600x900.*\*"; then
            xrandr --output eDP1 --off --output HDMI1 --auto --above eDP1
        else
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --auto --above eDP1
        fi
    fi
fi

~/.fehbg
# compton -b --config ~/.config/compton/compton.conf
~/.config/polybar/launch.sh
