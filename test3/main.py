from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model danych
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Endpoint dla ścieżki głównej "/"
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

# Obsługa POST dla "/items/"
@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

# Obsługa GET dla "/items/"
@app.get("/items/")
async def read_items():
    return {"items": [{"name": "Laptop", "price": 1500.0}]}