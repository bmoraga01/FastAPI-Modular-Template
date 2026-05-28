from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel):
    success: bool = True
    message: str


class DataResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T


class MessageResponse(BaseModel):
    success: bool = True
    message: str
