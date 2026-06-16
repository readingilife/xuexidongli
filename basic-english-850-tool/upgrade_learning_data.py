#!/usr/bin/env python3
"""Add usage, phonics, confusables, and parent-coaching data to the word list."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "basic_english_850_data.json"

CURATED = {
    "make": {
        "usage": ["make a cake", "make friends", "make me happy"],
        "exampleQuestion": {"sentence": "Let's ___ a cake.", "answer": "make"},
        "parentTip": "让孩子说一件今天可以 make 的东西或事情。",
        "confusables": ["take", "give", "do"]
    },
    "take": {
        "usage": ["take a seat", "take this book", "take a picture"],
        "exampleQuestion": {"sentence": "Please ___ a seat.", "answer": "take"},
        "parentTip": "让孩子做一个 take 的动作，比如拿起一本书。",
        "confusables": ["make", "give", "get"]
    },
    "give": {
        "usage": ["give me the book", "give a gift", "give help"],
        "exampleQuestion": {"sentence": "Can you ___ me the book?", "answer": "give"},
        "parentTip": "让孩子用 give 说一句把东西给别人的话。",
        "confusables": ["get", "take", "send"]
    },
    "get": {
        "usage": ["get a drink", "get up", "get home"],
        "exampleQuestion": {"sentence": "I want to ___ a drink.", "answer": "get"},
        "parentTip": "让孩子说一件自己想 get 的东西。",
        "confusables": ["give", "go", "take"]
    },
    "go": {
        "usage": ["go to school", "go home", "go to the park"],
        "exampleQuestion": {"sentence": "I ___ to school every day.", "answer": "go"},
        "parentTip": "问孩子今天想 go 哪里。",
        "confusables": ["come", "get", "do"]
    },
    "come": {
        "usage": ["come here", "come home", "come to school"],
        "exampleQuestion": {"sentence": "Please ___ here.", "answer": "come"},
        "parentTip": "让孩子边做动作边说 come here。",
        "confusables": ["go", "get", "some"]
    },
    "put": {
        "usage": ["put on a coat", "put it here", "put the bag on the table"],
        "exampleQuestion": {"sentence": "___ your bag on the table.", "answer": "put"},
        "parentTip": "让孩子把一个东西放到桌上，并说 put it here。",
        "confusables": ["get", "take", "cut"]
    },
    "see": {
        "usage": ["see the moon", "see a bird", "nice to see you"],
        "exampleQuestion": {"sentence": "I can ___ the moon.", "answer": "see"},
        "parentTip": "让孩子说出现在能 see 的三样东西。",
        "confusables": ["say", "sea", "look"]
    },
    "say": {
        "usage": ["say hello", "say sorry", "say the word"],
        "exampleQuestion": {"sentence": "Please ___ hello.", "answer": "say"},
        "parentTip": "让孩子用 say 说一句礼貌用语。",
        "confusables": ["see", "send", "sea"]
    },
    "have": {
        "usage": ["have a book", "have breakfast", "have fun"],
        "exampleQuestion": {"sentence": "I ___ a red bag.", "answer": "have"},
        "parentTip": "让孩子说三样自己 have 的东西。",
        "confusables": ["give", "make", "be"]
    },
    "do": {
        "usage": ["do homework", "do a good job", "do it now"],
        "exampleQuestion": {"sentence": "I ___ my homework after school.", "answer": "do"},
        "parentTip": "问孩子今天要 do 哪一件小事。",
        "confusables": ["go", "be", "make"]
    },
    "print": {
        "usage": ["print this page", "print a picture"],
        "exampleQuestion": {"sentence": "Please ___ this page.", "answer": "print"},
        "parentTip": "给孩子看一张纸，解释 print 是把内容打印出来。",
        "confusables": ["price", "process", "point"]
    }
}

ABSTRACT_PARENT_TIP = "这个词比较抽象，请家长用生活里的例子解释一下。"


def word_family(word, all_words):
    if len(word) < 3:
        return []
    pattern = word[-3:].lower()
    family = [item for item in all_words if item.lower().endswith(pattern) and item.lower() != word.lower()]
    return family[:4]


def default_usage(item):
    word = item["word"]
    if item["category"] == "Operations":
        return [f"use {word} in a sentence"]
    if item["category"] == "Qualities":
        return [f"a {word} thing"]
    return [f"talk about {word}"]


def default_question(item):
    usage = item["usage"][0]
    word = item["word"]
    if word in usage.split():
        sentence = usage.replace(word, "___", 1)
    else:
        sentence = f"We can talk about ___."
    return {"sentence": sentence[0].upper() + sentence[1:] + ("." if not sentence.endswith(".") else ""), "answer": word}


def main():
    words = json.loads(DATA.read_text(encoding="utf-8"))
    names = [item["word"] for item in words]
    by_name = {item["word"]: item for item in words}
    for item in words:
        word = item["word"]
        item.setdefault("usage", default_usage(item))
        if not item["usage"]:
            item["usage"] = default_usage(item)

        family = word_family(word, names)
        item.setdefault("phonics", {"pattern": word[-3:].lower() if len(word) >= 3 else word.lower(), "family": family})
        if not item["phonics"].get("family"):
            item["phonics"]["family"] = family

        siblings = [w for w in names if w != word and w[0].lower() == word[0].lower()][:6]
        item.setdefault("confusables", siblings[:3])
        item["confusables"] = [name for name in item["confusables"] if name != word]
        if len(item["confusables"]) < 3:
            more = [w for w in siblings if w not in item["confusables"]]
            item["confusables"].extend(more[: 3 - len(item["confusables"])])

        item.setdefault("parentTip", "让孩子读一遍单词，再用中文说说它是什么意思。")
        item.setdefault("exampleQuestion", default_question(item))

        if item["difficulty"] == "extension" or "adult-guidance" in item.get("tags", []):
            item["parentTip"] = item.get("parentTip") or ABSTRACT_PARENT_TIP
            if "needs-parent-help" not in item["tags"]:
                item["tags"].append("needs-parent-help")

    for word, patch in CURATED.items():
        if word not in by_name:
            continue
        by_name[word].update(patch)
        by_name[word]["confusables"] = [name for name in by_name[word].get("confusables", []) if name != word]
        by_name[word]["phonics"] = {
            "pattern": word[-3:].lower() if len(word) >= 3 else word.lower(),
            "family": word_family(word, names)
        }

    DATA.write_text(json.dumps(words, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"upgraded {len(words)} words")


if __name__ == "__main__":
    main()
