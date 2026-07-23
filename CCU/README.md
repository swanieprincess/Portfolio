# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows,
script headers, and tiny highlight accents. The CCU Edition pairs **aquamarine
& royal blue** primaries over a **navy** canvas, distinct from the portfolio's
aquamarine/purple-on-black look while keeping the same Neon Swan style.

## Files

- `css/neon-swan.css` — the theme stylesheet (drop-in; all colors and effects
  exposed as role-based CSS custom properties on `:root`)
- `fonts/` — self-hosted Sacramento 400 and Poppins 300 (woff2, latin +
  latin-ext) — no Google Fonts CDN dependency
- `index.html` — theme preview page demonstrating every element
- `js/accordion.js` — accordion toggle behavior

## Palette

| Role | Color | Hex | Token |
| --- | --- | --- | --- |
| Background | Navy Blue | `#000080` | `--ns-bg` |
| Primary — headers / bright accent | Aquamarine | `#7FFFD4` | `--ns-primary` |
| Primary — pull-quotes / deep glow | Royal Blue | `#4169E1` | `--ns-deep` |
| Secondary — body text | Light Gray | `#D3D3D3` | `--ns-gray` |
| Secondary / highlight | Pale Yellow | `#FFFFE0` | `--ns-pale` |
| Highlight accent | White | `#FFFFFF` | `--ns-white` |
| Page surround / icon circles | Pure Black | `#000000` | `--ns-black` |

White and pale yellow are **highlight accents**: bullets, dashes, links, and
other tiny elements only — never fills, text blocks, or buttons. White marks
bullets and unvisited links; pale yellow marks dashes, separators, and
visited links.

## Signature effects

- **Dual neon glow** — `box-shadow: 3px 3px 20px #4169E1, 5px 5px 20px #7FFFD4`
- **Heading glow** — `text-shadow: 3px 3px 5px #4169E1, 3.5px 3.5px 5px #7FFFD4`
- **Soft link glow** — `text-shadow: 2px 2px 2px #4169E1`
- **Two-tone panels** — hairline borders, royal blue top/left, aquamarine bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, aquamarine stroke, `box-shadow: 0 0 14px #4169E1`

## Typography

- **Headers** — Sacramento script, aquamarine
- **Subheadings** — Poppins / Century Gothic with soft royal blue glow
- **Body** — Poppins 300 / Century Gothic fallback, light gray

Fonts are self-hosted in `fonts/` and declared via `@font-face` in the
stylesheet, so pages work offline and without third-party requests.

## Usage

```html
<link rel="stylesheet" href="css/neon-swan.css">
```

Re-theming is a one-block edit: override the role tokens in `:root`
(`--ns-primary`, `--ns-deep`, `--ns-bg`, `--ns-pale`, …). For example, the
original portfolio palette is `--ns-bg: #000000; --ns-primary: #7FFFD4;
--ns-deep: #663399;`.
