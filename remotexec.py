#!/usr/bin/env python
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import io
import subprocess
import time
import shutil
import fcntl

class MyHTTPhandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.doHandler()

    def do_GET(self):
        self.doHandler()

    def doHandler(self):
        self.gen_conf()
        if self.exe() == 0:
            self.send_response(200)
            self.send_header("Content-Length", '')
            self.end_headers()
            f = io.BytesIO()
            f.write('')
            f.seek(0)
            self.copyfile(f ,self.wfile)

    def backup(self):
        tag = time.strftime("%Y%m%d%H%M%S", time.localtime())
        shutil.copy("nginx.conf","nginx.conf.%s"% tag)

    def gen_conf(self):
        self.backup()
        domains = ['test.com', 'map.com']
        rss = [("127.0.0.1",998),("127.0.0.2",666)]
        conf = ""
        for domain in domains:
            rs_conf = ""
            for rs,port in rss:
               rs_conf+="        proxy_pass http://%s:%s;\n" %(rs,str(port))

            conf +="""
server{
    listen 80;
    server_name %s;
    location /
    {
%s
    }
}
"""%(domain, rs_conf)

        f = open("nginx.conf",'w')
        fcntl.flock(f.fileno(), fcntl.LOCK_EX) 
        f.write(conf)
        f.close()

    def exe(self):
        r = subprocess.call(["ls", "-l"])
        return 0

def run(handler=MyHTTPhandler, server=SocketServer.TCPServer, port=8000):

    server_address = ('', port)
    httpd = server(server_address, handler)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("close")
        httpd.server_close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
        if(port > 1000):
            run(port=port)
        else:
            raise Exception('port must be more than 1000')
    else:
        run()
