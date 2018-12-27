from tornado import web
import tornado
import time


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world")


class PeopleIdHandle(web.RequestHandler):
    # 传入初始值
    def initialize(self, name):
        self.db_name = name

    async def get(self, id, *args, **kwargs):
        self.redirect(self.reverse_url('people_name', 'jeff'))


class PeopleNameHandle(web.RequestHandler):
    async def get(self, name, *args, **kwargs):
        self.write('user name {}'.format(name))


class PeopleInfoHandle(web.RequestHandler):
    async def get(self, name, id, gender, *args, **kwargs):
        self.write('user name {}, id {}, gender {}'.format(name, id, gender))


people_db = {
    'name': 'people'
}

urls = [
    tornado.web.URLSpec('/', MainHandler, name='index'),
    tornado.web.URLSpec('/people/(\d+)/?', PeopleIdHandle, people_db, name='people_id'),
    tornado.web.URLSpec('/people/(\w+)/?', PeopleNameHandle, name='people_name'),
    tornado.web.URLSpec('/people/(?P<name>\w+)/(?P<id>\d+)/(?P<gender>\w+)/?', PeopleInfoHandle, name='people_info'),

]

if __name__ == '__main__':
    app = web.Application(urls, debug=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
