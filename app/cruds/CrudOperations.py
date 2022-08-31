from typing import Optional, List, Any, Union
from databases.interfaces import Record
from sqlalchemy import Table
from app.cruds.CrudBuilder import Crud
from connection.databases import database
import logging
import sqlalchemy


class Operations(Crud):
    def __init__(self, model: Table) -> None:
        self.model = model

    async def get_all_items(self) -> List[Record]:
        query = self.model.select()
        return await database.fetch_all(query)

    async def get_item_by_pk(self, pk: Any) -> Optional[Record]:
        id_ = self._get_pk()
        query = self.model.select().where(self.model.c[id_] == pk)
        return await database.fetch_one(query)

    async def get_items_by_filter(self, filters: dict) -> Optional[Record]:
        try:
            data = [column.name for column in self.model.columns]
            valid_filters = {}
            for key, value in filters.items():
                if key not in data:
                    raise ValueError
                if value:
                    valid_filters[key] = value
            query = self.model.select().filter_by(**valid_filters)
            return await database.fetch_all(query)
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            logging.warning(f"Some filter is not inside table columns")
            return e

    async def create_item(self, values: dict) -> Optional[Record]:
        query = self.model.insert().values(values)
        id_ = await database.execute(query)
        return await self.get_item_by_pk(id_)

    async def update_item(self, pk: Any, values: dict) -> Optional[Record]:
        id_ = self._get_pk()
        query = self.model.update().where(self.model.c[id_] == pk).values(values)
        await database.execute(query)
        return await self.get_item_by_pk(pk)

    async def delete_item(self, pk: Any) -> Optional[Record]:
        id_ = self._get_pk()
        query = self.model.delete().where(self.model.c[id_] == pk)
        await database.execute(query)
        return await self.get_item_by_pk(pk)

    def _get_pk(self) -> str:
        for column in self.model.columns:
            if column.primary_key:
                return column.name
        return ""

    async def _check_fk_dependencies(
        self, model: Table, info: dict
    ) -> Union[bool, dict]:
        for item in model.constraints:
            if isinstance(item, sqlalchemy.sql.schema.ForeignKeyConstraint):
                pk = item.referred_table.primary_key.columns._all_columns[0].description
                id_ = info.get(item._col_description)
                query = item.referred_table.select().where(
                    item.referred_table.c[pk] == id_
                )
                resp = await database.fetch_one(query)
                if not resp:
                    return {
                        "error": f"The value of parameter {item._col_description} not exists"
                    }
        return False
