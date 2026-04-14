from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import uvicorn
from core.config import config
from core.logging import init_sentry
from contextlib import asynccontextmanager
from api.v1 import posts, auth, users


init_sentry()

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.create_db import create_db_and_tables
    await create_db_and_tables()
    yield
    
app = FastAPI(title=config.app_name, version=config.version, lifespan=lifespan)

# --- Security Middlewares ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Restrict this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"]) # TODO: Restrict in production

# --- Rate Limiting ---
limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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