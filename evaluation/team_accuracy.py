# app/evaluation/hallucination_detector.py

class HallucinationDetector:

    def detect(
        self,
        answer,
        evidence
    ):

        answer_words = set(
            answer.lower().split()
        )

        evidence_words = set(
            evidence.lower().split()
        )

        overlap = len(
            answer_words.intersection(
                evidence_words
            )
        )

        score = overlap / max(
            len(answer_words),
            1
        )

        return {
            "score": round(score, 2),
            "passed": score > 0.3
        }