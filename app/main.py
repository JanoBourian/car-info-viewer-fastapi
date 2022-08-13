from fastapi import FastAPI
from app.routers import engine
from connection.databases import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def index():
    return {"message": "nothing"}

app.include_router(engine.router)