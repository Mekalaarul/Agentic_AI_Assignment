import requests
from config import MANUS_API_KEY, MANUS_API_URL


def create_task(prompt, title):
    url = f"{MANUS_API_URL}/task.create"

    headers = {
        "Content-Type": "application/json",
        "x-manus-api-key": MANUS_API_KEY,
    }

    data = {
        "message": {
            "content": prompt
        },
        "title": title,
        "share_visibility": "private"
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    return result


if __name__ == "__main__":

    prompt = """
You are an Agentic AI engineering assistant.

Explain the following concept in a simple engineering-student
friendly way:

What is an AI agent?
Explain:
1. Perceive
2. Reason
3. Plan
4. Act
5. Observe

Give one simple real-world example.
"""

    print("Creating Manus task...")

    result = create_task(
        prompt,
        "Agentic AI Basic Test"
    )

    print("\nTask created successfully!")
    print("--------------------------------")
    print("Task ID :", result.get("task_id"))
    print("Task URL:", result.get("task_url"))
    print("--------------------------------")