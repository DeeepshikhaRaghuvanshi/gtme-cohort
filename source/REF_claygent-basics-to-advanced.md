# Claygent_ Basics to Advanced


Claygent: Basics to Advanced

Stable GTM · Instructor Reference Doc

Clay ships and reprices Claygent models frequently. Spot-check current model names and credit costs inside Clay right before class — the concepts below are stable, the exact numbers may drift.

## 1. What Claygent Is

Claygent is Clay's built-in AI agent for web research. Instead of pulling from a fixed data provider, it goes out onto the live web (or reads an attached document), follows your instructions, and writes a structured answer into a column. It's the tool you reach for when the answer isn't sitting in a clean database field — it's buried in a careers page, a press release, an About page, or a PDF.

Conceptually, Claygent sits apart from every other enrichment in Clay: normal enrichments call a fixed data provider and return whatever that provider has. Claygent instead reasons and browses on demand for each row, which is exactly why it's more powerful and more expensive.

## 2. How It Works, Structurally

You add a Claygent column to a table and give it input fields (e.g. Domain, Company Name).

You write a prompt describing the task, the source(s) to check, and the exact output format you want.

You pick a model (Helium, Neon, Argon, or an external model).

Claygent runs per row: it searches/browses, reasons over what it finds, and writes the answer into the column in your specified format.

You save and run it across your rows — start with a handful, confirm quality, then scale.

## 3. The Native Claygent Model Tiers

Clay has three first-party Claygent models. This tiering is the core mental model to teach — everything else is a variation on it.

## 4. Other Models in the Dropdown

Alongside the three native models, the Claygent model picker also offers general-purpose LLMs. These aren't Claygent-specific — they're the same foundation models available elsewhere in Clay's AI tools.

## 5. Why More Advanced Models Consume More Credits

Teach this as the core cost mechanic — students misuse Claygent almost entirely because they don't understand this part.

Fixed vs. variable pricing: Helium, Neon, and Argon use fixed pricing — a flat number of credits per run regardless of how much the model actually 'thinks.' Heavier reasoning models instead use variable pricing — credits scale with actual tokens used, plus a 20% premium on top.

More browsing = more compute: Argon-tier tasks often need to load multiple pages, follow links, and cross-reference content before answering. Each of those steps costs real compute, which is why deep multi-step research is priced higher than a single-page lookup.

Reasoning tokens are expensive: advanced reasoning models generate a large number of internal 'thinking' tokens before producing a final answer. Since variable-priced models are billed on total tokens, a model that reasons more literally costs more per run.

Actions vs. Data Credits: every AI enrichment also consumes one Action (Clay's flat charge for orchestrating the run) on top of the Data Credits the model itself costs. Data Credits are what change based on model choice — Actions don't.

Personal API keys shift the cost: connecting your own OpenAI/Anthropic/Gemini key lets you skip Data Credit charges entirely — you only pay the Action, and billing goes straight to your own account with that provider. This requires meeting that provider's own rate-limit tier (e.g. Anthropic Tier 4+, OpenAI Tier 2+) for Claygent's web research load.

## 6. Basics: Building Your First Claygent Column

In your table, click Add Enrichment.

Search for and select Claygent.

Write a prompt describing exactly what to find and how to format the answer.

Choose a model — default to Helium for a first pass.

Click Generate to preview, then Save.

Run it on 5–10 rows first, check quality, then scale to the full table.

## 7. Prompting Fundamentals

State the output format first. The opening lines of the prompt should say exactly what the answer should look like — not background context first, format first.

Give step-by-step instructions, not a vague goal. Tell Claygent where to look and in what order (e.g. "check the careers page first, then recent press").

Constrain verbosity explicitly. Left unconstrained, Claygent defaults to long explanatory answers — tell it to return only the field(s) you need.

Name the #1 failure mode. If you know the model tends to make a specific mistake (e.g. confusing a parent company with a subsidiary), call that out directly in the prompt.

Use Clay's Metaprompter / Sculptor to convert a plain-English description of the task into a structured prompt, instead of hand-writing and re-running raw prompts repeatedly.

## 8. Advanced Techniques

Model-tier escalation (a waterfall across Claygent models)

Run Helium first. If the field comes back empty, escalate the same row to Neon; if that also fails, escalate to Argon. This mirrors provider waterfalls but across model tiers — it keeps the cheap model doing 90% of the volume and reserves the expensive model for the rows that actually need it.

Claygent Builder / Sculptor

Clay's Claygent Builder lets you construct an agent conversationally, attach reference material (tone guides, ICP docs, PDFs, CSVs) directly to the prompt, test it for free against real rows before deploying, and reuse the same agent across multiple tables from one place instead of rebuilding the prompt each time.

Multi-Claygent workflows for judgment calls

For tasks that require real judgment (not just retrieval) — like qualifying a lead against your ICP — chain multiple focused Claygents instead of one giant prompt: one agent researches and summarizes, a second agent scores against defined criteria, a third drafts outreach copy using the first two outputs. Each agent stays narrow and is easier to debug than one prompt trying to do everything.

Conditional runs to control spend

Add a 'run only if' condition on every Claygent column so it never fires on rows that don't need it — e.g. only run the expensive research agent on rows that already passed a cheap firmographic filter. This is the same conditional-logic mechanic used elsewhere in Clay, applied specifically to cap AI spend.

## 9. Cost-Control Checklist to Teach

Never run a new Claygent prompt on a full table. Test on 5–10 rows, confirm quality, then scale to 50, then everything.

Default to Helium; escalate to Neon or Argon only when Helium demonstrably fails on your data.

Set a maximum output length in the model configuration so verbose models don't burn extra tokens.

Use conditional 'run only if' logic so expensive models only touch qualified rows.

Use the Metaprompter to get the prompt right before scaling, instead of paying for repeated trial-and-error runs across the full table.

Remember the trade-off explicitly: the cheapest model isn't always the cheapest choice — a small drop in accuracy across a large row count can cost more in missed leads than the credits saved.



| Model | Credits | Best for | Where it struggles |

|---|---|---|---|

| Helium | 1 credit | Single-page lookups: extract one field from one known page (e.g. a headline, a city, a LinkedIn URL). | Multi-page navigation, ambiguous content, multi-step reasoning — often returns blanks. |

| Neon | 2 credits | Semi-complex tasks: several typed fields from one page (yes/no, number, text, URL) with consistent structure. | Deep research that requires following multiple links or reading several pages. |

| Argon | 3 credits | Deep research and multi-step analysis: following links several clicks deep, unpredictable page structure, synthesizing across sources. | Simple single-field lookups — overkill, wastes credits. |



| Model | Typical cost | Notes |

|---|---|---|

| GPT-4o mini / Claude Haiku / Gemini Flash | 0.5 credit (outside Claygent) | Cheap, fast, good for simple text generation — not deep web research. |

| GPT-4o, Claude Sonnet, Claude Opus, Gemini Pro | Varies by model | General-purpose flagship models available in the Claygent model dropdown alongside Helium/Neon/Argon. |

| Advanced reasoning models (e.g. GPT o1-class) | Highest cost — several credits per run, priced on tokens | Billed on Clay's variable-pricing track: actual token usage plus a 20% premium, because these models 'think' through many reasoning tokens before answering. |