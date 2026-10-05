# D21-D22: Waterfall enrichment + Conditional logic & "run only if" (2026-09-22)

## TL;DR

- Full worked example (on sampath's "Goji Berry" strategy/company list) of building a multi-signal account qualification pipeline: SDR/BDR headcount → outbound tech stack (HG Insights technographics) → (attempted, dropped) lead-gen/appointment-setting AI check → ICP contact search → work email waterfall → email verification, all chained with run conditions.
- Deep dive on Run Conditions: what they are (a "reverse formula" — enrichment fires only if the condition is true), the operator set (equals, not equals, greater/less than, AND, OR), and real use cases (CRM upload gating, lead-score gating, round-robin assignment, region routing, waterfall provider fallback).
- Deep dive on Claygent AI models: Helium (single-page lookup, default/first choice), Neon (2 credits, semi-complex/multi-page), Argon (multi-search/multi-field capture, wasteful on simple single-field lookups) — always start cheapest (Helium) and escalate only on failure.
- Email validation statuses clarified precisely: Valid, Invalid, Valid-Catch-all (receives mail, safe to send), Catch-all-only (mail is accepted/delivered but the person may never actually see it) — only send to Valid and Valid-Catch-all.
- Portfolio and career guidance: a credible GTM engineering portfolio = strategy doc + Clay table + push to Heyreach/Instantly + Claude Code + Make/n8n automation + 5 Loom videos; industry benchmarks given (LinkedIn 70% accept / 30% reply, email 90%+ open / 3–5% reply); go slow, be a lead-list-builder first, don't chase clients before mastering the skill.

## Key concepts

**"Use Clay to serve the strategy, not the other way around."** Recurring framing (00:10:03): you start from a strategy document describing what you're trying to prove/qualify, and Clay is the execution tool for that document — not something to explore feature-by-feature hoping it produces a strategy. Also: AI performs better doing per-row lookups (which is what Clay's enrichment model is built for) than being handed a whole raw list and asked to reason over all of it at once (e.g., dumping a CSV into a chat LLM and asking it to search) — this is presented as the core reason Clay-style per-row enrichment beats a single bulk LLM query for this kind of work.

**A good GTM engineer notices when default search doesn't work.** When an initial contact search (SDR/BDR by job-title-keyword) returned nothing useful, Yogesh's lesson wasn't "trust the tool" — it was that recognizing a broken/ineffective filter configuration and correcting it (switching from free-text keyword matching to structured Job Function + Seniority filters) is itself the skill being tested. "A good GTM engineer is not the one who is using things right, [but] who is able to understand if things are not working perfectly."

