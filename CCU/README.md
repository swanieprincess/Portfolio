# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows,
script headers, and tiny highlight accents. The CCU Edition pairs **aqua &
dodger blue** primaries over a **dark navy** canvas, distinct from the
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
| Background | Dark Navy | `#001F3F` | `--ns-bg` |
| Primary — headers / bright accent | Aqua | `#00FFFF` | `--ns-primary` |
| Primary — pull-quotes / deep glow | Dodger Blue | `#1E90FF` | `--ns-deep` |
| Secondary — body text | Light Gray | `#D3D3D3` | `--ns-gray` |
| Secondary / highlight | Pale Goldenrod | `#EEE8AA` | `--ns-pale` |
| Highlight accent | White | `#FFFFFF` | `--ns-white` |
| Page surround / icon circles | Pure Black | `#000000` | `--ns-black` |

White and pale goldenrod are **highlight accents**: bullets, dashes, links,
and other tiny elements only — never fills, text blocks, or buttons. White
marks bullets and unvisited links; pale goldenrod marks dashes, separators,
and visited links.

## Signature effects

- **Dual neon glow** — `box-shadow: 3px 3px 20px #1E90FF, 5px 5px 20px #00FFFF`
- **Heading glow** — `text-shadow: 3px 3px 5px #1E90FF, 3.5px 3.5px 5px #00FFFF`
- **Soft link glow** — `text-shadow: 2px 2px 2px #1E90FF`
- **Two-tone panels** — hairline borders, dodger blue top/left, aqua bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, aqua stroke, `box-shadow: 0 0 14px #1E90FF`

## Typography

- **Headers** — Sacramento script, aqua
- **Subheadings** — Poppins / Century Gothic with soft dodger blue glow
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
