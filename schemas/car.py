from pydantic import BaseModel
from schemas.engine import EngineOut
from schemas.maker import MakerOut
from schemas.sold import SoldOut
from datetime import date

class CarIn(BaseModel):
    model:str
    year:date
    price:float
    autonomus:bool
    engine_id:int
    maker_id:int
    sold_id:int
    
    class Config:
        orm_mode = True

class CarOut(BaseModel):
    id:int
    model:str
    year:date
    price:float
    autonomus:bool
    engine_id:int
    maker_id:int
    sold_id:int
    
    class Config:
        orm_mode = True

class CarOutExplicit(BaseModel):
    id:int
    model:str
    year:date
    price:float
    autonomus:bool
    engine_id:EngineOut
    maker_id:MakerOut
    sold_id:SoldOut
    
    class Config:
        orm_mode = True