# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.grocery_items_api_base import BaseGroceryItemsApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt
from typing import List
# from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.grocery_item import GroceryItem
from openapi_server.models.grocery_item_create import GroceryItemCreate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/items",
    responses={
        201: {"model": GroceryItem, "description": "Item created successfully"},
        400: {"model": Error, "description": "Bad request - invalid input"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["grocery-items"],
    summary="Add a new grocery item",
    response_model_by_alias=True,
)
async def add_item(
    grocery_item_create: GroceryItemCreate = Body(..., description=""),
) -> GroceryItem:
    """Adds a new item to the grocery list"""
    if not BaseGroceryItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroceryItemsApi.subclasses[0]().add_item(grocery_item_create)


@router.delete(
    "/items/{itemId}",
    responses={
        204: {"description": "Item deleted successfully"},
        404: {"model": Error, "description": "The specified resource was not found"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["grocery-items"],
    summary="Delete a grocery item",
    response_model_by_alias=True,
)
async def delete_item(
    itemId: StrictInt = Path(..., description="ID of the grocery item to delete")
) -> None:
    """Deletes a grocery item from the list"""
    if not BaseGroceryItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroceryItemsApi.subclasses[0]().delete_item(itemId)


@router.get(
    "/items/{itemId}",
    responses={
        200: {"model": GroceryItem, "description": "Details of the grocery item"},
        404: {"model": Error, "description": "The specified resource was not found"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["grocery-items"],
    summary="Get a grocery item by ID",
    response_model_by_alias=True,
)
async def get_item_by_id(
    itemId: StrictInt = Path(..., description="ID of the grocery item to retrieve")
) -> GroceryItem:
    """Returns details of a specific grocery item"""
    if not BaseGroceryItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroceryItemsApi.subclasses[0]().get_item_by_id(itemId)


@router.get(
    "/items",
    responses={
        200: {"model": List[GroceryItem], "description": "A list of grocery items"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["grocery-items"],
    summary="List all grocery items",
    response_model_by_alias=True,
)
async def list_items(
    name: Optional[str] = None,
    category: Optional[str] = None,
    purchased: Optional[bool] = None,
    sort_by: Optional[str] = None,
) -> List[GroceryItem]:
    """Returns a list of all grocery items in the database"""
    if not BaseGroceryItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroceryItemsApi.subclasses[0]().list_items(
        name=name,
        category=category,
        purchased=purchased,
        sort_by=sort_by
    )


@router.put(
    "/items/{itemId}",
    responses={
        200: {"model": GroceryItem, "description": "Item updated successfully"},
        400: {"model": Error, "description": "Bad request - invalid input"},
        404: {"model": Error, "description": "The specified resource was not found"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["grocery-items"],
    summary="Update a grocery item",
    response_model_by_alias=True,
)
async def update_item(
    itemId: StrictInt = Path(..., description="ID of the grocery item to update"),
    grocery_item_create: GroceryItemCreate = Body(..., description=""),
) -> GroceryItem:
    """Updates an existing grocery item"""
    if not BaseGroceryItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroceryItemsApi.subclasses[0]().update_item(itemId, grocery_item_create)
