# Strategy Document — Saffron (v2)

Built by: Deepshikha · v2 adds SOM, segmentation, personas, ranked signals, messaging and list-build filters to the v1 doc (sections marked **[v2]**).

## Company Snapshot

- Company: Saffron
- HQ: San Francisco, California
- Founded: 2025 · YC Spring 2026 · team of 3
- YC: https://www.ycombinator.com/companies/saffron
- Website: https://www.trysaffron.ai/
- LinkedIn: https://www.linkedin.com/company/trysaffron/

## What Saffron Does

Saffron is an AI-native technical assessment platform. Candidates build a real feature on the hiring company's own codebase inside a browser IDE with Claude Code. Saffron records the whole process (prompts, diffs, edits, decisions), attributes every line as human-written, AI-generated or AI-modified, and has 10+ independent AI review agents score the work against the company's rubric. Hiring teams get a session replay and a scored report in hours, with zero interviewer hours.

Positioning line: "See who's engineering and who's vibecoding."

## Problem Being Solved

AI has changed how software engineers work, but technical hiring still runs on a pre-AI playbook. Coding tests either ban AI, constrain it, or can't see how the candidate used it. The result is a slow, expensive loop that measures the wrong thing: 3–4 weeks, 8+ interviewer hours and more than $500 per candidate (Saffron's own figures). Saffron measures the candidate's engineering process, judgment and AI fluency instead of only the final code.

## Founders

| Founder | Role | Background |
|---|---|---|
| Robert Chondro | Founder / CEO | Math & Computer Science, MIT; formerly Jane Street |
| Jerry Yao | Founder / CPO | Computer Science & Math, Stanford; formerly Jane Street |
| Kazuma Choji | Founder / CTO | CS/Math, Harvey Mudd; research published at NeurIPS, ICML and ICCV |

## [v2] Offer, Pricing & Proof

- Basic $199/month (5 assessments) · Standard $499/month (15 assessments, most popular) · Enterprise custom (unlimited) · extra assessments $49 each.
- First assessment offered free: this is the natural call-to-action for outbound.
- Proof we can use today: the "3–4 weeks / 8+ interviewer hours / $500+ per candidate" status quo versus "results in hours, zero interviewer hours". No public customer logos yet, so the founders' pedigree (Jane Street, MIT, Stanford, YC) is the credibility lever.
- Competitors / status quo: HackerRank, CodeSignal, Rounds.so, and in-house take-homes plus pair-programming loops.

What the pricing tells us about the ICP: $199–$499/month is self-serve, credit-card pricing. The fastest wins are companies hiring roughly 3–15 engineers a quarter where the CTO or VP Eng can say yes without procurement, which means 50–500 employees. Enterprise (1,000+) is real but a longer, later motion.

## Ideal Customer Profile (ICP)

### Firmographic Profile

- Company type: growth-stage, engineering-heavy technology companies; enterprise as an expansion segment
- Employees: 50–5,000+; **priority 50–500** [v2 tightened from 50–1,000 based on pricing]
- Revenue / funding: venture-backed (Seed+ to Series C) or established companies with a recruiting-software budget
- Geography: primarily US; secondary Canada, UK and Europe
- Industries: AI, SaaS, Developer Tools, Cybersecurity, FinTech, HealthTech, Cloud/Infrastructure, E-commerce and Marketplaces
- Engineering team: a meaningful engineering organization with recurring hiring
- AI maturity: AI coding tools or agents already in use or being rolled out
- Current assessment: coding tests, take-homes, pair programming, technical interviews or work trials
- Key pain points: interviewer overload, slow hiring, weak assessment signal, take-home review burden, AI misuse or over-reliance, inconsistent evaluation

### Decision Makers

- CTO / VP Engineering / Head of Engineering
- VP / Head of Talent Acquisition
- Head of Technical Recruiting
- CPO / VP People where recruiting tooling is centrally owned

### Champions

