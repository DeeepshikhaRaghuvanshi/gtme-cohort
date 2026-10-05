"""Render the Saffron course-summary video.

Stages (run in order, each idempotent):
  python3 render.py audio    # Piper TTS per scene -> build/audio/sNN.wav
  python3 render.py slides   # 1920x1080 PNG slides   -> build/slides/sNN_k.png
  python3 render.py clips    # per-scene MP4 with slow zoom + burned subtitles -> build/clips/sNN.mp4
  python3 render.py final    # concat -> Saffron-GTM-Course-Summary.mp4
Narration comes from script.md ("## Scene N" blocks, "Narration:" line), so the script stays the source of truth.
"""
import re
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
EVID = ROOT.parent / "buildlog" / "evidence"
BUILD = ROOT / "build"
PIPER = ROOT / "piper" / "piper"
VOICE = ROOT / "voice" / "en_US-lessac-medium.onnx"
W, H, FPS = 1920, 1080, 30

BG, INK, INK2, MUTED, ACCENT, SOFT, LINE = "#f4f6f7", "#15212e", "#3d4b59", "#6a7885", "#0e6f69", "#e2f1ef", "#dbe2e7"
FONT_DIR = "/usr/share/fonts/truetype/ubuntu"


def font(style, size):
    name = {"regular": "Ubuntu-R.ttf", "bold": "Ubuntu-B.ttf", "medium": "Ubuntu-M.ttf", "mono": "UbuntuMono-R.ttf"}[style]
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except OSError:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)


