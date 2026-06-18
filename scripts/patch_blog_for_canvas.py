#!/usr/bin/env python3
import shutil, sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
blog = Path(sys.argv[1]) if len(sys.argv) > 1 else root
pub = root / "publish"
public = blog / "public"
public.mkdir(parents=True, exist_ok=True)
shutil.copyfile(root / "canvas_viewer.html", public / "canvas_viewer.html")
canvas_dir = public / "canvas"
if canvas_dir.exists():
    shutil.rmtree(canvas_dir)
for src in pub.rglob("*.canvas"):
    dst = canvas_dir / src.relative_to(pub)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)

p = blog / "lib" / "markdownToHtml.ts"
s = p.read_text()
old = ".use(rehypeRewrite, { selector: 'a', rewrite: async (node) => rewriteLinkNodes(node, linkNodeMapping, currSlug) })"
new = ".use(rehypeRewrite, { selector: 'a, pre', rewrite: async (node) => { if (rewriteCanvasNodes(node)) return; rewriteLinkNodes(node, linkNodeMapping, currSlug) } })"
if old in s:
    s = s.replace(old, new)
marker = "function rewriteLinkNodes"
fn = """function rewriteCanvasNodes(node) { if (node.type !== 'element' || node.tagName !== 'pre') return false; const code = node.children?.[0]; const cls = code?.properties?.className || []; if (code?.tagName !== 'code' || !cls.includes('language-canvas-viewer')) return false; const src = String(code.children?.[0]?.value || '').trim(); if (!src) return false; node.tagName = 'iframe'; node.properties = { src: `/canvas_viewer.html?src=${encodeURIComponent(src)}`, style: 'width:100%;height:80vh;border:0;border-radius:12px;', loading: 'lazy' }; node.children = []; return true; } """
if "function rewriteCanvasNodes" not in s:
    s = s.replace(marker, fn + marker)
p.write_text(s)
