"""
Resize photos pro webovou galerii.
- Max šířka 1400px (zachová aspect ratio)
- Uloží jako JPEG quality=82
- Přeskočí foto-1 (banner) a foto-3 (23MB raw)
"""

import os, sys
from PIL import Image

INPUT_DIR  = os.path.join(os.path.dirname(__file__), "..", "photos")
OUTPUT_DIR = INPUT_DIR  # přepíše originály
MAX_WIDTH  = 1400
MAX_HEIGHT = 1400
QUALITY    = 82
SKIP       = {"foto-1.png", "foto-3.jpg"}  # banner a 23MB raw

files = sorted(f for f in os.listdir(INPUT_DIR) if f.startswith("foto-"))

for fn in files:
    if fn in SKIP:
        print(f"  [SKIP] {fn}")
        continue

    src = os.path.join(INPUT_DIR, fn)
    size_kb = os.path.getsize(src) // 1024

    try:
        img = Image.open(src).convert("RGB")
        w, h = img.size

        # Zmenšit pokud je větší než MAX
        if w > MAX_WIDTH or h > MAX_HEIGHT:
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
            nw, nh = img.size
        else:
            nw, nh = w, h

        # Přejmenuj na .jpg
        out_name = os.path.splitext(fn)[0] + ".jpg"
        out_path = os.path.join(OUTPUT_DIR, out_name)
        img.save(out_path, "JPEG", quality=QUALITY, optimize=True)

        new_kb = os.path.getsize(out_path) // 1024
        print(f"  [OK] {fn} ({size_kb}kB, {w}x{h}) → {out_name} ({new_kb}kB, {nw}x{nh})")

        # Smaž originální PNG pokud byl PNG a výstup je JPG
        if fn != out_name and os.path.exists(src):
            os.remove(src)

    except Exception as e:
        print(f"  [ERR] {fn}: {e}")

print("\nHotovo.")
