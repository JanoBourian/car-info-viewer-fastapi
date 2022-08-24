from pydantic import BaseModel
from typing import Optional


class MakerIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class MakerOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class MakerParams(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True
