import pandas as pd


class EvaluationDashboard:

    def build(self):

        return pd.DataFrame(

            [
                {
                    "metric":
                        "Groundedness",

                    "score":
                        91
                },

                {
                    "metric":
                        "Prediction Accuracy",

                    "score":
                        87
                },

                {
                    "metric":
                        "Retrieval Quality",

                    "score":
                        93
                }
            ]
        )