from pydantic import BaseModel, EmailStr
from datetime import datetime
from .posts import PostOut

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserCreateOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    class config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    posts : list[PostOut]
    created_at: datetime

    class config:
        from_attributes = True