#!/bin/bash

dir=~/works/maplebeats.github.com/_posts
cd $dir
temp=/tmp/post.$$
editor=vi

date +%y-%m-%d >$temp
echo $*.textile >>$temp
xargs -n10 <$temp |tee $temp
cat $temp|sed '/ \+/s//-/g' |tee $temp
touch "`cat $temp`"
#generate_filename ()
#{
#    echo -n `LANG=C date +%F`-"$1".textile
#}
#touch "`generate_filename miku`"
echo "输入文章title"
read post_title
echo "输入文章summary"
read post_summary
echo "---
layout: post
title: $post_title
summary: $post_summary
---
" >`cat $temp`
$editor `cat $temp`
exit 0
