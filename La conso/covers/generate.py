#!/usr/bin/env python3
"""
Generate podcast cover PNGs from the HTML designs in index.html.

Usage:
    python3 covers/generate.py              # Generate all covers at 3000x3000
    python3 covers/generate.py --size 1500  # Custom size

Requirements:
    pip install playwright Pillow
    playwright install chromium

How it works:
    1. Reads each cover design from index.html (#v1-2 section)
    2. Extracts the .cover-inner HTML + inline styles
    3. Renders each in a standalone page at TARGET size
    4. Screenshots to PNG

Proportions:
    The HTML card renders at ~280x280 in the browser grid.
    To scale to 3000x3000, all font-sizes, positions, and margins
    use % or clamp() so they scale naturally with the container.
    The image (filRouge.png) uses width:95% + absolute positioning,
    so it scales proportionally too.

    KEY: the standalone HTML must use the SAME CSS values as index.html,
    just with the container set to TARGET x TARGET pixels.
    Font sizes are scaled by ratio: TARGET / 280 (the card width).

Notes:
    - Fonts load from Google Fonts (needs internet)
    - filRouge.png must exist in images/nobg/
    - Output overwrites existing files in covers/
"""

import argparse
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate podcast cover PNGs")
    parser.add_argument(
        "--size", type=int, default=3000, help="Output size in px (square)"
    )
    args = parser.parse_args()

    TARGET = args.size
    base = Path(__file__).resolve().parent.parent
    covers_dir = base / "covers"
    img_path = base / "images" / "nobg" / "filRouge.png"

    if not img_path.exists():
        print(f"ERROR: {img_path} not found")
        sys.exit(1)

    # Scale factor from the 280px card to target
    S = TARGET / 280
    # Shadow blur scales slower — sqrt to avoid massive halos at high res
    import math

    SB = math.sqrt(S) * 1.5  # blur scale (~5.8x at 3000px instead of 10.7x)

    # Shared SVGs
    bb_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 280" fill="none" style="width:{logo_w}px;height:auto;"><mask id="cBa" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="80" width="200" height="200"><path d="M200 80H0V280H200V80Z" fill="white" fill-opacity="0.7"/></mask><g mask="url(#cBa)"><path d="M200 180C200 235.2 155.2 280 100 280C44.8 280 0 235.2 0 180V80H100C155.2 80 200 124.8 200 180Z" fill="currentColor"/></g><mask id="cBb" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="160" height="160"><path d="M160 0H0V160H160V0Z" fill="white" fill-opacity="0.7"/></mask><g mask="url(#cBb)"><path d="M160 80C160 124.2 124.2 160 80 160C35.8 160 0 124.2 0 80V0H80C124.2 0 160 35.8 160 80Z" fill="currentColor"/></g></svg>'
    bleen_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="270 60 450 160" fill="none" style="width:{text_w}px;height:auto;"><path d="M270 160.7V70H289V125C296.6 116.6 308 111 320.7 111C349.2 111 369.6 132 369.6 160.7C369.6 187.9 348.2 210 319.9 210C291.6 210 270 188.6 270 160.7ZM350.7 160.5C350.7 143.4 337.3 129.1 319.9 129.1C302.5 129.1 289 143.4 289 160.5C289 177.6 302.3 192.1 319.9 192.1C337.5 192.1 350.7 177.8 350.7 160.5Z" fill="currentColor"/><path d="M401.3 70V207.7H382.4V70H401.3Z" fill="currentColor"/><path d="M414.1 159.9C414.1 132.8 433.4 110.6 461.5 110.6C489.7 110.6 507.4 131.2 507.4 157.6V165.3H432.5C434.6 181.5 446.8 192.9 463.6 192.9C475.1 192.9 485.4 187.8 491 177.5L505.5 185C497.3 201.1 482.2 209.8 463.8 209.8C435.3 209.8 414.1 189 414.1 159.9ZM488.5 153C487.7 138 476.8 127.8 461.3 127.8C445.9 127.8 435.2 138.9 433.2 153H488.5Z" fill="currentColor"/><path d="M520.2 159.9C520.2 132.8 539.5 110.6 567.6 110.6C595.7 110.6 613.5 131.2 613.5 157.6V165.3H538.6C540.7 181.5 552.9 192.9 569.7 192.9C581.2 192.9 591.5 187.8 597.1 177.5L611.6 185C603.4 201.1 588.3 209.8 569.9 209.8C541.4 209.8 520.2 189 520.2 159.9ZM594.6 153C593.8 138 582.9 127.8 567.4 127.8C552 127.8 541.2 138.9 539.3 153H594.6Z" fill="currentColor"/><path d="M645.2 162.1V207.7H626.3V160.1C626.3 132.6 642.6 111 672.8 111C703 111 720 132.6 720 159.9V207.7H701.1V162.2C701.1 144.5 691.5 129.3 672.8 129.3C654 129.3 645.2 144.5 645.2 162.1Z" fill="currentColor"/></svg>'

    logo_w = int(24 * S)
    text_w = int(40 * S)
    bb_svg = bb_svg.replace("{logo_w}", str(logo_w))
    bleen_svg = bleen_svg.replace("{text_w}", str(text_w))

    # Cover definitions — font sizes scaled from the 280px card
    covers = [
        {
            "name": "cover-1-homo-consumens.png",
            "title_html": f"""
                <div style="font-size:{int(50 * S)}px;color:#ffffff;line-height:0.9;font-family:'Knewave',cursive;text-align:center;-webkit-text-stroke:{int(2 * S)}px rgba(0,0,0,0.5);paint-order:stroke fill;text-shadow:0 {int(3 * SB)}px {int(10 * SB)}px rgba(0,0,0,0.5);">Homo</div>
                <div style="font-size:{int(50 * S)}px;color:#ffdc37;line-height:0.85;font-family:'Knewave',cursive;text-align:center;margin-top:{int(-4 * S)}px;-webkit-text-stroke:{int(2 * S)}px rgba(0,0,0,0.5);paint-order:stroke fill;text-shadow:0 {int(3 * SB)}px {int(10 * SB)}px rgba(0,0,0,0.5);">Consumens</div>
                <div style="font-size:{int(13 * S)}px;color:rgba(255,255,255,0.9);font-family:'Caveat',cursive;font-weight:700;letter-spacing:0.06em;margin-top:{int(4 * S)}px;text-shadow:0 {int(1 * SB)}px {int(4 * SB)}px rgba(0,0,0,0.4);">Toujours plus. Jamais assez.</div>
            """,
        },
        {
            "name": "cover-2-trop.png",
            "title_html": f"""
                <div style="font-size:{int(100 * S)}px;color:#ffffff;line-height:0.8;font-family:'Knewave',cursive;-webkit-text-stroke:{int(3 * SB)}px rgba(0,0,0,0.4);paint-order:stroke fill;text-shadow:0 {int(6 * SB)}px {int(30 * SB)}px rgba(0,0,0,0.5);">TROP</div>
            """,
        },
    ]

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: pip install playwright && playwright install chromium")
        sys.exit(1)

    for cfg in covers:
        html = f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Knewave&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:{TARGET}px;height:{TARGET}px;overflow:hidden;}}
