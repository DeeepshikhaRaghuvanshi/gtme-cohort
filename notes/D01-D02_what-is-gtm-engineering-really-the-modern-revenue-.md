# D01-D02: What is GTM engineering, really + The modern revenue funnel (2026-09-07)

## TL;DR
- GTM engineering = building outcome-driven systems (not just "cool builds") that bridge engineering and go-to-market; today it is ~90% outbound lead generation, expanding into CRM hygiene, orchestration, and AI agents.
- Data & sourcing is ~80% of the job. Rule: never trust a single data provider — always waterfall across 3+ sources and validate with a second (often AI) layer.
- The 7-layer curriculum: Data & Sourcing → Enrichment → Signals/Intent → Orchestration → Execution (channels) → CRM/Reporting → AI Agents (Claude Code). Clay gets ~1 month of dedicated focus.
- Career advice: target GTM agencies (especially European ones) before in-house roles — lower barrier to entry, higher pay, less competition than India-based agencies.
- Revenue funnel logic: every founder's real goal is money → GTM engineers support this via lead scoring into three buckets: disqualified / nurture / sell.

## Key concepts

**GTM engineering, defined.** Neeraj: running outbound campaigns (ICP → infra → enrichment → signals → copy → campaigns). Deepu: sitting at the intersection of engineering and GTM strategy — integrating siloed revops/sales/marketing data to cut manual effort. Gagan: "running the pipelines" on top of foundational data hygiene. Yogesh's synthesis: still an unexplored field, currently centered on outbound lead gen but expanding into CRM cleanup, orchestration, and AI agents. Best-fit clients are new/high-growth/well-funded startups (Cursor, OpenAI, Anthropic) — not mature companies like Freshworks or ServiceNow that already have systems and trust built internally.

**"Builder syndrome."** Engineers who love building complex Clay/Claude Code systems for their own sake, disconnected from whether the build moves a business metric. Tied to agency churn — agencies that overbuild without outcomes lose clients. Rule: only build what's required to solve a specific, named business problem.

**Data quality & the "waterfall."** No single provider (Apollo, Prospio, ZoomInfo, Sales Navigator, Exa, Harmonic) has complete/accurate coverage — each returns a different subset for the same search (live example: 100 people searched → Apollo 60 emails, Prospio 90, Sales Nav 200 people, Exa 250). Standard: query 3+ sources and cross-validate, never rely on one. Second qualifying dimension: **refresh rate** — how fast a provider updates job changes; stale data (someone shown at their old employer days after switching) breaks the pipeline.

**Secondary/AI-layer validation.** Databases can't natively filter qualitative criteria like "AI-native company." Worked example: finding funded AI-native founders in Germany. Sales Navigator/Crunchbase alone can't filter "AI-native"; correct method is (1) pull a broad seed list of companies from Apollo/Prospio, (2) run it through Clay with an AI step classifying each as AI-native yes/no, (3) only then search people (founders/CEO/CTO/co-founder/founding member for coverage) against the qualified subset. A naive single-tool search might surface ~100 companies when the real set is 650–750+ — called a "wrong approach."

**Geo-filtering for events/outbound.** Don't filter narrowly by country — model realistic travel radius. Example: an event in Germany should include founders from the Netherlands too, since people travel. Ocean.io supports literal radius search (e.g., 30 miles around a city) for this; promised for a future live demo (didn't load this session).

**Revenue funnel & lead scoring.** Every company's real goal is money; GTM engineers optimize lead flow. Score every lead (out of 10 or 20) into three tiers — **disqualified** (no outreach), **nurture** (stay in touch, no hard sell), **sell** (immediate outreach, e.g., score 7–10) — cutoffs set jointly with the founder.

**Software sales economics.** Technical deals: $10K–millions/year, 3–9 month cycles; an AE costs ~₹15 LPA, so ~₹3–4 lakh/month for 9 months per closed deal. This is why there are 400+ GTM tools — companies want fewer, more leveraged people. Role ladder: SDR/BDR (cold outreach) → AE (deal closure) → Senior AE (large deals).

**Lookalike prospecting.** Ocean.io and Disco take a seed company (e.g., "Apollo Hospital" as a first customer) and return similar companies — valuable for early VC-backed startups building a customer base fast after landing first logos.

**Market maturity shift.** GTM engineering moved from industry-wide "testing everything" (email, LinkedIn automation, WhatsApp) to "we know what works for us." Examples: a company with 75 connected LinkedIn accounts found LinkedIn worked and email didn't; Chai Point (sells chai vending machines, not just cafés) found WhatsApp worked for UAE audiences; Moabara landed a big deal via an unexplored B2B partnership channel. Strategic clarity on channel now matters more than tool proficiency.

