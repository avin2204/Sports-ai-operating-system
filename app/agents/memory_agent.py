from app.memory.redis_memory import (
    RedisMemory
)


def memory_agent(state):

    memory_store = RedisMemory()

    user_id = state.get(
        "user_id",
        "avin"
    )

    question = state["question"]

    existing_memory = (
        memory_store.get_memory(
            user_id
        )
    )

    if (
        "favorite team is"
        in question.lower()
    ):

        team = (
            question.split("is")[-1]
            .strip()
        )

        memory_store.save_memory(
            user_id,
            "favorite_team",
            team
        )

        existing_memory[
            "favorite_team"
        ] = team

        print(
            f"\nMEMORY SAVED: {team}"
        )

    print(
        "\nMEMORY LOADED:",
        existing_memory
    )

    return {
        "memory":
        existing_memory
    }