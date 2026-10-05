# Saffron KT

## 000 · Newest: D37–D38 (5 Oct): micro-campaigns + HeyReach
Micro-campaigns beat mass AI personalization. HeyReach automates the LinkedIn sequences: max 25 connection requests and 40 messages a day, ~750 a month split into 4 test campaigns. Fix your profile and post thought leadership before outreach. LinkedIn gets ~30% replies vs 1–4% for email. Segment by context, not title. **Your homework:** the Saffron × CHRO HeyReach campaign, configured but not live. The guide is in Drive: "Homework - D37-D38 HeyReach CHRO Campaign".

## Course video: chapters

Drive: "Saffron - Course Summary Video" (37.8 min, Days 1–36)

- 0:00  Introduction
- 1:00  Foundations
- 5:05  Strategy before tools
- 12:19  The data layer
- 16:54  Clay, the workbench
- 22:19  Signals, AI and qualification
- 26:36  Getting data in and out
- 29:12  Sending email that lands
- 34:35  Efficiency and your career


## 00 · Latest classes: D29–D36 (29 Sep – 2 Oct)

See Session Notes → "D29-D36 summary notes" for detail. Key points: separate company/people tables and tier by size (D29–30); never send from the main domain, SPF/DKIM/DMARC, 3-week warm-up, simple placeholders, opt-out P.S. (D31–32); mailbox maths: 2,000 leads × 6 steps ≈ 12 mailboxes, and lead with LinkedIn under ~2,000 leads (D33–34); 6-email sequence with an options close, A/B tests, micro-campaigns, tracking off (D35–36). Homework: plan 10 Saffron campaigns (3 segments × 2 personas × signals). Ask Yogesh: tracking domain vs tracking off; the "avoid software companies" advice vs Saffron's ICP.


## 0 · What you missed on 28 Sep (D27–D28: Web scraping in Clay + HTTP API column)

## Things to know

1. HTTP API column: Clay's general connector to any external API without a native integration. Core vocabulary: endpoint, method (GET/POST/PUT/DELETE), headers, query parameters, JSON body, field path, authentication, test vs. production URL. Error codes: 400 bad request formatting, 401 not authenticated, 403 not permitted, 404 endpoint doesn't exist, 429 rate limited.
2. Web scraping ladder: cheapest to most expensive: Native Scraper, Chrome Extension, Claygent, Apify, Zenrows. Always try the cheapest tool that could work first. Claygent is expensive at scale (~$200/1,000 rows) vs. Apify (~$19/month) — use Claygent only when a page needs interpretation, not plain field extraction.
3. Clay table hygiene: a table must end in outreach-ready messaging, not just an email or LinkedIn URL. Use fewer columns, not one per detail. A clean table should take 2-3 hours to build, not days.
4. Signal filtering rule: at least 70% of sourced companies should survive qualification. One classmate dropped from 60 to 6 companies — a sign of too-strict signals or double-filtering across two tools.
5. Live table review: a classmate's 47-company table (SOC2-compliance signal, security/DevOps roles) got feedback to hide unused columns and add a People-table lookup (mapped on Company Name) pulling in company-level messaging — a reusable pattern.

## Homework given (check if it applies to you)

- Everyone: work through the shared 400+ tool directory, keep a one-line summary per tool tried.
- Two classmates: rebuild company lists to keep ≥70% after filtering, and generate a "Clay execution logic" doc via Claude/GPT.
- One classmate: expand target roles to "platform security" and build the company-to-people lookup.
- Nothing assigned to you specifically since you weren't there — ask Yogesh if the tool-directory task applies to you too.

## Questions worth asking Yogesh

1. HTTP API column for a free signal (GitHub or job-board data) — Enrichment or Source, given my table already has 50 rows?
2. Should I shift some Claygent-on-Helium AI-tool detection to a cheaper Native Scraper pass, given the cost gap raised in class?
3. Does my Outreach Eligibility formula pass the 70%-survival rule?



Knowledge transfer · 30 Sep 2026 · before the cohort class

Everything the cohort covered from D01 to D26, and the Saffron pipeline built on your accounts over the last two days, with the reasoning behind each decision. By the end you should be able to explain the pipeline in your own words and pick up tomorrow's class without gaps.

How to use this
Go top to bottom with Abi on a shared screen. The playbook explains concepts in more depth; the build log has every screenshot. Every section is complete as of 29 Sep 2026; the page uses pending markers only for work that was unfinished when it was drafted, and none remain.

1
## Agenda (about 2 hours)

| Time | Block | Outcome |
|---|---|---|
| 0:00–0:20 | GTM in 20 minutes (section 2) | You can explain funnel, ICP, TAM/SAM/SOM, signals and offer using Saffron's real numbers. |
| 0:20–0:30 | The course so far (section 3) | You know what each session covered and what comes next. |
| 0:30–1:15 | The build, live in Clay (section 4) | You can walk through every column and say why it exists and what it cost. |
| 1:15–1:30 | Credit efficiency and the LinkedIn post (section 5) | You can tell the bonus-point story with real numbers. |
| 1:30–1:45 | Field notes and your to-do list (sections 6–7) | You know the traps and what you own next. |
| 1:45–2:00 | Self-check (section 8) | You answer the 10 questions without looking. |

2
## GTM in 20 minutes

**Go-to-market (GTM)** is how a company finds customers and turns them into revenue. A **GTM engineer** builds the data pipeline behind that: which companies to target, why now, who to contact, and what to say. Think of it as an ETL job whose output is qualified sales conversations.

### Saffron, the company you're building for

Saffron (YC Spring 2026, San Francisco, 3 founders) sells an AI-native technical interview. A candidate builds a real feature in the hiring company's codebase using Claude Code; Saffron records every prompt and edit and 10+ AI reviewers score how they worked. Pricing is self-serve: $199/month for 5 assessments, $499/month for 15. Competitors: HackerRank, CodeSignal, Rounds.so, CoderPad, Karat.

### The funnel

