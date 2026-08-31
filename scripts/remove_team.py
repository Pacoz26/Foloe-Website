# -*- coding: utf-8 -*-
"""Remove all Core Team (陶鑫 / 龚大卫) content and links."""
import os
import re
import glob

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

TEAM_LINK_RE = re.compile(
    r'\n[ \t]*<li><a href="(?:\.\./)?about\.html#team">核心团队</a></li>'
)

INDEX_TEAM_RE = re.compile(
    r'\n[ \t]*<!-- ===== 核心团队 ===== -->\n'
    r'[ \t]*<section class="section alt" id="team">\n'
    r'.*?'
    r'[ \t]*</section>\n',
    re.DOTALL
)

ABOUT_TEAM = '''                <h2 class="mc-sub" id="team">核心团队 <small>Core Team</small></h2>
                <div class="team-grid">
                    <div class="team-card">
                        <div class="avatar">陶</div>
                        <div>
                            <h3>陶鑫</h3>
                            <div class="role">总经理 · 负责技术与产品开发</div>
                            <p>复旦大学 材料物理与化学专业；曾就任于上海瞻芯半导体、橙河微系统；主导开发多款微纳金属3D打印机与数码显微镜产品。</p>
                        </div>
                    </div>
                    <div class="team-card">
                        <div class="avatar">龚</div>
                        <div>
                            <h3>龚大卫</h3>
                            <div class="role">复旦大学 物理学博士</div>
                            <p>曾任复旦大学表面物理国家重点实验室副教授，韩国/美国博士后研究经历；2003年进入工业界，历任上海先进半导体高级工程师及器件与设计部经理、斯达半导体技术副总裁、中航微电子技术总监、中电科国基南方集团高级技术专家。</p>
                        </div>
                    </div>
                </div>

'''

targets = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
targets.append(os.path.join(ROOT, "scripts", "gen_products.py"))

for f in sorted(set(targets)):
    with open(f, "r", encoding="utf-8") as fh:
        s = fh.read()
    orig = s
    s = TEAM_LINK_RE.sub("", s)  # nav + footer links
    if os.path.basename(f) == "index.html":
        s = INDEX_TEAM_RE.sub("\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
    if os.path.basename(f) == "about.html":
        s = s.replace(ABOUT_TEAM, "", 1)
        s = s.replace("公司简介,核心团队,核心技术", "公司简介,核心技术")
    if s != orig:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        print("updated:", os.path.relpath(f, ROOT))
print("done")
