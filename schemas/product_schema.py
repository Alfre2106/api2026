from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    nombre: str
    precio: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True