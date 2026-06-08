#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import json
import asyncio
import edge_tts
from pathlib import Path
from typing import Dict, List, Optional


def extract_words_with_category(html_file: str) -> List[Dict]:
    """从HTML文件中提取所有单词和分类"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义分类映射
    categories = {
        'operations': 'Operations',
        'things-general': 'Things — General',
        'things-picturable': 'Things — Picturable',
        'qualities': 'Qualities',
        'wordorder': 'Word Order'
    }
    
    words = []
    seen = set()
    
    # 逐个分类提取
    for cat_id, cat_name in categories.items():
        # 找到该分类的section
        section_pattern = rf'<section class="grade-section" id="{cat_id}">.*?</section>'
        section_match = re.search(section_pattern, content, re.DOTALL)
        if section_match:
            section_content = section_match.group(0)
            # 提取该分类下的单词
            word_pattern = r'<li>([a-zA-Z]+)</li>'
            cat_words = re.findall(word_pattern, section_content)
            for word in cat_words:
                if word not in seen:
                    seen.add(word)
                    words.append({
                        'word': word,
                        'category': cat_name
                    })
    
    return words


def extract_existing_data(quiz_file: str) -> Dict:
    """从quiz.html中提取已有的音标和意思"""
    with open(quiz_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 直接匹配所有单词条目
    entry_pattern = r"'([a-zA-Z]+)':\s*\{\s*phonetic:\s*'([^']*)'\s*,\s*meaning:\s*'([^']*)'\s*\}"
    entries = re.findall(entry_pattern, content)
    
    word_data = {}
    for word, phonetic, meaning in entries:
        word_data[word] = {
            'phonetic': phonetic,
            'meaning': meaning
        }
    
    print(f"Extracted {len(word_data)} words from quiz file")
    return word_data


def check_existing_voices(voice_dir: str, word: str) -> Dict[str, bool]:
    """检查单词的发音文件是否存在"""
    female_exists = os.path.exists(os.path.join(voice_dir, f"{word}_female.mp3"))
    male_exists = os.path.exists(os.path.join(voice_dir, f"{word}_male.mp3"))
    return {
        'female': female_exists,
        'male': male_exists
    }


async def generate_voice(word: str, output_dir: str, voice_type: str) -> str:
    """生成单词的语音文件"""
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{word}_{voice_type}.mp3"
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath):
        return filepath
    
    # 选择语音
    voice = 'en-US-GuyNeural' if voice_type == 'male' else 'en-US-JennyNeural'
    
    # 生成语音
    communicate = edge_tts.Communicate(word, voice)
    await communicate.save(filepath)
    
    return filepath


async def generate_missing_voices(words: List[str], voice_dir: str):
    """生成缺失的发音文件"""
    print("\n开始检查并生成发音文件...")
    total = len(words)
    
    for i, word in enumerate(words, 1):
        voices = check_existing_voices(voice_dir, word)
        print(f"[{i}/{total}] {word}: female={voices['female']}, male={voices['male']}")
        
        if not voices['female']:
            print(f"  生成女声...")
            await generate_voice(word, voice_dir, 'female')
        
        if not voices['male']:
            print(f"  生成男声...")
            await generate_voice(word, voice_dir, 'male')


# 基础例句模板库
EXAMPLE_TEMPLATES = {
    # 动词
    'come': [
        {"en": "Come here, please.", "cn": "请过来。"},
        {"en": "Welcome to our school.", "cn": "欢迎来到我们学校。"}
    ],
    'go': [
        {"en": "Let's go to the park.", "cn": "让我们去公园吧。"},
        {"en": "I go to school every day.", "cn": "我每天去上学。"}
    ],
    'get': [
        {"en": "Can I get a drink?", "cn": "我可以喝一杯吗？"},
        {"en": "Get up early tomorrow.", "cn": "明天早点起床。"}
    ],
    'give': [
        {"en": "Give me the book, please.", "cn": "请把书给我。"},
        {"en": "I will give you a gift.", "cn": "我会给你一个礼物。"}
    ],
    'make': [
        {"en": "Let's make a cake.", "cn": "让我们做个蛋糕吧。"},
        {"en": "She can make beautiful drawings.", "cn": "她能画出漂亮的画。"}
    ],
    'take': [
        {"en": "Take this umbrella with you.", "cn": "带上这把伞。"},
        {"en": "Please take a seat.", "cn": "请坐。"}
    ],
    'keep': [
        {"en": "Keep quiet in the library.", "cn": "图书馆里要保持安静。"},
        {"en": "Keep this book for me.", "cn": "帮我保存这本书。"}
    ],
    'let': [
        {"en": "Let me help you.", "cn": "让我来帮你。"},
        {"en": "Let's play together.", "cn": "我们一起玩吧。"}
    ],
    'put': [
        {"en": "Put your bag on the table.", "cn": "把你的包放在桌子上。"},
        {"en": "Put on your coat.", "cn": "穿上你的外套。"}
    ],
    'do': [
        {"en": "What do you want to do?", "cn": "你想做什么？"},
        {"en": "I do my homework every day.", "cn": "我每天做作业。"}
    ],
    'have': [
        {"en": "I have a cat.", "cn": "我有一只猫。"},
        {"en": "We have a nice day.", "cn": "我们今天过得很愉快。"}
    ],
    'see': [
        {"en": "I can see the moon.", "cn": "我能看到月亮。"},
        {"en": "Nice to see you again.", "cn": "很高兴再次见到你。"}
    ],
    'say': [
        {"en": "Say hello to your teacher.", "cn": "向你的老师问好。"},
        {"en": "What did you say?", "cn": "你说什么？"}
    ],
    'send': [
        {"en": "Send me an email.", "cn": "给我发封邮件。"},
        {"en": "I will send you a letter.", "cn": "我会给你寄封信。"}
    ],
    
    # 名词（具象）
    'book': [
        {"en": "This is my favorite book.", "cn": "这是我最喜欢的书。"},
        {"en": "I read a book every day.", "cn": "我每天读一本书。"}
    ],
    'cat': [
        {"en": "The cat is sleeping.", "cn": "猫在睡觉。"},
        {"en": "I love my cat.", "cn": "我爱我的猫。"}
    ],
    'dog': [
        {"en": "The dog is running.", "cn": "狗在跑。"},
        {"en": "My dog is very friendly.", "cn": "我的狗很友好。"}
    ],
    'school': [
        {"en": "I go to school by bus.", "cn": "我坐公交去上学。"},
        {"en": "Our school is beautiful.", "cn": "我们的学校很漂亮。"}
    ],
    'water': [
        {"en": "Drink more water.", "cn": "多喝水。"},
        {"en": "The water is clean.", "cn": "水很干净。"}
    ],
    'tree': [
        {"en": "There is a big tree.", "cn": "有一棵大树。"},
        {"en": "The tree has green leaves.", "cn": "树有绿色的叶子。"}
    ],
    'flower': [
        {"en": "This flower is red.", "cn": "这朵花是红色的。"},
        {"en": "I like flowers.", "cn": "我喜欢花。"}
    ],
    'bird': [
        {"en": "The bird can fly.", "cn": "鸟会飞。"},
        {"en": "Listen to the bird sing.", "cn": "听鸟儿唱歌。"}
    ],
    'sun': [
        {"en": "The sun is hot.", "cn": "太阳很晒。"},
        {"en": "The sun rises in the east.", "cn": "太阳从东方升起。"}
    ],
    'moon': [
        {"en": "The moon is round.", "cn": "月亮是圆的。"},
        {"en": "Look at the moon tonight.", "cn": "看看今晚的月亮。"}
    ],
    
    # 形容词
    'good': [
        {"en": "You are a good student.", "cn": "你是个好学生。"},
        {"en": "This tastes good.", "cn": "这个尝起来不错。"}
    ],
    'bad': [
        {"en": "Don't be a bad boy.", "cn": "不要做坏孩子。"},
        {"en": "The weather is bad today.", "cn": "今天天气不好。"}
    ],
    'big': [
        {"en": "That's a big elephant.", "cn": "那是一头大象。"},
        {"en": "I have a big bag.", "cn": "我有一个大包。"}
    ],
    'small': [
        {"en": "The ant is small.", "cn": "蚂蚁很小。"},
        {"en": "I have a small toy.", "cn": "我有一个小玩具。"}
    ],
    'happy': [
        {"en": "I am very happy today.", "cn": "我今天很开心。"},
        {"en": "Happy birthday to you!", "cn": "祝你生日快乐！"}
    ],
    'sad': [
        {"en": "Don't be sad.", "cn": "不要难过。"},
        {"en": "The sad story made me cry.", "cn": "这个悲伤的故事让我哭了。"}
    ],
    'red': [
        {"en": "The apple is red.", "cn": "苹果是红色的。"},
        {"en": "I like the red one.", "cn": "我喜欢红色的那个。"}
    ],
    'blue': [
        {"en": "The sky is blue.", "cn": "天空是蓝色的。"},
        {"en": "My pen is blue.", "cn": "我的钢笔是蓝色的。"}
    ]
}


def generate_word_info(word: str, existing_data: Dict) -> Dict:
    """生成单词的完整信息"""
    # 先看是否有现成数据
    if word in existing_data:
        phonetic = existing_data[word]['phonetic']
        meaning = existing_data[word]['meaning']
    else:
        # 简单的默认值
        phonetic = f"/{word}/"
        meaning = f"{word}"
    
    # 尝试用模板生成例句
    if word in EXAMPLE_TEMPLATES:
        examples = EXAMPLE_TEMPLATES[word]
    else:
        # 通用例句
        examples = [
            {"en": f"I know the word '{word}'.", "cn": f"我知道这个单词'{word}'。"},
            {"en": f"Let's learn '{word}' together.", "cn": f"让我们一起学习'{word}'。"}
        ]
    
    return {
        'word': word,
        'phonetic': phonetic,
        'meaning': meaning,
        'examples': examples,
        'voice': {
            'female': f"voice/{word}_female.mp3",
            'male': f"voice/{word}_male.mp3"
        }
    }


async def main():
    # 文件路径
    base_dir = '/Users/apple/Documents/project/eduKB'
    html_file = os.path.join(base_dir, 'basic_english_850.md')
    quiz_file = os.path.join(base_dir, 'basic_english_850_quiz.html')
    voice_dir = os.path.join(base_dir, 'voice')
    output_file = os.path.join(base_dir, 'basic_english_850_data.json')
    
    # 1. 提取单词和分类
    print("步骤1: 提取单词和分类...")
    words_with_cat = extract_words_with_category(html_file)
    print(f"共找到 {len(words_with_cat)} 个单词")
    
    # 2. 提取已有数据
    print("\n步骤2: 提取已有的音标和意思...")
    existing_data = extract_existing_data(quiz_file)
    print(f"已有 {len(existing_data)} 个单词的数据")
    
    # 3. 生成发音文件
    print("\n步骤3: 检查并生成发音文件...")
    words = [w['word'] for w in words_with_cat]
    await generate_missing_voices(words, voice_dir)
    
    # 4. 生成完整数据
    print("\n步骤4: 生成完整单词数据...")
    final_data = []
    for word_info in words_with_cat:
        word = word_info['word']
        category = word_info['category']
        
        word_data = generate_word_info(word, existing_data)
        word_data['category'] = category
        
        final_data.append(word_data)
    
    # 5. 保存到JSON文件
    print(f"\n步骤5: 保存到 {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print("\n✅ 所有任务完成！")
    print(f"   - 单词数量: {len(final_data)}")
    print(f"   - 数据文件: {output_file}")


if __name__ == '__main__':
    asyncio.run(main())
