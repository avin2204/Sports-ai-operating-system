from fastapi import APIRouter

from app.analytics.team_rankings import (
    TeamRankings
)

router = APIRouter()


@router.post("/team-comparison")
def compare(payload: dict):

    chunks = payload.get(
        "chunks",
        []
    )

    ranking = TeamRankings()

    return ranking.rank(
        chunks
    )