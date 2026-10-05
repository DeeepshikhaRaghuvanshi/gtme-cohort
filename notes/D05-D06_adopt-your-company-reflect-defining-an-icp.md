# D05-D06: Adopt your company + reflect + Defining an ICP (2026-09-09)

## TL;DR
- Strategy documents come first, before any tooling work: company details, founder info, problem/pricing, ICP (decision makers + champions), TAM/SAM/SOM, signals/intents, exclusion lists, and messaging templates.
- ICP building has two mandatory sub-steps: (1) separate **title keywords** from **seniority level** (never search a combined job title like "Product Manager" as one string), and (2) always add **exclude keywords** (e.g., exclude "production" when targeting "product") to protect data quality and tool credits.
- Segmentation means splitting a target list by functional variant (product / innovation / digital / growth / operations, etc.) so each segment gets its own 5-10 campaigns — real client example: ~400 campaigns run for one company (cm.com).
- Exclusion lists are client-provided, dynamic (updated every 10-15 days), and standardly include competitors, active customers, companies already "in talks," Google/Microsoft-scale legacy companies, and .org/.gov/.edu domains.
- Firmographics need precise city+state+country structuring (New York is both a city and a state; duplicate city names exist across countries) and dual employee-count columns (raw number + range); Claude is used to auto-fill missing firmographic data.

## Key concepts

**ICP as a layered construct.** Gagan's framing (endorsed by Yogesh): an ICP is never 100% precise — realistically 80-93% accurate, ~10% "loophole" for edge cases. Three layers: (1) **firmographic** — headcount, revenue, industry, geography, funding stage; (2) **technographic** — what tools the target company already uses (relevant for competitive displacement, e.g., pitching HubSpot to a Salesforce user); (3) **persona** — the actual individual(s) reached out to. Persona is deceptively hard — took Yogesh ~2-3 months to get right.

**Title vs. seniority — the two-stage ICP filter.** Instead of searching a combined string like "Product Manager," split into **title keyword** ("product") and **seniority band** (C-level, VP, Director, Head) — lets you scale the search rather than hand-listing every title variant.

**Exclude keywords — a credit-protection mechanism.** Searching "product" without excluding "production" pollutes results and burns credits; "Chief Product Officer" without exclusions returns "Chief Production Officer" too. Standard excludes given: production, marketing, manufacturing, sales, recruitment (for product-adjacent roles).

**Title-variant expansion ("titles experimental").** Companies name similar functions differently (a "Growth Manager" elsewhere does what a "Product Manager" does here; newer titles like "Forward Deployed Engineer" exist too) — ask AI (Claude/GPT) to generate variants rather than guessing. Yogesh expanded "product" into product, digital, innovation, growth, operations, management, strategy, development, UX, CX — each its own **segment** because each reflects a genuinely different job aspect (digital = customer-facing strategy; innovation = AI/token-cost work; growth = marketing/positioning; operations = build execution), not a mere synonym.

**Segmentation → campaign math.** Each segment gets 5-10 campaigns; ~20 segments = 200-300 campaigns/company/quarter, spread across many LinkedIn/email accounts. Real example: cm.com (his first India-based client) ran ~400 campaigns total. Rationale: granular segmentation isolates what's working — a "two years back" mistake was one massive campaign to a big undifferentiated "product people" list, which never worked.

**Decision maker vs. champion.** Decision maker = buying authority (e.g., CPO). Champion = no purchase authority but internal influence (Product Director/Head/Manager) — a secondary path when the decision maker doesn't respond. New tactic: "borrowed authority" outreach — for a "Product & Innovation" segment, run LinkedIn outreach through your own company's actual Head of Product & Innovation's profile, since peer-to-peer framing lands better than a generic company account.