# Visual spec per scene: ("card", eyebrow, title, [lines]) or ("images", eyebrow, title, [(file, crop_box_or_None)])
SCENES = {
    1: ("title", "GTM ENGINEERING COURSE · DAYS 1–28", "Saffron: the GTM Engineering course so far",
        ["The brief: find the companies most likely to buy this quarter, and the right person to talk to at each."]),
    2: ("card", "DAYS 1–2 · THE ROLE", "What a GTM engineer does",
        ["GTM = go-to-market: everything a company does to win customers",
         "Lead → MQL (looks like a fit) → SQL (worth a real conversation) → Opportunity → Closed",
         "The GTM engineer owns the top: unknown companies → qualified conversations",
         "Systems do the research, so sales spends its day in conversations"]),
    3: ("card", "DAYS 3–4 · THE MAP", "The seven layers",
        ["L1 Data · L2 Enrichment · L3 Signals", "L4 Orchestration · L5 Execution", "L6 CRM · L7 AI & agents",
         "Value is created inside each layer and lost at the handoffs",
         "When something breaks: which layer, which handoff?"]),
    4: ("card", "DAYS 5–6 · COMPANY & ICP", "Saffron and its ideal customer",
        ["AI-era technical interviews · YC Spring 2026",
         "$199–$499 a month by card → one engineering leader can say yes",
         "ICP (ideal customer profile): US tech, 50–500 people, hiring engineers",
         "Decision maker: CTO / VP Engineering (signs)",
         "Champion: engineering manager / recruiter (feels the pain)"]),
    5: ("images", "DAYS 7–8 · MARKET SIZING", "TAM: everyone who could buy · ~54,000",
        [("02-tam-filters.png", (0, 0, 300, 340)), ("02-tam-filters.png", (0, 320, 300, 660)), ("02-tam-results.png", None)]),
    6: ("images", "DAYS 7–8 · MARKET SIZING", "SAM: who Saffron can serve · ~12,000",
        [("03-sam-filters.png", None), ("03-sam-results.png", None)]),
    7: ("images", "DAYS 7–8 · MARKET SIZING", "SOM: what it can win this year · 2,921",
        [("04-som-filters.png", (0, 0, 262, 450)), ("04-som-filters.png", (0, 445, 262, 895)), ("04-som-results.png", None)]),
    8: ("card", "DAYS 8–10 · SIGNALS & THE BRIEF", "Why now, and what to say",
        ["Signal: a public fact (posting 12 engineering jobs → dozens of interviews ahead)",
         "Intent: a person doing something toward you (visits the pricing page)",
         "Trigger: what you do in response",
         "Offer: “Your engineers ship with AI. Your interviews don't test it.”"]),
    9: ("card", "DAYS 11–14 · THE DATA LAYER", "Where the data comes from",
        ["Several sources → merge (no database is complete or current)",
         "Dedupe: LinkedIn URL → email → name + company",
         "Verify every email before sending",
         "Dead addresses → bounces → your domain starts to look like spam"]),
    10: ("images", "DAYS 15–16 · THE FIRST LIST", "50 target companies from two sources",
         [("05-clay-filters.png", (0, 0, 350, 300)), ("05-clay-filters.png", (0, 280, 350, 580)), ("05-clay-results.png", None)]),
    11: ("card", "DAYS 15–16 · CLAY", "Clay: the workbench",
         ["A spreadsheet where each column calls a service:",
          "a data provider, an AI researcher, or a free formula",
          "Every call costs credits, sometimes even when it fails",
          "Auto-run off · Hide, never delete · Test on 10 rows first · Formulas are free"]),
    12: ("images", "DAYS 17–20 · IMPORT & FORMULAS", "Start with three columns, clean the domain",
         [("06-clean-domain-formula.png", None)]),
    13: ("images", "DAYS 17–20 · ENRICHMENT", "Enrichment: facts from outside · 25 credits",
         [("06-run-menu.png", None), ("06-enrich-all-50.png", (0, 0, 722, 380)), ("06-credits-after-50.png", None)]),
    14: ("card", "DAYS 21–22 · RUN CONDITIONS", "Turning signals into columns",
         ["Open engineering roles = the hiring pain",
          "No recruiting team → hires through agencies → not a buyer",
          "Run condition: only run if openings ≥ 1",
          "Rows skipped by a run condition cost nothing"]),
    15: ("images", "DAYS 25–26 · CLAYGENT", "When no database has the answer",
         [("07-ai-tools-columns.png", (0, 0, 480, 380))]),
    16: ("images", "DAYS 25–26 · QUALIFICATION", "A decision with a reason: 30 of 50",
         [("07-formula-before.png", (0, 0, 880, 400)), ("07-formula-after.png", (0, 0, 880, 400))]),
    17: ("card", "PEOPLE SEARCH", "Finding the right people",
         ["First search: Co-Founder · Founder & CEO · Talent Acquisition Coordinator",
          "Fix: remove “Co-Founder”, filter seniority C-Level / VP / Head / Director / Manager",
          "Then: VP of Engineering · SVP of Engineering",
          "27 companies · 79 people · ~9 credits (0.1 per person)"]),
    18: ("images", "PEOPLE · PERSONA", "Decision maker, champion, or skip",
         [("raw-145.png", (430, 95, 715, 520)), ("raw-145.png", (430, 520, 715, 975))]),
    19: ("images", "A BUG WORTH REMEMBERING", "Read the preview before you save",
         [("raw-147.png", (30, 100, 400, 520)), ("raw-147.png", (440, 700, 910, 1180)),
          ("raw-148.png", (1545, 700, 2000, 1110)), ("raw-148.png", (75, 80, 425, 520))]),
    20: ("images", "EMAILS", "Verified work emails: 40 of 45",
         [("raw-157.png", (430, 95, 1060, 500))]),
    21: ("card", "THE BONUS POINT", "What it cost: 118.6 credits",
         ["50 companies → 30 qualified → 40 verified contacts",
          "Accounts 83 · People 9.1 · Emails 26.5",
          "AI column: 19 credits instead of ~150",
          "Cheapest model that works · run conditions · compare providers · test on 10 rows"]),
    22: ("card", "THE DELIVERABLE", "What sales uses on Monday",
         ["Client delivery sheet in Drive",
          "Contacts: 40 with verified emails + why their company qualified",
          "Accounts: all 50 with the decision and the reason",
          "Follow-ups: LinkedIn-only contacts, next batch, manual review"]),
    23: ("card", "DAYS 27–28 · YESTERDAY'S CLASS", "Web scraping + the HTTP API column",
         ["HTTP API column: call any outside API from Clay",
          "Scraping ladder: native scraper → Chrome extension → Claygent → Apify → Zenrows",
          "Start with the cheapest tool that can do the job",
          "New bar: at least 70% of a list should qualify"]),
    24: ("card", "WHAT'S NEXT", "Over to you",
         ["Share Strategy Doc v2 with Yogesh · post the LinkedIn post",
          "Record 5 Loom walkthroughs · connect with the GTM agencies",
          "Work the follow-ups · mail-server check before any email is sent",
          "Next in the course: outreach tools, automation, AI agents"]),
    25: ("card", "BACK TO THE BRIEF", "The brief, answered",
         ["Which companies are most likely to buy this quarter?",
          "→ 30 qualified companies, each with a written reason",
          "Who do we talk to? → 40 verified decision makers and champions",
          "Everything is in Drive: GTM Cohort Catch-up"]),
}


