# Kushagra session: Skills needed to crack future GTM engineering roles (2026-08-29)

## TL;DR
- GTM engineering exists because Clay built its early wedge through agencies doing outbound — that history is why the role still skews outbound-centric even as it starts overlapping with RevOps.
- The role is stage-agnostic but shape-shifts: early-stage = foundation building, post-Series-B = more RevOps-flavored work; it fits best under sales or growth leadership in sales-led B2B companies.
- The center of gravity is moving from Clay/no-code tools toward coding agents (Claude Code, Codex, Open Code) driving things via direct API endpoints — but Clay stays useful for its data-provider access and features like audience/ads matching that aren't worth rebuilding.
- The single biggest technical warning: dumping thousands of rows into a coding agent's context and asking it to "just research all of these" causes context degradation, hallucination, and silent quality collapse past ~50% of the context window — the fix is deterministic orchestration (scripts that stream/save results, are resumable, and treat the agent as an orchestrator, not the whole pipeline).
- Proof of work beats credentials and courses: doing work for free, answering questions in the Clay Slack community, and "value bombing" (building and giving away useful tools) are the fastest, most repeatable ways to break in.
- Niches: blue-collar/offline services (plumbing, landscaping, gyms) are easier to penetrate (less-saturated inboxes, high responsiveness) for building early proof of work; PE/VC deal-brokering outreach is a high-dollar niche once you have the experience.

## Who the speaker is
Kushagra Tiwari — GTM engineer at Starbridge; previously a lawyer, then a product manager (first PM at B2B company Spotdraft), then ran his own outbound agency for ~2 years; competed in the Clay World Cup, coaches for Clay Bootcamp, and built their "Cold Email Machine" course (focused on orchestration via coding agents, i.e. life after Clay for power users).

## Key insights (grouped by theme)

**The role**
- Origin story: Clay's early growth was built on agencies as power users, focused on outbound — this is the direct reason most GTM engineering roles today are still outbound-centered, even as the role's scope expands toward RevOps.
- CRM is not optional even in an outbound-only role: you still need your TAM stored somewhere accessible to the team, need to push/pull engagement and scoring data, and need attribution/pipeline tracking to work. A minority of boutique agencies (e.g., "Sculpted") specialize purely in CRM enrichment/cleaning, but that's the exception.
- Titles don't matter much (GTM engineer vs. growth engineer vs. "applied AI GTM engineer" are largely the same job); what matters is systems-thinking capability and the ability to build AI-driven workflows from scratch rather than mastery of one tool.
- It's overwhelmingly an individual-contributor (IC) role right now — no established "GTM engineering team/VP" org structure exists yet at most companies. Cited concepts: "high-impact IC" (Elena Verner, head of growth at Lovable) and Lenny's "super IC" — senior people moving back into IC roles because modern tooling lets one person own an end-to-end motion that used to require a team of SDRs.
- Long-term trajectory: Kushagra expects the role to evolve into a "pseudo-engineer" — deep technical/harness proficiency combined with genuine sales fluency (conversions, copy, ICP segmentation) — which is what will keep it distinct from a pure software engineer.

**Skills/tools**
- Multi-channel orchestration (email + calling combined) meaningfully multiplies conversion — e.g., calling a positive email responder within 5 minutes maximizes close rate.
- Coding proficiency (Python, SQL, JavaScript) is "beneficial but not intimidating" — the goal is to be able to audit a coding agent's output and understand rate limits/endpoints, not to become a full-stack engineer. SQL specifically was called "a couple of hours" to get functional in, since LLMs are very strong at generating it.
- List building remains a real, monetizable skill even in the API/coding-agent era — Yogesh's own experience: sticking to list-building quality (using ~8 data sources, no signals/intent) generated strong outbound results for niche industries like insurance.
- CRM basics for beginners: learn the core objects (accounts, contacts, opportunities/deals) and their properties first, then how to fetch/push data to them, then move on to analytics/reporting.
- No-code tools (n8n, Make) are being displaced by custom code/coding agents for control and quality, but pre-built connectors still win for one-off integrations (e.g., pulling an exclusion list from a CRM) where rebuilding the connector from scratch would waste time.

