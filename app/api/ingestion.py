import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.tasks.ingestion_task import (
    ingest_document_task
)

from app.models.ingestion_response import (
    IngestionResponse
)
print("INGESTION ROUTER LOADED")
router = APIRouter(
    prefix="/ingestion",
    tags=["Ingestion"]
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post(
    "/upload",
    response_model=IngestionResponse
)
async def upload_document(

    file: UploadFile = File(...)
):

    file_path = os.path.join(

        UPLOAD_DIR,

        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    task = (
        ingest_document_task.delay(
            file_path
        )
    )

    return IngestionResponse(

        task_id=task.id,

        status="queued",

        message=
        "Document uploaded successfully"
    )
