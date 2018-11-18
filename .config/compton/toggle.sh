#!/bin/bash

if [[ $(pgrep compton) == "" ]]; then
	echo "on"
	compton -b --config $HOME/.config/compton/compton.conf
else
	echo "off"
	pkill compton &
fi

