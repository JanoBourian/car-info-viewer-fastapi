from connection.models import Engine
from connection.databases import database

## Return all items
async def get_all_items():
    query = Engine.select()
    return await database.fetch_all(query)

## Return one item by id
async def get_item(id:int):
    query = Engine.select().where(Engine.c.id == id)
    return await database.fetch_one(query)

## Add one item 

## Modify one item

## Delete one item 

