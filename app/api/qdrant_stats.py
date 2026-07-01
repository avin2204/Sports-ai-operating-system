from fastapi import APIRouter

from qdrant_client import (
    QdrantClient
)

router = APIRouter(

    prefix="/qdrant",

    tags=["Qdrant"]
)


@router.get("/stats")
def stats():

    client = QdrantClient(
        host="localhost",
        port=6333
    )

    return client.get_collection(
        "sports_docs"
    )