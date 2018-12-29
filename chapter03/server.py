from tornado.web import StaticFileHandler, RedirectHandler
from tornado import web, template
import tornado
import aiomysql


class MainHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db

    async def get(self, *args, **kwargs):
        id = ''
        name = ''
        email = ''
        address = ''
        message = ''
        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset='utf8mb4')
        # db='message', loop=loop, charset='utf8mb4')
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT id, name, email, address, message from message;")
                try:
                    id, name, email, address, message = await cur.fetchone()
                except Exception as e:
                    pass
        self.render('message.html', id=id, name=name, email=email, address=address, message=message)

    async def post(self, *args, **kwargs):
        id = self.get_body_argument('id', '')
        name = self.get_body_argument('name', '')
        email = self.get_body_argument('email', '')
        address = self.get_body_argument('address', '')
        message = self.get_body_argument('message', '')

        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset='utf8mb4')
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO message(name, email, address, message) VALUES('{}','{}','{}','{}');".format(name,
                                                                                                             email,
                                                                                                             address,
                                                                                                             message))
                await conn.commit()
        self.render('message.html', id=id, name=name, email=email, address=address, message=message)


settings = {
    'static_path': './static',
    'static_url_prefix': '/static/',
    'template_path': 'templates',
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'name': 'message',
        'charset': 'utf8mb4'
    }
}

urls = [
    ('/', MainHandler, {'db': settings['db']}),
    ('/2/', RedirectHandler, {'url': '/'}),
    ('/image/(.*)', StaticFileHandler, {'path': './static'}),

]

if __name__ == '__main__':
    app = web.Application(urls, debug=True, **settings)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
