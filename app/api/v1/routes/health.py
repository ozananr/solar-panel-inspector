"""Health check endpoint."""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check(
    settings: Annotated[Settings, Depends(get_settings)],
) -> HealthResponse:
    """Report that the API is running."""
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )
