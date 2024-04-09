from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from routes.routes import router as item_router
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app.include_router(item_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: Union[str, int]):
    return {"item": item}

@app.put("/items2/{item_id}")
def create_item2(item_id, item: Item):
    return {"item": item, "item_id": item_id}

@app.post("/items/")
def create_item3(item: Item):
    return item

