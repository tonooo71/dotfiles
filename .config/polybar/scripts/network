#!/bin/bash

nw_ssid=$(nmcli c | sed -n 2P | awk '{print $1}')
nw_type=$(nmcli c | sed -n 2P | awk '{print $(NF-1)}')
nw_info=$(nmcli c | sed -n 2P | awk '{print $NF}')

if [ $nw_info != "--" ]; then
    if [ $nw_type = ethernet ]; then
        echo ""
    elif [ $nw_type = wifi ]; then
        QUALITY=$(grep $nw_info /proc/net/wireless | awk '{ print int($3 * 100 / 70) }')
        echo " $nw_ssid"
    fi
else
    [ $(nmcli r wifi) = "disabled" ] && nmcli r wifi on
    echo "%{F#e06c75}"
fi

