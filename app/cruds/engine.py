from fastapi import Request, HTTPException
from connection.models import Engine
from connection.databases import database
from schemas.engine import EngineIn, EngineOut

## Return all items
async def get_all_items():
    query = Engine.select()
    return await database.fetch_all(query)

## Return one item by id
async def get_item(id:int):
    query = Engine.select().where(Engine.c.id == id)
    return await database.fetch_one(query)

## Search item by name
async def get_item_by_name(name:str):
    query = Engine.select().where(Engine.c.name == name)
    return await database.fetch_one(query)

## Add one item 
async def add_item(data:EngineIn):
    query = Engine.insert().values(**data.dict())
    id_ = await database.execute(query)
    created_value = await get_item(id_)
    return created_value

## Update one item
async def update_item(id:int, data:EngineIn):
    query = Engine.update().where(Engine.c.id == id).values(**data.dict())
    await database.execute(query)
    return await get_item(id)

## Delete one item 
async def delete_item(id:int):
    query = Engine.delete().where(Engine.c.id == id)
    await database.execute(query)