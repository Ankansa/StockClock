from pydantic import BaseModel, Field
from datetime import datetime

class ClockInModel(BaseModel):
    email: str
    location: str

class UpdateClockInModel(BaseModel):
    email: str
    location: str
