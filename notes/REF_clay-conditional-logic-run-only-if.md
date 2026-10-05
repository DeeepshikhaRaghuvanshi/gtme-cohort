# Clay Conditional Logic & "Only Run If" — Cheat Sheet

## What it is
Every enrichment/action/integration column in Clay has an "Only run if" setting: `if (condition) { run } else { skip — no credits spent }`. This is the single mechanism that turns Clay from "pay for every provider on every row" into a decision engine. Found in a column's **Run Settings** (gear icon), sometimes nested one level deeper in newer UI versions — it hasn't been removed, just reorganized.

Two ways to build a condition:
- **Manual formula** — write Clay's formula syntax yourself.
- **"Use AI"** — describe the condition in plain English, click Generate formula; Clay shows sample outputs so you can sanity-check before saving.

## Syntax basics
- Reference a column with `/` in the UI (docs show it as `{{column_name}}`).
- Comparisons: `==` `!=` `>` `<` `>=` `<=` `is empty` `is not empty`.
- Logical: `AND` (all must be true), `OR` (at least one true), `NOT` (reverses).
- Clay's formula language is a **subset of JavaScript** — no custom functions/variables. A formula pasted in from ChatGPT/another LLM outside Clay may not run if it uses unsupported JS features; prefer Clay's own AI Formula Generator.

## Core patterns
- **Waterfall gate**: `{{previous_result}} is empty` → only try the next (usually pricier) provider if the first came back blank. Order waterfalls by cost + accuracy: most accurate/expensive first, cheap/broad fallback last.
- **Quality gate before export**: `{{email}} is not empty` → only push to CRM/sequencer/Slack when data is actually usable.
- **Score/segment gate**: `{{lead_score}} > 80 AND {{industry}} == "SaaS"` → only enroll high-fit leads.
- **Gate on a prior AI classification**: `{{qualification_column}} == "Yes"` → only spend deep-research credits on rows a cheap prior step already qualified.
- **Retry on error**: `{{prior_column_status}} == "error"` → re-run only the rows that failed, instead of re-running everything.
- **Nested logic**: `({{title}} == "Founder" OR {{title}} == "CEO") AND NOT {{industry}} == "Nonprofit"`.

## Advanced playbook
- Gate expensive steps behind cheap classifications — run a free/cheap AI formula or simple field check first, let it decide if the pricier Claygent/scrape/enrichment fires.
- Segment before you spend: separate Tier-1 (worth deep research) from Tier-3 (basic enrichment only) accounts via conditional runs rather than running the most expensive workflow on every row.
- Order waterfalls by cost + accuracy, never alphabetically/arbitrarily.
- Default to "is empty" as your waterfall gate — simplest, most reliable way to avoid duplicate spend across chained providers.
- Validate before export: gate CRM uploads, sequencer enrollment, Slack/webhook notifications behind data-quality checks (valid email, non-empty phone, correct region).
- Preview sample outputs next to the formula generator before saving — English descriptions can evaluate unexpectedly against real data (type mismatches, case sensitivity in `==`).

## Troubleshooting
| Problem | Fix |
|---|---|
| Can't find "Only run if" | It's in the column's Run Settings, one level deeper than the toolbar |
| Generated formula doesn't match intent | Rephrase more precisely (name exact columns/values), or hand-edit in code view |
| Formula errors on JS from outside Clay | Clay only supports a JS subset — rebuild with the AI Formula Generator |
| Condition always evaluates false | Check type mismatches (number vs. quoted string) and confirm the right column is referenced via `/` |
| Waterfall runs every provider on every row | Confirm each downstream provider has its own "Only run if `{{previous_output}} is empty`" — without it, Clay runs unconditionally |

## Credit-efficiency / model-choice points
This doc is the general conditional-logic mechanism, and it is the primary lever for controlling *all* spend in Clay, AI included:
- **Claygent-specific gating**: run a cheap prompt first that outputs Yes/No (e.g., "is this a founder/CXO/sales role?"), then gate the more expensive deep-research Claygent call behind `{{qualification_column}} == "Yes"` — this is the direct mechanism for keeping AI-model spend proportional to lead quality rather than list size.
- **Retry-on-error pattern applied to AI**: rather than re-running an entire Claygent column when some rows error out (wasting credits on rows that already succeeded), gate a follow-up column on `{{prior_column_status}} == "error"` so only the failed rows get retried.
- **The framing to use for the "bonus point" LinkedIn post**: conditional logic is the credit-efficiency lever that sits *above* model choice — picking Helium over Argon saves credits per call, but gating whether an expensive call fires at all (via "only run if") is what keeps total spend proportional to lead quality as a table scales from 50 rows to 5,000. The two levers (model tier + conditional gating) are meant to be used together, not as alternatives.
- As tables grow, conditional logic — not model selection alone — is described as "usually the single biggest lever for making a Clay build financially sustainable at scale."

## Applying this to the Saffron Clay table
- Gate any Claygent research column (e.g., checking a company's hiring process for AI-coding-tool usage) behind a cheap prior qualification step (company size, industry, "actively hiring engineers") using `{{qualification_column}} == "Yes"` — mirrors the exact pattern used for the Lantern build's job-posting/HR-team qualification.
- Build the qualify/disqualify decision as an explicit waterfall: cheap firmographic filter → cheap Claygent/Helium check → expensive Argon-tier research only for rows that clear both prior gates.
- Add a retry-on-error condition (`{{status}} == "error"`) on any Saffron research column prone to Claygent flakiness, instead of re-running the whole column and re-paying for rows that already succeeded.
- Gate CRM/export/outreach steps behind a data-quality check (valid email, non-empty key evidence field) so downstream systems never receive incomplete Saffron prospect rows.
- When writing the credit-efficiency LinkedIn post, use this doc's framing explicitly: model choice (Claygent doc) + conditional gating (this doc) are the two levers, and gating is the bigger one at scale.
