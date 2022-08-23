from typing import Protocol, List
from databases.interfaces import Record
from sqlalchemy import Table
from app.cruds.CrudBuilder import Crud
from connection.databases import database

class Operations(Crud):
    
    def __init__(self, model:Table) -> None:
        self.model = model
    
    async def get_all_items(self) -> List[Record]:
        query = self.model.select()
        return await database.fetch_all(query)
        