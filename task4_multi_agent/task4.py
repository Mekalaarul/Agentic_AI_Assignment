import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from manus_client import create_task, show_result


task_content = """
Complete Task 4: Multi-Agent Architecture.

A marketing team wants an agent system that can:

1. Research a competitor.
2. Draft a comparison blog post.
3. Fact-check the draft.
4. Publish the article after approval.

Design a multi-agent architecture.

Use a pipeline architecture:

Research Agent
       ↓
Writing Agent
       ↓
Fact-Checking Agent
       ↓
Human Approval
       ↓
Publishing

For each agent explain:

- Role
- Input
- Processing
- Output
- What is handed to the next agent

Explain what happens when the fact-checking agent discovers
an error.

Clearly identify the human checkpoint and explain why it should
exist before publication.

Include an ASCII architecture diagram.
"""


result = create_task(
    "Task 4 - Multi-Agent Architecture",
    task_content
)

show_result(result)