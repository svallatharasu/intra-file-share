import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    """Configuration for the application."""
    app_name: str
    version: str
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int
    sentry_dsn: str
    environment: str
    debug: bool = False

    @property
    def db_url(self) -> str:
        """Construct the database URL."""
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    class Config:
        env_file = ".env" if os.getenv("ENV", "development") == "development" else None

# Singleton instance of the configuration
config = Config()