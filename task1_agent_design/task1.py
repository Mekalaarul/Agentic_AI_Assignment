import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from manus_client import create_task, show_result


task_content = """
Complete Task 1: Agent Design.

A company wants to replace its FAQ chatbot with an agent that
can resolve customer issues such as checking order status,
issuing refunds, and escalating to a human.

Design the system using the:

Perceive → Reason → Plan → Act → Observe

agent loop.

Explain how the new agent differs from a traditional FAQ chatbot.

Then apply all five stages to this example:

"Customer wants to process a refund."

Explain:
- What the agent perceives
- What it reasons about
- What plan it creates
- What actions it takes
- What it observes after the action
- When it should escalate to a human

Provide a clear engineering explanation.
"""


result = create_task(
    "Task 1 - Agent Design",
    task_content
)

show_result(result)