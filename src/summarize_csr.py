from typing import Dict

from .prompts import build_summary_system_prompt, build_summary_user_prompt
from .llm_client import chat_completion


def summarize_csr(
    csr_text: str,
    model: str = "llama-3.1-8b-instant",  # Groq LLaMA 3.1 model
) -> Dict[str, str]:
    """
    Generate a concise summary of the Clinical Study Report (CSR)
    using a Groq-hosted LLaMA 3.1 model.
    """
    system = build_summary_system_prompt()
    user = build_summary_user_prompt(csr_text)

    output = chat_completion(
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        model=model,
        temperature=0.2,
    )

    return {"summary": output}

