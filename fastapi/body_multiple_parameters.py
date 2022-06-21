from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    password: str


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The Id of item to update", ge= 0, le=1000),
    q: str | None = None,
    item: Item = Body(embed=True),
    user: User,
    importance: int = Body()
):
    results = {
        'item_id':item_id,'user': user
    }
    if q:
        results.update({
            'q':q
        })
    if item:
        results.update(
            {
                'item': item
            }
        )
    return results