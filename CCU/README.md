# CCU · Neon Swan Design Theme (CCU Edition)

A reusable design theme for the Swan Moon portfolio's CCU project — neon glows
over pure black, script headers, and tiny jewel-tone accents. The CCU Edition
takes a **gold & royal violet** palette, distinct from the portfolio's
aquamarine/purple look while keeping the same Neon Swan style.

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
| Background | Pure Black | `#000000` | `--ns-black` |
| Headers / bright accent | Gold | `#FFD700` | `--ns-primary` |
| Pull-quotes / deep glow | Royal Violet | `#6A0DAD` | `--ns-deep` |
| Soft glow | Goldenrod | `#DAA520` | `--ns-soft` |
| Body text | Light Gray | `#D3D3D3` | `--ns-gray` |
| Micro-accent (bullets, visited links) | Magenta | `#FF00FF` | `--ns-magenta` |
| Micro-accent (dashes, unvisited links) | Dodger Blue | `#1E90FF` | `--ns-blue` |

Magenta and dodger blue are **micro-accents**: bullets, dashes, and other
tiny elements only — never fills, text blocks, or buttons.

## Signature effects

- **Dual neon glow** — `box-shadow: 3px 3px 20px #6A0DAD, 5px 5px 20px #FFD700`
- **Heading glow** — `text-shadow: 3px 3px 5px #6A0DAD, 3.5px 3.5px 5px #FFD700`
- **Soft link glow** — `text-shadow: 2px 2px 2px #DAA520`
- **Two-tone panels** — hairline borders, violet top/left, gold bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, gold stroke, `box-shadow: 0 0 14px #6A0DAD`

## Typography

- **Headers** — Sacramento script, gold
- **Subheadings** — Poppins / Century Gothic with soft goldenrod glow
- **Body** — Poppins 300 / Century Gothic fallback, light gray

Fonts are self-hosted in `fonts/` and declared via `@font-face` in the
stylesheet, so pages work offline and without third-party requests.

## Usage

```html
<link rel="stylesheet" href="css/neon-swan.css">
```

Re-theming is a one-block edit: override the role tokens in `:root`
(`--ns-primary`, `--ns-deep`, `--ns-soft`, …). For example, the original
portfolio palette is `--ns-primary: #7FFFD4; --ns-deep: #663399;
--ns-soft: #20B2AA;`.
