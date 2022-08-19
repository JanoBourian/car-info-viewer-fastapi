from connection.models import Sold
from connection.databases import database
from schemas.sold import SoldIn, SoldOut

## Return all items
async def get_all_items():
    query = Sold.select()
    return await database.fetch_all(query)


## Return one item by id
async def get_item(id: int):
    query = Sold.select().where(Sold.c.id == id)
    return await database.fetch_one(query)


## Search item by name
async def get_item_by_name(name: str):
    query = Sold.select().where(Sold.c.name == name)
    return await database.fetch_one(query)


## Add one item
async def add_item(data: SoldIn):
    query = Sold.insert().values(**data.dict())
    id_ = await database.execute(query)
    return await get_item(id_)


## Update one item
async def update_item(id: int, data: SoldIn):
    query = Sold.update().where(Sold.c.id == id).values(**data.dict())
    await database.execute(query)
    return await get_item(id)


## Delete one item
async def delete_item(id: int):
    query = Sold.delete().where(Sold.c.id == id)
    await database.execute(query)
