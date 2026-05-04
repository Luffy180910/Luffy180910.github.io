# Luffy180910.github.io

一个基于静态页面的个人主页项目，包含博客、视频、原神、德州与算法等内容展示页。

访问地址：https://luffy180910.github.io/

---

## 目录结构

```text
.
├── pages/
│   ├── home/index.html
│   ├── blog/                  # 博客页面
│   ├── video/                 # 视频页面
│   ├── genshin/               # 原神页面
│   ├── algorithm/
│   ├── mathematics/
│   └── texas/index.html
├── assets/
│   ├── blog/
│   │   ├── images/
│   │   └── videos/
│   ├── video/                 # 视频媒体文件
│   ├── genshin/               # 原神图片资源
│   ├── css/
│   ├── js/
│   └── site/
│       ├── base.css
│       ├── generated-list-pages.css
│       ├── media/             # 站点图片/背景/Logo
│       └── pages/             # 提取出的每页 CSS
├── projects/
│   └── webgl-coursework/
├── content/
│   └── index/                 # 生成的内容索引
└── scripts/
```

---

## 本地预览

可以使用 Python 内置服务器快速预览：

```bash
python3 -m http.server 8080
```

访问页面：

- 主页: http://localhost:8080/pages/home/index.html
- 博客: http://localhost:8080/pages/blog/index.html
- 视频: http://localhost:8080/pages/video/index.html
- 原神: http://localhost:8080/pages/genshin/index.html
- 德州: http://localhost:8080/pages/texas/index.html

或者直接访问根路径：

- http://localhost:8080

---

## 维护脚本

项目提供以下重构脚本，用于提取样式、规范文件名、以及生成内容索引：

```bash
python3 scripts/extract_inline_css.py
python3 scripts/normalize_filenames.py
python3 scripts/generate_content_index.py
```

