from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.db.database import Base


class QdrantMapping(Base):

    __tablename__ = "qdrant_mappings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_id = Column(
        Integer,
        nullable=False
    )

    qdrant_point_id = Column(
        String,
        nullable=False
    )