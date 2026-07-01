from app.db.session import (
    SessionLocal
)

from app.db.repositories.document_delete_repository import (
    DocumentDeleteRepository
)


class DocumentDeleteService:

    def __init__(self):

        self.repository = (
            DocumentDeleteRepository()
        )

    def delete(
        self,
        document_id: int
    ):

        db = SessionLocal()

        result = (
            self.repository.delete(
                db,
                document_id
            )
        )

        db.close()

        return result