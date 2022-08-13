from fastapi import APIRouter, HTTPException
from app.cruds.engine import get_all_items, get_item
from schemas.engine import Engine

router = APIRouter(tags = ["engine"], prefix = "/engine")

@router.get("/")
async def get_all_engines():
    data = await get_all_items()
    return data

@router.get("/{id}", response_model = Engine)
async def get_all_engines(id:int):
    data = await get_item(id)
    if not data:
        raise HTTPException(status_code = 404, detail = f"The id {id} was not found")
    return data