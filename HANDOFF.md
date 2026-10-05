# HANDOFF: Deepu's GTM Engineering cohort catch-up

Read this first in any new session. It's the single source of truth for what exists, where it lives, how it was built, and what's still open. Last updated: 5 Oct 2026 (cohort at D38).

**This is a git repo:** `git@github.com:DeeepshikhaRaghuvanshi/gtme-cohort.git` (private), accessed over SSH with plain git; no gh CLI. Pull before you start, and commit and push after every milestone; the rules are in CLAUDE.md. Paths like `/mnt/c/Users/Abi M/...`, the rclone remotes and the local Piper binary only exist on **Abi's WSL machine**. On another machine, use the Google Drive web UI or connector for Drive, and run `scripts/setup_video_tools.sh` for the video tools.

## 1. Who and what
- **Deepu** (Deepshikha Raghuvanshi): full-stack/data engineer (4+ yrs), enrolled in **Stable GTM's GTM Engineering cohort**. Instructor **Yogesh Jaiswal** (founder@stablegtm.com). Live classes ~08:55 IST, two "guide days" per session (D01+D02, …).
- **Abi**: her partner (also an engineer), who ran the catch-up with Claude from 27 Sep to 2 Oct 2026 while she was overloaded at work. Both are new to GTM vocabulary, not to software.
- **Portfolio company: Saffron** (YC Spring 2026, trysaffron.ai). AI-native technical interviews: a candidate builds a real feature in the client's codebase with Claude Code, and AI reviewers score the process. $199 / $499 a month, enterprise custom. Competitors: HackerRank, CodeSignal, Rounds.so, CoderPad, Karat, HackerEarth, micro1.
- **Cohort covered so far:** D01–D38 (to 5 Oct 2026) plus guest webinars (Rejoice 15 Aug, Kushagra 29 Aug), Sales Navigator and Instantly training videos. The course follows a 12-week, 60-session Learning Guide (`source/REF_learning-guide.md`).

## 2. Accounts and identities (important)
- **deepshikhagtme@gmail.com**: the dedicated GTM workspace account. Clay, Prospeo and the "GTM Cohort Catch-up" Drive folder live here. A Chrome profile "GTM" is signed in as this account, with bookmarks grouped by layer.
- **ddeepshikha.raghuvanshi@gmail.com**: her personal account. LinkedIn and Loom stay here (one LinkedIn per person; never create a second). The course Drive folder is shared to this account.
- **Apollo and Ocean.io reject Gmail sign-ups.** The fix is a custom domain + Zoho Mail (not done; it needs a purchase decision).
- **Clay workspace** "Deepshikha's Workspace", free plan: 1,005 credits at the start, **886.4 left** after the build. Free plan tables only allow **50 usable rows**.
- The cohort "Team Data" sheet holds other participants' personal data. Reading it was blocked; don't retry.

## 3. Where everything lives

