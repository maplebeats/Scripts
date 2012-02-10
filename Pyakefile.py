#!/usr/bin/env python
import os,time

def creatfile():
	time_format = "%Y-%m-%d-"
	time_file = time.strftime(time_format, time.localtime())
	title_file = raw_input("link title:")
	file_name = time_file + title_file + '.textile'
	print time_file + title_file
	f = file("/home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name,'w')
	return file_name

def writefile(file_name):
	post_title = raw_input("title:")
	f = open("/home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name,'w')
	f.write('---\nlayout: post\ntitle: ' + post_title + '\n---\n')
	f.close()
	os.system("gedit /home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name)
	time_format = "%Y-%m-%d %X"
	post_time = time.strftime(time_format, time.localtime())
	f = open("/home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name,'a')
	f.write('<p class=date>Posted on %s by \"maplebeats\":http://maplebeats.com/me</p>' % post_time)
	f.close()
	return file_name


def pushfile(file_name):
	pass
	os.system("cd ~/works/maplebeats.github.com/ && git add . && git commit -a -m 'new post' && git push")

pushfile(writefile(creatfile()))


