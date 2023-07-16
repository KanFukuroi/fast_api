from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field


class shopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[shopInfo] = None
    items: List[Item]


app = FastAPI()


@app.post("/")
async def index(data: Data):
    return {"data": data}


@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は税込価格、{int(item.price * item.tax)}円です"}


@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {"country_name": country_name, "country_no": country_no}
