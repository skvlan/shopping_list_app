from sqlalchemy import Table, Column, Integer, String
from openapi_server.impl.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("role", String, default="user", nullable=False),
)

