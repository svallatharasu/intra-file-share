import sentry_sdk
from core.config import config
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

def init_sentry():
    """Initialize Sentry for error tracking."""
    
    if not config.sentry_dsn:
        return

    environment = "development" if config.environment else "production"
    
    sentry_sdk.init(
        dsn=config.sentry_dsn,
        environment=environment,
        integrations=[FastApiIntegration(), SqlalchemyIntegration()],
        traces_sample_rate=2.0,
        profiles_sample_rate=0.0,
        send_default_pii=True # Only in Production
    )