- Engineering Managers / Directors
- Technical Recruiting Managers / Recruiters
- Engineering Talent Partners
- Interview-program owners
- Senior / Staff Engineers involved in hiring

### [v2] Disqualifiers (do not target)

- Fewer than 20 engineers, or no SWE openings in the last 180 days
- IT services, outsourcing and staffing agencies (they sell engineers rather than hire for their own product; a different motion)
- Government, defense and on-prem-only companies that cannot run candidate code in a cloud IDE on their codebase
- Existing Saffron customers or any company where a founder conversation is already underway

## TAM — Total Addressable Market

A broad global market of companies that hire software engineers and use technical assessment.

- US + Canada + Europe + other major engineering markets
- 50–5,000+ employees
- Industries: SaaS, AI, Developer Tools, Cybersecurity, FinTech, HealthTech, E-commerce, Cloud/Infrastructure, Marketplaces, IT Services and other technology-intensive sectors
- Hiring profile: recurring software-engineering / technical hiring
- Assessment profile: coding tests, technical interviews, take-homes, pair programming or work trials

Countable TAM: **~54,000 companies** (Prospeo, 28 Sep 2026). Filters: HQ in US / Canada / UK / Germany / Netherlands / France; 51–5,000 employees; Software Development; Technology, Information and Internet; Financial Services; Hospitals and Health Care. [screenshot]

## SAM — Serviceable Addressable Market

Companies with recurring SWE hiring, AI-tool adoption and a meaningful technical-assessment process.

- Primarily US; Canada / UK / Europe secondary
- 50–5,000+ employees; priority 50–500
- Industries: AI, SaaS, Developer Tools, Cybersecurity, FinTech, HealthTech, Cloud/Infrastructure and engineering-heavy technology businesses
- Hiring: active or recurring hiring for Software Engineers, Full-Stack, Backend, Frontend, ML/AI and other technical ICs
- AI maturity: engineering teams already using or actively adopting AI coding assistants or agents
- Process pain: technical-interview burden, take-home scalability, interviewer hours, inconsistent evaluation, weak visibility into reasoning and AI reliance
- Buying triggers: a hiring surge, new talent or engineering leadership, an interview redesign, AI adoption, or pressure to increase hiring velocity

Countable SAM: **~12,000 companies** (Prospeo, 28 Sep 2026). TAM filters + Engineering & Technical headcount ≥ 20 + headcount growth ≥ 1% over the past 6 months (stand-in for active hiring; Job Posting is locked on the free plan). [screenshot]

## [v2] SOM — Serviceable Obtainable Market

What a 3-person founding team can realistically win in the next 12 months through founder-led plus GTM-engineered outbound.

- Scope: **US only, 50–500 employees, Seed to Series C, AI / DevTools / SaaS, with at least 5 open SWE roles in the last 90 days** and a visible AI-coding-tool footprint.
- Reasoning:
  - US-first matches the SF founders, their time zone and the YC network.
  - 50–500 employees fits self-serve pricing and a single decision maker (CTO/VP Eng).
  - Active SWE hiring means the pain is live this quarter, not hypothetical.
  - AI-tool adoption means they already believe "AI changed engineering", so there's no need to convince them the problem exists.
- Sizing logic: SOM ≈ SAM(segment 1 + 2 filters) × reachable (verified decision-maker email or LinkedIn) × realistic win rate. With the measured SOM of **2,921 companies**, working ~1,200 of them in 12 months at a 1.5–2% account-to-close rate gives **~20–25 paying teams**. At the $499 Standard tier that is roughly **$120–150K ARR**, a credible YC-stage target.
- Per D11–D12 guidance: treat these numbers as hypotheses to validate after the first campaign experiments, not as final truth.

Countable SOM: **2,921 companies** (Prospeo, 28 Sep 2026). US only; 51–500 employees; founded 2012 or later (stand-in for venture-stage; Funding is locked on the free plan); plus the SAM filters. Funnel: ~54,000 → ~12,000 → 2,921. [screenshot]

