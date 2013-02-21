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
        return wubi.findall(r)

if len(sys.argv) < 2:
    raise TypeError("参数过少")
for i in sys.argv[1:]:
    for j in i:
        w = fetch(j)
        print("\x1B[1;45m{0}:\n{1}\n{2}\n{3}\n{4}\x1B[0m".format(j, w[4],w[9], w[10], w[12]))
