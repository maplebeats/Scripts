#!/usr/bin/env python3
'''
link.py file
'''

import shutil,sys 
dropbox = "/home/maplebeats/Dropbox/Public/"

def link(f):
    shutil.copyfile(f,dropbox+f)
    print("http://dropbox.maplebeats.com/u/21529715/"+f)

if __name__ == '__main__':
    link(sys.argv[1])
    
