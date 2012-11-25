#!/bin/bash
#pidgin-lwqq查看最近的记录

logdir="/home/maplebeats/.purple/logs/webqq/503979672/"
if [ "$#" == 0 ];then
    ctime=0
else
    ctime=$1
fi

find "$logdir" -ctime "$ctime" -type f -exec sed -e "s/.*<b>\(.*\)<\/b>.*;'>\(.*\)<\/span><br\/>/\1\2/g" -e "s/<html>.*<\/h3>/~~~~~~~~~~~~~~~~/g" {} \;