## [v2] Segmentation (campaigns are built per segment)

| # | Segment | Filters | Core pain | Why attack now |
|---|---|---|---|---|
| **S1 (attack first)** | AI-native & DevTools startups | US · 50–200 employees · Seed–Series B · AI / DevTools / SaaS · ≥5 SWE openings | Founders and CTO interview every candidate themselves; engineering time is the scarcest resource; they need people who ship *with* AI | Clearest pain, AI-tool adoption near-universal, CTO is reachable and decides alone, fits $199–$499 pricing |
| S2 | Growth-stage SaaS / Cloud / Cybersecurity | US + Canada · 200–1,000 employees · Series B–D · ≥10 SWE openings | Interviewer overload across many loops, inconsistent evaluation between interviewers, slow time-to-hire | Hiring volume is high and a TA function exists (champion + decision maker), so the Standard or Enterprise tier applies |
| S3 | FinTech / HealthTech (regulated) | US + UK · 200–2,000 employees | Need auditable, consistent and fair evaluation; worried about AI misuse in take-homes | Session replay plus line-level attribution is a strong compliance and fairness story; longer cycle, so it goes third |

Pick: **S1 first.** It has the sharpest pain, the easiest signals to detect (job posts and AI-tool mentions), reachable buyers and no procurement. Every Clay build in this program targets S1 first.

## [v2] Personas

**Primary — "Priya, CTO / VP Engineering at a 120-person AI startup"**
Owns shipping velocity and team quality; measured on roadmap delivery and hiring plan attainment. Her bad day: three take-homes to grade tonight, two on-site loops tomorrow that pull four senior engineers off the roadmap, and a gut feeling that last month's hire "interviewed well but can't actually drive Claude Code". She wants evidence of how a candidate works, not just whether the code compiles.

**Champion — "Marcus, Technical Recruiting Lead / Engineering Manager"**
Owns time-to-hire and candidate experience; measured on offers accepted per quarter. His bad day: chasing interviewers for feedback that's inconsistent from one to the next, and candidates dropping out of a four-week process.

## Signal

Observable characteristics that show a company is a good fit for Saffron.

- High software-engineering hiring: regular hiring of software engineers
- Large or growing engineering team: significant engineering headcount or continued growth
- Engineering-centric business: product or revenue depends heavily on engineering talent
- AI coding-tool adoption: engineers already use tools such as Claude Code, Cursor or Copilot
- Existing technical-assessment process: coding tests, take-homes, pair programming or technical interviews

## Intent

Observable actions or events that show a company is actively looking for a solution like Saffron.

- Technical hiring surge: a sudden increase in software-engineering openings
- Interview-process redesign: the company is changing or reviewing its technical assessment process
- AI-hiring discussions: leaders publicly discussing how AI is changing engineering hiring or evaluation
- New engineering or talent leadership: a new CTO, VP Engineering, Head of Talent or Technical Recruiting leader joins
- Hiring quality or efficiency pain: evidence of concerns about interviewer bandwidth, slow hiring, inconsistent evaluation or poor candidate quality

## [v2] Top 5 signals, ranked by ease of detection

