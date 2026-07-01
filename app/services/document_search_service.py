from app.db.session import (
    SessionLocal
)

from app.db.repositories.document_search_repository import (
    DocumentSearchRepository
)


class DocumentSearchService:

    def __init__(self):

        self.repository = (
            DocumentSearchRepository()
        )

    def search(
        self,
        keyword: str
    ):

        db = SessionLocal()

        results = (
            self.repository.search(
                db,
                keyword
            )
        )

        db.close()

        return results