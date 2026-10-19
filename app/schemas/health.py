"""Schemas for the health check endpoint."""

from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response."""

    status: Literal["ok"]
    app_name: str
    version: str
    environment: str
