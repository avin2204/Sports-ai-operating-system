from fastapi import APIRouter

from app.services.memory_service import (
    MemoryService
)

router = APIRouter(
    prefix="/history",
    tags=["Memory"]
)

service = (
    MemoryService()
)


@router.get("/{session_id}")
def history(
    session_id: str
):

    return service.history(
        session_id
    )