import pytest
from app.main import app
from httpx import AsyncClient

@pytest.mark.anyio
async def test_get_all_items_empty():
    async with AsyncClient(app=app, base_url="http://localhost:8000/") as ac:
        response = await ac.get("engine/")
    assert response.status_code == 307
    assert response.json == {'detail': 'Nothing item was found'}