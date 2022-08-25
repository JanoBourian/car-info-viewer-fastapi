from fastapi import APIRouter, HTTPException, Request
from app.cruds.CrudOperations import Operations
from connection.models import Car
from schemas.car import CarIn, CarOut, CarParams
from typing import List, Optional

router = APIRouter(tags=["CarOut"], prefix="/car")
crud = Operations(Car)

@router.get("/")
async def get_all_items():
    data = await crud.get_all_items()
    if not data:
        raise HTTPException(status_code=404, detail=f"Nothing item was found")
    return data

@router.get("/filter", response_model = List[Optional[CarOut]])
async def get_with_filter(request:Request):
    filters = request.query_params._dict
    if not filters:
        raise HTTPException(status_code=404, detail=f"Not filters added")
    filters = CarParams(**filters)
    data = await crud.get_items_by_filter(filters.dict())
    if isinstance(data, ValueError):
        raise HTTPException(
            status_code=404, detail=f"Some filter is not inside table columns"
        )
    if not data:
        raise HTTPException(status_code=404, detail=f"Any item was found")
    return data

@router.get("/{id}", response_model = CarOut)
async def get_item_by_id(id:int):
    data = await crud.get_item_by_pk(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"The id {id} was not found")
    return data

@router.post("/", response_model=CarOut)
async def create_item(request: CarIn):
    item = await crud.get_items_by_filter(request.dict())
    if item:
        raise HTTPException(
            status_code=409, detail=f"Item {request.name} already exists"
        )
    created_value = await crud.create_item(request.dict())
    return created_value


@router.patch("/{id}", response_model=CarOut)
async def update_item(id: int, request: CarIn):
    item = await crud.get_item_by_pk(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {request.name} not exists")
    return await crud.update_item(id, request.dict())


@router.delete("/{id}")
async def delete_item(id: int):
    item = await crud.get_item_by_pk(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {id} not exists")
    delete = await crud.delete_item(id)
    item = await crud.get_item_by_pk(id)
    if item:
        raise HTTPException(status_code=404, detail=f"Item {id} was not deleted")
    return {"message": f"Item {id} was deleted"}