from fastapi import FastAPI


app = FastAPI()


@app.get(path='/app')
@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}

# to run the app, 