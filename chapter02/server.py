from tornado import web
import tornado
import time


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world zz")


urls = [
    ('/', MainHandler),

]

if __name__ == '__main__':
    app = web.Application(urls, debug=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
