from sqlalchemy.orm import Session

from app.db.models.qdrant_mapping import (
    QdrantMapping
)


class QdrantMappingRepository:

    def create(
        self,
        db: Session,
        mapping: QdrantMapping
    ):

        db.add(mapping)

        db.commit()

        db.refresh(mapping)

        return mapping