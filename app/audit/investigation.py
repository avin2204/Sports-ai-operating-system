# app/audit/investigation_store.py

from sqlalchemy.orm import Session
from app.db.models import Investigation


class InvestigationStore:

    def save(
        self,
        db: Session,
        question: str,
        root_cause: str,
        report: str
    ):

        investigation = Investigation(
            question=question,
            root_cause=root_cause,
            report=report
        )

        db.add(investigation)
        db.commit()

        return investigation.id