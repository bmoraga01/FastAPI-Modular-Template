from datetime import datetime
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    brand: str
    description: str
    quantity: int
    price: float


class ProductRead(ProductCreate):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProductUpdate(BaseModel):
    name: str | None = None
    brand: str | None = None
    description: str | None = None
    quantity: int | None = None
    price: float | None = None
