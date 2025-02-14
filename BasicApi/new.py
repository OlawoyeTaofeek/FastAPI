from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime
from typing import List, Optional, Union
from fastapi import HTTPException, status, Response, Depends

app = FastAPI()
## Basic CRUD Operations

class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str
    published_date: datetime.datetime = Field(default_factory=datetime.datetime.now)
    rating: Optional[float] = None  # Default rating is None if not provided
    
# Schema for partial update (all fields optional)
class PostUpdate(BaseModel):
    author: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    rating: Optional[float] = None

# Pre-filled in-memory storage for posts
posts_db: List[Post] = []

# Add initial sample posts
posts_db.extend([
    Post(id=1, author="John Doe", title="FastAPI Guide", 
         content="FastAPI makes APIs easy!", 
         published_date=datetime.datetime(2025, 2, 1, 10, 30, 45), rating=4.5),
    Post(id=2, author="Alice", title="Machine Learning", 
         content="ML is transforming the world.", 
         published_date=datetime.datetime(2025, 2, 2, 12, 15, 30), rating=4.8),
    Post(id=3, author="Bob", title="Introduction to SQL", 
         content="SQL is the backbone of data management.", 
         published_date=datetime.datetime(2025, 2, 3, 9, 45, 10), rating=4.2),
])

# POST request - Create multiple posts
@app.post("/createposts")
async def create_posts(new_posts: List[Post]):
    posts_db.extend(new_posts)  # Add new posts to storage
    return {
        "message": "success",
        "posts": [post.model_dump() for post in new_posts]
    }
    
@app.post("/create_posts", status_code=201)
async def create_posts(new_posts: List[Post]):
    posts_db.extend(new_posts)  # Add new posts to storage
    return {
        "message": "success",
        "posts": [post.model_dump() for post in new_posts]
    }

@app.post("/create_posts_", status_code=status.HTTP_201_CREATED)
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
    for post in posts_db:
        if post.id == int(id):
            return {
                "message": "success",
                "post": post.model_dump()}
            

@app.get("/post/{id}")
# Response: Setting The status code yourself
async def get_post(id: int, response : Response):
    post = next((post for post in posts_db if post.id ==id ), None)
    
    if post:
        return {
            "message": "success",
            "post": post.model_dump()
        }
    else:
        response.status_code = 404
        return {"message": "Post not found"}
    
## Method 2: using status
## response_model : 
    #   1. Automatic Data Validation & Serialization
         ## Without response_model: You manually serialize the response using .model_dump().
    #   2. Automatic Error Handling & Validation
         ## If the provided data doesn't match the schema, FastAPI will automatically return a 422 response with an appropriate error message.
         # return Post.from_orm(next((post for post in posts_db if post.id == id), None))
    # 3. Performance Optimization (Excludes Extra Fields)
         ## If response_model is used, FastAPI removes any extra fields that are not defined in the model.
    # 4. Security: Prevents Leaking Sensitive Data
         
@app.get("/post_/{id}", response_model=Post)
async def get_post(id: int, response: Response):
    post = next((post for post in posts_db if post.id == id), None)
    
    if post:
        return post  # FastAPI auto-converts Pydantic model to JSON

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": f"Post with id {id} was not found"}
# Yes, when you search for an id that doesn't exist none is returned! The issue is that None does not match the response_model=Post, so FastAPI throws an error instead of returning your custom message.

@app.get("/posts_/{id}", response_model = Union[Post, dict])  # Allow dict for error response
async def get_post(id: int, response: Response):
    post = next((post for post in posts_db if post.id == id), None)

    if post:
        return post  # ✅ FastAPI converts it to JSON

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": f"Post with id {id} was not found"} 

## Using HTTP Exceptions instead 
@app.get("/posts__/{id}", response_model = Union[Post, dict])  # Allow dict for error response
async def get_post(id: int):
    post = next((post for post in posts_db if post.id == id), None)

    if post:
        return post  # ✅ FastAPI converts it to JSON

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id {id} was not found")

@app.get("/post_latest")
async def latest():
    if not posts_db:  # Check if posts_db is empty
        return {"message": "No posts available"}

    latest_post = max(posts_db, key=lambda post: post.published_date, default=None)

    if latest_post is None:
        return {"message": "No posts found"}

    return {
        "message": "success",
        "post": latest_post.model_dump()
    }


# Update
@app.put("/post/{id}")
async def update_post(id: int, updated_post: Post):
    for i, post in enumerate(posts_db):
        if post.id == id:
            posts_db[i] = updated_post
            return {"message": "success", "post": updated_post.model_dump()}
    
    return {"message": "Post not found"}

@app.put("/post/{id}")
async def update_post(id: int, updated_post: Post):
    post = next((p for p in posts_db if p.id == id), None)

    if post:
        posts_db.remove(post)  # Remove the old post
        posts_db.append(updated_post)  # Add the updated post
        return {"message": "success", "post": updated_post.model_dump()}
    
    return {"message": "Post not found"}


@app.put("/post/{id}")
async def update_post(id: int, updated_post: Post):
    post = next((p for p in posts_db if p.id == id), None)

    if post:
        post.author = updated_post.author
        post.title = updated_post.title
        post.content = updated_post.content
        post.published_date = updated_post.published_date
        post.rating = updated_post.rating
        
        return {"message": "success", "post": post.model_dump()}
    
    return {"message": "Post not found"}


# Delete
@app.delete("/delete_post/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    for i, post in enumerate(posts_db):
        if post.id == id:
            del posts_db[i]
            return {"message": "successful, post was deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id {id} was not found"
    )    
    
    
@app.patch("/post/{id}")
async def update_post(id: int, updated_data: PostUpdate):
    for post in posts_db:
        if post.id == id:
            # Update only provided fields
            updated_fields = updated_data.model_dump(exclude_unset=True)
            for key, value in updated_fields.items():
                setattr(post, key, value)
            return {"message": "success", "post": post.model_dump()}

    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")

@app.patch("/post_/{id}")
async def update_post(id: int, updated_data: PostUpdate):
    for index, post in enumerate(posts_db):
        if post.id == id:
            updated_fields = updated_data.model_dump(exclude_unset=True)

            # Convert Pydantic model to dictionary, update fields
            updated_post_data = post.model_dump()  # Convert to dict
            updated_post_data.update(updated_fields)  # Apply updates

            # Replace the existing post with an updated instance
            posts_db[index] = Post(**updated_post_data)  # Recreate the object
            return {"message": "success", "post": posts_db[index].model_dump()}

    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")