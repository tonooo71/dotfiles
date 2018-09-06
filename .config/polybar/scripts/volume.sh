#!/bin/bash

volume=$(pamixer --get-volume)
mute=$(pamixer --get-mute)

if [[ $1 = click ]]; then
    if [ $mute = true ]; then
        notify-send "Mute: ${volume}%"
    else
        notify-send "Volume: ${volume}%"
    fi
else
    if [ $mute = true -o $volume -eq 0 ]; then
        echo "%{F#e06c75}"
    else
        if [ $volume -lt 10 ]; then
            echo ""
        elif [ $volume -lt 40 ]; then
            echo ""
        elif [ $volume -lt 70 ]; then
            echo ""
        else
            echo "%{F#e5c07b}"
        fi
    fi
fi