Unknown → lead → MQL (marketing thinks they fit) → SQL (sales agrees they're worth a conversation) → opportunity (a deal with a value) → closed won or lost. The GTM engineer owns the start: turning unknown companies into qualified, contactable leads.

### ICP and personas

The **ICP** (ideal customer profile) describes the company that gets the most value: firmographics (size, industry, location, funding), technographics (tools they use) and situation (are they hiring?). A **persona** is the person you contact inside it.

- **Decision maker**: signs off. For Saffron: CTO, VP Engineering, Head of Talent Acquisition.
- **Champion**: feels the pain daily and pushes internally. For Saffron: engineering managers, technical recruiters.

Saffron's ICP as built: US tech companies of 50–500 people that hire engineers regularly and already use AI coding tools. The size cap comes from pricing: at $199–$499/month, one engineering leader can buy without procurement.

### TAM, SAM, SOM with Saffron's real numbers

Three nested market sizes. GTM engineers count them by applying filters in a data tool and reading the result count; the strategy doc needs the screenshots.

**~54,000**TAM: could ever buy
**~12,000**SAM: can actually serve
**2,921**SOM: can win this year
- **TAM** (Prospeo): HQ in US, Canada, UK, Germany, Netherlands, France · 51–5,000 employees · Software Development; Technology, Information and Internet; Financial Services; Hospitals and Health Care.
- **SAM**: TAM + Engineering & Technical headcount ≥ 20 (a real engineering team) + headcount growth ≥ 1% over 6 months (stand-in for hiring, since Job Posting is locked on the free plan). This also removed the hospitals and clinics that leaked in through the healthcare industry.
- **SOM**: SAM narrowed to US only, 51–500 employees, founded 2012 or later (stand-in for venture-stage, since Funding is locked). SOM is partly a filter and partly an argument: a 3-person team, self-serve pricing and one decision maker point to US startups of this size.

### Segments

You never write one campaign for the whole market. You split it into groups that share a pain and write one message per group. Saffron's: S1 AI-native startups of 50–200 (attack first), S2 growth SaaS and infrastructure of 200–1,000, S3 regulated FinTech and HealthTech.

### Signal, intent, trigger

- **Signal**: a public fact about the company. Saffron example: 12 open engineering roles, a new CTO.
- **Intent**: a person interacting with you. Saffron example: their Head of Talent visits the pricing page or likes the founder's post.
- **Trigger**: the action you take in response. Saffron example: a message to the CTO that references their hiring push.

Use signals as context, never recite them back ("we saw you raised money" reads as surveillance). Verify a signal is true before relying on it. Recent funding is easy to detect but, per Yogesh, a weak signal on its own.

### The offer: value → pain → proof

Value is the outcome in the buyer's words; pain is what they already feel; proof is why they should believe you. Apply the five-word test: a busy buyer should keep reading after the first five words.

"Your engineers ship with AI. Your interviews don't test it. Saffron has candidates build a real feature in your codebase with Claude Code, then scores how they used AI, with zero interviewer hours and results the same day."
3
## The course so far, on one screen

| Sessions | Topic | The one thing to remember |
|---|---|---|
| D01–D02 | What GTM engineering is; the revenue funnel | ~90% outbound today; data is ~80% of the work; never trust one provider. |
| D03–D04 | The seven layers; workspace setup | Order waterfalls cheapest-first; email infrastructure (SPF/DKIM/DMARC) is 80% of email success. |
| D05–D06 | Adopt a company; ICP | Strategy doc before tools. Separate title keywords from seniority; always add exclude keywords. |
| D07–D08 | TAM/SAM/SOM; signals and triggers | Count markets with filters and screenshot them. Signal (account) vs intent (person) vs trigger (your action). |
| D09–D10 | Offer and messaging; strategy brief | Interrogate the client first. LinkedIn beats cold email for differentiation. Never promise reply rates. |
| D11–D12 | Data landscape; Apollo | People-first vs company-first. Use 3+ sources; dedupe on LinkedIn URL → email → name + company. |
| D13–D14 | Sales Navigator; data quality | Valid / invalid / valid catch-all / catch-all only. Skip Mimecast/Proofpoint/Barracuda domains. ~60% of a list survives cleaning. |
| D15–D16 | 50-account list; Clay orientation | Accounts = companies. Auto-run off; hide columns, never delete. |
| D17–D18 | Import; first enrichment | Real clients give you only company names. Domain → enrich → persona → email → verify. |
| D19–D20 | Formulas; enriched list | Formulas are free. Account scoring is binary. Use day counts ("180 days") in AI prompts, never months. |
| D21–D22 | Waterfalls; run-only-if | Helium → Neon → Argon, escalate only on failure. Send only to valid and valid catch-all. |
| D23–D24 | Lookups; dedupe | Blacklist (permanent) vs exclusion list (temporary). "Similar to" beats "contains". A healthy qualifier passes 60–70%. |
| D25–D26 | Scored pipeline; Claygent | Lantern example: qualify on hiring pain + has a recruiting team. Regenerate the JSON schema after editing a prompt. |
| Guests | Rejoice; Kushagra | Revenue engineers beat tool operators. Proof of work beats courses. Coding agents are rising; don't dump thousands of rows into an agent's context. |

**Portfolio Yogesh expects** (D21–D22): strategy doc + Clay table + data pushed to a sequencer (HeyReach/Instantly) + a Claude Code integration + a Make or n8n automation + 5 Loom walkthroughs.

**What comes next in the course** (per the Learning Guide): signals at scale (L3), orchestration with n8n/Make and webhooks (L4), execution through Instantly and HeyReach including sending domains and warm-up (L5), CRM and reporting in HubSpot/Attio (L6), and AI agents with Claude Code (L7). The people table and email verification you'll finish this week feed directly into the execution layer.

4
## The build, step by step

### Tools and identity

Work happens in a separate Chrome profile signed in as `deepshikhagtme@gmail.com`, with Prospeo and Clay accounts on it. LinkedIn and Loom stay on your personal account: LinkedIn allows one account per person. Apollo rejected the gmail ("You cannot sign up with this email address"), so the list was built from two sources instead of three. Apollo can be added later with a custom-domain mailbox.

### Market sizing

TAM ~54,000 → SAM ~12,000 → SOM 2,921, all in Prospeo, as in section 2. Screenshots are in the Drive folder "Build Evidence" and in the build log.

### The 50-account list (two sources, 63 rows in, 50 out)

- **Prospeo**: page 1 of the SOM results, 23 exported, 18 kept. All were 250–490 employees because Prospeo sorts by relevance. The export has ~95 columns including active job count and job titles, which later served as a free cross-check.
- **Clay Find companies**: US, 51–200 employees, software industries, privately held, at least 20 current engineers and at least 5 open engineering roles (7 titles, "similar to"). 196 matches, 40 exported, 32 kept. Without the two hiring filters Clay returned ~31,000 companies led by media brands, job boards and a competitor.
- **Merge**: a script cleaned domains, deduplicated, dropped non-US HQs (2) and the exclusion list (11), leaving exactly 50 companies with Company Name, Domain and Company LinkedIn URL.

| Excluded | Reason |
|---|---|
| HackerRank, CodeSignal, Rounds.so, CoderPad, Karat, HackerEarth | Competitors (technical assessment) |
| micro1, Coffeee.io | Competitor-adjacent (AI interviews / pre-assessed talent) |
| Workable, Sense, Joveo | Partners, not buyers (hiring and recruiting software) |
| Fusemachines, thinkbridge, GoML, Tech9, Particle41, Velozient | Services, outsourcing or staffing: they sell engineering capacity rather than hire for their own product |
| Novolo AI | Hardware incubator and investor |
| Wing | Alphabet subsidiary; purchase would go through parent procurement |
| Zetheta, Prolific | HQ outside the US (India, UK); Clay's location filter matches any US office |

### The Clay table "Saffron | Qualified Pipeline", column by column

Table-level auto-run is set to **Manual**. Every paid column was tested on 10 rows before running the rest.

#### 1 · Clean Domain (formula, free)

Clay formulas are JavaScript. Described in English, Clay generated: `{{Domain}}?.toLowerCase()?.replace(/^https?:\/\//,"")?.replace(/^www\./,"")?.split("/")?.[0]`

#### 2 · Enrich company (0.5 credits/row, 25 credits for 50 rows)

Input: Clean Domain. Outputs shown: Employee Count, Industry, Country, Founded, Type. One lookup per row; the output toggles only choose which fields become columns and don't change the price.

Finding: Clay's search put all Clay-sourced companies in the "51–200" band, yet the enrichment counted Hugging Face at 1,140, Yuno 1,424, Cognition 604. The search uses the size band a company picked on LinkedIn; the enrichment counts actual profiles. Clay writes the country as `US`.

#### 3 · Find active job openings (by Clay, 0.5 credits per row with results)

Chosen over waterfalls and other providers priced at 2–8 credits/row for the same signal. Settings: Job Title Keywords = Software Engineer, Software Developer, Back End Engineer, Front End Developer, Full Stack Developer, Machine Learning Engineer, Artificial Intelligence Engineer. Exclude = Sales, Solutions, Recruiter, Support. Limit = 10 (the allowed range is 1–10; a limit of 50 made every row error, at no cost). Outputs: Job Count and the first Normalized Title.

Job Count reports the company's total, not the returned records: LawnStarter returned 10 jobs with a count of 23. Result: 24 companies with 5+ engineering openings, 16 with 1–4, 10 with none.

Free cross-check: Prospeo's export listed Sprinto with 23 active jobs, but only one was a software role. So a company's total job count is not an engineering job count, and Clay's zeros were real. That made a paid AI fallback unnecessary.

#### 4 · Find contacts at company → People Count (0.5 credits per row with results)

Match companies using LinkedIn URL with the Company LinkedIn URL column. Job Function = Human Resources and Recruiting. Output: People Count. Run condition `{{Jobcount}} >= 1`, so the 10 companies with no openings are skipped for free. Why it matters: a company with no recruiting team hires through agencies, and agencies don't buy assessment tools (D25–D26).

38 of the 40 companies with openings have a recruiting team (19 credits: 0.5 × 38 hits; skipped and "No Profile Found" rows were free). Two came back 0: Avoma (66 employees, believable) and Pinecone (137 employees, 9 openings, almost certainly a data gap).

#### 5 · AI coding tools mentioned (Use AI → Web research, Helium)

Only runs on the 16 companies with 1–4 openings. Rows with 5+ already qualify and rows with 0 fail anyway, so running it on all 50 would spend about two-thirds of the credits on answers that can't change a decision. The prompt asks whether job descriptions or the engineering blog mention Cursor, Claude Code, Copilot, Windsurf or Codex, returns JSON with evidence, and says "no" without explicit evidence. Helium on 10 rows first; only the wrong rows are re-run on Neon.

Run condition `{{Jobcount}} >= 1 && {{Jobcount}} < 5`. Helium: 19 credits (16 rows at 1 credit + 3 re-run). Neon was skipped on purpose: Helium's one failure was formatting (Artisan's answer landed as a sentence in the yes/no field), and setting the field type to True/False plus describing the tools field fixed it on the same cheap model. Clay's default was Argon (3 credits, "recommended"), which on all 50 rows would have cost about 150–190.

