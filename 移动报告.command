#!/bin/bash
# 学习力报告 - 自动移动脚本
# 将下载的报告移动到 xuexili 目录

cd "$(dirname "$0")"

echo "========================================="
echo "  学习力报告自动整理工具"
echo "========================================="
echo ""

# 下载目录
DOWNLOAD_DIR="$HOME/Downloads"
TARGET_DIR="$(pwd)/xuexili"

echo "正在查找最近下载的报告文件..."

# 查找最近的HTML文件
LATEST_FILE=$(ls -t "$DOWNLOAD_DIR"/*.html 2>/dev/null | head -1)

if [ -z "$LATEST_FILE" ]; then
    echo "❌ 在下载文件夹中没有找到 HTML 文件"
    echo ""
    echo "请先使用编辑器下载报告文件"
    read -p "按回车键退出..."
    exit 1
fi

echo ""
echo "找到文件: $(basename "$LATEST_FILE")"
echo "修改时间: $(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$LATEST_FILE")"
echo ""

read -p "是否将此文件移动到 xuexili 目录? (y/n): " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    mv "$LATEST_FILE" "$TARGET_DIR/"
    echo ""
    echo "✅ 文件已移动到: $TARGET_DIR/$(basename "$LATEST_FILE")"
    echo ""
    echo "文件已准备好，可以通过网页访问了！"
else
    echo ""
    echo "已取消操作"
fi

echo ""
read -p "按回车键退出..."
