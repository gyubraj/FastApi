
from fastapi import FastAPI, status


app = FastAPI()

@app.post("/items/",status_code= 201)
async def create_item(name: str):
    return {
        'name': name
    }

# HTTP status codes

@app.post("/create-item/", status_code= status.HTTP_201_CREATED)
async def create_item(name: str):
    return {
        'name': name
    }
