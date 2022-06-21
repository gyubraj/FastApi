
from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import FastAPI, Body

from pydantic import BaseModel

class Item(BaseModel):
    id: UUID
    created_on: datetime
    update_time: time



app = FastAPI()


@app.post("/data-items/{item_id}")
async def data_items(
    item_id: UUID,
    start_datetime: datetime = Body(),
    end_datetime: datetime = Body(),
    repeat_at: time = Body(),
    process_after: timedelta = Body(),
    item: Item = Body()
    ):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
        "item": item
    } 