#!/bin/bash

updates_pacman=$(checkupdates | wc -l)
#updates_yaourt=$(yaourt -Qua | wc -l)

if [[ $updates_pacman -eq 0 ]]; then
	echo " 0"
else
	echo "%{F#e5c07b} $updates_pacman"
fi
