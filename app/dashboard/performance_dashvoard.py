import pandas as pd


class PerformanceDashboard:

    def build(self):

        return pd.DataFrame(
            [
                {
                    "agent":"player",
                    "avg_latency":0.45
                },
                {
                    "agent":"team",
                    "avg_latency":0.33
                }
            ]
        )