import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from manus_client import create_task, show_result


task_content = """
Complete Task 5: Safety and Reliability.

An agent has access to:

- A company's internal knowledge base
- An email tool

The agent starts behaving unexpectedly after processing a
document containing hidden instructions.

Identify what likely happened.

Explain the specific agent safety risk involved.

Discuss prompt injection and indirect prompt injection.

Then propose TWO concrete guardrails that would limit the damage.

Consider:

1. Least-privilege tool access.
2. Human approval for sensitive actions.
3. Input/document trust boundaries.
4. Tool authorization.
5. Output validation.
6. Limiting the agent's ability to send emails automatically.

Explain exactly how each selected guardrail would reduce risk.

Focus on defensive engineering and reliability.
"""


result = create_task(
    "Task 5 - Safety and Reliability",
    task_content
)

show_result(result)