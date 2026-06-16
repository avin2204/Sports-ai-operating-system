from app.providers.gemini_provider import GeminiProvider


class LLMService:

    def __init__(self):

        self.provider = GeminiProvider()

    def ask(self, prompt: str) -> str:

        return self.provider.generate(
            prompt
        )