from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from .config import config

bearer_transport = BearerTransport(tokenUrl="api/v1/auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=config.secret_key, 
        lifetime_seconds=config.jwt_lifetime_seconds
    )

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
