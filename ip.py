#/usr/bin/env python3
import urllib.request as ur
import re,time
def getip():
    fp =ur.urlopen("http://icanhazip.com")
    ip = re.compile(r'[\d\.]*')
    return ip.findall(fp.read().decode("utf8"))[0]
temp = getip()
while True:
    myip = getip()
    if myip != temp:
        print(myip) #do
        temp = getip()
    print(myip)