### Google Drive (deepshikhagtme): "GTM Cohort Catch-up"
Folder: https://drive.google.com/drive/folders/1tq9Z9VRXfo366aSE9X9VroCUzCvNiWjw
- **Saffron - Course Summary Video.mp4** (now the full 37.8-min course): https://drive.google.com/file/d/1QRCvu_BWdcr9HMB9yA7XQzd65-vm4-Fh/view
- **KT Pack - Saffron** (Google Doc): https://docs.google.com/document/d/1iRNGee02RezXl-XNMse0UaERIm-fb9Q7cjOSkUqmxWY
- **Saffron - Client Delivery Sheet** (Google Sheet): https://docs.google.com/spreadsheets/d/1GYHrImz2G2mTps-sG9iZRxIKlayI84voEAyA3on5djY
- **LinkedIn Post - Draft** (Google Doc): https://docs.google.com/document/d/1DF_4a26ABSIbOnAaFQHY0WYbHyjxwp4HP_T-0NejyBM
- **Homework - D37-D38 HeyReach CHRO Campaign** (current homework): https://docs.google.com/document/d/10ArxuLqzYtNZMVl3LPMO-VCoKLGuc4d0vmNHjAZoeSA
- **Before Today's Class - 28 Sep Catch-up**: https://docs.google.com/document/d/13LuTb06qT1pqlWurzo2oySS0HYwr8i51pijHc5s5a24
- README - Start Here · 00 Cohort Master Notes · Strategy Doc - Saffron v2 · Clay Build Sheet · Clay Credit Log · Saffron 50 Accounts · Saffron Accounts - Qualified.csv
- **Session Notes/**: 23 docs (D01–D36, guests, videos, reference guides)
- **Build Evidence/**: ~128 files (cropped and original screenshots, raw exports, exclusions with reasons, offline build log)
- Deepu's original v1 strategy doc, "Stratergy Doc - Saffron", sits at the root of deepshikhagtme's Drive (id 1NKbR5ueSy7KNkYj2psqqIeyNpYA1q2r31dAb_uQU7gQ). Never overwrite it.

### Course material (Yogesh's folder, shared to her personal account)
https://drive.google.com/drive/folders/1xJu8MQoRouZqeaNaBxRTyJzww5tqjRrN
- **D29–D36 docs have downloads disabled by the owner** ("forbidden to download"). Don't work around it: ask Abi for screenshots or downloads, or ask Yogesh.
- Earlier sessions arrived as zips Abi downloaded (`C:\Users\Abi M\Downloads\GTM Engineering Course -*.zip`, `drive-download-20260929T030312Z-1-001.zip`).

### claude.ai pages (private; Deepu can open them only after Abi shares them)
- Playbook (GTM concepts for engineers + 2-hour Prospeo/Clay path): https://claude.ai/artifact/CM7zG8Jomdshb8pfFosbZW
- Build log (every step with evidence + "Field notes"): https://claude.ai/artifact/BoFqdK241doAAZc5NHpRDN
- KT pack (HTML version): https://claude.ai/artifact/E36QPQEcxCvTrKnYgK87tJ

### Repo / local workspace (on Abi's machine: ~/workspace/deepu/gtme-cohort)
- `HANDOFF.md`: this file
- `source/`: course docs extracted to markdown (Gemini notes include full transcripts for D01–D28), plus local transcripts of the Sales Navigator and Instantly videos, the reference guides, and the Learning Guide
- `homework/`: guides written for Deepu (current: D37–D38 HeyReach CHRO campaign)
- `docs/remote-access-setup.md`: the paused remote-access plan and how to resume it
- `notes/`: `00-cohort-master-notes.md` (one-page map, rules, glossary, tracker), one notes file per session, `D29-D36_summary-notes.md` (written from Gemini summary screenshots only) and `D27-D28_catchup-brief.md`
- `strategy/strategy-doc-saffron-v2.md`: v1 plus SOM, segments, personas, ranked signals, offers and filters, with the real TAM/SAM/SOM counts
- `data/`: `raw/` (prospeo.csv, clay.csv), `exclude.csv` (every exclusion with its reason), `merge_dedupe.py`, `saffron_50_accounts.csv`, `saffron_accounts_qualified.csv` (Clay export), `saffron_people_export.csv`, `build_delivery_sheet.py`, `Saffron - Client Delivery Sheet.xlsx`, `signal_swe_openings.csv`
- `clay/`: `build-sheet.md`, `credit-log.md`
- `kt/`: `kt-body.html` (source), `saffron-kt.html` (published), `saffron-kt.md` (Drive version)
- `buildlog/`: `saffron-build-log.html` and `evidence/` (cropped `NN-*.png` plus `raw-N.png` originals)
- `guide/saffron-gtme-playbook.html`
- `linkedin/post.md`: final post draft (uses → markers so it copies cleanly)
- `video/`: see section 6
- `scripts/`: `transcribe.py` (faster-whisper), `md2docx.py` (Markdown → .docx; no pandoc on this box)
- `out-drive/`: staging copies of what was uploaded to Drive (not in git; regenerate with md2docx)
- `docs/claude-memory/`: copy of the Claude memory notes from Abi's machine
- Not in git (they're in Drive or regenerable): videos, audio, `video/build/`, `video/piper/`, `video/voice/`, `out-drive/`

## 4. What was built (the Saffron pipeline, D11–D26 assignments)
- **Market sizing (Prospeo):** TAM ~54,000 → SAM ~12,000 → SOM **2,921**.
  - The free plan locks Funding, Job Posting and Technologies, so we used stand-ins: Engineering & Technical headcount ≥ 20, headcount growth ≥ 1% over 6 months, founded ≥ 2012.
  - SOM filters: US, 51–500 employees.
- **50-account list:** 23 from Prospeo + 40 from Clay "Find companies".
  - Clay search filters: US, 51–200 employees, software industries, ≥20 current engineers across 7 titles, ≥5 open engineering roles, privately held. That gave 196 matches; the first 40 were taken.
  - Merge: 11 excluded with reasons, 2 non-US HQ dropped, **50** kept.
- **Clay workbook "Saffron | Qualified Pipeline"** (Saffron folder):
  - Accounts table `saffron_50_accounts`:
    1. Clean Domain (JS formula)
    2. Enrich company (0.5/row): Employee Count, Industry, Country ("US"), Founded, Type
    3. Find active job openings (0.5/row, charged only on hits): 7 titles; excludes Sales/Solutions/Recruiter/Support; Limit 1–10 (Jobcount still reports the full total)
    4. Find contacts at company, HR/Recruiting → Peoplecount, run if `{{Jobcount}} >= 1`
    5. Use AI → Web research, **Helium**, run if `Jobcount >= 1 && < 5`. Outputs: `ai_tools_mentioned` (True/False), `tools`, `evidence_url`
    6. Formula **Outreach Eligibility**: "Don't outreach" if no TA team, <50 or >1000 employees, non-US or 0 openings; else "Outreach" if ≥5 openings or AI tools true. Result: **30 Outreach / 20 Don't (60%)**.
    7. A reason formula, auto-named "Staffing Summary" by Clay.
  - People table **Saffron People** (written via "Send table data", which is free):
    1. Surfe "Find people at company" (0.1/person), 8 titles, seniority C-Level/VP/Head/Director/Manager, limit 3, run if Outreach. 79 people found; only 50 rows usable on the free plan.
    2. Persona formula, auto-named "Job Seniority" by Clay: Decision maker / Champion / blank.
    3. Work Email waterfall, 11 providers (Findymail first), run if persona is set. **40 verified emails** of 45 eligible.
- **Credits:** 1,005 → 886.4, so **118.6 used**: Enrich 25, Openings 20, Recruiters 19, AI tools 19 (accounts table 83), People 9.1, Emails 26.5.
- **Client delivery sheet tabs:** Summary · Contacts (40) · Accounts (50) · Follow-ups (25).
- **Follow-ups:**
  - 10 Outreach companies beyond the 50-row limit
  - 4 LinkedIn-only contacts, plus Steven Yue (his address failed validation)
  - 3 companies where the people search found nobody (Cognition, Polymarket, RoboMQ)
  - Pinecone and Avoma to review by hand
  - 5 wrong-fit titles
- **Bugs caught in previews (good KT material):**
  - The AI answer was stored as the text "true", not the value true.
  - Pinecone's recruiting count of 0 wasn't caught by the first formula.
  - "Svp" and "Accounting" were missed by whole-word matching.
  - A run condition referenced `{{Persona}}`, but Clay had auto-named the column "Job Seniority", so it matched nothing.

## 5. Deviations from the course default (explain these to Yogesh if asked)
- Two list sources instead of three (Apollo was blocked).
- The waterfall's built-in validation was used instead of a separate Enrichly column.
- The MX / security-gateway check (Mimecast, Proofpoint, Barracuda) was **not** done. It's required before any sending.
- The 60% pass rate is below the newer ≥70% bar (D27–28).
- The free-plan 50-row cap.

## 6. The course video (v3)
- `video/Saffron-GTM-Course.mp4`: 37.8 min, 8 chapters, 73 scenes, 228 beats, D01–D36 plus guests. Uploaded to Drive under the same name as before ("Course Summary Video") so the link didn't change.
- **Pipeline:**
  - `video/course.py` holds the content: scenes, items and narration beats.
  - `video/render3.py` renders it, in stages `stills | sheets | script | audio | clips | final`, each idempotent.
  - Audio is re-recorded only for beats whose text changed (a `.txt` sidecar per wav), and the matching clip is deleted so it rebuilds.
  - Voice: local Piper binary `video/piper/piper` + `video/voice/en_US-lessac-medium.onnx`. Python venv isn't available on this box, so use the standalone binary.
  - Narration spells out acronyms and brand names for the voice (G T M, U S, Prospio, n eight n, Hey Reach, Clay-gent, …).
  - Subtitle style: FontSize=11, MarginV=19, which keeps them in the band above the progress bar.
- **Chapters:**
  - 0:00 Introduction
  - 1:00 Foundations
  - 5:05 Strategy before tools
  - 12:19 The data layer
  - 16:54 Clay, the workbench
  - 22:19 Signals, AI and qualification
  - 26:36 Getting data in and out
  - 29:12 Sending email that lands
  - 34:35 Efficiency and your career
- **Reviewed before rendering** by a Fable 5.1 agent. The review was applied, except where it lacked context: the funnel, value→pain→proof and the 2% bounce ceiling come from the Learning Guide, and "Argon recommended" and "Helium 1 credit" were seen in Clay itself.
- **The audio has never been listened to by Claude** (it can't hear). Ask Abi or Deepu to flag any mispronunciations; a fix re-records only that beat.
- Older versions: `render.py` / `script.md` (v1/v2 summary, superseded) and `course_v3_prereview.py` (pre-review backup).

## 7. Tooling notes (this machine)
- **rclone remotes:**
  - `deepshikhagtme:` has full scope on the GTM account. Write deliverables into "GTM Cohort Catch-up" only. Use `copy`/`copyto`, never `sync`, and never delete.
  - `deepu-personal-ro:` is read-only on the personal account. To list the course folder, use `--drive-root-folder-id 1xJu8MQoRouZqeaNaBxRTyJzww5tqjRrN`.
  - Both use rclone's shared client_id, which is being retired in 2026. If they stop working, set up a private client_id.
- **rclone uploads:**
  - .docx → Google Doc: `--drive-import-formats docx`.
  - .csv/.xlsx → Sheet: add `--drive-export-formats` matching the source.
  - Each call takes a few seconds per file; use `timeout` and `run_in_background` for batches.
- **Read-only OAuth:** `rclone authorize drive <base64url, no padding, of {"scope":"drive.readonly"}> --auth-no-open-browser`. The result is a **base64 blob** (decode it, then use the `token` field), not raw JSON.
- **The Google Drive MCP connector** is signed into the personal account, and its search can't see files newly added to the shared course folder.
- **Headless Chromium:** always pass the keyring-safe flags from the global CLAUDE.md.
- **faster-whisper** runs on the GPU (GTX 1650 Ti 4 GB) with medium.en int8_float16.

## 7b. Remote access for Deepu (Abi's WSL machine): ON HOLD, see docs/remote-access-setup.md
- A separate Linux user **`deepu`** runs a **VS Code tunnel** named `saffron-gtm`, as the systemd service `code-tunnel-deepu`.
- How Deepu connects: vscode.dev or VS Code → Remote Explorer → Tunnels, signed in with her GitHub.
- She sees only `/home/deepu`, which holds her own clone at `/home/deepu/gtme-cohort`. Abi's home is 750.
- The two clones sync through GitHub: pull before work, push after.
- Set up with `sudo bash scripts/setup_remote_user.sh`, then `sudo -iu deepu code tunnel user login --provider github`, then `sudo systemctl enable --now code-tunnel-deepu`.
- It only works while the Windows PC is on and WSL is running. Claude Code in her terminal uses her own Claude login.

## 8. Open items
**Current homework (D37–D38): `homework/D37-D38_heyreach-chro-campaign.md`.** Saffron × CHRO LinkedIn campaign in HeyReach: 4 context-segment micro-campaigns, configured but not live. Also: optimise her LinkedIn profile, watch last week's recordings, and review the segmentation from the previous session.

**Remote access:** paused 5 Oct. The script is ready but nothing has been run; resume from docs/remote-access-setup.md.

**For Deepu:**
- Share Strategy Doc v2 with Yogesh; paste the TAM/SAM/SOM screenshots from Build Evidence.
- Post the LinkedIn post from her own account (check whether the bonus point expects tagging Yogesh or Stable GTM).
- **D33–34 homework: plan 10 Saffron campaigns** (3 segments × 2 personas × top signals). Claude offered to draft it; not done yet.
- 5 Loom walkthroughs (outlines are in the KT pack) and a personal Loom (D29–30).
- LinkedIn connection requests to the agencies in "All GTM" (Agencies tab).
- Work the Follow-ups tab; run the MX check before any sending.
- Before email: a lookalike sending domain, SPF/DKIM/DMARC, 3-week warm-up, opt-out P.S., plain text, tracking off, LinkedIn first (under 2,000 leads).
- Practise Clay about 2 hours a day; consider adding a company-tier column (D29–30).

**Questions for Yogesh:**
- Binary vs 1–10 account scoring.
- Clay search as a list source.
- 50 vs 100 accounts.
- Lantern exercise vs Saffron.
- 60% vs 70% qualification.
- Tracking domain (D33) vs tracking off (D35).
- "Avoid software companies" (D31) vs Saffron's ICP.

**For Abi (optional):**
- Domain purchase + Zoho, for Apollo and future sending.
- Rename the Drive video to "Saffron - GTM Course (Days 1–36)"; the link stays the same.

**Adding new classes:**
1. Get the Gemini notes (download or screenshots).
2. Write `notes/<session>.md`.
3. Update the master notes and the KT section "Latest".
4. Convert with md2docx and upload to Drive "Session Notes".
5. Optionally extend `video/course.py` and re-render.

## 9. How Abi likes to work (also in memory)
- Explain GTM concepts fully; keep tool steps terse. No hand-holding on browsers or bookmarks.
- Hands-on tool work: **one step at a time**, then wait for his screenshot. Speed comes from doing docs and logs in parallel, not from batching his instructions.
- Say which identity each tool uses. Log every small learning in the build log's "Field notes".
- Verify outputs yourself (look at frames and files) before saying something is done. For big deliverables he asked for an independent review by the most capable model first.
- Copyable text follows the global CLAUDE.md format: label, `---`, flush-left body, blank line, `---`.
