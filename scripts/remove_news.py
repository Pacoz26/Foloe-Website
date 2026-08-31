# -*- coding: utf-8 -*-
"""Remove the whole 新闻中心 tab and its correspondents."""
import os
import re
import glob

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

NAV_NEWS_RE = re.compile(
    r'\n[ \t]*<li class="has-sub">\n'
    r'[ \t]*<a href="(?:\.\./)?news\.html">新闻中心</a>\n'
    r'[ \t]*<ul class="dropdown">\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html">企业新闻</a></li>\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html#industry">行业动态</a></li>\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html#tech">技术交流</a></li>\n'
    r'[ \t]*</ul>\n'
    r'[ \t]*</li>'
)

FOOTER_NEWS_RE = re.compile(
    r'\n[ \t]*<div>\n'
    r'[ \t]*<h4>新闻中心</h4>\n'
    r'[ \t]*<ul>\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html">企业新闻</a></li>\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html#industry">行业动态</a></li>\n'
    r'[ \t]*<li><a href="(?:\.\./)?news\.html#tech">技术交流</a></li>\n'
    r'[ \t]*</ul>\n'
    r'[ \t]*</div>'
)

HOME_NEWS_RE = re.compile(
    r'\n[ \t]*<!-- ===== 新闻中心 ===== -->\n'
    r'[ \t]*<section class="section alt">\n'
    r'.*?'
    r'[ \t]*</section>\n',
    re.DOTALL
)

targets = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
targets.append(os.path.join(ROOT, "scripts", "gen_products.py"))

for f in sorted(set(targets)):
    with open(f, "r", encoding="utf-8") as fh:
        s = fh.read()
    orig = s
    s = NAV_NEWS_RE.sub("", s)
    s = FOOTER_NEWS_RE.sub("", s)
    if os.path.basename(f) == "index.html":
        s = HOME_NEWS_RE.sub("\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
    if s != orig:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        print("updated:", os.path.relpath(f, ROOT))

p = os.path.join(ROOT, "news.html")
if os.path.exists(p):
    os.remove(p)
    print("deleted: news.html")
print("done")
