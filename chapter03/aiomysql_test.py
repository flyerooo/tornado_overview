import asyncio
import aiomysql


# async def test_example(loop):
async def test_example():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='p2pdev',
                                      db='message', charset='utf8mb4')
                                      # db='message', loop=loop, charset='utf8mb4')
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * from message;")
            value = await cur.fetchone()
            print(value)
    # pool.close()
    # await pool.wait_closed()

#
# if __name__ == '__main__':
#     from tornado import ioloop
#     # loop = asyncio.get_event_loop()
#     loop = ioloop.IOLoop.current()
#     # loop.run_until_complete(test_example(loop))
#     loop.run_sync(test_example)

def simple_corountine():
    print('-> coroutine started ')
    x = yield
    print('-> coroutine received:', x)