## Tools shown & how they were used
- **Apollo, Prospio (Prospeo), ZoomInfo, Sales Navigator, Exa, Harmonic** (00:38:34–00:43:44) — compared live for coverage differences on the same search; positioned as the standard "waterfall" data-sourcing stack. Exa described as a Google-search-style data tool from a fast-growing European startup; Harmonic as a startup/investor-data-only provider that gives clean, purpose-specific columns (vs. Apollo/Prospio's 30–50 column exports with irrelevant fields).
- **Ocean.io and Disco** (00:46:08–00:47:36) — demoed lookalike search: typed a seed company name ("Apollo Hospital") into Disco to generate a list of similar companies; same workflow shown conceptually for Ocean. Framed as the go-to tool for early-stage/VC portfolio company expansion.
- **Ocean.io geo-filter** (00:59:06) — mentioned/attempted live (didn't load) — a mile-radius filter (e.g., 30-mile radius around a city) for event-based geo-targeting; promised for a future class demo.
- **Clay** — referenced throughout as the central enrichment/validation/AI-classification layer (e.g., running the "is this company AI-native" check) and as the tool that consolidated waterfalling, dedup, enrichment, and API orchestration into one product — explaining why it became the anchor tool of the whole GTM-engineering discipline.
- **Agency contact sheet** (00:22:41) — Yogesh shared a pre-built spreadsheet of 1,584 people across 150 GTM engineering agencies worldwide (with LinkedIn URLs, websites, emails) already posted in the group description; instructed students to send connection requests only (no cold messaging yet).

## Instructor rules, opinions & decisions
- Never rely on a single data provider — minimum of three, always waterfall and cross-validate.
- Evaluate any data tool primarily on **refresh rate** (job changes, email/profile validity), not just breadth of columns.
- Avoid "builder syndrome" — every build must map to a measurable business outcome, not look impressive.
- Set explicit learning boundaries: don't try to master every one of the ~400+ GTM tools; pick a few, go deep, and know the landscape broadly.
- Career positioning: target agencies (not corporates) first, and specifically European agencies where language skill is a competitive moat; Indian companies/agencies pay less and value the skill less.
- Daily (not weekend-only) learning cadence is required — Yogesh cited a prior 15-person batch's outcomes (3 employed, 2 more in progress) as evidence this cadence works.
- Sessions are all recorded and linked via calendar automatically — no need to worry about missing a live session.
- Signals/intent-based outbound ("congrats on your funding" style messaging) is explicitly called out as largely not working anymore; what does still work is a genuinely customized opening line plus a clear offer — not full AI/GPT-generated customization throughout.

## Assignments / homework given
- **[Everyone]** Create a separate/dedicated Gmail account + a separate Chrome workspace/profile tied to it, to be used for signing up to ~30 GTM tools without spamming personal inboxes — due before the next session.
- **[Everyone]** Send LinkedIn connection requests (no messaging yet) to contacts in the shared 1,584-person GTM agency sheet.
- **[Yogesh]** Will share supplementary material on how software/tech sales cycles work (for non-sales-background students).
- **[Neeraj, but framed as a general suggestion to all]** Keep a personal roadmap/use-case document logging GTM engineering scenarios encountered (e.g., the Germany event-list problem) to build strategic "muscle," and optionally share with Yogesh for more use cases.

## Deepu's questions & the answers she got
- **Deepu's self-introduction / definition of GTM engineering:** She described a GTM engineer as someone who "sits at the cusp of engineering and go-to-market strategies," noting that revops/sales/marketing teams typically work in silos without engineering backing, and that AI has enabled engineers to integrate that siloed data and cut manual effort. Yogesh affirmed this ("this is good") without extended pushback.
- **Q: "You mentioned the geo-search feature in Ocean.io — I recall using something similar in Clay as well. How do we decide which tool to use for a certain kind of data?"** A: Yogesh explained that for geo-search specifically, tools like Ocean and Exa let you pick a radius in miles around a city and tune how far out to search; beyond that specific feature, the general right approach for a sourcing task is to first build a seed list of companies (from Apollo/Prospio), then push it through Clay for a second-layer AI qualification pass, then go back to people-search tools (Apollo/Prospio/AI-native databases/Sales Navigator) for personas — i.e., tool choice follows the stage of the workflow (company discovery → qualification → people discovery), not personal preference.
- She also gave her background when asked: full-stack developer background, has spent her working hours building data pipelines and automating workflows; had already built a few Clay workflows independently before joining the cohort, using Clay daily-ish tools like this but not yet run real campaigns or outreach.

## What this means for the Saffron build
- Saffron's ICP (engineering leaders/hiring managers evaluating AI-coding-tool usage) will not be reliably filterable in a single database — plan a two-stage sourcing pipeline: seed company/persona lists from Apollo/Prospio/Sales Navigator, then a Clay-based second-layer AI classification pass (e.g., "does this company evaluate/actively use AI coding tools in hiring") before outreach.
- Apply the disqualified/nurture/sell lead-scoring model directly to Saffron's pipeline — define concrete scoring signals (e.g., job postings mentioning AI-assisted coding assessments, recent funding, hiring velocity for engineers) rather than reaching out to every match.
- Treat data refresh rate as a selection criterion when picking Saffron's data stack — hiring signals and role changes go stale fast, so a provider with fast job-change refresh matters more than raw contact-count breadth.
- Resist "builder syndrome" on the Saffron Clay tables — every enrichment/workflow step should map to a specific qualification or personalization outcome for outreach, not just impressive-looking automation.
- Given YC/technical-hiring is a narrow, emerging niche, expect to need lookalike tools (Ocean/Disco) off Saffron's early design partners to find comparable companies, since no single database will have an "evaluates AI coding tools" filter.

## Resources mentioned
Apollo, Prospio (Prospeo), ZoomInfo, Sales Navigator, Exa, Harmonic, Clay, Ocean.io, Disco, Crunchbase, SmartLead, Instantly, HeyReach, PhantomBuster, Dripify, Lemlist, Claude Code, Rippling, Anthropic, Chai Point, Moabara, Yogesh Jaiswal, Kushagra (mentioned as a guest speaker/former lawyer-turned-PM-turned-GTM-engineer).
