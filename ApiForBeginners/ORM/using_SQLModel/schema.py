from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str
    username: str
    email: EmailStr
    role_id: int

class UserCreate(UserBase):
    password: str  # Password comes raw, will hash before saving

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Needed for ORM-like behavior

class RoleCreate(BaseModel):
    name: str
    description: str


class RoleResponse(RoleCreate):
    id: int

    class Config:
        from_attributes = True