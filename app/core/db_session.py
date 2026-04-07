from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import config

engine = create_async_engine(
    config.db_url,
    echo=config.debug,
    pool_size=10,          # Persistent connections in the pool
    max_overflow=20,       # Extra connections beyond the pool
    pool_recycle=3600,     # Reset connections every hour
)

# 2. Create a session factory 
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession, 
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# 3. Dependency to get DB session
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()