from typing import TypedDict, List, Dict


class EnterpriseState(TypedDict):

    question: str

    retrieved_chunks: List[str]

    player_findings: List[str]

    team_findings: List[str]

    statistics_findings: Dict

    prediction_result: Dict

    review_notes: List[str]

    final_report: str

    injury_findings: list

    transfer_findings: list

    scouting_findings: list

    commentary: str

    player_rankings: list

    team_rankings: list

    fantasy_team: list

    match_prediction: str