**AI & coding agents**
- "Harness engineering" is the emerging core skill: a coding agent should function as an *orchestrator* over a deterministic script (Python/JS) that makes the actual API calls, streams results, and saves them incrementally — not as the thing doing 1,000 rows of "research" directly in one prompt.
- Concrete failure mode described: dumping an Apollo API key into a coding agent and saying "search for these people and save it" without instructions about rate limits/streaming — this causes timeouts, data loss (you pay for the credit but get nothing back), and silent divergence in later rows once context degrades.
- The fix: explicitly instruct the agent (or write scripts) so work is resumable after a crash, results are streamed/saved incrementally, and you understand the target API's rate limits and endpoints well enough to direct the agent correctly — "knowing which questions to ask is more important than knowing how to code it yourself."
- Infrastructure recommendations: Supabase, Edge Functions, or Cloudflare Workers to run workflows asynchronously so they don't rely on someone's laptop staying open; Slack as the team-facing interface (minimizes context-switching for teammates already living in Slack); trigger.dev for async job orchestration.
- Clay vs. coding agents isn't binary: "you can do everything in Clay in a coding agent, but should you?" — Clay is worth keeping for cheap-per-lookup access to many data providers via one subscription and for features like ads audience-matching that aren't worth recreating.

**Hiring & portfolio**
- What Kushagra looks for hiring an entry-level GTM engineer: (1) a real conversation backed by actual numbers (replies, pipeline, meetings booked) as a pre-filter for follow-up questions, (2) prior use of Clay specifically — because that experience carries over into how you think even once you move to a coding agent, and (3) evidence of having built something in a coding agent and shipped a result.
- On "proof without a real project": doing work for free is the accepted path — his blunt framing was that if you can't sell your own services for free to get your first result, breaking into a sales-adjacent role will be difficult (an explicit exception is made for people with strong technical chops who can show projects instead).
- Clay Bootcamp / paid courses: he does not believe paid courses are required to succeed — the actual value is networking with experienced agency owners in the room, not the curriculum itself; he's a self-taught practitioner and coaches without having taken the course.
- Customize outreach to agencies/roles: sending a generic 2–3 workflow portfolio is weaker than building a workflow specific to that agency's actual niche/client base and showing exactly what you'd have built for their clients.

