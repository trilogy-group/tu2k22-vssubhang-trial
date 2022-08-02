from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    a: int = 0
    b: int = 0


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sum/")
async def sum_2_numbers(item: Item):
    return {"message": item.a + item.b}