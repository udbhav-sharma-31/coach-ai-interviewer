import json
import re

import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3:4b"


def ask_local_llm(prompt: str, system_prompt: str = "") -> str:
    """
    Send a prompt to the locally running Qwen model through Ollama.
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "/no_think\n" + system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "stream": False,
        "think": False,
        "options": {
            "num_predict": 400,
            "num_ctx": 4096,
            "temperature": 0.2,
        },
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=90,
    )

    response.raise_for_status()

    data = response.json()

    result = data["message"]["content"]

    if "</think>" in result:
        result = result.split("</think>", 1)[1].strip()

    return result.strip()


def _extract_json(text: str) -> str:
    """
    Extract the first complete JSON object or JSON array from model output.
    """

    text = text.strip()

    # Already valid JSON.
    try:
        json.loads(text)
        return text
    except json.JSONDecodeError:
        pass

    # Remove markdown code fences if Qwen added them.
    text = re.sub(r"```json\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```\s*", "", text)

    text = text.strip()

    # Try again after removing code fences.
    try:
        json.loads(text)
        return text
    except json.JSONDecodeError:
        pass

    # Find a JSON object.
    object_start = text.find("{")

    if object_start != -1:
        depth = 0
        in_string = False
        escape = False

        for index in range(object_start, len(text)):
            char = text[index]

            if escape:
                escape = False
                continue

            if char == "\\" and in_string:
                escape = True
                continue

            if char == '"':
                in_string = not in_string
                continue

            if in_string:
                continue

            if char == "{":
                depth += 1

            elif char == "}":
                depth -= 1

                if depth == 0:
                    candidate = text[object_start:index + 1]

                    try:
                        json.loads(candidate)
                        return candidate
                    except json.JSONDecodeError:
                        break

    # Find a JSON array as a fallback.
    array_start = text.find("[")

    if array_start != -1:
        depth = 0
        in_string = False
        escape = False

        for index in range(array_start, len(text)):
            char = text[index]

            if escape:
                escape = False
                continue

            if char == "\\" and in_string:
                escape = True
                continue

            if char == '"':
                in_string = not in_string
                continue

            if in_string:
                continue

            if char == "[":
                depth += 1

            elif char == "]":
                depth -= 1

                if depth == 0:
                    candidate = text[array_start:index + 1]

                    try:
                        json.loads(candidate)
                        return candidate
                    except json.JSONDecodeError:
                        break

    raise ValueError(
        "Local LLM did not return valid JSON.\n"
        f"Model output:\n{text}"
    )


def ask_local_llm_json(
    prompt: str,
    system_prompt: str = "",
    schema: dict | None = None,
) -> dict:
    """
    Send a prompt to Qwen through Ollama and return parsed JSON.

    The helper is tolerant of markdown fences or small amounts of
    surrounding model output while still requiring valid JSON.
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "/no_think\n" + system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "stream": False,
        "think": False,
        "format": schema or "json",
        "options": {
            "num_predict": 300,
            "num_ctx": 4096,
            "temperature": 0,
        },
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=False,
        timeout=90,
    )

    response.raise_for_status()

    data = response.json()

    content = data["message"]["content"]

    json_text = _extract_json(content)

    return json.loads(json_text)