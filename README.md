# 菱菱每日更新 🦍

一个清新的个人每日更新页面，使用 Tiffany Blue 海洋风格设计。

## 🌐 在线访问

- **GitHub Pages**: https://mizzlingling.github.io/lingling-daily/
- **LINE Git (place)**: https://git.linecorp.com/lingling-yang/place
- **LINE Git (kingkong)**: https://git.linecorp.com/lingling-yang/kingkong

## ✨ 功能特色

### 1. 日期计数器
- **LINEr**: 显示从 2018年2月19日 开始的天数和年数
- **十週年倒數**: 倒数到 2027年11月30日

### 2. 今日海語
- 31条英文海洋名言
- 每天自动切换不同的 quote
- 包含 Jacques Cousteau, Walt Whitman, Kate Chopin 等名人名言

### 3. 水瓶座運勢
- 每日星座运势
- 爱情、友情、事业配对

## 🎨 设计风格

- **配色**: Tiffany Blue / Mint Green (#a8d5d5, #7ec4c4)
- **特色**: 
  - 海浪动画效果
  - 线条装饰元素
  - 渐层背景
  - 响应式设计
- **图标**: 金刚 (120px)

## 📁 项目结构

```
lingling-daily-website/
├── index.html          # 主页面
├── kingkong.png        # 金刚图标
├── README.md          # 本文件
└── design-reference.png # 设计参考图
```

## 🚀 部署

### GitHub Pages
已自动部署到 GitHub Pages。每次推送到 `main` 分支会自动更新。

### 本地预览
```bash
cd ~/lingling-daily-website
open index.html
```

## 🔄 更新内容

### 更新海洋名言
编辑 `index.html` 中的 `oceanQuotes` 数组：

```javascript
const oceanQuotes = [
    { text: "Your quote here", author: "Author Name" },
    // ...
];
```

### 更新运势内容
修改 `loadHoroscope()` 函数中的内容。

## 📝 版本历史

- **v1.0** - 初始版本，紫色渐层设计
- **v2.0** - 海洋风格设计，Tiffany Blue 配色
- **v3.0** - 添加海洋名言功能
- **v4.0** - 优化为英文名言，缩小高度

## 🛠️ 技术栈

- HTML5
- CSS3 (渐层、动画、响应式)
- Vanilla JavaScript
- SVG (海浪效果)

## 📧 联系方式

- **Email**: lingling.yang@linecorp.com
- **GitHub**: @mizzlingling
- **Instagram**: @abearhug

## 📄 License

Personal Project - All Rights Reserved

---

Made with 🌊 by Claude & Lingling