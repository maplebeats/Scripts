#!/usr/bin/env python3

'''
text2josn.py < text > text.json
'''
import fileinput
f = fileinput.input()
for l in f:
    pass
print("[")
for line in fileinput.input():
    anime = line.rstrip().split('》')
    print('{\n"cn":"'+anime[0]+'》",\n"jp":"'+anime[1]+'"')
    if f.filelineno() == fileinput.lineno():
        print("}")
    else:
        print("},")
print("]")
