from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

class Item(BaseModel):
    a: int = 0
    b: int = 0


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sum/")
async def sum_2_numbers(item: Item):
    server_2_respone = requests.post("http://server-2:90/sum/", json = {"a": item.a, "b": item.b})
    return {"message": server_2_respone.json()["message"]}