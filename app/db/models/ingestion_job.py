from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.sql import func

from app.db.database import Base


class IngestionJob(Base):

    __tablename__ = "ingestion_jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    task_id = Column(
        String,
        unique=True
    )

    status = Column(
        String
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )