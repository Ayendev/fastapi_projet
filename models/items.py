from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    in_stock: bool

