# app/evaluation/evaluate_workflow.py

from evaluation.player_accuracy import (
    LLMJudge
)

from app.evaluation.hallucination_detector import (
    HallucinationDetector
)


def evaluate(
    answer,
    evidence
):

    judge = LLMJudge()

    hallucination = (
        HallucinationDetector()
    )

    judge_result = judge.evaluate(
        answer,
        evidence
    )

    hallucination_result = (
        hallucination.detect(
            answer,
            evidence
        )
    )

    return {
        "judge": judge_result,
        "hallucination":
            hallucination_result
    }