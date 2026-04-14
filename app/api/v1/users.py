from fastapi import APIRouter
from .auth import fastapi_users
from schemas.users import UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    tags=["users"],
)
