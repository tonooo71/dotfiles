#!/bin/bash

info=$(acpi -b | sed -e "s/Battery 0: //" -e "s/,//g")
status=$(echo $info | awk '{print $1}')
percent=$(echo $info | awk '{print $2}' | sed -e "s/%//")
lefttime=$(echo $info | awk '{print $3}' | rev | cut -c 4- | rev)

if [[ $1 = click ]]; then
    notify-send "BAT: ${percent}%($lefttime)"
else
    if [ $status = "Discharging" ]; then
        if [ $percent -lt 25 ]; then
            if [ $percent -lt 15 ]; then
                echo "%{F#e06c75}"
            else
                echo "%{F#e5c07b}"
            fi
        elif [ $percent -lt 50 ]; then
            echo ""
        elif [ $percent -lt 75 ]; then
            echo ""
        else
            echo ""
        fi
    else
        if [ $percent -gt 89 ]; then
            echo "%{F#98c379}"
        else
            echo ""
        fi
    fi
fi
