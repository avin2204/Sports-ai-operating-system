from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.db.database import Base


class DocumentVersion(Base):

    __tablename__ = "document_versions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    version = Column(
        Integer,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )