from app.providers.gemini_provider import (
    GeminiProvider
)

provider = GeminiProvider()

answer = provider.generate(
    "Who is Virat Kohli?"
)

print("\nAnswer:\n")
print(answer)