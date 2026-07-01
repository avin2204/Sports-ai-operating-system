import os

from app.db.models.document import (
    Document
)

from app.db.repositories.document_repository import (
    DocumentRepository
)

from app.db.session import (
    SessionLocal
)


class DocumentRegistryService:

    def __init__(self):

        self.repository = (
            DocumentRepository()
        )

    def register(
        self,
        file_path: str
    ):

        db = SessionLocal()

        document = Document(

            filename=
            os.path.basename(
                file_path
            ),

            file_type=
            file_path.split(".")[-1],

            source_path=
            file_path
        )

        result = (
            self.repository.create(
                db,
                document
            )
        )

        db.close()

        return result
    