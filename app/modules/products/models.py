import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

# Product model representing the products table in the database

class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, unique=True
    )
    name: Mapped[str]
    brand: Mapped[str]
    description: Mapped[str]
    quantity: Mapped[int]
    price: Mapped[float]

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), server_onupdate=func.now()
    )

    def __repr__(self):
        return f'<Product {self.id}>'
