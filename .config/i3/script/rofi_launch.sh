#!/bin/bash
# rofi_launch.sh / JennyM 2016 malkalech.com

options=(
  -modi            
"combi,system:$HOME/.config/i3/script/rofi_system.sh,run,ssh"
  -combi-modi      "window,drun"
  -show            "combi"
  -font            "Monospace 14"
  -width           "80"
  -padding         "80"
  -lines           "8"
  -fixed-num-lines
  -hide-scrollbar
  -sidebar-mode

  ##  key bindings  ##
  -kb-cancel        "Escape,Control+c"
  -kb-mode-next     "Shift+Right"
  -kb-mode-previous "Shift+Left"

)

rofi "$@" "${options[@]}"
