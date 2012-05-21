#!/usr/bin/env python3

'''
text2josn.py < text > text.json
'''
import fileinput
print("[")
for line in fileinput.input():
    line = line.rstrip()
    print('{\n"anime":"'+line+'"')
print("]")
