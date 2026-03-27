# DNA — Cairo Salon & Solárium (kadernictviuh.cz)

**Typ projektu:** Jednostránkový web kadeřnictví + solárium (landing page)
**Klient:** Cairo Salon & Solárium, Uherské Hradiště
**Datum dokončení:** 2026-03-27
**GitHub:** supercigan/kadernictviuh

---

## Vizuální archetype

**Exotic Luxe / Cairo Green** — Hluboká botanická zelená s teplým zlatem a krémovým pozadím. Název "Cairo" evokuje exotiku a mezinárodní charakter — tomu odpovídá editoriální serif Cormorant Garamond s výraznými thin/thick kontrasty. Celkový dojem: luxusní salon s osobitým, sofistikovaným charakterem — ne generická pink/nude paleta typická pro kadeřnictví.

---

## Barevná paleta

| Proměnná | Hex | Role |
|----------|-----|------|
| `--deep-green` | `#1A3A2A` | Nav scrolled, přechody |
| `--deep-green-d` | `#102518` | Hero pozadí, kontakt, footer |
| `--deep-green-m` | `#243F30` | Tmavé prvky |
| `--emerald` | `#2D6A4F` | Akcenty v textu, em tagy |
| `--gold` | `#C9A84C` | Primární akcent |
| `--gold-d` | `#A88530` | Hover gold |
| `--gold-l` | `#EDD98A` | Světlé gold plochy |
| `--cream` | `#F7F2EA` | Sekce O nás, Galerie pozadí |
| `--warm-white` | `#FDFBF7` | Hlavní pozadí, Solárium |
| `--text-dark` | `#0F2018` | Hlavní text |
| `--text-mid` | `#4A5A52` | Sekundární text |

**Charakter palety:** Botanická zelená + teplé zlato + krémová. V portfoliu zcela unikátní — žádný předchozí projekt nepoužil zelenou jako dominantní barvu.

---

## Typografie

| Řez | Font | Použití |
|-----|------|---------|
| Nadpisy | **Cormorant Garamond** (ital, 300–700) | H1–H4, dekorativní čísla, lightbox |
| Tělo | **Jost** (300–700) | Odstavce, navigace, formulář, labely |

- H1: `clamp(3.2rem, 7vw, 6rem)`, weight 700, line-height 1.15
- H2: `clamp(2.2rem, 4.5vw, 3.4rem)`, weight 600
- Section label: 0.72rem, letter-spacing 0.22em, uppercase, gold linka 32px vlevo (2px)
- Em tagy v nadpisech: italic + `color: var(--emerald)` nebo `var(--gold)`
- **Nav logo text: 1.65rem / 700** — osvědčené proporce
- **Nav logo ikona: 40×40px, SVG 22×22px** — gold čtverec, dark green SVG

Oba fonty **nové v DNA portfoliu** — nebyly použity v žádném předchozím projektu.

---

## Layout a struktura sekcí

```
1. NAV          — Fixed, průhledný → deep green při scrollu (scrollY > 40)
2. HERO         — 100vh deep green, dekorativní grid + radial glow, velké písmeno "C"
                  badge s pulsující tečkou, H1 s italic gold akcentem, 2 CTA,
                  info bar (tel / hodiny / adresa) oddělený border-top
3. O SALONU     — Cream, split header (h2 vlevo / text vpravo), 4 karty s gold border-top
4. SLUŽBY & CENÍK — Deep green sekce, tab widget (Dámské / Pánské / Ostatní)
                   price-grid: 2-sloupcový, dark rows s hover
5. SOLÁRIUM     — Warm-white, split: dekorativní box (velká cena 11 Kč + sun ikona) vlevo,
                  text + features vpravo
6. GALERIE      — Cream, 3×3 grid s reálnými fotkami, hover overlay, lightbox
7. KONTAKT      — Deep green, split: info + hodiny tabulka vlevo / formulář vpravo
8. FOOTER       — Near-black (#050E09), 3 sloupce + social ikony
```

---

## Klíčové UI vzory

