class CostTracker:

    def estimate(

        self,

        prompt_tokens,

        completion_tokens

    ):

        total = (
            prompt_tokens
            +
            completion_tokens
        )

        return round(
            total * 0.00001,
            4
        )