#!/usr/bin/python3
import re,os,sys
colon = re.compile(r'\:')
for name in sys.argv[1:]:
        change = re.sub(colon,'',name)
        os.system("mv '%s' '%s'" % (name,change))
