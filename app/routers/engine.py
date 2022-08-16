from fastapi import APIRouter, HTTPException
from app.cruds.engine import get_all_items, get_item, get_item_by_name, add_item, update_item, delete_item
from schemas.engine import EngineOut, EngineIn

router = APIRouter(tags = ["engineOut"], prefix = "/engine")

@router.get("/")
async def get_all_engines():
    data = await get_all_items()
    if not data:
        raise HTTPException(status_code = 404, detail = f"Nothing item was found")
    return data

@router.get("/{id}", response_model = EngineOut)
async def get_all_engines(id:int):
    data = await get_item(id)
    if not data:
        raise HTTPException(status_code = 404, detail = f"The id {id} was not found")
    return data

@router.post("/", response_model = EngineOut)
async def create_item(request:EngineIn):
    item = await get_item_by_name(request.name)
    if item:
        raise HTTPException(status_code=409, detail=f"Item {request.name} already exists")
    created_value = await add_item(request)
    return created_value

@router.patch("/{id}", response_model = EngineOut)
async def update_items(id:int, request:EngineIn):
    item = await get_item(id)
    if not item: 
        raise HTTPException(status_code=404, detail=f"Item {request.name} not exists")
    updated_item = await update_item(id, request)
    return updated_item

@router.delete("/{id}")
async def delete_items(id:int):
    item = await get_item(id)
    if not item: 
        raise HTTPException(status_code=404, detail=f"Item {id} not exists")
    delete = await delete_item(id)
    item = await get_item(id)
    if item:
        raise HTTPException(status_code=404, detail=f"Item {id} was not deleted")
    return {"message": f"Item {id} was deleted"}