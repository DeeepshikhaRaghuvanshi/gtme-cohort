# GTM Engineering Cohort: Master Notes (D01–D26 + guest sessions)

For Deepu · compiled 27 Sep 2026 from the Gemini transcripts of all 13 cohort sessions, 2 guest sessions, 2 instructor reference docs and 2 locally transcribed videos. Each session has a detailed file in this folder (`D01-D02_…md` etc.). This page is the map; the session files are the territory.

---

## 1. The one-minute picture

- **Program:** Stable GTM's GTM Engineering cohort, taught by Yogesh Jaiswal, 12 weeks, following the day-by-day "Learning Guide". Live classes run ~08:55 IST and cover two guide-days per session (D01+D02, D03+D04 …).
- **Where the cohort is now:** D25–D26 (24 Sep). Weeks 1–2 were strategy (ICP, TAM/SAM/SOM, signals, messaging). Week 3 was data sourcing (Apollo, Prospeo, Sales Nav, data quality). Weeks 4–5 were Clay (import, enrichment, formulas, waterfalls, run conditions, lookups, Claygent). Next up: signals at scale, then orchestration (n8n/Make), execution (Instantly/HeyReach), CRM, and AI agents / Claude Code.
- **Your portfolio company:** Saffron (YC S26; AI-native technical hiring assessments). Every deliverable targets Saffron.
- **What Yogesh says a credible portfolio needs** (D21–D22): strategy doc + Clay table + data pushed to a sequencer (HeyReach/Instantly) + a Claude Code integration + a Make/n8n automation + **5 Loom walkthroughs**.

## 2. The seven layers (the spine of the course)

| Layer | Job | Tools named in class | Characteristic failure |
|---|---|---|---|
| L1 Data & Sourcing | Find the right companies and people | Apollo, Prospeo, Sales Navigator, Ocean.io, ZoomInfo, PDL | Wrong companies → "precise garbage" downstream |
| L2 Enrichment | Name → verified email, firmographics, tech stack | Clay (waterfalls), Enrichly, MillionVerifier, Bounceban, HG Insights, Sumble | Guessed emails → bounces → burned domain |
| L3 Signals & Intent | The "why now" | Clay signals, Claygent, RB2B (US only), job boards, Crunchbase | Stale or false signals ("congrats on the funding" that belonged to a subsidiary) |
| L4 Orchestration | Move data between tools | n8n, Make, webhooks, Clay live tables, Supabase | A webhook silently fails |
| L5 Execution | Outreach | Instantly, Smartlead, HeyReach, Buffer (LinkedIn posting), Trigify | Unwarmed domains / generic copy |
| L6 CRM & Reporting | Source of truth | HubSpot, Salesforce, Attio | Duplicate swamp → routing lies |
| L7 AI & Agents | The multiplier | Claude, Claude Code, Claygent, MCP, DeepLine | Confident nonsense at scale |

Core idea: **value is created inside layers and destroyed at the handoffs between them.**

## 3. The workflow as Yogesh teaches it (end to end)

