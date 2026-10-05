# D13-D14: LinkedIn Sales Navigator + Data Quality Fundamentals (2026-09-16)

## TL;DR
- Sales Navigator is structurally like Apollo/Prospeo but has no API, no mass export beyond ~1,000-2,000 leads, and needs a mandatory cleaning pass in Clay before use — its one unique strength is detecting non-.com company domains (.uk, .fitness, etc.).
- Data quality in GTM engineering rests on two pillars: verified LinkedIn URL (real profile with followers/connections) and verified email (valid / catch-all / valid catch-all / invalid) — never trust one verification tool alone.
- Never email domains protected by Mimecast or similar spam gateways — they will silently block delivery regardless of email validity; align sender accounts ~80% Google / 20% Outlook to match target MX domains.
- Expect only ~60% of any exported list to end up usable after removing missing emails, invalid emails, Mimecast-protected domains, and mismatched name/company data.
- Store all cleaned/enriched data centrally in Supabase (queryable via API from Claude) so you never re-enrich the same records month after month.

## Key concepts
**The evolving scope of GTM engineering**: Yogesh frames the role as expanding beyond list-building into full-cycle ownership — if outbound fails, the GTM engineer is expected to try LinkedIn, then events, then Google paid ads, product-messaging revamps, or competitive repositioning. His long-term prediction: within 2-3 years, a single technical GTM engineer will replace what used to be separate sales + marketing teams for a company. Using a pre-built AI sales agent (e.g., Goji Berry, discussed with Sampath) is not GTM engineering itself — it's one tactic; a GTM engineer must think beyond any single tool/product and be ready with a plan B (competitor analysis, alternative channels, messaging pivots) if the primary approach underperforms.

**Sales Navigator's real niche**: It behaves like Apollo/Prospeo for filtering, but (a) mass export tops out around 1,000-2,000 leads without paid third-party export tools, (b) there is no API — everything is manual, (c) exported data quality is comparatively poor and needs a cleanup pass. Its standout strength: detecting companies with non-standard domains (e.g., netapp.uk, bold.fit) that other tools may miss. Outside of people-first searches, there's "no big use" for Sales Navigator relative to Apollo/Prospeo.

**API-as-data-provider model**: Tools like Blitz API and FullEnrich let you skip manual tool UIs entirely — you prompt Claude (via the API) directly, e.g., "find the top 10 CTOs of YC26 AI-native companies in the US," and get structured results back, letting you compare data quality across providers without ever opening a dashboard.

**Combine & dedupe (recap + deepened)**: Reconfirmed from D11-D12 — Claude runs a "skill" that dedupes across CSVs (Apollo, Prospeo, Sales Navigator, Blitz API, FullEnrich, etc.) using LinkedIn URL → email → full name + company name, in that priority order (full name alone is unreliable — common names collide). Claude's output is split into two clean tabs: a **Company tab** (company name, domain, LinkedIn URL, employee count) and a **People tab** (first/last/full name, job title, seniority, LinkedIn URL, city/state/country, company name, company domain, email). This structure is what makes the subsequent Clay enrichment fast — doing the same split/dedupe work natively inside Clay would take much longer ("might take 1 hour... very easy to do in Claude").

**Data quality — the two core parameters**: (1) **LinkedIn URL validity** — a real profile has followers/connections; check this in Clay. Sales Navigator exports specifically lack a clean LinkedIn profile URL field, so it must be separately enriched/fetched in Clay. (2) **Email validity**, which splits into four categories:
- **Valid** — will deliver and reach an active inbox.
- **Invalid** — will bounce.
- **Catch-all** — the mail server accepts (catches) anything sent to that domain/address even if the mailbox is dead or the person left the company; it "lands" but nobody will ever read/respond. Never send to plain catch-all.
- **Valid catch-all** — a catch-all domain where the specific address structure is confirmed to redirect to an active, real mailbox (e.g., an email-alias/forwarding setup still reaching the right person). Safe to send to.
Multiple verification tools can disagree (a tool may flag "catch-all" while another confirms "deliverable") — this is why the class rule is to run at least 2-3 verification tools and combine their signals into a single outreach/no-outreach decision (built as a formula in Clay).

