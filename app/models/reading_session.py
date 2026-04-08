from .base import Base

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ReadingSession(Base):
    __tablename__ = "reading_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    total_time_seconds: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relationships (derived from diagram image_3.png)
    user: Mapped["User"] = relationship(back_populates="reading_sessions")
    post: Mapped["Post"] = relationship(back_populates="reading_sessions")