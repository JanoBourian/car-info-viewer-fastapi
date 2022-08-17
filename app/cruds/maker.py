from connection.models import Maker
from connection.databases import database
from schemas.maker import MakerIn

## return all items
async def get_all_items():
    query = Maker.select()
    return await database.fetch_all(query)


## return one item filter by id
async def get_item_by_id(id: int):
    query = Maker.select().where(Maker.c.id == id)
    return await database.fetch_one(query)


## return one item filter by name
async def get_item_by_name(name: str):
    query = Maker.select().where(Maker.c.name == name)
    return await database.fetch_one(query)


## create new item
async def add_item(data: MakerIn):
    query = Maker.insert().values(**data.dict())
    id_ = await database.execute(query)
    return await get_item_by_id(id_)


## update item by id
async def update_item(id: int, data: MakerIn):
    query = Maker.update().where(Maker.c.id == id).values(**data.dict())
    await database.execute(query)
    return await get_item_by_id(id)


## Delete item
async def delete_item(id: int):
    query = Maker.delete().where(Maker.c.id == id)
    await database.execute(query)
