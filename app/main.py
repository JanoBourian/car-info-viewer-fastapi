from fastapi import FastAPI
from app.routers import engine

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "nothing"}

app.include_router(engine.router)