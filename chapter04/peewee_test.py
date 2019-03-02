from chapter04.models.model import Supplier, Goods
from chapter04.data import supplier_list, goods_list


def save_model():
    # for data in supplier_list:
    #     supplier = Supplier()
    #     supplier.name = data['name']
    #     supplier.address=data['address']
    #     supplier.phone=data['phone']
    #
    #     supplier.save()

    for data in goods_list:
        good = Goods(**data)

        good.save()


def query_model():
    # 获取一条数据
    # good = Goods.get(Goods.id==7)
    # good = Goods.get_by_id(7)
    # good = Goods[7]

    # 获取所有数据
    # select * from goods
    # goods = Goods.select(Goods.name, Goods.price).where((Goods.price>100)&(Goods.click_num>200))

    # select * from goods where name like '%like'
    goods = Goods.select().where(Goods.name.contains('飞天'))
    for good in goods:
        print(good.name, good.price, good.click_num)


def update_model():
    # update click_num=100 where id=7
    # Goods.update(click_num=110).where(Goods.id==7).execute() # execute 是阻塞的
    Goods.update(click_num=Goods.click_num+1).where(Goods.id==7).execute()


if __name__ == '__main__':
    update_model()
