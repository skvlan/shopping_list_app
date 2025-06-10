# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt
from typing import Any, List
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.grocery_item import GroceryItem
from openapi_server.models.grocery_item_create import GroceryItemCreate


class BaseGroceryItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGroceryItemsApi.subclasses = BaseGroceryItemsApi.subclasses + (cls,)
    async def add_item(
        self,
        grocery_item_create: GroceryItemCreate,
    ) -> GroceryItem:
        """Adds a new item to the grocery list"""
        ...


    async def delete_item(
        self,
        itemId: Annotated[StrictInt, Field(description="ID of the grocery item to delete")],
    ) -> None:
        """Deletes a grocery item from the list"""
        ...


    async def get_item_by_id(
        self,
        itemId: Annotated[StrictInt, Field(description="ID of the grocery item to retrieve")],
    ) -> GroceryItem:
        """Returns details of a specific grocery item"""
        ...


    async def list_items(
        self,
    ) -> List[GroceryItem]:
        """Returns a list of all grocery items in the database"""
        ...


    async def update_item(
        self,
        itemId: Annotated[StrictInt, Field(description="ID of the grocery item to update")],
        grocery_item_create: GroceryItemCreate,
    ) -> GroceryItem:
        """Updates an existing grocery item"""
        ...
