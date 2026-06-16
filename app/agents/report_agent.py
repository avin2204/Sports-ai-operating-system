def report_agent(state):

    prompt = f"""
Question:
{state['question']}

Root Cause:
{state['root_cause']}

Review:
{state['review_notes']}

Generate final report.
"""

    answer = llm_service.generate(prompt)

    state["final_report"] = answer

    return state