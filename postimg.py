#!/usr/bin/env python3
import fileinput,re
img = re.compile(r'<a href=.*(<img src(.*)width=)\"(.{3})\" height=\"(.{3})\".*></a>')
for line in fileinput.input(inplace=1):
        line = line.rstrip()
        test = re.search(img,line)
        if test:
                if test.group(3) > test.group(4):
                        print(re.sub(img,r'\1"400">',line))
                else:
                        print(re.sub(img,r'\1"650">',line))
        else:
                print(line)
