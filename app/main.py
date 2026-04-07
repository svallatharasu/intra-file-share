from fastapi import FastAPI

import uvicorn
from core.config import config
from core.logging import init_sentry
from contextlib import asynccontextmanager
from api.v1 import posts

init_sentry()

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.create_db import create_db_and_tables
    await create_db_and_tables()
    yield
    
app = FastAPI(title=config.app_name, version=config.version, lifespan=lifespan)
app.include_router(posts.router, prefix="/api/v1/posts")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )