welcome to see my web

https://luffy180910.github.io/

## Structure

```text
.
├── pages/                      # archived top-level standalone pages
│   ├── home/index.html
│   └── texas/index.html
├── assets/
│   └── site/
│       ├── base.css
│       ├── generated-list-pages.css
│       ├── media/              # site images/backgrounds/logo
│       └── pages/              # extracted per-page css
├── blog/
│   └── assets/
│       ├── images/
│       └── videos/
├── video/
│   └── videos/
├── projects/
│   └── webgl-coursework/
├── content/index/              # generated metadata indexes
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
