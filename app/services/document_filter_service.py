from app.db.session import (
    SessionLocal
)

from app.db.models.document import (
    Document
)


class DocumentFilterService:

    def filter_by_type(
        self,
        file_type: str
    ):

        db = SessionLocal()

        results = (

            db.query(
                Document
            )

            .filter(
                Document.file_type ==
                file_type
            )

            .all()
        )

        db.close()

        return results