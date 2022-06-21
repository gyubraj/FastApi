from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "example":{
                "name": "Book",
                "description": "Book is written by Yubraj Upadhaya.",
                "price": 45.3,
                "tax": 12.3
            }
        }

@app.post('/config-items/')
async def create_items(item: Item):
    return item.dict()




