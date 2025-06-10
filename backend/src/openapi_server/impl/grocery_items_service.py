from fastapi import HTTPException
from datetime import datetime
from openapi_server.apis.grocery_items_api_base import BaseGroceryItemsApi
from openapi_server.impl import crud
from openapi_server.models.grocery_item import GroceryItem
from openapi_server.models.grocery_item_create import GroceryItemCreate
from typing import Optional
from fastapi import Query, HTTPException



class GroceryItemsService(BaseGroceryItemsApi):

    async def add_item(self, grocery_item_create: GroceryItemCreate) -> GroceryItem:
        item_dict = await crud.add_item(grocery_item_create)
        return GroceryItem(**item_dict)

    async def delete_item(self, itemId: int) -> None:
        item = await crud.get_item_by_id(itemId)
        if item is None:
            raise HTTPException(status_code=404, detail=f"Item with ID {itemId} not found")
        await crud.delete_item(itemId)

    async def get_item_by_id(self, itemId: int) -> GroceryItem:
        item = await crud.get_item_by_id(itemId)
        if item is None:
            raise HTTPException(status_code=404, detail=f"Item with ID {itemId} not found")
        return GroceryItem(**item)

    async def list_items(
            self,
            name: Optional[str] = None,
            category: Optional[str] = None,
            purchased: Optional[bool] = None,
            sort_by: Optional[str] = None,
    ) -> list[GroceryItem]:
        items = await crud.list_items(name, category, purchased, sort_by)
        return [GroceryItem(**item) for item in items]

    async def update_item(self, itemId: int, grocery_item_create: GroceryItemCreate) -> GroceryItem:
        item = await crud.update_item(itemId, grocery_item_create)
        if item is None:
            raise HTTPException(status_code=404, detail=f"Item with ID {itemId} not found")
        return GroceryItem(**item)

