from fastapi import FastAPI

import uvicorn
from app.core.config import config
from app.core.logging import init_sentry
from contextlib import asynccontextmanager
from app.api.v1 import posts, auth, users

init_sentry()

@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.models.create_db import create_db_and_tables
    await create_db_and_tables()
    yield
    
app = FastAPI(title=config.app_name, version=config.version, lifespan=lifespan)
app.include_router(posts.router, prefix="/api/v1/posts")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )