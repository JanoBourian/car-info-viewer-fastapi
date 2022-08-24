from pydantic import BaseModel
from typing import Optional


class SoldIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SoldOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SoldParams(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True
