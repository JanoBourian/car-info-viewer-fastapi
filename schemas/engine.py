from pydantic import BaseModel
from typing import Optional


class Engine(BaseModel):
    id: int
    name: str


class EngineIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class EngineOut(Engine):
    class Config:
        orm_mode = True


class EngineParams(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True
