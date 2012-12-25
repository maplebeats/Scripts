#!/bin/bash
#绑定脚本到到meta+d

speakdir="/home/maplebeats/Documents/dir"
words=$(xsel -p)
icon='/usr/share/icons/gnome/24x24/apps/zen-icon.png' 
for w in $words
do  
    declare -l w #lower
    tran=`sdcv -n --utf8-output "$w"`
    notify-send -a 'dict' -i $icon "$w" "${tran:0:300}"
    mplayer "$speakdir"/z_"$w"__gb_1.wav
done