**Structured filters beat keyword filters for role-based headcount checks.** Rather than searching job-title keywords "SDR", "BDR" (which under-matched), the more reliable configuration was: Job Function = Sales + Business Development, Seniority = Entry level + Mid level (floor set at Entry, i.e., don't go below), Job Title Match Mode = Exact. This produced a materially different (better/more accurate) headcount result on the same company list.

**Technographic checks via HG Insights ("Verify Technology Usage").** Used to confirm a company already has certain tools in its stack (a buying-intent proxy) — demo checked for Apollo.io, Lemlist, Instantly, and Clay itself, with an install-count "limit" parameter set to 4. Output: an "installs found" nested field; you drill into it and output the actual product names into a clean column (index 0 = first product name).

**Dropping a qualification signal that returns no true results.** After running an AI check ("Check if the company is providing lead generation or appointment setting services") across the list and finding it returned false/no-signal for every single company, Yogesh's instruction was simply to delete that entire enrichment column and its filter — a signal that never fires for any row in your dataset isn't adding qualification value, so remove it rather than leave dead columns in the table.

**"Qualify then filter" is faster than "qualify then manually disqualify."** Rather than deleting/removing disqualified rows one by one, the efficient agency-style pattern is: run the qualification enrichments across the whole table, then apply column filters (e.g., "install counts is not empty") to view only the qualified subset, and build downstream steps (Find People, etc.) working from that filtered view. "This is a fast way when you work in an agency — you don't have time to qualify and disqualify [manually], so you qualify and just filter it."

**Run conditions, formally defined.** A run condition is attached inside a given enrichment column's settings (scroll down within "full configuration" to find "Run condition" / "Only run if..."). Mechanically: IF condition met → the enrichment executes (spends credits/actions); IF not met → it's skipped, saving both credits and "actions" (Clay's other billed resource). Yogesh explicitly calls this "a reverse formula" relative to a normal formula column. There are two ways to write a run condition: a manual field-by-field UI builder, or an AI/prompt-based builder ("write the condition in plain English, Clay's AI turns it into the rule") — Yogesh's strong recommendation is to always use the AI method: the manual method is "very difficult unless you put in at least 6-7 months learning Clay."

**Run condition operator set.** Equals, Not equals, Greater than / Less than, AND (multiple conditions must all be true, e.g., company size = 500 AND industry = X), OR (any one condition true, e.g., title = Founder OR title = CEO), plus "is empty" / "is not empty" checks (the exact pattern used for "only run if work email is not empty"). Conditions can be layered (e.g., status != closed) and reversed.

**Concrete run-condition use cases enumerated by Yogesh.**
- Industry filter — e.g., only enrich/act on SaaS companies.
- Status exclusion — e.g., skip records where status = closed.
- Lead/account score gating — e.g., only push to outreach tooling if score > 80.
- CRM upload gating — e.g., only push a lead to HubSpot/Zoho/Salesforce if the email field is populated, specifically to avoid handing a client false/incomplete information (an explicit trust/quality point: "when a company gets you as a GTM engineer, they don't want false information").
- Sequencer upload gating — e.g., only push to Heyreach/Instantly if lead score ≥ 80 AND industry matches.
- Region routing — e.g., only route to a specific table/rep set if region = North America.
- Round-robin lead assignment — Clay itself can do round-robin rep assignment (e.g., alternating an "assignment rep" field) without a separate round-robin tool; framed as a case where Clay increasingly replaces dedicated sales-ops tooling.
- Waterfall provider fallback — the waterfall mechanism itself is literally a chain of run conditions ("if email is empty, try the next provider") — Yogesh: "the Clay waterfall is also a run condition and a formula mixture."
- Web search gating — only trigger a Claygent web search when certain upstream conditions are met, to avoid wasting a research-grade AI call on rows that don't need it.
- Advanced/compound conditions — combining unrelated signal columns, e.g., "hiring an engineer" AND "tech stack includes AWS" (two separately-sourced columns combined in one run condition); also a very commonly reused pattern: "title = Founder OR title = CEO" AND "NOT industry = nonprofit" (nonprofits are excluded because "they will not buy").

**Run-condition troubleshooting rule ("cheat code").** Only rely on run conditions once the Clay table's column structure is finalized — because a run condition references a column by name, renaming a referenced column (even a trivial case change, e.g. "Industry" → "industry") silently breaks every run condition depending on it and can corrupt the whole table's logic. Lock your column names before layering run conditions on top.

**Claygent (Clay's built-in AI/web-search agent) model tiers, with explicit strengths/limits.**
- **Helium** — for single-page lookups. Struggles with multi-page navigation, ambiguous content, multi-step reasoning. This is the default/first-try model for almost everything.
- **Neon** — costs 2 credits, handles semi-complex tasks that require visiting multiple pages or pulling multiple fields off one page (e.g., go to a contact page and extract phone + email + more). Struggles with deep research.
- **Argon** — built for multiple searches and multi-field information capture across a broader research task. Using Argon for a simple single-field lookup "will kill" (waste) credits — it's overkill for anything Helium could handle.
- General guidance: never start with Neon or Argon. Try Helium first; escalate only if Helium fails. Claygent needs no separate API key — it's a self-contained web-search agent that follows instructions and navigates pages on its own. (GPT-class "advanced reasoning" models were mentioned as an alternative broader category, with Gemini flagged as a plausible future substitute for Claygent, but "there's no [current] replacement" in practice.)

**Claygent workflow best practices (cost control + accuracy).**
- Never run a Claygent prompt across a full table on the first try — test on 5–10 rows first.
- Default to Helium; only escalate to Neon/Argon if Helium demonstrably fails.
- Combine with run conditions so Claygent only fires on already-qualified rows (don't waste an AI web-search call on rows you'll discard anyway).
- The prompt-writing tool inside Clay (used to help you phrase a Claygent instruction) is called the "meta prompter."
- For any workflow where accuracy really matters and the addressable market is small (e.g., "we only sell to the ~100–200 good banks in India" — you can't afford to mis-qualify), run **two** separate Claygent columns: one to fetch the information, a second to independently judge/validate that the first one's answer looks correct — i.e., a dedicated "judgment" or debugging column rather than trying to make one prompt both fetch and self-validate. This is the recommended pattern for narrow/high-stakes target markets.
- Agencies typically buy Clay's Pro-tier plan with ~100,000 credits, which removes day-to-day credit anxiety — but a learner/freelancer without that scale still needs to be disciplined.

**Email validation statuses — precise definitions (important, often confused).** Four states: Valid (a genuinely valid, deliverable mailbox), Invalid (not deliverable), Valid Catch-all (the mailbox is receiving and can be safely emailed — "that person is receiving emails but not replying," i.e., it's real and reachable), and Catch-all-only / "only catch-all" (the mail server accepts anything addressed to that domain without verifying the specific mailbox exists — "the email is just delivered, he's not even receiving it"). Practical rule: build your outreach list from Valid + Valid-Catch-all only; never build a list purely from catch-all-only addresses.

## Tools shown & how they were used

**Clay — SDR/BDR headcount qualification (first attempt, keyword-based — shown to under-perform).** Add column → Add enrichment → "Find contacts at a company" → save results in this table → Job Title keywords: "SDR", "sales development representative", "BDR", "business development representative" → Save and run 10 rows. (00:13:40–00:16:17)

**Clay — SDR/BDR headcount qualification (corrected, structured-filter version).** Edit the same column → Job Functions = Sales + Business Development (clear the keyword filters) → Seniority levels = Entry + Mid, floor set to Entry (don't go lower) → Job Title Match Mode = Exact → Save and run for 50 rows. Result differed materially from the keyword version and was treated as the trustworthy one. (00:17:15–00:19:35)

**Clay — HG Insights technographics.** Add column → Add enrichment → search "Technographics" or "HG Insights" → "Verify Technology Usage" → select target tools: Apollo.io, Lemlist, Instantly, Clay → set installs limit = 4 → Continue to add fields → Save and run (first attempted on 10 rows, then run for all since the first pass showed nothing) → drill into "installs found" nested result → output the first product-name field to a clean column. (00:19:35–00:23:16)

**Clay — AI qualification check, later deleted (Use AI / Helium).** Add enrichment → Use AI → prompt: "Check if the company is providing lead generation or appointment setting services or not" → map Company Name + Website (remove auto-inserted mapping tokens and re-add cleanly if the mapping UI misbehaves) → model defaulted to Neon, manually changed to Helium → Generate → Save and run 50 rows. Result: zero true hits across the whole list → column (and its downstream filter) deleted as a dead signal. (00:24:46–00:29:20)

**Clay — filtering to the qualified subset.** On the technographics "install counts" column → Filter → "is not empty" → view narrows to companies that both (a) have SDR/BDR headcount and (b) use an outbound tool in-stack — this filtered view becomes the base for the next step (Find People) rather than manually deleting disqualified rows. (00:27:48–00:30:22)

**Clay — Find People (ICP contact search on the qualified subset).** Add → Find People (not "Add rows" — explicitly flagged as an easy, costly misclick to avoid) → Company Identifier = Company Domain column (must be mapped from an existing column; free-text input can't be used here) → Job Title filter = "sales," match mode "contains" → Seniority = Founder, CEO, C-suite, VP, Director → Confirm filter → Continue → Save results to a new table → Save and run (demo ran 9 rows). (00:30:22–00:33:54)

**Clay — Work Email waterfall (on the new ICP contacts table).** Add column → Add enrichment → Work Email (a suggested/popular enrichment, no need to search) → verify auto-mapping of Company Name/Org → Full configuration → drag lowest-cost providers to the top of the waterfall order → remove the built-in validation provider (Settings → remove provider) → Save and run 9 rows. (00:33:54–00:38:24)

**Clay — Enrichly email verification with a run condition.** Add column → Add enrichment → search "Enrichly" → Verify Email → scroll to Run Condition section → "Only run if [Work Email output] is not empty" (built via the AI/prompt method, i.e., typed as plain English and generated rather than manually configured field-by-field) → Continue to add fields → Save and run. Then: click into the validate/catch-all result → output MX Domain and Result (Result carries the human-readable status; the raw "valid" output field is just a checkbox/tick and isn't useful standalone). (00:38:24–00:43:34)

## Clay build steps demonstrated (reproducible order)

1. Start from the strategy document's defined signal (here: "target companies must have an SDR/BDR team") and translate it into a Find-Contacts-at-a-Company enrichment using structured Job Function + Seniority filters (not free-text keyword search).
2. Add a technographics check (HG Insights "Verify Technology Usage") for the specific outbound tools relevant to your ICP; output the actual product names, not just a count.
3. Prototype any additional AI qualification signal on the full list; if it returns zero true hits across every row, delete the column and its filter rather than keeping a dead signal.
4. Filter the qualified-signal column(s) to "is not empty" (or the relevant true condition) to produce a working subset — don't manually delete disqualified rows.
5. Run "Find People" against the filtered subset only, using the company's domain/website column as the identifier and the real buyer-persona job titles/seniorities from the strategy doc.
6. Build the Work Email waterfall on the resulting people table: reorder providers cheapest-first, remove the built-in validator.
7. Add a dedicated external verifier (Enrichly) gated by a run condition ("only run if work email is not empty"), written via Clay's AI/prompt-based run-condition builder rather than the manual UI.
8. Output MX Domain and Result fields from the verifier; classify results into Valid / Invalid / Valid-Catch-all / Catch-all-only, and build any outreach list only from Valid + Valid-Catch-all.
9. For any AI/Claygent-based signal: test on 5–10 rows first, default to Helium, gate with a run condition tied to prior qualification so the AI call only fires on already-qualified rows, and (for narrow/high-stakes markets) add a second Claygent column purely to validate the first.
10. Lock column names before relying on run conditions across the table — a later rename will silently break every condition that references that column.

## Instructor rules, opinions & decisions

- Clay exists to execute a strategy document, not to be explored feature-first; always start from what you're trying to prove.
- Recognizing when a filter/search configuration isn't working — and knowing how to fix it (e.g., switching keyword search to structured Job Function + Seniority filters) — is the actual skill of a GTM engineer, more than knowing which buttons to click.
- Delete any qualification signal/column that returns no true hits across your dataset; don't leave dead logic in a live table.
- Qualify, then filter to view the qualified subset — don't manually disqualify/delete rows one by one; this is standard agency practice for speed.
- Always use the AI/prompt-based method to write run conditions, not the manual field-by-field builder, unless you have 6+ months of deep Clay experience.
- Never let a run condition depend on a column whose name might later change; lock the table's column names before layering run conditions.
- Any CRM push or sequencer push should be gated by a run condition (e.g., email not empty, lead score ≥ threshold) — clients don't want false/incomplete information pushed to their systems.
- Always default to Helium for Claygent tasks; escalate to Neon then Argon only on failure; never start with the most expensive model.
- Test any Claygent prompt on 5–10 rows before running the full table.
- For narrow/high-stakes target markets (e.g., "only ~100–200 relevant banks in India"), use two separate Claygent columns — one to fetch, one to independently validate — rather than trusting a single prompt to both fetch and self-check.
- Build outreach lists only from Valid + Valid-Catch-all emails; never from catch-all-only addresses.
- AI agents (autonomous orchestration layers marketed on LinkedIn) are, in Yogesh's assessment, rarely actually used in production GTM engineering — cited at roughly "1 in 10,000 companies," largely blocked by data-compliance restrictions in Europe and in US insurance/consumer sectors — and most of what's shown on LinkedIn is "a gimmick for traction." He personally still uses Clay + Claude as the real production stack.
- Don't rush to find clients before mastering the skill; GTM engineering is a technical skill, not a department — build proof (portfolio) and trust before going to market.
- A credible portfolio needs, at minimum: a strategy document, a Clay table demonstrating the build, data pushed to a sequencer (Heyreach/Instantly), a Claude Code integration, a Make or n8n automation layer, and at least 5 Loom videos walking through the full pipeline.
- Because no beginner has real campaign metrics yet, cite industry benchmark numbers honestly when asked in interviews rather than fabricating results: LinkedIn — 70% connection-request acceptance, 30% reply rate on accepted connections; Email — 90%+ open rate, 3–5% reply rate.
- Enter the market slowly — start as a lead-list builder before managing full outbound campaigns; a real production Clay plan alone runs ~$3,000/month (agency tier), and a full GTM stack can run 5–10 lakh INR/month, so mistakes at the working-engineer level are genuinely costly to a hiring company.
- Growth in this field is gradual, not overnight — Yogesh cites his own progression (not yet at $5–6k, at ~$3k) as evidence that slow, methodical build-up is the realistic path, contrasted with one cited example of a fresher reaching a $45k/month agency role after ~2 months of disciplined portfolio-building.

## Assignments / homework given

- Whole group: build out the same qualification → find-people → find-work-email → validate-email pipeline demonstrated on Goji Berry, applied to each person's own selected 50-company list.
- Whole group: add the newly-found contacts to LinkedIn (network-building step, in preparation for outreach).
- Whole group (portfolio): pick a company, write a strategy document, build the supporting Clay table, run/execute a campaign, and record 5 Loom videos demonstrating the pipeline.
- Yogesh Jaiswal: will send the run-condition documentation, waterfall-logic notes, and the email catch-all/valid definitions document to the WhatsApp group (waterfall doc was confirmed not yet written — "I don't think I have it").
- Next session (explicitly previewed): validating LinkedIn URLs, plus additional unspecified topics.

## Deepu's questions & the answers she got

Deepshikha did not speak during this session (present on the invite list; no attributed transcript lines). The main active participants were sampath, Gagan, Alok, and Neeraj.

## What this means for the Saffron build

- Structure Saffron's qualification pipeline the same way: (1) a clear, written signal list from Saffron's own strategy doc, (2) each signal built as its own enrichment/filter column, (3) dead signals (zero true hits across the dataset) removed rather than left in the table.
- Use structured Job Function + Seniority filters (not free-text keyword search) when qualifying for Saffron's ICP roles (e.g., engineering leadership, hiring managers) — this session demonstrated keyword search under-performing structured filters on an almost identical role-headcount problem.
- Gate every expensive step (email verification, any Claygent AI call, any CRM/sequencer push) with an explicit run condition, written via Clay's AI/prompt-based builder, and finalize Saffron's column names before wiring those conditions in.
- Default every Claygent column to Helium and test on 5–10 rows before scaling to Saffron's full account list; if Saffron's evaluation criteria require high-confidence judgment calls (e.g., verifying "this company genuinely uses AI coding tools in hiring"), consider a second Claygent column dedicated purely to validating the first, per the "narrow/high-stakes market" pattern shown here.
- Build the eventual outreach/contact list from Valid + Valid-Catch-all emails only, and treat catch-all-only addresses as non-deliverable for practical outreach purposes.
- Frame the finished Saffron Clay table itself as the primary portfolio artifact — Yogesh's closing point that "the table decides what kind of GTM engineer you are" and "the table itself tells [a company] how much they'd be willing to pay you" applies directly to how the Saffron project should be evaluated and presented.

## Resources mentioned

Clay, Prosper/Prosperia (data source), HG Insights, Apollo.io, Lemlist, Instantly, Enrichly, HubSpot, Zoho, Salesforce, Heyreach, Claygent (Helium, Neon, Argon models), Claude/Claude Code, Make, n8n, Loom, Upwork, LinkedIn, WhatsApp group (for shared documents on run conditions, waterfall logic, catch-all/valid email definitions — none of these documents are included in the source transcript itself).
