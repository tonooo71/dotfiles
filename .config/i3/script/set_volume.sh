#!/bin/bash

volume=$(pamixer --get-volume)
mute=$(pamixer --get-mute)

if [ $1 = + ]; then
    pactl set-sink-volume @DEFAULT_SINK@ +5%
    if [ $(pamixer --get-mute) = true ]; then
        notify-send --urgency=low "Mute: $(pamixer --get-volume)%"
    else
        notify-send --urgency=low "VOL: $(pamixer --get-volume)%"
    fi
elif [ $1 = - ]; then
    pactl set-sink-volume @DEFAULT_SINK@ -5%
    if [ $(pamixer --get-mute) = true ]; then
        notify-send --urgency=low "Mute: $(pamixer --get-volume)%"
    else
        notify-send --urgency=low "VOL: $(pamixer --get-volume)%"
    fi
elif [ $1 = mute ]; then
    pactl set-sink-mute @DEFAULT_SINK@ toggle
    if [ $(pamixer --get-mute) = true ]; then
        notify-send --urgency=low "Mute"
    else
        notify-send --urgency=low "VOL: $(pamixer --get-volume)%"
    fi
fi
