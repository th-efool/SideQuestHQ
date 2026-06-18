#!/usr/bin/env python3
import re
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "publish"
def render_canvas(path):
    rel = path.relative_to(PUB).as_posix()
    return f"```canvas-viewer\n/canvas/{quote(rel)}\n```\n"


def rewrite_links():
    pat = re.compile(r"\[\[([^\]|]+\.canvas)(\|[^\]]+)?\]\]")
    for md in PUB.rglob("*.md"):
        s = md.read_text(errors="ignore")
        ns = pat.sub(lambda m: f"[[{Path(m.group(1)).with_suffix('').as_posix()}{m.group(2) or '|' + m.group(1)}]]", s)
        if ns != s:
            md.write_text(ns)


def main():
    for c in PUB.rglob("*.canvas"):
        title = c.name
        body = f"# {title}\n\n{render_canvas(c)}"
        c.with_suffix(".md").write_text(body)
    rewrite_links()

if __name__ == "__main__":
    main()
