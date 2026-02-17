from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):

    print("tohle je form")
    print(Annotated[str, Form()])

    return {"username": username}


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html") as responseDoc:
        return responseDoc.read() 
