from app.db.session import (
    SessionLocal
)

from app.db.models.qdrant_mapping import (
    QdrantMapping
)

from app.db.repositories.qdrant_mapping_repository import (
    QdrantMappingRepository
)


class QdrantMappingService:

    def __init__(self):

        self.repository = (
            QdrantMappingRepository()
        )

    def create_mapping(

        self,

        document_id: int,

        qdrant_point_id: str
    ):

        db = SessionLocal()

        mapping = QdrantMapping(

            document_id=
            document_id,

            qdrant_point_id=
            qdrant_point_id
        )

        result = (
            self.repository.create(
                db,
                mapping
            )
        )

        db.close()

        return result