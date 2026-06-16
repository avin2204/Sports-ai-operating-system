from fastapi import APIRouter

from app.analytics.player_performance import (
    PlayerPerformanceAnalyzer
)

router = APIRouter()


@router.post("/player-analysis")
def player_analysis(payload: dict):

    chunks = payload.get(
        "chunks",
        []
    )

    analyzer = (
        PlayerPerformanceAnalyzer()
    )

    return analyzer.analyze(
        chunks
    )