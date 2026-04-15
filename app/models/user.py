from .base import Base
from typing import List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyBaseOAuthAccountTable

class OAuthAccount(SQLAlchemyBaseOAuthAccountTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False)

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    organization: Mapped[str] = mapped_column(String(255), nullable=True)
    
    # OAuth Accounts
    oauth_accounts: Mapped[List["OAuthAccount"]] = relationship(
        "OAuthAccount", lazy="joined", cascade="all, delete"
    )
    
    groups_created: Mapped[List["Group"]] = relationship(back_populates="owner")
    
    # 1:M with Post (owner_id)
    posts_owned: Mapped[List["Post"]] = relationship(foreign_keys="Post.owner_id", back_populates="owner")
    
    # 1:M with Post (recipient_id) - direct shares
    posts_received: Mapped[List["Post"]] = relationship(foreign_keys="Post.recipient_id", back_populates="recipient")
    
    # 1:M with Comment (user_id)
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    
    # 1:M with ReadingSessions (user_id)
    reading_sessions: Mapped[List["ReadingSession"]] = relationship(back_populates="user")
    
    # N:M with Group (via Association table)
    memberships: Mapped[List["GroupMembership"]] = relationship(back_populates="user")

class GroupMembership(Base):
    __tablename__ = "group_memberships"
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    # Optional back-references to make it easier to traverse the connection
    user: Mapped["User"] = relationship(back_populates="memberships")
    group: Mapped["Group"] = relationship(back_populates="memberships")