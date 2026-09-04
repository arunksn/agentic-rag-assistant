from fastapi import FastAPI

from configs.settings import settings
from app.api.routes.health import router as health_router


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""

    application = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        debug=settings.debug,
    )

    application.include_router(
        health_router,
        prefix=settings.api_v1_prefix,
    )

    return application


app = create_application()