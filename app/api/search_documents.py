from fastapi import APIRouter

from app.services.document_search_service import (
    DocumentSearchService
)

router = APIRouter(

    prefix="/documents",

    tags=["Documents"]
)

service = (
    DocumentSearchService()
)


@router.get("/search")
def search_documents(
    keyword: str
):

    return (
        service.search(
            keyword
        )
    )