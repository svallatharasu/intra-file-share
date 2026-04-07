from fastapi import FastAPI

import uvicorn
from core.config import config
from core.logging import init_sentry
from api.v1 import posts

init_sentry()

app = FastAPI(title=config.app_name, version=config.version)
app.include_router(posts.router, prefix="/api/v1/posts")

@app.get("/err")

# --- Debugging Purpose ---
def trigger_error():
    raise ValueError("This is a test error")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )