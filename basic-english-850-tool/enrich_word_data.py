#!/usr/bin/env python3
"""Normalize the existing Ogden list into the child-friendly learning schema."""
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "basic_english_850_data.json"
RESOURCE_PATH = BASE / "basic_english_850.html"

MANUAL = {
    "print": ("/prɪnt/", "印刷；打印"),
    "automatic": ("/ˌɔːtəˈmætɪk/", "自动的"),
    "cold": ("/kəʊld/", "冷的；寒冷"),
    "complete": ("/kəmˈpliːt/", "完整的；完成"),
    "cruel": ("/ˈkruːəl/", "残忍的；让人难受的"),
    "like": ("/laɪk/", "喜欢；像"),
    "male": ("/meɪl/", "男性的；雄性的"),
    "married": ("/ˈmærid/", "已婚的；结婚的"),
    "material": ("/məˈtɪəriəl/", "材料；物料"),
    "medical": ("/ˈmedɪkl/", "医疗的；医学的"),
    "military": ("/ˈmɪlətri/", "军队的；军事的"),
    "natural": ("/ˈnætʃrəl/", "自然的；天然的"),
    "public": ("/ˈpʌblɪk/", "公共的；公众"),
    "stiff": ("/stɪf/", "硬的；僵直的"),
    "awake": ("/əˈweɪk/", "醒着的；醒来"),
    "bad": ("/bæd/", "不好的；坏的"),
    "bent": ("/bent/", "弯曲的"),
    "bitter": ("/ˈbɪtə(r)/", "苦的；令人难过的"),
    "certain": ("/ˈsɜːtn/", "确定的；某一个"),
    "comfortable": ("/ˈkʌmftəbl/", "舒服的"),
    "dark": ("/dɑːk/", "黑暗的；深色的"),
    "dead": ("/ded/", "死亡的；失去生命的"),
    "dear": ("/dɪə(r)/", "亲爱的；珍贵的"),
    "delicate": ("/ˈdelɪkət/", "易损的；精致的"),
    "different": ("/ˈdɪfrənt/", "不同的"),
    "dirty": ("/ˈdɜːti/", "脏的"),
    "false": ("/fɔːls/", "错误的；不真实的"),
    "feeble": ("/ˈfiːbl/", "虚弱的；无力的"),
    "female": ("/ˈfiːmeɪl/", "女性的；雌性的"),
    "foolish": ("/ˈfuːlɪʃ/", "不明智的；愚蠢的"),
    "future": ("/ˈfjuːtʃə(r)/", "未来；将来的"),
    "green": ("/ɡriːn/", "绿色的"),
    "ill": ("/ɪl/", "生病的；不舒服的"),
    "left": ("/left/", "左边的；留下的"),
    "shut": ("/ʃʌt/", "关闭；关上的"),
    "strange": ("/streɪndʒ/", "奇怪的；陌生的"),
    "wrong": ("/rɒŋ/", "错误的；不对的"),
}

EXTENSION = {
    "sex", "violent", "punishment", "crime", "death", "religion", "war", "attack",
    "military", "authority", "government", "political", "property", "theory",
}
ABSTRACT_HINTS = {
    "Things — General", "Qualities"
}
PLACEHOLDER_PREFIXES = ("I know the word", "Let's learn")


def embedded_dictionary():
    text = RESOURCE_PATH.read_text(encoding="utf-8")
    matches = re.findall(
        r"'([a-zA-Z]+)': \{ phonetic: '([^']*)', meaning: '([^']*)' \}", text
    )
    return {word: (phonetic, meaning) for word, phonetic, meaning in matches}


def short_example(word, category):
    if category == "Operations":
        return {"en": f"Please use {word} in a short sentence.", "cn": f"请在短句中使用 {word}。"}
    if category == "Qualities":
        return {"en": f"The word {word} describes something.", "cn": f"{word} 可以描述事物。"}
    return {"en": f"We talked about {word} in class.", "cn": f"我们在课堂上谈到了 {word}。"}


def main():
    words = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    known = embedded_dictionary()
    for item in words:
        word = item["word"]
        if word in known:
            item["phonetic"], item["meaning"] = known[word]
        elif word in MANUAL:
            item["phonetic"], item["meaning"] = MANUAL[word]
        item["childMeaning"] = item["meaning"].split("；")[0].strip()
        old_examples = item.get("examples") or []
        if not old_examples or old_examples[0].get("en", "").startswith(PLACEHOLDER_PREFIXES):
            item["examples"] = [short_example(word, item["category"])]
        item["difficulty"] = (
            "extension" if word.lower() in EXTENSION
            else "advanced" if item["category"] in ABSTRACT_HINTS
            else "basic"
        )
        item["tags"] = [item["category"], item["difficulty"]]
        if word.lower() in EXTENSION:
            item["tags"].append("adult-guidance")
        item["enabled"] = True
    DATA_PATH.write_text(json.dumps(words, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"enriched {len(words)} entries")


if __name__ == "__main__":
    main()
