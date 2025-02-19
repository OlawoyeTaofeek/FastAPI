from fastapi import FastAPI, HTTPException, Depends, Response, status
from models import Post 
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine, get_db
Base.metadata.create_all(bind=engine)
from schema import PostCreate, PostResponse
        
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

