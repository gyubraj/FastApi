
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/items/",response_model=Item)
async def create_item(item: Item):
    return item

# Don't do this in production
@app.post("/wrong-user/",response_model=UserIn)
async def create_wrong_user(user: UserIn):
    return user

@app.post("/right-user/", response_model=UserOut)
async def create_right_user(user: UserIn):
    return user