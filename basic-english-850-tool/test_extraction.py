#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# 简单测试
with open('basic_english_850_quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找 wordData
start = content.find("const wordData = {")
print(f"Start at position: {start}")
if start != -1:
    # 看一些内容
    sample = content[start:start+500]
    print(f"\nSample:\n{sample}")
    
    # 简单尝试提取几个单词
    test_pattern = r"'([a-z]+)':\s*\{\s*phonetic:\s*'([^']*)'\s*,\s*meaning:\s*'([^']*)'\s*\}"
    matches = re.findall(test_pattern, content)
    print(f"\nFound {len(matches)} entries")
    if matches:
        for i, m in enumerate(matches[:5]):
            print(f"{i+1}: {m}")
