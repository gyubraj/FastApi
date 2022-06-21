from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="Id of the item to get", ge= 0, le= 1000),
    q: str,
    size : float = Query(gt=0, lt=10.5)
):
    results = {
        "item_id": item_id
    }
    if q:
        results.update({
            'q':q
        })
    return results