# -*- coding: utf-8 -*-
"""Point the site at the renamed logo company_logo.png."""
import os
import glob

ROOT = r"c:\Users\zbj\Documents\Website\Foloe-Website"

# 1. Rename images/logo.png -> images/company_logo.png (same image)
old_file = os.path.join(ROOT, "images", "logo.png")
new_file = os.path.join(ROOT, "images", "company_logo.png")
if os.path.exists(old_file) and not os.path.exists(new_file):
    os.rename(old_file, new_file)
    print("renamed:", os.path.relpath(old_file, ROOT), "->", os.path.relpath(new_file, ROOT))
elif os.path.exists(new_file):
    print("already exists:", new_file)

# 2. Update references
targets = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
targets.append(os.path.join(ROOT, "scripts", "gen_products.py"))
count = 0
for f in sorted(set(targets)):
    with open(f, "r", encoding="utf-8") as fh:
        s = fh.read()
    if "logo.png" in s:
        s = s.replace("logo.png", "company_logo.png")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        count += 1
        print("updated:", os.path.relpath(f, ROOT))
print("updated", count, "files")
