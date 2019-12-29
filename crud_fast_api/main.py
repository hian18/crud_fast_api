import sys
sys.path.append('..')
from fastapi import FastAPI
from .routers.items import route as route_items


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(route_items, prefix='/items',tags=["Items"])