#!/bin/bash

mem_used=$(free -m | sed -n 2P | awk '{print $3}')
mem_used_2=$(echo "scale=1; $mem_used / 1024" | bc)

if [ ${mem_used_2::1} = "." ]; then
    echo " 0${mem_used_2}GB"
else
    echo " ${mem_used_2}GB"
fi
