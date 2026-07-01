from fastapi import APIRouter

from app.services.document_delete_service import (
    DocumentDeleteService
)

router = APIRouter(

    prefix="/documents",

    tags=["Documents"]
)

service = (
    DocumentDeleteService()
)


@router.delete("/{document_id}")
def delete_document(
    document_id: int
):

    return {

        "deleted":

        service.delete(
            document_id
        )
    }