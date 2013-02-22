#!/usr/bin/env python3

from urllib import request
import re
import sys

du = 'http://dict.baidu.com/s?wd='
wubi = re.compile(r'<p>(.{2,6}?: .*?)</p>')

def fetch(w):
    url = du + request.quote(w) 
    with request.urlopen(url) as r:
        r = r.read().decode('utf-8')
        d = wubi.findall(r)
    w = {k:v for k,v in (i.split(': ') for i in d )}
    return w

if len(sys.argv) < 2:
    raise TypeError("参数过少")
for i in sys.argv[1:]:
    for j in i:
        w = fetch(j)
        w.update({'字':j})
        print("""\x1B[1;45m{字}:
五笔码:{五笔98}
分解:{汉字首尾分解}
笔顺:{笔顺读写}\x1B[0m""".format(**w))
