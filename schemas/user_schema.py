from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    correo: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True