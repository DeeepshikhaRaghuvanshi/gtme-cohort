# D17-D18: Importing & structuring data + Your first enrichment (2026-09-18)

## TL;DR

- Yogesh ran a live, hands-on Clay session (mainly driving Medha's screen) covering: importing a second CSV into an existing sheet with manual column mapping, deduping, running a basic company enrichment, building an ICP contact search inside the same sheet, writing a formula to bucket job titles into seniority tiers, building a full company-domain → company-enrich → persona → email → verify pipeline, and using run conditions to save credits.
- Central lesson: real clients only give you a list of company names — you have to build the whole domain/enrichment/persona/email pipeline yourself. Prospio/Apollo-sourced data is only for practice.
- House rule repeated multiple times: always put the *cheapest, most reliable* provider first in any Clay waterfall, and delete providers you don't need (Clearbit, Smartlead were both removed in this session) to control credit spend.
- MX domain output matters for deliverability: match sending domain type (Outlook-to-Outlook, Google-to-Google) and exclude MX domains behind email-security gateways (Mimecast, Proofpoint, Barracuda Networks) that block sequencer sends.
- Weekend homework: process a list of company names end-to-end (domain → ICP check → contacts → email validation) — 10 companies per person, even though some already had a 50-company Crossview/Prospio-derived dataset.

## Key concepts

**Column mapping on CSV import.** When you already have a working sheet and need to merge in a second CSV (e.g., you built a sheet from Apollo, then need more fields from Prospio), Clay does not auto-align columns. You go to Tools → Import → Import from CSV, select the file, and on the mapping screen you manually match each source column (company name, domain, LinkedIn URL) to the corresponding column in the destination sheet, then choose "Add to table" and "Save and don't run" so the merge happens without immediately re-triggering paid enrichments.

**Dedup is a manual, explicit step, not automatic.** After merging, duplicate rows have to be removed by hand — sort/group by domain and by LinkedIn URL and delete extras. Yogesh: dedup on domain, then separately dedup on LinkedIn URL, because a duplicate can be a domain match without matching the URL field (or vice versa) if the source data is inconsistent.

**Live/webhook tables are NOT deduplicated.** Gagan asked how you dedupe live intent-signal data flowing in via webhook (e.g., same company visiting the site twice). Yogesh's answer: webhook tables are used to drive automations, and each new event is treated as fresh information on purpose — you generally do *not* dedupe them, though you can manually dedupe if you choose to. If you want deduped data, use a normal (non-webhook) table instead.

**Why you enrich data you already have.** Rithika pushed back — the sheet already had employee count/industry/etc. from Prospio, so re-running Clay enrichment on it burns credits for nothing. Yogesh's answer, which is the core mental model for the whole session: this is a training exercise. In real GTM engineering work, a client almost never hands you a Prospio-enriched dataset — they hand you a bare list of company names. You have to go find the domain, then enrich company details, then find the right people, from scratch. Practicing the full pipeline (even on data you already have) builds the muscle you need when the client only gives names.

**Find Contacts vs Find People at a Company** — two different Clay enrichments with different behavior (Rithika's question, ~01:01:07): "Find people at a company" spins up a brand-new table of results. "Find contacts [at a company]" keeps the results inside the current sheet/row as columns. For a company-centric strategic scan (do we even have the right decision-makers at these accounts?), you use Find Contacts so everything stays on one row per company.

**The 10-result cap on person search inside a sheet.** When you run "Find Contacts" filtered to a company, Clay caps returned people at 10 (in one case a company returned 7). Yogesh's framing: this isn't a limitation to fight — the filters should be kept *conservative* (senior/strict) specifically because you only want to strategically confirm "does this company have the right decision-maker present," not build a full contact list. A full contact list export is a separate, later step.

**Formulas are the control layer.** Once you have raw values (like job title strings), formulas let you derive categorical fields — e.g., turning free-text titles into a clean seniority bucket. Yogesh's framing: "GTM engineering requires you to be decent at basic mathematics/logic, because this is what a formula column is doing."

**Run conditions = the credit-saving mechanism.** Every expensive enrichment step (waterfalls especially) can be gated with a "Run only if [condition]" clause so Clay skips rows that don't need that column, instead of enriching every row and wasting credits on people/companies that don't qualify.

**MX domain / email infrastructure matching.** MX domain identifies which email workspace a target company's domain runs on (Google Workspace vs Microsoft 365/Outlook). Best practice in outbound: send from a domain/provider that matches the recipient's — Outlook-domain targets get emails from an Outlook-based sending domain, Google targets get emails from a Google-based sending domain — because same-provider delivery has measurably better deliverability than cross-provider (Outlook↔Gmail). This is an established, long-standing email-infra practice, not a Clay-specific quirk.

**Security-gateway MX tags (Mimecast/Proofpoint/Barracuda) = do-not-send list.** These are cybersecurity email-filtering layers sitting in front of a company's real mail server. Sequencers get blocked sending to them, so once you output the MX domain / workspace-detection field, you filter out (exclude from outreach) any row tagged with one of these vendors before ever loading a list into a sequencer.

## Tools shown & how they were used

**Clay — Import from CSV (merge into existing sheet).** Tools → Import → Import from CSV → select file → Continue → map each incoming column to the matching destination column (company name → company name, domain → domain, etc.) → Select all → Add to table → Save and don't run. (00:12:00–00:14:31)

**Clay — Enrich Company (basic firmographics).** Add column → Add enrichment → "Enrich Company" → remove default fields you already have (name, website) → add: employee count, industry, country location, annual revenue → Save and run for 50 rows. (00:19:12)

**Clay — Find Contacts at a Company (in-sheet ICP search).** Add column → Add enrichment → "Find contacts at a company" (NOT "Find people at a company," which spawns a new table) → filters used in the demo:
- Seniority: exact match, floor set at VP (i.e., VP and above — C-suite through VP, "don't go less than VP")
- Job function: Finance
- Job title keywords: "finance" (not "CFO" specifically, since seniority + function already narrows it; keyword should be broader, e.g. "accounting AI agents" context meant finance leads generally)
- Also available/shown: "minimum number of months since start of current role" filter
- Save and run for 50 rows. Results capped at 10 people per company. (00:21:28–00:24:55)

**Clay — Output fields from a nested search result (list indexing).** To pull a person's Name and Title out of the returned list, click into result "0" first (Clay list indexing is zero-based: 0, 1, 2, not 1, 2, 3), add Name and Title to column, then repeat for index "1" if you want a second contact. (00:26:07)

**Clay — Formula column for title bucketing.** Insert column to the right → Formula → logic dictated verbatim by Yogesh: "if title contains chief then output 'C level', and if title contains VP or vice president then output 'VP'" → Generate → Save column. This is a nested IF/CONTAINS formula, effectively:
`IF(title contains "chief", "C level", IF(title contains "VP" OR title contains "vice president", "VP", ...))`
(00:27:24–00:30:55)

**Clay — Company Domain waterfall (Search Domain / Find Company Domain enrichment).** Add column to the right of Company Name → Add enrichment → Domain → "Search domain" / Company Domain → Full configuration (not Quick setup) → reorder waterfall so the cheapest/lowest-credit provider is on top; order used: Google (top) → Company U (unclear name in transcript) → Snowview → Edge Insights → and Clearbit was explicitly deleted from the waterfall. Save and run for 10 rows (not 50, to control cost during testing). (00:32:11–00:33:27)

**Clay — AI "Find the company domain" enrichment (fallback when waterfall is wrong).** Used when the waterfall's domain output is visibly wrong (case in point: "Premier Search" waterfall returned a bad-looking domain "mariambster.com" that Yogesh doubted was correct vs. LinkedIn). Steps: Add column to the right of Company Name → Use AI → prompt text (exact wording used): "Find the company domain" → then on a new line map in "Company name" as the input variable → Generate → model selector: select Helium (top choice; "always select Helium first, if it doesn't work then move to a new model") → Save and run for 10 rows. This correctly resolved Premier Search's domain where the waterfall had failed. One other company ("Association for Medicine," per Medha) was named as still wrong even by this method. (00:34:56–00:36:23, reused later at 01:09:59 for "PhonePe/PTM" domain fixes)

**Clay — Work Email waterfall with run condition.** Add column → Add enrichment → "Work email" → Full configuration → arrange waterfall providers, cheapest-safe first → explicitly turn off/remove Smartlead ("it's expensive") → map Name, Domain, LinkedIn URL as inputs (LinkedIn URL had to be added as an extra mapped field since it wasn't already present) → Run settings → Add run condition → "Run only if Seniority level is [in] VP" (comma-separated value, exact match) → Generate → Save → Save and run 50 rows. Verified: only VP rows populated an email; non-VP rows were skipped, saving credits. (00:37:51–00:42:00ish)

**Clay — Removing the built-in waterfall verifier (best practice, demoed as a fix).** Work email column → Edit column → Full configuration → scroll to the verifier/validation section → Settings → delete/remove that validation provider → Save and don't run. Rationale given: the in-waterfall verifier is redundant once you add a dedicated external verifier (Enrichly) downstream, and keeping both wastes credits. Yogesh: "in reality [practice] you should remove it... we kept it only because we're learning right now." (00:45:10–00:47:10)

**Clay — Enrichly (external email verification tool).** Add column → Add enrichment → search "Enrichly" (spelled out E-N-R-I-C-H-L-Y in transcript; product likely "Enrichly" or possibly a homophone — treat name as best-effort (unclear in transcript)) → select "Verify email" → map input = Work email → Continue to add fields → Add run condition: "Run only if [Work] email is available" (i.e., only run the paid verification call if the email field is non-empty) → Generate → Save and run for 50 rows. (00:43:21–00:45:10)

**Clay — MX domain + result output fields.** On the Work Email waterfall column, after removing the internal verifier: click into the "catch-all valid" style status field, then output two new fields — MX domain and Result (the validation status, e.g., "valid" vs "catch-all valid"). These are the two fields used downstream for both deliverability tuning (MX/workspace matching) and list-quality triage (valid vs catch-all vs invalid). (00:47:10–00:48:33)

**Clay — full single-company pipeline test ("Razorpay" then "PhonePe"/"PTM").** Fresh blank table → one row, Company Name column → type "Razorpay" → chain: Company Domain waterfall → Enrich Company → Find Contacts (filtered: VP/Director+, Finance function) → output Name/LinkedIn URL/Title for the chosen contact → Work Email (with validation provider removed) → validate email → output MX domain + Result. Then demoed **auto-run automation**: with auto-run toggled on for the table, typing a new company name into the next empty row cell (e.g., "PhonePe," abbreviated "PTM" in the transcript) causes the entire chain of enrichments to fire automatically on that new row with no manual re-triggering. (00:56:29–01:08:57)

**Clay AI model selection note.** For any "Use AI" / Claygent-style column, always try the Helium model first before switching models — cited as both cheaper and Yogesh's default recommendation.

## Clay build steps demonstrated (reproducible order)

1. Import a second CSV into an existing sheet: Tools → Import → Import from CSV → map every incoming column to its sheet counterpart → Add to table → Save and don't run.
2. Dedupe the merged table: remove duplicate rows by domain, then separately by LinkedIn URL.
3. Run "Enrich Company" for firmographics (employee count, industry, country, annual revenue) on all rows.
4. Add "Find contacts at a company" (in-sheet variant) with a tight ICP filter: seniority floor = VP, exact seniority match, job function = target function (e.g. Finance), optional job-title keyword.
5. Pull Name + Title for result index 0 (and 1, 2… as needed) — remember Clay list indices start at 0.
6. Add a formula column that buckets Title into a seniority label (contains "chief" → "C level"; contains "VP"/"vice president" → "VP").
7. Build the Company Domain waterfall: order cheap/reliable providers first, delete unreliable/expensive ones (Clearbit removed), run on a small row sample first (10, not 50) to sanity-check.
8. Where the domain waterfall output looks wrong, add a parallel "Use AI" column prompted "Find the company domain" mapped to Company Name, model = Helium, as a corrective/alternative source — don't blindly trust the waterfall.
9. Build the Work Email waterfall: order providers, remove expensive ones (Smartlead removed), map Name/Domain/LinkedIn URL, add a Run Condition ("Run only if Seniority = VP") to skip non-target rows, remove the built-in verifier once a dedicated verifier is added downstream.
10. Add Enrichly as a separate verification step, gated by "Run only if email is available" run condition.
11. Output MX Domain and Result (validation status) fields from the email waterfall for deliverability/quality triage.
12. Optionally wire the whole chain into a single-row "type a company name → auto-run populates everything" flow, using the table's auto-run toggle.

## Instructor rules, opinions & decisions

- Real clients give you a bare list of company names — always build for that case, not for pre-enriched data. Practicing on already-enriched Prospio data is intentional training, not the target real-world workflow.
- Webhook/live-intent tables are not deduplicated by default; normal tables should be deduplicated.
- Always order waterfall providers cheapest/most-reliable first; delete providers that are expensive or unreliable (Clearbit and Smartlead were removed in this session).
- Test waterfalls on a small row count (5–10 rows) before scaling to the full 50, to control credit burn while validating quality.
- Don't blindly trust the company-domain waterfall — cross-check with an AI "Find the company domain" prompt when results look wrong, and prefer that AI method with the Helium model as the default/first-try model.
- Remove the built-in waterfall email verifier once you add a dedicated external verifier (Enrichly) — running both is redundant spend. (Left in during this session only "because we are learning.")
- Match sending-domain provider to recipient MX/workspace (Outlook→Outlook, Google→Google) for deliverability; exclude MX domains behind Mimecast, Proofpoint, or Barracuda Networks from outreach entirely — sequencers get blocked.
- Do not connect Claude directly to Clay via MCP for list extraction — Clay credits are too expensive ($190 for 2,000 credits) for that use pattern; use direct provider APIs (e.g., the verifier's own API) instead unless you're on a heavily-funded Clay plan.
- Filters on person search should stay conservative/strict — the goal at this stage is a strategic check ("do we have the decision-maker?"), not a full contact-list build; a later "select top person among candidates" enrichment step is needed for production but was deliberately skipped in this training session.
- Person enrichment output should always include full Name + LinkedIn URL + Title — LinkedIn URL specifically called out as a must-have for any person enrichment.
- Use "Find Contacts" (stays in the same sheet) rather than "Find People at a Company" (spawns a new table) when you want a company-centric, one-row-per-company view.

## Assignments / homework given

- Medha Das: finish the remaining Clay training exercise by end of day.
- Medha Das: run the full Razorpay pipeline end-to-end (domain → business details → ICP targeting → professional email → validation) as practice — done live in-session.
- Yogesh Jaiswal: will send the group a list of restricted MX domains (Mimecast, Barracuda Networks, etc.) to exclude from outreach — not delivered yet as of this session.
- Whole group (weekend portfolio task): process 10 company names end-to-end — find domain, verify ICP fit, find the right contact(s), validate email. Participants with an existing 50-company Crossview/Prospio dataset were told they could use a subset of it, but the assignment was explicitly capped at 10 companies "to prevent errors in Clay" while Yogesh finalizes exact task guidelines (to be sent before Monday).

## Deepu's questions & the answers she got

Deepshikha did not speak during this session — she was present on the invite list but the transcript shows no attributed lines from her.

## What this means for the Saffron build

- Saffron's target company list will almost certainly arrive as bare company names (or at best names + rough vertical), matching exactly the workflow trained here — plan the Clay table around "Company Name in, everything else derived."
- Build the domain waterfall with cheap providers first and a Helium-model "Find the company domain" AI column as a parallel/fallback check, since waterfall-only domain resolution was shown to be unreliable on at least two companies in this session.
- Gate the person/email enrichment steps with run conditions tied to Saffron's actual ICP signal (e.g., seniority ≥ a chosen floor, function = engineering/technical hiring, or a specific title-keyword match relevant to "how engineers use AI coding tools"), not blanket enrichment of every row.
- Add a formula column early to bucket found titles into seniority tiers (C-level / VP / Director, etc.) — this becomes a reusable scoring input later (see D23-D24 ICP scoring notes).
- Before any outreach step, output and check MX domain + validation Result, and exclude Mimecast/Proofpoint/Barracuda-protected domains from the sequencer load — get the exclusion list from Yogesh once he circulates it.
- Remove the internal waterfall verifier once Enrichly (or an equivalent) is wired in as the dedicated verification step, to avoid double-charging credits.

## Resources mentioned

Clay, Prospio, Apollo, Crossview/Crosspio (participant's existing 50-company dataset source — name inconsistent in transcript), Enrichly, Smartlead, Email Bison, Mimecast, Proofpoint, Barracuda Networks, Clearbit, Google Workspace, Microsoft Outlook/365, Clay-Claude MCP integration (mentioned and advised against), Helium (Clay AI model).
