from collections.abc import AsyncGenerator
from datetime import datetime

from sqlalchemy import DateTime, MetaData
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.core.config import settings

engine = create_async_engine(
    settings.POSTGRES_URL,
)

SessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

metadata = MetaData()

Base = declarative_base(
    metadata=metadata, type_annotation_map={datetime: DateTime(timezone=True)}
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
