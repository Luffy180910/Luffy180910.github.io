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
