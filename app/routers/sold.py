from fastapi import APIRouter, HTTPException
from app.cruds.sold import (
    get_all_items,
    get_item,
    get_item_by_name,
    add_item,
    update_item,
    delete_item,
)
from schemas.sold import SoldOut, SoldIn
from app.cruds.CrudOperations import Operations
from connection.models import Sold

router = APIRouter(tags=["sold"], prefix="/sold")
crud = Operations(Sold)

@router.get("/")
async def get_all_solds():
    data = await crud.get_all_items()
    if not data:
        raise HTTPException(status_code=404, detail=f"Nothing item was found")
    return data


@router.get("/{id}", response_model= SoldOut)
async def get_all_solds(id: int):
    data = await get_item(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"The id {id} was not found")
    return data


@router.post("/", response_model= SoldOut)
async def create_item(request: SoldIn):
    item = await get_item_by_name(request.name)
    if item:
        raise HTTPException(
            status_code=409, detail=f"Item {request.name} already exists"
        )
    created_value = await add_item(request)
    return created_value


@router.patch("/{id}", response_model= SoldOut)
async def update_items(id: int, request: SoldIn):
    item = await get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {request.name} not exists")
    return await update_item(id, request)


@router.delete("/{id}")
async def delete_items(id: int):
    item = await get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {id} not exists")
    delete = await delete_item(id)
    item = await get_item(id)
    if item:
        raise HTTPException(status_code=404, detail=f"Item {id} was not deleted")
    return {"message": f"Item {id} was deleted"}