1. **Strategy doc first, tools second** (D05–D10): company snapshot, founders, problem, pricing, ICP (decision makers + champions), TAM/SAM/SOM **with filter screenshots**, 3–5 checkable signals/intents, exclusion list, messaging. Interrogate the client before building (D09–D10).
2. **Decide the list type** (D11–D12): *why* are we building it (outbound / event / webinar), fresh or repeat, **People-first vs Company-first**.
3. **Source from ≥3 providers** (Apollo, Prospeo, Sales Nav) → combine and **dedupe with the cascade LinkedIn URL → email → full name + company** (D11–D12, D23–D24). For an account list keep only **Company Name, Domain, Company LinkedIn URL** (D15–D16).
4. **Clay** (D15–D26): import → dedupe → enrich company → signals → binary qualification (Outreach / Don't outreach, with the reason) → blacklist/exclusion lookup → find people → email waterfall (cheapest first) → external verification → only Valid + Valid-catch-all, no Mimecast/Proofpoint/Barracuda MX.
5. **Deliver** a clean client delivery sheet, QA'd with Sculptor in *Analyze* mode.
6. Later in the course: push to the sequencer / CRM behind run conditions, automate with n8n/Make, and add Claude Code.

## 4. House rules (collected from every session)

**Clay hygiene**
- Auto-run **OFF** except on webhook/live tables. **Hide, never delete** columns: recovery costs ~50 credits or is impossible (D15–D16).
- Test on **5–10 rows** before any full run; use "run rows X–Y" to continue (D17–D20).
- Lock column names before writing run conditions; write conditions with the AI prompt builder (D21–D22).
- After editing a Claygent prompt, **regenerate the JSON schema**. Never hand-delete output fields (D25–D26).

**Credit efficiency (the bonus point)**
- Waterfalls: cheapest reliable provider first; remove expensive or unreliable ones (Clearbit and Smartlead were removed in class) and the built-in verifier once an external verifier exists (D03–D04, D17–D18).
- AI models: **Helium by default → Neon only on failure → Argon last**. GPT-mini-class models are for text editing only (D15–D16, D19–D22).
- Gate every expensive column with **"only run if"** so spend scales with lead quality, not list size (REF conditional-logic doc).
- Formulas are free: use them for anything deterministic. Use Lookups for joins and counts, never AI (D19–D20, D23–D24).
- Prefer Claude over Clay where Claude does the job just as well (~$20/month vs $120–190+/month) (D23–D24). Don't wire Claude to Clay via MCP for extraction; it's too credit-expensive (D17–D18).

**Data quality**
- Never trust one provider or one verifier (D01–D02, D13–D14). Expect only ~60% of an exported list to survive cleaning (D13–D14).
- Email statuses: Valid, Invalid, Valid catch-all (safe), Catch-all only (don't send) (D21–D22).
- Exclude MX behind Mimecast/Proofpoint/Barracuda; match sender type to the recipient's MX (Google→Google, Outlook→Outlook) (D13–D14, D17–D18).
- Flag false profiles where the LinkedIn company doesn't match the email domain (D11–D12).
- Job-title search: **"similar to", never "contains"** (up to ~60% more coverage); separate title keywords from seniority; always add exclude keywords (D05–D06, D23–D24).
- People quality gates: ≥100 connections/followers, ≥6–12 months in role (D23–D24).

**Qualification and messaging**
- Account scoring is **binary**; 1–10 scores are only for people (D19–D20).
- A healthy qualifier passes ~**60–70%** of a list. At 20–30% your rules are too strict (D23–D24).
- Qualification signals are often enough; don't stack disqualifiers in a small TAM (D25–D26).
- Use **day counts** ("last 180 days"), never months, in AI prompts (D19–D20).
- Use signals as *context*, never recite them ("we saw you raised…"). Verify a signal is true before using it (D15–D16).
- Blacklist = permanent (competitors). Exclusion list = temporary (current clients, open deals) (D05–D06, D23–D24).
- Cold email reply rates sit around 2%, so signal-based, warm and multi-channel (LinkedIn) wins. Never promise open or reply rates (D09–D10, D19–D20). Benchmarks you can quote in interviews: LinkedIn 70% accept / 30% reply; email 90%+ open / 3–5% reply (D21–D22).

## 5. Session digest

- **D01–D02 · What is GTM engineering + the revenue funnel.** Outcome-driven systems linking engineering to revenue; today ~90% outbound. Data is ~80% of the job, so always waterfall 3+ sources. Funnel buckets: disqualified / nurture / sell. Career tip: target agencies (especially European ones) first.
- **D03–D04 · Seven-layer model + workspace.** A tool per layer; order waterfalls by credit cost; email infrastructure (SPF/DKIM/DMARC) is 80% of email success. Homework: separate Chrome profile + dedicated gmail, sign up for ~30 tools, pick a YC company.
- **D05–D06 · Adopt a company + ICP.** The strategy-doc structure; titles vs seniority; exclude keywords; segmentation by function (one real client ran ~400 campaigns); exclusion lists; precise city/state/country columns.
- **D07–D08 · TAM/SAM/SOM + signals.** Live Apollo sizing on "Below AI": TAM 151k → SAM 54k → ICP 184 people. **Screenshots are mandatory.** SOM is a written market-conditions argument, not a filter. Signal (account, public) vs Intent (person, behavioral) vs Trigger (your action).
- **D09–D10 · Offer & message-market fit + strategy brief.** The GTM engineer operationalizes the strategy; interrogate the client first; build a Claude Project knowledge base; LinkedIn beats email for differentiation; pick unsaturated niches.
- **D11–D12 · Data landscape + Apollo.** Why/fresh-vs-repeat/people-vs-company questions; Sales Nav is required for people-first lists (Apollo/Prospeo locations lag ~30 days); dedupe cascade; false-profile QA; Clay is orchestration, not a data source.
- **D13–D14 · Sales Nav + data quality.** No API, ~1–2k export cap, good at non-.com domains. The two pillars are a verified LinkedIn URL and a verified email; the Mimecast rule; the ~60% survival rate; store clean data in Supabase. Homework: 50 accounts (name, domain, LinkedIn).
- **D15–D16 · 50-account list + Clay orientation.** Account = company, not people. Auto-run off; hide, don't delete. Don't source companies from Clay's own data. Prompter → JSON schema; trust only green-confidence AI outputs. Use signals as context.
- **D17–D18 · Import + first enrichment.** A real client gives you only company names, so build domain → enrich → persona → email → verify yourself. Cheapest-first waterfalls; Enrichly behind "only run if email exists"; MX exclusions.
- **D19–D20 · Formulas + enriched list.** Add "tech companies" to domain prompts; run row ranges; warm-network search via past employers/schools; free formulas (first name, title buckets); **binary account scoring**; day counts in prompts.
- **D21–D22 · Waterfalls + run-only-if.** Full Goji Berry pipeline: SDR headcount → HG Insights tech stack → people → email → verify. Run-condition operators and use cases; the Helium → Neon → Argon ladder; email statuses; a second Claygent column to validate the first in narrow markets; the portfolio checklist.
- **D23–D24 · Lookups & dedupe** (title says ICP scoring, but scoring was D19–D20). Blacklist vs exclusion via Lookup "has no results"; dedupe in Claude; "similar to" > "contains"; language, network and tenure filters; Sculptor (Analyze mode only); live tables.
- **D25–D26 · Scored pipeline + Claygent.** Lantern AI table (Germany/Netherlands software companies, 51–500 employees): qualify on jobs open >30 days (or ≥10 postings) + has an HR/recruiting team. Funding is a weak signal; companies with no TA team are disqualified; regenerate schemas; cross-check Claygent verdicts with formulas.
- **Guest · Rejoice (15 Aug).** Revenue engineers vs tool operators; skill order is fundamentals → systems thinking → technical fluency → tools → communication; her best Clay build had one enrichment; build a project, record a Loom, DM the founder; learn in public.
- **Guest · Kushagra (29 Aug).** The role is shifting toward coding agents calling APIs directly, while Clay stays for data access. Don't dump thousands of rows into an agent's context; use resumable, streaming scripts. Proof of work and "value bombing" beat courses. Blue-collar niches are easy wins early.
- **Bonus videos:** the Sales Navigator walkthrough and Instantly training, transcribed locally (`source/X2_…`, `source/X3_…`).

### D29–D36 (29 Sep – 2 Oct): from tables to sending
- **D29–30 · Intelligence tables:** separate company and people tables, mandatory keys, company tiering → persona mapping, write data out to Sheets or a CRM (upsert), plan the logic in Claude first.
- **D31–32 · Deliverability:** infrastructure and data cause most failures; never use the main domain; SPF/DKIM/DMARC; 3-week warm-up; simple placeholders; opt-out P.S.
- **D33–34 · Mailbox maths and warm-up:** leads × steps → mailboxes; under ~2,000 leads lead with LinkedIn; behavioural subsequences; plain text; multi-channel. Homework: 10 campaigns.
- **D35–36 · Cold email frameworks:** 6-email sequence with an options close, A/B tests, micro-campaigns, tracking off.
(Written from Gemini summaries; see D29-D36_summary-notes.md.)

### D37–D38 (5 Oct): personalization beyond {first_name}
- Micro-campaigns over mass AI personalization. HeyReach for LinkedIn automation: 25 connection requests and 40 messages a day; ~750 a month split into 4 campaigns. Optimise the profile and post thought leadership first; LinkedIn ~30% replies vs 1–4% for email. Segment by context (events), not seniority. Results show in ~1 month; getting it right takes 2–3 months. Trigify was acquired by HubSpot.
- Homework: a Saffron × CHRO campaign in HeyReach, configured but not live. See `homework/D37-D38_heyreach-chro-campaign.md` and `notes/D37-D38_personalization-micro-campaigns-heyreach.md`.

## 6. Glossary

- **ICP / persona:** the ideal company vs the ideal person inside it. Decision maker = signs; champion = pushes internally.
- **TAM / SAM / SOM:** everyone who could buy / who you can serve / what you'll realistically win now, and why.
- **Signal / intent / trigger:** a public account-level fact / a person-level engagement with you / the action you take in response.
- **Waterfall:** try provider A, and if it comes back empty try B, then C… Order by cost and reliability.
- **Run condition / "only run if":** a per-row gate so an enrichment fires only when a condition is true.
- **Catch-all:** a domain that accepts any address. "Valid catch-all" = verified safe; "catch-all only" = unverifiable, don't send.
- **MX filtering:** checking the recipient's mail server and excluding security gateways that block sequencers.
- **Blacklist vs exclusion list:** permanent vs temporary do-not-contact lists.
- **Lookup:** a join from one Clay table to another (single record or multiple rows).
- **Claygent / Helium / Neon / Argon:** Clay's web-research agent and its model tiers, from cheapest to most thorough.
- **Sculptor:** Clay's table-aware AI assistant. Keep it in Analyze mode.
- **Live table:** an API/webhook-fed Clay table that runs headless.
- **SPF / DKIM / DMARC:** DNS records that prove an email really comes from your domain (sender list, cryptographic signature, policy for failures).
- **Warm-up:** gradually raising a new mailbox's daily sending volume (about 10 → 30 a day over ~3 weeks) so mail providers learn to trust it.
- **Upsert:** write to a CRM by updating the record if it exists, otherwise inserting it.
- **Data credits vs actions:** Clay's two meters. Credits are charged per attempt, not per success.

## 7. Assignment tracker for Deepu

| Session | Assignment | Status |
|---|---|---|
| D01–D04 | Dedicated gmail + Chrome workspace | ✅ deepshikhagtme |
| D01–D04 | Sign up for tools; bookmarks bar | ◐ Apollo blocked (needs work email) |
| D01 | LinkedIn-connect with the agency list (no messages) | ☐ Deepu |
| D05 | Pick a company | ✅ Saffron |
| D05–D10 | Strategy doc (ICP, segments, TAM/SAM/SOM + screenshots, signals, messaging) → share with Yogesh | ◐ v2 drafted; screenshots + share pending |
| D11–D16 | 50-account list from ≥3 providers, deduped, 3 columns | ☐ in progress |
| D16–D18 | Clay: import, enrich, domains, people, emails, verify | ☐ build sheet ready |
| D19–D20 | Formulas, binary account scoring, signal list | ☐ in build sheet |
| D21–D22 | Waterfall + run conditions; portfolio (strategy + table + campaign + 5 Looms); add contacts to LinkedIn | ☐ |
| D23–D24 | Client delivery sheet for 50 companies | ☐ in build sheet |
| D25–D26 | Qualification table (group exercise: Lantern) | ☐ applied to Saffron |

## 8. Things to clarify with Yogesh

- Account scoring: D07–D08 describes a 1–10 account score, but D19–D20 says account scoring must be binary. Current guidance appears to be binary.
- Sourcing: D15–D16 says don't source companies from Clay's own data, while D25–D26 built the Lantern list with Clay "Find companies". Is Clay search acceptable for territory builds?
- The Learning Guide says ~100 accounts on D15; class says 50. Confirm 50.
- Is the Lantern exercise expected from everyone, or is applying the same pattern to your own company (Saffron) acceptable?
