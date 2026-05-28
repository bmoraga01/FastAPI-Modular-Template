from app.common.exceptions import NotFoundException
from app.common.pagination import build_paginated_response
from app.common.schemas.pagination import PaginatedResponse, PaginationParams
from app.modules.products.repository import ProductRepository
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.products.schemas import ProductCreate, ProductRead


class ProductService:
    def __init__(self, repository: ProductRepository):
        # self.repository = ProductRepository()
        self.repository = repository

    async def create_product(
        self, db: AsyncSession, data: ProductCreate
    ) -> ProductRead:
        product = await self.repository.create(db, data)

        return ProductRead.model_validate(product)

    async def get_by_id(self, db: AsyncSession, id: str) -> ProductRead:
        product = await self.repository.get_by_id(db, id)

        if not product:
            raise NotFoundException("Producto no encontrado")

        return ProductRead.model_validate(product)

    async def get_products(
        self, db: AsyncSession, base_url: str, pagination: PaginationParams
    ) -> PaginatedResponse[ProductRead]:
        offset = (pagination.page - 1) * pagination.size

        total = await self.repository.get_total(db)

        products = await self.repository.get_paginated(
            db, offset, pagination.size
        )

        # next_page = (
        #     f"{base_url}?page={pagination.page + 1}&size={pagination.size}"
        #     if offset + pagination.size < total
        #     else None
        # )

        # prev_page = (
        #     f"{base_url}?page={pagination.page - 1}&size={pagination.size}"
        #     if pagination.page > 1
        #     else None
        # )

        # data = [ProductRead.model_validate(product) for product in products]

        # return PaginatedResponse(
        #     data=data,
        #     page=pagination.page,
        #     size=pagination.size,
        #     total=total,
        #     next=next_page,
        #     prev=prev_page,
        # )

        return build_paginated_response(
            items=products,
            total=total,
            pagination=pagination,
            base_url=base_url,
            schema=ProductRead,
        )

    async def update(
        self, db: AsyncSession, id: str, data: ProductCreate
    ) -> ProductRead:
        product = await self.repository.get_by_id(db, id)

        if not product:
            raise NotFoundException("Producto no encontrado")

        product = await self.repository.update(db, data, product)

        return ProductRead.model_validate(product)

    async def delete(self, db: AsyncSession, id: str):
        product = await self.repository.get_by_id(db, id)

        if not product:
            raise NotFoundException("Producto no encontrado")

        await self.repository.delete(db, product)

        return {"message": "Producto eliminado"}
