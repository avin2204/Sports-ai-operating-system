from fastapi import APIRouter

from app.services.llm_service import LLMService


router = APIRouter()

llm_service = LLMService()


@router.get("/ask")
def ask_ai(question: str):

    response = llm_service.ask(
        question
    )

    return {
        "response": response
    }