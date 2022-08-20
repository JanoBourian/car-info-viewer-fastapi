import pytest
from app.main import app
from starlette.testclient import TestClient
from httpx import AsyncClient
import httpx
import json

@pytest.mark.anyio
async def test_root():
    async with httpx.AsyncClient() as ac:
        response = await ac.get("http://localhost:8000/")
    assert response.status_code == 200
    assert json.loads(response.content) == {"message": "nothing"}

@pytest.mark.anyio
async def test_get_all_items_empty():
    async with httpx.AsyncClient() as ac:
        response = await ac.get("http://localhost:8000/engine/")
    assert response.status_code == 404
    assert json.loads(response.content) == {"detail": "Nothing item was found"}
    
# @pytest.mark.anyio
# async def test_create_item():
#     data = {
#             "name": "sierra"
#         }
#     async with httpx.AsyncClient() as ac:
#         response = await ac.post("http://localhost:8000/engine/", json = data)
#     assert json.loads(response.content) == {"id": 1, "name": "sierra"}

# @pytest.mark.anyio
# async def test_delete_item():
#     async with httpx.AsyncClient() as ac:
#         response = await ac.delete("http://localhost:8000/engine/1")
#     assert json.loads(response.content) == {"message": "Item 1 was deleted"}