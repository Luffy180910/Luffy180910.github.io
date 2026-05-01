from __future__ import annotations

from tests.conftest import load_script_module


def test_css_output_path_mirrors_html_path(tmp_path, monkeypatch):
    module = load_script_module("extract_inline_css")
    monkeypatch.setattr(module, "ROOT", tmp_path)

    html_path = tmp_path / "pages" / "blog" / "post.html"
    html_path.parent.mkdir(parents=True)
    html_path.write_text("<html></html>", encoding="utf-8")

    result = module.css_output_path(html_path)

    assert result == tmp_path / "assets" / "site" / "pages" / "pages__blog__post.css"


def test_ensure_link_inserts_stylesheet_before_head_close():
    module = load_script_module("extract_inline_css")
    content = "<head>\n</head>"

    updated = module.ensure_link(content, "./style.css")

    assert '<link rel="stylesheet" href="./style.css">' in updated
    assert updated.index("./style.css") < updated.index("</head>")


def test_extract_from_file_writes_css_and_relinks_html(tmp_path, monkeypatch):
    module = load_script_module("extract_inline_css")
    monkeypatch.setattr(module, "ROOT", tmp_path)

    html_path = tmp_path / "pages" / "home" / "index.html"
    html_path.parent.mkdir(parents=True)
    html_path.write_text(
        """<html><head><title>Home</title></head><body>
<style>
body { color: red; }
</style>
<h1>Hello</h1>
</body></html>
""",
        encoding="utf-8",
    )

    base_css = module.ensure_base_css()

    changed = module.extract_from_file(html_path, base_css)

    page_css = tmp_path / "assets" / "site" / "pages" / "pages__home__index.css"
    html = html_path.read_text(encoding="utf-8")
    css = page_css.read_text(encoding="utf-8")

    assert changed is True
    assert "body { color: red; }" in css
    assert "<style>" not in html
    assert "../../assets/site/base.css" in html
    assert "../../assets/site/pages/pages__home__index.css" in html
