from pydantic import BaseModel


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
