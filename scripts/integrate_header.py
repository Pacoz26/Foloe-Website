# -*- coding: utf-8 -*-
"""Integrate the topbar into the header: remove the slogan topbar, move lang/search into the navbar."""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ROOT_PAGES = ["index.html", "about.html", "contact.html", "news.html", "products.html", "search.html"]

# Root pages
ROOT_TOPBAR_OLD = (
    '    <!-- ===== 顶部通栏 ===== -->\n'
    '    <div class="topbar">\n'
    '        <div class="container">\n'
    '            <div class="slogan"><b>精密制造 · 智能检测 · 科学仪器</b><span>致力于成为高端智能装备解决方案提供商</span></div>\n'
    '            <div class="right">\n'
    '                <span class="lang"><span class="cn">中文</span> | EN</span>\n'
    '                <form class="search" action="search.html" method="get">\n'
    '                    <input type="text" name="q" placeholder="产品搜索">\n'
    '                    <button type="submit">搜索</button>\n'
    '                </form>\n'
    '            </div>\n'
    '        </div>\n'
    '    </div>\n'
    '\n'
    '    <!-- ===== 导航 ===== -->\n'
)
ROOT_TOPBAR_NEW = '    <!-- ===== 导航 ===== -->\n'

ROOT_NAV_OLD = (
    '                    <li><a href="contact.html">联系我们</a></li>\n'
    '                </ul>\n'
    '            </nav>\n'
)
ROOT_NAV_NEW = (
    '                    <li><a href="contact.html">联系我们</a></li>\n'
    '                </ul>\n'
    '                <div class="nav-right">\n'
    '                    <span class="lang"><span class="cn">中文</span> | EN</span>\n'
    '                    <form class="search" action="search.html" method="get">\n'
    '                        <input type="text" name="q" placeholder="产品搜索">\n'
    '                        <button type="submit">搜索</button>\n'
    '                    </form>\n'
    '                </div>\n'
    '            </nav>\n'
)

# gen_products.py (product pages)
GEN = os.path.join(ROOT, "scripts", "gen_products.py")
GEN_TOPBAR_OLD = (
    '<div class="topbar">\n'
    '    <div class="container">\n'
    '        <div class="slogan"><b>精密制造 · 智能检测 · 科学仪器</b><span>致力于成为高端智能装备解决方案提供商</span></div>\n'
    '        <div class="right">\n'
    '            <span class="lang"><span class="cn">中文</span> | EN</span>\n'
    '            <form class="search" action="../search.html" method="get">\n'
    '                <input type="text" name="q" placeholder="产品搜索">\n'
    '                <button type="submit">搜索</button>\n'
    '            </form>\n'
    '        </div>\n'
    '    </div>\n'
    '</div>\n'
    '<header class="header">\n'
)
GEN_TOPBAR_NEW = '<header class="header">\n'

GEN_NAV_OLD = (
    '                <li><a href="../contact.html">联系我们</a></li>\n'
    '            </ul>\n'
    '        </nav>\n'
)
GEN_NAV_NEW = (
    '                <li><a href="../contact.html">联系我们</a></li>\n'
    '            </ul>\n'
    '            <div class="nav-right">\n'
    '                <span class="lang"><span class="cn">中文</span> | EN</span>\n'
    '                <form class="search" action="../search.html" method="get">\n'
    '                    <input type="text" name="q" placeholder="产品搜索">\n'
    '                    <button type="submit">搜索</button>\n'
    '                </form>\n'
    '            </div>\n'
    '        </nav>\n'
)


def edit(path, old, new):
    with open(path, "r", encoding="utf-8") as fh:
        s = fh.read()
    if old not in s:
        print("SKIP (not found):", path)
        return False
    s = s.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)
    print("updated:", os.path.relpath(path, ROOT))
    return True


for p in ROOT_PAGES:
    path = os.path.join(ROOT, p)
    edit(path, ROOT_TOPBAR_OLD, ROOT_TOPBAR_NEW)
    edit(path, ROOT_NAV_OLD, ROOT_NAV_NEW)

edit(GEN, GEN_TOPBAR_OLD, GEN_TOPBAR_NEW)
edit(GEN, GEN_NAV_OLD, GEN_NAV_NEW)
print("done")