Found: 10 of 16 mention AI coding tools (ITILITE, Artisan, ButterflyMX, H2O.ai, Cognition, Polymarket, HeyGen, Kalshi, Avoma, Rillet). Cursor and Claude Code come up most. 6 don't (Branch, Observe.AI, Opkey, Bik.ai, Gridware, SuperAnnotate).

#### 6 · Outreach Eligibility and Qualification Reason (formulas, free)

Don't outreach if People Count = 0, employees < 50 or > 1,000, country is not US, or Jobcount = 0. Otherwise Outreach if Jobcount ≥ 5 or AI tools = yes. The Reason column lists the facts that drove the result, because vague qualification is the most common learner mistake (D19–D20). Target pass rate 60–70% (D23–D24).

**Outreach: 30 of 50 · Don't outreach: 20 · Pass rate: 60%**, the bottom of the instructor's healthy 60–70% range. Failures: 10 with no engineering openings (7 from the Prospeo half), 2 over 1,000 employees (Hugging Face, Yuno), 6 with 1–4 openings and no AI-tool mention, 2 with no recruiting team found (Pinecone, Avoma).

The formula preview caught two type bugs before saving: the AI field stores the text "true", so `== true` never matched; and a stored 0 recruiting team slipped past `!{{Peoplecount}}`. The fix was `Number(x || 0)` for counts and `String(x).toLowerCase() === "true"` for the AI field. Clay auto-named the reason column "Staffing Summary".

