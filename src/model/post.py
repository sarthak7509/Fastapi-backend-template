from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import String, ForeignKey

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String[255])

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["User"] = Relationship(back_populates="posts")