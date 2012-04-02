#!/usr/bin/env python3
import fileinput,re
img = re.compile(r'<a href=(.*)(<img src(.*)width=).*></a>')
for line in fileinput.input(inplace=1):
        line = line.rstrip()
        image = re.findall
        if re.search(img,line):
                print(re.sub(img,r'\2"650">',line))
        else:
                print(line)
