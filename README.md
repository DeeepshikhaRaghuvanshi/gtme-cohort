# Saffron · GTM Engineering cohort workspace

**Private repo:** it contains third-party personal data. Do not make it public.

Deepu's working files for the Stable GTM "GTM Engineering" cohort (Days 1–36 so far), built around her portfolio company Saffron.

- **Start here:** [HANDOFF.md](HANDOFF.md) for status, links, what was built and open items.
- **Course notes:** [notes/00-cohort-master-notes.md](notes/00-cohort-master-notes.md)
- **Working with Claude Code:** [CLAUDE.md](CLAUDE.md) is loaded automatically and covers the session rules and how to keep the repo in sync.
- **Shared deliverables** (Google Docs and the course video) are in the "GTM Cohort Catch-up" Google Drive folder. Links are in HANDOFF.md.

## Setup on a new machine
```bash
git clone <this repo> && cd <repo>
pip install python-docx openpyxl pillow   # for scripts/ and data/ tools
./scripts/setup_video_tools.sh            # only if you'll re-render the course video (needs ffmpeg)
```
