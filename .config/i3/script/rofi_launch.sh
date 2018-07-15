#!/bin/bash
# rofi_launch.sh / JennyM 2016 malkalech.com

alpha="cc"   # opacity (00〜FF)

options=(
# -modi            "combi,system:$HOME/.config/i3/script/rofi_system.sh,run,ssh"
  -modi            "drun,window,system:$HOME/.config/i3/script/rofi_system.sh"
#  -combi-modi      "window,drun"
  -show            "drun"
  -font            "Monospace Bold 12"
  -width           "60"
  -padding         "40"
  -lines           "8"
  -fixed-num-lines
  -hide-scrollbar
  -sidebar-mode

  ##  key bindings  ##
  -kb-cancel        "Escape,Control+c"
  -kb-mode-next     "Shift+Right"
  -kb-mode-previous "Shift+Left"

  #### color scheme
  -color-enabled   "true"
  ## window         bg                   border               separator
  -color-window    "argb:${alpha}282c34, argb:${alpha}282c34, argb:${alpha}c8ccd4"
  ## text & cursor  bg             fg                   bg (alt)       bg (highlight)       fg (highlight)
  -color-normal    "argb:00000000, argb:${alpha}c8ccd4, argb:00000000, argb:${alpha}98c379, argb:${alpha}282c34"
  -color-active    "argb:00000000, argb:${alpha}61afef, argb:00000000, argb:${alpha}61afef, argb:${alpha}282c34"
  -color-urgent    "argb:00000000, argb:${alpha}e06c75, argb:00000000, argb:${alpha}e06c75, argb:${alpha}282c34"
)

rofi "$@" "${options[@]}"
