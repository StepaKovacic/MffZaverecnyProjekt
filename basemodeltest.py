
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Form</title>
</head>
<body>

    <form action="/login/" method="post">
        
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="description">Description:</label><br>
        <textarea id="description" name="description" rows="4" cols="50" required></textarea><br><br>

        <label for="pricec">Price:</label><br>
        <input type="number" id="pricec" name="pricec" step="0.01" min="0" required><br><br>

        <label for="tax">Tax:</label><br>
        <input type="number" id="tax" name="tax" step="0.01" min="0" required><br><br>

        <button type="submit">Submit</button>

    </form>

</body>
</html>
"""

@app.post("/items/")
async def create_item(item: Item):
    return item
