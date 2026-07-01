from app.celery_app import celery

from app.services.ingestion_service import (
    IngestionService
)


@celery.task
def ingest_document_task(
    file_path: str
):

    service = (
        IngestionService()
    )

    return service.ingest(
        file_path
    )