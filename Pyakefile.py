#!/usr/bin/env python
import os,sys,time

def creatfile():
	time_format = "%Y-%m-%d-" #time format
	time_file = time.strftime(time_format, time.localtime())
	title_file = raw_input("title:")
	print time_file + title_file
	f = file(time_file + title_file + '.textile','w')

def writefile():
	pass

def pushfile():
	pass

creatfile()
writefile()
pushfile()