- **Hero animace:** CSS `@keyframes heroFadeUp` na hero elementech (ne JS observer) — okamžitá viditelnost
- **Hero dekorace:** CSS grid lines `rgba(gold, 0.07)` + 2 radial glow gradienty + velké průhledné "C" (text-stroke)
- **Hero badge:** pill s pulsující tečkou `@keyframes blink`
- **Section label:** gold linka 32px/2px vlevo + text uppercase 0.72rem 0.22em tracking — konzistentní přechod každé sekce; na centrovných sekcích oboustranné linky (before + after)
- **O salonu karty:** gold `border-top: 3px`, hover `translateY(-6px) + box-shadow`
- **Tab widget:** 3 taby (Dámské/Pánské/Ostatní), aktivní = gold fill; sparse tabu centrovaný grid `max-width: 740px`
- **Price items:** dark row `rgba(15,32,24,0.65)`, hover `rgba(45,106,79,0.35)`, cena v Cormorant Garamond gold
- **Solárium box:** dark gradient + radial gold glow, velká cena `5.5rem Cormorant gold`, sun icon v circle
- **Checkmarky:** `content: '✓'` v gold kroužku s border (ne clip-path hack)
- **Galerie:** `object-fit: cover`, `aspect-ratio: 4/3` (portrait items: 1, 6, 11), hover `scale(1.06)` na img + overlay lupa
- **Lightbox:** fixed overlay, šipky prev/next, klávesnice ←→Esc, počítadlo `X/N`
- **Kontakt hodiny:** tabulka s border oddělením, gold time, dimovaný "Zavřeno"
- **Watermark:** dual-layer SVG pattern, font-size 11px, spacing 220×110, rotate(-25°) — tmavá + světlá vrstva

---

## Scraping fotek (Wix CDN)

**Key insight:** Wix v HTML ukládá jen miniatury (`w_50`). Plné fotky = base URL bez transform params:
```
https://static.wixstatic.com/media/{hash}~mv2.jpg  ← originál, plná velikost
```
Regex pro extrakci ID: `wixstatic\.com/media/([a-zA-Z0-9_]+~mv2\.[a-zA-Z]+)`

Workflow: `tools/scrape_photos.py` → `tools/resize_photos.py` (Pillow, max 1400px, JPEG 82)

---

## Technický stack

- Čistý HTML/CSS/JS — jeden soubor `index.html` + `photos/` složka
- Google Fonts (Cormorant Garamond + Jost)
- Lightbox: vanilla JS (IntersectionObserver + custom lightbox)
- Formulář: lokální simulace success stavu — Formspree ID nutno doplnit
- Deploy: GitHub → supercigan/kadernictviuh → Vercel (automaticky z master)

---

## Co se osvědčilo

- **Botanická zelená jako hero** — v portfoliu unikát, odlišuje od kosmetiky/pedikúry (růžové/mauve tóny)
- **Cormorant Garamond** — luxusní serif s výraznými thin/thick kontrasty, sedí k exotickému názvu
- **Tab widget pro ceník** — kompaktní řešení pro 3 kategorie služeb bez scrollování
- **Wix base URL scraping** — `/v1/fill/` endpoint vrací 400, ale base URL dá originál
- **Dual-layer watermark** — tmavá + světlá vrstva současně, viditelný na zelené i tmavé sekci
- **CSS heroFadeUp místo JS observer** — hero je okamžitě viditelný, animace probíhá přirozeně

## Co se nepovedlo / co příště udělat jinak

- **Wix CDN transform URL** — `w_1200,q_90,enc_auto` vrátí HTTP 400; Wix vyžaduje buď base URL nebo přesný formát z originálu (`w_X,h_Y,al_c,q_85,usm_0.66_1.00_0.01,...`)
- **Galerie ikony v první verzi** — štít, srdce, stack = nedávaly smysl pro kadeřnictví; příště projít ikony před commitem
- **Nízké opacity na tmavých sekcích** — rgba(255,255,255,0.3) pro popisky nesplňuje kontrast; příště začínat s min. 0.65 na dark bg
- **clip-path checkmark hack** — polygon pro checkmark nefunguje spolehlivě; vždy použít `content: '✓'` nebo SVG

---

*Vytvořeno: 2026-03-27*
