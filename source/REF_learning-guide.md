# GTM-Engineering-Learning Guide


THE GTM ENGINEERING PROGRAM

Learning Guide

The full day-by-day playbook for working through all 65 sessions

12 weeks  ·  60 sessions  ·  12 portfolio deliverables  ·  Data → Signals → Agents

Current as of mid-2026 · Named tools are today's defaults; the layer principles outlast any tool.

## Contents

If this list appears empty, right-click it and choose “Update Field” (Word) or it will populate automatically on open (Google Docs).

## How to use this guide

This is your companion to the one-page GTM Engineering Program. The one-pager tells you what to do each day; this guide tells you exactly what to study, understand, and build to get there. Every one of the 60 sessions is expanded into seven parts: the objective (what you'll be able to do by the end), why it matters, the core material to learn, the 2026 market reality to keep in mind, a minute-by-minute plan for your build hour, the tips and common mistakes to avoid, and resources to go deeper.

You can open this document and work straight through it, one session per day. Read the 'What you'll learn' blocks as your study notes — they hold the concepts, distinctions, and examples in plain language. Then follow the timed plan and do the build yourself; reading it is not enough, the skill is in the doing. Aim for roughly one focused hour a day over 13 weeks. The Friday sessions each produce a portfolio deliverable; those are highlighted so you never lose the through-line.

The three rules that hold the whole program together

One company. every project targets one company you adopt on Day 5, so by Week 12 the portfolio tells one coherent story instead of thirteen disconnected exercises.

One portfolio. hiring in this field is portfolio-based — there is no certificate that matters. You must finish with 3–5 shipped workflows, each with a measurable outcome. Protect the Friday ships above everything.

Seven layers. named tools change every 6–12 months, but the seven layers do not. Learn the layer principle first, the tool second. If a tool named here has changed by the time you reach it, the layer it serves has not.

## The 2026 market snapshot (read this in Week 1)

Here is the context up front, so you understand why the role is worth 13 weeks of your life. These are the numbers and facts as of mid-2026 — verify the live figures yourself before you lean on them, because this niche moves fast.

Clay coined the title 'GTM engineer' in 2023. In under three years it went from a made-up job title to one of the fastest-growing categories in B2B SaaS, with thousands of open roles at any given time.

The median GTM engineer salary in 2026 sits around $127K; senior roles at strong companies exceed $250K in total comp. The single biggest pay lever is technical skill — engineers comfortable with SQL, Python, APIs and Claude Code out-earn pure no-code operators by roughly $50K.

The average posting wants ~4 years of experience and screens with a paid trial project, not a resume. This is why the portfolio is everything: a candidate who can build a lead list live and explain waterfall logic beats a candidate with a longer CV.

The economics that created the role: a modern B2B team runs 14+ GTM tools, and the value of enriching and acting on a signal within minutes now dwarfs untargeted volume. One GTM engineer plus two SDRs routinely outperforms five SDRs with no builder — because the builder manufactures the pipeline the closers convert.

Most GTM engineering jobs are not titled 'GTM Engineer.' Adjacent titles — growth engineer, RevOps, marketing/sales ops, founding GTM, automation specialist — hide the same work. Series A–B startups are the most active hirers, and many teams buy the capability as an agency (a 'Claygency') before hiring in-house.

## The seven-layer model (the spine of the program)

Everything in this program is organized around seven layers. Data flows down through them: strangers enter at the top of the funnel, and each layer does one job in turning them into pipeline. Learn one layer at a time, bottom to top. You should be able to redraw this from memory by the end of Week 1, and again — fully specified for your own company — in Week 13.

L1  Data & Sourcing — where prospects come from — databases, LinkedIn, scraping. The core tension is coverage vs. accuracy. Tools: Apollo, ZoomInfo, Sales Navigator.

L2  Enrichment — turning a name into verified emails, firmographics, tech stack and context — using waterfalls that chain providers. Tool: Clay.

L3  Signals & Intent — the 'why now' — funding, hiring, job changes, website visits, product usage. Tools: RB2B, RSS, scrapers.

L4  Orchestration — the connective tissue — webhooks and workflows that move data between every tool. Tools: n8n, Make, raw APIs.

L5  Execution — the outreach itself — deliverable email plus LinkedIn, personalized at scale. Tools: Smartlead/Instantly, HeyReach.

L6  CRM & Reporting — the source of truth — routing, scoring, data hygiene, attribution. Tools: HubSpot, Salesforce.

L7  AI & Agents — the multiplier — LLM research and copy, custom scripts, agents that run plays for you. Tools: Claude, Claude Code, MCP.

The most important point about the model: value is destroyed at the handoffs between layers, not inside them. A perfect enrichment (L2) feeding a broken orchestration (L4) produces nothing. Most of a GTM engineer's real job is making the handoffs reliable.

## Week 1 — Foundations — the GTM engineering mindset

What the role is, the revenue system you'll build, and your workspace.

Days 1–5

### D01 · Week 1, Day 1 — What is GTM engineering, really?

Understand the role, why it exists, and how it differs from RevOps, SDR and software engineering.

Objective:  You can define the GTM engineer role in your own words and place it correctly against three adjacent roles.

WHY THIS MATTERS

If you can't articulate what this role is and isn't, they'll drift toward being a 'button-pusher' — someone who operates tools without commercial judgment. The whole program's premise is that judgment plus building is what gets paid. Start by installing a crisp mental model of the job.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What a GTM engineer actually is

A GTM engineer is a hybrid: half commercial thinker, half builder. They design and operate the technical systems that generate pipeline — enrichment workflows, ICP scoring models, outbound automation, signal monitoring, and CRM architecture. The role sits at the intersection of revenue thinking and technical building. The shorthand practitioners use is 'marketers who can build' or 'engineers who care more about moving revenue than writing perfect code.'

The role was coined by Clay in 2023. Originally it was one overwhelmed person doing RevOps, sales support, BDR work, and data analysis at once; the title emerged to name the person who builds revenue systems rather than manually running them. Three forces made it a real, fast-growing category: modern GTM stacks got complex (14+ tools per team), intent data and AI scoring made timely targeted outbound far more valuable than volume, and AI made it possible for one builder to do what a five-person team used to.

How it differs from the three roles it's confused with

Versus RevOps: a RevOps analyst reports on the pipeline — conversion rates, stage velocity, attribution. A GTM engineer builds the infrastructure that generates the pipeline in the first place. RevOps looks backward at what happened; GTM engineering builds forward the machine that makes it happen. Many teams incubate GTM engineering under RevOps, then spin it out.

Versus SDR: an SDR handles conversations and books meetings by working a list. A GTM engineer builds the system that produces the qualified list and fires the right message at the right moment. The 2026 ratio has flipped — one GTM engineer plus two SDRs beats five SDRs with no builder, because the builder manufactures the pipeline.

Versus software engineer: a SWE builds product for end users, optimizes for correctness and maintainability, and works in a codebase. A GTM engineer builds internal revenue plumbing, optimizes for speed-to-pipeline, and works mostly in no-code tools (Clay, n8n) plus light scripting. They care more about a working play shipped this week than elegant code.

The one-sentence definition to land

By the end of the hour, you write your own three-sentence definition. A good target: 'A GTM engineer builds and runs the automated systems that turn strangers into pipeline. They combine commercial judgment about who to target and why, with the technical ability to wire data, enrichment, signals and outreach into one engine. They are measured on pipeline generated, not tools operated.'

2026 MARKET REALITY (KNOW THIS COLD)

Median 2026 salary ~$127K; senior/technical roles $250K+. Technical skill (SQL, Python, APIs, Claude Code) is the biggest pay multiplier.

Clay is the #1 tool in job postings; HubSpot appears in ~52%, Outreach ~49%, Salesforce ~45%. Roughly a third of postings explicitly require coding.

Hiring is portfolio-first and screens with a paid trial project. Nobody will care about a certificate — they'll ask to see something you built.

RUN THE HOUR

0:00–0:20  Read 2–3 role overviews and the salary/market data. Use the 2026 snapshot in this guide plus one current source.

0:20–0:50  Build a comparison table: GTM Engineer vs RevOps vs SDR vs SWE, across focus, core skills, and primary deliverable. Fill it, then discuss.

0:50–1:00  Write your own three-sentence definition of the role and reads it aloud. Push for specificity, not buzzwords.

TIPS & COMMON MISTAKES TO AVOID

The most common wrong answer is 'it's just RevOps' or 'it's an SDR who uses Clay.' The fix is to anchor on the deliverable: build vs. report vs. converse.

Don't fixate on salary. The point of the data is to justify the effort, then move on to the craft.

If you already work in ops or sales, map your current job onto the table — it makes the distinction concrete.

Resources  gofractional / cleanlist / clay.com role guides · the 2026 market snapshot in this guide

### D02 · Week 1, Day 2 — The modern revenue funnel

Map how a stranger becomes revenue and where GTM engineers own the flow.

Objective:  You can draw the full funnel and label exactly where data, enrichment, and outreach plug in.

WHY THIS MATTERS

The funnel is the shared language of every revenue team. A GTM engineer who can't map it can't explain where your system creates value or diagnose where it's leaking. This session gives you the coordinate system they'll use for the rest of the program.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The stages, in order

Walk through the pipeline as a sequence of states a person moves through: unknown → lead → MQL (marketing-qualified lead) → SQL (sales-qualified lead) → opportunity → closed (won or lost). 'Unknown' is everyone in the market who has never touched you. A 'lead' is a known contact. MQL means they've shown enough interest or fit that marketing hands them forward. SQL means sales has accepted them as worth a real conversation. 'Opportunity' means there's an active deal with a dollar value. 'Closed' is the outcome.

Remember that these are not universal — every company draws the lines slightly differently, and part of RevOps/GTM engineering is defining the exact criteria for each transition. But the shape is consistent everywhere.

Where the GTM engineer owns the flow

The GTM engineer's territory is heaviest at the top and left: turning unknowns into qualified, contacted leads. Concretely: sourcing (data layer) populates unknown → lead; enrichment turns thin records into complete, targetable ones; signals decide who moves first and why; execution (email/LinkedIn) makes first contact; and orchestration + CRM make sure a reply routes correctly and nothing is dropped.

The key teaching point: outbound GTM engineering manufactures the top of the funnel that inbound marketing hopes will arrive on its own. Where a demand-gen marketer buys ads to fill 'unknown → lead,' the GTM engineer builds a targeted machine that does the same thing with data and signals instead of ad spend.

Where value leaks

For every stage transition, ask: what data has to be correct, and what has to happen automatically, for a person to move to the next stage? A bad email address leaks at first contact. A missing enrichment field leaks personalization. A broken CRM handoff means a hot reply sits unread. Leaks compound — a 50% loss at each of four stages leaves you 6% of what you started with.

2026 MARKET REALITY (KNOW THIS COLD)

In 2026 the highest-leverage part of the funnel is the join between signals and execution: detecting a 'why now' event and acting within minutes is where modern outbound wins.

AI now writes a large share of the copy and does the research, but the funnel logic — who qualifies and when — is still human-defined judgment. That judgment is the durable skill.

RUN THE HOUR

0:00–0:25  Learn the stages and the transition criteria. Draw the funnel as you go.

0:25–0:55  Draw a full funnel diagram and label where data, enrichment, signals, and outreach plug in for your (soon-to-be-adopted) company type.

0:55–1:00  Note the one stage they understand least — this becomes something to revisit later.

TIPS & COMMON MISTAKES TO AVOID

Learners often conflate MQL and SQL. Anchor it: MQL = marketing thinks they're interested; SQL = sales agrees they're worth time.

Keep the diagram physical or on a whiteboard. The goal is a mental model, not a pretty artifact.

Resources  Any reputable B2B funnel primer + your own diagram

### D03 · Week 1, Day 3 — The seven-layer mental model

Internalize the stack this whole program is built around.

Objective:  You can redraw all seven layers from memory and name two tools and one failure mode per layer.

WHY THIS MATTERS

This model is the spine of the program. Learners will build one layer per week; if you hold the whole map in your head, each week's work has an obvious place to live. This is also the exact structure of the Week 13 capstone, so time spent here pays off twice.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The seven layers, and the one idea that connects them

Revisit the layers from the front-matter reference: L1 Data & Sourcing, L2 Enrichment, L3 Signals & Intent, L4 Orchestration, L5 Execution, L6 CRM & Reporting, L7 AI & Agents. Each layer does exactly one job. Data flows down through them, top to bottom, as a stranger becomes pipeline.

The single most important idea, and the thing that distinguishes a real engineer: value is created inside layers but destroyed at the handoffs between them. A perfect enriched list that never reaches the sequencer is worthless. Most of the job is making handoffs reliable — which is why orchestration (L4) is the connective tissue the whole thing depends on.

The failure mode per layer (this is what makes it stick)

Learn each layer by its characteristic failure. L1: you source the wrong companies, so everything downstream is precise garbage. L2: you enrich with guessed emails, so you bounce and burn your domain. L3: your signals are stale, so you reach out about something that happened three months ago. L4: a webhook silently fails and half your leads never move. L5: your copy is generic or your domain isn't warmed, so nothing lands. L6: your CRM is a swamp of duplicates, so routing and reporting lie to you. L7: your AI writes confident nonsense with no quality control, at scale.

Making you name the failure per layer forces them to understand what each layer is for, not just which tool sits there.

2026 MARKET REALITY (KNOW THIS COLD)

The stack evolves every 6–12 months, but Clay as the L2/orchestration center has held since 2023. Treat any tool name as replaceable and the layer as permanent.

L7 (AI & agents) is the layer growing fastest and the one that most separates high earners. It's deliberately taught last, once you knows what to automate.

RUN THE HOUR

0:00–0:20  Re-read the seven layers together from the front-matter reference.

0:20–0:55  Redraw the stack from memory. Under each layer, list two tools and describe one broken-handoff failure it would cause.

0:55–1:00  Save the diagram. Tell you explicitly: you will rebuild this, fully specified for your own company, in Week 13.

TIPS & COMMON MISTAKES TO AVOID

Don't just copy the reference. The value is in reconstructing it from memory — that's what proves internalization.

If you list a tool in the wrong layer (e.g. puts HubSpot in Execution), treat it as a prompt to learn what each layer's job actually is.

Resources  The seven-layer reference in this guide + any current stack breakdown (e.g. gtmai.nl)

### D04 · Week 1, Day 4 — Stand up your workspace

Create free accounts for the core tools so you can build from Day 15 on.

Objective:  You have working free-tier accounts for Clay, Apollo, HubSpot, Google, and Claude, and know where the key buttons live.

WHY THIS MATTERS

Nothing kills momentum like discovering on build day that an account isn't set up or a free tier ran out. This session removes that friction now. It's mostly administrative, but a smooth workspace is what lets the rest of the program be hands-on.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The core free-tier stack and what each is for

Clay — the gravitational center of the stack: enrichment, research, and orchestration in a spreadsheet. The free tier gives unlimited seats and tables, multi-provider waterfalls, Claygent, and the Clay Sequencer, but caps tables at 200 rows and gives a small monthly credit allowance. That's plenty to learn on.

Apollo.io — contact database plus basic sequencing, with the fastest list-to-launch and a generous free tier. HubSpot — a genuinely free CRM that becomes your source of truth. Google account — needed for OAuth, Sheets, and connecting tools. Claude — the AI copilot for research, copy, and writing code you don't know yet.

The Clay pricing model you must understand now

Since Clay's March 2026 overhaul there are two separate meters: Data Credits (spent on enrichment lookups) and Actions (spent on platform operations). The free plan includes a small monthly allotment of each. Crucially, credits are charged per attempt, not per success — a failed lookup still costs. This is the single fact that most surprises new users and the reason Week 5 spends a whole week on cost efficiency. Plant that flag today.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's free tier realistically fully enriches only a handful of contacts before the monthly Data Credits run out — enough to learn, not to run production. Budget credits like a scarce resource from Day 1.

Apollo's and Lusha's free tiers are more generous for basic enrichment, which is why Apollo is a good first sourcing tool before you graduate to Clay waterfalls.

RUN THE HOUR

0:00–0:45  Sign up on free tiers: Clay, Apollo, HubSpot CRM, a Google account, and Claude. Verify each logs in.

0:45–1:00  Open each tool, click around for three minutes, and note where 'import data' and 'create table/list' live. Screenshot each for reference.

TIPS & COMMON MISTAKES TO AVOID

Use a dedicated email (or Google account) for these tools so credits and domains don't tangle with personal accounts.

Don't spend any Clay credits today — just create the account and look around. Credits are for Week 4 onward.

If self-hosting n8n later, note that today is not the day — n8n stands up in Week 10.

Resources  clay.com · apollo.io · hubspot.com · claude.ai

### D05 · Week 1, Day 5 — Adopt your company + reflect

Pick the one B2B company you'll build for all program long.

Objective:  You have chosen a company and written a one-page profile of it — the first portfolio deliverable.

WHY THIS MATTERS

This is the single most important structural decision in the program. Every subsequent project targets this company, so by Week 13 the portfolio reads as one coherent story: 'here is a complete GTM system I designed and built for a real ICP.' A vague or badly chosen company makes the whole portfolio mushy.

WHAT YOU'LL LEARN — THE CORE MATERIAL

How to choose well

Three valid options: your own employer (best if you have one — the work becomes immediately useful), a real startup they admire (good for realism and public data), or an invented company with a clear, specific product (fine, but force specificity). The company must be B2B and must sell something with an identifiable buyer. 'A SaaS tool' is too vague; 'a scheduling tool for dental clinics with 2–10 chairs' is buildable.

The test of a good choice: can you name who buys it, what problem it solves, and roughly what it costs? If not, the ICP work in Week 2 will be impossible.

The one-pager (deliverable #1)

The one-pager captures: what the company sells, who buys it (role and company type), the problem it solves, and a rough price point. This is deliberately short — one page — because it's a foundation, not a finished artifact. It becomes the input to Week 2's ICP and strategy work.

Frame this as the start of a portfolio document (Notion page or doc) that will accumulate all 13 deliverables. Every Friday adds to it. By Day 64 it's the thing that gets them hired.

2026 MARKET REALITY (KNOW THIS COLD)

Because hiring uses paid trial projects, a portfolio built around one realistic company is close to the exact artifact a hiring manager will ask for. Choosing a real, gettable-data company makes later signal and enrichment work far easier.

Series A–B startups are the most active hirers — picking a company that resembles one (clear product, growing, sells to other businesses) makes the portfolio maximally relevant.

RUN THE HOUR

0:00–0:15  Choose the company. Pressure-test your choice and drop it if it fails the 'who buys it / what problem / what price' test.

0:15–0:55  Write the one-pager: product, buyer, problem, rough price point.

0:55–1:00  Start the portfolio document and drop the one-pager in as deliverable #1.

TIPS & COMMON MISTAKES TO AVOID

Resist the urge to keep your options open with two companies. One company, all program long. Commitment is the point.

If you pick something wildly complex (multi-product enterprise), narrow them to a single product line and buyer.

Resources  clay.com company-profile examples · your own portfolio doc

◆  Portfolio deliverable #1: Company one-pager

## Week 2 — GTM strategy & business acumen

The commercial thinking that separates engineers from tool operators.

Days 6–10

### D06 · Week 2, Day 6 — Defining an ICP

Learn to specify an Ideal Customer Profile with firmographics, technographics and personas.

Objective:  You can write a first-pass ICP for your company and identify which attributes need data to confirm.

WHY THIS MATTERS

The ICP is the specification the entire machine is built against. A sloppy ICP means precise garbage — you'll enrich, personalize and send to the wrong people flawlessly. Everything downstream inherits the quality of this definition.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The components of an ICP

An ICP has three layers. Firmographics: company size (headcount, revenue), industry, geography, funding stage. Technographics: what's in their tech stack (a company using a competitor, or a complementary tool, is often a strong signal). Persona: the specific buyer role you're reaching — their title, what they own, what they're measured on, and what pain your product removes from your day.

Distinguish the ICP (the ideal company) from the persona (the ideal person inside it). You target a company because it fits firmo/technographics, then you reach specific personas within it. Both are needed: a great-fit company with no reachable buyer is a dead end.

Tight beats broad

The instinct is to define the ICP broadly to maximize the market. Learn the opposite: a narrow ICP makes every downstream step better. Narrow means you can write copy that names your exact situation, pick signals specific to them, and score fit cleanly. You can always widen later. Generic tools leave bad-fit companies in the list; a sharp ICP is what keeps the list clean.

A good first-pass ICP reads like a sentence you could hand to someone and they'd know exactly who to look for: 'Seed-to-Series-B B2B SaaS companies, 20–150 employees, US-based, using HubSpot, where we sell to the Head of Growth or first RevOps hire.'

Which attributes need data to confirm

The final move: for each attribute, ask whether it's observable in a database. Headcount and industry are easy (Apollo, Clay). Tech stack needs a technographic source or scraping. Funding stage needs a signal source. Whether they have a 'first RevOps hire' might need Claygent research. Listing which attributes need data — and how hard each is to get — is the bridge into the data layer in Week 3.

2026 MARKET REALITY (KNOW THIS COLD)

In interviews, candidates are asked to explain ICP and build a targeted account list live. Getting the ICP framework crisp here is directly job-relevant.

Clay's whole value proposition assumes a sharp ICP: waterfalls and scoring only pay off when you know precisely who qualifies.

RUN THE HOUR

0:00–0:25  Learn the ICP components: firmographics, technographics, persona. Learn the 'tight beats broad' argument.

0:25–0:55  Draft a first-pass ICP for your adopted company as a single specific sentence plus a persona description.

0:55–1:00  List three attributes that will need data to confirm, noting how hard each looks to get.

TIPS & COMMON MISTAKES TO AVOID

The classic mistake is an ICP so broad it's useless ('B2B companies that need more sales'). Force yourself to use numbers and named attributes.

Write the persona as a person with a job and a bad day, not a title. It makes copywriting far easier in Week 8.

Resources  clay.com ICP + targeted-account guides

### D07 · Week 2, Day 7 — TAM / SAM / SOM (SOM-Conditions that affect getting deals from SAM)

Size a market and understand why segmentation drives everything downstream.

Objective:  You can estimate a rough TAM for your ICP, split it into 2–3 segments, and justify which to attack first.

WHY THIS MATTERS

Sizing forces a reality check: is this ICP big enough to build a real motion around, and small enough to be specific? Segmentation is the practical output — it decides which slice you build the first campaign for, and campaigns are always built per-segment, never for 'everyone.'

WHAT YOU'LL LEARN — THE CORE MATERIAL

The three numbers

TAM (Total Addressable Market): everyone who could theoretically buy — the whole universe that fits the ICP. SAM (Serviceable Addressable Market): the portion you can actually reach and serve given your geography, product, and channels. SOM (Serviceable Obtainable Market): the slice you can realistically win in a given period. Each is a subset of the one before.

For a GTM engineer, the useful move is not a precise financial TAM but a countable one: how many companies match the ICP? You can sanity-check this directly in Apollo or Sales Navigator by applying the ICP filters and reading the result count. If the ICP returns 40 companies, the motion is too narrow; if it returns 400,000, it's too broad to personalize.

Why segmentation drives everything

You never build a campaign for the whole TAM. You split it into 2–3 segments — by size band, industry vertical, tech stack, or use case — because each segment has a different pain and therefore a different message. Segmentation is what makes 'personalization at scale' possible: you write one sharp message per segment, not one bland message for all.

Picking which segment to attack first is a judgment call: prefer the segment with the clearest pain, the easiest-to-detect signals, and reachable buyers. The first segment is where you will build every subsequent deliverable, so choosing well matters.

2026 MARKET REALITY (KNOW THIS COLD)

Modern practice sizes markets by running the actual ICP filters in Apollo/Sales Nav and reading the count — a live, checkable number beats a slide-deck estimate.

Signals-first outbound rewards narrow segments: the tighter the segment, the more specific the 'why now' event you can build a play around.

RUN THE HOUR

0:00–0:25  Learn TAM/SAM/SOM and the logic of segmentation. Work out how to get a countable TAM from Apollo/Sales Nav filters.

0:25–0:55  Estimate a rough TAM for the ICP and split it into 2–3 segments with a one-line rationale each.

0:55–1:00  Pick the segment to attack first and write why (pain clarity, signal availability, reachability).

TIPS & COMMON MISTAKES TO AVOID

Don't get lost in financial TAM math. The countable 'how many companies' number is what's actionable.

If every segment looks equally good, the ICP is probably too vague — go back and sharpen it.

Resources  Any TAM primer + LinkedIn/Apollo filters to sanity-check size

### D08 · Week 2, Day 8 — Buying signals, intent & triggers

Understand the 'why now' — the events that make outreach warm instead of cold.

Objective:  You can list five signals that would make your product suddenly relevant and rank them by how easy each is to detect.

WHY THIS MATTERS

The difference between cold outreach and warm outreach is a reason. Signals are that reason — the events that mean 'this account needs you this week, not in the abstract.' Signal-based outbound is the core of the modern motion and the reason the whole Week 9 exists. Introduce the taxonomy now so it threads through everything.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The three signal types

First-party signals: activity on your own properties — a form fill, a demo request, a pricing-page visit, a reply. These are the warmest because the person acted toward you. Product-usage signals: for products with a free tier or PLG motion, what a user does inside the product (hit a limit, invited a teammate, used a key feature). Third-party signals: public events about the account — funding rounds, hiring for a relevant role, a job change into a buying seat, a tech-stack change, a news mention.

Learn that warmth roughly tracks the type: first-party is warmest, product-usage next, third-party coldest but most abundant. The art is combining a third-party signal ('they just raised a Series A') with fit ('and they match our ICP') to manufacture a warm-enough reason to reach out today.

Signals for your company

Brainstorm: what has to be true about an account for our product to be urgently relevant right now? For a compliance tool: they just hit a headcount that triggers a regulation. For a sales tool: they just posted three SDR job openings. For a data tool: they just switched CRMs. Five concrete signals, tied to the specific product.

Ranking by detectability

Every signal has a detection cost. 'They visited our pricing page' needs a visitor-ID tool. 'They raised funding' is in news/RSS. 'They're hiring SDRs' is on job boards. 'They use a competitor' needs technographic data or scraping. Ranking signals by how easy each is to detect tells you which plays to build first — always start with the highest-intent signal that's cheapest to detect.

2026 MARKET REALITY (KNOW THIS COLD)

The winning move in 2026 is speed: the team that enriches and acts on a signal within minutes beats the team sending untargeted volume. Signal detection + fast response is the whole game.

Clay now offers Signals natively (job changes, promotions, hiring, news), and Signals are priced separately (roughly one credit per five records) — cheap enough to run broadly.

RUN THE HOUR

0:00–0:25  Learn the three signal types and the warmth-by-type idea.

0:25–0:55  List five signals that would mean the product is suddenly relevant to an account.

0:55–1:00  Rank the five by how easy each is to detect, and note the detection source for each.

TIPS & COMMON MISTAKES TO AVOID

Learners often list generic signals ('they're a big company'). Push for events — something that changed recently, with a date.

Tie each signal back to the message it would justify. A signal you can't act on with a specific line isn't useful yet.

Resources  unifygtm signal-based selling explainer + intent-data primers

### D09 · Week 2, Day 9 — Offer & message-market fit

Turn 'we do X' into a reason to reply.

Objective:  You can write one sharp one-liner offer per segment and gut-check whether a busy buyer would care in the first five words.

WHY THIS MATTERS

The best-targeted, best-timed outreach still fails if the offer is a feature dump. Message-market fit — saying the thing the buyer already cares about — is what converts a well-built list into replies. Engineers who skip this ship beautiful machines that get ignored.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Value prop → pain → proof

Learn the three-part structure of a compelling offer. Value prop: the outcome you create, in the buyer's terms (not your feature). Pain: the specific problem the buyer feels that the outcome removes. Proof: the reason to believe you — a number, a comparable customer, a concrete result. Weak outreach leads with the value prop as a feature ('we have an AI enrichment engine'); strong outreach leads with the pain and the outcome ('your SDRs waste half your week researching accounts — here's how three similar teams got that time back').

Message-market fit means the message matches what the segment already believes is a problem. You're not convincing them a problem exists; you're showing you understand a problem they already have and can remove it.

One offer per segment

Because different segments have different pains (from Day 7's segmentation), you write a different one-liner per segment. The enterprise segment might care about compliance and control; the startup segment about speed and cost. Same product, different framing. This is the practical reason segmentation matters.

The five-word gut check

The final discipline: would a busy buyer care about this in the first five words? Buyers skim. If the first line is about you ('We're a platform that...'), they're gone. If it names your situation ('Scaling SDR hiring is expensive...'), they read on. Rewrite until the opening earns the second line.

2026 MARKET REALITY (KNOW THIS COLD)

With AI writing most first drafts in 2026, the scarce skill is judgment about what to say, not the ability to produce words. A human-defined sharp offer is what makes AI-generated copy land.

Reply-rate benchmarks reward relevance over volume: a tight offer to a small, well-fit segment beats a generic blast to a large one.

RUN THE HOUR

0:00–0:25  Learn value prop → pain → proof and the idea of message-market fit.

0:25–0:55  Write one sharp one-liner offer per segment (2–3 total).

0:55–1:00  Gut-check each: would a busy buyer care in the first five words? Rewrite until yes.

TIPS & COMMON MISTAKES TO AVOID

Ban feature-first openers. Every offer must start from the buyer's world, not the product's capabilities.

If you can't name the proof, that's a real gap — note it; it'll shape what social proof they gather for real campaigns.

Resources  clay.com offer-validation guide

### D10 · Week 2, Day 10 — Ship: the GTM strategy brief

Package your thinking into a brief you'll build against.

Objective:  You produce a one-page strategy brief: ICP + top segment + 3 target signals + one-liner offer + persona.

WHY THIS MATTERS

This brief is the specification for every technical build that follows. It converts a week of commercial thinking into a single artifact you (and any teammate) can build against. In a real job, this is the document a GTM engineer writes before touching a tool — and the thing that separates them from someone who just starts clicking.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Assembling the brief

The brief is a synthesis, not new work — it pulls together the week's outputs into one page: the ICP (Day 6), the top segment chosen from the sizing (Day 7), three target signals ranked by detectability (Day 8), the one-liner offer for that segment (Day 9), and the persona you'll reach. One page, tight, readable at a glance.

The test of a good brief: could a competent stranger read it and know exactly who to source, what data to gather, what event to watch for, and what to say? If yes, it's a real spec. If it needs you to explain it verbally, it's not done.

Why this is a portfolio piece

This brief demonstrates the commercial judgment that hiring managers screen for — the thing that separates engineers from button-pushers. It shows you can think about who and why before how. Every subsequent deliverable references it, so it's also the anchor of the portfolio's narrative.

2026 MARKET REALITY (KNOW THIS COLD)

This brief is close to the artifact a paid trial project would ask for. Building it well now is direct interview preparation.

In real teams, the strategy brief is what a GTM engineer brings to a founder for approval before building — it's how you avoid building the wrong machine efficiently.

RUN THE HOUR

0:00–0:50  Assemble the one-page brief: ICP + top segment + 3 target signals + one-liner offer + persona.

0:50–1:00  Add it to the portfolio as deliverable #2.

TIPS & COMMON MISTAKES TO AVOID

Keep it to one page. The discipline of fitting it on a page forces the thinking to be sharp.

Read it against the 'competent stranger' test before calling it done.

Resources  The week's four outputs, synthesized

◆  Portfolio deliverable #2: GTM strategy brief

## Week 3 — The data layer — sourcing companies & people

Where GTM data comes from and how to source targeted lists.

Days 11–15

### D11 · Week 3, Day 11 — The data landscape

Map the sources: databases, scraping, and LinkedIn — and the coverage vs. accuracy tradeoff.

Objective:  You can explain where each data source is strong and weak, and choose a starting source for your ICP with a reason.

WHY THIS MATTERS

Every downstream layer inherits the quality of the data layer. If you understand the tradeoffs between sources, they'll make deliberate choices instead of defaulting to whatever tool they saw first. This is also the conceptual foundation for waterfalls in Week 5.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The three source types

Databases (Apollo, ZoomInfo): large pre-built stores of company and contact data. Strength: instant coverage, easy filtering, fast list-to-launch. Weakness: data decays — people change jobs, so a database is always somewhat stale, and coverage varies by region and company size. ZoomInfo skews toward enterprise/US accuracy; Apollo is broader and cheaper with more variable quality.

LinkedIn / Sales Navigator: the most current source of who-works-where, because people maintain your own profiles. Strength: freshness and rich filtering (boolean search, seniority, function). Weakness: you can't easily export at scale within terms of service, and it gives you the person, not their verified email. It's a sourcing and verification layer, not an enrichment engine.

Scraping: pulling data directly from websites (company sites, directories, job boards). Strength: reaches data no database has — the specific, fresh, niche stuff. Weakness: brittle, effortful, and needs cleanup. In modern practice this is increasingly done by AI agents (Claygent) rather than hand-built scrapers.

Coverage vs. accuracy is the eternal tradeoff

The core tension: broad sources have high coverage but lower accuracy; narrow/fresh sources have high accuracy but lower coverage. No single source is best. This is exactly why waterfalls exist (Week 5) — you chain sources to get both. For now, you just needs to pick a sensible starting source for your ICP and know its blind spots.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's waterfall approach reaches 95%+ coverage precisely by chaining 100+ providers — the industry has largely accepted that no single database is enough.

For most ICPs in 2026, the practical starting move is Apollo for breadth plus Sales Navigator to verify and fill senior contacts, then Clay to enrich and waterfall.

RUN THE HOUR

0:00–0:30  Learn how databases, Sales Nav, and scraping each source data, and where each is strong/weak.

0:30–0:55  For the ICP, decide which source to start with and write why.

0:55–1:00  Note the expected coverage gaps of that starting choice.

TIPS & COMMON MISTAKES TO AVOID

Learners assume one tool 'has all the data.' Disabuse this early — it's the mental block that waterfalls solve.

Tie the choice back to your ICP: an enterprise-US ICP and a global-SMB ICP call for different starting sources.

Resources  lagrowthmachine GTM stack + data-layer breakdowns

### D12 · Week 3, Day 12 — Apollo deep dive

Use filters to build precise company and people lists.

Objective:  You can build a saved Apollo search matching your ICP, refine it until clean, and eyeball export quality.

WHY THIS MATTERS

Apollo is usually the fastest path from ICP to a real list, and the free tier is generous enough to learn on. Getting fluent with filters is a concrete, job-relevant skill — 'build me a list of these companies' is a task you will do constantly.

WHAT YOU'LL LEARN — THE CORE MATERIAL

How Apollo's filters map to the ICP

Apollo lets you filter companies and people separately, then combine. Company filters: employee count, industry, location, revenue, technologies used, funding. People filters: title, seniority, department, and keywords. The workflow is to translate the ICP sentence into filter settings, then read the result count as a live TAM check.

Learn the iterative loop: apply filters, look at the results, spot the mismatches (a wrong-industry company, a title that isn't really the buyer), tighten the filters, repeat. A clean list is made, not found — the refinement is the skill.

Reading data quality

After building a search, export a small sample and eyeball it. Look for: verified vs. unverified emails, obviously wrong titles, companies that slipped through the filter, and blank fields. This teaches the habit of never trusting a list at face value — a habit that becomes 'data quality bar' on Day 14.

2026 MARKET REALITY (KNOW THIS COLD)

Apollo remains a strong first tool because of its free-tier generosity and speed; many workflows still start in Apollo and finish enrichment in Clay.

A live-build exercise like this ('build a clean ICP list in Apollo') mirrors exactly what a paid trial project asks candidates to do.

RUN THE HOUR

0:00–0:15  Tour Apollo's company and people filters; map them to the ICP sentence.

0:15–0:55  Build a saved search matching the ICP; refine filters until results look clean.

0:55–1:00  Export a small sample and eyeball data quality — note what looks off.

TIPS & COMMON MISTAKES TO AVOID

Watch free-tier export limits — Export a small sample, not the whole list, to conserve quota.

The most common error is too-loose filters producing a huge, noisy list. Push for a tight, clean 50–100 before celebrating volume.

Resources  apollo.io in-app search + help docs

### D13 · Week 3, Day 13 — LinkedIn Sales Navigator

Master advanced filters and boolean search to build account lists.

Objective:  You can build a Sales Nav account list for your top segment using boolean search and compare it to your Apollo list.

WHY THIS MATTERS

Sales Navigator is the freshest source of who-works-where and the best tool for precise account and people targeting. Boolean search is a transferable skill that shows up across the whole stack. Comparing Sales Nav to Apollo teaches the coverage-vs-accuracy lesson concretely rather than abstractly.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Sales Nav filters and boolean operators

Sales Navigator offers deep filters: seniority level, function, company headcount, geography, industry, years in role, and more. The power tool is boolean search in keyword fields: AND (both terms), OR (either term), NOT (exclude), and quotes for exact phrases. For example, ('Head of Growth' OR 'VP Marketing') NOT 'assistant' targets the buyer while excluding the noise.

Learn that Sales Nav is where you build the account list and identify the right people, but it deliberately doesn't hand you verified emails — that's the enrichment layer's job. So Sales Nav feeds names into Clay, which waterfalls to find the email.

Comparing to Apollo

Building the same segment in both tools reveals the tradeoff live. Sales Nav often has fresher titles and better senior coverage; Apollo often has more contacts with emails already attached. Neither is 'right' — which is exactly why the enrichment layer exists to reconcile them. This comparison is the aha that motivates waterfalls.

2026 MARKET REALITY (KNOW THIS COLD)

Sales Nav data freshness is a genuine edge because profiles are self-maintained; it's often the best source for verifying that a database's contact still holds the role.

Boolean fluency transfers directly to LinkedIn automation tools (HeyReach) in Week 8 and to search-based signal detection in Week 9.

RUN THE HOUR

0:00–0:20  Learn Sales Nav filters and boolean operators (AND/OR/NOT, quotes).

0:20–0:55  Build an account list for the top segment (use the free trial if needed).

0:55–1:00  Compare its results to the Apollo list from Day 12 — note the differences.

TIPS & COMMON MISTAKES TO AVOID

If no Sales Nav trial is available, learn the boolean logic on paper and demo on a free LinkedIn search — the skill is the logic.

Remember that Sales Nav gives people, not emails. Learners often expect exportable emails and are confused when there aren't any.

Resources  LinkedIn Sales Navigator (free trial) + a boolean cheatsheet

### D14 · Week 3, Day 14 — Data quality fundamentals

Understand why bad data silently breaks every downstream layer.

Objective:  You can distinguish verified vs. guessed emails and catch-all domains, and can write your own data-quality bar.

WHY THIS MATTERS

Bad data doesn't announce itself — it silently poisons everything. A guessed email bounces, a bounce hurts your domain reputation, a hurt domain sends your good emails to spam. Learners who internalize a data-quality bar now avoid the single most common way beginners destroy your own campaigns.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Verified vs. guessed emails, and catch-all domains

A verified email has been checked (via SMTP or a verification provider) and is very likely to deliver. A guessed email is pattern-generated (firstname.lastname@company.com) and may or may not exist. A catch-all domain accepts mail to any address, so verification can't confirm a specific mailbox exists — these are risky because they look valid but may bounce or dead-end. Treat catch-alls as a separate, lower-confidence bucket, not as verified.

Bounce rate is the consequence metric. In 2026 the hard ceiling from Gmail/Yahoo/Microsoft is a bounce rate under 2%; cross it and you get throttled or rejected. Because verification isn't free and isn't perfect, there's always a small residual bounce risk — which is why list hygiene matters before every send.

Why it breaks everything downstream

Trace the cascade: a bad email → a bounce → damaged sender reputation → your legitimate emails land in spam → your whole campaign underperforms → you blame the copy when the real cause was data three layers up. This is the silent failure mode of L1/L2. The defense is a quality bar applied before data ever reaches the execution layer.

Writing a data-quality bar

The your personal data-quality bar is a short standard: e.g. 'only send to verified emails; treat catch-alls as a separate low-priority segment; never send to a row with a missing company or title; re-verify anything older than 90 days.' This becomes a reusable rule they apply to every list for the rest of the program.

2026 MARKET REALITY (KNOW THIS COLD)

2026 enforcement is unforgiving: non-compliant or high-bounce mail is now rejected outright (a hard bounce), not just filtered to spam. A clean list is now a deliverability requirement, not a nicety.

Cross-verification (waterfalling verification providers) reliably pulls bounce rates from 5–8% down to 1–2%. The tiny per-record cost pays back many times over in retained reputation.

RUN THE HOUR

0:00–0:30  Learn verified vs. guessed emails, catch-all domains, bounce rates, and the ~2% bounce ceiling.

0:30–0:55  Inspect the sample list from Days 12–13; flag rows with missing or risky data.

0:55–1:00  Write a personal data-quality bar as a short reusable standard.

TIPS & COMMON MISTAKES TO AVOID

This is the session that prevents you from burning domains later. Give it real weight — it's not a formality.

Show a real catch-all example so you can recognize the pattern; it's the trap that catches beginners most.

Resources  instantly / clay deliverability + data-quality benchmarks

### D15 · Week 3, Day 15 — Ship: a 50-account target list

Produce a clean, ICP-matched list of accounts + key contacts.

Objective:  You ship a deduped, sanity-checked list of ~50 accounts with key personas, sourced from Apollo/Sales Nav.

WHY THIS MATTERS

This is the first tangible asset the machine will run on — real accounts and contacts matching the strategy brief. It's also the input for every Clay exercise in Weeks 4–6. A clean list here makes the next three weeks smooth; a messy one makes them painful.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Assembling the list

Pull ~100 accounts matching the ICP and top segment, with the key persona contact(s) for each, from Apollo and/or Sales Nav. The list should have consistent columns (company, domain, contact name, title, LinkedIn URL, and email where available). Apply the Day 14 quality bar as you build.

Two disciplines make this a real deliverable: dedup (no company appears twice, no contact duplicated) and sanity-check (spot-read 10–15 rows to confirm they actually match the ICP — right size, right industry, plausible buyer). 100 clean rows beats 500 noisy ones.

Why 100

100 is deliberately small: big enough to be a real campaign, small enough to inspect by hand and enrich on free tiers without exhausting credits. Learn that starting small and clean is a professional habit — you validate the machine on a controlled list before scaling.

2026 MARKET REALITY (KNOW THIS COLD)

'Build a clean 100-account list from scratch' is one of the most common live exercises in GTM engineer interviews. This deliverable is literal interview practice.

Keeping the list at ~100 also respects Clay free-tier limits (tables cap at 200 rows and Data Credits are scarce), so it flows straight into Week 4 without a paywall.

RUN THE HOUR

0:00–0:50  Assemble ~100 accounts and key personas into a spreadsheet, sourced from Apollo/Sales Nav, deduped and sanity-checked.

0:50–1:00  Add it to the portfolio as deliverable #3.

TIPS & COMMON MISTAKES TO AVOID

Enforce dedup and the quality bar — this is where the professional habit forms. A dirty list here compounds into wasted credits in Week 4.

Keep the column structure clean and consistent; it becomes the import schema for Clay on Day 17.

Resources  The Apollo/Sales Nav lists from this week + the Day 14 quality bar

◆  Portfolio deliverable #3: Target account list

## Week 4 — Clay fundamentals

Get fluent in the tool at the center of the entire GTM stack.

Days 16–20

### D16 · Week 4, Day 16 — Clay orientation

Learn the grid, tables, and how Clay thinks about data.

Objective:  You can navigate Clay's interface, create a table, add rows, and articulate the row/column mental model.

WHY THIS MATTERS

Clay is the center of the entire stack and the default training ground for the whole skillset — practitioners say 100+ hours in Clay is a good proxy for technical readiness. Everything in Weeks 4–6 builds on a clear grasp of how Clay thinks. Get the mental model right on Day 1 and the rest compounds.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The core mental model: a programmable spreadsheet

Clay looks like a spreadsheet but thinks like a program. Each row is a record (a company or a person). Each column is an operation: it can hold static data, call a data provider to enrich, run an AI prompt (Claygent), apply a formula, or hit an integration. You build a workflow by chaining columns left to right — the output of one column feeds the next. This 'building block' feel, where you can see the pieces assemble across the row, is exactly why Clay is the best place to learn the thinking patterns of the role.

The critical shift from a normal spreadsheet: columns aren't just values, they're actions that cost credits and can succeed or fail per row. Understanding that a column is a live operation — not a static cell — is the whole conceptual leap.

Tables, views, and how data enters

A table holds records. You get data in by importing (CSV, Apollo/LinkedIn sources) or by adding rows manually. Views let you filter and slice the same table without duplicating it. Spend the hour clicking: create a table, add a few manual rows, and note what surprises you about the interface — the surprises are usually the places the mental model needs adjusting.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's free tier (unlimited seats/tables, 200-row cap, waterfalls, Claygent, Sequencer) is ideal for orientation; you won't spend credits just clicking around.

The 'programmable table' framing is why Clay reframed GTM as something you build, test and improve — the same mindset the whole role is built on.

RUN THE HOUR

0:00–0:35  Work through Clay University's 'Clay 101' intro lessons.

0:35–0:55  Create the first table and add a few manual rows.

0:55–1:00  Note three things about the interface that surprised you.

TIPS & COMMON MISTAKES TO AVOID

Reinforce 'column = action, not just value' relentlessly this week — it's the concept that unlocks everything else.

Don't run any enrichment columns yet; today is navigation only, to preserve credits for Day 18.

Resources  university.clay.com → Clay 101: GTM Automation

### D17 · Week 4, Day 17 — Importing & structuring data

Get your list into Clay cleanly.

Objective:  You can import your Week-3 list into Clay with correct column types and verify nothing broke.

WHY THIS MATTERS

A clean import is the foundation for every enrichment that follows. Mis-typed columns and broken imports cause silent errors downstream that are painful to trace. This is a small skill with an outsized payoff in reliability.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Import options and column types

Clay imports from CSV, and directly from Apollo and LinkedIn sources. When importing, Clay assigns each column a type; getting the types right matters because operations behave differently on text vs. URL vs. email vs. company fields. A company/domain column feeds enrichment differently than a plain-text column. Check and correct column types on import, not after they've built columns on top of them.

The professional habit: import, then immediately verify. Spot-check that rows landed intact, that the domain column is recognized as a domain, that no rows were dropped or merged. Five minutes of verification prevents hours of confusion.

2026 MARKET REALITY (KNOW THIS COLD)

Because Clay charges Data Credits per attempt (not per success), a dirty import that triggers enrichment on garbage rows costs real money. Clean structure before enrichment is a cost-control discipline, not just tidiness.

Clay's free tables cap at 200 rows, so the ~100-row Week-3 list imports comfortably with headroom.

RUN THE HOUR

0:00–0:15  Learn import options (CSV, Apollo/LinkedIn sources) and column types.

0:15–0:55  Import the Week-3 list into Clay; set correct column types.

0:55–1:00  Verify nothing broke on import — spot-check rows and column types.

TIPS & COMMON MISTAKES TO AVOID

Watch for the domain/company column being imported as plain text — it's the most common break and it silently degrades enrichment.

Keep the original spreadsheet as a backup so a botched import is a five-minute redo, not a disaster.

Resources  Clay University import lessons

### D18 · Week 4, Day 18 — Your first enrichment

Enrich a company and find a work email — and learn how credits work.

Objective:  You can add enrichment columns to find firmographics and a work email, and can measure credits used per row.

WHY THIS MATTERS

This is the moment Clay becomes real — a name turns into a complete, targetable record. But it's also where credits start burning, so you must build the habit of measuring cost per enriched row now, before scaling. Cost-awareness from the first enrichment is what makes them efficient later.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Enrichment columns and the credit model

An enrichment column calls a data provider to fill in a field — company headcount, industry, tech stack, or a work-email finder. You add the column, point it at the input (usually the company or person), and run it. Clay's dual-meter model (since March 2026) separates Data Credits (enrichment lookups) from Actions (platform operations). The rule that matters most: credits are charged per attempt, not per success — a lookup that returns nothing still costs.

Run enrichment on a small batch (10 rows) first, and record credits used per row. This teaches the unit economics viscerally: you see that a three-provider run on ten rows costs real credits whether or not it finds anything, which motivates every efficiency technique in Week 5.

Firmographics vs. email finding

Firmographic enrichment (size, industry, tech) is usually cheap and high-hit-rate. Email finding is the harder, higher-value operation and the one that benefits most from waterfalls later. Doing both on ten rows shows you the range of cost and reliability across enrichment types.

2026 MARKET REALITY (KNOW THIS COLD)

After the March 2026 overhaul, Clay says the most-used enrichments cost ~50% fewer credits on average, with some lookups down as much as 90% — but the per-attempt charge on failures remains the main hidden cost driver.

Cost-per-verified-contact is a metric hiring managers respect. Starting to measure it on Day 18 means you can quote real numbers in interviews.

RUN THE HOUR

0:00–0:20  Learn enrichment columns and the Data Credits / Actions model, emphasizing per-attempt billing.

0:20–0:55  Enrich 10 rows: company firmographics + a work-email finder.

0:55–1:00  Record credits used per enriched row.

TIPS & COMMON MISTAKES TO AVOID

Cap the run at 10 rows. The instinct is to enrich all 100 immediately — that's how a free tier evaporates in one session.

Write down the credits-per-row number. It's the baseline they'll improve against in Week 5.

Resources  Clay University enrichment + credit-optimization lessons

### D19 · Week 4, Day 19 — Clay formulas basics

Manipulate and combine data without leaving the table.

Objective:  You can build 2–3 formula columns to clean and combine data, and can tell when a formula beats manual editing.

WHY THIS MATTERS

Formulas are how you shape messy data into clean, usable fields without exporting to a spreadsheet. They're free (no data credits) and they're the bridge to thinking programmatically inside Clay. Small formula skills eliminate huge amounts of manual cleanup.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Text formulas and combining columns

Clay supports formula columns that transform existing data: cleaning a name (trimming, capitalizing), combining columns (building a 'company + domain' field), extracting parts of a string, or standardizing formats. These run on data you already have, so they don't cost data credits — they're pure logic.

The AI Formula Generator lets you describe what you want in plain language ('extract the first name from the full name column') and Clay writes the formula. Learn this as a productivity tool but Read the generated formula so you understand it, not just trust it.

When a formula beats manual editing

The judgment: a formula pays off when the transformation is consistent across rows and the list is large enough that manual editing would be slow or error-prone. For a one-off fix on three rows, edit manually. For 'clean every company name' across 100 rows, write the formula once. Learning where that line is makes you efficient.

2026 MARKET REALITY (KNOW THIS COLD)

Formula columns don't consume Data Credits, so they're the cheapest way to improve list quality — heavy use of formulas is a hallmark of a cost-efficient Clay operator.

The AI Formula Generator reflects the broader 2026 pattern: AI writes the mechanical logic, the human supplies the intent and the check.

RUN THE HOUR

0:00–0:25  Learn text formulas, combining columns, and the AI Formula Generator.

0:25–0:55  Build 2–3 formula columns (e.g. clean a name, build a 'company + domain' field).

0:55–1:00  Note where a formula beat manual editing — and where it wouldn't have.

TIPS & COMMON MISTAKES TO AVOID

Encourage reading AI-generated formulas rather than blindly accepting them — it builds the programmatic intuition they'll need for Python in Week 12.

A great first formula is normalizing domains (stripping https://, www) — it's immediately useful for enrichment inputs.

Resources  clay.com formulas-without-coding guide

### D20 · Week 4, Day 20 — Ship: an enriched list

Deliver your target list, enriched in Clay.

Objective:  You ship your full list enriched with emails + firmographics, with total credits tracked and output cleaned.

WHY THIS MATTERS

This turns the raw Week-3 list into a genuinely usable asset and produces the first artifact with a cost attached — a number you can defend. Tracking and documenting the credit cost is what makes this a professional deliverable rather than a class exercise.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Enriching the full list responsibly

Now enrich the whole ~100-row list with emails and firmographics, applying what Week 4 taught: correct column types, formulas to clean inputs first (so you don't waste lookups on malformed rows), and a small pilot before the full run. Track total credits consumed across the run.

Then clean the output: flag or separate rows where enrichment failed or returned catch-alls, and apply the Day 14 quality bar. The deliverable is not 'I ran enrichment' — it's 'here is a clean, enriched list, and here is what it cost.'

Documenting cost

Screenshot the table and note the total credits and the resulting cost-per-enriched-row. This is the first time you produces a metric a hiring manager cares about. It also sets up Week 5, where they'll cut this cost dramatically with waterfalls and conditional logic — the before/after story is a strong portfolio narrative.

2026 MARKET REALITY (KNOW THIS COLD)

Documenting cost-per-verified-contact is a directly hireable habit — it's one of the core metrics the role is measured on.

Expect the free-tier credit allowance to be tight for a full 100-row enrichment; if it runs out, enrich a clean subset and note the extrapolated cost. The skill is the method, not the volume.

RUN THE HOUR

0:00–0:50  Enrich the full list (emails + firmographics), track total credits, and clean the output.

0:50–1:00  Screenshot the table + note cost; add to portfolio as deliverable #4.

TIPS & COMMON MISTAKES TO AVOID

If credits are tight, enrich a representative subset and clearly note the per-row cost — don't let a paywall block the lesson.

Write down the total cost. In Week 5 they'll beat it, and that before/after is the story that sells the portfolio.

Resources  The Week-4 Clay table + the credit tracking from Day 18

◆  Portfolio deliverable #4: Enriched account list

## Week 5 — Clay intermediate — waterfalls, logic & efficiency

Build enrichment that's both reliable and cost-efficient.

Days 21–25

### D21 · Week 5, Day 21 — Waterfall enrichment

Learn why chaining data providers beats any single source.

Objective:  You can build a 2–3 provider email waterfall and compare its match rate to a single-source run.

WHY THIS MATTERS

Waterfalling is the single most important Clay technique and the thing interviewers explicitly ask candidates to explain. It's the practical solution to the coverage-vs-accuracy tradeoff from Week 3: no single provider is enough, so you chain them. Master this and Clay stops being a spreadsheet and starts being a coverage engine.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What a waterfall is and why it works

A waterfall queries a sequence of data providers per record and keeps the first verified result, stopping there. Provider A runs; if it finds a verified email, you're done; if not, provider B runs; then C. Because different providers have different coverage, chaining them lifts your overall match rate far above any single source — routinely from ~50–60% single-source to 90%+ combined.

The elegance is in the economics: because you stop at the first hit, you don't pay every provider for every row — you only escalate to the more expensive providers when the cheap ones miss. This is why waterfalls lift coverage without multiplying cost, and why they're the default professional pattern.

Ordering the waterfall

Order matters enormously. Put the cheapest, highest-hit-rate provider first and the most expensive last, so most rows resolve cheaply and only the stubborn ones reach the pricey provider. Learn the principle: 'start cheap, go expensive.' This ordering decision is where a thoughtful operator saves 50–70% of enrichment cost versus a naive chain.

2026 MARKET REALITY (KNOW THIS COLD)

Clay waterfalls across 100–200 providers and only spends data on providers that return a result at each step, which is how it reaches 95%+ coverage. Cross-verification through a waterfall pulls bounce rates from 5–8% down to 1–2%.

Explaining waterfall logic clearly is a named screening criterion in 2026 GTM engineer interviews — this session is directly interview-relevant.

RUN THE HOUR

0:00–0:25  Learn what a waterfall is and why it lifts match rates without multiplying cost.

0:25–0:55  Build an email waterfall (2–3 providers in sequence) on a sample.

0:55–1:00  Compare match rate vs. the single-source run from Week 4.

TIPS & COMMON MISTAKES TO AVOID

Make the match-rate comparison explicit and numeric — the jump from single-source to waterfall is the aha that sells the technique.

Reinforce 'cheapest first': it's the one ordering rule that separates efficient operators from credit-burners.

Resources  Clay University waterfall lessons

### D22 · Week 5, Day 22 — Conditional logic & 'run only if'

Save credits and branch your workflows intelligently.

Objective:  You can add 'only run if' conditions so expensive columns fire only when needed, and estimate credits saved.

WHY THIS MATTERS

This is the second half of cost control. Waterfalls make each lookup efficient; conditional logic makes sure you don't run lookups you don't need at all. Because Clay charges per attempt, skipping unnecessary runs is pure savings. This is the difference between a hobbyist who burns your credits in a day and a professional who runs sustained campaigns.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Conditional run settings

Every column in Clay can be set to run only if a condition is met. The pattern: qualify cheaply first, then only spend expensive credits on rows that pass. For example, use free/cheap firmographic data to filter to in-ICP rows, and only run the expensive email waterfall on those. A non-ICP row never triggers the costly lookup, so you never pay for it.

Learn the mental frame: 'gate expensive operations behind cheap qualifications.' Ask, for each expensive column, 'what cheap condition must be true for this to be worth running?' — then encode that condition.

Estimating the savings

Estimate: if 40% of imported rows are out-of-ICP and you gate the waterfall behind an ICP check, you've cut waterfall spend by ~40% with zero loss of useful output. Making them do the arithmetic turns an abstract feature into a visible cost lever.

2026 MARKET REALITY (KNOW THIS COLD)

Because Clay bills per attempt regardless of success, 'qualify before enriching' is the highest-ROI cost technique in 2026 — running full enrichment on every import is the most common way teams waste credits.

Combined with batch (not real-time) processing and result caching, conditional logic is what keeps sustained multi-step campaigns affordable on Clay's dual-credit model.

RUN THE HOUR

0:00–0:20  Learn conditional run settings and the 'gate expensive behind cheap' pattern.

0:20–0:55  Add 'only run if' conditions so expensive columns fire only for in-ICP rows.

0:55–1:00  Estimate the credits saved versus running everything on every row.

TIPS & COMMON MISTAKES TO AVOID

Identify your most expensive column and gate it first — the savings are most dramatic there.

Warn against over-gating to the point of missing good rows; the goal is to skip clearly-unqualified rows, not to be stingy with good ones.

Resources  clay.com credit-optimization + conditional-run guide

### D23 · Week 5, Day 23 — Lookups & deduplication

Reference data across tables and kill duplicates.

Objective:  You can set up a lookup between tables (e.g. contacts to companies) and produce a clean, deduped row count.

WHY THIS MATTERS

Real GTM data lives in related tables — a companies table and a contacts table that reference each other, mirroring how a CRM works. Lookups are how you connect them without copying data, and dedup is how you keep the whole system trustworthy. This is the first taste of relational thinking, which pays off directly in the CRM week.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Lookups between tables

A lookup lets one table reference data in another by a shared key (usually a domain or company name). Instead of duplicating company firmographics onto every contact row, you keep companies in one table and have the contacts table look up your company's data. This mirrors the CRM object model (accounts and contacts) and keeps data consistent — update the company once, every contact sees it.

Learn this as the beginning of relational thinking: separate your entities (companies vs. people), give them a shared key, and connect them by reference rather than by copy-paste. It's the same idea that underlies HubSpot/Salesforce in Week 11.

Deduplication

Duplicates are poison: they inflate your counts, double your enrichment cost, and produce embarrassing double-sends. Learn dedup approaches — deduping by domain for companies, by email or LinkedIn URL for people. After a dedup pass, the row count should drop to something you can explain ('120 imported, 8 duplicates removed, 112 unique'). A clean, explainable count is the mark of a trustworthy list.

2026 MARKET REALITY (KNOW THIS COLD)

Dedup and cross-table hygiene are core RevOps/GTM engineering responsibilities — 'keep the data clean automatically' is a stated job function, not an afterthought.

Relational structure (companies ↔ contacts) is exactly how CRMs model data, so this session is the conceptual on-ramp to Week 11's CRM object modeling.

RUN THE HOUR

0:00–0:20  Learn lookups between tables and dedup approaches (by domain, email, LinkedIn URL).

0:20–0:55  Set up a lookup (match contacts to a companies table) and dedupe the list.

0:55–1:00  Confirm the row count is clean and explainable.

TIPS & COMMON MISTAKES TO AVOID

Frame companies-and-contacts as two tables from the start; it prevents the flat-spreadsheet habit that breaks at scale.

State your dedup logic out loud ('unique by domain') — vague dedup produces vague results.

Resources  Clay University data-management lessons

### D24 · Week 5, Day 24 — ICP scoring in Clay

Turn your Week-2 ICP into a computed fit score.

Objective:  You can build conditional formula columns that compute a fit score and sort accounts by it.

WHY THIS MATTERS

This is where strategy becomes system. The ICP written in Week 2 has been a document; now it becomes a live, computed score that ranks every account automatically. Scoring is what lets a GTM engineer prioritize outreach objectively and defend it — 'we contacted these first because they scored highest, here's the rubric.'

WHAT YOU'LL LEARN — THE CORE MATERIAL

Designing a scoring rubric

A fit score converts ICP attributes into points. Design a simple, transparent rubric: e.g. company size in range = +2, target industry = +2, uses a relevant technology = +1, has a target signal = +3. Sum to a score. The rubric should reflect the strategy brief — the attributes that matter most get the most weight.

Learn the discipline of keeping it explainable. A score nobody can interpret is worse than no score. Each point should trace to a reason the account is a good fit. This is fit scoring; intent scoring (based on signals) gets layered on in Week 11 to make a combined score.

Building it as conditional columns

Implement the rubric as conditional formula columns (each attribute contributes its points), then a final column sums them. Sort the table by score. Then apply judgment: look at the top 10 — do they actually feel like the best-fit accounts? If the top of the list looks wrong, the rubric's weights are wrong, and you tune them. This human check keeps scoring honest.

2026 MARKET REALITY (KNOW THIS COLD)

Configuring Clay AI columns for ICP scoring is an explicitly named skill interviewers test for. Building a defensible scoring model is a portfolio-grade demonstration of the role.

Fit scoring here feeds directly into the combined fit-plus-intent lead score built in the CRM in Week 11 — this is a deliberate two-part build.

RUN THE HOUR

0:00–0:20  Design a simple scoring rubric (size + industry + tech + signal = score) tied to the strategy brief.

0:20–0:55  Build it as conditional formula columns; sort accounts by score.

0:55–1:00  Check the top 10 — do they feel right? Tune the weights if not.

TIPS & COMMON MISTAKES TO AVOID

Keep the rubric to 4–5 factors. Over-engineered scores are unexplainable and no better than simple ones.

The 'do the top 10 feel right?' gut check is the most important step — it's how you learn to calibrate weights against reality.

Resources  clay.com auto-qualify / lead-scoring guide

### D25 · Week 5, Day 25 — Ship: an efficient scored pipeline

Deliver a waterfall-enriched, scored, deduped table.

Objective:  You ship one table combining waterfall + conditional logic + ICP score, with a documented before/after cost.

WHY THIS MATTERS

This deliverable proves you can build enrichment that is both reliable and cost-efficient — the exact framing of a real GTM engineering problem ('cut enrichment cost 40% while improving match rate'). The before/after cost story, versus the Week-4 naive enrichment, is one of the strongest narratives in the whole portfolio.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Combining the week into one table

Assemble everything from Week 5 into a single table: the email waterfall (Day 21), conditional gating so expensive columns only run on qualified rows (Day 22), clean lookups and dedup (Day 23), and the computed ICP fit score (Day 24). The output is a deduped, enriched, scored, prioritized account list — a genuine pipeline-generation asset.

Then compute cost-per-verified-contact and compare it to the Week-4 naive run. The story to document: 'In Week 4, enriching everything cost X per verified contact. In Week 5, waterfalling plus conditional gating cut that to Y — a Z% reduction — while raising match rate from A% to B%.' That sentence is what a hiring manager wants to hear.

2026 MARKET REALITY (KNOW THIS COLD)

'How do we cut enrichment cost per record by 40% while improving match rate?' is quoted as a canonical GTM engineering question. This deliverable answers it with your own numbers.

Cost-per-verified-contact and match rate are two of the metrics the role is measured on; documenting both makes this a metrics-backed portfolio piece.

RUN THE HOUR

0:00–0:50  Combine waterfall + conditional logic + ICP score into one table; compute cost-per-verified-contact.

0:50–1:00  Document the before/after cost; add as deliverable #5.

TIPS & COMMON MISTAKES TO AVOID

Insist on the before/after number. Without it, this is just a nicer table; with it, it's a story that gets someone hired.

If credits limited the Week-4 baseline, use the per-row figures to compute the comparison honestly — the method is what matters.

Resources  The full Week-5 build + the Week-4 cost baseline

◆  Portfolio deliverable #5: Scored enrichment pipeline

## Week 6 — Clay advanced — AI research, scraping & APIs

Unlock the power features that make Clay feel like a superpower.

Days 26–30

### D26 · Week 6, Day 26 — Claygent — AI research at scale

Use Clay's AI agent to answer research questions across hundreds of rows.

Objective:  You can write a Claygent prompt that answers a real research question per account and returns structured output.

WHY THIS MATTERS

Claygent is where Clay stops being an enrichment tool and becomes a research team. It automates the manual research a human SDR would do — reading a website, checking whether a company sells to enterprise — across hundreds of rows. This is the capability that makes deep personalization possible at scale, and it's a defining 2026 feature.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What Claygent is and how to prompt it

Claygent is Clay's AI research agent: it visits websites, reads pages, and answers freeform questions about a company or person, returning structured output you can use in later columns. A newer version, Claygent Navigator, adds vision-based website crawling. The key skill is prompting for structured, verifiable outputs — not 'tell me about this company' but 'Answer only Yes or No: does this company sell to enterprise (1,000+ employee) customers? Base your answer only on their website. Cite the page.'

Learn the structured-output discipline: specify the exact format you want (Yes/No, a category, a one-line summary), tell it what source to use, and ask it to cite. Structured output is what makes the result usable in a formula or filter downstream; a rambling paragraph isn't.

Accuracy and prompt tightening

AI research is powerful but fallible — it can confidently invent. So the workflow is: run on a small sample (10 rows), read the outputs against the actual source, find where it went wrong, and tighten the prompt (more constraints, clearer format, explicit 'if unsure, say Unknown'). This iterative tightening is the real skill, and it directly parallels the AI quality-control discipline that recurs in Weeks 8 and 12.

2026 MARKET REALITY (KNOW THIS COLD)

Claygent surfaces public buying signals (LinkedIn posts, funding, job openings, press) that standard databases don't carry — 'using AI to research prospects' is now a baseline 2026 expectation, not an edge.

Claygent queries are slower and cost more credits per row than database lookups, so gate them behind conditional logic (Week 5) and run on qualified rows only.

RUN THE HOUR

0:00–0:20  Learn Claygent and how to request structured outputs (format, source, citation).

0:20–0:55  Write a prompt answering a real research question per account and run it on 10 rows.

0:55–1:00  Review accuracy against the real source; tighten the prompt.

TIPS & COMMON MISTAKES TO AVOID

Force structured outputs from the first prompt — 'Yes/No' or a fixed category — so the result is usable downstream.

Always spot-check against the actual website. Learners who trust AI output blindly here will ship confident nonsense in Week 8.

Resources  Clay University Claygent / AI lessons

### D27 · Week 6, Day 27 — Web scraping in Clay

Extract data from pages without writing a scraper.

Objective:  You can scrape a specific data point from each account's website and judge what scraped cleanly versus not.

WHY THIS MATTERS

Scraping reaches data no database carries — the specific, fresh signal on a company's own site (a pricing change, a careers page, a headline). Doing it inside Clay without building a fragile custom scraper is a practical superpower. Knowing what scrapes reliably versus not is the judgment that keeps it useful.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Clay's scraping approach

Clay can fetch and extract data from web pages as a column operation — you point it at a URL (often the company domain or a specific page) and pull a target element: the homepage headline, whether a careers page lists relevant roles, a pricing signal, a specific mention. This gets you first-party, current data straight from the source, complementing database enrichment.

Learn the practical limits: structured, consistent pages scrape cleanly; inconsistent or JavaScript-heavy pages are unreliable. Part of the skill is knowing which data points are reliably present across your target sites and which aren't worth the effort. For messier extraction, Claygent (which reasons over the page) often beats raw scraping.

2026 MARKET REALITY (KNOW THIS COLD)

Scraping-into-Clay for signals (careers pages, pricing, product pages) is a standard part of the modern intent workflow feeding Week 9's signal plays.

In 2026 the line between 'scraping' and 'AI research' has blurred — Claygent Navigator's vision-based crawling handles pages that broke traditional scrapers, so learn both as complementary.

RUN THE HOUR

0:00–0:20  Learn Clay's scraping approach and sources.

0:20–0:55  Scrape a data point from each account's website (headline, pricing signal, careers page).

0:55–1:00  Note what scraped cleanly versus not, and why.

TIPS & COMMON MISTAKES TO AVOID

Pick a data point that's consistently present across their target sites — inconsistent targets produce frustrating, patchy results.

When raw scraping fails, show that Claygent can often extract the same thing by reasoning over the page — it teaches when to reach for which tool.

Resources  clay.com web-scraping-without-code guide

### D28 · Week 6, Day 28 — The HTTP API column

Call any external API directly from a Clay table.

Objective:  You can call a simple public API from Clay, read the JSON response, and map a field into a column.

WHY THIS MATTERS

The HTTP API column is what makes Clay infinitely extensible — any service with an API becomes a data source. This is also your first real contact with APIs and JSON, the literacy that underpins the whole orchestration and coding half of the program. Demystifying APIs here removes the fear that stops non-engineers from building.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Anatomy of an API call

Learn the pieces concretely: the endpoint URL (where you're calling), the method (GET to read, POST to send), headers (metadata, including auth like an API key), and the body (data you send, for POST). The response comes back as JSON — a nested structure of keys and values. To use it, you read a specific field out of the JSON and map it into a Clay column.

Use a simple free/public API so there's no auth friction on the first try (a weather API, a company-info API, a public data endpoint). The goal is the mechanic: call → get JSON → extract a field → put it in a column. Once that clicks, you realize every API-having tool in the world is now reachable from a Clay table.

Reading JSON without fear

JSON intimidates non-engineers, so understand it plainly: it's just labeled boxes inside boxes. To get a value you name the path to it (response → data → email). Have Claude explain any response you don't understand — this is a good first example of using AI as a patient tutor for technical literacy, a theme that returns in Week 12.

2026 MARKET REALITY (KNOW THIS COLD)

API and webhook basics are an explicitly listed 2026 GTM engineer skill; the HTTP column is the gentlest on-ramp to it.

This literacy is what separates the ~$50K-higher technical GTM engineers from pure no-code operators — it starts here and compounds through orchestration and coding.

RUN THE HOUR

0:00–0:30  Learn the HTTP API column: methods, headers, auth, reading JSON.

0:30–0:55  Call one simple free/public API and map a field from the JSON response into a column.

0:55–1:00  Save this as an API reference row for later reuse.

TIPS & COMMON MISTAKES TO AVOID

Start with a no-auth public API so the first success is fast; auth complexity can come once the mechanic is understood.

Encourage you to paste confusing JSON into Claude and ask 'what field holds X?' — it builds confidence and independence.

Resources  Clay University HTTP API lesson + the target API's own docs

### D29 · Week 6, Day 29 — Writing data out

Send enriched rows to your CRM, sequencer, or a webhook.

Objective:  You can set up an export/webhook that fires when a row meets a condition, and confirm it landed.

WHY THIS MATTERS

Enrichment is worthless if the data stays trapped in Clay. Writing data out — to a CRM, a sequencer, or a webhook — is the handoff that connects Clay to the rest of the stack. This is your first orchestration act and the conceptual bridge into Week 10.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Export options and outbound webhooks

Clay can push data out several ways: native integrations (to HubSpot, a sequencer, Slack), CSV export, or a raw outbound webhook that sends the row's data to any URL. The webhook is the most general and the most important to understand, because it's how Clay talks to n8n and custom systems later. When a row meets a condition (e.g. score above threshold and email verified), the webhook fires and sends that row onward.

Learn conditional export as the natural extension of conditional logic: you don't dump the whole table downstream, you send only the rows that are ready. This is the 'handoff' from the seven-layer model made concrete — the point where value moves from L2 to L5/L6.

Confirming it landed

Fire the webhook/export once and verify the data actually arrived where it should — check the CRM record, the sequencer contact, or a webhook-testing endpoint. Learn the habit of confirming every handoff, because silent handoff failures (data that seems sent but never arrives) are the most common and most expensive orchestration bug.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's 2026 integrations include direct pushes to sequencers and CRMs (and tools like Email Bison for isolated sending infrastructure), but the outbound webhook remains the universal escape hatch for anything not natively supported.

The 'push personalized sequences directly to email or CRM without manual work' capability is central to the modern signal-to-send loop built in Week 9.

RUN THE HOUR

0:00–0:20  Learn Clay's export options and outbound webhooks; connect to conditional logic.

0:20–0:55  Set up an export/webhook that fires when a row meets a condition.

0:55–1:00  Trigger it once and confirm it landed at the destination.

TIPS & COMMON MISTAKES TO AVOID

Use a free webhook-testing endpoint (e.g. a request-bin style tool) so you can see the exact payload that leaves Clay.

Drill the 'confirm it landed' habit hard — assuming a handoff worked is how you lose leads silently.

Resources  Clay University export / integrations lessons

### D30 · Week 6, Day 30 — Ship: an intelligence table

Build a table that researches and enriches an account end-to-end.

Objective:  You ship a table that takes a company in and outputs one clean, outreach-ready row with a personalized insight field.

WHY THIS MATTERS

This is the first genuinely impressive artifact — a table where a company name goes in one side and a complete, researched, outreach-ready record comes out the other, including a personalized insight that would normally take a human ten minutes to produce. It demonstrates the full L2+L3+L7 stack in one build and is a portfolio centerpiece.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Assembling the end-to-end row

Chain the whole week: company in → scrape the site (Day 27) + Claygent research (Day 26) + waterfall email (Week 5) → one clean row with a personalized insight field. The insight field is the payoff — an AI-generated, source-grounded sentence about that specific account ('They're hiring three SDRs and still list a manual outbound process on your careers page') that becomes the hook for personalized outreach.

Apply the week's cost discipline: gate the expensive research behind qualification, request structured outputs, and QC the insight field. The deliverable is a repeatable machine, not a one-off — the value is that it runs on any new company you drop in.

2026 MARKET REALITY (KNOW THIS COLD)

Building a Clay table that autonomously researches prospects and produces personalization fields is exactly the capability job postings describe as the core of the role.

The personalized-insight field is the raw material for Week 8's 'personalization beyond {first_name}' — a strong intelligence table makes the copywriting week dramatically easier.

RUN THE HOUR

0:00–0:50  Build: company in → scrape + Claygent research + waterfall email → one clean, outreach-ready row with a personalized insight field.

0:50–1:00  Add as deliverable #6.

TIPS & COMMON MISTAKES TO AVOID

The personalized insight field is the star — spend the QC time there. A generic insight undermines the whole table's value.

Frame it as a reusable machine: Drop in a brand-new company to prove it runs end-to-end, not just on the prepared list.

Resources  The combined Week-5 and Week-6 builds

◆  Portfolio deliverable #6: Account intelligence table

## Week 7 — Email infrastructure & deliverability

The unglamorous foundation that decides whether outbound ever lands.

Days 31–35

### D31 · Week 7, Day 31 — Deliverability is infrastructure

Understand inbox placement, sender reputation, and the cost of getting it wrong.

Objective:  You can explain the chain of events that sends a campaign to spam, in your own words.

WHY THIS MATTERS

This is the unglamorous foundation that decides whether any outbound ever lands. Learners are tempted to skip it for the fun copy work — resist that. In 2026, deliverability failures don't just underperform, they get your mail rejected outright. A GTM engineer who ignores infrastructure ships machines that send into the void.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Inbox placement and sender reputation

Getting an email 'sent' is not getting it 'delivered to the inbox.' Mailbox providers (Gmail, Yahoo, Microsoft) decide whether each message lands in the inbox, the spam folder, or is rejected entirely. That decision is driven by sender reputation — a score the provider maintains for your domain and IP, based on your authentication, your complaint and bounce rates, and recipient engagement. Roughly one in six legitimate emails misses the inbox, so this is a real, constant tax on outbound.

The crucial 2026 shift: infrastructure now beats copy. The best-written email fails if it's sent from an unauthenticated, cold, or bad-reputation domain. So the professional order of operations is infrastructure first, copy second — which is why this week precedes copywriting week.

The chain of events to spam

Walk the causal chain you must be able to recite: missing/misconfigured authentication (SPF/DKIM/DMARC) → provider distrusts you → mail flagged or rejected. Or: bad list → bounces spike above 2% → reputation drops → good mail goes to spam. Or: generic blast → recipients hit 'report spam' → complaint rate crosses 0.3% → provider stops delivering. Each is a specific, avoidable failure mode. Understanding the chain is what lets a GTM engineer diagnose 'why did our campaign die?'

2026 MARKET REALITY (KNOW THIS COLD)

As of 2026, Google, Yahoo and Microsoft all enforce bulk-sender rules, and non-compliant mail is now rejected at the door with a hard failure — the message never reaches any folder. A spam-foldered email at least arrived; a rejected one doesn't exist.

The bar is effectively universal now: the strict rules formally target 5,000+/day senders, but the safe assumption for cold email is that they apply to you regardless of volume.

RUN THE HOUR

0:00–0:35  Learn why ~1 in 6 legit emails miss the inbox, what reputation is, and why infra beats copy.

0:35–1:00  Write, in your own words, the chain of events that sends a campaign to spam.

TIPS & COMMON MISTAKES TO AVOID

This is the week you want to rush. Give deliverability the same weight as Clay — it's what makes everything else land.

Write the spam chain as a causal sequence, not a list. Diagnosis is a causal skill.

Resources  unifygtm / leadhaste 2026 deliverability guides

### D32 · Week 7, Day 32 — Domains & mailbox math

Plan sending domains that protect your primary domain.

Objective:  You can plan how many domains/mailboxes are needed to send a target volume without risking the primary domain.

WHY THIS MATTERS

Sending cold email from your main company domain is how you burn the domain your business actually depends on. Professionals send from separate, dedicated domains. The math of how many domains and mailboxes you need for a given volume is a concrete planning skill every outbound operation requires.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Why secondary domains

Never send cold outbound from your primary domain — a reputation hit there means your invoices, contracts, and internal mail start landing in spam. Instead, register dedicated secondary domains that resemble your brand (variations, alternate TLDs like .co or .io), each used only for outbound. If a secondary domain's reputation degrades, you retire it without touching the business's real domain.

Learn domain hygiene: use reputable registrars, pick clean domains that don't pattern-match known spam, and avoid free-provider lookalikes. A typical setup runs several dedicated sending domains with a few mailboxes each.

The mailbox math

Each mailbox can safely send only a limited volume per day (roughly 20–30/day for cold outreach once warmed). So volume drives the math: to send X cold emails a day, you need X ÷ (per-mailbox daily cap) mailboxes, spread across several domains for rotation. Compute your own: 'to send 200/day at 30/mailbox, I need ~7 mailboxes across ~2–3 domains.' This turns an abstract worry into a concrete plan.

2026 MARKET REALITY (KNOW THIS COLD)

2026 best practice is 3–8 dedicated sending domains per program, varied TLDs, with DMARC alignment configured from day one — single-domain sending at scale is a known failure pattern.

Multi-domain rotation is considered required above roughly 1,000 sends/month; below that a smaller setup is fine, but the principle (never the primary domain) always holds.

RUN THE HOUR

0:00–0:25  Learn secondary domains, TLD/prefix choices, reputable registrars, and per-mailbox daily limits (~20–30/day).

0:25–0:55  Plan how many domains/mailboxes are needed to send the target daily volume.

0:55–1:00  Optionally buy one cheap test domain to practice DNS on.

TIPS & COMMON MISTAKES TO AVOID

Do the actual arithmetic for your own target volume — it's the difference between knowing the rule and being able to plan a real program.

One cheap test domain (~$10) is worth buying if budget allows; hands-on DNS on Day 33 is far more memorable than paper.

Resources  devcommx / mailreach cold-email domain guides

### D33 · Week 7, Day 33 — Authentication: SPF, DKIM, DMARC

Configure the three records that prove you're a real sender.

Objective:  You can explain what SPF, DKIM, DMARC and MX do, and configure or write the exact records for a domain.

WHY THIS MATTERS

These three DNS records are now mandatory — without them, major providers reject your mail. This is the single most important technical setup in all of deliverability, and it's very learnable. A GTM engineer who can set up authentication correctly is immediately more valuable than one who outsources it and doesn't understand it.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What each record does

MX (Mail Exchange): tells the world which servers receive mail for your domain. SPF (Sender Policy Framework): a DNS record listing which servers are authorized to send on your domain's behalf — receivers check it to confirm the sending server is allowed. DKIM (DomainKeys Identified Mail): a cryptographic signature added to each message, proving it genuinely came from your domain and wasn't altered in transit. DMARC (Domain-based Message Authentication): a policy that tells receivers what to do when a message fails SPF or DKIM — monitor (p=none), send to spam (p=quarantine), or reject (p=reject).

Learn that all three are now required together — SPF alone or DKIM alone is no longer enough. The standard progression is to publish DMARC at p=none first (monitor only, break nothing), confirm your legitimate mail passes, then tighten toward p=quarantine or p=reject as reputation stabilizes. Also introduce custom tracking domains so open/click tracking doesn't drag on a shared, flagged domain.

Configuring and verifying

Either configure the records on your test domain or write out the exact records they'd add (the SPF include, the DKIM key from your sending tool, the DMARC policy string). Then verify with a tool like mail-tester or MXToolbox, which checks the records and flags misconfigurations — a typo in SPF or a missing DKIM key is a common, silent failure that a verification tool catches before it kills a campaign.

2026 MARKET REALITY (KNOW THIS COLD)

In 2026, Gmail permanently rejects mail from senders without DMARC — this is a hard bounce, not a spam-filter issue. DMARC presence has passed 75% of large domains, but only ~35% enforce (p=quarantine/reject), and that enforcement gap is where most deliverability risk now sits.

One-click unsubscribe (RFC 8058) is also required for marketing/bulk mail alongside authentication — learn it as part of the same compliance bundle even though it's a header, not a DNS record.

RUN THE HOUR

0:00–0:30  Learn what MX, SPF, DKIM, DMARC each do, why to start DMARC at p=none, and custom tracking domains.

0:30–0:55  Configure them on the test domain (or write the exact records you'd add).

0:55–1:00  Verify with mail-tester or MXToolbox.

TIPS & COMMON MISTAKES TO AVOID

Even without a test domain, Write the literal records — the specificity is what proves understanding.

Show a mail-tester score report; seeing the pass/fail per record makes the abstract concrete and memorable.

Resources  leadhaste checklist + mail-tester.com / mxtoolbox.com

### D34 · Week 7, Day 34 — Warmup & sending discipline

Ramp a domain safely and stay inside bulk-sender rules.

Objective:  You can write a concrete 21-day warmup schedule and state the complaint/bounce thresholds to stay under.

WHY THIS MATTERS

A brand-new domain that immediately blasts 100 emails a day looks exactly like a spammer and gets flagged. Warmup — ramping volume gradually while building positive engagement — is how you establish reputation. Sending discipline (staying under the thresholds) is how you keep it. This is the operational routine that keeps outbound alive.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The warmup ramp

A new domain must ramp slowly. Start very low (roughly 5–10 sends/day) and increase gradually over about 4–6 weeks toward the target volume, keeping daily volume predictable rather than spiky. During warmup, warmup tools exchange positive engagement (opens, replies, moving mail out of spam) to teach providers your domain is trustworthy. Inbox rotation — spreading sends across multiple mailboxes — keeps any single mailbox under its safe cap.

Write a concrete 21-day schedule: day-by-day send counts ramping from ~5 to ~50, across your planned mailboxes. A specific schedule is the deliverable, not a vague 'warm it up.'

The thresholds that must not be crossed

Drill the numbers: keep spam-complaint rate under 0.3% (and really aim under 0.1% — treat 0.3% as an emergency ceiling, not a target), and bounce rate under 2%. Cross the complaint line and you become ineligible for delivery mitigation until you're back under it for seven consecutive days — a punishing feedback loop. Monitoring these via Google Postmaster Tools is part of the daily discipline. Learn monitoring on slope, not just threshold: a 0.1% complaint rate climbing 10% week over week is heading for trouble even though it's 'under the line.'

2026 MARKET REALITY (KNOW THIS COLD)

2026 thresholds are enforced tightly: 0.3% spam complaints and 2% bounce are hard ceilings across Gmail/Yahoo/Microsoft; stable senders work to stay under 0.1% complaints.

Skipping warmup 'because the timeline is tight' is named as a mistake that always fails. There is no compliant shortcut — the ramp is non-negotiable.

RUN THE HOUR

0:00–0:30  Learn the multi-week warmup, the ramp schedule (~5 → 50/day), inbox rotation, and the provider thresholds (complaints <0.3%, bounce <2%).

0:30–1:00  Write a concrete 21-day warmup schedule with day-by-day send counts across mailboxes.

TIPS & COMMON MISTAKES TO AVOID

Require actual numbers per day, not 'increase gradually.' The specific schedule is what makes this operational.

Introduce Google Postmaster Tools as the dashboard they'll live in — monitoring is a daily habit, not a one-time check.

Resources  instantly 2026 deliverability + Gmail Postmaster docs

### D35 · Week 7, Day 35 — Ship: a deliverability runbook

Produce the setup doc a company could hand to any new hire.

Objective:  You ship a runbook covering domains to buy, exact DNS records, warmup schedule, daily caps, and a monitoring checklist.

WHY THIS MATTERS

A runbook proves you can operationalize deliverability — turn scattered knowledge into a repeatable procedure anyone could follow. This is exactly the kind of internal documentation a real GTM engineer produces, and it's a portfolio piece that signals operational maturity, not just tool knowledge.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What goes in the runbook

Assemble the week into one document a new hire could execute without asking questions: which domains to buy and from where, the exact DNS records (SPF include, DKIM setup, DMARC policy progression), the mailbox count and daily caps, the day-by-day warmup schedule, the compliance items (one-click unsubscribe), and a monitoring checklist (what to watch in Postmaster Tools, the thresholds, and what to do when a number goes red).

The test of a good runbook: hand it to someone with no deliverability knowledge — could they set up a compliant sending operation from it alone? That's the standard for real operational documentation, and it's what makes this a hireable artifact.

2026 MARKET REALITY (KNOW THIS COLD)

Agencies running 2026 outbound give every client 3–8 dedicated domains with DMARC alignment from day one and a documented deliverability playbook — this runbook mirrors that professional deliverable.

Because enforcement now hard-bounces non-compliant mail, a runbook that bakes in authentication and warmup isn't bureaucracy — it's the thing standing between a campaign and total silence.

RUN THE HOUR

0:00–0:50  Write the runbook: domains to buy, exact DNS records, warmup schedule, daily caps, monitoring checklist.

0:50–1:00  Add as deliverable #7.

TIPS & COMMON MISTAKES TO AVOID

Push for 'a new hire could execute this' completeness — vague steps disqualify it as a runbook.

Include the 'when a number goes red, do this' section; troubleshooting instructions are what make runbooks genuinely valuable.

Resources  The full Week-7 material, assembled into procedure form

◆  Portfolio deliverable #7: Deliverability runbook

## Week 8 — Copywriting & personalization at scale

Turn enriched data into messages that actually get replies.

Days 36–40

### D36 · Week 8, Day 36 — Cold email frameworks

Learn structure, subject lines, and the CTA philosophy that gets replies.

Objective:  You can write one framework-following email for your offer, with a compliant subject line and a soft CTA.

WHY THIS MATTERS

Now that the infrastructure lands mail in the inbox, the copy has to earn a reply. Cold email has a proven structure that consistently outperforms improvisation. Learning the framework — and what kills replies — gives you a reliable baseline they can personalize, rather than staring at a blank page.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The proven structure

Learn a simple, durable structure: a relevant opener (about them, not you — ideally tied to a signal or insight), a concise problem/value line (the pain you remove, in their terms), light proof (a number or comparable customer), and a soft call to action. Keep it short — a cold email should be readable in under ten seconds. Walls of text kill replies.

Subject lines: short, specific, lowercase-ish and human, no hype, no spam-trigger words (free, guarantee, act now), no clickbait. The subject's only job is to earn the open; it should feel like a note from a person, not a marketing blast.

The CTA philosophy: soft beats hard

The instinct is to ask for a 30-minute demo in the first email. Learn the opposite: a soft CTA (an interest-check question — 'worth a quick look?' or 'is this a priority this quarter?') gets far more replies than a hard meeting ask, because it lowers the commitment to respond. The goal of email one is a reply, not a booked call. Also learn what kills replies: hype, jargon, walls of text, multiple asks, and spam-trigger words that also hurt deliverability.

2026 MARKET REALITY (KNOW THIS COLD)

Reply-rate benchmarks in 2026 reward short, relevant, single-ask emails; generic templated copy reused across thousands of sends now pattern-matches to spam fast and hurts both replies and deliverability.

Spam-trigger words are a copy problem and a deliverability problem simultaneously — this session connects directly back to Week 7.

RUN THE HOUR

0:00–0:30  Learn the email structure, subject-line rules, soft CTAs, and what kills replies (walls of text, hype, spam-trigger words).

0:30–1:00  Write one framework-following email for the offer.

TIPS & COMMON MISTAKES TO AVOID

Enforce brevity ruthlessly — count the words. Most first drafts are twice as long as they should be.

Ban the hard demo ask in email one. The soft CTA is counterintuitive and you resist it until they see the reply-rate logic.

Resources  clay.com cold-email + reply-rate benchmark guides

### D37 · Week 8, Day 37 — Personalization beyond {first_name}

Make relevance the personalization, not tokens.

Objective:  You can rewrite an email to open with a specific, data-derived insight about the account and compare it to the token version.

WHY THIS MATTERS

Merge tags like {first_name} and {company} are not personalization — every spammer uses them. Real personalization is relevance: showing you understand this specific account's situation. This is where the Week-6 intelligence table pays off, and it's the skill that separates outreach that feels human from outreach that feels automated.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The 'one real insight' approach

True personalization means opening with one specific, true observation about the account that proves you did the work — pulled from the enrichment and research built in Week 6. 'I saw you're hiring three SDRs but still running manual outbound' beats 'Hi {first_name}, I hope this finds you well.' The insight earns attention because it's evidently not mass-produced, even though the system produced it at scale.

Pair the insight with a proof strategy: connect the observation to the outcome you create and a reason to believe. Insight → implication → proof → soft ask. The insight makes them read; the rest makes them reply.

Rewrite and compare

Take yesterday's framework email and rewrite the opener to lead with a data-derived insight from your intelligence table. Then compare the two versions side by side. The token version reads generic; the insight version reads like a human who researched them. Feeling that difference is the lesson — and it's the argument for why the Week-6 enrichment work mattered.

2026 MARKET REALITY (KNOW THIS COLD)

With AI producing most copy in 2026, the differentiator is the quality of the underlying insight, not the fluency of the sentence — relevance is the scarce input, and it comes from good data.

The 'one real insight' opener is what makes AI-personalized email at scale (tomorrow's session) actually land instead of reading like obvious template-filling.

RUN THE HOUR

0:00–0:25  Learn the 'one real insight' approach and proof strategy.

0:25–0:55  Rewrite yesterday's email to open with a specific, data-derived insight about the account.

0:55–1:00  Compare the two versions — feel the difference in relevance.

TIPS & COMMON MISTAKES TO AVOID

Insist the insight be verifiably true and specific. A vague 'I see you care about growth' is worse than no personalization.

Point you back to your Week-6 intelligence table — the insight field they built is exactly the raw material for this.

Resources  copywriting principles from Clay / Nebor practitioner posts

### D38 · Week 8, Day 38 — AI personalization at scale

Use an LLM inside Clay to write relevant openers from enriched data — with quality control.

Objective:  You can build an AI column that writes a one-line personalized opener per row, with a QC rule that catches bad outputs.

WHY THIS MATTERS

This is the multiplier: the 'one real insight' opener from yesterday, generated automatically across the whole list. But AI at scale without quality control produces confident nonsense at scale — so the QC discipline is as important as the generation. This is the exact skill (AI + quality control) that defines the modern role.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Prompting an AI column from enriched fields

Build an AI column (using Clay's 'Use AI', which aggregates Claygent/Anthropic/OpenAI/Gemini) that takes the row's scraped and researched fields as input and writes one personalized opening line. The prompt must feed it the specific data ('here is what we know about this account: [scraped headline], [Claygent research], [hiring signal]') and constrain the output ('write one sentence, specific to this account, no greeting, under 20 words, no hype'). Good input fields plus a tight prompt produce openers that read human.

Learn that the AI is only as good as the data you feed it — a rich intelligence table (Week 6) produces rich openers; a thin one produces generic filler. This closes the loop on why the enrichment weeks mattered.

Quality control at scale

AI will sometimes hallucinate, produce awkward phrasing, or reference something false. So add a QC rule: a second column (AI or logic) that flags outputs that are too long, mention something not in the source data, sound generic, or are empty. Then spot-check a sample of 10 by hand. Never send AI-generated copy unreviewed — the QC layer is what makes automation safe. This same generate-then-verify pattern recurs in the coding week.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's 2026 'Use AI' unifies multiple models into one enrichment; the skill is prompt design and QC, which transfer across whichever model sits underneath.

AI prompt engineering for personalization at scale is an explicitly named 2026 baseline skill — a GTM engineer who can't use an LLM to generate quality-controlled variants is 'operating below the baseline.'

RUN THE HOUR

0:00–0:20  Learn prompting an AI column using scraped/Claygent fields.

0:20–0:55  Build an AI column that writes a one-line personalized opener per row; add a QC rule to catch bad outputs.

0:55–1:00  Spot-check 10 openers against the source data.

TIPS & COMMON MISTAKES TO AVOID

The QC rule is not optional — make it part of the deliverable. Ungated AI copy is a liability, not an asset.

If openers come out generic, the fix is usually richer input fields, not a cleverer prompt. Go back to the intelligence table.

Resources  clay.com AI-for-prospecting guide + the Week-6 table

### D39 · Week 8, Day 39 — LinkedIn & multichannel

Add LinkedIn touches and route by channel — the 'wall of sound.'

Objective:  You can design a 2-channel (email + LinkedIn) sequence with routing logic and map which step fires when.

WHY THIS MATTERS

Buyers ignore single channels but notice coordinated presence across several — the 'wall of sound.' Adding LinkedIn to email roughly doubles the touchpoints and dramatically increases the chance of a reply. Designing the choreography (which channel, which order, what timing) is a core GTM engineering skill.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Multichannel sequencing

A multichannel sequence coordinates touches across email and LinkedIn (a connection request, a profile view, a message) so the prospect encounters you in more than one place. The effect is cumulative: an email plus a LinkedIn touch feels like genuine interest, where either alone is easy to ignore. Learn the concept of channel routing — deciding, per step, which channel fires and in what order, based on what's available (do you have their email? are they connectable on LinkedIn?).

LinkedIn automation (via tools like HeyReach) has tighter limits than email — LinkedIn caps connection requests and messages per day, and aggressive automation risks account restrictions. So build TOS/limits awareness into the design: LinkedIn is a lower-volume, higher-trust channel, used to complement email, not replace it.

Mapping the sequence

Design a concrete 2-channel sequence: e.g. Day 1 email, Day 2 LinkedIn connect, Day 4 email follow-up, Day 6 LinkedIn message. Map exactly which step fires when and the routing logic for prospects missing a channel. A clear step map is what you'd load into a sequencer — it's the executable plan, not a vague 'we'll also use LinkedIn.'

2026 MARKET REALITY (KNOW THIS COLD)

LinkedIn automation goes through tools like HeyReach in the 2026 stack; the 'wall of sound' multichannel approach is standard practice for serious outbound.

Respecting LinkedIn's limits matters more than ever — a restricted LinkedIn account can't be swapped as easily as a burned email domain, so channel discipline protects a scarcer asset.

RUN THE HOUR

0:00–0:25  Learn multichannel sequencing and LinkedIn automation via HeyReach; note TOS/limits.

0:25–0:55  Design a 2-channel sequence (email + LinkedIn) with channel routing logic.

0:55–1:00  Map which step fires when.

TIPS & COMMON MISTAKES TO AVOID

Stress LinkedIn's daily limits — over-automating LinkedIn is a fast way to lose an account, which is costlier than a burned email domain.

Keep the sequence realistic (4–6 touches over ~10 days). Aggressive over-sequencing annoys buyers and hurts reply rates.

Resources  heyreach.io + multichannel orchestration guides

### D40 · Week 8, Day 40 — Ship: a personalized sequence

Deliver an AI-personalized, multichannel sequence for your 100 leads.

Objective:  You ship a full email + LinkedIn sequence with AI openers and QC checks, ready to load into a sequencer.

WHY THIS MATTERS

This assembles the whole execution layer into one deliverable — real leads, AI-personalized openers, quality-controlled, coordinated across channels, ready to run. It's the first artifact that could literally be launched, and it demonstrates you can go from data to inbox-ready campaign. A strong portfolio centerpiece.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Assembling the launch-ready sequence

Combine the week: the framework email (Day 36), the insight-led personalization (Day 37), the AI-generated openers with QC (Day 38), and the multichannel step map (Day 39), applied to the 100-lead enriched list. The output is a complete sequence — every step written, every opener personalized and checked, channel routing defined — in a form you could load straight into a sequencer.

Remember 'ready to load.' The deliverable isn't 'I wrote some emails'; it's a fully specified, QC'd, multichannel campaign for a real list. Note whether it's actually loaded/launched (if paid sending tools are in reach) or fully built and documented on free tiers — either way the build logic is the skill.

2026 MARKET REALITY (KNOW THIS COLD)

A launch-ready multichannel sequence built on enriched, scored leads is close to a real deliverable a Claygency ships for a client — it demonstrates end-to-end execution capability.

Because deliverability (Week 7) is already handled, this sequence is built on compliant infrastructure — the combination of clean infra plus personalized copy is what actually books meetings in 2026.

RUN THE HOUR

0:00–0:50  Assemble the full email + LinkedIn sequence with AI openers and QC checks, ready to load into a sequencer.

0:50–1:00  Add as deliverable #8.

TIPS & COMMON MISTAKES TO AVOID

Verify the QC actually happened on every opener before calling it shippable — one hallucinated line undermines the whole sequence.

If you can't afford live sending tools, have them fully build and document the sequence on free trials or on paper — the setup logic is what's assessed.

Resources  The combined Week-8 builds + the Week-4/5 enriched list

◆  Portfolio deliverable #8: Personalized multichannel sequence

## Week 9 — Signals & intent-based outbound

Trigger the right message at the exact moment it's relevant.

Days 41–45

### D41 · Week 9, Day 41 — Signal types & sources

Catalog first-party, product-usage and third-party signals.

Objective:  You can list every signal they could realistically detect for your company and name the source of each.

WHY THIS MATTERS

Week 2 introduced signals conceptually; this week makes them operational. Before building signal plays, you needs a complete inventory of what's detectable and where it comes from. Signal-based outbound is the modern motion's core, and a thorough source map is the foundation for every play that follows.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The full signal taxonomy, revisited operationally

Revisit the three types (first-party, product-usage, third-party) but now focused on sources and detectability. First-party: form fills, pricing-page visits, replies, demo requests — detected via your website (visitor-ID tools) and your own systems. Product-usage: feature use, limits hit, seats added — detected via product analytics/events (for PLG products). Third-party: funding (news/RSS/funding databases), hiring (job boards), job changes and promotions (LinkedIn/Clay Signals), tech-stack changes (technographic sources), news mentions (news feeds/scraping).

The operational insight: each signal has a specific, findable source and a detection cost. Mapping signal → source → cost turns the abstract 'watch for intent' into a concrete build list. This map is the blueprint for the whole week.

Building the company's signal inventory

Produce an exhaustive list for your adopted company: every signal that would indicate relevance, paired with the source that would detect it and a rough sense of how fresh and reliable that source is. This is the raw material for choosing which play to build (Days 42–44). A rich inventory means more play options; a thin one signals the ICP may need sharpening.

2026 MARKET REALITY (KNOW THIS COLD)

The 2026 edge is acting on a signal within minutes — so an inventory that notes freshness (how fast each source updates) is more useful than one that just lists signals.

Signal/intent platforms now aggregate hundreds of signals from dozens of sources, but a GTM engineer still needs to know which signals map to your specific product's 'why now' — generic intent data without ICP fit is noise.

RUN THE HOUR

0:00–0:30  Deep-dive the signal taxonomy and where each type comes from (forms, product events, funding, hiring, tech changes, news).

0:30–1:00  For the company, list every signal you could realistically detect and its source and freshness.

TIPS & COMMON MISTAKES TO AVOID

Push for signals tied to a specific 'why now,' not static attributes. 'They're big' isn't a signal; 'they just doubled headcount' is.

Note detection cost/freshness per signal — it's what makes the inventory actionable when choosing plays.

Resources  unifygtm signal-based selling + intent-data explainers

### D42 · Week 9, Day 42 — Website visitor identification

Turn anonymous traffic into warm outbound.

Objective:  You can design a visitor-identified → enrich → qualify → sequence play and articulate the privacy/consent considerations.

WHY THIS MATTERS

Most website visitors never fill out a form — they browse and leave anonymously. Visitor-ID tools de-anonymize a portion of that traffic, turning your warmest, highest-intent prospects (people already on your site) into reachable leads. This is one of the highest-ROI signal plays and a staple of the 2026 stack.

WHAT YOU'LL LEARN — THE CORE MATERIAL

How visitor-ID works and the play it enables

Visitor-ID tools (e.g. RB2B) identify some anonymous website visitors — matching them to a company and sometimes a person — so you know who was on your pricing page even though they never submitted a form. The play: visitor identified → enrich them in Clay → qualify against ICP/score → route into a personalized sequence referencing their visit. Because a pricing-page visit is a strong first-party intent signal, this outbound is among the warmest you can run.

Learn the full loop as a handoff chain: the visitor-ID tool fires a signal → orchestration passes it to Clay → Clay enriches and scores → a webhook pushes qualified visitors into a sequence. This is the signal-to-send loop that Week 10's orchestration will wire together.

Privacy and consent

This is the session where responsibility matters most. Visitor identification sits in a sensitive area — privacy regulations, consent requirements (cookie/consent banners), and regional rules (stricter in the EU) all apply. Consider consent and compliance before deploying: prefer the most privacy-preserving configuration, and understand that 'because it's technically possible' isn't the same as 'appropriate to do.' A GTM engineer who ignores privacy creates legal and reputational risk for the business.

2026 MARKET REALITY (KNOW THIS COLD)

Visitor ID (RB2B and peers) is a standard 2026 warm-outbound source; Clay has native walkthroughs for the visitor-identified → enrich → sequence play.

Privacy scrutiny of visitor-ID has increased — designing the play with consent and regional rules in mind is now part of doing it competently, not an optional add-on.

RUN THE HOUR

0:00–0:25  Learn visitor-ID tools (e.g. RB2B) and the warm-outbound play they enable.

0:25–0:55  Design the play: visitor identified → enrich → qualify → sequence.

0:55–1:00  Note the privacy/consent considerations for deploying it.

TIPS & COMMON MISTAKES TO AVOID

Make the privacy discussion real, not a disclaimer. State the consent and regional considerations that apply to your company.

Frame this as the warmest signal in the inventory — it earns priority precisely because the visit already happened.

Resources  clay.com warm-outbound (RB2B) walkthrough

### D43 · Week 9, Day 43 — Funding, hiring & job-change signals

Detect the highest-intent third-party events.

Objective:  You can build a Clay table or n8n feed that captures one third-party signal type for your ICP and verify fresh signals flow in.

WHY THIS MATTERS

Third-party signals — funding, hiring, job changes — are abundant, public, and often high-intent. A funding round means new budget; a wave of relevant job postings means a scaling pain; a champion changing jobs means a warm door at a new company. Building an automated feed that captures these is a concrete, repeatable GTM engineering skill.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The high-intent third-party signals

Funding: a raise means budget and growth pressure — a strong buying window for tools that help them scale. Hiring: job postings reveal priorities and pain (three SDR openings = an outbound scaling problem you might solve). Job changes: a past champion or good-fit persona moving into a buying role at a new company is one of the warmest signals in B2B — you already have a relationship. Learn which of these maps to your specific product's 'why now.'

Sources: RSS feeds and news for funding, job boards for hiring, LinkedIn/Clay Signals for job changes. The build is a feed that watches a source and captures matching events into a table, filtered to the ICP.

Building and verifying the feed

Build one signal feed — a Clay table pulling one signal type (or an n8n feed if they want a head start on Week 10) — scoped to your ICP. Then verify fresh signals are actually flowing in: the feed should populate with recent, relevant events, not stale or off-ICP noise. A feed that captures the wrong companies or old events is worse than none, so verification is part of the build.

2026 MARKET REALITY (KNOW THIS COLD)

Clay's native Signals (job changes, promotions, hiring, funding) make this far easier than hand-built scrapers did a year ago, and Signals are cheap (roughly one credit per five records).

Job-change signals are widely considered among the highest-converting because they combine a warm relationship with a fresh buying window — prioritize them in the play list.

RUN THE HOUR

0:00–0:25  Learn sources: RSS feeds, job boards, funding news, and scraping/Signals into Clay.

0:25–0:55  Build a Clay table (or n8n feed) capturing one signal type for the ICP.

0:55–1:00  Verify fresh, on-ICP signals are flowing in.

TIPS & COMMON MISTAKES TO AVOID

Pick the single highest-value signal for your product rather than trying to build all three feeds at once.

Insist on the freshness check — a feed full of three-month-old or off-ICP events silently wastes the whole play.

Resources  nebor / Growth Engine X intent-workflow breakdowns

### D44 · Week 9, Day 44 — Build a triggered play

Wire signal → enrich → personalize → send in under an hour.

Objective:  You can design trigger logic connecting a signal source to enrichment and an AI opener that references the signal, and dry-run one record.

WHY THIS MATTERS

This is where signals stop being a list and become a play — an automated chain where an event triggers enrichment, personalization referencing that exact event, and a send. The 'under an hour from signal to send' capability is the modern outbound advantage, and building it is the essence of the role.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Trigger logic: from event to message

A triggered play is a conditional chain: when a signal fires (a company appears in the funding feed), automatically enrich it, qualify it against ICP/score, and generate an opener that references the specific signal ('congrats on the Series A — teams at your stage usually hit [pain] next'). The message is relevant because it's tied to a real, recent event about that exact account. This is the combination of everything so far: signal (Week 9) + enrichment (Weeks 4–6) + AI personalization (Week 8).

Learn the design as a sequence of gated steps: trigger → qualify (skip if off-ICP) → enrich → generate signal-referencing opener → QC → route to send. Each step passes data to the next; the gating keeps it efficient and on-target.

Dry-running one record

Before automating at volume, dry-run a single record end to end: take one real signal event, walk it through the whole chain manually or in test mode, and confirm the output is a correct, personalized, ready-to-send message. This catches logic errors and bad handoffs on one record instead of on a thousand. The dry-run habit is professional discipline — never launch an untested play.

2026 MARKET REALITY (KNOW THIS COLD)

Speed from signal to personalized send is the specific thing that wins in 2026 — 'the team that can enrich and act on a signal in five minutes wins' is the market's stated logic, and this play operationalizes it.

This play reuses the Week-6 intelligence table and Week-8 AI opener, now triggered by a signal — it's a deliberate convergence of prior builds, not new tooling.

RUN THE HOUR

0:00–0:20  Design the trigger logic: signal → qualify → enrich → signal-referencing opener → QC → route.

0:20–0:55  Connect the signal source to enrichment and an AI opener that references the signal.

0:55–1:00  Dry-run one record end-to-end and confirm the output.

TIPS & COMMON MISTAKES TO AVOID

Make the opener reference the specific signal, not just the company. 'Congrats on the raise' beats a generic line but 'saw you raised to expand into [X]' is better still.

The dry-run on one record is non-negotiable — it's how you internalize testing before scaling, a habit that saves them repeatedly.

Resources  The Week-6 and Week-8 builds, now signal-triggered

### D45 · Week 9, Day 45 — Ship: a complete signal play

Deliver one end-to-end intent-based play.

Objective:  You ship a documented, built play: which signal, how it's detected, the enrichment, the message, and the timing target.

WHY THIS MATTERS

A complete signal play is arguably the most impressive single artifact in the portfolio — it shows you can detect a real-world event and convert it into relevant, timely outreach automatically. It's the clearest demonstration of the modern GTM engineering value proposition, and exactly what a hiring manager wants to see built.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Documenting and building the full play

The deliverable has two parts: the built play (working, dry-run-verified) and its documentation. Document: which signal it watches, how it's detected (source, freshness), the enrichment applied, the message logic (how the opener references the signal), and the timing target (how fast from signal to send). This documentation is what makes it teachable and hireable — it proves you understands the play, not just clicked it together.

Frame the timing target explicitly, because speed is the differentiator: 'this play sends a personalized, signal-referencing email within [X] hours of the funding announcement.' A stated timing target turns a workflow into a competitive claim.

2026 MARKET REALITY (KNOW THIS COLD)

Signal-based plays with a fast timing target are the highest-value demonstrations in 2026 — they directly embody why the role exists and why one builder outperforms a team of manual reps.

In a paid trial project, 'build a play that turns [signal] into personalized outreach' is a plausible prompt; this deliverable is that project, done for your own company.

RUN THE HOUR

0:00–0:50  Document + build the full play: which signal, how detected, enrichment, message, timing target.

0:50–1:00  Add as deliverable #9.

TIPS & COMMON MISTAKES TO AVOID

Require a stated timing target — it's the metric that makes the play sound like a competitive weapon rather than a workflow.

Write the documentation as if handing the play to a teammate. Clarity here is what makes it portfolio-grade.

Resources  The full Week-9 build

◆  Portfolio deliverable #9: Signal-based play

## Week 10 — Orchestration & automation (n8n + APIs)

Connect the whole stack so the system runs without you.

Days 46–50

### D46 · Week 10, Day 46 — Orchestration concepts

Understand the connective tissue: webhooks, triggers, and why n8n.

Objective:  You can sketch the data flow for your system (Clay → ? → CRM → sequencer → alert) and explain where handoffs break.

WHY THIS MATTERS

Orchestration (L4) is the connective tissue that turns a pile of tools into one system that runs without you. It's also where value is most often destroyed — at the handoffs between layers. Understanding webhooks and triggers is what lets a GTM engineer build a machine that operates unattended, which is the whole promise of the role.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Webhooks and triggers, plainly

A webhook is a message one tool sends to another when something happens — 'this event occurred, here's the data.' A trigger is the condition that starts a workflow. Together they let tools drive each other: Clay finishes enriching a row → fires a webhook → an orchestration tool receives it → writes to the CRM → triggers a sequence → posts an alert. No human touches it. This is how the seven layers become one engine instead of seven islands.

Why n8n (and Make): these are orchestration platforms that receive webhooks, transform data, and call other tools' APIs — the middleware that sits between Clay, the CRM, the sequencer, and Slack. n8n is open-source and self-hostable (free), which is why the program uses it. The concept transfers to any orchestrator.

Where handoffs break

Revisit the seven-layer lesson concretely: value is destroyed at handoffs. A webhook that silently fails, a data-format mismatch between tools, a field that's null when the next step expects a value — these are where working systems quietly stop working. Sketch your own system's data flow (Clay → orchestrator → CRM → sequencer → alert) and mark every handoff as a potential break point. This map is what they'll build and harden in the rest of the week.

2026 MARKET REALITY (KNOW THIS COLD)

Automation is named as the core deliverable of the role — hiring teams want people who've built workflows across the full stack, not just used the tools individually.

Webhooks and API basics are an explicitly listed 2026 skill; orchestration is where the earlier API literacy (Day 28) becomes a system-building capability.

RUN THE HOUR

0:00–0:30  Learn how a webhook fires from one tool and drives another, and where handoffs between layers usually break.

0:30–1:00  Sketch the data flow for the system: Clay → ? → CRM → sequencer → alert.

TIPS & COMMON MISTAKES TO AVOID

Mark every handoff on your sketch as a potential failure point — it primes the reliability mindset for the rest of the week.

Keep 'why n8n' about the concept (open-source orchestrator), not the specific tool — orchestration outlasts any one platform.

Resources  devcommx orchestration-layer + n8n intro

### D47 · Week 10, Day 47 — n8n fundamentals

Learn nodes, triggers and workflows hands-on.

Objective:  You can stand up n8n and build a toy workflow (webhook trigger → transform → send a message), understanding how nodes pass data.

WHY THIS MATTERS

n8n is the hands-on core of the orchestration layer. Building even a trivial workflow demystifies automation — you see that a 'workflow' is just nodes passing data along a chain. This foundational fluency is what lets them wire real tools together tomorrow.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Nodes, triggers, and data flow

In n8n, a workflow is a chain of nodes. A trigger node starts it (a webhook received, a schedule, a manual run). Each subsequent node does one thing — transform data, call an API, send a message — and passes its output to the next node. The mental model is a pipeline: data enters at the trigger and flows left to right, changing shape at each node. This is the same building-block thinking as Clay columns, now across tools instead of within a table.

Stand up n8n (cloud trial or self-host — self-host is free) and build a toy workflow: a webhook trigger receives data → a transform node reshapes it → a final node sends you a message (email or Slack). Trivial, but it makes the data-flow concept tangible.

How nodes pass data

The key thing to notice: each node's output is the next node's input, and you reference fields from earlier nodes by name. When something breaks, it's usually because a field a node expects isn't there or is a different shape than assumed. Inspect the data at each node — n8n shows the payload flowing through — because reading the data between nodes is how you debug orchestration.

2026 MARKET REALITY (KNOW THIS COLD)

n8n's open-source, self-hostable model keeps orchestration on the mostly-free learning budget; the node/data-flow concepts transfer directly to Make, Zapier, and custom code.

Hands-on workflow building (not just tool familiarity) is what hiring teams screen for — someone who has built and debugged n8n workflows can speak to real orchestration experience.

RUN THE HOUR

0:00–0:15  Spin up n8n (cloud trial or self-host).

0:15–0:55  Build a toy workflow: webhook trigger → transform → send yourself a message.

0:55–1:00  Note how nodes pass data from one to the next.

TIPS & COMMON MISTAKES TO AVOID

Self-hosting is free but fiddlier; if setup eats the hour, the cloud trial is fine — the concepts are identical.

Inspect the payload at each node. Reading inter-node data is the single most useful debugging habit in orchestration.

Resources  docs.n8n.io + the n8n template gallery

### D48 · Week 10, Day 48 — APIs, JSON & webhooks 101

Get comfortable reading API docs and JSON — no CS degree needed.

Objective:  You can read API docs, call one API in n8n, and parse a field from the JSON response — using Claude to unblock anything unclear.

WHY THIS MATTERS

APIs and JSON are the literacy that underpins everything technical in the stack. Learners who fear them stay stuck at no-code ceilings; those who read them fluently can integrate anything. This session deepens the Day-28 introduction into working competence, and models using Claude as a patient technical tutor.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Reading API docs and JSON responses

Re-ground the pieces from Day 28 in a real integration: methods (GET reads, POST sends), authentication (usually an API key in a header), request parameters, and the JSON response. The skill this session adds is reading API documentation — every API has docs that specify the endpoint, required parameters, and response shape. Find, in any doc, 'what URL do I call, what do I send, and what comes back.'

In n8n, call one API and parse a specific field from the response. JSON is nested labeled data; to extract a value you follow its path. Reinforce that this is the same skill whether in Clay's HTTP column, n8n's HTTP node, or Python later — the concept is portable.

Using Claude to unblock

Model the professional habit: when an API doc or JSON response is confusing, paste it into Claude and ask 'what does this parameter mean?' or 'which field holds the email?' This is not cheating — it's how working GTM engineers move fast. Deliberately use Claude to explain any part they don't get. This normalizes AI as a tutor and sets up the Week-12 coding sessions, where Claude does most of the heavy lifting.

2026 MARKET REALITY (KNOW THIS COLD)

API and webhook fluency is a stated 2026 skill and a gate to the higher-paying technical tier of the role; this is where no-code operators either level up or plateau.

Using Claude to read docs and debug is now standard practice — the 2026 expectation isn't that you memorize every API, but that you can figure any of them out fast with AI help.

RUN THE HOUR

0:00–0:30  Learn methods (GET/POST), auth, headers, and how to read a JSON response and API docs.

0:30–0:55  In n8n, call one API and parse a field from the response.

0:55–1:00  Have Claude explain any part you didn't get.

TIPS & COMMON MISTAKES TO AVOID

Choose an API with clear docs for the first real call — a badly documented API is a demoralizing first experience.

Actively encourage pasting confusing bits into Claude. The goal is fearless doc-reading, and AI assistance is the accelerant.

Resources  docs.n8n.io HTTP node + any REST API primer

### D49 · Week 10, Day 49 — Build a real GTM workflow

Wire your actual tools together.

Objective:  You can build Clay webhook → n8n → HubSpot → sequence → Slack alert, test it with one record, and fix the first break.

WHY THIS MATTERS

This is the payoff of the week — your actual tools wired into one working pipeline. It's the difference between knowing the concepts and having built a real system. And the inevitable first break, then fix, is where the most durable learning happens: real orchestration is as much debugging as building.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Wiring the real pipeline

Build the genuine chain: Clay finishes enriching a row and fires a webhook → n8n receives and parses it → writes the record to HubSpot → triggers a sequence → posts a Slack (or email) alert so a human knows a new lead moved. Every layer of the seven-layer model is now connected: L2 to L4 to L6 to L5, with an alert closing the loop. Test it with a single record end to end.

Hold onto the handoffs — each arrow is a place data could break. Building it with one record makes each handoff inspectable: did the webhook fire? did n8n parse the right fields? did HubSpot get the record with the right values? did the sequence trigger? A single record walked through slowly teaches more than a batch that fails opaquely.

Fix the first thing that breaks

Something always breaks — a field name mismatch, an auth error, a null value, a wrong data type. This is expected and is the point. Learn systematic debugging: inspect the data at each node, find where it stops matching expectations, fix that one thing, re-run. The lesson isn't that it broke; it's that you can find and fix the break. That diagnostic skill is a large part of the actual job.

2026 MARKET REALITY (KNOW THIS COLD)

A working Clay → CRM → sequencer → notification pipeline is a canonical GTM engineering deliverable; 'built workflows across the full stack' is exactly what job postings ask for.

The debugging competence this session builds is undervalued by beginners and prized by employers — 'fix the first thing that breaks (something always does)' is the real texture of the job.

RUN THE HOUR

0:00–0:55  Build: Clay webhook → n8n parses → writes to HubSpot → triggers a sequence → posts a Slack/email alert. Test with one record.

0:55–1:00  Fix the first thing that breaks (something always does).

TIPS & COMMON MISTAKES TO AVOID

Walk one record through slowly and inspect each handoff — batch testing hides which arrow failed.

Treat the first break as the lesson, not a setback. Coach the diagnostic loop: inspect → locate → fix one thing → re-run.

Resources  docs.n8n.io HubSpot + webhook nodes

### D50 · Week 10, Day 50 — Ship: the automated handoff

Deliver a working Clay → CRM → sequencer → notification pipeline.

Objective:  You ship a finished, documented n8n workflow with a screenshot of a successful run.

WHY THIS MATTERS

This deliverable proves you can make a system run without them — the core promise of orchestration. A documented, screenshotted working pipeline is strong evidence of end-to-end technical capability and is exactly the kind of artifact that distinguishes a builder from an operator.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Finishing and documenting the pipeline

Harden yesterday's workflow into something reliable: handle the common failure cases (missing fields, dedup so the same lead isn't double-written), and document what it does — the trigger, each step, the handoffs, and what to check if it breaks. Capture a screenshot of a successful end-to-end run showing data flowing all the way through. The screenshot is the proof; the documentation is what makes it reusable and hireable.

Frame the deliverable as an operational asset: 'this pipeline takes an enriched, qualified lead and automatically puts it in the CRM, starts outreach, and alerts the team — here's a successful run.' That sentence, plus the evidence, is a portfolio piece that speaks directly to the role.

2026 MARKET REALITY (KNOW THIS COLD)

A documented orchestration workflow with proof of a successful run is close to what a real GTM engineer hands off internally — it demonstrates both building and operational thinking.

This pipeline becomes a component of the Week-13 capstone, where all the pieces connect into one full system — so a clean, documented workflow here pays off twice.

RUN THE HOUR

0:00–0:50  Finish and document the n8n workflow with a screenshot of a successful run.

0:50–1:00  Add as deliverable #10.

TIPS & COMMON MISTAKES TO AVOID

Insist on the successful-run screenshot — it's the evidence that separates 'I built a pipeline' from 'here's proof it works.'

Add a short 'if it breaks, check X' note — it turns a workflow into a maintainable system.

Resources  The Week-10 build, hardened and documented

◆  Portfolio deliverable #10: Orchestration workflow

## Week 11 — CRM & RevOps systems

Own the lead-to-revenue flow and keep the data clean automatically.

Days 51–55

### D51 · Week 11, Day 51 — CRM as source of truth

Learn the data model behind HubSpot/Salesforce and when to use which.

Objective:  You can model your company's core objects in HubSpot and explain how accounts, contacts, deals and activities relate.

WHY THIS MATTERS

The CRM (L6) is the source of truth the whole revenue system references — if it's a mess, routing, scoring, and reporting all lie. Understanding the object model is foundational RevOps/GTM engineering knowledge, and HubSpot appears in over half of job postings. This is where you learns to think in structured, relational revenue data.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The CRM object model

A CRM organizes revenue data into objects that relate to each other. Accounts (companies): the businesses you sell to. Contacts (people): individuals at those companies. Deals (opportunities): potential or active sales, with a value and a stage. Activities: the interactions (emails, calls, meetings, tasks) logged against contacts and deals. These relate: a contact belongs to an account; a deal is associated with an account and its contacts; activities attach to contacts and deals. This is the same relational thinking as Clay's lookups (Day 23), now as the system of record.

HubSpot vs. Salesforce: HubSpot is easier, faster to stand up, and free at entry — the common choice for startups and the default in this program. Salesforce is more powerful and customizable but heavier and enterprise-oriented. Learn the 'when to use which' as a maturity/complexity call: HubSpot until the org's needs outgrow it.

Modeling the company's objects

Model your adopted company's core objects in HubSpot: what defines an account, what contact properties matter, what deal stages the sales process has. Then identify one field they'd never let go stale — the field whose accuracy the whole system depends on (often the account's ICP-fit data or the deal stage). Naming that field teaches what 'source of truth' actually means: some data is load-bearing.

2026 MARKET REALITY (KNOW THIS COLD)

HubSpot appears in ~52% of GTM engineering postings (Salesforce ~45%); fluency with at least one CRM's object model is effectively required.

'Data hygiene is non-negotiable — every win traces back to clean, enriched, well-modeled data' is a stated principle of the role; the object model is where that cleanliness is enforced or lost.

RUN THE HOUR

0:00–0:30  Learn objects (accounts, contacts, deals, activities) and how records relate.

0:30–0:55  Model the company's core objects in HubSpot.

0:55–1:00  Note one field you'd never let go stale, and why it's load-bearing.

TIPS & COMMON MISTAKES TO AVOID

Connect back to Clay's lookups — the accounts↔contacts relationship is the same relational idea, so you already have the intuition.

The 'never let it go stale' field is a great discussion — it surfaces what data the whole revenue motion actually depends on.

Resources  HubSpot Academy CRM fundamentals

### D52 · Week 11, Day 52 — Lead routing & rules of engagement

Implement a routing policy as automation.

Objective:  You can build a routing rule (in HubSpot or n8n) for your leads and handle the edge case of missing data.

WHY THIS MATTERS

A great lead is worthless if it sits unassigned or goes to the wrong rep. Routing — automatically getting each lead to the right owner — is a core RevOps function, and doing it as automation (not manual assignment) is the GTM engineering way. Handling the missing-data edge case is where amateurs' rules fall apart and professionals' hold up.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Routing logic

Routing assigns each incoming lead to an owner based on rules: by territory/geo, by company size or segment, by product interest, or round-robin within a team. Learn it as a decision tree — 'if enterprise and US, route to [owner]; if SMB, round-robin the SMB team.' The rules encode the team's rules of engagement (who owns what), turned into automation so no lead waits for a human to assign it.

Implement one routing rule for your leads, in HubSpot's workflow tools or in n8n (connecting to the Week-10 pipeline). The point is that routing is just conditional logic applied to the CRM — the same thinking as Clay's conditional columns, now governing ownership.

The missing-data edge case

The rule that always breaks: what happens when the data the routing depends on is missing or enrichment failed? A lead with no company size can't be routed by size. Learn fallbacks — a default owner or a manual-review queue for un-routable leads — so nothing falls through a crack. Deliberately test a lead with missing data and confirm it lands somewhere sensible rather than vanishing. This edge-case discipline is what makes routing production-grade.

2026 MARKET REALITY (KNOW THIS COLD)

Lead routing and CRM architecture are named parts of the GTM engineer's territory (distinct from RevOps reporting); building routing as automation is squarely the role's work.

Enrichment-failure fallbacks matter because Clay charges per attempt and some lookups return nothing — routing must gracefully handle the rows enrichment couldn't complete.

RUN THE HOUR

0:00–0:25  Learn routing logic (size/segment/geo → owner) and fallbacks when enrichment fails.

0:25–0:55  Build a routing rule (in HubSpot or n8n) for the leads.

0:55–1:00  Test an edge case: what happens with missing data?

TIPS & COMMON MISTAKES TO AVOID

Actually run a missing-data lead through the rule — testing the edge case beats theorizing about it.

Keep the routing rule simple and correct rather than clever and fragile; one solid rule with a fallback beats an elaborate untested tree.

Resources  cleanlist RevOps-vs-GTME routing examples

### D53 · Week 11, Day 53 — Lead scoring & lifecycle

Combine fit and intent into a lifecycle a rep can trust.

Objective:  You can extend your Week-5 fit score with intent signals into a combined CRM score and define the 'contact now' threshold.

WHY THIS MATTERS

This is where the two halves of the program converge: fit (who they are, from Week 5) plus intent (what they're doing, from Week 9) become one score that tells a rep who to contact and when. A trustworthy combined score with a clear action threshold is what makes the whole machine's output usable by humans.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Fit + intent = a combined score

Fit scoring (Week 5) answers 'is this a good-fit account?' Intent scoring answers 'are they showing buying signals right now?' Neither alone is enough — a perfect-fit account with no intent isn't urgent; a high-intent account that doesn't fit isn't worth it. Combining them produces a score that captures both: high fit AND high intent = contact now. Learn this as the synthesis of the program's two threads.

Also cover lifecycle stages (MQL, SQL, and the transitions from Week 2's funnel) as the states a lead moves through, and how the score drives those transitions — crossing a threshold promotes a lead from marketing to sales. The score isn't decoration; it triggers action.

The 'contact now' threshold

The most important output: define the score threshold that means 'a rep should reach out today.' This turns a continuous number into a clear action signal reps can trust. Set it too low and reps drown in mediocre leads; too high and good leads go untouched. Define your threshold and justify it against the top of your scored list — the same 'do the top ones feel right?' calibration from Day 24, now for the combined score.

2026 MARKET REALITY (KNOW THIS COLD)

ICP scoring models and combined fit/intent scoring are named skills interviewers test; a defensible, action-triggering score is a portfolio-grade demonstration.

This combined score is the input to the capstone's full pipeline (Week 13), where fit + intent drives who the whole system prioritizes — it's a load-bearing build.

RUN THE HOUR

0:00–0:25  Learn MQL/SQL, fit vs. intent scoring, and lifecycle stages.

0:25–0:55  Extend the Week-5 fit score with intent signals into a combined score in the CRM.

0:55–1:00  Define the threshold that means 'contact now.'

TIPS & COMMON MISTAKES TO AVOID

Explicitly connect Week 5 (fit) and Week 9 (intent) — this is the session where you see the whole program was building toward one score.

Push for a specific, justified threshold. 'High score = contact' is too vague to act on; a number with a rationale is usable.

Resources  HubSpot lead-scoring docs + the Week 5/9 work

### D54 · Week 11, Day 54 — Data hygiene at scale

Keep the CRM clean without manual work.

Objective:  You can build one automated hygiene rule (e.g. re-enrich stale records or flag duplicates) and explain what breaks when data is dirty.

WHY THIS MATTERS

A CRM decays constantly — people change jobs, data goes stale, duplicates creep in. Manual cleanup doesn't scale, so hygiene must be automated. 'Keep the data clean automatically' is a stated job function, and every win traces back to clean, well-modeled data. This is where you build the immune system of the revenue engine.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Automated hygiene

Data hygiene at scale means rules that keep the CRM clean without a human doing it. Common rules: re-enrich records older than N days (job titles and company data go stale), flag or merge duplicates automatically, standardize field formats on entry, and sync enrichment so CRM data stays current with source data. These run continuously in the background — the CRM stays clean because the system maintains it, not because someone remembers to.

Build one hygiene rule — for example, an automation that flags records with missing critical fields, or re-enriches contacts whose data is older than 90 days (connecting Clay's enrichment to the CRM via the Week-10 orchestration). One working rule demonstrates the pattern.

What dirty data breaks

Make the stakes concrete: dirty data breaks routing (can't route on missing fields), breaks scoring (stale attributes produce wrong scores), breaks reporting (duplicates inflate counts, attribution lies), and breaks outreach (wrong titles, bounced emails). Every downstream system inherits the CRM's data quality. Teaching what breaks is what motivates the discipline — hygiene isn't tidiness, it's keeping the whole engine honest.

2026 MARKET REALITY (KNOW THIS COLD)

'Data hygiene is non-negotiable' is a stated principle; automated hygiene (not manual cleanup) is the scalable, GTM-engineering way to enforce it.

Because Clay's credit model charges for failed lookups on stale/bad data, automated hygiene also protects the budget — clean inputs mean fewer wasted enrichment attempts.

RUN THE HOUR

0:00–0:25  Learn dedup, enrichment sync, and automated hygiene.

0:25–0:55  Build one automated hygiene rule (e.g. re-enrich stale records, flag duplicates).

0:55–1:00  Note what breaks when data is dirty.

TIPS & COMMON MISTAKES TO AVOID

Connect the hygiene rule to the Week-10 orchestration — automated re-enrichment is a natural extension of the pipeline they already built.

Trace one dirty-data failure end to end (bad title → wrong score → wrong routing) — the cascade makes the abstract case for hygiene visceral.

Resources  clay.com CRM data-hygiene / bulk-enrichment guide

### D55 · Week 11, Day 55 — Ship: the CRM system map

Deliver a documented lead-to-revenue model.

Objective:  You ship a diagram plus notes documenting your CRM: objects, stages, routing rules, scoring model, and hygiene automations.

WHY THIS MATTERS

A CRM system map proves you can architect the source-of-truth layer, not just click around in it. It's the RevOps-grade artifact that shows systems thinking — how objects, routing, scoring, and hygiene fit into one coherent lead-to-revenue model. This is exactly the kind of documentation that signals senior capability.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Documenting the lead-to-revenue model

Assemble the week into one map: the object model (accounts/contacts/deals/activities and their relationships), the lifecycle stages and their transition criteria, the routing rules and fallbacks, the combined fit+intent scoring model with its threshold, and the hygiene automations. Present it as a diagram plus explanatory notes — a competent reader should understand how a lead enters, gets scored and routed, moves through stages, and stays clean.

The test: could a new RevOps hire read this map and understand the company's entire lead-to-revenue system? That's the standard for architecture documentation, and it's what makes this a portfolio piece that reads as senior-level systems thinking rather than tool operation.

2026 MARKET REALITY (KNOW THIS COLD)

CRM architecture and lead-to-revenue modeling are core to the role; a documented system map demonstrates the 'builds the infrastructure' capability that distinguishes GTM engineering from RevOps reporting.

This map is a direct input to the Week-13 capstone system design — the CRM is L6 in the full pipeline, so a clear map here accelerates the capstone.

RUN THE HOUR

0:00–0:50  Document the CRM: objects, stages, routing rules, scoring model, hygiene automations — as a diagram + notes.

0:50–1:00  Add as deliverable #11.

TIPS & COMMON MISTAKES TO AVOID

Push for a real diagram, not just prose — systems thinking is best shown visually, and it reads as more senior.

Apply the 'new hire could understand it' test; if it needs verbal explanation, it isn't finished.

Resources  The full Week-11 build, documented as architecture

◆  Portfolio deliverable #11: CRM system map

## Week 12 — The AI layer — coding, Claude Code & agents

Use AI to build 3–5× more than a traditional operator.

Days 56–60

### D56 · Week 12, Day 56 — Why GTM engineers who code earn more

Understand where SQL and Python fit and when to reach for code.

Objective:  You can explain what code unlocks beyond no-code tools and identify 3 things in your system that no-code couldn't do well.

WHY THIS MATTERS

The single biggest pay lever in the role is technical skill — engineers comfortable with code out-earn no-code operators by ~$50K. This session reframes code not as a scary prerequisite but as the tool that removes the ceilings no-code tools hit. And with AI writing most of the code now, the barrier to crossing that line has never been lower.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What code unlocks

No-code tools (Clay, n8n) are powerful but bounded — they do what their builders anticipated. Code removes the boundary: custom logic no tool offers, transformations too complex for a formula, integrations with services that have no pre-built connector, batch operations over data too large for a table, and anything genuinely bespoke. SQL lets you query and manipulate data at scale; Python lets you script arbitrary logic and glue anything to anything. You reach for code when the no-code tool would be awkward, impossible, or hit a limit.

The 2026 reframe: AI now writes roughly 80% of the code for you. The skill is no longer 'memorize syntax' — it's knowing what to build, reading and directing AI-generated code, and running it. That shift is why a non-CS background can now cross into the technical tier faster than ever, and why the pay premium is accessible rather than gated behind a degree.

Finding the candidates for code in your own system

Audit your system from Weeks 4–11 and name three things no-code couldn't do well — a transformation that was clumsy in a formula, an integration that didn't exist, a batch job that would be painful in a table. These become the candidates for a script in Day 60's deliverable. Grounding 'why code' in your own system's limits makes it concrete rather than abstract.

2026 MARKET REALITY (KNOW THIS COLD)

Technical GTM engineers (SQL, Python, custom APIs, Claude Code) earn ~$50K+ more than no-code peers; over a third of postings explicitly require programming, and the real figure is likely higher.

A common senior stack is SQL + Python + a CRM + an enrichment tool + at least one LLM-orchestration tool — code sits alongside, not instead of, the no-code layer.

RUN THE HOUR

0:00–0:30  Learn what code unlocks beyond no-code tools, and that AI now writes ~80% of it for you.

0:30–1:00  List 3 things in your system that no-code couldn't do well — candidates for a script.

TIPS & COMMON MISTAKES TO AVOID

Reframe code as ceiling-removal, not a new career. Learners intimidated by 'programming' relax when it's 'the thing that does what Clay can't.'

Ground the three candidates in your actual system — abstract 'maybe I'd use code somewhere' doesn't motivate; 'this exact clumsy step' does.

Resources  gtmepulse tools report + cleanlist skill-stack notes

### D57 · Week 12, Day 57 — Python for GTM (with AI help)

Read and run a simple script that touches an API.

Objective:  You can run a small Python script (with Claude's help) that calls an API and transforms the result, then change one thing and re-run.

WHY THIS MATTERS

This is the first real code, and the goal is to remove fear, not to make anyone a software engineer. Running a script that does something useful — with Claude writing most of it — proves you can operate in code with AI support. That confidence is the gateway to the higher-paying technical tier.

WHAT YOU'LL LEARN — THE CORE MATERIAL

The minimum Python that matters

Learn only what's needed to be dangerous: variables (named values), a function (reusable block of logic), an API call (using a library to hit an endpoint), and a loop (do something for each item). That's enough to write scripts that automate real GTM tasks. Don't try to learn comprehensive Python — learn the pieces that appear in a script that calls an API and processes the response.

The workflow is AI-assisted from the start: describe what you want to Claude ('write a Python script that calls this API for each row in a CSV and adds the result as a new column'), read the code it produces, run it, and understand what each part does. You direct and reads; Claude writes. This is exactly how technical GTM work happens in 2026.

Change one thing and re-run

After running the script, Change one thing — a parameter, the field being extracted, the API called — and re-run. This is where understanding forms: seeing how a change in the code changes the output builds real intuition, versus passively running someone else's script. The 'modify and observe' loop is how non-engineers learn to actually work in code.

2026 MARKET REALITY (KNOW THIS COLD)

The 2026 baseline is comfort with SQL/Python 'to solve problems independently' — not to write production software. AI assistance makes this reachable for GTM-background you.

'With Claude's help, run a small script' reflects how the work is actually done — the valued skill is directing and reading AI-generated code, which is precisely what this session practices.

RUN THE HOUR

0:00–0:20  Learn Python basics: variables, a function, an API call, a loop.

0:20–0:55  With Claude's help, run a small script that calls an API and prints/transforms the result.

0:55–1:00  Change one thing and re-run to see how the change propagates.

TIPS & COMMON MISTAKES TO AVOID

Keep it to a script that does one useful thing. Ambition here overwhelms; a small win builds the confidence that matters.

The 'change one thing and re-run' step is the real learning — don't skip it for time. Modifying beats passively running.

Resources  claude.ai + any Python-basics quickstart

### D58 · Week 12, Day 58 — Claude Code & the terminal

Build a tiny custom GTM tool from the command line.

Objective:  You can install Claude Code, have it build a small tool (e.g. a CSV enricher or list deduper), and run it on real data.

WHY THIS MATTERS

Claude Code is the agentic tool that lets a GTM engineer build custom tools by describing them, without deep coding expertise. It's a named part of the highest-earning technical stack. Building even a tiny tool from the terminal shows you they can create bespoke capabilities on demand — a genuine superpower for the role.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What Claude Code is and the basic loop

Claude Code is an agentic coding tool that works from the command line (or desktop/mobile app): you describe a task in plain language, and it writes, runs, and iterates on code to accomplish it, asking for direction as needed. The basic loop: install it, tell it what you want built, review what it does, run the result, and refine by describing changes. It handles the code; you supplies the intent and the judgment about whether the output is right.

This is the practical face of the 'AI writes 80% of the code' reality. A GTM engineer using Claude Code can build a custom enricher, a data cleaner, a bespoke integration — things that would otherwise require a developer — by describing them clearly and directing the iteration.

Building a small real tool

Build something small but genuinely useful on real data: a script that enriches a CSV (adds a computed or looked-up field to each row), or one that dedupes a messy list, or reformats data for import. Then run it on your actual Week-3/4 data. The point is the end-to-end experience — describe, build, run on real data, see it work — which demystifies custom tooling entirely.

2026 MARKET REALITY (KNOW THIS COLD)

Claude Code is named as part of the technical stack that earns $50K+ more; it's specifically called out as a differentiator for the highest-paying roles.

The install/requirements and current capabilities can change — check the official Claude Code docs before teaching this niche so setup instructions are accurate.

RUN THE HOUR

0:00–0:20  Install Claude Code and learn the basic loop (describe → build → run → refine).

0:20–0:55  Have it build a small tool (e.g. a script that enriches a CSV or dedupes a list).

0:55–1:00  Run it on real data.

TIPS & COMMON MISTAKES TO AVOID

Verify current install steps from the official docs before class — agentic tools update often and stale instructions derail the hour.

Pick a tool that solves a real annoyance from earlier weeks (deduping, reformatting) so the payoff is immediately felt.

Resources  docs.anthropic.com Claude Code docs (verify current install steps)

### D59 · Week 12, Day 59 — MCP & AI agents

Connect tools to an AI and understand AI-SDR-style agents.

Objective:  You can explain what MCP is, connect one tool via MCP (or design an agent workflow), and run one instruction through it.

WHY THIS MATTERS

MCP (Model Context Protocol) is how AI models connect to tools and act on real systems — the foundation of agentic GTM. Understanding it, and how AI-SDR-style agents differ from a hand-built stack, is the frontier of the role. This is the L7 capstone concept: AI that doesn't just research and write, but runs plays.

WHAT YOU'LL LEARN — THE CORE MATERIAL

What MCP is

MCP (Model Context Protocol) is an open standard for connecting AI models to external tools and data sources. Instead of an AI being a closed chat box, MCP lets it call tools — read a CRM, query a database, send a message, run a workflow — through a standard interface. It's the plumbing that turns a language model into an agent that can act on your actual systems. Learn it as 'the USB port for AI-to-tool connections' — a common standard so any MCP-compatible tool can plug into any MCP-compatible model.

Either connect one tool via MCP and run a single instruction through it, or (if setup is heavy) design the agent workflow on paper: what tools the agent can access, what instruction it takes, and what it does step by step. Either way, the learning is understanding how an AI agent is wired to real tools.

AI SDRs vs. a custom stack

Learn the important distinction: 'AI SDR' products promise an autonomous agent that prospects and emails for you out of the box. A custom stack (what this program built) is composed of Clay, orchestration, CRM, and targeted AI — more work to build but fully controllable, transparent, and tuned to the specific ICP. Learn the tradeoff honestly: AI SDRs are convenient but generic and opaque; a custom stack is the GTM engineer's craft — more capable and defensible when built well. This is why the role exists: someone has to build and control the system, whether or not off-the-shelf agents are in the mix.

2026 MARKET REALITY (KNOW THIS COLD)

MCP is the emerging standard for tool-connected AI agents; understanding it is increasingly expected as agentic workflows move into GTM.

The market view is that a well-built custom stack outperforms generic AI-SDR products for a specific ICP — which is precisely the value a GTM engineer provides over buying an off-the-shelf agent.

RUN THE HOUR

0:00–0:30  Learn what MCP is, how it connects tools to an AI, and how AI SDRs differ from a custom stack.

0:30–1:00  Connect one tool via MCP (or design the agent workflow on paper) and run one instruction through it.

TIPS & COMMON MISTAKES TO AVOID

If MCP setup is heavy, the paper design is a fully valid substitute — the concept (AI wired to tools) is the objective, not a specific integration.

Give the AI-SDR-vs-custom-stack tradeoff evenhandedly — you will be asked about it, and the honest answer (it depends) shows maturity.

Resources  modelcontextprotocol.io + clay.com Claude/ChatGPT workflow posts

### D60 · Week 12, Day 60 — Ship: a custom tool

Deliver one script or agent that does what no-code can't.

Objective:  You ship a small custom tool (Python script, n8n code node, or MCP-connected workflow) with documentation of what it does and why.

WHY THIS MATTERS

This deliverable is the proof of technical capability that unlocks the higher-earning tier of the role. Even a small custom tool demonstrates you can go beyond no-code ceilings — the exact thing that separates $127K operators from $250K technical engineers. It's one of the most differentiating pieces in the portfolio.

WHAT YOU'LL LEARN — THE CORE MATERIAL

Finishing and documenting the custom tool

Take one of the three no-code-can't-do-it candidates from Day 56 and build it into a finished small tool — a Python script, an n8n code node, or an MCP-connected workflow. It should do one useful thing that the no-code stack couldn't do well. Then document what it does and why it needed code: what limit it removes, what it takes as input, what it produces. The 'why code' explanation is as important as the tool — it shows you understands when code is the right choice.

Frame the deliverable modestly but clearly: this isn't production software, it's evidence you can reach past no-code limits with AI assistance. That evidence is what the technical pay premium rewards.

2026 MARKET REALITY (KNOW THIS COLD)

A custom tool is the portfolio piece that signals membership in the technical tier — the one that correlates with the ~$50K pay premium.

Because AI writes most of the code, 'shipped a working custom tool' is now an achievable, honest claim for a GTM-background you — and a credible one to a hiring manager.

RUN THE HOUR

0:00–0:50  Finish the small custom tool (Python script, n8n code node, or MCP-connected workflow) and document what it does + why.

0:50–1:00  Add as deliverable #12.

TIPS & COMMON MISTAKES TO AVOID

Small and working beats ambitious and broken. A tidy script that reliably does one thing is a stronger portfolio piece than a half-built agent.

Require the 'why it needed code' note — it demonstrates judgment about when to reach past no-code, which is the actual skill being shown.

Resources  The Day-56 candidates + Claude Code / Python from this week

◆  Portfolio deliverable #12: Custom GTM tool