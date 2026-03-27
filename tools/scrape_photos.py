"""
Scrape photos from Wix-based kadernictviuh.cz
Extrahuje Wix media ID z HTML, rekonstruuje URL plných fotek (w_1200),
filtruje příliš malé soubory a ikony, ukládá do photos/.
"""

import os
import re
import sys
import json
import urllib.request
import urllib.parse

SOURCE_URL  = "https://www.kadernictviuh.cz/"
OUTPUT_DIR  = os.path.join(os.path.dirname(__file__), "..", "photos")
MIN_SIZE    = 25 * 1024   # 25 kB — jen skutečné fotky (ne ikony/loga)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": SOURCE_URL,
}

# Hashe které chceme přeskočit (logo, ikony sociálních sítí, …)
# — poznáme je podle prefixu nebo přímo z URL kontextu
SKIP_CONTEXTS = re.compile(
    r'(logo|icon|social|badge|btn|arrow|sprite|pixel|favicon|star|rating)',
    re.IGNORECASE
)


def fetch(url, binary=False):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as r:
            return (r.read(), r.geturl())
    except Exception as e:
        print(f"  [FAIL] {url[:80]} — {e}")
        return (None, url)


def wix_full_url(media_id):
    """Wix CDN: base URL bez transformů = originální soubor v plné velikosti."""
    return f"https://static.wixstatic.com/media/{media_id}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- 1. Stáhni HTML hlavní stránky ---
    print(f"Stahuji stránku: {SOURCE_URL}")
    html_bytes, real_url = fetch(SOURCE_URL)
    if html_bytes is None:
        print("Stránka nedostupná.")
        sys.exit(1)
    html = html_bytes.decode("utf-8", errors="replace")

    # --- 2. Extrahuj všechny Wix media ID ---
    media_ids = list(dict.fromkeys(
        re.findall(r'wixstatic\.com/media/([a-zA-Z0-9_]+~mv2\.[a-zA-Z]+)', html)
    ))
    print(f"Nalezeno {len(media_ids)} unikátních Wix media ID.\n")

    # --- 3. Zkus také JSON blob (Wix ukládá data stránky do <script>) ---
    # Hledáme imageUri / mediaId / src hodnoty v JSON datových blocích
    json_ids = re.findall(
        r'"(?:uri|src|imageUri|mediaId)"\s*:\s*"([a-zA-Z0-9_]+~mv2\.[a-zA-Z]+)"',
        html
    )
    for jid in json_ids:
        if jid not in media_ids:
            media_ids.append(jid)
    print(f"Po prohledání JSON dat: {len(media_ids)} unikátních ID.\n")

    # --- 4. Stáhni každý v plné velikosti ---
    counter = 1
    saved   = []

    for media_id in media_ids:
        url = wix_full_url(media_id)

        # Přeskoč zjevné ikony/loga podle kontextu v HTML
        # Najdi kontext media_id v HTML
        ctx_match = re.search(
            r'.{0,120}' + re.escape(media_id.split('~')[0]) + r'.{0,120}',
            html
        )
        ctx = ctx_match.group(0) if ctx_match else ""
        if SKIP_CONTEXTS.search(ctx):
            print(f"  [SKIP ctx] {media_id}")
            continue

        data, _ = fetch(url, binary=True)
        if data is None:
            continue

        size = len(data)
        if size < MIN_SIZE:
            print(f"  [SMALL {size//1024}kB] {media_id}")
            continue

        ext = "jpg" if media_id.endswith(".jpg") else "png"
        out = os.path.join(OUTPUT_DIR, f"foto-{counter}.{ext}")
        with open(out, "wb") as f:
            f.write(data)
        print(f"  [OK] foto-{counter}.{ext}  ({size//1024} kB)  ← {media_id}")
        saved.append(f"foto-{counter}.{ext}")
        counter += 1

    print(f"\n=== Staženo celkem: {len(saved)} fotek ===")
    for s in saved:
        print(f"  photos/{s}")
    return saved


if __name__ == "__main__":
    main()
