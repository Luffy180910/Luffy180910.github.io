#!/usr/bin/env python3
from __future__ import annotations

import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TARGET_DIRS = [
    ROOT / "assets" / "blog" / "images",
    ROOT / "assets" / "blog" / "videos",
    ROOT / "assets" / "video",
    ROOT / "assets" / "genshin",
]
ASSET_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".mp4", ".webm", ".ico"}
TEXT_EXTS = {".html", ".md", ".js", ".css", ".json", ".py"}


def slugify_stem(stem: str) -> str:
    out: list[str] = []
    for ch in stem:
        if ch.isascii():
            if ch.isalnum():
                out.append(ch.lower())
            else:
                out.append("-")
            continue

        cat = unicodedata.category(ch)
        if cat.startswith(("L", "N")):
            out.append(ch)
        else:
            out.append("-")

    slug = "".join(out)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "file"


def rename_assets() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for target in TARGET_DIRS:
        if not target.exists():
            continue
        used: set[str] = set()
        files = sorted([p for p in target.iterdir() if p.is_file()], key=lambda p: p.name)
        for old_path in files:
            if old_path.suffix.lower() not in ASSET_EXTS:
                continue
            ext = old_path.suffix.lower()
            base = slugify_stem(old_path.stem)
            candidate = f"{base}{ext}"
            index = 2
            while candidate in used or (target / candidate).exists() and (target / candidate) != old_path:
                candidate = f"{base}-{index}{ext}"
                index += 1
            used.add(candidate)

            if candidate == old_path.name:
                continue
            new_path = target / candidate
            old_rel = old_path.relative_to(ROOT).as_posix()
            new_rel = new_path.relative_to(ROOT).as_posix()
            old_path.rename(new_path)
            mapping[old_rel] = new_rel
    return mapping


def build_replacements(mapping: dict[str, str]) -> dict[str, str]:
    replacements: dict[str, str] = {}
    for old_rel, new_rel in mapping.items():
        replacements[old_rel] = new_rel

        old_name = Path(old_rel).name
        new_name = Path(new_rel).name

        if old_rel.startswith("assets/blog/images/"):
            replacements[f"/assets/blog/images/{old_name}"] = f"/assets/blog/images/{new_name}"
        if old_rel.startswith("assets/blog/videos/"):
            replacements[f"/assets/blog/videos/{old_name}"] = f"/assets/blog/videos/{new_name}"
        if old_rel.startswith("assets/video/"):
            replacements[f"/assets/video/{old_name}"] = f"/assets/video/{new_name}"
        if old_rel.startswith("assets/genshin/"):
            replacements[f"./{old_name}"] = f"./{new_name}"
            replacements[f"/assets/genshin/{old_name}"] = f"/assets/genshin/{new_name}"

    return replacements


def replace_in_text_files(replacements: dict[str, str]) -> int:
    changed = 0
    text_files = []
    for ext in TEXT_EXTS:
        text_files.extend(ROOT.rglob(f"*{ext}"))

    for path in sorted(set(text_files)):
        if ".git" in path.parts:
            continue
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    mapping = rename_assets()
    if not mapping:
        print("No filename changes needed.")
        return
    replacements = build_replacements(mapping)
    updated_files = replace_in_text_files(replacements)
    print(f"Renamed {len(mapping)} assets and updated {updated_files} text files.")


if __name__ == "__main__":
    main()
