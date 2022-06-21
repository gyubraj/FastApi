from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(max_length= 50)
    description : str | None = Field(default=None, title="Description of the Item",max_length=300)
    price: float = Field(gt=10, le= 100)
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(ge=0),
    item: Item = Body(embed=True)
    ):
    return {
        'item_id': item_id,
        'item': item
    }
