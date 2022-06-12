# from unittest import result
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str = Query(default=...,max_length=20)):
    results = {
        'data':[1,2,3]
    }
    if q:
        results.update({
            'q':q
        })
    return results

@app.get('/list-items/')
async def read_list_items(q: list[str] | None = Query(default=None,title="Query Items")):
    query_items = {
        'q': q
    }

    return query_items