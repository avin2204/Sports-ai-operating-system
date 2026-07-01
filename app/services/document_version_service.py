from app.db.session import (
    SessionLocal
)

from app.db.models.document_version import (
    DocumentVersion
)


class DocumentVersionService:

    def create_version(

        self,

        document_id: int,

        file_path: str,

        version: int
    ):

        db = SessionLocal()

        obj = DocumentVersion(

            document_id=
            document_id,

            file_path=
            file_path,

            version=
            version
        )

        db.add(
            obj
        )

        db.commit()

        db.refresh(
            obj
        )

        db.close()

        return obj