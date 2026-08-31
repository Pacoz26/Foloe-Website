# -*- coding: utf-8 -*-
"""Remove the search feature entirely: forms, search page, and search data."""
import os
import re

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

FORM_RE = re.compile(
    r'\n[ \t]*<form class="search" action="(?:\.\./)?search\.html" method="get">\n'
    r'[ \t]*<input type="text" name="q" placeholder="产品搜索">\n'
    r'[ \t]*<button type="submit">搜索</button>\n'
    r'[ \t]*</form>'
)

root_pages = ["index.html", "about.html", "contact.html", "news.html", "products.html"]
for p in root_pages:
    path = os.path.join(ROOT, p)
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    s2, n = FORM_RE.subn("", s)
    if n:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s2)
        print("updated:", p, "(%d form)" % n)

gen = os.path.join(ROOT, "scripts", "gen_products.py")
with open(gen, "r", encoding="utf-8") as f:
    g = f.read()
g2, n = FORM_RE.subn("", g)
if n:
    with open(gen, "w", encoding="utf-8") as f:
        f.write(g2)
    print("updated: scripts/gen_products.py (%d form)" % n)

for rel in ["search.html", os.path.join("js", "products-data.js")]:
    p = os.path.join(ROOT, rel)
    if os.path.exists(p):
        os.remove(p)
        print("deleted:", rel)
print("done")
