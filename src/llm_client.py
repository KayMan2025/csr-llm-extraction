import os
from typing import List

from dotenv import load_dotenv
from groq import Groq

# Load .env and override any existing environment vars
load_dotenv(override=True)


def get_groq_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Check your .env file.")
    return Groq(api_key=api_key)


def chat_completion(messages: List[dict], model: str, temperature: float = 0.0) -> str:
    """
    Thin wrapper around Groq chat completions.
    """
    client = get_groq_client()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content


