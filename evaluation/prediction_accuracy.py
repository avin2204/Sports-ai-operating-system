# app/evaluation/agent_metrics.py

import time


class AgentMetrics:

    def start(self):
        return time.time()

    def stop(
        self,
        start_time
    ):
        return round(
            time.time() - start_time,
            3
        )