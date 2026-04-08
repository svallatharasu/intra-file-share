from datetime import datetime, UTC
from typing import List
from .base import Base

from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    created_by_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Relationships (derived from diagram image_2.png)
    owner: Mapped["User"] = relationship(back_populates="groups_created")
    posts: Mapped[List["Post"]] = relationship(back_populates="group")
    
    # N:M with User (via Association table)
    memberships: Mapped[List["GroupMembership"]] = relationship(back_populates="group")