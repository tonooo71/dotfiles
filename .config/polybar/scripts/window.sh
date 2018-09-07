#!/bin/bash

windowFocus=$(xdotool getwindowfocus);
echo $(xprop -id $windowFocus | grep WM_CLASS | sed -e 's/"/ /g' | awk '{print $NF}');
