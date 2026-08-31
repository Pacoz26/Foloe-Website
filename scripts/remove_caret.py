# -*- coding: utf-8 -*-
"""Remove the caret triangles (▾) from the top-nav dropdown items."""
import os
import glob

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

targets = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
targets.append(os.path.join(ROOT, "scripts", "gen_products.py"))

old = ' <span class="caret">▾</span>'
changed = 0
for f in sorted(set(targets)):
    with open(f, "r", encoding="utf-8") as fh:
        s = fh.read()
    if old in s:
        s = s.replace(old, "")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        changed += 1
        print("updated:", os.path.relpath(f, ROOT))
print("changed", changed, "files")
