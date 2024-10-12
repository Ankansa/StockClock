from fastapi import HTTPException
from bson import ObjectId
from app.database.connection import get_database
from app.models.clock_in_model import ClockInModel, UpdateClockInModel
from datetime import datetime

db = get_database()

async def create_clock_in(clock_in: ClockInModel):
    clock_in_data = clock_in.dict()
    clock_in_data['insert_date'] = datetime.now()
    result = db.clock_in_records.insert_one(clock_in_data)
    return {"id": str(result.inserted_id)}

async def get_clock_in(clock_in_id: str):
    record = db.clock_in_records.find_one({"_id": ObjectId(clock_in_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    record['_id'] = str(record['_id'])
    return record

async def filter_clock_ins(email: str = None, location: str = None, insert_date: str = None):
    filters = {}
    if email:
        filters['email'] = email
    if location:
        filters['location'] = location
    if insert_date:
        filters['insert_date'] = {"$gt": insert_date}
    
    records = db.clock_in_records.find(filters)
    return [{"_id": str(record['_id']), **record} for record in records]

async def delete_clock_in(clock_in_id: str):
    result = db.clock_in_records.delete_one({"_id": ObjectId(clock_in_id)})
    if result.deleted_count == 1:
        return {"message": "Record deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

async def update_clock_in(clock_in_id: str, clock_in: UpdateClockInModel):
    result = db.clock_in_records.update_one({"_id": ObjectId(clock_in_id)}, {"$set": clock_in.dict()})
    if result.modified_count == 1:
        return {"message": "Record updated"}
    raise HTTPException(status_code=404, detail="Record not found")
