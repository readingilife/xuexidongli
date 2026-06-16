#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import asyncio
import edge_tts
from pathlib import Path

def extract_words(html_file):
    """从HTML文件中提取所有单词"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 <li> 标签中的单词
    pattern = r'<li>([a-zA-Z]+)</li>'
    words = re.findall(pattern, content)
    
    # 去重并保持顺序
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    
    return unique_words

async def generate_voice(word, output_dir, voice_type):
    """生成单词的语音文件"""
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 检查文件是否已存在，避免重复生成
    filename = f"{word}_{voice_type}.mp3"
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath):
        print(f"已存在，跳过: {filename}")
        return filepath
    
    # 选择不同的语音
    # 男声: en-US-GuyNeural, en-US-ChristopherNeural
    # 女声: en-US-JennyNeural, en-US-AriaNeural
    voice = 'en-US-GuyNeural' if voice_type == 'male' else 'en-US-JennyNeural'
    
    # 生成语音
    communicate = edge_tts.Communicate(word, voice)
    
    # 保存文件
    await communicate.save(filepath)
    
    print(f"已生成: {filename}")
    return filepath

async def main():
    # 文件路径均相对于脚本，项目移动后也能正常工作。
    base_dir = Path(__file__).resolve().parent
    html_file = base_dir / 'basic_english_850.html'
    voice_dir = base_dir / 'voice'
    
    # 提取单词
    print("正在提取单词...")
    words = extract_words(str(html_file))
    print(f"共找到 {len(words)} 个单词")
    
    # 为所有单词生成语音
    print(f"\n将为所有 {len(words)} 个单词生成语音")
    
    # 创建语音目录
    os.makedirs(voice_dir, exist_ok=True)
    print(f"\n语音文件将保存到: {voice_dir}")
    
    # 生成男声和女声
    print("\n开始生成语音文件...")
    total = len(words)
    for i, word in enumerate(words, 1):
        print(f"\n[{i}/{total}] 处理单词: {word}")
        await generate_voice(word, str(voice_dir), 'male')
        await generate_voice(word, str(voice_dir), 'female')
    
    print("\n✅ 所有语音文件生成完成！")

if __name__ == '__main__':
    asyncio.run(main())
