import statistics


class DriftDetector:

    def detect(self, scores):

        if len(scores) < 10:
            return False

        baseline = statistics.mean(
            scores[:-5]
        )

        recent = statistics.mean(
            scores[-5:]
        )

        return recent < baseline * 0.85