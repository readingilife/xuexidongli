#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "basic_english_850_data.json"
DATA_JS = BASE / "basic_english_850_data.js"
REQUIRED = {
    "word", "phonetic", "meaning", "childMeaning", "examples", "voice",
    "category", "difficulty", "tags", "enabled", "usage", "phonics",
    "confusables", "parentTip", "exampleQuestion"
}
BAD_EXAMPLE_PREFIXES = ("I know the word", "Let's learn", "Please use ", "We talked about ", "The word ", "This one is ")
BAD_EXAMPLE_SNIPPETS = ("matters to us", "can happen at school", "We can digestion safely", "We can driving safely")


def validate():
    words = json.loads(DATA.read_text(encoding="utf-8"))
    errors = []
    names = [item.get("word") for item in words]
    if len(words) != 850:
        errors.append(f"expected 850 unique Ogden entries, got {len(words)}")
    if not DATA_JS.exists() or "window.BASIC_ENGLISH_850_DATA" not in DATA_JS.read_text(encoding="utf-8")[:200]:
        errors.append("missing script fallback basic_english_850_data.js")
    if len(set(names)) != len(names):
        errors.append("duplicate words found")
    for item in words:
        word = item.get("word", "<missing>")
        missing = REQUIRED - item.keys()
        if missing:
            errors.append(f"{word}: missing {sorted(missing)}")
        if not item.get("childMeaning") or item.get("childMeaning", "").lower() == word.lower():
            errors.append(f"{word}: invalid childMeaning")
        # Some short words genuinely have an IPA spelling identical to the word
        # (for example /let/ and /red/), so only reject that shape when the
        # meaning is also still an unresolved English placeholder.
        if not item.get("phonetic") or (
            re.fullmatch(rf"/{re.escape(word)}/", item.get("phonetic", ""), re.I)
            and item.get("childMeaning", "").lower() == word.lower()
        ):
            errors.append(f"{word}: placeholder phonetic")
        examples = item.get("examples") or []
        if not examples or any(not ex.get("en") for ex in examples):
            errors.append(f"{word}: missing example")
        if any(ex.get("en", "").startswith(BAD_EXAMPLE_PREFIXES) for ex in examples):
            errors.append(f"{word}: placeholder example")
        if any(any(snippet in ex.get("en", "") for snippet in BAD_EXAMPLE_SNIPPETS) for ex in examples):
            errors.append(f"{word}: weak template example")
        for example in examples:
            audio_path = example.get("audio")
            if not audio_path:
                errors.append(f"{word}: missing example audio")
                continue
            audio_file = BASE / audio_path
            if not audio_file.exists() or audio_file.stat().st_size == 0:
                errors.append(f"{word}: missing example audio {audio_path}")
        for path in (item.get("voice") or {}).values():
            voice_file = BASE / path
            if not voice_file.exists() or voice_file.stat().st_size == 0:
                errors.append(f"{word}: missing voice {path}")
        if not isinstance(item.get("usage"), list) or not item["usage"]:
            errors.append(f"{word}: missing usage")
        phonics = item.get("phonics") or {}
        if not phonics.get("pattern") or not isinstance(phonics.get("family", []), list):
            errors.append(f"{word}: invalid phonics")
        if not isinstance(item.get("confusables"), list):
            errors.append(f"{word}: invalid confusables")
        if word in item.get("confusables", []):
            errors.append(f"{word}: confusables contains itself")
        if not item.get("parentTip"):
            errors.append(f"{word}: missing parentTip")
        question = item.get("exampleQuestion") or {}
        if not question.get("sentence") or question.get("answer") != word:
            errors.append(f"{word}: invalid exampleQuestion")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems[:100]))
        raise SystemExit(1)
    print("word data valid: 850 unique entries")
