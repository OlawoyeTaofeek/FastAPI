from fastapi import FastAPI, HTTPException, status, Response, Depends, Query
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

@app.post("/create_user", response_model=UserResponse, 
          status_code=status.HTTP_201_CREATED)
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

@app.post("/create_role", response_model=RoleResponse, 
          status_code=status.HTTP_201_CREATED)
async def create_role(role: RoleCreate, db: SessionDep) -> RoleResponse:
    # check for existing role
    statement = select(Role).where(Role.name == role.name)
    role_in_db = db.exec(statement).first()
    if role_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role already exists"
        )
    else:
        new_role = Role(**role.model_dump())
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return new_role

@app.get("/users", response_model=List[UserResponse])
async def get_users(db: SessionDep, limit: Annotated[int, Query(le=100)] = 5) -> List[UserResponse]:
    users = db.exec(select(User).order_by(User.id).limit(limit)).all()
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users

@app.get("/roles", response_model=List[RoleResponse])
async def get_roles(db: SessionDep) -> List[RoleResponse]:
    role = db.exec(select(Role).order_by(Role.id)).all()
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No roles found")
    return role