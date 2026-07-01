class PromptService:

    def build_prompt(
        self,
        question: str,
        context: str
    ):

        return f"""
You are a sports analyst.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""