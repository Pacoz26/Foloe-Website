import os
import sys
from PIL import Image

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
IMG_DIR = os.path.abspath(IMG_DIR)

def dhash(path, hash_size=8):
    """Difference hash (64-bit). Small threshold -> visually near-identical images group together."""
    img = Image.open(path).convert("L").resize((hash_size + 1, hash_size), Image.LANCZOS)
    px = list(img.getdata())
    bits = []
    for row in range(hash_size):
        for col in range(hash_size):
            left = px[row * (hash_size + 1) + col]
            right = px[row * (hash_size + 1) + col + 1]
            bits.append(1 if left > right else 0)
    return sum(bit << i for i, bit in enumerate(bits))

def hamming(a, b):
    return bin(a ^ b).count("1")

def ahash(path, hash_size=8):
    img = Image.open(path).convert("L").resize((hash_size, hash_size), Image.LANCZOS)
    px = list(img.getdata())
    avg = sum(px) / len(px)
    bits = [1 if p > avg else 0 for p in px]
    return sum(bit << i for i, bit in enumerate(bits))

def main():
    files = sorted(f for f in os.listdir(IMG_DIR)
                   if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif")))
    info = {}
    for f in files:
        p = os.path.join(IMG_DIR, f)
        try:
            d = dhash(p)
            a = ahash(p)
            w, h = Image.open(p).size
            info[f] = {"d": d, "a": a, "size": (w, h)}
        except Exception as e:
            print(f"ERR {f}: {e}")

    names = list(info.keys())
    groups = []
    used = set()
    # dHash distance <= 4 -> considered visually duplicate/near-identical
    for i, f1 in enumerate(names):
        for f2 in names[i + 1:]:
            d1, d2 = info[f1]["d"], info[f2]["d"]
            dist = hamming(d1, d2)
            if dist <= 4:
                groups.append((f1, f2, dist, info[f1]["size"], info[f2]["size"]))

    if not groups:
        print("No near-duplicate images found (dHash distance <= 4).")

    print("=== Closest 50 pairs (dHash distance) ===")
    pairs = []
    for i, f1 in enumerate(names):
        for f2 in names[i + 1:]:
            pairs.append((hamming(info[f1]["d"], info[f2]["d"]), f1, f2))
    for dist, f1, f2 in sorted(pairs)[:50]:
        print(f"{dist:2d}  {f1}  <->  {f2}")

if __name__ == "__main__":
    main()
