from typing import List, Optional
from sqlalchemy import select, update, delete
from datetime import datetime

from .models import grocery_items
from .schemas import GroceryItemCreate
from .database import database


async def list_items(
    name: Optional[str] = None,
    category: Optional[str] = None,
    purchased: Optional[bool] = None,
    sort_by: Optional[str] = None,
) -> List[dict]:

    query = grocery_items.select()

    if name:
        query = query.where(grocery_items.c.name.ilike(f"%{name}%"))
    if category:
        query = query.where(grocery_items.c.category == category)
    if purchased is not None:
        query = query.where(grocery_items.c.purchased == purchased)

    if sort_by in ("created_at", "updated_at"):
        query = query.order_by(getattr(grocery_items.c, sort_by))

    rows = await database.fetch_all(query)
    return [dict(row) for row in rows]


async def get_item_by_id(item_id: int) -> Optional[dict]:
    query = grocery_items.select().where(grocery_items.c.id == item_id)
    item = await database.fetch_one(query)
    return dict(item) if item else None


async def add_item(item_create: GroceryItemCreate) -> dict:
    now = datetime.utcnow()
    query = grocery_items.insert().values(
        name=item_create.name,
        quantity=item_create.quantity,
        unit=item_create.unit,
        category=item_create.category,
        notes=item_create.notes,
        created_at=now,
        updated_at=now,
        purchased=False,
    )
    item_id = await database.execute(query)
    return await get_item_by_id(item_id)


async def update_item(item_id: int, item_update: GroceryItemCreate) -> Optional[dict]:
    now = datetime.utcnow()
    query = (
        grocery_items.update()
        .where(grocery_items.c.id == item_id)
        .values(
            name=item_update.name,
            quantity=item_update.quantity,
            unit=item_update.unit,
            category=item_update.category,
            notes=item_update.notes,
            updated_at=now,
        )
    )
    await database.execute(query)
    return await get_item_by_id(item_id)


async def delete_item(item_id: int) -> None:
    query = grocery_items.delete().where(grocery_items.c.id == item_id)
    await database.execute(query)
