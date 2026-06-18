#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "publish"


def canvas_src(path):
    rel = path.relative_to(PUB).as_posix()
    return "/canvas/" + quote(rel)


def rewrite_links():
    import re
    pat = re.compile(r"\[\[([^\]|]+\.canvas)(\|[^\]]+)?\]\]")
    for md in PUB.rglob("*.md"):
        s = md.read_text(errors="ignore")
        ns = pat.sub(lambda m: f"[[{Path(m.group(1)).with_suffix('').as_posix()}{m.group(2) or '|' + m.group(1)}]]", s)
        if ns != s:
            md.write_text(ns)


def main():
    for c in PUB.rglob("*.canvas"):
        title = c.stem
        body = f"# {title}\n\n```canvas-viewer\n{canvas_src(c)}\n```\n"
        c.with_suffix(".md").write_text(body)
    rewrite_links()


if __name__ == "__main__":
    main()
