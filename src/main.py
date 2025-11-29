import argparse
import json
from pathlib import Path

from .extract_structured import extract_structured_csr
from .summarize_csr import summarize_csr


def main():
    parser = argparse.ArgumentParser(
        description="Extract structured data and summaries from a CSR text file using Groq LLM."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the input CSR text file",
    )
    # Optional override; if not provided, functions will use their own default model
    parser.add_argument(
        "--model",
        "-m",
        default=None,
        help="(Optional) Groq model name, e.g. 'llama3-8b-8192'",
    )

    args = parser.parse_args()

    csr_path = Path(args.input)
    if not csr_path.exists():
        raise FileNotFoundError(f"Input file not found: {csr_path}")

    text = csr_path.read_text(encoding="utf-8")

    if args.model:
        structured = extract_structured_csr(text, model=args.model)
        summary = summarize_csr(text, model=args.model)
    else:
        # Use defaults defined in each function (llama3-8b-8192)
        structured = extract_structured_csr(text)
        summary = summarize_csr(text)

    output = {
        "structured": structured,
        "summaries": summary,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
