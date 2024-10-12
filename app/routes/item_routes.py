from fastapi import APIRouter
from app.controllers.item_controller import (
    create_item,
    get_item,
    filter_items,
    aggregate_items,
    delete_item,
    update_item
)
from app.models.item_model import ItemModel, UpdateItemModel

router = APIRouter()

@router.post("/", response_model=dict)
async def post_item(item: ItemModel):
    return await create_item(item)

@router.get("/{item_id}", response_model=dict)
async def get_single_item(item_id: str):
    return await get_item(item_id)

@router.get("/filter", response_model=list)
async def get_filtered_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    return await filter_items(email, expiry_date, insert_date, quantity)

@router.get("/aggregate", response_model=list)
async def get_item_aggregates():
    return await aggregate_items()

@router.delete("/{item_id}", response_model=dict)
async def remove_item(item_id: str):
    return await delete_item(item_id)

@router.put("/{item_id}", response_model=dict)
async def put_item(item_id: str, item: UpdateItemModel):
    return await update_item(item_id, item)
