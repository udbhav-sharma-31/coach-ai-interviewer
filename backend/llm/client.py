import os

from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()


MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


def ask_llm(message: str, system_prompt: str = "") -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is not set")

    with OpenRouter(api_key=api_key) as client:
        response = client.chat.send(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("LLM returned an empty response")

    return content.strip()
