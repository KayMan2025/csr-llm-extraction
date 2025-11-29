import json
from typing import Any, Dict

from .prompts import build_extraction_user_prompt, build_extraction_system_prompt
from .llm_client import chat_completion


def _extract_json_from_text(text: str) -> str:
    """
    Try to pull a clean JSON string out of an LLM response that may contain
    markdown fences like ```json ... ``` or other extra text.
    """
    stripped = text.strip()

    # If it uses markdown fences, strip them
    if stripped.startswith("```"):
        # Remove leading and trailing ```...``` blocks
        # e.g. ```json\n{...}\n```  ->  {...}
        lines = stripped.splitlines()
        # Drop first and last line if they start/end with ```
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()

    # Now try to find the JSON object between the first '{' and last '}'
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start != -1 and end != -1 and end > start:
        return stripped[start : end + 1]

    # If we can't locate it, just return the original text and let json.loads fail
    return stripped


def extract_structured_csr(
    csr_text: str,
    model: str = "llama-3.1-8b-instant",  # Groq LLaMA 3.1 model
) -> Dict[str, Any]:
    system = build_extraction_system_prompt()
    user = build_extraction_user_prompt(csr_text)

    raw = chat_completion(
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        model=model,
    )

    # First, try to parse the raw output directly
    try:
        return json.loads(raw)
    except Exception:
        pass

    # If that fails, try to clean it up (strip ```json fences, etc.)
    cleaned = _extract_json_from_text(raw)
    try:
        return json.loads(cleaned)
    except Exception:
        # If all parsing attempts fail, keep the raw text for debugging
        return {"_raw_output": raw}

