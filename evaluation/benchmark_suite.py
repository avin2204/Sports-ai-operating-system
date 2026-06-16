class BenchmarkSuite:

    def evaluate(

        self,

        retrieval,

        groundedness,

        prediction

    ):

        score = round(

            (
                retrieval
                +
                groundedness
                +
                prediction
            )
            / 3,

            2
        )

        return {

            "benchmark_score":
                score
        }