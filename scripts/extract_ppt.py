import os
import re
import zipfile
import xml.etree.ElementTree as ET

PPTX = r"c:\Users\zbj\Documents\Website\Foloe-Website\上海复乐思仪器有限公司技术产品介绍20260526.pptx"
NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

def rels_map(z, slide_path):
    """Map rId -> target for a slide."""
    rels_path = slide_path.replace("slides/", "slides/_rels/") + ".rels"
    m = {}
    if rels_path in z.namelist():
        root = ET.fromstring(z.read(rels_path))
        for rel in root:
            m[rel.get("Id")] = rel.get("Target")
    return m

def main():
    z = zipfile.ZipFile(PPTX)
    slides = sorted([n for n in z.namelist()
                     if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                    key=lambda n: int(re.search(r"(\d+)", n).group(1)))
    print(f"Total slides: {len(slides)}\n")
    for sp in slides:
        num = re.search(r"slide(\d+)\.xml", sp).group(1)
        root = ET.fromstring(z.read(sp))
        # extract all text
        texts = []
        for t in root.iter():
            tag = t.tag.split("}")[-1]
            if tag == "t" and t.text and t.text.strip():
                texts.append(t.text.strip())
        # image references
        rmap = rels_map(z, sp)
        imgs = []
        for blip in root.iter():
            tag = blip.tag.split("}")[-1]
            if tag == "blip":
                rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                if rid and rid in rmap:
                    imgs.append(os.path.basename(rmap[rid]))
        print(f"--- Slide {num} ---")
        print("  text: " + " | ".join(texts)[:600])
        print("  imgs: " + ", ".join(imgs))
        print()
    z.close()

if __name__ == "__main__":
    main()
