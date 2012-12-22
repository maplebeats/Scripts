#!/bin/bash
#解压:)

ex () {
    bname=$(basename "$1")
    name=${bname%%.*}

    [ -d "$name" ] && echo "已经解压过了$name" && exit 0

    mkdir "$name" && cd "$name"
    
    trap 'rm -rf ../$name' INT QUIT

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
            unrar x ../"$1"
            ;;
        *.zip | *.7z)
            unzip ../"$1"
            ;;
        *)
            echo "呃，不支持"
            ;;
    esac

    trap - INT QUIT
}

for i in $@
do
    if [ -f "$i" ] ;then
        ex $i
    else
        echo "$i文件不存在" && break
    fi
done
