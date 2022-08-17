from pydantic import BaseModel


class MakerIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class MakerOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
