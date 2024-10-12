from fastapi import APIRouter
from app.controllers.clock_in_controller import (
    create_clock_in,
    get_clock_in,
    filter_clock_ins,
    delete_clock_in,
    update_clock_in
)
from app.models.clock_in_model import ClockInModel, UpdateClockInModel

router = APIRouter()

@router.post("/", response_model=dict)
async def post_clock_in(clock_in: ClockInModel):
    return await create_clock_in(clock_in)

@router.get("/{clock_in_id}", response_model=dict)
async def get_single_clock_in(clock_in_id: str):
    return await get_clock_in(clock_in_id)

@router.get("/filter", response_model=list)
async def get_filtered_clock_ins(email: str = None, location: str = None, insert_date: str = None):
    return await filter_clock_ins(email, location, insert_date)

@router.delete("/{clock_in_id}", response_model=dict)
async def remove_clock_in(clock_in_id: str):
    return await delete_clock_in(clock_in_id)

@router.put("/{clock_in_id}", response_model=dict)
async def put_clock_in(clock_in_id: str, clock_in: UpdateClockInModel):
    return await update_clock_in(clock_in_id, clock_in)
