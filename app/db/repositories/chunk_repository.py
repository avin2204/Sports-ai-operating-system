from sqlalchemy.orm import Session

from app.db.models.document_chunk import (
    DocumentChunk
)


class ChunkRepository:

    def create(
        self,
        db: Session,
        chunk: DocumentChunk
    ):

        db.add(
            chunk
        )

        db.commit()

        db.refresh(
            chunk
        )

        return chunk