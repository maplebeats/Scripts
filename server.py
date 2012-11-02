#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler,HTTPServer

class MyHTTPhandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        path = self.translate_path(self.path)
        try:
            f = open(path,"rb")
        except FileNotFoundError:
            self.send_error(404, "no such file")
        self.copyfile(f, self.wfile)
        f.close()

def run(handler=MyHTTPhandler,server=HTTPServer):

    server_address = ('', 8000)
    httpd = server(server_address, handler)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("close")
        httpd.server_close()
run()
