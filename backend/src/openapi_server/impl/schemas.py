from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GroceryItemBase(BaseModel):
    name: str
    quantity: int
    unit: Optional[str] = None
    category: Optional[str] = None
    notes: Optional[str] = None

class GroceryItemCreate(GroceryItemBase):
    pass

class GroceryItem(GroceryItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    purchased: bool

    class Config:
        orm_mode = True
