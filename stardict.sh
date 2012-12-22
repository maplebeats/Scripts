#!/bin/bash
#绑定脚本到到meta+d

words=$(xsel -p)
icon='/usr/share/icons/gnome/24x24/apps/zen-icon.png' 
for w in $words
do
    tran=`sdcv -n --utf8-output "$w"`
    notify-send -a 'dict' -i $icon "$w" "${tran:0:300}"
done
