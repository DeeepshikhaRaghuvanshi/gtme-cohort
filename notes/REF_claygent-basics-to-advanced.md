# Claygent: Basics to Advanced — Cheat Sheet

*Instructor note: Clay ships/reprices Claygent models often — verify current model names/costs inside Clay before relying on exact numbers below.*

## What it is
Claygent is Clay's built-in AI research agent: unlike a normal enrichment (fixed data provider, returns whatever it has), Claygent browses the live web (or an attached doc) per row, reasons, and writes a structured answer. Use it when the answer isn't in a clean database field — careers pages, press releases, About pages, PDFs.

## How it works
1. Add a Claygent column; give it input fields (Domain, Company Name, etc.).
2. Write a prompt: task, source(s) to check, exact output format.
3. Pick a model (Helium / Neon / Argon, or an external LLM).
4. Generate to preview, then Save.
5. Run on 5–10 rows first, check quality, then scale.

## The three native model tiers

| Model | Credits | Best for | Struggles with |
|---|---|---|---|
| Helium | 1 | Single-page lookups (one field, one known page) | Multi-page nav, ambiguous content, multi-step reasoning — often blank |
| Neon | 2 | Several typed fields from one page, consistent structure | Deep research needing multiple linked pages |
| Argon | 3 | Deep research: multi-click navigation, unpredictable structure, cross-source synthesis | Simple single-field lookups — overkill |

Other models in the same dropdown: GPT-4o mini / Claude Haiku / Gemini Flash (~0.5 credit, cheap/fast, not for deep research); GPT-4o / Claude Sonnet / Claude Opus / Gemini Pro (flagship, variable cost); advanced reasoning models (o1-class) — highest cost, billed on tokens + 20% premium.

## Prompting fundamentals
- State the output format **first** — not background, format first.
- Give step-by-step instructions (e.g. "check careers page first, then recent press"), not a vague goal.
- Explicitly constrain verbosity — unconstrained, Claygent defaults to long explanations.
- Name the model's #1 known failure mode directly in the prompt (e.g. "don't confuse the parent company with a subsidiary").
- Use Clay's Metaprompter/Sculptor to convert plain English into a structured prompt instead of hand-tuning through repeated paid runs.

## Advanced techniques
- **Model-tier escalation (waterfall across models)**: run Helium first; if empty, escalate to Neon; if still empty, escalate to Argon. Keeps the cheap model doing ~90% of volume.
- **Claygent Builder/Sculptor**: build an agent conversationally, attach reference docs (ICP doc, tone guide, PDFs, CSVs), test free against real rows before deploying, reuse across tables.
- **Multi-Claygent chains for judgment calls**: don't cram research + scoring + copywriting into one giant prompt — chain narrow agents (one researches/summarizes, one scores against criteria, one drafts copy). Each stays debuggable.
- **Conditional runs to control spend**: gate every Claygent column with "Only run if" so it never fires on rows that don't need it (e.g. only run deep research on rows that already passed a cheap firmographic filter).

## Cost-control checklist
- Never run a new prompt on a full table — test 5–10 rows, confirm, scale to 50, then everything.
- Default to Helium; escalate only when it demonstrably fails on your data.
- Set a max output length in model config so verbose models don't burn extra tokens.
- Use "Only run if" logic so expensive models only touch qualified rows.
- Use the Metaprompter to get the prompt right *before* scaling, instead of paying for trial-and-error across the full table.
- Remember the trade-off isn't just "cheapest wins": a small accuracy drop across a large row count can cost more in missed leads than the credits saved by the cheaper model.

## Credit-efficiency / model-choice points
- **Fixed vs. variable pricing** is the core cost mechanic to understand: Helium/Neon/Argon are flat-rate regardless of how much the model "thinks"; heavier reasoning models are variable — billed on actual tokens used, plus a 20% premium.
- **More browsing = more compute**: Argon-tier tasks load multiple pages/follow links/cross-reference before answering — each step is real compute, which is why deep multi-step research costs more than a single-page lookup.
- **Reasoning tokens are expensive**: advanced reasoning models generate large internal "thinking" token counts before answering; since variable-priced models bill on total tokens, a model that reasons more costs more per run.
- **Actions vs. Data Credits**: every AI enrichment consumes one flat Action (Clay's orchestration charge) *plus* Data Credits from the model itself. Model choice only changes the Data Credit side.
- **Personal API keys bypass Data Credits**: connecting your own OpenAI/Anthropic/Gemini key means you only pay the Action — model usage bills straight to your own provider account. Requires meeting that provider's rate-limit tier (e.g. Anthropic Tier 4+, OpenAI Tier 2+) for Claygent's web-research load.
- Bottom line for a LinkedIn post on this: the actual lever isn't "always pick the cheapest model" — it's (1) tiering by task complexity (Helium→Neon→Argon waterfall), (2) gating expensive calls behind cheap qualification with conditional runs, and (3) testing small before scaling. Those three together are what actually control spend, more than any single model swap.

## Applying this to the Saffron Clay table
- Default every new Saffron research column to Helium/Neon first; reserve Argon (or an external reasoning model) only for genuinely multi-page tasks like verifying how a company's hiring process uses AI coding tools across multiple job postings/careers pages.
- Gate any Claygent research step behind a cheap firmographic/ICP filter first (company size, industry) so AI research credits only hit companies that already pass basic qualification — directly mirrors the D25-D26 Lantern build's job-posting/HR-team gate.
- For anything resembling a judgment call (e.g., "does this company evaluate AI coding tool usage in hiring: yes/no"), don't trust a single Claygent verdict — cross-check with a deterministic formula against the raw evidence text, the same fix Gagan used for compliance signals.
- Use the Metaprompter to lock down Saffron's research prompts before running on the full prospect list, not after burning credits on 50+ rows of trial and error.
- If Saffron's research volume grows large, consider a personal API key to shift billing off Clay's Data Credits and onto direct provider billing — worth flagging as a credit-efficiency point in the LinkedIn post.