**Exclusion list contents and governance.** Standard categories: direct competitors (same-space companies — a voice-AI company won't sell to another voice-AI company), active customers, companies already "in discussion" with the client's sales team, and — confirmed with the client each time — mega-companies like Google/Microsoft. Refresh every 10-15 days and re-upload as a CSV into the outreach tool (demoed in HeyReach). Internal nuance: once one team LinkedIn account reaches a person, no other team account should reach them again.

**Why not sell to Google/Microsoft.** Two reasons: (1) sales-side — huge company, long compliance-heavy cycles, builds in-house, consumes disproportionate bandwidth; (2) GTM-specific — including a mega-company returns 2,000-3,000+ people, poor ROI for list-building bandwidth vs. targeting via an event or warm intro instead.

**Excluded domain types.** .org/.gov/.edu excluded as standard practice — these buyer types don't fit typical fast-moving B2B SaaS motion. Apollo/Prospio can't filter these natively; filtering happens downstream in Clay/Claude.

**Firmographics — location precision.** Live "quick task": how to filter for "companies in New York"? Naive answer (type "New York" in city) is wrong — New York is both city and state, and city names repeat across countries/states (Bristol US vs. UK; Adelaide Australia vs. US). Rule: always structure location as **city + state + country**, both company-level and person-level (they can differ). Also flagged: UK is not part of the EU — assuming an "EU" filter covers UK silently excludes it.

**Firmographics — funding & employee count.** Funding stages run pre-seed through Series A+. Employee count needs **two columns**: raw number (99) and bucketed range (50-100) — Claude trained to backfill missing values.

**Technographics.** Two components: (1) front-end visible stack (hosting, CRM, anything visible on the public site) via BuiltWith; (2) deeper researched detection — HG Insights (research-based) and Sumble (newer, more intelligent account-level mapping than HG Insights). Matters more now because pure signal-based outbound is less effective than it used to be.

**AI-first ICP construction.** Prompt Claude/GPT first ("if this is the company, what should the ideal ICP be?"), then verify/adjust manually. For scaling across many clients, Claude Projects is the mechanism — a company-specific project with the knowledge base loaded, generating/refining segmentation and ICP lists directly.

**Bandwidth constraint.** A solo GTM engineer should not manually handle more than 2-3 clients at once for high-quality work; scaling further needs AI automation or an agency team.

## Tools shown & how they were used
- **Ocean.io sign-up issue** (00:04:15-00:05:51) — Deepu reported Ocean.io rejects personal/disposable email addresses; Yogesh offered spare business emails to the group.
- **Strategy document template** (00:06:51-00:09:39) — shown live (with a real prior example, "Bounty"): company details/founder info, product/pricing/competitors, ICP (decision makers + champions), exclusion list, TAM/SAM/SOM, signals/intents/triggers, messaging templates.
- **Apollo / Prospio** (00:16:32-00:20:02) — demoed building title-keyword + exclude-keyword strings ("product" excluding "production"; CPO excluding "Chief Production Officer").
- **A real client list (voice-AI company, Euro-based)** (00:21:18) — 993 companies worldwide, segmented into CTOs, VP/Head of Engineering, Security titles, CEOs, Founders, Founding Team, other staff (e.g., ML engineers) — illustrating real-world segment granularity.
- **HeyReach** (00:49:48) — shown uploading a CSV as an exclusion list inside the tool.
- **BuiltWith** (00:12:24) — front-end technographic lookup (visible tool stack, e.g., CRM in use).
- **HG Insights** (00:12:24, 01:00:37) — research-based technographic tool, deeper than BuiltWith.
- **Sumble** (01:00:37-01:02:00) — recommended as superior to HG Insights for account-level tech-stack mapping.
- **Claude / Claude Projects** (00:44:08-00:48:36, 01:03:25-01:04:35) — the engine for title-variant expansion, segmentation math on seed data, auto-suggesting an ICP, and scaling ICP-building across clients via a company-specific Claude Project.

## Instructor rules, opinions & decisions
- Always split title from seniority when filtering; never search a combined literal job title string.
- Always add exclude keywords to every title-based search — treat this as mandatory, not optional, to protect data quality and credit spend.
- Segment lists by genuine functional variation (not by cosmetic title synonyms) — each real segment gets its own 5-10 campaigns.
- Never include direct competitors (same-space companies), active customers, or companies already "in discussion" with the client's sales team in a target list.
- Confirm with the client, every time, whether mega-companies (Google/Microsoft-scale) should be included — default is exclude, due to poor ROI on bandwidth.
- Always exclude .org/.gov/.edu domains from commercial B2B outbound.
- Refresh exclusion lists every 10-15 days via direct client check-ins — skipping this is called out as a common, costly mistake (reaching a company already in active client discussions).
- Location data must always be structured as city + state + country (both company-level and person-level) — never a bare city name.
- Build the ICP with AI first (Claude/GPT), then verify — don't hand-build from a blank page.
- Cap manual client load at 2-3 companies at a time unless operating as an agency with a team.
- GTM engineers don't need deep sales training — only the specific working vocabulary (ICP, ICP filters, firmographics, technographics, exclusion filters, decision maker vs. champion).
- Strategy documents from students would be personally refined by Yogesh over the weekend — students should submit their current understanding, not a polished final draft.

## Assignments / homework given
- **[Gagan, Deepu — explicitly named, but applies to everyone who hadn't yet]** Finalize selection of a YC-directory (or own/existing) company to adopt as the ongoing GTM-engineering project company.
- **[Everyone]** Draft a strategy document for the chosen company covering firmographics, technographics, and ICP definition (through the ICP section only — decision-maker/champion split not required yet); a Loom video will also eventually accompany outreach to the founder.
- **[Everyone]** Research US/Europe city-state naming structures (e.g., New York city vs. state, Bristol US vs. UK, Adelaide US vs. Australia, UK vs. EU) to avoid firmographic filtering errors.
- **[Everyone]** Compare Sumble vs. HG Insights for account-level technographic mapping and form a view on which is better.
- **[Yogesh]** Share business email addresses to unblock Ocean.io signups; share the strategy document template file via WhatsApp; refine submitted strategy documents over the weekend.

## Deepu's questions & the answers she got
- **Reported blocker:** Ocean.io rejected her signup (no personal/disposable emails accepted). Resolution: Yogesh offered spare business emails to the group.
- **Company status:** Hadn't picked a company yet — said she'd skimmed the YC list and would decide later that day.
- **Q: "Is this segment list the same one we brainstormed with AI earlier? I'm confused."** A: Targeting only the literal department (e.g., product) won't yield enough people, so AI surfaces title variants representing adjacent departments (innovation, digital, growth) — expanding the pool while each variant stays a distinct, genuine segment, not a duplicate list.
- **Q: "I see two downstream flows in data cleaning — targeting by department and by seniority level — is that right?"** A: Confirmed yes; both are required outputs before campaigns are built.
- **Q (bigger picture): "We select a company to build a portfolio, and also to pitch to that same company — am I understanding correctly?"** A: Confirmed — prior-batch students reached out to founders directly after finishing the strategy; since these are early-stage/pre-product companies, students can offer to work with them once ready. GTM roles are rarely posted publicly, so this is a real hiring channel.
- **Follow-up: "Does it matter if the company is already hiring for a similar role?"** A: Doesn't matter — GTM roles are inherently insider-referral roles; the strategy artifact itself earns consideration. Portfolio/practice is the primary goal; the pitch opportunity is a "byproduct."

## What this means for the Saffron build
- Write Saffron's strategy document now, using this exact template (company/founder/problem/pricing/competitors, ICP, exclusion list, TAM/SAM/SOM, signals/intents, messaging) to stay compatible with Yogesh's feedback loop.
- Define Saffron's ICP with the title/seniority split: title keywords like "engineering," "hiring," "talent," "platform" against CTO/VP-Eng seniority bands — plus exclude keywords (generic "recruiter"/"HR" titles, unrelated "engineering" hits).
- Build Saffron's exclusion list early: known competitors in AI-coding-hiring-assessment, existing design partners, and confirm with Saffron's team on excluding mega-companies and .edu/.gov.
- Use technographic detection (BuiltWith/Sumble-style: does the org already use Copilot/Cursor-type tools) as a core qualifying filter for Saffron's ICP.
- Apply the AI-first ICP workflow: prompt Claude with Saffron's product description for a first-draft ICP and title-variant list, then verify manually — mirrors exactly how the class was instructed to work.

## Resources mentioned
Apollo, Prospio, Ocean.io, ZoomInfo, Sales Navigator, People Data Labs, Clearbit, BuiltWith, HG Insights, Sumble, HeyReach, Claude, Claude Projects, GPT, Whisperflow (example company), cm.com (real prior client example), YC startup directory, Yogesh Jaiswal.
