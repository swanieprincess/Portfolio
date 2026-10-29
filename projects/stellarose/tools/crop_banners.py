#!/usr/bin/env python3
"""Cut text-free artwork out of the Clutch Stellaaa example banners.

Put the original example images in assets/source/ with these names, then run
    python3 tools/crop_banners.py
from projects/stellarose/. Output lands in assets/ and index.html picks it up.

  source/logo.png                   -> assets/logo.webp           (transparent, resized to 1100px)
  source/current-challenges.jpg     -> assets/current-left.webp, assets/current-right.webp
  source/leaderboard.jpg            -> assets/leaderboard-art.webp, assets/leaderboard-edge.webp
  source/ongoing-challenges.jpg     -> assets/ongoing-art.webp,     assets/ongoing-edge.webp
  source/upcoming-events.jpg        -> assets/events-art.webp,      assets/events-edge.webp
  source/community.jpg              -> assets/community-art.webp,   assets/community-edge.webp
  source/birthday-bonus.jpg         -> assets/birthday-art.webp,    assets/birthday-edge.webp

The banners carry their headline and button baked into the middle, so this
script keeps only the illustration on the left and the blossom/column edge on
the right. The fractions below were measured on the examples; tweak them if a
sliver of text survives.
"""
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install pillow")

HERE = Path(__file__).resolve().parent.parent
SRC = HERE / "assets" / "source"
OUT = HERE / "assets"

# name: (source file, left-art fraction, right-edge fraction)
STRIPS = {
    "leaderboard": ("leaderboard", 0.44, 0.12),
    "ongoing":     ("ongoing-challenges", 0.42, 0.10),
    "events":      ("upcoming-events", 0.45, 0.09),
    "community":   ("community", 0.41, 0.13),
    "birthday":    ("birthday-bonus", 0.40, 0.13),
}
WIDE = ("current-challenges", 0.24, 0.24)   # text-free left and right thirds of the wide banner


def find(stem):
    for ext in ("png", "jpg", "jpeg", "webp"):
        p = SRC / f"{stem}.{ext}"
        if p.exists():
            return p
    return None


TRIM = 8  # px shaved off the outer sides so the example's own card border does not come along


def crop_frac(img, left=None, right=None):
    w, h = img.size
    if left is not None:
        return img.crop((TRIM, TRIM, int(w * left), h - TRIM))
    return img.crop((int(w * (1 - right)), TRIM, w - TRIM, h - TRIM))


def knock_out_background(img, tol=28):
    """Flood-fill near-white pixels connected to the corners to transparent."""
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()
    seen = bytearray(w * h)
    stack = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    while stack:
        x, y = stack.pop()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x]:
            continue
        r, g, b, a = px[x, y]
        if min(r, g, b) < 255 - tol:
            continue
        seen[y * w + x] = 1
        px[x, y] = (r, g, b, 0)
        stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
    return img


WEBP = dict(format="WEBP", quality=85, method=6)  # every output is WebP: a fraction of the PNG/JPG size


def main():
    made = []
    logo = find("logo")
    if logo:
        img = Image.open(logo)
        if img.mode != "RGBA" or img.getpixel((0, 0))[3] != 0:
            img = knock_out_background(img)
        img = img.convert("RGBA")
        if img.width > 1100:
            img = img.resize((1100, int(img.height * 1100 / img.width)), Image.LANCZOS)
        img.save(OUT / "logo.webp", **WEBP)
        made.append("logo.webp")

    for name, (stem, left, right) in STRIPS.items():
        src = find(stem)
        if not src:
            continue
        img = Image.open(src).convert("RGB")
        crop_frac(img, left=left).save(OUT / f"{name}-art.webp", **WEBP)
        crop_frac(img, right=right).save(OUT / f"{name}-edge.webp", **WEBP)
        made += [f"{name}-art.webp", f"{name}-edge.webp"]

    src = find(WIDE[0])
    if src:
        img = Image.open(src).convert("RGB")
        crop_frac(img, left=WIDE[1]).save(OUT / "current-left.webp", **WEBP)
        crop_frac(img, right=WIDE[2]).save(OUT / "current-right.webp", **WEBP)
        made += ["current-left.webp", "current-right.webp"]

    if not made:
        sys.exit(f"No source images found in {SRC}. See the docstring for the expected names.")
    print("wrote:", ", ".join(made))


if __name__ == "__main__":
    main()
