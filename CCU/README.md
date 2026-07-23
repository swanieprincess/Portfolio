# CCU · Neon Swan Design Theme

A reusable design theme for the Swan Moon portfolio — neon glows over pure
black, script headers, and tiny jewel-tone accents.

## Files

- `css/neon-swan.css` — the theme stylesheet (drop-in; all colors and effects
  exposed as CSS custom properties on `:root`)
- `index.html` — theme preview page demonstrating every element
- `js/accordion.js` — accordion toggle behavior

## Palette

| Role | Color | Hex |
| --- | --- | --- |
| Background | Pure Black | `#000000` |
| Headers / accents | Aquamarine | `#7FFFD4` |
| Pull-quotes / glow | Rebecca Purple | `#663399` |
| Soft glow | Light Sea Green | `#20B2AA` |
| Body text | Light Gray | `#D3D3D3` |
| Micro-accent (bullets, visited links) | Magenta | `#FF00FF` |
| Micro-accent (dashes, unvisited links) | Dodger Blue | `#1E90FF` |

Magenta and dodger blue are **micro-accents**: bullets, dashes, and other
tiny elements only — never fills, text blocks, or buttons.

## Signature effects

- **Dual neon glow** — `box-shadow: 3px 3px 20px #663399, 5px 5px 20px #7FFFD4`
- **Heading glow** — `text-shadow: 3px 3px 5px #663399, 3.5px 3.5px 5px #7FFFD4`
- **Soft link glow** — `text-shadow: 2px 2px 2px #20B2AA`
- **Two-tone panels** — hairline borders, purple top/left, aquamarine bottom/right
- **Circular imagery** — `border-radius: 50%` on avatars and photos
- **Icon glow** — black circle, aquamarine stroke, `box-shadow: 0 0 14px #663399`

## Typography

- **Headers** — Sacramento script, aquamarine
- **Subheadings** — Poppins / Century Gothic with soft sea-green glow
- **Body** — Poppins 300 / Century Gothic fallback, light gray

## Usage

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&family=Sacramento&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/neon-swan.css">
```

Override any color or effect via the custom properties in `:root`
(e.g. `--ns-aquamarine`, `--ns-dual-glow`).
