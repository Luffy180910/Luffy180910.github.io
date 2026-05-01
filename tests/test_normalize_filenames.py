from __future__ import annotations

from tests.conftest import load_script_module


def test_slugify_stem_handles_ascii_and_unicode():
    module = load_script_module("normalize_filenames")

    assert module.slugify_stem("Hello, World!") == "hello-world"
    assert module.slugify_stem("春游 梅花山") == "春游-梅花山"


def test_build_replacements_covers_known_asset_prefixes():
    module = load_script_module("normalize_filenames")

    replacements = module.build_replacements(
        {
            "assets/blog/images/Old Name.png": "assets/blog/images/old-name.png",
            "assets/video/My Clip.mp4": "assets/video/my-clip.mp4",
            "assets/genshin/角色 图.png": "assets/genshin/角色-图.png",
        }
    )

    assert replacements["assets/blog/images/Old Name.png"] == "assets/blog/images/old-name.png"
    assert replacements["/assets/blog/images/Old Name.png"] == "/assets/blog/images/old-name.png"
    assert replacements["/assets/video/My Clip.mp4"] == "/assets/video/my-clip.mp4"
    assert replacements["./角色 图.png"] == "./角色-图.png"


def test_replace_in_text_files_updates_matching_references(tmp_path, monkeypatch):
    module = load_script_module("normalize_filenames")
    monkeypatch.setattr(module, "ROOT", tmp_path)

    page = tmp_path / "pages" / "sample.html"
    page.parent.mkdir(parents=True)
    page.write_text('<img src="/assets/video/My Clip.mp4">', encoding="utf-8")

    changed = module.replace_in_text_files({"/assets/video/My Clip.mp4": "/assets/video/my-clip.mp4"})

    assert changed == 1
    assert page.read_text(encoding="utf-8") == '<img src="/assets/video/my-clip.mp4">'
