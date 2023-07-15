from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


app = FastAPI()


@app.post("/item/")
async def create_item(item: Item):
    return item


@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {"country_name": country_name, "country_no": country_no}
