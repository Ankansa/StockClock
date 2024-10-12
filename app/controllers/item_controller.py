from fastapi import HTTPException
from bson import ObjectId
from app.database.connection import get_database
from app.models.item_model import ItemModel, UpdateItemModel
from datetime import datetime

db = get_database()

async def create_item(item: ItemModel):
    item_data = item.dict()
    item_data['insert_date'] = datetime.now()
    result = db.items.insert_one(item_data)
    return {"id": str(result.inserted_id)}

async def get_item(item_id: str):
    item = db.items.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item['_id'] = str(item['_id'])
    return item

async def filter_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    filters = {}
    if email:
        filters['email'] = email
    if expiry_date:
        filters['expiry_date'] = {"$gt": expiry_date}
    if insert_date:
        filters['insert_date'] = {"$gt": insert_date}
    if quantity:
        filters['quantity'] = {"$gte": quantity}
    
    items = db.items.find(filters)
    return [{"_id": str(item['_id']), **item} for item in items]

async def aggregate_items():
    pipeline = [{"$group": {"_id": "$email", "count": {"$sum": 1}}}]
    result = list(db.items.aggregate(pipeline))
    return result

async def delete_item(item_id: str):
    result = db.items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

async def update_item(item_id: str, item: UpdateItemModel):
    result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    if result.modified_count == 1:
        return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")
