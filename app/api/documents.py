from fastapi import APIRouter

from app.db.session import (
    SessionLocal
)

from app.db.models.document import (
    Document
)

router = APIRouter(

    prefix="/documents",

    tags=["Documents"]
)


@router.get("/")
def list_documents():

    db = SessionLocal()

    documents = (

        db.query(
            Document
        ).all()
    )

    result = [

        {
            "id":
            doc.id,

            "filename":
            doc.filename,

            "file_type":
            doc.file_type,

            "source_path":
            doc.source_path
        }

        for doc in documents
    ]

    db.close()

    return result