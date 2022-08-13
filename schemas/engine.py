from pydantic import BaseModel

class Engine(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True