#!/usr/bin/env python3
import subprocess,time,os
from threading import Thread
class Deamon:
        
    def __init__(self):
        pass

    def clearfile(self,filename):
        size = os.path.getsize(filename)
        if size>10000:
            with open(filename,'W') as f:
                f.write('')

if __name__=='__main__':
    
