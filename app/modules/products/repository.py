from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Product
from .schemas import ProductCreate, ProductUpdate

class ProductRepository:
    async def create(self, db: AsyncSession, data: ProductCreate) -> Product:
        product = Product(
            name=data.name,
            brand=data.brand,
            description=data.description,
            quantity=data.quantity,
            price=data.price,
        )

        db.add(product)

        await db.commit()
        await db.refresh(product)

        return product

    async def get_by_id(
        self, db: AsyncSession, product_id: str
    ) -> Product | None:
        query = await db.execute(
            select(Product).where(Product.id == product_id)
        )
        return query.scalar_one_or_none()

    async def get_total(self, db: AsyncSession) -> int:
        query = await db.execute(select(func.count()).select_from(Product))
        return query.scalar() or 0

    async def get_paginated(
        self, db: AsyncSession, offset: int, limit: int
    ) -> list[Product]:
        query = await db.execute(select(Product).offset(offset).limit(limit))

        return list(query.scalars().all())

    async def update(
        self, db: AsyncSession, data: ProductUpdate, product: Product
    ) -> Product:
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(product, field, value)

        await db.commit()
        await db.refresh(product)

        return product

    async def delete(self, db: AsyncSession, product: Product) -> None:
        await db.delete(product)
        await db.commit()
