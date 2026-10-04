import os
from dotenv import load_dotenv

load_dotenv()

MANUS_API_KEY = os.getenv("MANUS_API_KEY")

if not MANUS_API_KEY:
    raise ValueError(
        "MANUS_API_KEY not found. Please check your .env file."
    )

MANUS_API_URL = "https://api.manus.ai/v2"