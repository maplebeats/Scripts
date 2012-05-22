#!/usr/bin/env python3

'''
text2josn.py < text > text.json
'''
import fileinput
print("[")
for line in fileinput.input():
    anime = line.rstrip().split('》')
    print('{\n"cn":"'+anime[0]+'》"\n"jp":"'+anime[1]+'"')
print("]")
