from __future__ import annotations
from fastapi import Body, FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tags: set[str]
    image: list[Image]


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items : list[Item]

@app.post('/offers/')
async def create_offers(offer: Offer):
    return offer

@app.post("/images/")
async def create_images(images: list[Image]):
    return images

