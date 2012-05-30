#/usr/bin/env python3
import sys,os
for (i,j) in zip(sys.argv[2:],range(len(sys.argv[2:]))):
    os.system(r'mv "%s" "%s%s%s"'%(i,sys.argv[1],j,os.path.splitext(i)[1]))
