#!/bin/bash
#txt码表 to fcitx txt码表
#其实这脚本的意思就是 awk '{ for(i=2;i<NF;i++) print $1,$i) }' file
#eg.
#a 工 戈  
#to
#a 工
#a 戈

function split (){
    for w in $*
    do
        if [ $w = $1 ]
        then
            continue
        else
            echo "$1 $w"
        fi
    done
}

while read line
do
    split $line
done < $1
