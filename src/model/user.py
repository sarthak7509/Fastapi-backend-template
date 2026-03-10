from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import String, Boolean, DateTime, func
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(
        String[255],
        unique=True,
        index=True,
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    posts: Mapped[list["Post"]] = Relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )