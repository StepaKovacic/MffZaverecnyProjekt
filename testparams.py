from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html") as responseDoc:
        response = responseDoc.read() 
    return response 
