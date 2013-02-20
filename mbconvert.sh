#!/bin/bash
#txt码表 to fcitx txt码表
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
