from fastapi import APIRouter, HTTPException, Request
from app.cruds.engine import (
    get_item,
    update_item,
    delete_item,
)
from app.cruds.CrudOperations import Operations
from schemas.engine import EngineOut, EngineIn, EngineParams
from connection.models import Engine
from typing import List, Optional


router = APIRouter(tags=["engineOut"], prefix="/engine")
crud = Operations(Engine)


@router.get("/")
async def get_all_engines():
    data = await crud.get_all_items()
    if not data:
        raise HTTPException(status_code=404, detail=f"Nothing item was found")
    return data


@router.get("/filter", response_model=List[Optional[EngineOut]])
async def get_with_filter(request: Request):
    filters = request.query_params._dict
    if not filters:
        raise HTTPException(status_code=404, detail=f"No filters added")
    filters = EngineParams(**filters)
    data = await crud.get_items_by_filter(filters.dict())
    if isinstance(data, ValueError):
        raise HTTPException(
            status_code=404, detail=f"Some filter is not inside table columns"
        )
    if not data:
        raise HTTPException(status_code=404, detail=f"Any item was found")
    return data


@router.get("/{id}", response_model=EngineOut)
async def get_all_engines(id: int):
    data = await crud.get_item_by_pk(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"The id {id} was not found")
    return data


@router.post("/", response_model=EngineOut)
async def create_item(request: EngineIn):
    item = await crud.get_items_by_filter(request.dict())
    if item:
        raise HTTPException(
            status_code=409, detail=f"Item {request.name} already exists"
        )
    created_value = await crud.create_item(request.dict())
    return created_value


@router.patch("/{id}", response_model=EngineOut)
async def update_items(id: int, request: EngineIn):
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
