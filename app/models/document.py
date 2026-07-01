from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.db.session import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    file_name = Column(
        String,
        nullable=False
    )

    source = Column(
        String,
        nullable=False
    )

    document_type = Column(
        String,
        nullable=True
    )

    version = Column(
        Integer,
        default=1
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )