from fastapi import FastAPI

from app.api.player_analysis import (
    router as player_router
)

from app.api.team_comparison import (
    router as team_router
)

from app.api.match_analysis import (
    router as match_router
)

from app.api.rag import (
    router as rag_router
)


app = FastAPI(
    title="Sports Enterprise AI OS"
)


app.include_router(
    player_router,
    prefix="/api"
)

app.include_router(
    team_router,
    prefix="/api"
)

app.include_router(
    match_router,
    prefix="/api"
)

app.include_router(
    rag_router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "message": "Sports Enterprise AI OS Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }