class RetrievalEvaluator:

    def evaluate(
        self,
        expected,
        retrieved
    ):

        overlap = len(
            set(expected)
            &
            set(retrieved)
        )

        return overlap / len(expected)