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

addlan(){
    route add -net 172.0.0.0 netmask 255.0.0.0 gw 172.18.116.1
    route add -net 202.202.0.0 netmask 255.255.0.0 gw 172.18.116.1
}

wifigw(){
    route -n |grep -Eo '125\.[0-9]+\.[0-9]+\.[0-1]'|sed 's/0$/1/g'|sort -u
}

wifi=`wifigw`
route add default gw $wifi
route del default lan0
addlan
