# Clay build sheet: "Saffron | Qualified Pipeline"

This rebuilds everything taught in D15–D26 on Deepu's Saffron list. Abi clicks in Clay (logged in as deepshikhagtme) and screenshots each checkpoint (📸). Each step cites the session it comes from, so Deepu can explain *why* during the KT.

## House rules (from Yogesh, apply everywhere)
- **Auto-run OFF** on this table; only webhook tables auto-run (D15–D16).
- **Hide columns, never delete** a column that has run. Exceptions: a dead signal column that returned 0 true hits on every row (D21–D22); unused *default* columns before anything has run (D25–D26).
- **Test every enrichment on 10 rows first** (Run column → rows 1–10), check the output, then run rows 11–50 (D17–D20).
- **Lock column names before writing run conditions.** Renaming later silently breaks every condition that references the column (D21–D22).
- Write run conditions with Clay's **AI/prompt run-condition builder**, not the manual builder (D21–D22).
- **AI model ladder:** default **Helium** → escalate to **Neon** only for rows that fail → **Argon** only as a last resort. Never start expensive (D21–D22; the bonus point). GPT-mini-class models are for text editing only, not research (D19–D20).
- **Deterministic work = formulas** (free), never AI credits (D19–D20). Joins and counts = Lookup, never Claygent (D23–D24).
- **Account scoring is binary: "Outreach" / "Don't outreach".** No 1–10 scores at company level (D19–D20).
- **Qualify, then filter.** Never delete disqualified rows by hand (D21–D22).
- After each run, log credits in `credit-log.md` (the numbers feed the LinkedIn post).

Before starting: 📸 the workspace credit balance (Settings → Billing/Usage).

---

## Table 1: Accounts (50 companies)

**Input:** `saffron_50_accounts.csv` (Company Name, Domain, Company LinkedIn URL), produced by `data/merge_dedupe.py` from ≥3 provider exports.

### A. Import and hygiene
1. New workbook "Saffron GTM" → New table → Import from CSV → map the 3 columns → **Save, don't run**.
2. Dedupe on Domain, then on Company LinkedIn URL (D17–D18). Expected: 50 rows, 0 dupes (the script already deduped). 📸
3. Formula **`Clean Domain`**: lowercase; strip `https://`, `www.` and any path (free; D19–D20).
4. Delete any unused default columns Clay auto-added *before* running anything (D25–D26).

### B. Firmographics (cheapest pass)
5. Enrichment **Enrich Company** on `Clean Domain` → output only: Employee Count, Industry, Country, Founded, Latest Funding Date, Latest Funding Stage. Output only what you need; don't take "everything available" (D19–D20). Rows 1–10 → check → 11–50. 📸
6. Formula **`Days Since Funding`** = today − Latest Funding Date (in days). Free. It's a tiebreaker only, because funding is a weak signal (D25–D26).

### C. Signals (from Strategy v2 → "Top 5 signals")
7. **`SWE Openings (count)`**: job-postings enrichment (LinkedIn-scraping provider, *not* Claygent) filtered to titles similar to "Software Engineer / Backend / Full Stack / ML Engineer". Fallback, **only run if** count is empty: a Use-AI column (**Helium**), prompt below. 10 rows first (D25–D26 cross-check pattern).
   > Prompt: "Visit the careers page of {{Clean Domain}}, a technology company. Count open software-engineering roles (software, backend, frontend, full-stack, ML/AI engineer) posted in the last 90 days. Return JSON: {\"swe_open_roles\": number, \"careers_url\": string}. If no careers page is found, return 0."
8. **`Has TA Team`**: Find Contacts (in-sheet, *not* "Find People", which spawns a new table; D17–D18) → Job Function = HR/Recruiting/Talent, identifier = domain → output **people count** (D25–D26). Companies with 0 are disqualified: they hire through agencies.
9. **`New Eng/Talent Leader (≤180d)`**: Find Contacts → titles similar to CTO, VP Engineering, Head of Engineering, Head of Talent, Head of Technical Recruiting; seniority VP+; output Title + Start Date → Formula: start date within the last **180 days** → true/false. Use **day counts, not months** (D19–D20).
10. **`AI Coding Tools Mentioned`**: Use AI / Claygent **Helium**, **only run if** `SWE Openings (count)` ≥ 1:
    > "Check {{Clean Domain}}'s engineering job descriptions and engineering blog. Does the company mention using or requiring AI coding tools such as Cursor, Claude Code, GitHub Copilot, Windsurf or Codex? Return JSON: {\"ai_tools_mentioned\": \"yes\"|\"no\", \"tools\": [string], \"evidence_url\": string}. Answer \"no\" if there is no explicit evidence. Do not guess."
    Click **"Generate JSON Schema from prompt"** after any prompt edit, and never delete output fields by hand (D25–D26).
    **Bonus-point experiment:** run rows 1–10 on Helium and log the credits. Only if more than 2 of 10 look wrong, re-run *only those rows* on Neon in a second column and compare. Log both.
    If this column returns "no" on all 50 rows, delete it; it's a dead signal (D21–D22).

