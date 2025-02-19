from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/posts")
async def get_posts():
    # Simulating fetching data from a database
    posts = [
        {"id": 1, "title": "Post 1", "author": "John Doe"},
        {"id": 2, "title": "Post 2", "author": "Jane Smith"},
        {"id": 3, "title": "Post 3", "author": "Bob Johnson"}
    ]
    return posts


# Define the request model
class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True  # Default value is True

@app.post("/create_post", status_code=201)
async def create_post(post: PostCreate):
    return {
        "message": "Post created Successfully",
        "post": post
    }
    
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/create_posts")
async def create_post(post: dict = Body(...)):
    return {
        "message": "Post created successfully",
        "post": post
    }
