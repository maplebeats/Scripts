#!/usr/bin/python3
'''
when the name has colon,then remove it
RmColon.py file
'''
import re,os,sys
colon = re.compile(r'\:')
for name in sys.argv[1:]:
        if re.search(colon,name):
            change = re.sub(colon,'',name)
            os.rename(name,change)
