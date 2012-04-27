#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time,os,sys
import re
import platform

format = ".textile"
if platform.system()=='Linux':
    editor = "gedit"
    dir = "/home/maplebeats/works/maplebeats.github.com/_posts/"
    tmpfile = "/tmp/post"
    gitdir = "/home/maplebeats/works/maplebeats.github.com/"
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
        return 'p(data). Posted on %s by "maplebeats":http://maplebeats.com/me'%posttime
        
class Post:
 
    def edit(self):
        with open('%s'%tmpfile,'w') as f:
            f.write('')
        os.system(r'%s %s'%(editor,tmpfile))
        summary = open('%s'%tmpfile,'r').readline().rstrip()
        content = open('%s'%tmpfile,'r').read().rstrip()
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
        except:    
            return content
        
    def code(self):
        co = re.compile(r'\[code\](.*)\[\\code\]')
        pass
        
class push:

    def __init__(self,filename,title):
        if input('push?(yes/y)').lower() == ('yes' or 'y'):
            os.system(r'cd %s;git add %s;git commit -a -m "%s %s";git push'%(gitdir,filename,time.asctime(),title))
        else:
           sys.exit()
            
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
    push(lable.filename,title)
 
