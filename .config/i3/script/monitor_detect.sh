#!/bin/bash

#st_prev=$(cat /sys/class/drm/card0-HDMI-A-1/status)
st_prev="eDP1"
st_next=""

while :
do
    if [ $(cat /sys/class/drm/card0-HDMI-A-1/status) = "connected" ]; then
        if [ $(cat /sys/class/drm/card0-DP-2/status) = "connected" ]; then
            st_next="ALL"
        else
            st_next="HDMI1"
        fi
    else
        if [ $(cat /sys/class/drm/card0-DP-2/status) = "connected" ]; then
            st_next="DP2"
        else
            st_next="eDP1"
        fi
    fi

    if [ $st_prev != $st_next ]; then
        st_prev=$st_next
        if [ $st_next = "eDP1" ]; then
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --off --output DP2 --off
        elif [ $st_next = "HDMI1" ]; then
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --auto --above eDP1 --output DP2 --off
        elif [ $st_next = "DP2" ]; then
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --off --output DP2 --auto --above eDP1
        elif [ $st_next = "ALL" ]; then
            xrandr --output eDP1 --mode 1600x900 --output HDMI1 --auto --above eDP1 --output DP2 --auto --right-of HDMI1
        fi
        ~/.fehbg
	~/.config/polybar/launch.sh
    fi
    sleep 1
done
