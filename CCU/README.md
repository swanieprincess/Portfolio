# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows,
script headers, and tiny highlight accents. The CCU Edition pairs the classic
**vaporwave palette** (cyan, purple, hot pink, mint, pale yellow) over a
**charcoal** canvas, distinct from the portfolio's aquamarine/purple-on-black
look while keeping the same Neon Swan style.

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
| Primary — headers / bright accent | Cyan | `#01CDFE` | `--ns-primary` |
| Primary — pull-quotes / deep glow | Purple | `#B967FF` | `--ns-deep` |
| Secondary — body text | Light Gray | `#D3D3D3` | `--ns-gray` |
| Secondary / highlight | Pale Yellow | `#FFFB96` | `--ns-pale` |
| Highlight accent | Hot Pink | `#FF71CE` | `--ns-pink` |
| Highlight accent | Mint | `#05FFA1` | `--ns-mint` |
| Page surround / icon circles | Pure Black | `#000000` | `--ns-black` |

Hot pink, pale yellow, and mint serve as **highlight accents**: bullets,
dashes, links, and other tiny elements only — never fills, text blocks, or
buttons. Hot pink marks bullets and visited links; cyan marks unvisited
links (doubling as a primary); pale yellow marks em-dashes; mint marks
separators, nested list markers, and link hover.

## Signature effects

- **Dual neon glow** — `box-shadow: 1.5px 1.5px 20px #B967FF, 2.5px 2.5px 20px #01CDFE`
- **Heading glow** — `text-shadow: 1.5px 1.5px 5px #B967FF, 1.75px 1.75px 5px #01CDFE`
- **Soft link glow** — `text-shadow: 1.5px 1.5px 2px #B967FF`
- **Two-tone panels** — hairline borders, purple top/left, cyan bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, cyan stroke, `box-shadow: 0 0 14px #B967FF`

## Typography

- **Headers** — Sacramento script, cyan
- **Subheadings** — Poppins / Century Gothic with soft purple glow
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
