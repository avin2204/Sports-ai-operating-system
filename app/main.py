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

from app.api.ask import (
    router as ask_router
)

from app.api.ingestion import (
    router as ingestion_router
)

from app.api.task_status import (
    router as task_router
)

from app.api.qdrant_stats import (
    router as qdrant_router
)

from app.api.session import (
    router as session_router
)

from app.api.chat_history import (
    router as history_router
)

print("AVIN TEST 123")

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
    ingestion_router
)

app.include_router(
    task_router
)

app.include_router(
    ask_router
)

app.include_router(
    qdrant_router
)

app.include_router(
    session_router
)

app.include_router(
    history_router
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