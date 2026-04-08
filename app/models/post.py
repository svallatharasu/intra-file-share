from .base import Base
from typing import List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_url: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(String(50), nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)

    # Relationships
    owner: Mapped["User"] = relationship(back_populates="posts_owned")
    group: Mapped["Group"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    reading_sessions: Mapped[List["ReadingSession"]] = relationship(back_populates="post")