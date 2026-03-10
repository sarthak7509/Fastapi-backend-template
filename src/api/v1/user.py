from fastapi import APIRouter, Depends, HTTPException
from src.api.deps import get_db
from src.schema.user import UserCreate, UserOut, UserCreateOut
from src.service.user_repository import UserRepository
from src.security.hash import hash_password
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix='/v1/user')

@router.post("/", response_model=UserCreateOut)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await UserRepository.get_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail= " Email already Exisits")
    user = await UserRepository.create_user(
        db,
        {
            "email": payload.email,
            "hashed_password": hash_password(payload.password)
        }
    )
    return user

@router.get("/", response_model=list[UserOut])
async def get_user(skip: int=0, limit: int=0, db: AsyncSession = Depends(get_db)):
    return await UserRepository.get_users(db, skip, limit)

@router.delete("/{user_id}", response_model=UserCreateOut)
async def delete_user(user_id:int, db: AsyncSession= Depends(get_db)):
    return await UserRepository.delete_user(db, user_id)