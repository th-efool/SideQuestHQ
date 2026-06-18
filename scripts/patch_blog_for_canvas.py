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

plugin = r"""
function rehypeCanvasViewer(): any {
  return (tree) => {
    visitCanvasNodes(tree);
  };
}

function visitCanvasNodes(node) {
  if (!node || typeof node !== 'object') return;
  rewriteCanvasNode(node);
  if (Array.isArray(node.children)) {
    node.children.forEach(visitCanvasNodes);
  }
}

function rewriteCanvasNode(node) {
  if (node.type !== 'element' || node.tagName !== 'pre') return;
  const code = node.children?.[0];
  if (code?.type !== 'element' || code.tagName !== 'code') return;
  const src = String(code.children?.[0]?.value || '').trim();
  if (!/^\/canvas\/.+\.canvas$/i.test(src)) return;
  node.tagName = 'iframe';
  node.properties = {
    src: `/canvas_viewer.html?src=${encodeURIComponent(src)}`,
    style: 'width:100%;height:80vh;border:0;border-radius:12px;',
    loading: 'lazy',
  };
  node.children = [];
}
"""

# Replace any older injected canvas helper with the current plugin.
s = re.sub(
    r"\nfunction (?:rewriteCanvasNodes|rehypeCanvasViewer)\([\s\S]*?\n(?=function rewriteLinkNodes)",
    "\n" + plugin + "\n",
    s,
    count=1,
)
if "function rehypeCanvasViewer" not in s:
    marker = "function rewriteLinkNodes"
    if marker not in s:
        raise RuntimeError(f"Could not find {marker} in {p}")
    s = s.replace(marker, plugin + "\n" + marker, 1)

# Ensure canvas conversion runs after sanitize, independent of rehype-rewrite selectors.
if ".use(rehypeCanvasViewer)" not in s:
    s, count = re.subn(
        r"(\.use\(rehypeSanitize\))",
        r"\1\n    .use(rehypeCanvasViewer)",
        s,
        count=1,
    )
    if count == 0:
        raise RuntimeError(f"Could not insert rehypeCanvasViewer after rehypeSanitize in {p}")

# Keep link preview rewriting focused on links only.
s, count = re.subn(
    r"\.use\(rehypeRewrite,\s*\{\s*selector:\s*['\"]a(?:,\s*pre)?['\"]\s*,\s*rewrite:\s*async\s*\(node\)\s*=>\s*(?:\{\s*if\s*\(rewriteCanvasNodes\(node\)\)\s*return;\s*rewriteLinkNodes\(node,\s*linkNodeMapping,\s*currSlug\)\s*\}|rewriteLinkNodes\(node,\s*linkNodeMapping,\s*currSlug\))\s*,?\s*\}\s*\)",
    ".use(rehypeRewrite, {\n      selector: 'a',\n      rewrite: async (node) => rewriteLinkNodes(node, linkNodeMapping, currSlug)\n    })",
    s,
    count=1,
    flags=re.S,
)
if count == 0:
    raise RuntimeError(f"Could not normalize rehypeRewrite call in {p}")

p.write_text(s)
