#!/usr/bin/env python
import os,time

def creatfile():
	time_format = "%Y-%m-%d-"
	time_file = time.strftime(time_format, time.localtime())
	title_file = raw_input("link title:")
	file_name = time_file + title_file + '.textile'
	d_file = "/home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name
	print time_file + title_file
	f = file(d_file,'w')
	return d_file

def writefile(d_file):
	post_title = raw_input("title:")
	f = open(d_file,'w')
	f.write('---\nlayout: post\ntitle: ' + post_title + '\n---\n')
	f.close()
	os.system("gedit %s" % d_file)
	f = open(d_file,'a')
	f.write('<p class=date>Posted on %s by \"maplebeats\":http://maplebeats.com/me</p>' %
			time.asctime())
	f.close()

def pushfile():
	qus = raw_input("are you sure to push to github?")
	ans = ['Y','y','Yes','yes']
	if qus in ans:
		os.system("cd ~/works/maplebeats.github.com/ && git add . && git commit -a -m 'new post' && git push")
	else:
		pass

writefile(creatfile())
pushfile()


