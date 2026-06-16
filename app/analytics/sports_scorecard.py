class SportsScorecard:

    def calculate(

        self,

        prediction_accuracy,

        retrieval_score,

        groundedness_score

    ):

        final_score = round(

            (
                prediction_accuracy
                +
                retrieval_score
                +
                groundedness_score
            )
            / 3,

            2
        )

        return {

            "prediction_accuracy":
                prediction_accuracy,

            "retrieval_score":
                retrieval_score,

            "groundedness_score":
                groundedness_score,

            "final_score":
                final_score
        }