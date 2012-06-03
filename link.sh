#!/bin/bash
#link.sh file
dropbox="/home/maplebeats/Dropbox/Public"
file=$1

clink(){
    link="http://dropbox.maplebeats.com/u/21529715/$file"
    echo $link |xsel
    echo "the link is: $link"
}
creat(){
    cp $file $dropbox
    echo "sucess"
}
if [ -f $dropbox/$file ] ;then
    echo "file already exists"
    clink
else
    creat
    clink
fi
