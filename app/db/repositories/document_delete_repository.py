from sqlalchemy.orm import Session

from app.db.models.document import (
    Document
)


class DocumentDeleteRepository:

    def delete(
        self,
        db: Session,
        document_id: int
    ):

        document = (

            db.query(
                Document
            )

            .filter(
                Document.id ==
                document_id
            )

            .first()
        )

        if not document:

            return False

        db.delete(
            document
        )

        db.commit()

        return True