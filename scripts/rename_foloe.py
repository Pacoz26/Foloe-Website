# -*- coding: utf-8 -*-
"""Bulk-rename foloe.html -> index.html across all pages and the generator."""
import os
import glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

targets = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
targets.append(os.path.join(ROOT, "scripts", "gen_products.py"))

changed = []
for f in sorted(set(targets)):
    with open(f, "r", encoding="utf-8") as fh:
        s = fh.read()
    if "foloe.html" in s:
        s2 = s.replace("foloe.html", "index.html")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s2)
        changed.append(os.path.relpath(f, ROOT))

print("updated", len(changed), "files:")
for c in changed:
    print(" -", c)
