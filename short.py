import tornado.ioloop
import tornado.web
import hashlib
import shelve

class ShortHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
<html>
<body>
<form action="/short" method="post">
  <p>url:<input type="text" name="url" /></p>
  <input type="submit" value="Submit" />
</form>
</body>
</html>
""")
    def post(self):
        url=self.get_argument('url')
        m = hashlib.md5()
        m.update(url)
        hashkey = m.hexdigest()[0:6]
        db = shelve.open("data")
        db[hashkey] = url
        db.close()
        self.write("""
<html>
<body>
    <a href="/s?h=%s">here</a>
</form>
</body>
</html>
"""%(hashkey))
        
class JumpHandler(tornado.web.RequestHandler):
    def get(self):
        h=self.get_argument('h')        
        db = shelve.open("data")
        url = db[h]
        db.close()
        if url[0:7]!="http://":
            url = "http://" + url
        self.redirect(url)
        

application = tornado.web.Application([
    (r"/short", ShortHandler),
    (r"/s",JumpHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
