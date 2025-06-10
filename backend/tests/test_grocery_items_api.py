# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt  # noqa: F401
from typing import Any, List  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.grocery_item import GroceryItem  # noqa: F401
from openapi_server.models.grocery_item_create import GroceryItemCreate  # noqa: F401


def test_add_item(client: TestClient):
    """Test case for add_item

    Add a new grocery item
    """
    grocery_item_create = {"unit":"liters","quantity":2,"notes":"Lactose-free","name":"Milk","category":"Dairy"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/items",
    #    headers=headers,
    #    json=grocery_item_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_item(client: TestClient):
    """Test case for delete_item

    Delete a grocery item
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/items/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_item_by_id(client: TestClient):
    """Test case for get_item_by_id

    Get a grocery item by ID
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/items/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_items(client: TestClient):
    """Test case for list_items

    List all grocery items
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/items",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_item(client: TestClient):
    """Test case for update_item

    Update a grocery item
    """
    grocery_item_create = {"unit":"liters","quantity":2,"notes":"Lactose-free","name":"Milk","category":"Dairy"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/items/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=grocery_item_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