def narration():
    text = (ROOT / "script.md").read_text()
    out = {}
    for m in re.finditer(r"^## Scene (\d+):.*?^Narration: (.+?)$", text, re.M | re.S):
        out[int(m.group(1))] = m.group(2).strip()
    return out


ARROW_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def text_fb(dr, xy, text, fnt, fill):
    """Draw text; characters missing from Ubuntu ("→") are drawn with DejaVu Sans at the same size."""
    x, y = xy
    fb = ImageFont.truetype(ARROW_FONT, fnt.size)
    for i, part in enumerate(text.split("→")):
        if i:
            dr.text((x, y + int(fnt.size * 0.08)), "→", font=fb, fill=fill)
            x += dr.textlength("→", font=fb)
        dr.text((x, y), part, font=fnt, fill=fill)
        x += dr.textlength(part, font=fnt)


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


# ---------- stage: audio ----------
def stage_audio():
    d = BUILD / "audio"
    d.mkdir(parents=True, exist_ok=True)
    for n, text in sorted(narration().items()):
        out = d / f"s{n:02d}.wav"
        if out.exists():
            continue
        run([str(PIPER), "-m", str(VOICE), "-f", str(out), "--sentence_silence", "0.35", "--length_scale", "1.05"],
            input=text.encode(), capture_output=True)
        print(f"audio s{n:02d} {duration(out):.1f}s", flush=True)


# ---------- stage: slides ----------
def draw_header(dr, eyebrow, title, title_size):
    dr.text((110, 70), eyebrow, font=font("medium", 30), fill=ACCENT)
    size = title_size
    while dr.textlength(title, font=font("bold", size)) > W - 560 and size > 36:
        size -= 2
    dr.text((110, 115), title, font=font("bold", size), fill=INK)
    dr.text((W - 110, 78), "Saffron · GTM Engineering catch-up", font=font("regular", 24), fill=MUTED, anchor="ra")


def card(eyebrow, title, lines, is_title=False):
    im = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(im)
    if is_title:
        dr.rectangle([0, 0, W, H], fill=INK)
        dr.text((140, 330), eyebrow, font=font("medium", 34), fill="#4cc2b6")
        y = 390
        for ln in textwrap.wrap(title, 26):
            dr.text((140, y), ln, font=font("bold", 96), fill="#ffffff")
            y += 112
        y += 40
        for ln in textwrap.wrap(lines[0], 62):
            dr.text((140, y), ln, font=font("regular", 44), fill="#c1ccd5")
            y += 58
        return im
    draw_header(dr, eyebrow, title, 76)
    dr.line([(110, 230), (W - 110, 230)], fill=LINE, width=2)
    y, f = 285, font("regular", 42)
    for ln in lines:
        wrapped = textwrap.wrap(ln, 70) or [""]
        dr.rounded_rectangle([110, y + 12, 122, y + 24], radius=3, fill=ACCENT)
        for i, part in enumerate(wrapped):
            text_fb(dr, (150, y), part, f, INK2 if i else INK)
            y += 56
        y += 20
        if y > 880:
            break
    return im