### D. Qualification (binary)
11. Formula **`Outreach Eligibility`** (free):
    - **Disqualify** if `Has TA Team` = 0, OR Employee Count < 50, OR Employee Count > 1,000, OR Country ≠ United States (S1/S2 scope), OR `SWE Openings (count)` = 0.
    - **Qualify ("Outreach")** if not disqualified AND (`SWE Openings` ≥ 5 OR `New Eng/Talent Leader` = true OR `AI Coding Tools` = yes).
    - Otherwise → "Don't outreach".
12. Formula **`Qualification Reason`**: concatenate the parameters that drove the outcome, e.g. "✔ 12 SWE roles · ✔ TA team 3 · ✔ Cursor in JDs". Yogesh calls vague qualification the #1 learner failure (D19–D20).
13. **Sanity check:** roughly 60–70% of rows should be "Outreach". If only 20–30% pass, the logic is too strict; fix the rule rather than accepting the loss (D23–D24). 📸 the filtered view.

### E. Exclusions
14. Small table **"Saffron Blacklist"**: direct competitors (HackerRank, CodeSignal, Rounds.so, CoderPad, Karat, and Saffron itself). **Lookup Single Record** on Company → filter "has no results" (D23–D24).

---

## Table 2: People (only from "Outreach" accounts)

15. Filter Accounts to `Outreach Eligibility` = Outreach and no blacklist match → **Find People** using the domain as identifier → new table (D19–D22).
    - Titles, match mode **"similar to"** (never "contains", which loses up to 60%; D23–D24):
      - Decision maker: CTO, VP Engineering, Head of Engineering, Co-founder (≤200 employees)
      - Champion: Engineering Manager, Director of Engineering, Head of Talent, Technical Recruiting Lead
    - Quality gates: ≥100 LinkedIn connections/followers; ≥6 months in role (D23–D24). Limit 2–3 people per company.
    - Always output Full Name, Title and **LinkedIn URL** (D17–D18).
16. Formula **`First Name`**: first token of Full Name, proper-cased (free; D19–D20).
17. Formula **`Persona`**: title contains cto/vp/head of eng/founder → "Decision maker"; manager/director/talent/recruit → "Champion".
18. Missing LinkedIn URL? Use AI (Helium) "Find the LinkedIn URL" on Full Name + Title + Company, **only run if** LinkedIn URL is empty (D23–D24).
19. **Work Email waterfall**: order providers cheapest and most reliable first. Remove the expensive ones (Clearbit, Smartlead) and the built-in validator (D17–D22). Map Full Name, Domain, LinkedIn URL. **Only run if** Persona is not empty. Rows 1–10 first. 📸 the provider order.
20. **Verify** with an external verifier (Enrichly, or MillionVerifier/Bounceban if unavailable), **only run if** Work Email is not empty. Output **Result** + **MX Domain** (D17–D22).
21. Formula **`Sendable`**: Result ∈ {Valid, Valid catch-all} AND MX provider NOT in {Mimecast, Proofpoint, Barracuda} → "Yes", else "No". Catch-all-only never goes out (D17–D22).
22. **Personalization line**: Use AI (Helium), **only run if** Sendable = Yes. Uses the account's Qualification Reason + SWE count + AI tools:
    > "Write one sentence (max 25 words) for {{First Name}}, {{Title}} at {{Company}}, referencing this evidence: {{Qualification Reason}}. Tie it to how they test AI-coding fluency in engineering interviews. No flattery, no exclamation marks. Return JSON {\"line\": string}."

---

## F. Deliverable: client delivery sheet (D23–D24)
23. Export Accounts and People to CSV → dedupe in Claude with the cascade **LinkedIn URL → Email → Full Name + Company** (never name alone) (D23–D24).
24. Final sheet columns: Company, Domain, Company LinkedIn, Employee Count, SWE Openings, TA Team size, New Leader?, AI tools, Eligibility, Reason | First Name, Full Name, Title, Persona, LinkedIn URL, Work Email, Verify Result, Personalization line.
25. **Sculptor → "Analyze" mode** (never "Build") → "Which rows are missing a LinkedIn URL or a verified email, and are any qualification reasons empty?" (D23–D24). 📸
26. Upload to the deepshikhagtme Drive as "Saffron — Client Delivery Sheet (50 accounts)".

## Checkpoints Abi sends back (📸)
Credit balance before → dedupe result → Enrich Company, 10 rows → SWE openings, 10 rows → AI-tools Helium, 10 rows (+ Neon comparison) → eligibility filtered view → waterfall provider order → verify results → Sculptor analysis → credit balance after.
