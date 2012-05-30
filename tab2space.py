#!/usr/bin/env python3
'''
replace the tabs to space
tab2space file1 file2...
tips:backup yours files
'''
import fileinput,re
tab = re.compile(r'	')
for line in fileinput.input(inplace=1):
        line = line.rstrip()
        if re.search(tab,line):
                space = re.sub(tab,r'    ',line)
                print(space)
        else:
                print(line)
