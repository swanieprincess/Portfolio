# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows,
script headers, and tiny highlight accents. The CCU Edition pairs **aqua &
white** primaries over a **charcoal** canvas, distinct from the
portfolio's aquamarine/purple-on-black look while keeping the same Neon Swan
style.

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
| Background | Charcoal | `#36454F` | `--ns-bg` |
| Primary — headers / bright accent | Aqua | `#00FFFF` | `--ns-primary` |
| Primary — pull-quotes / deep glow | White | `#FFFFFF` | `--ns-deep` |
| Secondary — body text | Light Gray | `#D3D3D3` | `--ns-gray` |
| Secondary / highlight | Pale Goldenrod | `#EEE8AA` | `--ns-pale` |
| Highlight accent | Dodger Blue | `#1E90FF` | `--ns-blue` |
| Highlight accent | Magenta | `#FF00FF` | `--ns-magenta` |
| Highlight accent | White | `#FFFFFF` | `--ns-white` |
| Page surround / icon circles | Pure Black | `#000000` | `--ns-black` |

Dodger blue, pale goldenrod, magenta, and white serve as **highlight
accents**: bullets, dashes, links, and other tiny elements only — never
fills, text blocks, or buttons. Dodger blue marks bullets and unvisited
links; pale goldenrod marks em-dashes; magenta marks visited links; white
marks separators, nested list markers, and link hover (doubling as a
primary).

## Signature effects

- **Dual neon glow** — `box-shadow: 1.5px 1.5px 20px #FFFFFF, 2.5px 2.5px 20px #00FFFF`
- **Heading glow** — `text-shadow: 1.5px 1.5px 5px #FFFFFF, 1.75px 1.75px 5px #00FFFF`
- **Soft link glow** — `text-shadow: 1.5px 1.5px 2px #FFFFFF`
- **Two-tone panels** — hairline borders, white top/left, aqua bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, aqua stroke, `box-shadow: 0 0 14px #FFFFFF`

## Typography

- **Headers** — Sacramento script, aqua
- **Subheadings** — Poppins / Century Gothic with soft white glow
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