**Your call:** check Pinecone and Avoma on LinkedIn and override if they do have recruiters.

#### 7 · People, emails, verification

**Find people** with Surfe's "Find people at company" (0.1 credits per person found) on the 30 Outreach companies only, up to 3 each. The first 10-row test returned AuditBoard's co-founder, CEO and a TA coordinator: wrong buyers. Removing "Co-Founder" and adding Seniorities (C-Level, Director, Head, Manager, VP) returned the VP and SVP of Engineering. Openmart (1/result) or Pubrio (3/row) would have cost about 90 credits.

**One row per person:** "Write each item to new row in other table" → "Send table data" into a new table, Saffron People, carrying 7 company columns. Free. New tables default to Auto-run on, so switch to Manual first. The free plan only makes **50 of the 79 rows** usable (the Learning Guide says 200).

**Persona formula** (Clay named it "Job Seniority"): blank for sales/account/GTM/field/solutions/customer/marketing titles; Decision maker for CTO, VP/SVP/EVP, chief technology/product, head of engineering or talent; Champion for other engineering, talent, recruiting, director or head titles. The preview caught "Svp" and "Accounting" slipping past whole-word matches. 5 of 50 came out blank (Sales Engineering, a sales engineer, Technical Account Management, GTM Engineering, Field CTO) and cost nothing further.

**Work email waterfall** across 11 providers (Findymail first), each with its own validation step, only for Decision makers and Champions. Two traps: the run condition was typed as `{{Persona}}` but the column was named "Job Seniority", so the preview said "Will not run" everywhere (fix: insert columns with `/`); and in Manual mode you run the **final** "Work Email" column to run the whole chain.

**People found: 79 at 27 of 30 companies (50 usable on the free plan) · Verified emails: 40 of 45 eligible (89%) · Credits: 9.1 people + 26.5 emails.** Findymail found 39, Hunter 1. No provider found Guanning Zhao, Douglas Sloan, Weisi Duan or Nebojša Miletić; Steven Yue's address failed validation and was excluded.

#### 8 · Client delivery sheet

