from pydantic import BaseModel
import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass  # Inherits title, content, and published from PostBase

class PostResponse(PostBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True  # Converts SQLAlchemy models to Pydantic models
