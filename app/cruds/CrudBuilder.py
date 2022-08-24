from typing import Protocol, List, Optional
from databases.interfaces import Record
from sqlalchemy import Table


class Crud(Protocol):

    ## get all items
    async def get_all_items(self, model: Table) -> List[Record]:
        ...

    # get item by pk
    async def get_item_by_pk(self) -> Optional[Record]:
        ...

    # get item by some filters
    async def get_items_by_filter(self) -> Optional[Record]:
        ...

        # # create item
        # async def create_item(self):
        #     ...

        # # update some item (n parameters)
        # async def update_item(self):
        #     ...

        # # delete item
        # async def delete_item(self):
        ...
