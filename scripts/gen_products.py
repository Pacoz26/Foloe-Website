# -*- coding: utf-8 -*-
"""Generate the 14 product detail pages from PPT-derived data."""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDIR = os.path.join(ROOT, "products")
os.makedirs(PDIR, exist_ok=True)

CATS = {
    1: "智能化高精度加工检测设备",
    2: "专用控制板卡与工业控制软件",
    3: "科学仪器与设备",
}

PRODUCTS = [
    # (key, name, category, summary, images, params[(label,value)], applications[..])
    ("pogopin-probe-insertion-machine", "PogoPin探针卡植针机", 1,
     "兼容直径0.2–2mm，装配公差≤0.01mm，组装速度1,500 pcs/hr，自动化柔性生产。",
     ["p1-pogopin-insert-1.jpg", "p1-pogopin-insert-2.jpg", "p1-pogopin-insert-3.jpg"],
     [("兼容范围", "直径0.2–2mm，支持20+款探针型号"),
      ("组装精度", "装配公差 ≤ 0.01mm"),
      ("组装速度", "1,500 pcs/hr（2–3倍人工效率）"),
      ("控制方式", "自动化柔性生产，参数化配置")],
     ["半导体测试探针卡制造", "IC测试插座装配"]),

    ("pogopin-probe-assembly-insertion-machine", "PogoPin探针组装与植针一体机", 1,
     "自动打点、插接、铆合、植针一体化，探针制造全流程自动化。",
     ["p2-assembly-insert-1.png", "p2-assembly-insert-2.png", "p2-assembly-insert-3.png"],
     [("功能", "自动打点、插接、铆合、植针一体化"),
      ("最小零件尺寸", "≤ 0.05mm"),
      ("装配公差", "≤ 0.01mm"),
      ("集成度", "探针制造全流程自动化")],
     ["高密度探针批量制造", "精密探针组件自动化装配"]),

    ("semi-automatic-pogopin-dispensing-assembly-machine", "半自动PogoPin探针打点组装机", 1,
     "手动辅助探针打点与组装，支持完全离线独立运行，适配小批量试制。",
     ["p3-semi-auto-1.jpg", "p3-semi-auto-2.jpg"],
     [("功能", "手动辅助探针打点与组装"),
      ("工作模式", "支持完全离线独立运行"),
      ("最小零件尺寸", "≤ 0.05mm"),
      ("装配公差", "≤ 0.01mm")],
     ["小批量探针定制加工", "实验室与研发试制场景"]),

    ("automatic-pogopin-dispensing-assembly-machine", "全自动PogoPin探针打点组装机", 1,
     "在搭载半自动探针组装机的基础上实现全自动探针组装，上位机调节，极大节省人工成本。",
     ["p4-auto-1.jpg", "p4-auto-2.jpg", "p4-auto-3.jpg", "p4-auto-4.png"],
     [("功能", "在搭载半自动探针组装机的基础上实现全自动探针组装"),
      ("控制方式", "上位机调节打点位置、速度、组装模式等"),
      ("数据记录", "自动记录组装时间、故障次数、良品率")],
     ["探针组件自动化装配", "探针批量化生产"]),

    ("probe-inspection-sorter", "探针综合检料仪", 1,
     "机器视觉自动识别，探针计数 + 外形质量检测，服务来料检验与质量控制。",
     ["p5-inspection-1.png", "p5-inspection-2.png"],
     [("检测项目", "探针计数 + 外形质量检测"),
      ("检测方式", "机器视觉自动识别"),
      ("适用场景", "来料检验与质量控制")],
     ["探针来料批量检验", "生产过程质量管控"]),

    ("thermal-compression-bonding-module", "芯片封装热压贴头焊机模块", 1,
     "芯片吸附、角度控制与水平调节，精确升降温，支持银浆固化工艺。",
     ["p6-bonding-1.png", "p6-bonding-2.png"],
     [("功能", "芯片吸附、角度控制、水平调节"),
      ("温度控制", "精确升降温，支持银浆固化工艺"),
      ("压力控制", "实时压力检测与反馈"),
      ("仿真能力", "热传导有限元模型验证温度均匀性")],
     ["高精度贴片机（微型片状元器件）", "半导体封装设备效率提升"]),

    ("probe-force-tester", "全自动探针针压测试仪", 1,
     "Excel坐标输入 + 视觉图像识别，高效准确的全自动针压测量，三维图形输出。",
     ["p7-force-1.jpg", "p7-force-2.jpg", "p7-force-3.png"],
     [("功能", "探针卡针压测量，全自动对针"),
      ("技术亮点", "Excel坐标输入 + 视觉图像识别，三维图形输出"),
      ("测力范围", "0.1–10g"),
      ("测力精度", "±0.01g"),
      ("测量针压行程", "1μm–200μm")],
     ["晶圆测试中MEMS探针卡探针弹力测试", "探针故障测试"]),

    ("multi-axis-motion-controller", "步进电机多路驱控一体卡", 2,
     "较传统控制器缩小体积，实现多路控制、多种控制方式、精准调节。",
     ["p8-motion-1.png", "p8-motion-2.png"],
     [("技术亮点", "较传统控制器缩小体积，多路控制、多种控制方式、精准调节"),
      ("通信方式", "WiFi无线控制 / 有线控制")],
     ["显微镜电动载物台", "光学调整架", "自动化测试系统"]),

    ("multi-channel-ad-da-card", "多通道AD/DA采集卡", 2,
     "单板100通道 AD/DA，12位精度，支持多板并联扩展，弹簧探针接触简化互联。",
     ["p9-adda.jpg"],
     [("通道数量", "单板100通道 AD/DA"),
      ("扩展性", "支持多板并联扩展"),
      ("分辨率", "12位精度"),
      ("输入输出范围", "0–10V / -5V–5V / -10V–0V"),
      ("接口方式", "弹簧探针接触，简化互联结构")],
     ["多通道信号采集系统", "工业自动化数据采集"]),

    ("htol-test-card", "IC与功率器件高温老化测控卡", 2,
     "40组独立控制通道，25–175°C双向PID控温，多设备联网监控。",
     ["p10-htol-1.jpg", "p10-htol-2.jpg"],
     [("适用器件", "IC / MOSFET / IGBT / SiC MOSFET"),
      ("单卡工位", "40组独立控制通道"),
      ("系统规模", "最多扩展至200个控制卡"),
      ("温控范围", "25–175°C，支持升降双向PID控温"),
      ("软件功能", "上位机自动启停，多设备联网监控")],
     ["功率半导体器件可靠性测试", "批次老化筛选与质量验证"]),

    ("magnetic-levitation-stiffness-tester", "磁悬浮转子三维刚度测试仪", 3,
     "定位精度0.01mm，三维力测量±50N，服务人工心脏与磁悬浮轴承测试。",
     ["p12-maglev-1.png", "p12-maglev-2.png"],
     [("定位精度", "0.01mm"),
      ("三维力测量", "±50N，精度 ±0.1N"),
      ("转速测试", "0.01–800 rpm 反电势测量"),
      ("测试对象", "磁悬浮转子刚度特性")],
     ["人工心脏（血泵）研发与产品检测", "磁悬浮轴承性能测试"]),

    ("micro-nano-3d-metal-printer", "微纳三维金属加工设备", 3,
     "微米/亚微米级 3D增材制造，室温大气环境直接成型，精确定位、原位加工。",
     ["p13-micronano-1.jpg", "p13-micronano-2.png", "p13-micronano-3.jpg",
      "p13-micronano-4.png", "p13-micronano-5.jpg", "p13-micronano-6.jpg"],
     [("加工精度", "微米/亚微米级 3D增材制造"),
      ("材料体系", "铜、锌、镍、铂等金属"),
      ("工艺条件", "室温大气环境直接成型"),
      ("定位方式", "精确定位，原位加工")],
     ["高密度IC探针卡 / 射频芯片探针卡", "高密度芯片互联与引线键合",
      "神经探针 / 脑机接口微电极", "微型器件（同轴接头/电感/变压器/MEMS）"]),

    ("smart-multi-core-cable-tester", "智能多芯线缆测试仪", 3,
     "100芯线束快速自动检测，内置100V绝缘耐压测试，图形化显示与自动报告。",
     ["p14-cable.png"],
     [("测试容量", "100芯线束快速自动检测"),
      ("耐压测试", "内置100V绝缘耐压测试"),
      ("功能", "电阻测量、绝缘性能测试"),
      ("架构", "主从机分布式测试系统"),
      ("输出", "图形化显示，自动生成测试报告")],
     ["现场复杂多芯线束检修与维护", "船舶、飞机等大型装备线缆检测", "军用装备维护与抢修"]),
]


