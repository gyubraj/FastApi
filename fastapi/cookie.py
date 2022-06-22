
from fastapi import FastAPI, Cookie

app = FastAPI()

# auto docs doesn't support cookie passing currently so need to test from terminal
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    print(ads_id)
    return {
        'ads_id': ads_id
    }