from enum import Enum
from fastapi import FastAPI

from pydantic import BaseModel


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


# Query Parameters

fake_object : list[dict[str,str]] =[
    {
        'name' : 'yubraj'
    },
    {
        'name' : 'shreeva'
    },
    {
        'name' : 'dev'
    },
    {
        'name' : 'saugat'
    },
    {
        'name' : 'manish'
    },
    {
        'name' : 'puskal'
    },

]

@app.get('/query-parameter')
async def query_parameters(start :int = 0, limit :int = 2):
    return fake_object[start:start+limit]

@app.get('/optional-query-parameter')
async def optional_query_parameter(data: int = 0, q: str | None = None):
    if q:
        return {
            'q': q
        }
    return {
        'data': data
    }

# Request Body 

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    # This will chnage model into dict
    print(type(item.dict()))

    item_dict = item.dict()

    if item.tax:
        item.price = item.price + item.tax
    
    item_dict.update({
        'price_with_tax': item_dict['price'] + item_dict['tax']
    })
    
    return item_dict

# Request Body + Path Parameters

@app.post('/items-path-parameters/{item_id}')
async def create_item_with_path_parameter(item_id: str, item: Item):
    """
    This is just for testing purpose as i want to see docs
    """
    return {
        'item_id': item_id,
        **item.dict()
    }

# request Body + Path + Query Parameters
@app.post('/items-path-query-parameter/{item_id}')
async def create_item_path_query_parameter(item_id: int, item: Item, query: str):
    return {
        'item_id': item_id,
        'query': query,
        **item.dict()
    }
