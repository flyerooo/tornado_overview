from tornado.web import StaticFileHandler, RedirectHandler
from tornado import web, template
import tornado


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        word = "hello word aa"
        self.render('hello.html', word=word)


class MainHandler2(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world")


urls = [
    ('/', MainHandler),
    ('/2/', RedirectHandler, {'url':'/'}),
    ('/image/(.*)', StaticFileHandler, {'path':'./static'}),

]

settings = {
    'static_path':'./static',
    # 'static_url_prefix':'/static/'
    'template_path':'templates'
}

if __name__ == '__main__':
    app = web.Application(urls, debug=True, **settings)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
