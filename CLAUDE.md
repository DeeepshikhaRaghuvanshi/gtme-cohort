# Saffron GTM cohort workspace

Deepu's (Deepshikha's) working repo for the Stable GTM "GTM Engineering" cohort, with **Saffron** (YC S26) as her portfolio company. Deepu and Abi both use it, from Claude Code sessions on different machines.

## Start of every session
1. `git pull --rebase` before touching anything.
2. Read **HANDOFF.md**. It's the source of truth for status, deliverables and links, how things were built, and open items.
3. For course content, start with `notes/00-cohort-master-notes.md`, then the per-session files in `notes/`.

## Keep the repo in sync (required)
- **After every meaningful change** (a new class's notes, a deliverable, a Clay step, a decision):
  1. update HANDOFF.md: the status line, §3 "Where everything lives", §8 "Open items"
  2. `git add` the specific files
  3. commit with a clear message, e.g. `notes: add D37-D38`
  4. `git push`
- Don't end a session with uncommitted work. If a push is rejected, `git pull --rebase`, resolve, then push. Never force-push.
- Two people edit this repo. Make small, focused commits and pull before starting.
- Drive is the sharing layer for Deepu's Google Docs. After changing a deliverable, regenerate the .docx with `python3 scripts/md2docx.py <in.md> <out.docx>` and update the Drive copy (rclone if set up on that machine, otherwise upload manually). Say which Drive files changed in the commit message.

## GitHub access
- Remote: `git@github.com:DeeepshikhaRaghuvanshi/gtme-cohort.git` (private). Use plain `git` over **SSH** only. **Don't use or install the `gh` CLI**; it isn't part of this setup.
- On Abi's machine, any repo under `~/workspace/deepu/` automatically uses Deepu's SSH key (`~/.ssh/id_ed25519_deepu`) and her git identity via `includeIf` → `~/.gitconfig-deepu` (see `~/workspace/SSH-Multi-Account-Setup.md`). Don't change the remote URL or add credential helpers.
- On Deepu's own machine, her normal GitHub SSH key works as-is.

## Never commit
- Media or large binaries: videos, audio, voice models, zips. They live in Drive; `.gitignore` covers them.
- Secrets: API keys, OAuth tokens, rclone config, Clay or Apollo credentials.
- **This repo holds third-party personal data** (classmates' details in `source/` transcripts; prospects' names and work emails in `data/` and `buildlog/evidence/`). **Keep it private.** Never make it public, never paste that data into public posts, and don't add more personal data than the work needs.

## How Deepu and Abi like to work
- Both are experienced engineers (full-stack/data) who are new to GTM vocabulary. Explain GTM concepts fully, keep tool steps terse, and don't hand-hold on browsers or bookmarks.
- For hands-on tool work (Clay, Prospeo, Instantly…), give **one step at a time** and wait for their screenshot. Speed up by doing docs and notes in parallel, not by batching instructions.
- Say which account each tool uses: **deepshikhagtme@gmail.com** for GTM tools (Clay, Prospeo, the Drive deliverables folder); her **personal account** for LinkedIn and Loom. Never create a second LinkedIn.
- Clay house rules: auto-run off; hide columns, never delete; test on 10 rows; formulas are free; cheapest AI model first (Helium); gate expensive columns with run conditions; read the preview before saving.
- Log every small practical learning in the build log's "Field notes" (`buildlog/saffron-build-log.html`) and in HANDOFF.md.
- Before calling something done, check the real output (open the file, look at frames). For big deliverables, get an independent review from the most capable model first.
- Text meant to be copied out (messages, posts, prompts): plain flush-left lines between `---` rules, with a blank line before the closing rule. No blockquotes or tables.

## Layout
- `notes/`: study notes per class plus the master notes. `source/` holds the raw class material they were written from.
- `strategy/`: Strategy Doc v2. `clay/`: build sheet and credit log. `data/`: lists, exports, merge and delivery-sheet scripts.
- `kt/`: KT pack. `guide/`: playbook. `buildlog/`: build log plus evidence screenshots. `linkedin/`: post draft.
- `video/`: course video source (`course.py` content, `render3.py` renderer). Run `scripts/setup_video_tools.sh` once per machine before rendering.
- `docs/claude-memory/`: copy of the Claude memory notes from Abi's machine, for context.

## Adding a new class
Get the Gemini notes (download or screenshots; some course docs have downloads disabled by the owner, so don't work around that). Then:
1. Write `notes/<Dxx-Dyy>_<topic>.md`.
2. Update `notes/00-cohort-master-notes.md` and the "Latest" section of the KT pack.
3. Optionally add scenes to `video/course.py` and re-render.
4. Update HANDOFF.md, commit, push.
