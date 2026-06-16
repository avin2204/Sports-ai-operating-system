import pandas as pd


class AgentMetricsDashboard:

    def build(self):

        return pd.DataFrame(

            [
                {
                    "agent": "retrieval",
                    "runtime": 1.2
                },

                {
                    "agent": "player",
                    "runtime": 0.7
                },

                {
                    "agent": "prediction",
                    "runtime": 0.4
                }
            ]
        )