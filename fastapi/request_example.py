
from fastapi import FastAPI, Body
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


@app.post('/single-example-items')
async def single_example_item(item: Item = Body(example={
                "name": "Book",
                "description": "Book is written by Yubraj Upadhaya.",
                "price": 45.3,
                "tax": 12.3
            })):
            return item.dict()



@app.post('/multiple-example-items/')
async def multiple_example_items(item: Item = Body(examples={
                "normal":{
                    "summary": "A normal example.",
                    "description": "Just Test",
                    "value":{
                        "name": "Book",
                        "description": "Book is written by Yubraj Upadhaya.",
                        "price": 45.3,
                        "tax": 12.3
                    },
                },
                "converted":{
                    "summary": "A converted example.",
                    "description": "Just Test",
                    "value":{
                        "name": "Book",
                        "description": "Book is written by Yubraj Upadhaya.",
                        "price": 45.3,
                        "tax": 12.3
                    },
                },
            })):
    return item.dict()



