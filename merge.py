#!/usr/bin/env python3
import os
def check(walk):
    for i in walk:
        for j in i[2]:
            if j.find('.py') != -1:
                code = open(i[0]+'/'+j).read()
                print("<h1>%s</h1>\n<h2>%s</h2>\n<code>%s</code>"%(j,i[0],code),file=log)
with open('merge.html','w') as log:
    files = os.walk(r'./')
    check(files)

