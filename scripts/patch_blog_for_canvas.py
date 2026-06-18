#!/usr/bin/env python3
import re
import shutil
import sys
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

fn = r"""
function rewriteCanvasNodes(node) {
  if (node.type !== 'element' || node.tagName !== 'pre') return false;
  const code = node.children?.[0];
  if (code?.tagName !== 'code') return false;
  const src = String(code.children?.[0]?.value || '').trim();
  if (!/^\/canvas\/.+\.canvas$/i.test(src)) return false;
  node.tagName = 'iframe';
  node.properties = {
    src: `/canvas_viewer.html?src=${encodeURIComponent(src)}`,
    style: 'width:100%;height:80vh;border:0;border-radius:12px;',
    loading: 'lazy',
  };
  node.children = [];
  return true;
}
"""

if "function rewriteCanvasNodes" not in s:
    marker = "function rewriteLinkNodes"
    if marker not in s:
        raise RuntimeError(f"Could not find {marker} in {p}")
    s = s.replace(marker, fn + "\n" + marker, 1)

s, count = re.subn(
    r"\.use\(rehypeRewrite,\s*\{\s*selector:\s*[\'\"]a[\'\"]\s*,\s*rewrite:\s*async\s*\(node\)\s*=>\s*rewriteLinkNodes\(node,\s*linkNodeMapping,\s*currSlug\)\s*,?\s*\}\s*\)",
    ".use(rehypeRewrite, { selector: 'a, pre', rewrite: async (node) => { if (rewriteCanvasNodes(node)) return; rewriteLinkNodes(node, linkNodeMapping, currSlug) } })",
    s,
    count=1,
    flags=re.S,
)

if count == 0 and "selector: 'a, pre'" not in s and 'selector: "a, pre"' not in s:
    raise RuntimeError(f"Could not patch rehypeRewrite selector in {p}")

p.write_text(s)
