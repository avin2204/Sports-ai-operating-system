from fastapi import APIRouter

from app.analytics.team_similarity import (
    TeamSimilarity
)

router = APIRouter()


@router.get(
    "/team-similarity"
)
def compare():

    service = TeamSimilarity()

    return service.compare(

        "India",

        "Australia"
    )