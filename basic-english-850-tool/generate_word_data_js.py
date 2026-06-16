#!/usr/bin/env python3
"""Generate a script-friendly copy of the word data for file:// fallback."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "basic_english_850_data.json"
TARGET = BASE / "basic_english_850_data.js"


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    TARGET.write_text(
        "window.BASIC_ENGLISH_850_DATA = " + payload + ";\n",
        encoding="utf-8",
    )
    print(f"wrote {TARGET.name}: {len(data)} words")


if __name__ == "__main__":
    main()
