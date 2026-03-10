"""
Application configuration holder
Version: 1.0
Author
    Sarthak Bhatnagar
"""
import sys
from fastapi import FastAPI
from .core import logger
from .db.base import Base
from .db.session import engine
from .api.v1.user import router as user_router
from .api.v1.posts import router as post_router
from contextlib import asynccontextmanager


# Base.metadata.create_all(bind=engine)
# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await init_models()
    yield
app = FastAPI(lifespan=lifespan)

# Add routers
app.include_router(user_router)
app.include_router(post_router)

# Export the app
__all__ = [
    app
]