.cover{{width:{TARGET}px;height:{TARGET}px;position:relative;overflow:hidden;
background:linear-gradient(90deg, #00B4F0, #FF4D6A);
display:flex;flex-direction:column;align-items:center;}}
.vignette{{position:absolute;inset:0;z-index:1;
background:radial-gradient(ellipse 90% 90% at 50% 50%, transparent 40%, rgba(0,0,0,0.12) 100%);}}
.photo{{position:absolute;bottom:-8%;left:-5%;width:95%;height:auto;z-index:2;
filter:drop-shadow(0 {int(4 * SB)}px {int(12 * SB)}px rgba(0,0,0,0.3));}}
.title{{position:absolute;top:5%;left:0;right:0;z-index:10;display:flex;flex-direction:column;align-items:center;padding:0 6%;}}
.logo-area{{position:absolute;bottom:0;right:0;width:45%;height:30%;z-index:3;
background:radial-gradient(ellipse at 100% 100%, rgba(0,0,0,0.35) 0%, transparent 70%);pointer-events:none;}}
.logo{{position:absolute;bottom:5%;right:5%;z-index:10;display:flex;align-items:center;gap:{int(6 * S)}px;color:#ffffff;
filter:drop-shadow(0 {int(1 * SB)}px {int(3 * SB)}px rgba(0,0,0,0.5));}}
</style></head>
<body>
<div class="cover">
  <div class="vignette"></div>
  <img class="photo" src="file://{img_path}" alt="">
  <div class="title">{cfg["title_html"]}</div>
  <div class="logo-area"></div>
  <div class="logo">{bb_svg}{bleen_svg}</div>
</div>
</body></html>"""

        tmp_html = covers_dir / "_tmp_cover.html"
        tmp_html.write_text(html)

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": TARGET, "height": TARGET})
            page.goto(f"file://{tmp_html}", wait_until="networkidle")
            page.wait_for_timeout(3000)

            out_path = covers_dir / cfg["name"]
            page.screenshot(
                path=str(out_path),
                type="png",
                clip={"x": 0, "y": 0, "width": TARGET, "height": TARGET},
            )
            browser.close()

        size = out_path.stat().st_size
        print(f"  {cfg['name']}: {size / 1024 / 1024:.1f} MB ({TARGET}x{TARGET})")

        tmp_html.unlink()

    print("Done!")


if __name__ == "__main__":
    main()
