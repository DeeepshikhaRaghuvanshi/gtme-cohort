# D19-D20: Clay formulas basics + Ship an enriched list (2026-09-21)

## TL;DR

- Two big topics: (1) fixing AI domain-lookup prompts (specify "tech companies" to disambiguate generic names) and running enrichments on a specific row range instead of all-or-nothing; (2) using Clay's "Find People" filters on past-experience/education to build warm-network outreach lists, then using formula columns (free, no credits) for name-splitting, title-cleaning, and account-level signal scoring.
- Core reframe: GTM engineering in 2026 is mostly about qualifying accounts on 3–5 signals and pushing qualified companies to sales/CRM, not blasting cold emails (2% reply rate cited as the reason cold email is basically dead).
- Account-level scoring should be binary (outreach / don't outreach), not a 1–10 scale — 1–10 scoring is reserved for scoring individual people (lead scoring), covered later.
- AI prompts with calendar/month-based timeframes ("last 6 months") return stale/wrong data; day-count timeframes ("last 180 days," "last 365 days") work reliably — a concrete, transferable prompting rule.
- Formulas are free in Clay and should replace paid AI/enrichment calls wherever the logic is deterministic (splitting names, title bucketing, cleaning LinkedIn URLs, shortening company names) — framed as a real professional differentiator (companies burn 8–10 hours/week on this kind of data cleaning).

## Key concepts

**Prompt engineering for ambiguous company names.** Khushboo's AI-based domain lookup ("Helium" model, run twice) returned two different wrong domains for a company called "Cast" (once "castscience," once "castconsultancy") instead of the correct castsoftware.com. Yogesh's diagnosis: short/generic company names (his example: "Cast" could just as easily be an interior design firm in Delhi) confuse the AI because it has no industry context. Fix: explicitly state the target's industry/category inside the prompt — e.g., add a line noting "these are tech companies" — so the model's search is scoped correctly. He frames this as a durable limitation: "you can never be perfect here in domains," so plan for a correction pass, don't expect one-shot accuracy.

**Running enrichment on a specific row range (not all-or-nothing).** After testing on the first 10 rows, you don't have to choose between "10" and "50" again — you can run a column starting at an arbitrary row. Steps: open the enrichment column → click "Run column" → choose "number of rows to run" → set starting row (e.g., row 11) → set count (e.g., 2, or however many remain) → Create enrichment. This lets you incrementally enrich rows 11–50 after validating rows 1–10, without re-spending credits on already-enriched rows.

**Find Contacts vs Find People (revisited/clarified).** "Find contacts at a company" is used to check for the *presence* of a role (a qualification/strategic check — "does this account even have a CTO?"). "Find people" is the enrichment you use when your actual goal is to *locate specific individuals* to build a contact/outreach list. Whether to search for VP-only or also Chief-level titles depends entirely on the actual ICP of the business being served — there's no universal rule; Yogesh: "if you need chief you need to find chief also."

**Warm-network outreach — the core GTM strategy taught this session.** Because outbound to a completely unknown company/founder is "very risky" (you don't know how the market will respond, and email reply rates are ~2%), the first outreach wave should always target people already connected to the founder through two channels: (1) shared education (same university/college, regardless of graduation year — "even if you graduated today and someone else 10 years ago, it's the same alumni network"), and (2) shared past employment (people who worked at the founder's previous companies — typically the last 3–4 companies). The pitch for these first-wave emails explicitly references the shared connection ("we both studied at X," "I saw you worked at Y where our founder also worked") — this is what makes it warm rather than cold. Investors are a third warm-network channel mentioned in passing (reach out to other portfolio companies of the same investor).

**Building the warm-network list in Clay (via "Find People", company-level filters).** In the Company table view, enable/open the "Past Experience" filter panel. Two usable sub-filters:
- Education: "school name contains [University Name]" (demo used "Bits Pilani," typed in caps as "BITS PILANI") combined with Job title "contains founder" → returned 469 people.
- Past experience: "Company name contains [Company]" with the "past" toggle (so it matches people who USED to work there, not current employees) — demo used "Pixis.ai" (Gagan's company) → 1,171 people who previously worked there, then added Job Title "founder" → narrowed to 116 founders who are Pixis alumni.
Filters can be stacked/broadened: add a second past-employer (e.g., Microsoft, HubSpot) to widen the pool (jumped to 17,000 — Yogesh called this too broad and narrowed back down by adding a geography filter, e.g., "United States" or an Indian-companies filter, landing around 188–532 depending on combination). Adding seniority (founder / C-suite) and company size (100+ employees) filters further refines the list (~257 in one filtered pass in the demo). Yogesh's summary framing: across college + 3–4 past employers, a founder can typically surface roughly ~2,000 warm-network people to start outreach with, rather than going in cold.

**Formula columns output exactly one column.** Gagan initially assumed a formula could split "Full Name" into two output columns (First/Last). Yogesh corrected this: a Clay formula column always outputs a single value/column. So to get a first name, you prompt the formula for one output only — worded to explicitly constrain format: "from full name, output single-word first name, first letter capital" — and stop there (don't ask it to also strip suffixes/initials unless separately instructed, e.g. "Jonathan K" should not retain the trailing "K"; add an explicit rule like "don't add any prefix or any signs in between" to handle multi-part or transliterated names, e.g. a Chinese name with a middle prefix).

**Building an account-level (company) signal/scoring workflow.** For Gagan's own company (an AI security tool for DevOps/code-push/database pipelines, ICP = Director of DevOps, Director of Engineering, VP/CTO/Chief of Engineering, Director of Security), the class built 3 signal-detection enrichments using "Use AI" (Helium model) against the company GTM doc's signal list:
1. Company adopts AI coding tools (Claude Code / Codex) — detected via job postings/technographic signals (a "detection source" like GitHub activity or job post language), output fields "tool one," "tool two," "tools mentioned" (indices 0 and 1).
2. Company recently achieved/invested in SOC 2 compliance — worded as a check, e.g. "Check if the company is [newly] SOC 2 compliant."
3. Originally "hiring first security engineer" / "security incident disclosure" — dropped because companies essentially never publicly disclose security incidents, so that signal can never populate reliably (Yogesh: "this will never work properly because the company will not disclose what happened"). Replaced with a "recent funding" signal instead.

**Timeframe phrasing rule (important, transferable).** Gagan found that specifying a **calendar-based** window in an AI prompt (e.g., "raised funding in the last 6 months") unreliably pulled stale data (one result was from 2020, ~6 years old, despite the model returning "false" for the actual condition) — the model doesn't consistently reason about relative months correctly. Switching the same logic to a **day-count** window (e.g., "last 180 days" or "last 365 days") worked reliably. Also: don't specify a funding round type (e.g., "Series A") in the prompt, or the model will incorrectly narrow to only that round type in the lookback window. For anything AI keeps getting wrong on funding specifically, Yogesh recommends falling back to Crunchbase data instead of AI-only detection.

**Model choice for research-style AI columns.** Gagan asked why not use "GPT-4 mini" for a one-off task instead of Helium. Yogesh: GPT-4 mini is for text editing, not research — it's not good at open-ended research/lookup tasks — stick with Helium for anything requiring the model to search/reason over data.

**Formula for combining/deriving the final scoring column.** After the three signal columns exist (tool adoption true/false, SOC2 compliant true/false, recent funding true/false), a formula column combines them: check if Tool 1 = "Claude Code" and Tool 2 = "Codex" (cleaning True/False and removing stray dashes from raw AI output first), AND SOC2-compliant = true, AND has-recent-funding = true → THEN output "Outreach", ELSE output "Don't outreach". This produces a binary eligibility column. Filtering that column to "Outreach" isolates the exact accounts to pursue — described explicitly as "this is your SOM [Serviceable Obtainable Market]" in this exercise (out of the pool tested, 2 companies passed all filters).

**Binary account scoring vs. 1–10 lead scoring.** Company/account-level scoring should be binary (Outreach / Don't outreach) because there typically isn't enough distinguishing data per account to justify a granular numeric score, and it keeps the qualification decision unambiguous and trackable. A 1–10 scale is reserved for scoring individual *people* (leads) later in the program, where much richer per-person data exists (valid email present, right geography, right past employer, etc.).

**"90% of daily Clay usage" claim.** Yogesh states that qualifying companies and identifying/searching ICP contacts inside those qualified companies constitutes about 90% of what a GTM engineer actually does in Clay day to day — everything else in the tool is comparatively minor.

**GTM engineer's actual deliverable, in many real engagements.** Once qualified companies + contacts are found, in many setups you don't personally send outreach at all — your job is to push the qualified account list into the client's CRM for their own sales team to work (example given: Razorpay's ~200 salespeople selling into the US; the GTM engineer's job is only to surface and qualify the right accounts, not to email them).

**Signal-list strategy discipline.** Any GTM strategy document should define at least 3–5 concrete signals, and the qualification logic must clearly state what makes an account qualify vs. disqualify, and by which specific parameters. Yogesh flags this as the step "8 out of 10 people get wrong" — either running too many/irrelevant enrichments, too few, or outputting vague/unstructured fields instead of clean booleans. Practical shortcut: use free Claude (chat, not API) to draft the actual Clay prompt text for a signal, given your ICP/signal description — "Claude will give you a very good clay prompt."

**Scope of formulas (explicitly enumerated by Yogesh).** Formulas can, at zero credit cost: split a full name into first/last; count/filter how many people are in a given location (e.g., India); bucket seniority from job titles (C-level, VP, etc. — same logic as D17-D18); strip honorific/title prefixes (Professor, Mr., Mrs.) from names; fix malformed/inconsistent LinkedIn URLs (variants like www.lin.com/in/x vs linkedin.com/in/x from different data providers); shorten long company or institution names for natural-sounding personalization (e.g., "Tata Institute of Social Sciences" → "TISS"; "Boston Consulting Group" → "BCG"); strip corporate-entity suffixes (LLC, Co., Alphabet-style parent naming). Mastering enrichments + formulas together is presented as sufficient to avoid needing most other Clay features.

**Built-in "Normalized Company Name" is a formula too, but a shallow one.** It strips domain suffixes (.com/.in/.co) and fixes casing/capitalization, but does not intelligently shorten multi-word institution names (Yogesh's test: "Tata Institute of Social Sciences" stays unchanged under Normalized Company Name; only a custom formula collapses it to "TISS"). Yogesh frames writing your own cleaning formulas — rather than relying only on built-in normalization — as a genuine hiring differentiator, citing that companies spend 8–10 hours/week manually cleaning this kind of data.

## Tools shown & how they were used

**Clay — running an enrichment over a custom row range.** Open the enrichment column → "Run column" → select "choose number of rows to run" → set starting row (e.g., 11) and row count (e.g., 2) → Create enrichment. (00:08:30)

**Clay — Find People with Past Experience + Education filters (warm network build).** In Company table view → open Past Experience panel → Education sub-filter: "school name contains BITS PILANI" + Job title "contains founder" (469 results). Separately: Past Experience sub-filter: "Company name contains Pixis.ai" with past-experience toggle enabled (1,171 results) → add Job title "founder" (116 results) → optionally add more past employers (Microsoft, HubSpot) and geography filters (United States / India) to tune volume, plus seniority (founder/C-suite) and employee-count filters to refine further. (00:15:01–00:26:34)

**Clay — Formula column, first-name extraction.** Add column to the right of Full Name → Formula → prompt: "From full name, output single-word first name, first letter capital" (explicit no-prefix/no-extra-signs rule optional for edge cases like transliterated names) → Generate → Save column. (00:29:37–00:32:59)

**Clay — "Use AI" signal-detection columns (Helium model).** Add enrichment → Use AI → paste/adapt the GTM doc's signal wording as a yes/no question (e.g., "Check if the company adopts [Claude Code / Codex]") → map Company Domain as input → Generate → model = Helium (top) → Save and run for 10 rows first. Repeated for SOC2-compliance signal and (after dropping the unreliable security-incident signal) a recent-funding signal ("Check if the company has raised any recent funding in the last 180/365 days" — no round type specified). (00:38:57–00:52:58)

**Clay — Formula column, combined eligibility/scoring.** Add column → Formula → logic: IF Tool1 = "Claude Code" (cleaned true/false, dash removed) AND Tool2 = "Codex" AND SOC2-compliant = true AND has-recent-funding = true THEN "Outreach" ELSE "Don't outreach" → Generate → Save column → filter that column to "Outreach" to isolate the qualifying account set (SOM). (00:54:00–00:59:10)

**Clay — Find People, ICP contact search on the qualified accounts only.** On the filtered "Outreach" subset → Add → Find People → Company identifier = Website column → set ICP job titles (VP-level + role, e.g. Director/VP of Engineering or Security) → Continue → send results to a new table → Save and run (demo ran 8–10 rows). (01:00:17–01:02:10)

## Clay build steps demonstrated (reproducible order)

1. Diagnose bad AI domain lookups by checking whether the company name is generic/ambiguous; fix by adding an explicit industry qualifier ("these are tech companies") to the AI prompt rather than re-running the same prompt.
2. Use "Run column → choose number of rows → set start row + count" to enrich remaining rows (e.g., 11–50) after validating on the first batch, instead of re-running the whole column.
3. Build a warm-network candidate list: Find People → Past Experience (education contains target school; separately, company name contains target past employer, "past" toggle on) → add Job Title (founder / seniority) → stack 2–4 past employers and a geography filter to tune list size (~2,000 total across channels as a rough target).
4. Add a Formula column on Full Name to output a clean single-word capitalized First Name (used later in personalized outreach copy).
5. Pull the company's own GTM/signal doc and translate each written signal into a "Use AI" (Helium) enrichment worded as a yes/no check, mapped on Company Domain, tested on 10 rows first.
6. Prefer day-count language ("last 180/365 days") over calendar/month language ("last 6 months") in any AI prompt involving a time window; never specify a funding round type unless you want to restrict to it.
7. Drop signals that structurally cannot be detected (e.g., undisclosed security incidents) and replace with a detectable proxy (e.g., recent funding).
8. Add a Formula column that ANDs the cleaned signal booleans together and outputs a binary "Outreach"/"Don't outreach" eligibility field.
9. Filter the eligibility column to "Outreach" to isolate the qualified account set (this is effectively your SOM for that pass).
10. Run "Find People" against only the qualified accounts, using Website as the company identifier and the account's real ICP titles/seniority, output into a new table.

## Instructor rules, opinions & decisions

- Always disambiguate short/generic company names in AI domain-lookup prompts by stating the target industry explicitly; accept that domain-finding will never be 100% accurate and budget for a manual correction pass.
- Whether to search VP-only or also Chief-level contacts depends on the client's actual ICP — there is no universal rule; match the search to what the business truly sells to.
- Warm-network outreach (shared education + shared past employers, and investor networks) should always be exhausted before cold outbound — it is lower-risk and higher-response than blind cold outreach.
- Cold email reply rates (~2%) mean traditional high-volume cold email is not a viable primary channel anymore; signal-based warm outbound (or simply qualifying accounts for a client's own sales team) is the primary effective GTM-engineering deliverable today.
- Account-level (company) scoring must be binary — Outreach / Don't outreach — never a 1–10 scale; reserve numeric 1–10 scoring for individual lead/person scoring, where more granular data exists.
- A GTM strategy needs 3–5 concrete, checkable signals, and the qualification/disqualification logic must be explicit about which parameters drove each outcome — vagueness here is called out as the single most common failure mode among learners.
- Use day-count time windows, not calendar/month windows, in AI prompts that involve "recent" activity; fall back to a hard data source (Crunchbase) for funding data rather than trusting AI-only detection when AI is unreliable.
- Use GPT-4-mini-class models for text editing only, not for research/lookup tasks; default to Helium for anything requiring search/reasoning.
- Prefer formulas over paid enrichments wherever the transformation is deterministic (splitting, cleaning, shortening, bucketing) — formulas cost no Clay credits.
- Built-in "Normalized Company Name" is useful but shallow; build custom formulas for real personalization-grade name shortening — this is presented as a genuine differentiator in hiring/interviews for GTM engineering roles.
- When outputting enrichment results, be deliberate about output shape — output a clean yes/no or specific field, not "everything available."

## Assignments / homework given

- Khushboo: update her AI domain-lookup prompt to explicitly specify that target companies are tech companies.
- Gagan Bhaisa: use Crunchbase (not AI) to verify recent funding rounds going forward.
- Gagan Bhaisa: execute outbound outreach for the two companies that passed the "Outreach" eligibility filter.
- Gagan Bhaisa: build out the complete GTM signal list properly in the live table by the next day; Yogesh will review it.
- Gagan Bhaisa (via Yogesh's promised video): once received, score 50 accounts using the account-scoring methodology (Outreach/Don't outreach) shown in this session.
- Yogesh Jaiswal: will share more detail on the scope/possibilities of Clay formulas over WhatsApp.
- Yogesh Jaiswal: will send a video on lead/account scoring for further context.
- No separate weekend-style task was assigned to the rest of the group this session beyond building on the existing 10/50-company lists from D17-D18.

## Deepu's questions & the answers she got

Deepshikha did not speak during this session (present on the invite list, but no attributed transcript lines).

## What this means for the Saffron build

- Before building any domain-lookup AI column for Saffron's target companies, explicitly state the industry/category in the prompt (e.g., "these are software companies" / "these are engineering-hiring tech companies") to avoid Cast-style ambiguous-name failures.
- Consider a warm-network layer for Saffron's own outreach: search LinkedIn/Clay for people who share Saffron's founders' past employers or schools, since Saffron is an early-stage/YC company exactly in the position this warm-outreach strategy targets.
- Define Saffron's 3–5 real qualifying signals up front (e.g., "company has an active engineering-hiring pipeline," "company already trials AI coding tools," "company recently raised funding," "company posts SWE job listings mentioning Copilot/Cursor/Claude Code") and encode each as a Helium "Use AI" yes/no check, tested on a small batch before scaling.
- Any timeframe logic in Saffron's signal prompts (e.g., "recently hiring," "raised funding recently") must use day-count phrasing (180/365 days), never calendar-month phrasing, based on this session's demonstrated failure mode.
- Build a binary Outreach/Don't-outreach formula column combining Saffron's signals — this becomes the gate before running any per-contact enrichment, keeping credit spend limited to qualified accounts only (mirrors the SOM-isolation pattern shown here).
- Add formula-based name/title cleaning (first name extraction, seniority bucketing, company-name shortening) early, since these feed both personalization and the later ICP-scoring work (see D23-D24 notes).

## Resources mentioned

Clay, Crunchbase, Claude (free tier, for prompt drafting), GPT-4 mini, Helium (Clay AI model), Prospio, Pixis.ai (Gagan's company), Razorpay, Microsoft, HubSpot, BITS Pilani (as example alumni network), Boston Consulting Group / BCG, Tata Institute of Social Sciences / TISS (formula example), WhatsApp group (channel for follow-up formula resources and the promised scoring video).
