from fastapi import FastAPI, HTTPException, Depends, Response, status
from models import Post 
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine, get_db
Base.metadata.create_all(bind=engine)
from schema import PostCreate, PostResponse, PostUpdate
from typing import List
from sqlalchemy import select
        
app = FastAPI()

@app.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.title == post.title).first()
    if db_post:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail="Post already exists")
    else:
        new_post = Post(**post.model_dump())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post

@app.get("/posts", response_model=List[PostResponse], status_code=status.HTTP_200_OK)
def get_post(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found")
    return posts 

@app.get("/posts/{post_id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    # post = db.query(Post).filter(Post.id == post_id).first()
    post = db.execute(select(Post).where(Post.id == post_id)).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post[0]


@app.get("/posts/{post_id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.put("/posts/{id}", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def update_post(id: int, updated_post: PostUpdate, db: Session= Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    else:
        post.title = updated_post.title
        post.content = updated_post.content
        post.published = updated_post.published
        db.commit()
        db.refresh(post)
        return post
    
@app.put("/posts_/{id}", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def update_post(id: int, updated_post: PostUpdate, db: Session= Depends(get_db)):
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    else:
        post_query.update(updated_post.model_dump(exclude_unset=True))
        db.commit()
        return post_query.first()
    
    
@app.delete("/posts/{id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    else:
        post_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    


