from agents import developer_agent, qa_agent, reviewer_agent

MAX_ITERATIONS = 3

def multi_agent_pipeline(user_query: str):

    # Step 1: Developer writes initial code
    developer_output = developer_agent.run(user_query).content
    current_code = developer_output

    for iteration in range(MAX_ITERATIONS):

        # Step 2: QA fixes bugs
        qa_output = qa_agent.run(current_code).content

        # Step 3: Reviewer validates logic
        review_output = reviewer_agent.run(qa_output).content

        # If approved, return final result
        if "approved" in review_output.lower():
            return {
                "final_code": qa_output,
                "review_feedback": review_output,
                "iterations": iteration + 1,
                "full_text": f"""
==============================
USER QUERY
==============================
{user_query}

==============================
FINAL CODE
==============================
{qa_output}

==============================
REVIEWER FEEDBACK
==============================
{review_output}
"""
            }

        # Feedback loop
        current_code = f"""
Reviewer feedback:
{review_output}

Improve the following code accordingly:
{qa_output}
"""

    # Fallback if max iterations reached
    return {
        "final_code": current_code,
        "review_feedback": "Max iterations reached. Final version returned.",
        "iterations": MAX_ITERATIONS,
        "full_text": f"""
==============================
USER QUERY
==============================
{user_query}

==============================
FINAL CODE
==============================
{current_code}

==============================
REVIEW STATUS
==============================
Max iterations reached.
"""
    }
