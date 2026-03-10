from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import Post

class PostRepository:

    @staticmethod
    async def create(db: AsyncSession, data: dict):
        post = Post(**data)
        db.add(post)
        await db.commit()
        await db.refresh(post)
        return post

    @staticmethod
    async def get_by_user(db: AsyncSession, user_id: str):
        result = await db.execute(
            select(Post).where(Post.id==user_id)
        )
        return result.scalars().all()
    
    async def get_posts(db: AsyncSession, skip:int=0, limit:int=10):
        stmt = (
            select(Post).offset(skip).limit(limit=limit)
        )
        result = await db.execute(stmt)
        return result.scalars().unique().all()