def image_slide(eyebrow, title, path, crop):
    im = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(im)
    draw_header(dr, eyebrow, title, 60)
    shot = Image.open(EVID / path).convert("RGB")
    if crop:
        shot = shot.crop(crop)
    box_w, box_h, top = W - 220, 880 - 215, 215
    scale = min(box_w / shot.width, box_h / shot.height, 3.0)
    shot = shot.resize((int(shot.width * scale), int(shot.height * scale)), Image.LANCZOS)
    x, y = (W - shot.width) // 2, top + (box_h - shot.height) // 2
    shadow = Image.new("RGBA", (shot.width + 40, shot.height + 40), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([20, 20, shot.width + 20, shot.height + 20], radius=10, fill=(20, 33, 46, 60))
    im.paste(shadow.filter(ImageFilter.GaussianBlur(12)), (x - 20, y - 14), shadow.filter(ImageFilter.GaussianBlur(12)))
    im.paste(shot, (x, y))
    dr.rectangle([x - 1, y - 1, x + shot.width, y + shot.height], outline=LINE, width=2)
    return im


def stage_slides():
    d = BUILD / "slides"
    d.mkdir(parents=True, exist_ok=True)
    for n, spec in SCENES.items():
        kind, eyebrow, title, items = spec
        if kind in ("card", "title"):
            card(eyebrow, title, items, kind == "title").save(d / f"s{n:02d}_0.png")
        else:
            for k, (path, crop) in enumerate(items):
                image_slide(eyebrow, title, path, crop).save(d / f"s{n:02d}_{k}.png")
    print("slides:", len(list(d.glob("*.png"))), flush=True)


# ---------- stage: clips ----------
def srt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def write_srt(text, total, path):
    sents = [s.strip() for s in re.split(r"(?<=[.!?:])\s+", text) if s.strip()]
    chunks = []
    for s in sents:  # keep each subtitle short enough for two lines
        chunks.extend(textwrap.wrap(s, 110))
    weights = [len(c) + 12 for c in chunks]
    t, lines = 0.15, []
    usable = total - 0.3
    for i, (c, w) in enumerate(zip(chunks, weights), 1):
        dt = usable * w / sum(weights)
        lines.append(f"{i}\n{srt_time(t)} --> {srt_time(t + dt - 0.05)}\n{c}\n")
        t += dt
    path.write_text("\n".join(lines))


def stage_clips():
    d = BUILD / "clips"
    d.mkdir(parents=True, exist_ok=True)
    narr = narration()
    for n in sorted(SCENES):
        out = d / f"s{n:02d}.mp4"
        if out.exists():
            continue
        audio = BUILD / "audio" / f"s{n:02d}.wav"
        total = duration(audio) + 0.8
        slides = sorted((BUILD / "slides").glob(f"s{n:02d}_*.png"))
        seg = total / len(slides)
        frames = int(seg * FPS) + 1
        srt = d / f"s{n:02d}.srt"
        write_srt(narr[n], total, srt)
        inputs, filters = [], []
        for i, s in enumerate(slides):
            inputs += ["-loop", "1", "-t", f"{seg:.3f}", "-i", str(s)]
            filters.append(
                f"[{i}:v]scale=3840:2160,zoompan=z='min(zoom+0.00015,1.03)':d={frames}:"
                f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},trim=duration={seg:.3f},setpts=PTS-STARTPTS[v{i}]")
        cat = "".join(f"[v{i}]" for i in range(len(slides)))
        style = ("FontName=Ubuntu,FontSize=13,PrimaryColour=&H00FFFFFF,BackColour=&HA0151F2B,"
                 "BorderStyle=4,Outline=0,Shadow=0,MarginV=22,MarginL=60,MarginR=60")
        filters.append(f"{cat}concat=n={len(slides)}:v=1:a=0,fade=t=in:st=0:d=0.35,"
                       f"fade=t=out:st={total - 0.4:.3f}:d=0.4,subtitles={srt}:force_style='{style}'[v]")
        cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", *inputs, "-i", str(audio),
               "-filter_complex", ";".join(filters), "-map", "[v]", "-map", f"{len(slides)}:a",
               "-af", "apad=pad_dur=0.8", "-t", f"{total:.3f}",
               "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-threads", "4",
               "-c:a", "aac", "-b:a", "160k", "-ar", "44100", str(out)]
        run(cmd)
        print(f"clip s{n:02d} {total:.1f}s", flush=True)


# ---------- stage: final ----------
def stage_final():
    d = BUILD / "clips"
    lst = BUILD / "concat.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in sorted(d.glob("s*.mp4"))))
    out = ROOT / "Saffron-GTM-Course-Summary.mp4"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-c", "copy", "-movflags", "+faststart", str(out)])
    print(f"final {out} {duration(out):.1f}s", flush=True)


if __name__ == "__main__":
    {"audio": stage_audio, "slides": stage_slides, "clips": stage_clips, "final": stage_final}[sys.argv[1]]()
