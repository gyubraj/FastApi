from fastapi import FastAPI


app = FastAPI()


@app.get(path='/app')
@app.get('/')
async def root():
    return {"message": "Hello World"}