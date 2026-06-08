# 学习力报告编辑器 - 使用说明

## 🚀 简单三步

### 1️⃣ 编辑报告
双击打开 `CMS/report-editor.html`

### 2️⃣ 下载文件
点击「📥 下载报告」按钮

### 3️⃣ 自动整理
下载完成后，**双击「移动报告.command」**
→ 文件自动移动到 `xuexili` 目录！

---

## 文件名规则
- 格式: `yatai-{姓名全拼}-{年级数字}.html`
- 示例: `yatai-liupinyan-7.html` (刘品延 - 7年级)

---

## 添加更多学生姓名拼音映射

如需支持更多学生姓名，请编辑 `report-editor.html` 中的 `pinyinMap` 对象:

```javascript
const pinyinMap = {
    '刘':'liu','品':'pin','延':'yan',
    '张':'zhang','三':'san',
    '李':'li','四':'si'
};
```
