import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from manus_client import create_task, show_result


task_content = """
Complete Task 2: Tool Design and Function Calling.

An agent has three tools:

1. search_orders
2. issue_refund
3. send_email

The agent keeps calling issue_refund before checking whether
the order actually qualifies.

Analyze the problem.

Explain:

1. What could be wrong with the tool descriptions.
2. Why the agent may select issue_refund too early.
3. How tool preconditions should be described.
4. How search_orders should be required before issue_refund.
5. How structured function arguments can reduce errors.
6. How application-level validation can prevent invalid refunds.
7. How guardrails can prevent dangerous tool calls.
8. When human confirmation should be required.

Design improved tool definitions for:

search_orders
issue_refund
send_email

Focus on safe and reliable function calling.
"""


result = create_task(
    "Task 2 - Tool Design and Function Calling",
    task_content
)

show_result(result)