# -*- coding: utf-8 -*-
"""Add company logo (图片1.png) in front of the brand text, without moving the words."""
import os
import shutil

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

# 1. Copy the logo to a clean path
src = os.path.join(ROOT, "图片1.png")
dst = os.path.join(ROOT, "images", "logo.png")
shutil.copyfile(src, dst)
print("copied logo ->", dst)

ROOT_PAGES = ["index.html", "about.html", "contact.html", "news.html", "products.html", "search.html"]

ROOT_OLD = (
    '<a class="logo" href="index.html">\n'
    '                    <span class="brand-text">'
)
ROOT_NEW = (
    '<a class="logo" href="index.html">\n'
    '                    <img src="images/logo.png" alt="上海复乐思仪器有限公司">\n'
    '                    <span class="brand-text">'
)

for p in ROOT_PAGES:
    path = os.path.join(ROOT, p)
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    if ROOT_OLD not in s:
        print("SKIP (not found):", p)
        continue
    s = s.replace(ROOT_OLD, ROOT_NEW, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print("updated:", p)

# gen_products.py
GEN = os.path.join(ROOT, "scripts", "gen_products.py")
GEN_OLD = (
    '<a class="logo" href="../index.html">\n'
    '                <span class="brand-text">'
)
GEN_NEW = (
    '<a class="logo" href="../index.html">\n'
    '                <img src="../images/logo.png" alt="上海复乐思仪器有限公司">\n'
    '                <span class="brand-text">'
)
with open(GEN, "r", encoding="utf-8") as f:
    g = f.read()
if GEN_OLD in g:
    g = g.replace(GEN_OLD, GEN_NEW, 1)
    with open(GEN, "w", encoding="utf-8") as f:
        f.write(g)
    print("updated: scripts/gen_products.py")
else:
    print("SKIP (not found): scripts/gen_products.py")
print("done")
