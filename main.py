#!/usr/bin/env python3
"""Write the competition's single commit-subject artifact deterministically."""

import os
from pathlib import Path

ENTRY = "fix: taught the workaround to reproduce itself"


def main():
    if not ENTRY or ENTRY.isspace() or len(ENTRY) > 100 or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be one nonblank line of at most 100 characters")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_path = output_dir / "entry.txt"
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as output_file:
            output_file.write(ENTRY)
    except OSError as exc:
        raise SystemExit(f"cannot write entry artifact: {exc}") from exc


if __name__ == "__main__":
    main()