| Rank | Signal / intent | Type | How we detect it (tool) | Detection cost | Message it justifies |
|---|---|---|---|---|---|
| 1 | **SWE hiring surge**: ≥5 open engineering roles, or openings up vs last quarter | 3rd-party signal | Clay job-openings enrichment / Apollo "job postings" filter / careers page via Claygent | Low | "Hiring N engineers this quarter means ~8 interviewer-hours × N…" |
| 2 | **Recent funding** (last 180 days) | 3rd-party signal | Clay company enrichment (funding date) → formula "days since funding"; verify on Crunchbase | Low | "Congrats on the Series A; the hiring plan that follows is where interview time disappears." |
| 3 | **New eng/talent leader** (CTO, VP Eng, Head of TA joined in the last 180 days) | Intent | Clay "Find people" + job-start-date, or Clay Signals (job change) | Medium | "New leaders usually redesign the interview loop in their first 90 days…" |
| 4 | **AI coding-tool adoption**: job descriptions or eng blog mention Cursor, Claude Code or Copilot | Signal | Claygent over the careers page and job posts (cheap model first) | Medium | "Your JDs ask for Cursor/Claude Code fluency. How do you test that today?" |
| 5 | **AI-hiring discussion**: a leader posts about AI changing engineering interviews | Intent (warmest) | LinkedIn / Sales Nav keyword search and alerts; Claygent on the leader's recent posts | Higher | Reference the post directly: warmest opener |

Build order: rank 1 + 2 in the first Clay pass (cheap, broad), rank 3 + 4 only on qualified rows (run-only-if), rank 5 manually for Tier-1 accounts.

Weighting note (Yogesh, D25–D26): recent funding is easy to detect but a *weak* buying signal on its own. Use it as a tiebreaker in scoring, not a qualifier. New engineering or talent leadership, plus sustained hiring volume (≥10 open roles, or roles open for more than 30 days), are the stronger qualifiers. Companies with **no recruiting / TA team at all** are disqualified, because they hire through agencies and agencies don't buy assessment tools directly.

## [v2] Messaging: one-liner offer per segment

Structure: value (buyer's outcome) → pain (what they feel) → proof (reason to believe). Five-word test: the first five words must be about *their* world.

- **S1 AI-native startups:** "Your engineers ship with AI. Your interviews don't test it. Saffron has candidates build a real feature in your codebase with Claude Code, then scores how they used AI, with zero interviewer hours and results the same day."
- **S2 Growth SaaS:** "Eight interviewer-hours per engineering hire adds up fast. Saffron replaces the take-home and first technical round with an AI-scored assessment on your own codebase, so every candidate is judged against the same rubric."
- **S3 FinTech / HealthTech:** "Can you prove a take-home wasn't written by ChatGPT? Saffron records every prompt and attributes each line to human or AI, giving you an auditable, consistent technical evaluation."

CTA for all segments: "Want to run your next candidate through it free?" (Saffron offers the first assessment free.)

Sample S1 opener using signals 1 + 4:
"Hi {first_name}, saw {company} has {n} engineering roles open, and the JDs ask for Cursor/Claude Code experience. Curious how you're testing that in interviews today? Most teams we talk to are still using LeetCode-style rounds that ban AI entirely."

## [v2] List-build filters (use these for the TAM/SAM/SOM screenshots)

**Apollo: Companies tab**
- Location: United States
- # Employees: 51–200 (S1); 201–500 and 501–1,000 (S2)
- Industry and keywords: Computer Software, Internet, Information Technology & Services + keywords "AI", "developer tools", "API", "platform", "SaaS"
- Funding: Seed, Series A, Series B (S1), last funding date within 12 months
- Job postings: job title contains "software engineer" OR "backend" OR "full stack" OR "ML engineer"; posted in the last 90 days
- Screenshot the result count at each step: TAM (no job/funding filters) → SAM (+ hiring) → SOM (+ S1 size/funding)

**Prospeo: company search**
- Same geography, headcount and industry; add technology filters where available (GitHub, AWS/GCP; Cursor/Copilot if listed)

**Sales Navigator: Account search**
- Headcount 51–200, HQ US, Industry Software Development / Technology, Information and Internet
- "Department headcount growth — Engineering" > 10% in 6 months
- Keyword boolean: ("AI" OR "LLM" OR "developer") NOT ("staffing" OR "consulting" OR "outsourcing")

**List hygiene (per D11–D16):** export from ≥3 providers → merge → dedupe on the cleaned domain → keep only **Company Name, Domain, Company LinkedIn URL** → spot-check 10 rows against the ICP → 50 accounts.
