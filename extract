#!/bin/bash

dname=$(basename "$1")
d_name=${dname%.*}
[ -d "$d_name" ] && echo "已经解压过了" && exit 0
mkdir "$d_name" && cd "$d_name"
case $1 in 
	*.tar.bz2 | *.tbz2)
		tar xvjf ../"$1"
		;;
	*.tar.gz | *.tgz)
		tar xvzf ../"$1"
		;;
	*.tar.xz | *.txz)
		tar xvJf ../"$1"
		;;
	*.rar)
		unrar e ../$1
		;;
	*.zip | *.7z)
		unzip ../"$1"
esac

