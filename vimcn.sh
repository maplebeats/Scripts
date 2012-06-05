#!/bin/bash
#vimcn.sh tager
#po code or img

ename=${1##*.}
if [ "$ename" = "png" ] || [ "$ename" = "jpg" ] ;then
    echo $1
    curl -F "name=@$1" http://img.vim-cn.com/
else
    $* | curl -F 'vimcn=<-' http://p.vim-cn.com | xsel
fi
