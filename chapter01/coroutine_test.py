from tornado.gen import coroutine

async def yield_test():
    yield 1
    yield 2
    yield 3

async def main():
    result = await yield_test()


my_yield = yield_test()
for item in my_yield:
    print(my_yield)