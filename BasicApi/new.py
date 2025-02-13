from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime
from typing import List, Optional

app = FastAPI()

class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str
    published_date: datetime.datetime = Field(default_factory=datetime.datetime.now)
    rating: Optional[float] = None  # Default rating is None if not provided

# Pre-filled in-memory storage for posts
posts_db: List[Post] = []

# Add initial sample posts
posts_db.extend([
    Post(id=1, author="John Doe", title="FastAPI Guide", content="FastAPI makes APIs easy!", published_date=datetime.datetime(2025, 2, 1, 10, 30, 45), rating=4.5),
    Post(id=2, author="Alice", title="Machine Learning", content="ML is transforming the world.", published_date=datetime.datetime(2025, 2, 2, 12, 15, 30), rating=4.8),
    Post(id=3, author="Bob", title="Introduction to SQL", content="SQL is the backbone of data management.", published_date=datetime.datetime(2025, 2, 3, 9, 45, 10), rating=4.2),
])

# POST request - Create multiple posts
@app.post("/createposts")
async def create_posts(new_posts: List[Post]):
    posts_db.extend(new_posts)  # Add new posts to storage
    return {
        "message": "success",
        "posts": [post.model_dump() for post in new_posts]
    }

# GET request - Retrieve all posts
@app.get("/getposts")
async def get_posts():
    return {
        "message": "success",
        "posts": [post.model_dump() for post in posts_db]
    }


@app.get("/posts/{id}")
async def get_post(id):
    ...