
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "yubrajupdahaya" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_paasword = fake_password_hasher(user_in.password)
    user_in_db = UserDB(**user_in.dict(), hashed_password=hashed_paasword)
    return user_in_db

@app.post('/user', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


# Reduce Duplication 

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class ReduceUserIn(UserBase):
    password: str

class ReduceUserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

# Union or anyOf

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = "car"

class PlaneItem(BaseItem):
    type = "plane"
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
    "item3": {
        "description": "Music is my aeroplane, it's my aeroplane"
    }
}

@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_items(item_id: str):
    return items[item_id]

