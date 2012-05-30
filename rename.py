#/usr/bin/env python3
'''
rename.py name file1 file2 ...
'''
import sys,os
for (i,j) in zip(sys.argv[2:],range(len(sys.argv[2:]))):
    os.rename(i,sys.argv[1]+j+os.path.splitext(i)[1])
