from fastapi import APIRouter

from app.services.document_version_service import (
    DocumentVersionService
)

router = APIRouter(

    prefix="/versions",

    tags=["Document Versions"]
)

service = (
    DocumentVersionService()
)


@router.post("/")
def create_version(

    document_id: int,

    file_path: str,

    version: int
):

    return (

        service.create_version(

            document_id,

            file_path,

            version
        )
    )