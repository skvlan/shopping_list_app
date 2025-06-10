from sqlalchemy import create_engine, MetaData
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@postgres:5432/postgres")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)
