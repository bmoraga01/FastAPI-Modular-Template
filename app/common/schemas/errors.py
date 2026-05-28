from typing import Any
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: Any | None = None