def products_dropdown(current_key):
    rows = []
    for cat_id in (1, 2, 3):
        rows.append('<li><a class="group" href="../products.html#cat{0}">{1}</a></li>'.format(cat_id, CATS[cat_id]))
        items = [p for p in PRODUCTS if p[2] == cat_id]
        shown = items[:2]
        cur = [p for p in items if p[0] == current_key]
        if cur and cur[0] not in shown:
            shown[1] = cur[0]
        for p in shown:
            key, name = p[0], p[1]
            cls = ' class="current"' if key == current_key else ''
            rows.append('<li><a{0} href="{1}.html">{2}</a></li>'.format(cls, key, name))
        rows.append('<li><a class="more" href="../products.html#cat{0}">更多...</a></li>'.format(cat_id))
    return "".join(rows)


def header(title, keywords, current_key=None):
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 上海复乐思仪器有限公司</title>
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
    <div class="container">
        <nav class="navbar">
            <a class="logo" href="../index.html">
                <img src="../images/company_logo.png" alt="上海复乐思仪器有限公司">
                <span class="brand-text">
                    <span class="cn">上海复乐思仪器有限公司</span>
                    <span class="en">Shanghai Foloe Instrument Co., Ltd.</span>
                </span>
            </a>
            <button class="nav-toggle" aria-label="切换导航"><span></span><span></span><span></span></button>
            <ul class="nav-menu">
                <li><a href="../index.html">首页</a></li>
                <li class="has-sub">
                    <a href="../about.html">关于我们</a>
                    <ul class="dropdown">
                        <li><a href="../about.html">公司简介</a></li>
                        <li><a href="../about.html#tech">核心技术栈</a></li>
                        <li><a href="../about.html#partners">合作伙伴</a></li>
                    </ul>
                </li>
                <li class="has-sub active">
                    <a href="../products.html">产品中心</a>
                    <ul class="dropdown">
                        {products_dropdown}
                    </ul>
                </li>
                <li><a href="../contact.html">联系我们</a></li>
            </ul>
            <div class="nav-right">
                <span class="lang"><span class="cn">中文</span> | EN</span>
            </div>
        </nav>
    </div>
