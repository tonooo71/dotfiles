#!/bin/bash

mem_used=$(free -m | sed -n 2P | awk '{print $3}')
mem_used_2=$(echo "scale=1; $mem_used / 1024" | bc)

if [[ $1 = click ]]; then
    if [ ${mem_used_2::1} = "." ]; then
        notify-send "MEM: 0${mem_used_2}GB"
    else
        notify-send "MEM: ${mem_used_2}GB"
    fi
else
    echo ""
fi
