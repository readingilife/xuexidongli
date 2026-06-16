#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import asyncio
import json
import re
from pathlib import Path

import edge_tts

BASE = Path(__file__).resolve().parent
DATA = BASE / "basic_english_850_data.json"
VOICE_DIR = BASE / "voice" / "examples"
VOICE = "en-US-JennyNeural"
RATE = "-12%"


def audio_name(word, index):
    safe_word = re.sub(r"[^a-zA-Z0-9]+", "_", word).strip("_").lower()
    return f"{safe_word}_{index + 1}_female.mp3"


def iter_examples(words):
    for word_index, item in enumerate(words):
        for example_index, example in enumerate(item.get("examples") or []):
            sentence = (example.get("en") or "").strip()
            if sentence:
                yield word_index, example_index, item["word"], example, sentence


async def save_sentence(sentence, path, force=False):
    if path.exists() and path.stat().st_size > 0 and not force:
        return "skip"
    path.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(sentence, VOICE, rate=RATE)
    await communicate.save(str(path))
    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f"empty audio file: {path}")
    return "created"


async def generate(limit=None, force=False, paths_file=None, start=1):
    words = json.loads(DATA.read_text(encoding="utf-8"))
    allowed_paths = None
    if paths_file:
        allowed_paths = {
            line.strip()
            for line in Path(paths_file).read_text(encoding="utf-8").splitlines()
            if line.strip()
        }
    generated = 0
    created = 0
    skipped = 0

    seen = 0
    for _, example_index, word, example, sentence in iter_examples(words):
        seen += 1
        if seen < start:
            continue
        if limit is not None and generated >= limit:
            break
        relative = f"voice/examples/{audio_name(word, example_index)}"
        example["audio"] = relative
        if allowed_paths is not None and relative not in allowed_paths:
            continue
        result = await save_sentence(sentence, BASE / relative, force=force)
        generated += 1
        if result == "created":
            created += 1
        else:
            skipped += 1
        print(f"[{generated}] {result}: {relative} :: {sentence}")

    DATA.write_text(json.dumps(words, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"example audio updated: {generated} examples, {created} created, {skipped} skipped")


def main():
    parser = argparse.ArgumentParser(description="Generate local MP3 files for example sentences.")
    parser.add_argument("--limit", type=int, default=None, help="Generate only the first N examples.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing MP3 files.")
    parser.add_argument("--paths-file", help="Only generate audio paths listed in this file.")
    parser.add_argument("--start", type=int, default=1, help="Start from this 1-based example number.")
    args = parser.parse_args()
    asyncio.run(generate(args.limit, args.force, args.paths_file, args.start))


if __name__ == "__main__":
    main()
