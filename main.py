from fastapi import FastAPI
from pydantic import BaseModel
from calendar_api import create_calendar_event  
app = FastAPI()

class BookingRequest(BaseModel):
    name: str
    email: str
    title: str
    start_time: str  # ISO 8601 format
    end_time: str
    description: str

@app.post("/book")
async def book_event(request: BookingRequest):
    event = create_calendar_event(request)
    return {"message": "Booking successful", "event": event}