**MX domain / cybersecurity gateway filtering**: The MX domain reveals which email workspace a company uses (Google Workspace, Outlook/Microsoft 365) and whether they sit behind a security gateway like **Mimecast** ("Mcast" in the transcript — likely referring to Mimecast) which blocks inbound spam-like cold email entirely, regardless of validity. Rule: never send to Mimecast-protected (or similar mail-spam-protection) domains — the send is guaranteed wasted. This is common in Europe. Because most recipients use Google or Outlook, align sending infrastructure roughly 80% Google-based / 20% Outlook-based domains to match typical target MX distribution.

**The 60% usable-data rule**: From a raw exported list of ~1,000 records, expect roughly: some with missing emails entirely, some invalid emails, some blocked by Mimecast/similar gateways, some with mismatched name/company data — leaving only about 600 (60%) genuinely usable for outreach. Budget for this shrinkage when promising list sizes to clients.

**Supabase as the data warehouse layer**: Agencies store all cleaned/enriched records centrally in Supabase rather than re-enriching the same people every campaign cycle — this saves recurring enrichment cost/time. Claude can be connected to Supabase via API to query historical records on demand.

## Tools shown & how they were used
- **LinkedIn Sales Navigator** (00:08:24-00:11:22): Walked through the dashboard (company, past company, current company fields) noting export limits (~1,000-2,000 leads without paid export tooling), no native API, and strong detection of non-.com domains like .uk/.fitness TLDs. Instructor sent a separate 1-hour full walkthrough video after class.
- **Blitz API and FullEnrich** (00:11:22-00:14:03): Demonstrated running a Claude Code prompt — "find the top 10 CTOs of YC26 AI-native companies in the US using Blitz API and FullEnrich" — to fetch structured people data directly via API, comparing output quality between the two providers, bypassing manual tool downloads.
- **Claude — combine & dedupe skill** (00:14:03-00:18:13): Re-walked the dedupe skill (LinkedIn URL → email → full name+company) applied across Apollo/Prospeo/Sales Navigator/Blitz/FullEnrich CSVs, producing separated Company and People tabs, then shown how that clean sheet flows into Clay for the enrichment stage.
- **Website ICP-reading exercise ("Guest")** (00:19:38-00:33:00): Had the class read a vacation-rental property-management software company's website cold and derive its ICP without prompts. Correct answer: property management companies (segmented small hosts, 1-3 listings, sold via paid ads/marketing at $9/seat; vs. property managers with 4-200+ listings, sold via outbound). Used this to teach that a "small" self-serve-priced segment doesn't merit 1:1 outbound — paid channels are more efficient there.
- **Apollo / Prospeo — company-level (account) export for the homework list** (00:53:10-00:56:54): Demonstrated exporting a company-first list (not a people list): go to the Companies tab, filter to the right firmographic profile for the selected client company, select ~25 rows at a time (Prospeo gives 100 free credits, Apollo 75), export in batches, then consolidate two export batches (25+25) into one Google Sheet with company name, company domain, and company LinkedIn URL as the three required columns.
- **Enrichly** (00:38:43-00:41:39): Shown validating emails into categories — verified/deliverable/catch-all/safe — used as the primary classification tool for valid vs. catch-all vs. valid-catch-all.
- **BounceBan** (00:42:51): Shown giving a simpler binary deliverable/undeliverable signal, used as a cross-check against Enrichly (an email Enrichly calls "catch-all" may still show "deliverable" in BounceBan).
- **Million Verifier** (00:43:54): A third verification tool with similar verify/block/clean functions to Enrichly and BounceBan — the class rule is to combine outputs from at least two-three of these tools rather than trust one.
- **Supabase**: Referenced (not live-demoed) as the centralized data store for all cleaned/enriched records, queried via API from Claude to avoid re-enrichment costs.

