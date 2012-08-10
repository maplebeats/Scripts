#!/bin/bash
#
# Author: maplebeats
#
# gtalk/mail: maplebeats@gmail.com
#
# Last modified: 2012-08-09 13:53
#
# Filename: hackthunder.sh
#
# Description: 迅雷鏈接轉換
#

address=`echo $1 |sed 's/thunder\:\/\///'|base64 -d |sed -e 's/^AA//' -e 's/\/ZZ$//'`
echo $address
echo $address|xsel
