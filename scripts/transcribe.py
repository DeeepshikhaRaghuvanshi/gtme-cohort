"""Transcribe the two cohort videos that have no Gemini transcript.
Streams each mp4 out of its zip into the scratchpad, converts to 16k mono wav,
runs faster-whisper on GPU (CPU fallback), writes timestamped markdown, cleans temps."""
import os, subprocess, sys, time
from faster_whisper import WhisperModel

SCRATCH = sys.argv[1]
DL = "/mnt/c/Users/Abi M/Downloads"
OUT = os.path.expanduser("~/workspace/deepu/gtme-cohort/source")
JOBS = [
    ("GTM Engineering Course -20260927T044631Z-1-002.zip",
     "GTM Engineering Course /LinkedIn Sales Navigator - 2026_07_21 08_59 IST - Recording.mp4",
     "X2_linkedin-sales-navigator-walkthrough"),
    ("GTM Engineering Course -20260927T044631Z-1-003.zip",
     "GTM Engineering Course /Instantly Training_.mp4",
     "X3_instantly-training"),
]

def load_model():
    try:
        return WhisperModel("medium.en", device="cuda", compute_type="int8_float16"), "cuda medium.en"
    except Exception as e:
        print("CUDA load failed, falling back to CPU:", e, flush=True)
        return WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=4), "cpu small.en"

def ts(s):
    s = int(s); return f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}"

model, desc = load_model()
for zname, member, slug in JOBS:
    out_md = f"{OUT}/{slug}.md"
    if os.path.exists(out_md):
        print("skip (exists)", out_md, flush=True); continue
    mp4, wav = f"{SCRATCH}/{slug}.mp4", f"{SCRATCH}/{slug}.wav"
    try:
        t0 = time.time()
        with open(mp4, "wb") as f:
            subprocess.run(["unzip", "-p", f"{DL}/{zname}", member], stdout=f, check=True)
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", mp4,
                        "-ac", "1", "-ar", "16000", wav], check=True)
        os.remove(mp4)
        segs, info = model.transcribe(wav, vad_filter=True, beam_size=1)
        lines, para, start = [], [], None
        for s in segs:
            if start is None: start = s.start
            para.append(s.text.strip())
            if s.end - start > 60:
                lines.append(f"**[{ts(start)}]** " + " ".join(para)); para, start = [], None
        if para: lines.append(f"**[{ts(start)}]** " + " ".join(para))
        with open(out_md, "w") as f:
            f.write(f"# {member.split('/')[-1]}\n\nTranscribed locally with faster-whisper ({desc}); "
                    f"duration {ts(info.duration)}. Machine transcript — expect some misheard tool names.\n\n")
            f.write("\n\n".join(lines) + "\n")
        print(f"DONE {slug}: {len(lines)} paragraphs, {time.time()-t0:.0f}s", flush=True)
    except Exception as e:
        print(f"FAILED {slug}: {e}", flush=True)
    finally:
        for p in (mp4, wav):
            if os.path.exists(p): os.remove(p)
print("ALL FINISHED", flush=True)
