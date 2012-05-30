#!/bin/bash
LANG=zh
dir=~/works/maplebeats.github.com/_posts
cd $dir
temp=/tmp/post.$$
editor=gedit

echo "input file name"
read name_file
echo "input title"
read post_title
echo "---
layout: post
title: $post_title
---
" > `date +%F-$name_file.textile`
$editor `date +%F-$name_file.textile`

echo "Are you sure to push to github?(N)"
read ans
echo "p(date). Posted on `date +%c` by \"maplebeats\":http://maplebeats.com/me" >> `date +%F-$name_file.textile`
case "$ans" in 
	n* | N* )
		exit 0
		;;
	*)
		git add `date +%F-$name_file.textile`
		git commit -a -m "`date` $post_title"
		git push
		;;
esac
exit 0
