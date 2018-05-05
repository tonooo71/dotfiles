#!/bin/bash

if [ $# -eq 3 ]; then
    status=$(i3-msg "[class=\"$1\"] focus")
    if [ $status != [{\"success\":true}] ]; then
        i3-msg workspace "$3"
        i3-msg exec "$2"
    fi
fi
