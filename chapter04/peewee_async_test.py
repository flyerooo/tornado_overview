import asyncio
import peewee
import peewee_async

from chapter04.models.model import Goods
from chapter04.models.model import objects


async def handler():
    await objects.create(Goods, supplier_id=7,
                         name='贵州茅台酒厂（集团）保健酒业有限公司生产，是以“龙”字打头的酒水。中国龙文化上下8000年，源远而流长，龙的形象是一种符号、一种意绪、一种血肉相联的情感。',
                         click_num=20, goods_num=1000, price=200,brief='贵州茅台')
    goods = await objects.execute(Goods.select())
    for good in goods:
        print(good.name)


loop = asyncio.get_event_loop()
loop.run_until_complete(handler())
# loop.close()
