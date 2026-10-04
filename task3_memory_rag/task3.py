import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from manus_client import create_task, show_result


task_content = """
Complete Task 3: Memory vs RAG.

A support agent needs to:

A. Remember what the customer said earlier in the same chat.

B. Answer questions about a company's 40-page return policy.

Explain which requirement should use short-term conversation
memory and which should use RAG (Retrieval-Augmented Generation).

Explain:

1. What short-term memory is.
2. What RAG is.
3. Why conversation history belongs in short-term memory.
4. Why the return-policy document should use RAG.
5. Why using memory for the entire policy document is a poor
   approach.
6. Why using RAG for simple conversation history is unnecessary.
7. How memory and RAG can work together in one support agent.

Give a practical example.
"""


result = create_task(
    "Task 3 - Memory vs RAG",
    task_content
)

show_result(result)