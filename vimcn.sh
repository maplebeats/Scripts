#!/bin/bash

#贴代码，贴图片！

ename=${1##*.}
if [ "$ename" = "png" ] || [ "$ename" = "jpg" ] ;then
    echo $1
    curl -F "name=@$1" http://img.vim-cn.com/ | xsel
else
    $* | curl -F 'vimcn=<-' http://p.vim-cn.com | xsel
fi
