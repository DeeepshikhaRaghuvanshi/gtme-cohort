"""Renderer for the v3 course video (content in course.py).

  python3 render3.py stills     # build/v3/stills/sNN_bK.png, one per beat (state K of scene NN)
  python3 render3.py sheets     # contact sheets of every scene's final state -> build/v3/sheets/
  python3 render3.py script     # build/v3/script.md (readable script for review)
  python3 render3.py audio      # Piper wav per beat -> build/v3/audio/
  python3 render3.py clips      # one MP4 per beat (still + audio + subtitles) -> build/v3/clips/
  python3 render3.py final      # concat -> Saffron-GTM-Course.mp4
Each stage is idempotent (skips existing outputs) except stills/sheets/script, which always rebuild.
"""
import importlib
import re
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
EVID = ROOT.parent / "buildlog" / "evidence"
OUT = ROOT / "build" / "v3"
PIPER = ROOT / "piper" / "piper"
VOICE = ROOT / "voice" / "en_US-lessac-medium.onnx"
W, H, FPS = 1920, 1080, 30
sys.path.insert(0, str(ROOT))
course = importlib.import_module("course")

# ── palette ──
BG, PAPER, INK, INK2, MUTED, LINE = "#f3f5f6", "#ffffff", "#14202c", "#3a4856", "#6b7986", "#d9e0e6"
DARK, DARK2 = "#0f1b26", "#1b2a38"
MOD_COLORS = ["#0e6f69", "#0e6f69", "#2f6fb5", "#7a4fb0", "#0e7a8a", "#b0571a", "#2e7d4f", "#b4373f", "#8a6d12"]
GOOD, OK2, WARN, BAD = "#2c7a3f", "#0e7a8a", "#b8860b", "#b4373f"
TIP_C, REAL_C, MIST_C = "#0e6f69", "#2f6fb5", "#b4373f"

FD = "/usr/share/fonts/truetype/ubuntu"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FALLBACK_CHARS = set("→←≈≥≤✓✗⚠")
_fc = {}


def F(style, size):
    key = (style, size)
    if key not in _fc:
        name = {"r": "Ubuntu-R.ttf", "b": "Ubuntu-B.ttf", "m": "Ubuntu-M.ttf", "l": "Ubuntu-L.ttf"}[style]
        _fc[key] = ImageFont.truetype(f"{FD}/{name}", size)
    return _fc[key]


def FBK(size, bold=False):
    key = ("fb", size, bold)
    if key not in _fc:
        _fc[key] = ImageFont.truetype(FB_BOLD if bold else FB, size)
    return _fc[key]


def tlen(dr, text, font):
    w = 0
    for seg, fb in segments(text):
        w += dr.textlength(seg, font=FBK(font.size, "B" in font.getname()[1]) if fb else font)
    return w


def segments(text):
    out, cur, curfb = [], "", None
    for ch in text:
        fb = ch in FALLBACK_CHARS
        if curfb is None or fb == curfb:
            cur += ch
        else:
            out.append((cur, curfb))
            cur = ch
        curfb = fb
    if cur:
        out.append((cur, bool(curfb)))
    return out


def text(dr, xy, s, font, fill, anchor_right=False, center=False):
    x, y = xy
    if anchor_right:
        x -= tlen(dr, s, font)
    if center:
        x -= tlen(dr, s, font) / 2
    for seg, fb in segments(s):
        f = FBK(font.size, "B" in font.getname()[1]) if fb else font
        dy = int(font.size * 0.06) if fb else 0
        dr.text((x, y + dy), seg, font=f, fill=fill)
        x += dr.textlength(seg, font=f)


