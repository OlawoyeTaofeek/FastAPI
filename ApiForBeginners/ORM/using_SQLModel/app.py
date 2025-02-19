from fastapi import FastAPI, HTTPException, status, Response, Depends
from pydantic import BaseModel
from models import *
from schema import *
from database import get_session
from sqlmodel import Session
from typing import Annotated
from sqlmodel import select

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

app = FastAPI()
SessionDep = Annotated[Session, Depends(get_session)]
# Here, it tells FastAPI that a Session object should be provided by calling get_session whenever SessionDep is used.

@app.post("/create_user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: SessionDep) -> UserResponse:
    # Check for existing user
    statement = select(User).where(User.username == user.username)
    user_in_db = db.exec(statement).first()
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User already exists"
        )

    # Create user with hashed password
    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        role_id=user.role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
