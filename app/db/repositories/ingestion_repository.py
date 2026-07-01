from sqlalchemy.orm import Session

from app.db.models.ingestion_job import (
    IngestionJob
)


class IngestionRepository:

    def create(
        self,
        db: Session,
        job: IngestionJob
    ):

        db.add(
            job
        )

        db.commit()

        db.refresh(
            job
        )

        return job