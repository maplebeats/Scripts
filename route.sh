#!/bin/bash
#
# Author: maplebeats
#
# gtalk/mail: maplebeats@gmail.com
#
# Last modified: 2012-11-10 13:05
#
# Filename: route.sh
#
# Description: 呃
#
[[ $(id -u) != 0 ]] && echo "must root" && exit 1
addlan () {
    route add -net 172.0.0.0 netmask 255.0.0.0 gw 172.18.116.1
    route add -net 202.202.0.0 netmask 255.255.0.0 gw 172.18.116.1
}

wifigw () {
    route -n |awk '{if($8=="wlan0") if($1!="0.0.0.0") print $1}'|sed 's/.[0-255]$/.1/g'|uniq
}
route add default gw $(wifigw)
route del default lan0
addlan
