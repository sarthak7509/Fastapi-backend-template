from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from src.api.deps import get_db
from src.service.post_respository import PostRepository
from src.schema.posts import PostCreate, PostOut

router = APIRouter(prefix="/v1")

@router.post("/{user_id}/post", response_model=PostOut)
async def create_post(user_id: int, payload: PostCreate, db: AsyncSession = Depends(get_db)):
    post = await PostRepository.create(
        db,
        {
            "title": payload.title,
            "user_id": user_id
        }
    )
    return post

@router.get("/posts", response_model=list[PostOut])
async def get_post(skip:int, limit:int=10, db: AsyncSession = Depends(get_db)):
    return await PostRepository.get_posts(db, skip, limit)