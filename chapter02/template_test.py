from tornado.web import StaticFileHandler, RedirectHandler
from tornado import web, template
import tornado


class MainHandler(web.RequestHandler):
    def cal_total(self, price, nums):
        return price * nums

    async def get(self, *args, **kwargs):
        orders = [
            {
                'name': '小米T恤 忍者米兔双截棍 军绿 XXL',
                'image': 'http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg',
                'price': 39,
                'nums': 3,
            },
            {
                'name': '招财猫米兔 白色',
                'image': 'http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg',
                'price': 40,
                'nums': 2,
            },
            {
                'name': '小米圆领纯色T恤 男款 红色 XXL',
                'image': 'http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg',
                'price': 41,
                'nums': 2,
            }
        ]
        self.render('index.html', orders= orders)
        # self.render('index.html', orders= orders, cal_total= self.cal_total)


class MainHandler2(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world")


urls = [
    ('/', MainHandler),
    ('/2/', RedirectHandler, {'url': '/'}),
    ('/image/(.*)', StaticFileHandler, {'path': './static'}),

]

settings = {
    'static_path': './static',
    'static_url_prefix': '/static/',
    'template_path': 'templates',
}

if __name__ == '__main__':
    app = web.Application(urls, debug=True, **settings)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
