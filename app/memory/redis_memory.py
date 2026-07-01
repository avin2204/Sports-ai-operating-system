import json

import redis

from app.memory.base_memory import (
    BaseMemory
)


class RedisMemory(
    BaseMemory
):

    def __init__(self):

        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def save(
        self,
        session_id,
        role,
        content
    ):

        self.redis.rpush(

            f"chat:{session_id}",

            json.dumps(
                {
                    "role": role,
                    "content": content
                }
            )
        )

    def get_history(
        self,
        session_id
    ):

        data = self.redis.lrange(
            f"chat:{session_id}",
            0,
            -1
        )

        return [
            json.loads(item)
            for item in data
        ]