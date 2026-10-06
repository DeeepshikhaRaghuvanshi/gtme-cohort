---
name: feedback-homework-guides
description: "Homework guides for Deepu must teach the missed class topics in depth AND be research-backed with a Gemini (agy) second opinion, cross-verified"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3474aab4-ca23-4bb2-82e2-d8fe7719b9b2
  modified: 2026-10-06T13:56:00.353Z
---

Homework guides for Deepu (e.g. homework/*.md → Drive "Homework - …" docs) must:
1. **Teach the class topics in depth, not just the assignment.** Deepu did not attend those classes, so the guide is first a self-contained course on the sessions it draws on (what/why/how/rules/numbers/mistakes/what it means for Saffron), then the assignment.
2. **Be research-backed and cross-verified.** Two tracks: Claude (class notes + web, cited) and Gemini via `agy -p --model gemini-3.1-pro-high` (fallback gemini-3.8-flash-high; `agy models` lists them). Each checks the other; resolve conflicts with sources; flag anything unverified.
3. Confirm which assignment is meant before planning. On 2026-10-06 I assumed a redo of the D37–38 HeyReach guide, but Abi meant the D35–36 Instantly one.

**Why:** the 2026-10-05 HeyReach CHRO guide was written from the class summary alone, and Deepu had to enrich it with Gemini herself. Abi wants the guides to be complete when they reach her.

**How to apply:** budget for a research brief, both tracks, a verification table, and an independent review before upload. See [[feedback-verify-and-review]], [[deepu-gtme-catchup]].