</header>
""".format(title=title, keywords=keywords, products_dropdown=products_dropdown(current_key))


def banner(name, crumb):
    return """
<section class="page-banner">
    <div class="container">
        <h1>{name}</h1>
        <div class="crumbs">{crumb}</div>
    </div>
</section>
""".format(name=name, crumb=crumb)


def footer():
    return """
<footer class="footer">
    <div class="container">
        <div class="top">
            <div class="brand">
                <div class="name">上海复乐思仪器有限公司</div>
                <p style="color:#b9b9b9;">Shanghai Foloe Instrument Co., Ltd.<br>精密制造 · 智能检测 · 科学仪器</p>
            </div>
            <div>
                <h4>关于我们</h4>
                <ul>
                    <li><a href="../about.html">公司简介</a></li>
                    <li><a href="../about.html#tech">核心技术栈</a></li>
                    <li><a href="../about.html#partners">合作伙伴</a></li>
                </ul>
            </div>
            <div>
                <h4>产品中心</h4>
                <ul>
                    <li><a href="../products.html#cat1">智能化高精度加工检测设备</a></li>
                    <li><a href="../products.html#cat2">专用控制板卡与工业控制软件</a></li>
                    <li><a href="../products.html#cat3">科学仪器与设备</a></li>
                </ul>
            </div>
            <div>
                <h4>联系我们</h4>
                <ul class="contact">
                    <li><span class="k">电话</span><span>13916754256</span></li>
                    <li><span class="k">邮箱</span><span>taoxin@foloe.cn</span></li>
                    <li><span class="k">地址</span><span>上海市青浦区双联路168号复襄公社</span></li>
                </ul>
            </div>
        </div>
        <div class="bottom">
            <span>Copyright © 2026 上海复乐思仪器有限公司 All Rights Reserved.</span>
            <a href="https://beian.miit.gov.cn/" class="beian-link"><img src="../images/logopolice.png" alt="备案图标" class="beian-icon">沪ICP备2023010105号</a>
        </div>
    </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>
