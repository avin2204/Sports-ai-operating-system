from fastapi import APIRouter

from app.services.document_filter_service import (
    DocumentFilterService
)

router = APIRouter(

    prefix="/documents",

    tags=["Documents"]
)

service = (
    DocumentFilterService()
)


@router.get("/filter")
def filter_documents(
    file_type: str
):

    return (
        service.filter_by_type(
            file_type
        )
    )