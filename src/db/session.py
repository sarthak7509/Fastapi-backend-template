from src.core.config import database_settings as settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

DB_URL = f"postgresql+asyncpg://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_IP}/{settings.POSTGRES_DATABASE}"

engine = create_async_engine(
    url=DB_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