"""


def sidebar(cur_cat, cur_key):
    rows = []
    for cat_id in (1, 2, 3):
        rows.append('<li>')
        rows.append('<a class="cat-link" href="../products.html#cat{0}">{1}</a>'.format(cat_id, CATS[cat_id]))
        rows.append('<ul class="side-sub">')
        for p in PRODUCTS:
            if p[2] == cat_id:
                key, name = p[0], p[1]
                cls = ' class="cur"' if key == cur_key else ''
                rows.append('<li><a{0} href="{1}.html">{2}</a></li>'.format(cls, key, name))
        rows.append('</ul>')
        rows.append('</li>')
    return '<aside class="side"><div class="side-title">产品中心</div><ul class="side-root">{}</ul></aside>'.format("".join(rows))


def gallery(key, images, name):
    if not images:
        return ""
    if key == "thermal-compression-bonding-module":
        main = '<img id="mainImage" src="../images/{0}" alt="{1}" class="pos-1">'.format(images[0], name)
        thumbs = []
        for idx, i in enumerate(images):
            on = ' on' if idx == 0 else ''
            thumbs.append('<img src="../images/{0}" alt="{1}" class="{2}" data-full="../images/{0}" onclick="switchImage(this, \'pos-{3}\')">'.format(
                i, name, on.strip(), idx + 1))
    else:
        main = '<img src="../images/{0}" alt="{1}">'.format(images[0], name)
        thumbs = []
        for idx, i in enumerate(images):
            on = ' on' if idx == 0 else ''
            thumbs.append('<img src="../images/{0}" alt="{1}" class="{2}" data-full="../images/{0}">'.format(i, name, on.strip()))
    return """
<div class="pd-gallery">
    <div class="main-pic">{main}</div>
    <div class="thumbs">{thumbs}</div>
</div>""".format(main=main, thumbs="".join(thumbs))


def gen_page(p):
    key, name, cat, summary, images, params, apps = p
    cat_name = CATS[cat]
    rows = "".join('<tr><th>{0}</th><td>{1}</td></tr>'.format(k, v) for k, v in params)
    app_li = "".join('<li>{0}</li>'.format(a) for a in apps)
    crumb = '<a href="../index.html">首页</a> &gt; <a href="../products.html">产品中心</a> &gt; <a href="../products.html#cat{0}">{1}</a> &gt; {2}'.format(cat, cat_name, name)

    html = header(name, name, current_key=key) + banner(name, crumb) + """
<div class="container">
    <div class="page-wrap">
        {side}
        <main class="main-col">
            <h2 class="mc-title">{name} <small>{cat_name}</small></h2>
            <div class="pd-wrap">
                {gallery}
                <div class="pd-info">
                    <span class="pd-cat">{cat_name}</span>
                    <h1>{name}</h1>
                    <p class="summary">{summary}</p>
                    <div class="pd-block">
                        <h3>核心技术参数</h3>
                        <table>{rows}</table>
                    </div>
                    <div class="pd-block">
                        <h3>应用领域</h3>
                        <ul class="app">{app_li}</ul>
                    </div>
                    <a class="btn btn-green" href="../contact.html">联系我们</a>
                </div>
            </div>
        </main>
    </div>
</div>
""".format(side=sidebar(cat, key), name=name, cat_name=cat_name,
           gallery=gallery(key, images, name), summary=summary, rows=rows, app_li=app_li)
    html += footer()
    with open(os.path.join(PDIR, key + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("generated:", key + ".html")


for p in PRODUCTS:
    gen_page(p)
print("done:", len(PRODUCTS), "pages")
