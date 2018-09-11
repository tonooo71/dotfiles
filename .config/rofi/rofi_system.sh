#!/bin/bash
# rofi_system_menu.sh / JennyM 2017 malkalech.com

list=(
  ##  Lock  ##
  "Lock Screen" "light-locker-command -l"
  ##  Power ##
  "Reboot"      "systemctl reboot"
  "Shutdown"    "systemctl poweroff"
  "Suspend"     "systemctl suspend"
  "Logout"      "i3-msg exit"
)

for (( i=1; i<=$((${#list[@]}/2)); i++ )); do
  [[ -z "$@" ]] && echo "${list[$i*2-2]}" && continue
  [[ "$@" == "${list[$i*2-2]}" ]] && command="${list[$i*2-1]}" && break
done
eval "${command:-:}"
