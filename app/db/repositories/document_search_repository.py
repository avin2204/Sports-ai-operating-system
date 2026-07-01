from sqlalchemy.orm import Session

from app.db.models.document import (
    Document
)


class DocumentSearchRepository:

    def search(
        self,
        db: Session,
        keyword: str
    ):

        return (

            db.query(
                Document
            )

            .filter(
                Document.filename.ilike(
                    f"%{keyword}%"
                )
            )

            .all()
        )