from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from httpx_oauth.clients.google import GoogleOAuth2
from core.config import config

from models.user import User
from core.user_manager import get_user_manager
from core.security import auth_backend
from schemas.users import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

if config.google_oauth_client_id and config.google_oauth_client_secret:
    google_oauth_client = GoogleOAuth2(
        config.google_oauth_client_id,
        config.google_oauth_client_secret
    )
    router.include_router(
        fastapi_users.get_oauth_router(
            google_oauth_client,
            auth_backend,
            config.secret_key,
            associate_by_email=True,
            is_verified_by_default=True,
        ),
        prefix="/google",
        tags=["auth"],
    )

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)
