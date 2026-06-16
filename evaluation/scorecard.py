class EvaluationScorecard:

    def build(
        self,
        relevance,
        groundedness,
        completeness
    ):

        final_score = round(
            (
                relevance
                + groundedness
                + completeness
            ) / 3,
            2
        )

        return {
            "relevance": relevance,
            "groundedness": groundedness,
            "completeness": completeness,
            "final_score": final_score
        }