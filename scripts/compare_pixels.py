import os
from PIL import Image
import numpy as np

IMG_DIR = r"c:\Users\zbj\Documents\Website\Foloe-Website\images"

def feat(path):
    im = Image.open(path).convert("L").resize((32, 32), Image.LANCZOS)
    a = np.asarray(im, dtype=np.float32).flatten()
    a = (a - a.mean()) / (a.std() + 1e-6)
    return a

def main():
    files = sorted(f for f in os.listdir(IMG_DIR)
                   if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
    dims = {}
    feats = {}
    for f in files:
        p = os.path.join(IMG_DIR, f)
        with Image.open(p) as im:
            dims[f] = (im.size[0], im.size[1], im.format, im.mode)
        feats[f] = feat(p)

    print("=== All images (w x h, format, mode) ===")
    for f in files:
        w, h, fmt, mode = dims[f]
        print(f"{w:5d}x{h:<5d} {fmt:5s} {mode:6s}  {f}")

    print("\n=== Highest-similarity pairs (correlation > 0.90) ===")
    names = list(feats.keys())
    hits = []
    for i, f1 in enumerate(names):
        for f2 in names[i + 1:]:
            corr = float(np.dot(feats[f1], feats[f2]))
            if corr > 0.90:
                hits.append((corr, f1, f2))
    if not hits:
        print("(none found above 0.90)")
    for corr, f1, f2 in sorted(hits, reverse=True):
        print(f"{corr:.4f}  {f1}  <->  {f2}")

if __name__ == "__main__":
    main()
