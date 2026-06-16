class PromptBuilder:

    def build(
        self,
        question: str,
        contexts: list
    ) -> str:

        context_text = "\n\n".join(
            [
                item["text"]
                for item in contexts
            ]
        )

        prompt = f"""
You are a helpful AI assistant.

Use the provided context to answer the question.

Context:
{context_text}

Question:
{question}

Answer:
"""

        return prompt