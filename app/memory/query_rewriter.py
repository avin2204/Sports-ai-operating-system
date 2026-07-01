class QueryRewriter:

    def rewrite(
        self,
        question: str,
        history: list
    ):

        if not history:

            return question

        recent = history[-4:]

        context = " ".join(
            item["content"]
            for item in recent
        )

        return (
            context
            + " "
            + question
        )