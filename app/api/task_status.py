from fastapi import APIRouter

from app.tasks.ingestion_task import (
    ingest_document_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/{task_id}")
def get_task_status(
    task_id: str
):

    task = (
        ingest_document_task.AsyncResult(
            task_id
        )
    )

    return {

        "task_id":
        task.id,

        "status":
        task.status,

        "result":
        task.result
    }