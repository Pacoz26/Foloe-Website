# -*- coding: utf-8 -*-
"""Remove the 燃料棒内氦压无损检测设备控制软件 product entirely."""
import os
import re
import glob

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

NAV_HELIUM_RE = re.compile(
    r'\n[ \t]*<li><a href="(?:products/)?helium-pressure-control-software\.html">燃料棒内氦压无损检测设备控制软件</a></li>'
)

HELIUM_ENTRY = '''    ("helium-pressure-control-software", "燃料棒内氦压无损检测设备控制软件", 2,
     "实时采集双通道温度数据，配合PLC实现自动化控制，一键启动11步检测流程。",
     ["p11-helium-1.jpg", "p11-helium-2.jpg", "p11-helium-3.jpg"],
     [("功能", "燃料棒内部氦气压力检测自动化控制系统"),
      ("数据采集", "实时采集双通道温度数据，配合PLC自动化控制"),
      ("自动检测", "一键启动完整的11步检测流程"),
      ("手动控制", "支持7个独立设备动作的手动触发"),
      ("数据管理", "测试记录存储、查询、导出")],
     ["气压检测", "自动化控制"]),

'''

HELIUM_CARD = '''                    <div class="pro-card">
                        <div class="pic"><img src="images/p11-helium-1.jpg" alt="燃料棒内氦压无损检测设备控制软件"></div>
                        <div class="body">
                            <h3>燃料棒内氦压无损检测设备控制软件</h3>
                            <p>双通道温度采集+PLC自动化控制，一键启动11步检测流程。</p>
                            <a class="more" href="products/helium-pressure-control-software.html">了解更多 →</a>
                        </div>
                    </div>
'''

HELIUM_CHIP = '''                        <a href="products/helium-pressure-control-software.html">燃料棒内氦压检测控制软件</a>
'''

# 1. Remove nav item from root pages
for p in ["index.html", "about.html", "contact.html", "products.html"]:
    path = os.path.join(ROOT, p)
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    orig = s
    s = NAV_HELIUM_RE.sub("", s)
    if s != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        print("nav removed:", p)

# 2. products.html: remove the product card
path = os.path.join(ROOT, "products.html")
with open(path, "r", encoding="utf-8") as f:
    s = f.read()
if HELIUM_CARD in s:
    s = s.replace(HELIUM_CARD, "", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print("card removed: products.html")
else:
    print("SKIP card: products.html (not found)")

# 3. index.html: remove the category chip + update product count
path = os.path.join(ROOT, "index.html")
with open(path, "r", encoding="utf-8") as f:
    s = f.read()
s = s.replace(HELIUM_CHIP, "", 1)
s = s.replace("三大产品线 · 十四款核心产品", "三大产品线 · 十三款核心产品")
s = s.replace('data-count="14"', 'data-count="13"')
with open(path, "w", encoding="utf-8") as f:
    f.write(s)
print("index.html: chip + count updated")

# 4. gen_products.py: remove nav item + product entry
path = os.path.join(ROOT, "scripts", "gen_products.py")
with open(path, "r", encoding="utf-8") as f:
    g = f.read()
g = NAV_HELIUM_RE.sub("", g)
g = g.replace(HELIUM_ENTRY, "", 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(g)
print("gen_products.py: nav + entry removed")

# 5. Delete the product detail page
p = os.path.join(ROOT, "products", "helium-pressure-control-software.html")
if os.path.exists(p):
    os.remove(p)
    print("deleted:", os.path.relpath(p, ROOT))
print("done")
