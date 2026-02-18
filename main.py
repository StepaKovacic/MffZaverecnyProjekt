from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

class InvoiceInfo(BaseModel):
    username: str 
    password: str 

@app.post("/login/")
async def login(inv: InvoiceInfo):
    return inv

#@app.post("/login/")
#async def login(
#        username: Annotated[str, Form()], 
#        password: Annotated[str, Form()]
#        ):
#    print(Form())
#
#    return {"username": username}


params = {"a":"1"}

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html") as responseDoc:
        return responseDoc.read() 
