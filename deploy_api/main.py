from fastapi import FastAPI
from pydantic import BaseModel


class Data(BaseModel):
    x: int
    y: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello Data"}


@app.post("/")
def calc(data: Data):
    z = data.x * data.y
    return {"result": z}
