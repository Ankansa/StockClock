from pydantic import BaseModel, Field
from datetime import date

class ItemModel(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

class UpdateItemModel(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date
