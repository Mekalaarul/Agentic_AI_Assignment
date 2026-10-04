import requests

from config import MANUS_API_KEY, MANUS_API_URL


def create_task(title, content):

    url = f"{MANUS_API_URL}/task.create"

    headers = {
        "Content-Type": "application/json",
        "x-manus-api-key": MANUS_API_KEY
    }

    data = {
        "message": {
            "content": content
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

    return response.json()


def show_result(result):

    print("\n====================================")
    print("Task created successfully")
    print("====================================")
    print("Task ID :", result.get("task_id"))
    print("Task URL:", result.get("task_url"))
    print("====================================")