from fastapi import APIRouter, Depends
from .auth import fastapi_users, current_active_user
from schemas.users import UserRead, UserUpdate
from models.user import User

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    tags=["users"],
)

@router.get("/search")
def search_users(query: str, user: User = Depends(current_active_user)):
    pass

@router.get("/sidebar")
def get_user_sidebar_api(user: User = Depends(current_active_user)):
    pass
