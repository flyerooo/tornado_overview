from tornado.web import RequestHandler
from tornado import web
import tornado


class MainHandler(RequestHandler):
    # def initialize(self, db):
    #     self.db = db

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        data1 = self.get_query_argument('name')
        data2 = self.get_query_arguments('name')
        pass



urls = [
    tornado.web.URLSpec('/', MainHandler, name='index'),

]

if __name__ == '__main__':
    app = web.Application(urls, debug=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()