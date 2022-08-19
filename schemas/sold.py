from pydantic import BaseModel


class SoldIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SoldOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