## Instructor rules, opinions & decisions
- Never assume outbound (email/LinkedIn) is the only lever — be ready to pivot to events, paid ads, product/messaging changes, or competitive repositioning if outbound underperforms.
- Sales Navigator data always needs a cleaning pass in Clay (fetch missing LinkedIn URLs, verify profile authenticity) before use; Apollo/Prospeo data can be used immediately.
- Never send email to plain catch-all addresses; valid catch-all is fine.
- Never send email to domains behind Mimecast or similar spam-protection gateways — it's a guaranteed wasted send.
- Always use at least 2-3 independent email-verification tools and combine signals rather than trusting one tool's classification.
- Budget for ~40% attrition on any raw exported list before it's outreach-ready (60% rule).
- Store all cleaned/enriched data in Supabase for reuse — never re-enrich the same contacts repeatedly.
- When evaluating a company's GTM approach (as in the Guest roleplay), always ask about product roadmap, competition, and target-market positioning — the class was critiqued for skipping these in the roleplay.
- A company-first ("account") list export needs only company name, company domain, and company LinkedIn URL — people search happens later, inside Clay, not at the account-list stage.
- It doesn't matter which tool (Apollo, Prospeo, etc.) you use to pull a company-level account list — "every platform has good company data" for this purpose.

## Assignments / homework given
- All participants: build a target account list of **50 companies** for their previously selected client company (e.g., Sampath's Goji Berry), containing company name, company domain, and company LinkedIn URL, exported in batches (e.g., 25+25) from Apollo/Prospeo/similar, consolidated into one Google Sheet — needed for the next session's live Clay work.
- Yogesh Jaiswal: send the 1-hour Sales Navigator walkthrough video, and send supporting documents explaining catch-all vs. valid catch-all concepts.
- Sampath Vemulapati: finish preparing his account list (was mid-export at end of session).

## Deepu's questions & the answers she got
Deepshikha does not appear to speak in this session's transcript (she is listed only as an invitee). No questions/answers from her are recorded here.

## What this means for the Saffron build
- Do not rely on Sales Navigator as a primary data source for Saffron's engineering-hiring-manager lists beyond people-first searches; pair it with Apollo/Prospeo and always run a Clay cleanup pass to recover LinkedIn URLs and verify profile authenticity before using Sales Navigator exports.
- Build Saffron's email-verification step as a multi-tool formula (e.g., Enrichly + BounceBan + Million Verifier) rather than trusting a single verifier, and explicitly exclude/flag catch-all (non-valid) addresses and any domains sitting behind Mimecast-class gateways — likely relevant since enterprise engineering orgs (Saffron's buyers) often run hardened email security.
- Plan Saffron outreach volume assuming only ~60% of any raw hiring-manager list will end up usable after verification/domain filtering — don't promise a client (or your own pipeline dashboard) the full raw export count.
- Set up a Supabase store (or equivalent) early for Saffron's enriched contact data so repeated enrichment runs (e.g., quarterly refreshes of "companies currently hiring engineers") don't re-spend credits on the same people.
- When defining Saffron's ICP, apply the same segmentation logic used in the Guest exercise: distinguish self-serve/low-ACV segments (e.g., small startups doing ad-hoc technical hiring — better served by content/paid channels) from enterprise-segment accounts (dedicated outbound with a defined buying committee — e.g., Head of Engineering + Talent/Recruiting lead + possibly a security/compliance stakeholder).

## Resources mentioned
LinkedIn Sales Navigator, Apollo, Prospeo, Clay, Claude, Blitz API, FullEnrich, Enrichly, BounceBan, Million Verifier, ZeroBounce (mentioned as too expensive, not used), Supabase, Mimecast ("Mcast," unclear exact spelling in transcript), Google Workspace, Outlook/Microsoft 365, Goji Berry (Sampath's selected AI sales-agent company), Guest (vacation-rental property management software — ICP exercise subject), Yogesh Jaiswal (instructor), Sampath Vemulapati, Neeraj Sujan, Gagan Bhaisa, Rithika Murthy, Shubham Gosavi.
