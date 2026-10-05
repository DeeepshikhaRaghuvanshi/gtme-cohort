---
name: feedback-verify-and-review
description: "Before calling a deliverable done, inspect the actual output yourself; for big deliverables Abi wants an independent review by the most capable model first"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b2f209e2-18a4-4623-ad2e-e3a33a89146a
  modified: 2026-10-05T13:40:24.662Z
---

Inspect the real output before reporting it done: extract frames from videos, open the generated files, read back uploads. Say plainly what you could not check (e.g. Claude can't hear audio).

**Why:** On 2026-10-02, after the first video upload, Abi asked "did you check the video output yourself?". A full frame check then found broken arrow glyphs and subtitles covering content, which earlier spot checks had missed. For the full course video he explicitly asked for a review agent on the latest, most capable model (Fable) before rendering.

**How to apply:** For videos, check a frame from every scene on contact sheets. For large or important deliverables, run an independent review agent on the most capable model before final render or publish, then apply the suggestions that hold up against the sources and explain any you didn't apply. Related: [[feedback-lean-guides]], [[deepu-gtme-catchup]]