**Niches / learning approach**
- Domain expertise is a real unlock — coming from legal tech and selling into lawyers, for example, means you already speak the buyer's language.
- Easier niches for building early proof of work: blue-collar/offline services (plumbing, landscaping, roofing, gyms, dental clinics) — inboxes aren't saturated, contact data is harder to find (so competitors don't bother), and response rates on something as simple as `info@` are high.
- High-value niche once established: PE/VC outreach acting as a broker for a deal — potentially taking a percentage of the deal rather than a flat outbound fee.
- Learning system-thinking: it's a byproduct of repeated building — either build your own passion projects, recreate workflows you find online, or (fastest) hang out in the Clay Slack and build a solution every time someone posts a support question. He personally spent ~8 hours/day early on doing exactly this.
- Avoid "human-wrapper" mode with coding agents: use a learning/verbose mode (he cited Claude Code's approach of surfacing what it did and why) and stay in the loop overseeing early work, rather than blindly delegating and losing understanding of what the agent actually built.
- On the pace of learning never ending: don't chase every new tool/trend by reflex — the important thing is knowing there's a solution to a given problem (or knowing where to look), not memorizing every tool name; it's fine to miss some hype cycles (e.g., knowledge graphs → RAG → back to graphs) and still do well.

## Practical advice to act on (checklist)
- [ ] If building anything with a coding agent over many rows/companies, script the API calls yourself (or have the agent write the script) so results stream/save incrementally and the job is resumable — never just "dump the CSV and ask for research."
- [ ] Learn CRM objects (accounts, contacts, opportunities) and how to fetch/push to them before moving to analytics/reporting.
- [ ] Keep Clay in the stack for data-provider breadth and ads/audience matching even while building most orchestration in a coding agent.
- [ ] Build free work or community-support answers (e.g., in the Clay Slack) as your first proof of work rather than waiting for a paid project.
- [ ] When reaching out to an agency or company, tailor the actual built workflow to their specific niche/clients, not a generic portfolio.
- [ ] Pick a niche where you already have domain expertise, or default to less-saturated blue-collar/offline verticals to build early wins.
- [ ] Stay "in the loop" with coding agents — use a learning/verbose mode and review what was built rather than fully delegating.

## Notable Q&A (paraphrased)
- **Shivani** — "Is GTME splitting into 'table enrichment' vs. 'AI agent building,' and is there a separate 'applied AI GTM' title emerging?" → Don't over-index on titles; the real split is agency (narrower, hand-off responsibility) vs. in-house (owns the full pipeline, needs systems architecture); most things people call "agents" today are really just workflows, since a true agent needs actual decision-making agency.
- **Yogesh** — "Is CRM cleaning/RevOps becoming a bigger part of the role?" → Still a minority focus area; CRM interfacing is necessary everywhere but pure CRM-only roles remain rare (cites boutique agency "Sculpted" as one of few exceptions).
- **Deblina Boral** — "A founder posted a job saying 'we don't use Clay, learn to do it all in Claude Code' — is Clay becoming obsolete?" → You *can* do most of it in a coding agent, but shouldn't for everything — Clay still wins for cheap multi-provider data access and native features like ads/audience matching.
- **Rithika** — "How do I transition from a growth background with no recent campaign evidence — agency first or in-house?" → Agency first, since it's faster to find remote openings and builds proof-of-work fastest; in-house pays off more for long-term impact once you already have results.
- **Yogesh** — "At what point does the learning ever stop — can GTM engineers eventually 'coast' like doctors do after training?" → No — learning doesn't stop, and AI hasn't reduced anyone's workload; but you don't need to chase every tool, only know that a solution exists (or where to find it) when you hit a real problem.
- **Snigdha** — "How did you self-teach GTM specifically (not just tools)?" → Early on, learned via conversations with engineer friends; now the fastest path is treating a coding agent as "the smartest engineer you'll ever have access to" — ask it real questions, stay in learning mode, don't become a "human wrapper."
- **Rakesh** — "Will demo/practice projects suffice as proof, since we don't have real client results?" → Yes in principle, but the fastest way to get a *real* project is to do the first one for free — that itself is the entry point most people (including Kushagra) used.

## What this means for Deepu
- Her engineering background directly satisfies Kushagra's "technical fluency" bar and then some — her differentiator should be demonstrating harness-engineering discipline (deterministic, resumable orchestration) rather than proving basic coding ability.
- The context-window/hallucination warning is highly relevant to the Saffron build if it involves researching many companies via a coding agent — batch/stream results and checkpoint rather than dumping a large company list into one prompt.
- Kushagra's Clay-vs-coding-agent framing ("can vs. should") is a useful lens for deciding which parts of the Saffron pipeline belong in Clay (data-provider lookups, any ads/audience matching) versus a custom script (bulk research orchestration, resumability, cost control).
- Given her data-pipeline background, she's well positioned to pursue the "in-house SaaS GTM engineer" path Kushagra describes (more RevOps/systems-architecture flavored) rather than the outbound-agency entry path most non-technical cohort members are pointed toward.
- The "proof of work over credentials" theme reinforces that a polished, well-documented Saffron Clay/coding-agent build is more valuable for her job search than the cohort certificate itself.
