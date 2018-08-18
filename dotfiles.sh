#!/bin/bash

pacman -Q > ~/.config/packagelist/pacman.list
pip list > ~/.config/packagelist/pip.list

git add .
msg="`date`"
if [ $# -eq 1 ]
    then msg="$1"
fi
git commit -m "$msg"
git push origin master

