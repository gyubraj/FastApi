from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    app = "app"
    rasaj = "maharjan"
    yubraj = "upadhaya"


app = FastAPI()


@app.get(path='/app')
@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/modelname/{model_name}')
async def get_model(model_name: ModelName):

    if model_name == ModelName.app:
        return {
            "model_name": model_name,
            "message": f"This is model {model_name}"
        }
    if model_name == ModelName.rasaj:
        return {
            "model_name": model_name,
            "message": f"This is model {model_name}"
        }
    if model_name == ModelName.yubraj:
        return {
            "model_name": model_name,
            "message": f"This is model {model_name}"
        }

# for file path as an argument

@app.get('/files/{file_path:path}')
async def get_file_path(file_path: str):
    return {
        'filepath': file_path,
        "message" : "This is just testing"
    }

# to run the app, 