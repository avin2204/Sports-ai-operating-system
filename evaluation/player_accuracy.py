class LLMJudge:

    def evaluate(
        self,
        answer: str,
        evidence: str
    ):

        score = 0

        if len(answer) > 100:
            score += 3

        if len(evidence) > 100:
            score += 3

        if "root cause" in answer.lower():
            score += 2

        if "recommendation" in answer.lower():
            score += 2

        return {
            "score": score,
            "passed": score >= 7
        }