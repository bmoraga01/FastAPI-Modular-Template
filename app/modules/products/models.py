from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.common.helpers import generate_uuid


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(
        String(24), primary_key=True, default=generate_uuid
    )
    name: Mapped[str]
    brand: Mapped[str]
    description: Mapped[str]
    quantity: Mapped[int]
    price: Mapped[float]

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f'<Product {self.id}>'
