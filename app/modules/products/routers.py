from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.common.schemas.pagination import PaginatedResponse, PaginationParams
from app.common.schemas.responses import DataResponse
from app.core.database import get_db
from app.modules.products.repository import ProductRepository
from .schemas import ProductCreate, ProductRead
from .services import ProductService

router = APIRouter()

service = ProductService(repository=ProductRepository())


@router.post("/", response_model=DataResponse[ProductRead])
async def create_product(
    data: ProductCreate, db: AsyncSession = Depends(get_db)
):
    return DataResponse(data=await service.create_product(db, data))


@router.get("/{id}", response_model=DataResponse[ProductRead])
async def get_product_by_id(id: str, db: AsyncSession = Depends(get_db)):
    return DataResponse(data=await service.get_by_id(db=db, id=id))


@router.get("/", response_model=DataResponse[PaginatedResponse[ProductRead]])
async def get_products(
    request: Request,
    pagination: PaginationParams = Depends(),
    db: AsyncSession = Depends(get_db),
):
    return DataResponse(
        data=await service.get_products(
            db=db,
            base_url=str(request.url.path).split("?")[0],
            pagination=pagination,
        )
    )


@router.put("/{id}", response_model=DataResponse[ProductRead])
async def update_product(
    id: str, data: ProductCreate, db: AsyncSession = Depends(get_db)
):
    return DataResponse(data=await service.update(db, id, data))


@router.delete("/{id}")
async def delete_product(id: str, db: AsyncSession = Depends(get_db)):
    return await service.delete(db, id)
