﻿#!/usr/bin/env python3
'''
creat new post to my blog
'''
import time,os,sys
import re
import platform

format = ".textile"
if platform.system()=='Linux':
    editor = "leafpad"
    dir = "/home/maplebeats/Works/maplebeats.github.com/_posts/"
    tmpfile = "/tmp/post"
    gitdir = "/home/maplebeats/Works/maplebeats.github.com/"
else:
    editor = 'notepad'
    dir = 'c:\\'
    tmpfile = 'c:\\post'
    
class Lable:
    
    def __init__(self,filetitle,posttitle,summary):
        self.filetitle = filetitle
        self.posttile = posttitle
        self.summary = summary
        
    def filename(self):
        filetime = time.localtime()
        return '%s-%s-%s-'%filetime[:3] + self.filetitle + format
        
    def filehead(self):
        head = "---\nlayout: post\ntitle: %s\nsummary: %s\n---"%(self.posttile,self.summary)
        return head
        
    def fileend(self):
        posttime = time.asctime()
        return 'p(date). Posted on %s by "maplebeats":http://maplebeats.com/me'%posttime
        
class Post:
 
    def edit(self):
        with open('%s'%tmpfile,'w') as f:
            f.write('')
        os.system(r'%s %s'%(editor,tmpfile))
        summary = open('%s'%tmpfile,'r').readline().rstrip().replace('"',"'") #ensure json
        content = open('%s'%tmpfile,'r').readlines()
        content.pop(0)
        content = ''.join(content)
        return summary,content
        
class Transition:
       
    def postimg(self,content):
        img = re.compile(r'<a href=.*(<img src(.*)width=)\"(.{3})\" height=\"(.{3})\".*></a>')
        test = re.search(img,content)
        try:
            if test and test.group(3) > '300':
                if test.group(3) > test.group(4):
                     content = img.sub(r'\1"400">',content)
                else:
                    content = img.sub(r'\1"650">',content)
            return content
        except:    
            return content
        
    def code(self):
        co = re.compile(r'\[code\](.*)\[\\code\]')
        pass
        
class push:

    def __init__(self,filename,title):
        self.filename = filename
        self.title = title
        self.view()
        self.push()
    
    def push(self): 
        if input('push?(yes/y)').lower() == ('yes' or 'y'):
            os.system(r'cd %s;git add %s;git commit -a -m "%s %s";git push'%(gitdir,self.filename,time.asctime(),self.title))
        else:
           sys.exit()

    def view(self):
        os.system(r'%s %s%s'%(editor,dir,self.filename))
           
if __name__ == "__main__":
    file_title = '-'.join(input("输入文章短链名:").split(' '))
    title = input("输入文章标题:")
    post = Post()
    summary,content = post.edit()
    lable = Lable(file_title,title,summary)
    if content.find('flick') != -1:
        tran = Transition()
        content = tran.postimg(content)
    with open(dir + lable.filename(),'w') as f:
        f.write('%s\n%s\n\n%s'%(lable.filehead(),content,lable.fileend()))
    p = push(lable.filename(),title)
