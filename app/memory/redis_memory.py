# app/memory/redis_memory.py

import redis
import json

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


class RedisMemory:

    def save_context(
        self,
        session_id,
        state
    ):

        redis_client.set(
            session_id,
            json.dumps(state),
            ex=86400
        )

    def load_context(
        self,
        session_id
    ):

        data = redis_client.get(session_id)

        if not data:
            return {}

        return json.loads(data)