#!/bin/bash

volume=$(pamixer --get-volume)
mute=$(pamixer --get-mute)

if [ $mute = "true" ]; then
    echo "%{F#e06c75} "
else
    if [ $volume -eq 0 ]; then
        echo " ${volume}%"
    elif [ $volume -lt 30 ]; then
        echo " ${volume}%"
    elif [ $volume -lt 70 ]; then
        echo " ${volume}%"
    else
        echo "%{F#e5c07b} ${volume}%"
    fi
fi
