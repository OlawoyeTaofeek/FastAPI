from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union, Dict, List 
import datetime 

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str
    date: datetime.datetime
    
@app.post("/create")
async def create(post: Post):
    return {
        "message": "Post created successfully",
        "post": post
    }