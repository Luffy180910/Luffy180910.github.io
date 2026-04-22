#!/usr/bin/env python3
from __future__ import annotations

import re
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
STYLE_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.IGNORECASE | re.DOTALL)


def to_posix(path: Path) -> str:
    return path.as_posix()


def ensure_base_css() -> Path:
    base_css = ROOT / "assets" / "site" / "base.css"
    base_css.parent.mkdir(parents=True, exist_ok=True)
    if not base_css.exists():
        base_css.write_text(
            """* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  line-height: 1.5;
}
a { color: inherit; }
img, video { max-width: 100%; height: auto; }
""",
            encoding="utf-8",
        )
    return base_css


def css_output_path(html_path: Path) -> Path:
    rel = html_path.relative_to(ROOT)
    safe_stem = to_posix(rel.with_suffix("")).replace("/", "__")
    return ROOT / "assets" / "site" / "pages" / f"{safe_stem}.css"


def ensure_link(content: str, href: str) -> str:
    link = f'<link rel="stylesheet" href="{href}">'
    if href in content:
        return content
    if "</head>" in content:
        return content.replace("</head>", f"    {link}\n</head>")
    return content


def extract_from_file(html_path: Path, base_css: Path) -> bool:
    original = html_path.read_text(encoding="utf-8")
    matches = STYLE_RE.findall(original)
    if not matches:
        return False

    css_content = "\n\n".join(block.strip() for block in matches if block.strip())
    if not css_content:
        return False

    out_css = css_output_path(html_path)
    out_css.parent.mkdir(parents=True, exist_ok=True)
    out_css.write_text(css_content + "\n", encoding="utf-8")

    content = STYLE_RE.sub("", original)
    rel_base = os.path.relpath(base_css, html_path.parent).replace("\\", "/")
    rel_page_css = os.path.relpath(out_css, html_path.parent).replace("\\", "/")
    content = ensure_link(content, rel_base)
    content = ensure_link(content, rel_page_css)
    html_path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    base_css = ensure_base_css()
    html_files = sorted(ROOT.rglob("*.html"))
    changed = 0
    for html_path in html_files:
        if ".git" in html_path.parts:
            continue
        if extract_from_file(html_path, base_css):
            changed += 1
    print(f"Extracted inline CSS from {changed} HTML files.")


if __name__ == "__main__":
    main()
