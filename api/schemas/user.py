from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    is_verified: bool=False
    created_at: datetime
    update_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str

class UserUpdate(BaseModel):
    password: str
