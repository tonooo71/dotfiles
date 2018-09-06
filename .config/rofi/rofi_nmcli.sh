#!/bin/bash

# input
if [ -z "$@" ]; then
    for ssid in `nmcli c show | grep 'wifi' | awk '{print $1}'`; do
        nmcli d wifi | grep $ssid
    done
else
    ssid=`echo $@ | awk '{print $1}'` 
    [ $ssid != '*' ] && command=`nmcli c up $ssid`
fi
eval "${command:-:}"
