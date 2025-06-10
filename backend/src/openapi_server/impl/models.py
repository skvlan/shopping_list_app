from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime
from .database import metadata

grocery_items = Table(
    "grocery_items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("unit", String, nullable=True),
    Column("category", String, nullable=True),
    Column("notes", String, nullable=True),
    Column("created_at", DateTime, nullable=False),
    Column("updated_at", DateTime, nullable=False),
    Column("purchased", Boolean, default=False),
)
