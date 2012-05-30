#/bin/bash
#link.sh file
dropbox="/home/maplebeats/Dropbox/Public/"

cp $1 $dropbox
link="http://dropbox.maplebeats.com/u/21529715/$1"
echo $link |xsel
echo $link
