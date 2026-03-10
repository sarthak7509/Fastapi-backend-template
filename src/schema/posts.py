from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostCreate(BaseModel):
    title: str

class PostOut(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        from_attributes = True