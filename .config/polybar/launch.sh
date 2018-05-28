#!/bin/bash

## restart i3
if [[ $1 = "restart" ]]; then
	i3-msg restart
fi

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch bar
polybar eDP1 &
polybar HDMI1 &
polybar DP2

