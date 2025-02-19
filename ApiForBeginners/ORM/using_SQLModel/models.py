from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    users: List["User"] = Relationship(back_populates="role")  # ✅ Matching name now

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    email: str
    password_hash: str
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role: Optional[Role] = Relationship(back_populates="users")  # ✅ Matching name now

  # Many-to-one side


# In SQLModel, the Field function is used to provide additional metadata and configuration for columns in your database model. It allows you to specify properties like default values, primary keys, indexes, nullable constraints, and more.