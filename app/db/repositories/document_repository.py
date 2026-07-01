from sqlalchemy.orm import Session

from app.db.models.document import (
    Document
)


class DocumentRepository:

    def create(
        self,
        db: Session,
        document: Document
    ):

        db.add(
            document
        )

        db.commit()

        db.refresh(
            document
        )

        return document

    def get_all(
        self,
        db: Session
    ):

        return db.query(
            Document
        ).all()