def wrap(dr, s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tlen(dr, t, font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def hexa(c, a):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


# ── frame chrome ──
def base(scene, dark=False):
    im = Image.new("RGB", (W, H), DARK if dark else BG)
    return im, ImageDraw.Draw(im)


def footer(dr, scene, dark=False):
    m = scene["module"]
    if m == 0:
        return
    names = course.MODULES[1:]
    x0, x1, y = 110, W - 110, H - 62
    seg = (x1 - x0) / len(names)
    for i, nm in enumerate(names, 1):
        sx = x0 + (i - 1) * seg
        col = MOD_COLORS[i] if i == m else ("#2a3a48" if dark else "#dfe5ea")
        dr.rounded_rectangle([sx + 4, y, sx + seg - 4, y + 8], radius=4, fill=col)
        fc = ("#ffffff" if dark else INK) if i == m else ("#6f8091" if dark else "#93a0ab")
        text(dr, (sx + 6, y + 16), f"{i} · {nm}", F("m" if i == m else "r", 22), fc)


def header(dr, scene, title_size=64, dark=False):
    accent = MOD_COLORS[scene["module"]]
    text(dr, (110, 70), scene["eyebrow"], F("m", 27), "#5fd0c4" if dark else accent)
    size = title_size
    while tlen(dr, scene["title"], F("b", size)) > W - 460 and size > 38:
        size -= 2
    text(dr, (110, 110), scene["title"], F("b", size), "#ffffff" if dark else INK)
    text(dr, (W - 110, 76), "Saffron · GTM Engineering", F("r", 22), "#8aa0b2" if dark else MUTED, anchor_right=True)
    if not dark:
        dr.line([(110, 205), (W - 110, 205)], fill=LINE, width=2)


# ── kinds ──
def k_title(scene, r):
    im, dr = base(scene, dark=True)
    for i in range(14):  # quiet geometric texture
        dr.ellipse([1300 + i * 22, 140 + i * 30, 1900 + i * 10, 740 + i * 20], outline="#162636", width=2)
    text(dr, (140, 300), scene["eyebrow"], F("m", 32), "#5fd0c4")
    y = 360
    for ln in wrap(dr, scene["title"], F("b", 92), 1300):
        text(dr, (140, y), ln, F("b", 92), "#ffffff")
        y += 108
    for ln in wrap(dr, scene["items"][0], F("r", 42), 1250):
        text(dr, (140, y + 30), ln, F("r", 42), "#c1ccd5")
        y += 56
    footer(dr, scene, dark=True)
    return im


def k_chapter(scene, r):
    im, dr = base(scene, dark=True)
    m = scene["module"]
    accent = MOD_COLORS[m]
    dr.rectangle([0, 0, 26, H], fill=accent)
    text(dr, (150, 170), f"{m:02d}", F("b", 260), accent)
    text(dr, (150, 470), scene["eyebrow"], F("m", 32), "#8fd6cd")
    text(dr, (150, 515), scene["title"], F("b", 96), "#ffffff")
    text(dr, (150, 660), "IN THIS CHAPTER", F("m", 24), "#8aa0b2")
    y = 705
    for it in scene["items"]:
        dr.ellipse([152, y + 14, 166, y + 28], fill=accent)
        text(dr, (190, y), it, F("r", 38), "#dfe7ee")
        y += 56
    footer(dr, scene, dark=True)
    return im


def bullet_list(dr, items, n, x, y, maxw, size=44, color=INK, dot=None, check=False, gap=26, measure=False):
    f = F("r", size)
    for i, it in enumerate(items[:n]):
        lines = wrap(dr, it, f, maxw)
        cy = y + int(size * 0.55)
        if measure:
            y += int(size * 1.32) * len(lines) + gap
            continue
        if check:
            text(dr, (x - 6, y - 2), "✓", F("b", size), dot or GOOD)
        else:
            dr.rounded_rectangle([x, cy - 7, x + 14, cy + 7], radius=4, fill=dot or MOD_COLORS[1])
        for j, ln in enumerate(lines):
            text(dr, (x + 44, y), ln, f, color if j == 0 else INK2)
            y += int(size * 1.32)
        y += gap
    return y


def k_bullets(scene, r):
    im, dr = base(scene)
    header(dr, scene)
    n = len(scene["items"]) if len(scene["beats"]) == 1 else (r + 1 if len(scene["beats"]) == len(scene["items"]) else r)
    size, gap = 54, 40
    h = bullet_list(dr, scene["items"], len(scene["items"]), 0, 0, 1560, size=size, gap=gap, measure=True)
    y0 = 235 + max(0, (700 - h) // 2)
    bullet_list(dr, scene["items"], n, 130, y0, 1560, size=size, gap=gap, dot=MOD_COLORS[scene["module"]])
    footer(dr, scene)
    return im


def card(scene, r, color, label, icon):
    im, dr = base(scene)
    header(dr, scene)
    size, gap = 50, 34
    h = bullet_list(dr, scene["items"], len(scene["items"]), 0, 0, W - 220 - 200, size=size, gap=gap, measure=True)
    ch = 190 + h + 40
    x0, x1 = 110, W - 110
    y0 = 235 + max(0, (710 - ch) // 2)
    y1 = y0 + ch
    dr.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=PAPER, outline=LINE, width=2)
    dr.rounded_rectangle([x0, y0, x0 + 18, y1], radius=9, fill=color)
    dr.ellipse([x0 + 60, y0 + 48, x0 + 150, y0 + 138], fill=color)
    text(dr, (x0 + 105, y0 + 64), icon, F("b", 52), "#ffffff", center=True)
    text(dr, (x0 + 180, y0 + 72), label, F("b", 34), color)
    n = len(scene["items"]) if len(scene["beats"]) == 1 else min(r + 1, len(scene["items"]))
    bullet_list(dr, scene["items"], n, x0 + 70, y0 + 190, x1 - x0 - 200, size=size, gap=gap, dot=color)
    footer(dr, scene)
    return im


def k_tip(scene, r):
    return card(scene, r, TIP_C, "PRO TIP", "!")


def k_real(scene, r):
    return card(scene, r, REAL_C, "IN THE REAL WORLD", "◆" if False else "W")


def k_mistake(scene, r):
    return card(scene, r, MIST_C, "COMMON MISTAKE", "×")


def k_recap(scene, r):
    im, dr = base(scene)
    header(dr, scene)
    h = bullet_list(dr, scene["items"], len(scene["items"]), 0, 0, W - 420, size=52, gap=44, measure=True)
    ch = h + 120
    x0, x1 = 110, W - 110
    y0 = 235 + max(0, (710 - ch) // 2)
    dr.rounded_rectangle([x0, y0, x1, y0 + ch], radius=22, fill=PAPER, outline=LINE, width=2)
    bullet_list(dr, scene["items"], len(scene["items"]), x0 + 70, y0 + 64, x1 - x0 - 200, size=52, check=True,
                dot=MOD_COLORS[scene["module"]], gap=44)
    footer(dr, scene)
    return im


def k_quiz(scene, r):
    im, dr = base(scene, dark=True)
    text(dr, (110, 70), scene["eyebrow"], F("m", 30), "#ffcf6b")
    dr.ellipse([110, 160, 270, 320], fill="#ffcf6b")
    text(dr, (190, 178), "?", F("b", 110), DARK, center=True)
    y = 180
    for ln in wrap(dr, scene["items"][0], F("b", 54), 1450):
        text(dr, (320, y), ln, F("b", 54), "#ffffff")
        y += 70
    if r == 0:
        text(dr, (320, y + 60), "Pause the video and answer…", F("r", 36), "#8aa0b2")
    else:
        y += 50
        lines = wrap(dr, scene["items"][1], F("r", 44), 1380)
        dr.rounded_rectangle([300, y, W - 110, y + 70 + len(lines) * 58], radius=18, fill="#163a35", outline="#2f8f84", width=2)
        text(dr, (340, y + 22), "ANSWER", F("m", 26), "#7fe0d4")
        yy = y + 60
        for ln in lines:
            text(dr, (340, yy), ln, F("r", 44), "#e6f4f2")
            yy += 58
    footer(dr, scene, dark=True)
    return im


def fit_shot(path, crop, maxw, maxh, cap=3.0):
    shot = Image.open(EVID / path).convert("RGB")
    if crop:
        shot = shot.crop(crop)
    s = min(maxw / shot.width, maxh / shot.height, cap)
    return shot.resize((int(shot.width * s), int(shot.height * s)), Image.LANCZOS)


def k_shots(scene, r):
    im, dr = base(scene)
    header(dr, scene)
    accent = MOD_COLORS[scene["module"]]
    # persistent caption chips: past ones outlined, current one filled; shrink to fit the width
    caps = [scene["items"][j][2] for j in range(r + 1)]
    fs = 36
    while fs > 22 and sum(tlen(dr, c, F("b", fs)) + 56 + 58 for c in caps) - 58 > W - 220:
        fs -= 2
    x = 110
    for j in range(r + 1):
        cap = scene["items"][j][2]
        f = F("b", fs)
        cw = tlen(dr, cap, f) + 56
        if j == r:
            dr.rounded_rectangle([x, 226, x + cw, 286], radius=30, fill=accent)
            text(dr, (x + 28, 234), cap, f, "#ffffff")
        else:
            dr.rounded_rectangle([x, 226, x + cw, 286], radius=30, fill=PAPER, outline=accent, width=3)
            text(dr, (x + 28, 234), cap, f, accent)
        x += cw + 18
        if j < r:
            text(dr, (x - 8, 236), "→", F("b", fs), MUTED)
            x += 40
    path, crop, cap = scene["items"][r]
    top, box_h = 310, 650
    shot = fit_shot(path, crop, W - 260, box_h, cap=4.0)
    x0, y0 = (W - shot.width) // 2, top + (box_h - shot.height) // 2
    sh = Image.new("RGBA", (shot.width + 60, shot.height + 60), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([30, 30, shot.width + 30, shot.height + 30], radius=12, fill=(20, 33, 46, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    im.paste(sh, (x0 - 30, y0 - 20), sh)
    im.paste(shot, (x0, y0))
    dr.rectangle([x0 - 1, y0 - 1, x0 + shot.width, y0 + shot.height], outline=LINE, width=2)
    footer(dr, scene)
    return im


# ── diagrams ──
def d_funnel(scene, r, dr):
    items = scene["items"]
    cols = ["#d8eeeb", "#bfe4df", "#9fd3cb", "#7dc0b7", "#4fa59b", "#0e6f69"]
    top, hstep, maxw, minw, cx = 250, 105, 1200, 360, 760
    for i in range(r + 1):
        w0 = maxw - (maxw - minw) * i / len(items)
        w1 = maxw - (maxw - minw) * (i + 1) / len(items)
        y0, y1 = top + i * hstep, top + i * hstep + hstep - 10
        dr.polygon([(cx - w0 / 2, y0), (cx + w0 / 2, y0), (cx + w1 / 2, y1), (cx - w1 / 2, y1)], fill=cols[i])
        text(dr, (cx, y0 + 26), items[i], F("b", 42), INK if i < 4 else "#ffffff", center=True)
    if r == len(items) - 1:
        x = 1440
        dr.rounded_rectangle([x, 330, W - 110, 760], radius=20, fill=PAPER, outline=LINE, width=2)
        text(dr, (x + 40, 365), "LOSSES COMPOUND", F("m", 26), BAD)
        text(dr, (x + 40, 420), "50% lost × 4 steps", F("b", 38), INK)
        text(dr, (x + 40, 490), "≈ 6%", F("b", 120), BAD)
        text(dr, (x + 40, 640), "left at the end", F("r", 36), INK2)


def d_layers(scene, r, dr):
    cols = ["#0e6f69", "#14808a", "#2f6fb5", "#5b5fc7", "#7a4fb0", "#b0571a", "#b4373f"]
    for i in range(r + 1):
        y = 235 + i * 98
        w = 1300 - i * 40
        dr.rounded_rectangle([110, y, 110 + w, y + 82], radius=14, fill=cols[i])
        code, name = scene["items"][i].split(" ", 1)
        text(dr, (140, y + 20), code, F("b", 40), "#ffffff")
        text(dr, (240, y + 20), name, F("m", 40), "#ffffff")


def d_tam(scene, r, dr):
    cx, cy = 560, 590
    sizes = [(460, 330, "#d8eeeb", "#0e6f69"), (320, 230, "#ffffff", "#2f6fb5"), (170, 125, "#e7edf8", "#7a4fb0")]
    offs = [(0, 0), (60, 40), (110, 70)]
    labels = ["TAM", "SAM", "SOM"]
    defs = ["Every company that could ever buy", "The part you can actually serve", "What you can realistically win this year"]
    for i in range(r + 1):
        rx, ry, fill, edge = sizes[i]
        ox, oy = offs[i]
        dr.ellipse([cx + ox - rx, cy + oy - ry, cx + ox + rx, cy + oy + ry], fill=fill, outline=edge, width=4)
        lx = cx + ox - rx + 40 if i < 2 else cx + ox - 50
        ly = cy + oy - ry + 30 if i < 2 else cy + oy - 25
        text(dr, (lx, ly), labels[i], F("b", 46), edge)
        y = 270 + i * 215
        dr.rounded_rectangle([1130, y, W - 110, y + 190], radius=18, fill=PAPER, outline=LINE, width=2)
        dr.rectangle([1130, y, 1142, y + 190], fill=edge)
        text(dr, (1170, y + 22), labels[i], F("b", 46), edge)
        for j, ln in enumerate(wrap(dr, defs[i], F("r", 36), 580)):
            text(dr, (1170, y + 84 + j * 44), ln, F("r", 36), INK2)


def grid_cards(dr, items, r, cols, colors, top=260, h=280, sub=None):
    n = len(items)
    rows = (n + cols - 1) // cols
    gw = (W - 220 - (cols - 1) * 30) / cols
    for i in range(r + 1):
        c, rr = i % cols, i // cols
        x0 = 110 + c * (gw + 30)
        y0 = top + rr * (h + 30)
        col = colors[i % len(colors)]
        dr.rounded_rectangle([x0, y0, x0 + gw, y0 + h], radius=20, fill=PAPER, outline=LINE, width=2)
        dr.rounded_rectangle([x0, y0, x0 + gw, y0 + 16], radius=8, fill=col)
        lines = wrap(dr, items[i], F("b", 44), gw - 70)
        yy = y0 + 50
        for ln in lines:
            text(dr, (x0 + 35, yy), ln, F("b", 44), col)
            yy += 56
        if sub:
            for ln in wrap(dr, sub[i], F("r", 32), gw - 70):
                text(dr, (x0 + 35, yy + 10), ln, F("r", 32), INK2)
                yy += 42


def d_emailstatus(scene, r, dr):
    grid_cards(dr, scene["items"], r, 2, [GOOD, OK2, WARN, BAD], top=250, h=300,
               sub=["Mailbox exists → send", "Server accepts all; verifier says real → send",
                    "Accepted, maybe never read → don't send", "Bounces → never send"])


def d_rules(scene, r, dr):
    items = scene["items"]
    gw = (W - 220 - 4 * 24) / 5
    for i in range(r + 1):
        x0 = 110 + i * (gw + 24)
        dr.rounded_rectangle([x0, 300, x0 + gw, 820], radius=22, fill=PAPER, outline=LINE, width=2)
        text(dr, (x0 + gw / 2, 340), str(i + 1), F("b", 150), MOD_COLORS[4], center=True)
        yy = 560
        for ln in wrap(dr, items[i], F("b", 40), gw - 50):
            text(dr, (x0 + gw / 2, yy), ln, F("b", 40), INK, center=True)
            yy += 50


def chain(dr, items, r, y=470, h=170, colors=None, last_good=False):
    n = len(items)
    gap = 70
    bw = (W - 220 - gap * (n - 1)) / n
    for i in range(r + 1):
        x0 = 110 + i * (bw + gap)
        col = (colors[i] if colors else MOD_COLORS[4])
        if last_good and i == n - 1:
            col = GOOD
        dr.rounded_rectangle([x0, y, x0 + bw, y + h], radius=18, fill=col)
        lines = wrap(dr, items[i], F("b", 34), bw - 30)
        yy = y + h / 2 - len(lines) * 22
        for ln in lines:
            text(dr, (x0 + bw / 2, yy), ln, F("b", 34), "#ffffff", center=True)
            yy += 44
        if i < n - 1 and i < r:
            ax = x0 + bw + 10
            dr.polygon([(ax, y + h / 2 - 18), (ax + gap - 20, y + h / 2), (ax, y + h / 2 + 18)], fill=MUTED)


def d_waterfall(scene, r, dr):
    chain(dr, scene["items"], r, colors=["#2f6fb5", "#5b5fc7", "#7a4fb0", GOOD], last_good=True)
    notes = ["Cheapest, most reliable first", "Only if A found nothing", "Only if B found nothing", "Later steps never charge"]
    for i in range(r + 1):
        n = len(scene["items"])
        bw = (W - 220 - 70 * (n - 1)) / n
        x0 = 110 + i * (bw + 70)
        for j, ln in enumerate(wrap(dr, notes[i], F("r", 30), bw)):
            text(dr, (x0 + bw / 2, 670 + j * 38), ln, F("r", 30), INK2, center=True)


def d_runcond(scene, r, dr):
    cx = 560
    dr.polygon([(cx, 260), (cx + 230, 470), (cx, 680), (cx - 230, 470)], fill=MOD_COLORS[4])
    for j, ln in enumerate(["Row", "qualifies?"]):
        text(dr, (cx, 420 + j * 50), ln, F("b", 42), "#ffffff", center=True)
    if r >= 1:
        dr.line([(cx + 230, 470), (1050, 360)], fill=MUTED, width=6)
        dr.rounded_rectangle([1050, 290, W - 110, 430], radius=20, fill=GOOD)
        text(dr, (1090, 330), "Yes → run the column", F("b", 46), "#ffffff")
    if r >= 2:
        dr.line([(cx + 230, 470), (1050, 590)], fill=MUTED, width=6)
        dr.rounded_rectangle([1050, 520, W - 110, 660], radius=20, fill="#9aa7b2")
        text(dr, (1090, 560), "No → skip · 0 credits", F("b", 46), "#ffffff")
        text(dr, (110, 790), "Example: recruiting-team lookup ran only where engineering openings ≥ 1", F("r", 36), INK2)


def d_pipeline(scene, r, dr):
    items = scene["items"]
    n = len(items)
    gw = (W - 220) / n
    # spreadsheet look: header row + body rows
    for i in range(r + 1):
        x0 = 110 + i * gw
        col = MOD_COLORS[5] if i == n - 1 else ("#2f6fb5" if i < 3 else MOD_COLORS[4])
        dr.rectangle([x0, 330, x0 + gw - 6, 420], fill=col)
        for j, ln in enumerate(wrap(dr, items[i], F("b", 30), gw - 30)):
            text(dr, (x0 + gw / 2 - 3, 345 + j * 36), ln, F("b", 30), "#ffffff", center=True)
        for k in range(6):
            yy = 430 + k * 64
            dr.rectangle([x0, yy, x0 + gw - 6, yy + 56], fill=PAPER, outline=LINE)
            if i == n - 1:
                lab, c = (("Outreach", GOOD) if k in (0, 2, 3, 5) else ("Don't", BAD))
                text(dr, (x0 + gw / 2 - 3, yy + 12), lab, F("m", 28), c, center=True)
            else:
                dr.rounded_rectangle([x0 + 24, yy + 22, x0 + gw - 40 - (k * 13 + i * 7) % 60, yy + 34], radius=6, fill="#e3e9ee")
    costs = ["free", "free", "0.5/row", "0.5 on hits", "0.5, gated", "1, gated", "free"]
    for i in range(r + 1):
        x0 = 110 + i * gw
        text(dr, (x0 + gw / 2 - 3, 830), costs[i], F("m", 30), MOD_COLORS[5] if "gated" in costs[i] else MUTED, center=True)


def d_models(scene, r, dr):
    items = scene["items"]
    notes = ["Single-page lookups · start here", "Multi-page research · escalate failures", "Clay's default “recommended” · avoid by default"]
    cols = [GOOD, "#2f6fb5", BAD]
    gw = (W - 220 - 60) / 3
    for i in range(r + 1):
        x0 = 110 + i * (gw + 30)
        dr.rounded_rectangle([x0, 300, x0 + gw, 820], radius=24, fill=PAPER, outline=LINE, width=2)
        name, cost = items[i].split(" · ")
        text(dr, (x0 + gw / 2, 340), name, F("b", 64), cols[i], center=True)
        for k in range(i + 1):  # coins
            ccx = x0 + gw / 2 - (i * 45) + k * 90
            dr.ellipse([ccx - 38, 450, ccx + 38, 526], fill="#f2c94c", outline="#b8860b", width=4)
            text(dr, (ccx, 462), "1", F("b", 44), "#7a5b00", center=True)
        text(dr, (x0 + gw / 2, 560), cost, F("b", 44), INK, center=True)
        for j, ln in enumerate(wrap(dr, notes[i], F("r", 32), gw - 60)):
            text(dr, (x0 + gw / 2, 640 + j * 42), ln, F("r", 32), INK2, center=True)


def d_people(scene, r, dr):
    items = scene["items"]
    cols = ["#2f6fb5", "#5b5fc7", "#7a4fb0", MOD_COLORS[4], GOOD]
    for i in range(r + 1):
        y = 235 + i * 135
        w = 1500 - i * 150
        x0 = (W - w) / 2
        dr.rounded_rectangle([x0, y, x0 + w, y + 112], radius=18, fill=cols[i])
        text(dr, (W / 2, y + 32), items[i], F("b", 44), "#ffffff", center=True)


def d_ladder(scene, r, dr):
    items = scene["items"]
    notes = ["cheapest", "manual, page by page", "interprets pages · ~$200 / 1,000 rows", "~$19 / month", "hardest sites"]
    for i in range(r + 1):
        x0 = 110 + i * 340
        y0 = 800 - i * 120
        dr.rounded_rectangle([x0, y0, x0 + 320, 880], radius=14, fill=PAPER, outline=LINE, width=2)
        dr.rectangle([x0, y0, x0 + 320, y0 + 14], fill=MOD_COLORS[6])
        nl = wrap(dr, items[i], F("b", 34), 290)
        for j, ln in enumerate(nl):
            text(dr, (x0 + 20, y0 + 28 + j * 42), ln, F("b", 34), INK)
        for j, ln in enumerate(wrap(dr, notes[i], F("r", 28), 290)):
            text(dr, (x0 + 20, y0 + 36 + len(nl) * 42 + j * 34), ln, F("r", 28), INK2)
    text(dr, (110, 245), "Climb only as high as the page needs  →  cost and effort rise", F("m", 34), MOD_COLORS[6])


def d_dns(scene, r, dr):
    items = scene["items"]
    icons = ["✓", "✓", "?"]
    cols = ["#2f6fb5", "#7a4fb0", MOD_COLORS[7]]
    for i in range(r + 1):
        y = 260 + i * 210
        dr.rounded_rectangle([110, y, W - 110, y + 180], radius=22, fill=PAPER, outline=LINE, width=2)
        dr.rounded_rectangle([110, y, 330, y + 180], radius=22, fill=cols[i])
        name, desc = items[i].split(" · ")
        text(dr, (220, y + 58), name, F("b", 56), "#ffffff", center=True)
        text(dr, (380, y + 58), desc, F("m", 46), INK)


def d_warmup(scene, r, dr):
    items = scene["items"]
    base_y, unit = 860, 16
    vals = [10, 20, 30]
    for i in range(min(r + 1, 3)):
        x0 = 260 + i * 330
        hh = vals[i] * unit
        dr.rounded_rectangle([x0, base_y - hh, x0 + 220, base_y], radius=12, fill=MOD_COLORS[7])
        text(dr, (x0 + 110, base_y - hh - 60), f"{vals[i]}/day", F("b", 44), INK, center=True)
        text(dr, (x0 + 110, base_y + 20), items[i].split(" · ")[0], F("m", 34), INK2, center=True)
    dr.line([(200, base_y), (1300, base_y)], fill=MUTED, width=3)
    if r >= 3:
        for xx in range(1260, 1700, 40):
            dr.line([(xx, base_y - 170), (xx + 22, base_y - 170)], fill=MOD_COLORS[7], width=6)
        text(dr, (1300, base_y - 240), "Keep warm-up running", F("b", 40), MOD_COLORS[7])
        text(dr, (1300, base_y - 140), "alongside every campaign", F("r", 34), INK2)
    text(dr, (110, 245), "New mailboxes have no reputation: earn it over ~3 weeks", F("m", 34), MOD_COLORS[7])


def d_mailbox(scene, r, dr):
    items = scene["items"]
    for i in range(r + 1):
        y = 260 + i * 160
        dr.rounded_rectangle([110, y, W - 110, y + 135], radius=20, fill=PAPER if i < 3 else "#fbecec", outline=LINE, width=2)
        text(dr, (160, y + 18), f"{i + 1}", F("b", 80), MOD_COLORS[7])
        text(dr, (260, y + 38), items[i], F("b", 54), INK)


def d_sequence(scene, r, dr):
    items = scene["items"]
    roles = ["Signal opener + offer", "New proof point", "Another pain angle", "Social proof / result", "Short nudge", "Budget? Timing? Not relevant?"]
    y = 520
    dr.line([(170, y), (W - 170, y)], fill=LINE, width=8)
    gap = (W - 340) / (len(items) - 1)
    for i in range(r + 1):
        cx = 170 + i * gap
        col = MOD_COLORS[7] if i < 5 else GOOD
        dr.ellipse([cx - 62, y - 62, cx + 62, y + 62], fill=col)
        num, when = items[i].split(" · ")
        text(dr, (cx, y - 40), num, F("b", 64), "#ffffff", center=True)
        text(dr, (cx, y - 140), when, F("m", 40), INK2, center=True)
        for j, ln in enumerate(wrap(dr, roles[i], F("m", 36), 270)):
            text(dr, (cx, y + 95 + j * 46), ln, F("m", 36), INK, center=True)
    if r == len(items) - 1:
        text(dr, (110, 850), "Then: A/B test every step · micro-campaigns over heavy AI personalisation · follow-up sequence for non-responders",
             F("r", 32), INK2)


def d_credits(scene, r, dr):
    items = scene["items"]
    vals = [float(it.split()[-1]) for it in items]
    names = [" ".join(it.split()[:-1]) for it in items]
    maxv, x0, bw = 30, 420, 900
    for i, (nm, v) in enumerate(zip(names, vals)):
        y = 250 + i * 88
        text(dr, (x0 - 30, y + 14), nm, F("m", 38), INK, anchor_right=True)
        dr.rounded_rectangle([x0, y + 8, x0 + bw * v / maxv, y + 66], radius=10, fill=MOD_COLORS[8])
        text(dr, (x0 + bw * v / maxv + 20, y + 14), f"{v:g}", F("b", 38), INK)
    text(dr, (x0, 790), "Total: 118.6 credits · 50 companies → 30 qualified → 40 verified contacts", F("b", 38), MOD_COLORS[8])
    if r >= 1:
        dr.rounded_rectangle([1420, 250, W - 110, 740], radius=22, fill=PAPER, outline=LINE, width=2)
        text(dr, (1460, 285), "AI COLUMN", F("m", 28), MUTED)
        text(dr, (1460, 330), "19", F("b", 120), GOOD)
        text(dr, (1460, 470), "credits spent", F("r", 34), INK2)
        text(dr, (1460, 540), "~150", F("b", 80), BAD)
        text(dr, (1460, 640), "Argon on all 50", F("r", 34), INK2)


DIAGRAMS = {k[2:]: v for k, v in globals().items() if k.startswith("d_")}


def k_diagram(scene, r):
    im, dr = base(scene)
    header(dr, scene)
    DIAGRAMS[scene["kind"].split(":")[1]](scene, r, dr)
    footer(dr, scene)
    return im


KINDS = {"title": k_title, "chapter": k_chapter, "bullets": k_bullets, "tip": k_tip, "real": k_real,
         "mistake": k_mistake, "recap": k_recap, "quiz": k_quiz, "shots": k_shots}


CREDITS_SO_FAR = {"Formula, then enrichment": "25", "Pick the cheapest model that works": "83",
                  "The contact pipeline": "118.6"}


def render_state(scene, r):
    k = scene["kind"]
    im = k_diagram(scene, r) if k.startswith("diagram:") else KINDS[k](scene, r)
    c = CREDITS_SO_FAR.get(scene["title"])
    if c:
        dr = ImageDraw.Draw(im)
        label = f"Credits used so far: {c}"
        f = F("b", 30)
        w = tlen(dr, label, f) + 50
        x1 = W - 110
        dr.rounded_rectangle([x1 - w, 128, x1, 180], radius=26, fill="#fff4d6", outline=MOD_COLORS[8], width=3)
        text(dr, (x1 - w + 25, 136), label, f, "#7a5b00")
    return im


# ── stages ──
def stage_stills():
    d = OUT / "stills"
    d.mkdir(parents=True, exist_ok=True)
    for old in d.glob("*.png"):
        old.unlink()
    for i, sc in enumerate(course.S, 1):
        for r in range(len(sc["beats"])):
            render_state(sc, r).save(d / f"s{i:02d}_b{r}.png")
    print("stills:", len(list(d.glob("*.png"))))


def stage_sheets():
    d = OUT / "sheets"
    d.mkdir(parents=True, exist_ok=True)
    for old in d.glob("*.png"):
        old.unlink()
    finals = [(i, OUT / "stills" / f"s{i:02d}_b{len(sc['beats']) - 1}.png") for i, sc in enumerate(course.S, 1)]
    for k in range(0, len(finals), 12):
        sheet = Image.new("RGB", (1920, 1080), "white")
        dr = ImageDraw.Draw(sheet)
        for j, (i, p) in enumerate(finals[k:k + 12]):
            x, y = (j % 4) * 480, (j // 4) * 360
            sheet.paste(Image.open(p).resize((480, 270)), (x, y))
            dr.rectangle([x, y + 270, x + 480, y + 300], fill="#fff6b0")
            dr.text((x + 6, y + 276), f"scene {i}: {course.S[i - 1]['title'][:48]}", fill="black")
        sheet.save(d / f"sheet{k // 12 + 1}.png")
    print("sheets:", len(list(d.glob("*.png"))))


def stage_script():
    lines = ["# GTM Engineering, from zero: the Saffron course (v3 script)\n"]
    words = 0
    for i, sc in enumerate(course.S, 1):
        lines.append(f"\n## Scene {i} · {course.MODULES[sc['module']]} · {sc['kind']} · {sc['eyebrow']} · {sc['title']}")
        lines.append("Visual items: " + " | ".join(it if isinstance(it, str) else it[2] for it in sc["items"]))
        for r, b in enumerate(sc["beats"]):
            lines.append(f"- Beat {r + 1}: {b}")
            words += len(b.split())
    lines.insert(1, f"\n{len(course.S)} scenes · {sum(len(s['beats']) for s in course.S)} beats · {words} words (~{words / 157:.0f} min at Piper's pace)\n")
    (OUT / "script.md").write_text("\n".join(lines))
    print("script words:", words)


def duration(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def stage_audio():
    d = OUT / "audio"
    d.mkdir(parents=True, exist_ok=True)
    n = 0
    for i, sc in enumerate(course.S, 1):
        for r, b in enumerate(sc["beats"]):
            out = d / f"s{i:02d}_b{r}.wav"
            side = out.with_suffix(".txt")
            if out.exists() and side.exists() and side.read_text() == b:
                continue
            subprocess.run([str(PIPER), "-m", str(VOICE), "-f", str(out), "--sentence_silence", "0.3",
                            "--length_scale", "1.03"], input=b.encode(), capture_output=True, check=True)
            side.write_text(b)
            clip = OUT / "clips" / f"s{i:02d}_b{r}.mp4"
            if clip.exists():
                clip.unlink()
            n += 1
    print("audio rendered:", n)


def srt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def write_srt(txt, total, path):
    sents = [s.strip() for s in re.split(r"(?<=[.!?:])\s+", txt) if s.strip()]
    chunks = []
    for s in sents:
        chunks.extend(textwrap.wrap(s, 96))
    wts = [len(c) + 10 for c in chunks]
    t, out = 0.1, []
    usable = total - 0.2
    for k, (c, w) in enumerate(zip(chunks, wts), 1):
        dt = usable * w / sum(wts)
        out.append(f"{k}\n{srt_time(t)} --> {srt_time(t + dt - 0.04)}\n{c}\n")
        t += dt
    path.write_text("\n".join(out))


def stage_clips():
    d = OUT / "clips"
    d.mkdir(parents=True, exist_ok=True)
    style = ("FontName=Ubuntu,FontSize=11,PrimaryColour=&H00FFFFFF,BackColour=&H96151F2B,"
             "BorderStyle=4,Outline=0,Shadow=0,MarginV=19,MarginL=80,MarginR=80")
    for i, sc in enumerate(course.S, 1):
        for r, b in enumerate(sc["beats"]):
            out = d / f"s{i:02d}_b{r}.mp4"
            if out.exists():
                continue
            still = OUT / "stills" / f"s{i:02d}_b{r}.png"
            wav = OUT / "audio" / f"s{i:02d}_b{r}.wav"
            pad = 0.9 if (r == len(sc["beats"]) - 1) else 0.35
            if sc["kind"] == "quiz" and r == 0:
                pad = 3.0  # thinking time
            total = duration(wav) + pad
            srt = d / f"s{i:02d}_b{r}.srt"
            write_srt(b, total - pad + 0.2, srt)
            vf = f"fps={FPS},format=yuv420p"
            if r == 0:
                vf += f",fade=t=in:st=0:d=0.35:color={'0x0f1b26' if sc['kind'] in ('chapter', 'title', 'quiz') else '0xf3f5f6'}"
            vf += f",subtitles={srt}:force_style='{style}'"
            subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-loop", "1", "-framerate", str(FPS),
                            "-i", str(still), "-i", str(wav), "-vf", vf, "-af", f"apad=pad_dur={pad}",
                            "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage",
                            "-crf", "21", "-threads", "4", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
                            "-ac", "1", str(out)], check=True)
        print(f"clips scene {i}/{len(course.S)}", flush=True)


def stage_final():
    clips = []
    for i, sc in enumerate(course.S, 1):
        clips += [OUT / "clips" / f"s{i:02d}_b{r}.mp4" for r in range(len(sc["beats"]))]
    lst = OUT / "concat.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in clips))
    out = ROOT / "Saffron-GTM-Course.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", "-movflags", "+faststart", str(out)], check=True)
    print(f"final {out} {duration(out) / 60:.1f} min")


if __name__ == "__main__":
    {"stills": stage_stills, "sheets": stage_sheets, "script": stage_script, "audio": stage_audio,
     "clips": stage_clips, "final": stage_final}[sys.argv[1]]()
