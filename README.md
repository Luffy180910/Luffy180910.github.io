welcome to see my web

https://luffy180910.github.io/

## Structure

```text
.
├── pages/
│   ├── home/index.html
│   ├── blog/                  # blog pages
│   ├── video/                 # video page
│   ├── genshin/               # genshin page
│   ├── algorithm/
│   ├── mathematics/
│   └── texas/index.html
├── assets/
│   ├── blog/
│   │   ├── images/
│   │   └── videos/
│   ├── video/                 # video media files
│   ├── genshin/               # genshin image assets
│   ├── css/
│   ├── js/
│   └── site/
│       ├── base.css
│       ├── generated-list-pages.css
│       ├── media/             # site images/backgrounds/logo
│       └── pages/             # extracted per-page css
├── projects/
│   └── webgl-coursework/
├── content/
│   └── index/                 # generated metadata indexes
└── scripts/
```

## Refactor scripts

```bash
python3 scripts/extract_inline_css.py
python3 scripts/normalize_filenames.py
python3 scripts/generate_content_index.py
```

<pre>
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░   ░▒▓██████▓▒░    ░▒▓██████▓▒░  
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     
░▒▓████████▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░        ░▒▓█▓▒░           ░▒▓█▓▒░     
</pre>

##
 Bash(python3 -m http.server 8080)
  ⎿  Running in the background (↓ to manage)

● 本地服务器已启动。你可以在浏览器中访问：

  - 主页: http://localhost:8080/pages/home/index.html
  - 博客: http://localhost:8080/pages/blog/index.html
  - 视频: http://localhost:8080/pages/video/index.html
  - 原神: http://localhost:8080/pages/genshin/index.html
  - 德州: http://localhost:8080/pages/texas/index.html

  或者从根路径自动跳转：http://localhost:8080
