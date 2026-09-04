from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health_check() -> dict:
    """Return application health information."""

    return {
        "status": "healthy",
        "service": "agentic-rag-assistant",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }