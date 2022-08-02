from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome")
async def welcome_message(name: str = "Stranger"):
    if not len(name):
        name = "Stranger"
    return "Welcome " + name + "!"