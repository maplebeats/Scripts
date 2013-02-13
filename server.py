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

def run(handler=MyHTTPhandler, server=HTTPServer, port=8000):

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
