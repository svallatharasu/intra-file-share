from typing import Optional
from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    name: str
    organization: Optional[str] = None

class UserCreate(schemas.BaseUserCreate):
    name: str
    organization: Optional[str] = None

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str] = None
    organization: Optional[str] = None
