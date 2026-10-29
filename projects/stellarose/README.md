# Stellarose — Clutch Stellaaa leaderboard site

Single-page design for the streamer **Stellarose** (brand: *Clutch Stellaaa*).
The site shows her clutch.com leaderboard plus challenges, events and community
links. Open `index.html` directly — it is self-contained apart from the Google
Fonts link.

The look follows the client's supplied mockups: crystal pink and white,
rose-gold accents, icy-blue gems, cherry-blossom petals, pill buttons, a soft
terrace scene (sky, mountains, columns, balustrade) behind every banner, and
gradient "gem" lettering. Everything is real HTML text and inline SVG; the
mockup images were design references only.

## Fonts

- **Sacramento** — script display words (*Challenges*, *Events*, the wordmark)
- **Century Gothic** — all caps headings, eyebrows, nav, buttons and body.
  It is a system font; Poppins is loaded from Google Fonts as the web fallback.

## Layout (desktop)

```
+------------------+------------------------------------------+
|                  | Home · Leaderboard · Challenges · Events  |
|   Clutch         |------------------------------------------|
|   Stellaaa       |   CURRENT  Challenges   [View Challenges] |
|   logo hero      |          (terrace scene banner)          |
+------------------+------------------------------------------+
|  podium 2 1 3    LEADERBOARD                 [View Leaderboard]
+------------------+------------------------------------------+
| LEADERBOARD      | trophy   ONGOING Challenges  [View Ongoing]
|  table w/ medals |------------------------------------------|
|  period select   | calendar UPCOMING Events     [View Events]
|                  |------------------------------------------|
|                  | orbs     COMMUNITY           [Join Now]   |
+------------------+------------------------------------------+
```

Collapses to a single column under 1040px; the nav becomes a hamburger under
760px.

## Falling sakura petals

A fixed, click-through canvas draws petals that drift down the page slowly
like snow with a gentle side-to-side sway. They are interactive: petals near
the pointer are nudged away in the direction the mouse (or finger) is moving,
and clicking empty space releases a small burst of petals. The count scales
with viewport size and the effect is disabled for `prefers-reduced-motion`.

## Logo

The hero expects the wolf artwork at `assets/clutch-stellaaa-logo.png`
(transparent PNG). Until that file exists a typographic wordmark with a small
tiara-wolf mark renders in its place.

## Wiring the leaderboard

`DATA` in the inline script holds sample rows for *This Month*, *This Week* and
*All Time*. Replace it with a `fetch()` to the clutch.com leaderboard feed and
call `render(period)`; rows take `{ player, wager }`. Top three get gold,
silver and bronze rank medals automatically. All buttons and footer links are
`#` placeholders.
