#!/bin/bash
#update my configure at github

cdir='/home/maplebeats/Works/configuration/'

update() {
    cp ~/.zshrc $cdir
    cp ~/.vimrc $cdir
}

push() {
    cd $cdir
    git commit -a -m "update config `date`"
    git push
}

update
push

exit 0
