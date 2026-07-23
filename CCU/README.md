# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows,
script headers, and tiny highlight accents. The CCU Edition pairs **electric
blue & purple** primaries with a **hot pink** accent and **white** text
over a **black** canvas, distinct from the portfolio's
aquamarine/purple-on-black look while keeping the same Neon Swan style.

## Files

- `css/ccudesign.css` — the theme stylesheet (drop-in; all colors and effects
  exposed as role-based CSS custom properties on `:root`)
- `fonts/` — self-hosted Sacramento 400 and Poppins 300 (woff2, latin +
  latin-ext) — no Google Fonts CDN dependency
- `index.html` — theme preview page demonstrating every element
- `js/accordion.js` — accordion toggle behavior

## Palette

| Role | Color | Hex | Token |
| --- | --- | --- | --- |
| Background | Black | `#000000` | `--ns-bg` |
| Primary — headers / bright accent | Blue | `#11B4F5` | `--ns-primary` |
| Primary — pull-quotes / deep glow | Purple | `#8705E4` | `--ns-deep` |
| Secondary — body text / hover | White | `#FFFFFF` | `--ns-light` |
| Highlight accent | Hot Pink | `#FF06C1` | `--ns-pink` |
| Page surround / icon circles | Pure Black | `#000000` | `--ns-black` |

Hot pink, blue, and white serve as **highlight accents**: bullets,
dashes, links, and other tiny elements only — never fills, text blocks, or
buttons. Hot pink marks bullets and visited links; blue marks unvisited
links, em-dashes, separators, and nested list markers (doubling as a
primary); white marks link hover (doubling as body text).

## Signature effects

- **Dual neon glow** — `box-shadow: 1.5px 1.5px 20px #8705E4, 2.5px 2.5px 20px #11B4F5`
- **Heading glow** — `text-shadow: 1.5px 1.5px 5px #8705E4, 1.75px 1.75px 5px #11B4F5`
- **Soft link glow** — `text-shadow: 0.5px 0.5px 2px #8705E4`
- **Two-tone panels** — hairline borders, purple top/left, blue bottom/right
- **Accordion button** — `border: 4px solid #FF06C1` with `box-shadow: 0 0 3px #8705E4`
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, blue stroke, `box-shadow: 0 0 14px #8705E4`

## Typography

- **Headers** — Sacramento script, blue
- **Subheadings** — Poppins / Century Gothic with soft purple glow
- **Body** — Poppins 300 / Century Gothic fallback, white

Fonts are self-hosted in `fonts/` and declared via `@font-face` in the
stylesheet, so pages work offline and without third-party requests.

## Usage

```html
<link rel="stylesheet" href="css/ccudesign.css">
```

Re-theming is a one-block edit: override the role tokens in `:root`
(`--ns-primary`, `--ns-deep`, `--ns-bg`, `--ns-light`, …). For example, the
original portfolio palette is `--ns-bg: #000000; --ns-primary: #7FFFD4;
--ns-deep: #663399;`.
