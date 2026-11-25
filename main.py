#!/usr/bin/env python3
"""Write a concise, self-contained commit subject to the judged artifact."""

import os
from pathlib import Path

SUBJECT = "fix: stopped the leak by giving every bug a bigger bucket"
OUTPUT_NAME = "entry.txt"
MAX_SUBJECT_CHARS = 100


def validate_subject(subject):
    if not subject or subject.isspace():
        raise ValueError("subject must not be blank")
    if len(subject) > MAX_SUBJECT_CHARS:
        raise ValueError(f"subject must be at most {MAX_SUBJECT_CHARS} characters")
    if "\n" in subject or "\r" in subject:
        raise ValueError("subject must be exactly one line")
    return subject


def main():
    subject = validate_subject(SUBJECT)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_path = output_dir / OUTPUT_NAME
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as output_file:
            output_file.write(subject)
    except OSError as exc:
        raise SystemExit(f"cannot write entry artifact: {exc}") from exc


if __name__ == "__main__":
    main()
