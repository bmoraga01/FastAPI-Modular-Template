from typing import TypeVar
from pydantic import BaseModel

from app.common.schemas.pagination import PaginatedResponse, PaginationParams

T = TypeVar("T")
K = TypeVar("K", bound=BaseModel)


def build_paginated_response(
    *,
    items: list[T],
    total: int,
    pagination: PaginationParams,
    base_url: str,
    schema: type[K],
) -> PaginatedResponse[K]:
    next_page = (
        f"{base_url}?page={pagination.page + 1}&size={pagination.size}"
        if pagination.page * pagination.size < total
        else None
    )

    prev_page = (
        f"{base_url}?page={pagination.page - 1}&size={pagination.size}"
        if pagination.page > 1
        else None
    )

    data = [schema.model_validate(item) for item in items]

    return PaginatedResponse[K](
        data=data,
        page=pagination.page,
        size=pagination.size,
        total=total,
        next=next_page,
        prev=prev_page,
    )