Built from the two Clay exports with `data/build_delivery_sheet.py`, saved to Drive as "Saffron - Client Delivery Sheet". Four tabs: **Summary** (segment, counts, credits, rules), **Contacts** (40 verified contacts with persona, LinkedIn, email, which provider found it, and the account's reason), **Accounts** (all 50 with signals and eligibility) and **Follow-ups** (25 items: 5 LinkedIn-only contacts, 5 wrong-fit titles, 10 next-batch companies, 3 companies with no people found, Pinecone and Avoma to review).

Deviations from the course default: the waterfall's built-in validation replaced a separate Enrichly column, and the Mimecast/Proofpoint/Barracuda MX check has **not** been done yet. Do it before any sending.

5
## Credit efficiency (the bonus point)

Yogesh's bonus point was about spending Clay credits well by choosing the right model for the job. The build showed that model choice is one of three levers, and that the other two matter at least as much.

### The three levers

1. **Cheapest adequate model or provider.** The same signal (job openings) ranged from 0.5 to 8 credits/row across providers. Helium first for AI, Neon only for rows Helium got wrong.
2. **Run conditions.** Expensive columns only fire on rows where the answer can change the decision. The recruiting-team column skips companies with no openings; the AI column runs on 16 rows instead of 50.
3. **Test on 10 rows.** It catches bad settings (the limit error) and shows the real price before you commit.

### Real numbers

- Starting balance: 1,005 credits.
- Enrich company: 5 credits for the 10-row test, 25 for all 50 (0.5/row as quoted).
- "Run 40 empty or out-of-date rows" cost 20; "Force run all 50" would have re-charged the tested rows (25).
- Job openings: 10 rows cost 2.5 credits because only the 5 rows with results were charged. Misses were free. Invalid-input errors were free.
- Run-condition-skipped rows were free: balance 957.5 after the first 10 recruiting-team rows.
- A free cross-check against the Prospeo export avoided a paid AI fallback on the 10 zero-opening companies.
- AI coding-tools column: 19 credits on Helium for the 16 rows that could change a decision, versus about 150–190 for Clay's default Argon on all 50. Neon wasn't needed; fixing the output types solved Helium's formatting miss.
- **Whole accounts table: 83 credits** (1,005 → 922): Enrich company 25, job openings 20, recruiting team 19, AI column 19, formulas 0.
- People search: 9.1 credits on Surfe (0.1 per person found) against about 90 on the alternatives.
- Moving people into their own table and pulling their fields into columns: free.
- Email waterfall: 26.5 credits for 40 verified emails. The cheapest provider, first in line, found 39 of them; misses were free.
- **Whole pipeline: 118.6 credits** (1,005 → 886.4) from 50 companies to 30 qualified accounts and 40 verified contacts.

Correction to the course material
The course says Clay "charges per attempt, not per success". That isn't true for every enrichment: here, rows with no result and rows with errors cost nothing. Billing depends on the enrichment and provider, so the reliable habit is to run 10 rows and check the balance.

### The LinkedIn post (draft, for the bonus point)

Built from these numbers. Edit it into your own voice and post it from your account.

This week I built a full account-qualification pipeline in Clay, and the lesson I didn't expect was how much the cost depends on choices you make before anything runs.

The project: find the right companies and buyers for Saffron (YC S26), an AI-native technical interview platform. I started with 50 target companies and ended with 30 qualified accounts and 40 verified work emails for their engineering and talent leaders. Total cost: 118.6 Clay credits.

Four decisions kept it that low:

→ Cheapest model that can do the job. Clay pre-selected its most expensive research model (3 credits a row). The cheapest one (1 credit) answered my question just as well once I tightened the output format. When it returned messy answers, fixing the output fields worked; a pricier model wasn't needed.

→ Only run expensive columns where the answer can change the decision. My AI research ran on 16 of 50 companies, not all 50. It cost 19 credits instead of an estimated 150+.

→ Compare providers. The same "find people" step cost 0.1 per person on one provider and 1 to 3 on others. People search came to 9 credits.

→ Test on 10 rows first. Twice, the preview caught a bug before it cost anything: a true/false field stored as text, and a filter pointing at a column that didn't exist.

Also worth knowing: not every Clay enrichment charges per attempt. Some only charge when they find something.

#GTMEngineering #Clay #RevOps #Outbound

6
## Field notes

### Accounts

- Data vendors (Apollo, Ocean.io) reject free email domains. A custom-domain mailbox fixes it.
- LinkedIn, Sales Navigator and Loom stay on your real identity. The dedicated gmail is only for tools with credits and trials.

### Prospeo

- Free plan locks Funding, Job Posting, Technologies and Revenue. Stand-ins: Engineering headcount, headcount growth, founded year.
- Results sort by relevance, which favours bigger companies.
- The export is rich (~95 columns) and is free signal data for cross-checks. Export is the button at the far right of the results header.
- Industry filters leak: "Hospitals and Health Care" includes clinics.
- A company's total job count is not its engineering job count. Read the titles.

### Clay: finding companies

- Raw company data is noisy; the free "people are…" and "job openings are…" filters are where the value is.
- Job title appears in two filters: employee titles (is there a team?) and job-opening titles (are they hiring now?).
- Use generic titles with "similar to". Stack-specific titles (SAP, Salesforce, SharePoint) pull in IT-services companies.
- "Location is United States" means any US office, not HQ.
- Continue → "Save to new workbook and table" (not "Save to Companies"). Close the "Enrich companies" wizard with × to avoid spending credits on a source table. Export is under Tools → Export → Download CSV.
- Search filters and enrichments disagree: 11 of 32 companies that passed "5+ openings" in search had fewer than 5 in the enrichment, and size bands differed from counted employees. A search filter narrows a list; it doesn't prove a signal.

### Clay: building the table

- Two auto-run switches: the table-level Manual/Auto-run button, and each column's own Auto-run toggle, which is on by default.
- Formulas are JavaScript and free.
- "Run empty or out-of-date rows" avoids re-charging rows already done.
- Check each enrichment's allowed input ranges (job openings Limit is 1–10).
- Match the "match using" type to the column you select (LinkedIn URL with a LinkedIn column).
- Clay writes country as `US`; formulas must test for that.

### Clay: people and email

- The free plan caps a table at 50 usable rows.
- New tables default to Auto-run on; "Send table data" and "Add to column" are free.
- Clay auto-names formula columns, so typed `{{Name}}` references can point at nothing. Insert columns with `/` and check "Referenced columns".
- In Manual mode, run the final waterfall column; it runs every provider and validation step in order.
- The cheapest provider found 39 of 40 emails; validation kept one unverifiable address out.
- Tune people search with seniorities, not only titles, then filter sales-flavoured titles with a formula before paying for emails.

### Judgment

- Screen every export by hand and record each exclusion with its reason. Filters let through competitors, services firms, subsidiaries and partners.
- HQ location isn't where the team or buyer sits; several US-registered companies have engineering in India.

7
## Your to-do list after the KT

1. **Strategy Doc v2**: open it in the Drive folder, paste the TAM/SAM/SOM screenshots from "Build Evidence" into the three blanks, read it once against the "competent stranger" test, then share with Yogesh as editor.
2. **LinkedIn post**: edit the draft into your own voice and post it from your account. Check the WhatsApp group for whether Yogesh or Stable GTM should be tagged.
**5 Looms** (portfolio requirement), 3–5 minutes each:
  - **Strategy doc**: who Saffron sells to and why; decision maker vs champion; TAM ~54K → SAM ~12K → SOM 2,921 and the filters; why 50–500 employees; segments; the S1 offer.
  - **List build**: why companies first; Prospeo vs Clay search; the hiring filters that cut ~31,000 to 196; screening and every exclusion reason; merge to 50.
  - **Enrichment and signals**: Clean Domain formula; Enrich company and the size-band finding; job openings settings and the total-vs-engineering finding; recruiting team and why it disqualifies.
  - **Qualification and delivery**: the eligibility rules; the Reason column; pass rate vs the 60–70% benchmark; people, emails and verification; the delivery sheet.
  - **Credit efficiency**: the three levers with real numbers; 0.5 vs 8 credits for the same signal; gating the AI column to 16 rows; the "charged per attempt" correction.
4. **Before any sending**: run the MX check and drop contacts whose company mail goes through Mimecast, Proofpoint or Barracuda (the delivery sheet has not had this check).
**Follow-ups tab of the delivery sheet**:
  - Reach 5 people on LinkedIn instead of email: Guanning Zhao (DataVisor), Douglas Sloan (AuditBoard), Weisi Duan (Kalshi), Nebojša Miletić (Gigs), and Steven Yue (SandboxAQ; his address failed validation).
  - Next batch of 10 Outreach companies whose people sit beyond the free plan's 50-row limit: MoonPay, Artisan, H2O.ai, Ema, Lightning AI, Phantom, Suno, Nooks, RevenueCat, Rillet. Needs a paid plan or a second people table.
  - Find people manually at Cognition, Polymarket and RoboMQ (the people search returned nobody matching).
  - Review Pinecone (disqualified only because no recruiter was found) and Avoma (AI tools but 66 employees, no TA team) and override if LinkedIn says otherwise.
6. **Agency connections**: send connection requests (no message) to the agencies on the list from the cohort WhatsApp group (D01–D02).
7. **Apollo**, when you have time: buy a cheap domain, set up a Zoho mailbox with MX, SPF, DKIM and DMARC, sign up to Apollo, and add it as the third list source.
**Questions for Yogesh**:
  - D07–D08 described 1–10 account scoring, D19–D20 said binary. Is binary the rule?
  - Is Clay's own company search acceptable as a list source (D15–D16 said no, D25–D26 used it)?
  - The Learning Guide says 100 accounts; class said 50. Confirm 50.
  - Is applying the Lantern qualification pattern to Saffron acceptable instead of building the Lantern table?

8
## Self-check

Answer out loud first, then open the answer.

**Q:** 1. What are TAM, SAM and SOM for Saffron, with numbers?

TAM ~54,000: companies of 51–5,000 in six countries and four industries that could ever buy. SAM ~12,000: those with 20+ engineers and a growing headcount. SOM 2,921: US-only, 51–500, founded 2012 or later, which a 3-person team with self-serve pricing can realistically win.

**Q:** 2. Who is Saffron's decision maker, who is the champion, and why do you need both?

Decision maker: CTO, VP Engineering or Head of TA, who signs. Champion: engineering managers and technical recruiters, who feel the interview load daily and push internally. A fit company with nobody to push or sign goes nowhere.

**Q:** 3. Give a Saffron example of a signal, an intent and a trigger.

Signal: 12 open engineering roles. Intent: their Head of Talent visits Saffron's pricing page. Trigger: a message to the CTO referencing the hiring push.

**Q:** 4. Why does the account list start with only three columns?

Real clients usually hand over a bare list of company names. Starting minimal practices deriving everything else yourself in Clay.

**Q:** 5. Why not trust one data source, and how do you dedupe?

Every source has gaps and stale data (coverage vs accuracy); combining sources raises coverage. Dedupe on LinkedIn URL, then email, then full name plus company, never name alone.

**Q:** 6. Valid catch-all vs catch-all only: which do you send to?

Only valid and valid catch-all. Catch-all-only addresses are accepted by the server but may never reach a person, and bounces above ~2% damage the sending domain.

**Q:** 7. Why exclude companies with no recruiting team?

They hire through agencies, and agencies partner with tools rather than buy them. The company isn't the buyer.

**Q:** 8. What are Clay's two auto-run switches, and why keep both off?

The table-level Manual/Auto-run button and each column's own Auto-run toggle (on by default). With either on, edits or new columns can run on every row and spend credits you didn't plan to.

**Q:** 9. How did the build keep AI spend proportional to lead quality?

The AI column only runs on the 16 companies with 1–4 openings, where its answer can change the decision; Helium runs first and Neon only re-runs the rows Helium got wrong; everything is tested on 10 rows.

**Q:** 10. If only 25% of the list qualifies, what does that tell you?

The rules are too strict or the signals too narrow. The benchmark is 60–70%, so loosen or add a qualifying signal rather than accept the loss.

9
## Where everything lives

- **Playbook** (concepts + build guide): claude.ai/artifact/CM7zG8Jomdshb8pfFosbZW (https://claude.ai/artifact/CM7zG8Jomdshb8pfFosbZW)
- **Build log** (every step with screenshots and field notes): claude.ai/artifact/BoFqdK241doAAZc5NHpRDN (https://claude.ai/artifact/BoFqdK241doAAZc5NHpRDN)
- **Drive folder "GTM Cohort Catch-up"** (Strategy Doc v2, Saffron - Client Delivery Sheet, KT Pack, LinkedIn Post draft, master notes, 19 session notes, build sheet, credit log, 50-account sheet, Build Evidence): drive.google.com/drive/folders/1tq9Z9VRXfo366aSE9X9VroCUzCvNiWjw (https://drive.google.com/drive/folders/1tq9Z9VRXfo366aSE9X9VroCUzCvNiWjw)
- **Clay**: workbook "Saffron | Qualified Pipeline" in the Saffron folder (deepshikhagtme account); source table "Software Companies, US, 51-200 Employees" in the same folder.

Prepared from the cohort's session notes (D01–D26, two guest sessions, two recorded trainings), the Learning Guide and the Saffron build log.
