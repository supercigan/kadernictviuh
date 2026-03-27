# Projekt: Cairo Salon & Solárium — kadernictviuh.cz

**Datum zahájení:** 2026-03-26
**Datum dokončení:** 2026-03-27
**Pracovní složka:** C:\Users\karel\weby\kadernictviuh
**GitHub:** supercigan/kadernictviuh (Vercel auto-deploy)

---

## Co je hotovo

- [x] Přečteny DNA soubory všech předchozích projektů
- [x] Proveden scraping a screenshoty originálu kadernictviuh.cz
- [x] Navržena paleta a fonty (Cormorant Garamond + Jost, Deep Green + Gold)
- [x] Vytvořen index.html — kompletní jednostránkový web
- [x] Sekce: Nav, Hero, O Salonu, Služby & Ceník (tab widget), Solárium, Galerie, Kontakt, Footer
- [x] Animace: hero CSS keyframes + fade-up IntersectionObserver pro ostatní sekce
- [x] Responzivita: 960px tablet, 600px mobil, hamburger menu
- [x] Vizuální opravy: kontrast, ikony galerie, checkmarky, spacing karet
- [x] Reálné fotky ze starého webu (14 fotek, Wix CDN scraping)
- [x] Lightbox: šipky, klávesnice ←→Esc, počítadlo
- [x] Watermark: dual-layer SVG pattern "Demoverze – Tomáš Smolík"
- [x] GitHub push (3 commity)
- [x] DNA soubor vytvořen

---

## Informace z originálu

**Firma:** Cairo Salon & Solárium
**Adresa:** Josefa Stancla 153, Uherské Hradiště 1
**Tel:** +420 606 452 190
**Email:** info@kadernictviuh.cz
**Provoz:** Pondělí–Pátek 8:00–18:00
**Produkty:** Goldwell

---

## Vizuální archetype

**Exotic Luxe / Cairo Green**
- Deep botanic green (#1A3A2A) + Cairo gold (#C9A84C) + warm cream (#F7F2EA)
- Cormorant Garamond (nadpisy) + Jost (tělo)
- Oba fonty i zelená jako dominantní barva = unikát v DNA portfoliu

---

## Důležitá rozhodnutí

- Zelená jako hlavní barva — v portfoliu nepoužitá, sedí k luxusnímu/botanickému charakteru
- Cormorant Garamond — exotický editoriální serif odpovídá názvu "Cairo"
- Ceník jako tab widget (Dámské / Pánské / Ostatní) — kompaktní, přehledné
- Wix CDN scraping: base URL bez transform params = originální soubor (key insight)
- Fotky zmenšeny Pillow na max 1400px, JPEG quality 82 (bylo 6–23 MB → 56–240 kB)
- Watermark: dual-layer SVG pattern — tmavá + světlá vrstva = viditelný všude

---

## Co se řeší

- Web dokončen, připraven k předání klientovi

---

## Příští kroky (po předání)

- Smazat watermark (odstranit blok `<!-- WATERMARK -->` v index.html)
- Doplnit Formspree ID do kontaktního formuláře
- Případně doplnit jména kadeřnic
