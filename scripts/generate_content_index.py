#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "index"
BLOG_DIR = ROOT / "pages" / "blog"
VIDEO_ASSETS_DIR = ROOT / "assets" / "video"


TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
HEADING_RE = re.compile(r"<h[1-3][^>]*>(.*?)</h[1-3]>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def extract_title(html: str, fallback: str) -> str:
    heading = HEADING_RE.search(html)
    if heading:
        text = TAG_RE.sub("", heading.group(1))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            return text

    match = TITLE_RE.search(html)
    if match:
        title = re.sub(r"\s+", " ", match.group(1)).strip()
        if title:
            return title
    return fallback


def humanize_filename(stem: str) -> str:
    return re.sub(r"[-_]+", " ", stem).strip() or stem


def collect_blog_items() -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for path in sorted(BLOG_DIR.rglob("*.html")):
        rel = path.relative_to(BLOG_DIR).as_posix()
        if rel == "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        title = extract_title(html, path.stem)
        items.append({"title": title, "href": f"/pages/blog/{rel}"})
    return items


def collect_video_items() -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if not VIDEO_ASSETS_DIR.exists():
        return items
    for path in sorted(VIDEO_ASSETS_DIR.glob("*.mp4")):
        rel = path.relative_to(ROOT).as_posix()
        items.append({"title": humanize_filename(path.stem), "src": f"/{rel}"})
    return items


def write_json(name: str, payload: list[dict[str, str]]) -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    (CONTENT_DIR / f"{name}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def render_blog_index(items: list[dict[str, str]]) -> str:
    lines = "\n".join(
        f'        <li><a href="{item["href"]}" target="_blank">{item["title"]}</a></li>'
        for item in items
    )
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>my blog</title>
    <meta http-equiv="content-language" content="en">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="stylesheet" href="/assets/site/base.css">
    <link rel="stylesheet" href="/assets/site/generated-list-pages.css">
</head>
<body class="list-page blog-page">
    <div class="wrap">
        <h1>Blog Articles</h1>
        <ul>
{lines}
        </ul>
    </div>
</body>
</html>
"""


def render_video_index(items: list[dict[str, str]]) -> str:
    cards = "\n".join(
        f"""        <section class="video-card">
            <h2>{item["title"]}</h2>
            <video controls preload="metadata">
                <source src="{item["src"]}" type="video/mp4">
            </video>
        </section>"""
        for item in items
    )
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>video</title>
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="stylesheet" href="/assets/site/base.css">
    <link rel="stylesheet" href="/assets/site/generated-list-pages.css">
</head>
<body class="list-page video-page">
    <div class="wrap">
        <h1>Video Gallery</h1>
{cards}
    </div>
</body>
</html>
"""


def ensure_generated_css() -> None:
    css_path = ROOT / "assets" / "site" / "generated-list-pages.css"
    css_path.parent.mkdir(parents=True, exist_ok=True)
    css_path.write_text(
        """.list-page {
  min-height: 100vh;
  padding: 40px 16px;
}
.list-page .wrap {
  max-width: 1080px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 10px;
  padding: 24px;
}
.list-page h1 { margin: 0 0 16px; }
.blog-page { background: #f4f6fb; }
.blog-page ul { margin: 0; padding-left: 20px; }
.blog-page li { margin: 8px 0; }
.blog-page a { color: #1651d1; text-decoration: none; }
.blog-page a:hover { text-decoration: underline; }
.video-page { background: #0f172a; color: #e5e7eb; }
.video-page .wrap { background: rgba(2, 6, 23, 0.7); }
.video-card { margin-bottom: 24px; }
.video-card h2 { margin: 0 0 8px; font-size: 22px; }
.video-card video { width: 100%; border-radius: 8px; background: #000; }
""",
        encoding="utf-8",
    )


def main() -> None:
    blog_items = collect_blog_items()
    video_items = collect_video_items()

    write_json("blog", blog_items)
    write_json("video", video_items)
    ensure_generated_css()

    (BLOG_DIR / "index.html").write_text(render_blog_index(blog_items), encoding="utf-8")
    (ROOT / "pages" / "video" / "index.html").write_text(
        render_video_index(video_items), encoding="utf-8"
    )
    print(f"Generated blog index ({len(blog_items)} items) and video index ({len(video_items)} items).")


if __name__ == "__main__":
    main()
