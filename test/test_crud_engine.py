import pytest
from app.main import app
from starlette.testclient import TestClient
from httpx import AsyncClient
import httpx
import json


@pytest.mark.anyio
async def test_root():
    # async with AsyncClient(app=app, base_url="http://localhost:8000/") as ac:
    async with httpx.AsyncClient() as ac:
        response = await ac.get("http://localhost:8000/")
    assert response.status_code == 200
    assert json.loads(response.content) == {"message": "nothing"}


@pytest.mark.anyio
async def test_get_all_items_empty():
    # async with AsyncClient(app=app, base_url="http://localhost:8000/") as ac:
    async with httpx.AsyncClient() as ac:
        response = await ac.get("http://localhost:8000/engine/")
    assert response.status_code == 404
    assert json.loads(response.content) == {"detail": "Nothing item was found"}
