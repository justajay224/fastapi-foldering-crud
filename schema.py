from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, description="Product name cannot be empty")
    category: str
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    stock: int = Field(..., ge=0, description="Stock must be zero or greater")
    

class ProductCreate(ProductBase):
    pass 

class ProductResponse(ProductBase):
    id: int 

    class Config:
        from_attributes = True  
