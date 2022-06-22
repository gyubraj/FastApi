
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float  = 10.5
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


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get('/items/{item_id}', response_model=Item,response_model_exclude_unset= True)
async def read_items(item_id: str):
    return items[item_id]

@app.get('/include-items/{item_id}', response_model=Item, response_model_include=['name','price'])
async def read_items(item_id: str):
    return items[item_id]


@app.get('/exclude-items/{item_id}', response_model=Item, response_model_exclude=['description','price'])
async def read_items(item_id: str):
    return items[item_id]