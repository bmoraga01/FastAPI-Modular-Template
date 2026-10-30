from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.schemas.pagination import PaginatedResponse, PaginationParams
from app.common.schemas.responses import DataResponse, MessageResponse
from app.core.database import get_db
from app.modules.products.repository import ProductRepository

from .schemas import ProductCreate, ProductRead, ProductUpdate
from .services import ProductService

router = APIRouter()

service = ProductService(repository=ProductRepository())


@router.post("/", response_model=DataResponse[ProductRead])
async def create_product(
    data: ProductCreate, db: AsyncSession = Depends(get_db)
):
    product = await service.create_product(db, data)

    return DataResponse(data=product)


@router.get("/{product_id}", response_model=DataResponse[ProductRead])
async def get_product_by_id(
    product_id: str, db: AsyncSession = Depends(get_db)
):
    product = await service.get_by_id(db, product_id)

    return DataResponse(data=product)


@router.get("/", response_model=DataResponse[PaginatedResponse[ProductRead]])
async def get_products(
    request: Request,
    pagination: PaginationParams = Depends(),
    db: AsyncSession = Depends(get_db),
):
    product = await service.get_products(
        db=db,
        base_url=str(request.url.path).split("?")[0],
        pagination=pagination,
    )

    return DataResponse(data=product)


@router.put("/{product_id}", response_model=DataResponse[ProductRead])
async def update_product(
    product_id: str, data: ProductUpdate, db: AsyncSession = Depends(get_db)
):
    product = await service.update(db, product_id, data)

    return DataResponse(data=product)


@router.delete("/{product_id}", response_model=MessageResponse)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):
    return await service.delete(db, product_id)
