# 学习力报告编辑器 - 使用说明

## 快速开始

### 1. 安装依赖
```bash
cd CMS
npm install
```

### 2. 启动服务器
```bash
npm start
```

### 3. 打开编辑器
在浏览器中访问: `http://localhost:3000/CMS/report-editor.html`

## 功能说明

### 编辑报告
- 左侧面板用于编辑学生信息和报告内容
- 修改内容时，右侧会自动更新预览
- 支持添加/删除各项要点

### 保存报告
点击「保存报告」按钮，报告将自动保存到 `xuexili` 目录

### 文件命名规则
- 格式: `姓名全拼 + 年级数字.html`
- 示例: `liupinyan7.html` (刘品延 - 7年级)

## 添加更多学生姓名拼音映射

如需支持更多学生姓名，请编辑 `report-editor.html` 中的 `pinyinMap` 对象:

```javascript
const pinyinMap = {
    '刘':'liu','品':'pin','延':'yan',
    '张':'zhang','三':'san',
    '李':'li','四':'si'
};
```
