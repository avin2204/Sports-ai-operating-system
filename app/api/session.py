from fastapi import APIRouter

from app.memory.session_manager import (
    SessionManager
)

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"]
)


@router.post("/")
def create_session():

    return {

        "session_id":

        SessionManager.create_session()
    }
