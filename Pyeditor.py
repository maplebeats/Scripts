#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,wx,sys

def savefile(event):
	time_format = "%Y-%m-%d-"
	time_file = time.strftime(time_format, time.localtime())
	file_name = time_file + linktitle.GetValue() + '.textile'
	d_file = "/home/maplebeats/works/maplebeats.github.com/_posts/%s" % file_name
	f = open(d_file,'w')
	f.write('---\nlayout: post\ntitle: ' + titlefile.GetValue().encode('utf8') + '\n---\n' +
			contents.GetValue().encode('utf8'))
	f.close()
	f = open(d_file,'a')
	f.write('\n<p class=date>Posted on %s by \"maplebeats\":http://maplebeats.com/me</p>' %
			time.asctime())
	f.close()

def pushfile(event):
	os.system("cd ~/works/maplebeats.github.com/ && git add . && git commit -a -m 'New post on %s' && git push"
			% time.asctime)

app = wx.App()
win = wx.Frame(None,title="Pyakefile Editor",size=(800,500))

bkg = wx.Panel(win)

saveButton = wx.Button(bkg,label='Save')
saveButton.Bind(wx.EVT_BUTTON,savefile)
pushButton = wx.Button(bkg,label='push')
pushButton.Bind(wx.EVT_BUTTON,pushfile)

linktitle = wx.TextCtrl(bkg)
titlefile = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

tbox = wx.BoxSizer()
tbox.Add(linktitle,proportion=3,flag=wx.EXPAND)
tbox.Add(saveButton,proportion=1,flag=wx.LEFT,border=5)

hbox = wx.BoxSizer()
hbox.Add(titlefile,proportion=3,flag=wx.EXPAND)
hbox.Add(pushButton,proportion=1,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(tbox,proportion=0,flag=wx.LEFT,border=5)
vbox.Add(hbox,proportion=0,flag=wx.LEFT,border=5)
vbox.Add(contents,proportion=1,
		flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()

