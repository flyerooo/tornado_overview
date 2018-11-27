from tornado import httpclient
from tornado.httpclient import AsyncHTTPClient


# http_client = httpclient.HTTPClient()
# try:
#     response = http_client.fetch("http://www.baidu.com/")
#     print(response.body)
# except httpclient.HTTPError as e:
#     # HTTPError is raised for non-200 responses; the response
#     # can be found in e.response.
#     print("Error: " + str(e))
# except Exception as e:
#     # Other errors are possible, such as IOError.
#     print("Error: " + str(e))
# http_client.close()



async def f():
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch("http://www.baidu.com")
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body.decode('utf8'))


if __name__=="__main__":
    import tornado
    io_loop = tornado.ioloop.IOLoop.current()

    # run_sync 可以在运行完某个协程之后停止事件循环
    # io_loop.run_sync(f)

    import asyncio
    # asyncio.ensure_future(f)
    asyncio.get_event_loop().run_until_complete(f())