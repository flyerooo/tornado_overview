from tornado import web
import tornado
from tornado.options import define, options, parse_command_line


# 定义一些可以在命令行中传递的参数以及类型
define('port', default=8008, help='run on the given port', type=int)
define('debug', default=True, help='set tornado debug model', type=bool)

# 从命令行或配置文件中获取参数
# options.parse_command_line()
options.parse_config_file('conf.cfg')

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
    app = web.Application(urls, debug=options)

    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
