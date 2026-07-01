from fastapi import APIRouter

from app.models.ask_request import AskRequest
from app.services.ask_service import AskService

router = APIRouter(
    prefix="/api",
    tags=["RAG"]
)

service = AskService()


@router.post("/ask")
def ask_question(
    request: AskRequest
):

    return service.ask(
        request.question
    )