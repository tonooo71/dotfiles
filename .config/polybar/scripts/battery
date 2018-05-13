#!/bin/bash

info=$(acpi -b | sed -e "s/Battery 0: //" -e "s/,//g")
status=$(echo $info | awk '{print $1}')
percent=$(echo $info | awk '{print $2}' | sed -e "s/%//")

text=''

if [ $status = "Discharging" ]; then
    if [ $percent -lt 25 ]; then
        if [ $percent -lt 15 ]; then
	    echo "%{F#e06c75} ${percent}%"
        else
	    echo "%{F#e5c07b} ${percent}%"
	fi
    elif [ $percent -lt 50 ]; then
        echo " ${percent}%"
    elif [ $percent -lt 75 ]; then
        echo " ${percent}%"
    else
        echo " ${percent}%"
    fi
else
    if [ $percent -gt 89 ]; then
        echo "%{F#98c379} ${percent}%"
    else
        echo " ${percent}%"
    fi
fi
