from __future__ import annotations

from tests.conftest import load_script_module


def test_extract_title_prefers_heading_over_title():
    module = load_script_module("generate_content_index")
    html = "<title>Fallback</title><h1>  Hello <em>World</em> </h1>"

    assert module.extract_title(html, "post") == "Hello World"


def test_collect_blog_items_skips_index_and_uses_extracted_title(tmp_path, monkeypatch):
    module = load_script_module("generate_content_index")
    blog_dir = tmp_path / "pages" / "blog"
    blog_dir.mkdir(parents=True)
    (blog_dir / "index.html").write_text("<title>Index</title>", encoding="utf-8")
    (blog_dir / "hello-world.html").write_text(
        "<html><head><title>Ignored</title></head><body><h2>Hello Blog</h2></body></html>",
        encoding="utf-8",
    )

    monkeypatch.setattr(module, "BLOG_DIR", blog_dir)

    assert module.collect_blog_items() == [
        {"title": "Hello Blog", "href": "/pages/blog/hello-world.html"}
    ]


def test_collect_video_items_humanizes_mp4_filenames(tmp_path, monkeypatch):
    module = load_script_module("generate_content_index")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    video_dir = tmp_path / "assets" / "video"
    video_dir.mkdir(parents=True)
    (video_dir / "my_demo-video.mp4").write_bytes(b"")
    (video_dir / "ignored.webm").write_bytes(b"")

    monkeypatch.setattr(module, "VIDEO_ASSETS_DIR", video_dir)

    assert module.collect_video_items() == [
        {"title": "my demo video", "src": "/assets/video/my_demo-video.mp4"}
    ]
