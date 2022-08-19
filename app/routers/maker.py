from fastapi import APIRouter, HTTPException
from app.cruds.maker import get_all_items, get_item_by_id, get_item_by_name, add_item, update_item, delete_item
from schemas.maker import MakerOut, MakerIn

router = APIRouter(tags=["makers"], prefix="/maker")


@router.get("/")
async def get_all():
    data = await get_all_items()
    if not data:
        raise HTTPException(status_code=404, detail="Nothing item was found")
    return data


@router.get("/{id}", response_model=MakerOut)
async def get_item_id(id:int):
    data = await get_item_by_id(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"The id {id} was not found")
    return data

## POST
@router.post("/", response_model=MakerOut)
async def create_item(request:MakerIn):
    item = await get_item_by_name(request.name)
    if item:
        raise HTTPException(
            status_code=409, detail=f"Item {request.name} already exists"
        )
    return await add_item(request)
    
## PATCH
@router.patch("/{id}", response_model=MakerOut)
async def update_items(id:int, request: MakerIn):
    data = await get_item_by_id(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Item {request.name} not exists")
    return await update_item(id, request)

## DELETE
@router.delete("/{id}")
async def delete_item_endpoint(id:int):
    data = await get_item_by_id(id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Item {id} not exists")
    await delete_item(id)
    item = await get_item_by_id(id)
    if item:
        raise HTTPException(status_code=404, detail=f"Item {id} was not deleted")
    return {"message": f"Item {id} was deleted"}