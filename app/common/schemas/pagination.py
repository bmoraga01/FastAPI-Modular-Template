from fastapi import Query
from pydantic import BaseModel
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class PaginationParams(BaseModel):
    page: int = Query(1, ge=1)
    size: int = Query(10, ge=1, le=100)


class PaginatedResponse(BaseModel, Generic[T]):
    data: list[T]
    page: int
    size: int
    total: int
    next: Optional[str] = None
    prev: Optional[str] = None
