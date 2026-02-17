from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class it(BaseModel):
    par1 : str 
    par2 : str 


@app.get("/")
async def root():
    return {"message": "Hello World"}
