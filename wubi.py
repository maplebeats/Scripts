#!/usr/bin/env python3

from urllib import request
import re
import sys

du = 'http://dict.baidu.com/s?wd='
wubi = re.compile(r'<p>五笔(?:86|98): ([a-y]{1,4})</p>')

def fetch(w):
    url = du + request.quote(w) 
    with request.urlopen(url) as r:
        r = r.read().decode('utf-8')
        return wubi.findall(r)

for i in sys.argv[1:]:
    w = fetch(i)
    print("86版五笔:{0}\n98版五笔:{1}\n\n".format(*w))
