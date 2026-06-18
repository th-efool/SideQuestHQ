#!/usr/bin/env python3
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "publish"
COLORS = {
    "1": (255, 99, 132), "2": (255, 159, 64), "3": (255, 205, 86),
    "4": (75, 192, 192), "5": (54, 162, 235), "6": (153, 102, 255),
}


def esc(s):
    return html.escape(str(s), quote=True)


def rel_link(path, base):
    p = (base / path).resolve()
    try:
        return p.relative_to(PUB).as_posix()
    except ValueError:
        return path


def node_text(n, base):
    t = n.get("type", "text")
    if t == "text":
        return n.get("text", "")
    if t == "file":
        f = n.get("file", "")
        p = (base / f).resolve()
        title = Path(f).stem or f
        body = ""
        if p.exists() and p.suffix.lower() in {".md", ".txt"}:
            body = p.read_text(errors="ignore")[:1200]
        return f"[{title}]({esc(rel_link(f, base))})\n\n{body}" if body else f"[{title}]({esc(rel_link(f, base))})"
    if t == "link":
        url = n.get("url", "")
        return f"[{url}]({url})"
    if t == "group":
        return n.get("label", "Group")
    return t


def color(n, alpha=.10):
    c = n.get("color")
    if c in COLORS:
        r, g, b = COLORS[c]
        return f"rgba({r},{g},{b},{alpha})", f"rgb({r},{g},{b})"
    if isinstance(c, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", c):
        return c + "22", c
    return "rgba(148,163,184,.12)", "rgb(148,163,184)"


def render_canvas(path):
    data = json.loads(path.read_text(errors="ignore"))
    nodes, edges = data.get("nodes", []), data.get("edges", [])
    if not nodes:
        return "_Empty canvas._\n"
    minx = min(n.get("x", 0) for n in nodes)
    miny = min(n.get("y", 0) for n in nodes)
    maxx = max(n.get("x", 0) + n.get("width", 260) for n in nodes)
    maxy = max(n.get("y", 0) + n.get("height", 120) for n in nodes)
    pad = 80
    w, h = maxx - minx + pad * 2, maxy - miny + pad * 2
    pos = {n["id"]: n for n in nodes if "id" in n}
    out = [f'<div class="obsidian-canvas" style="overflow:auto;border:1px solid #33415533;border-radius:12px;background:#0f172a08;padding:12px;margin:1rem 0;">',
           f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="min-width:min(100%, {max(640, int(w/2))}px);height:auto;font-family:Inter,system-ui,sans-serif;">',
           '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#64748b"/></marker></defs>']
    for e in edges:
        a, b = pos.get(e.get("fromNode")), pos.get(e.get("toNode"))
        if not a or not b: continue
        x1 = a.get("x",0) - minx + pad + a.get("width",260)/2
        y1 = a.get("y",0) - miny + pad + a.get("height",120)/2
        x2 = b.get("x",0) - minx + pad + b.get("width",260)/2
        y2 = b.get("y",0) - miny + pad + b.get("height",120)/2
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="3" marker-end="url(#arrow)"/>')
    for n in nodes:
        x, y = n.get("x",0)-minx+pad, n.get("y",0)-miny+pad
        nw, nh = n.get("width",260), n.get("height",120)
        fill, stroke = color(n)
        txt = esc(node_text(n, path.parent))
        cls = "group" if n.get("type") == "group" else "node"
        out.append(f'<foreignObject x="{x}" y="{y}" width="{nw}" height="{nh}"><div xmlns="http://www.w3.org/1999/xhtml" class="canvas-{cls}" style="box-sizing:border-box;width:100%;height:100%;overflow:hidden;border:2px solid {stroke};border-radius:10px;background:{fill};padding:10px;color:#0f172a;font-size:14px;line-height:1.35;white-space:pre-wrap;word-break:break-word;"><strong>{esc(n.get("type","text"))}</strong><br/>{txt}</div></foreignObject>')
    out += ["</svg>", "</div>\n"]
    return "\n".join(out)


def rewrite_links():
    pat = re.compile(r"\[\[([^\]|]+\.canvas)(\|[^\]]+)?\]\]")
    for md in PUB.rglob("*.md"):
        s = md.read_text(errors="ignore")
        ns = pat.sub(lambda m: f"[[{m.group(1)}.md{m.group(2) or '|' + m.group(1)}]]", s)
        if ns != s:
            md.write_text(ns)


def main():
    for c in PUB.rglob("*.canvas"):
        title = c.name
        body = f"# {title}\n\n{render_canvas(c)}"
        c.with_name(c.name + ".md").write_text(body)
    rewrite_links()

if __name__ == "__main__":
    main()
