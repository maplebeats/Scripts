#!/usr/bin/env python3
import fileinput,re
tab = re.compile(r'	')
for line in fileinput.input(inplace=1):
        line = line.rstrip()
        space = re.sub(tab,r'    ',line)
        print(space)
