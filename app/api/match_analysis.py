from fastapi import APIRouter

router = APIRouter()


@router.post("/match-analysis")
def analyze(payload: dict):

    chunks = payload.get(
        "chunks",
        []
    )

    result = {

        "goals": 0,

        "wickets": 0,

        "runs": 0
    }

    for chunk in chunks:

        text = chunk.lower()

        result["goals"] += text.count(
            "goal"
        )

        result["wickets"] += text.count(
            "wicket"
        )

        result["runs"] += text.count(
            "runs"
        )

    return result