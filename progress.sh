#!/bin/bash
time1=`date +'%s'`
go() {
    time2=`date +'%s'`
    for ((i=0;j<=$(($time2-$time1));j+=1))
        do
            printf ">"
        done
}
while :
do
    go
    sleep 1
done
