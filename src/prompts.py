from .config import CSR_SCHEMA

def build_extraction_system_prompt():
    return (
        "You are a clinical trial expert. "
        "Extract structured fields accurately. "
        "Return ONLY valid JSON."
    )

def build_extraction_user_prompt(csr_text: str):
    fields = "\n".join(
        [f'"{f.name}": "{f.description}"' for f in CSR_SCHEMA]
    )

    return f"""
Extract the following fields as JSON:

{fields}

CSR TEXT:
\"\"\"{csr_text}\"\"\"
"""

def build_summary_system_prompt():
    return "You are a medical writer producing plain and technical summaries."

def build_summary_user_prompt(csr_text: str):
    return f"""
Write:

1. Plain language summary
2. Technical summary for clinicians

CSR TEXT:
\"\"\"{csr_text}\"\"\"
"""
