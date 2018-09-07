#!/bin/bash
# rofi_launch.sh / JennyM 2016 malkalech.com

options=(
# -modi            "combi,system:$HOME/.config/i3/script/rofi_system.sh,run,ssh"
  -modi            "drun,system:$HOME/.config/rofi/rofi_system.sh,window"
#  -combi-modi      "window,drun"
  -show            "drun"
  -font            "Monospace Bold 12"
#  -width           "60"
#  -padding         "40"
#  -lines           "8"

  ##  key bindings  ##
  -kb-cancel        "Escape,Control+c"
  -kb-mode-next     "Shift+Right"
  -kb-mode-previous "Shift+Left"
)

rofi "$@" "${options[@]}"
