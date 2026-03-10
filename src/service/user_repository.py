from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.model import User
class UserRepository:

    @staticmethod
    async def get_users(db: AsyncSession, skip: int=0, limit: int=10):
        stmt = (
            select(User)
            .options(selectinload(User.posts))
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(stmt)
        return result.scalars().unique().all()

    @staticmethod
    async def create_user(db: AsyncSession, data: dict):
        user = User(**data)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    
    @staticmethod
    async def get_by_email(db: AsyncSession, email: str):
        result = await db.execute(
            select(User).where(User.email==email)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, id: int):
        result = await db.execute(
            select(User).where(User.id==id)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def delete_user(db: AsyncSession, id: int):
        user = await UserRepository.get_by_id(db, id)
        if not user:
            return
        await db.delete(user)
        await db.commit()
        return user