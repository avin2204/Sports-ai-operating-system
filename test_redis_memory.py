from app.memory.redis_memory import (
    RedisMemory
)

memory = RedisMemory()

memory.save_memory(
    "avin",
    "favorite_team",
    "Arsenal"
)

result = memory.get_memory(
    "avin"
)

print(result)

