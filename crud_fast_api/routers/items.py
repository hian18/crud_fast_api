from typing import List
from fastapi import APIRouter
from ..models.items import Item

route=APIRouter()

@route.get('/',response_model=List[Item])
def get():
    return []     
@route.post('/',response_model=Item)
def post(item:Item):
    return item  
@route.put('/{item_id}')
def put():
    ...     
@route.delete('/{item_id}')
def delete():
    ...
