from fastapi import APIRouter

from app.api.player_similarity import (
    PlayerSimilarity
)

router = APIRouter()


@router.get(
    "/player-similarity"
)
def compare():

    service = PlayerSimilarity()

    return service.compare(

        "Virat Kohli",

        "Rohit Sharma"
    )