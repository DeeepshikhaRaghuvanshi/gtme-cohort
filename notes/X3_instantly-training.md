# Instantly Cold-Email Training (undated recording)

Session runs alongside a live Sales-Navigator-export discussion (tools heard as "Visa"/"EVAboard," unclear in transcript) before pivoting to a full Instantly walkthrough with two students, Deblina and Mahir.

## TL;DR

- **Infrastructure setup is a 4-step sequence**: (1) connect email accounts, (2) enable a custom tracking domain, (3) start warmup, (4) set SPF/DKIM/DMARC at DNS. Done properly, this takes at least 2–3 hours and is treated as the highest-leverage "boring" skill a GTM engineer can have.
- **Warmup never stops.** It runs in three escalating weekly stages (roughly +1/day up to 10, then +2/day up to 20, then +3/day up to 30, tapering to a permanent low frequency) and continues even once a domain is actively sending campaigns — stopping warmup once "ready" is a common, costly mistake.
- **Email health score** (per-inbox metric) governs whether an inbox is safe to send from. Below 80%, pull that inbox from campaigns and put it back into pure warmup until it returns to 100%.
- **Campaign planning is a formula**: working days × email IDs × daily send limit per inbox (capped at 50/day after ramp-up) ÷ emails-per-lead = leads coverable per month. Outreach volume also ramps gradually (20/day → 30 → 40 → 50 cap) — never blast full volume from day one.
- **Hygiene**: keep to ~3 mailboxes per sending domain (instructor runs 5, flags it as not ideal); agencies commonly provision ~10 domains × 5 mailboxes per client, illustrating how quickly volume scales and why infra discipline matters.
- Deliverability depends on **SPF**, **DKIM**, and **DMARC** — every serious email-outreach interview tests these three terms.
- Bulk-connect many mailboxes via Instantly's CSV import template rather than adding accounts one by one.

## Key concepts

- **Warmup**: gradually ramping an inbox's send/receive volume with simulated natural engagement so Gmail/Outlook trust the sender; sudden bot-like sending gets flagged to spam.
- **Email health score**: Instantly's per-inbox trust indicator; dips on spam placements — any inbox under 80% should be pulled from active campaigns.
- **Campaign slow ramp**: gradually increases daily campaign volume per inbox — the real-outreach equivalent of warmup ramping.
- **Custom tracking domain**: a client-owned subdomain (vs. Instantly's shared default) for tracking opens/clicks — protects sender reputation and gives cleaner data. Analogy: one mall guard for every store vs. a dedicated guard for just your store.
- **Warmup filter tag**: a per-inbox label (never per-client) tracking warmup stage or health status — health is strictly a per-email issue, unrelated to which client an inbox serves.
- **SPF / DKIM / DMARC**: DNS-based authentication. SPF lists authorized sending IPs/services; DKIM signs each message cryptographically; DMARC is the policy layer governing what happens on an SPF/DKIM failure.
- **IMAP vs. SMTP**: IMAP is the receiving protocol (mailbox access); SMTP is the sending protocol. Each provider has its own host; IMAP port is near-universally 993, SMTP offers legacy (465) and modern (587) ports.
- **Reply-to address**: the address that actually receives replies, which can differ from the sender (e.g., send from a founder's inbox, route replies to head-of-sales).
- **Opt-out/unsubscribe**: a safety valve — without it, angry recipients report you as spam instead of unsubscribing, tanking domain health.
- **Subsequence**: a branch triggered by detected reply sentiment — negative → apologize + confirm removal; positive → book a meeting; neutral/no reply → retry.
- **Pre-warmed / "done for you" accounts**: Instantly sells inboxes already warmed up, or a fully managed service where an Instantly-side GTM engineer runs the client's infrastructure.
- **Technographic/intent tools**: BuiltWith scans front-end/HTTP headers for tech stack (broad, surface-level); a deeper spend/ownership tool (heard as "at the inside," unclear — possibly HG Insights) flags spend and companies evaluating new tools; a third (heard as "sambal"/"someball," unclear — possibly Slintel/6sense) reportedly combines both plus team-ownership data, described as trending for account-based signal work.

## Step-by-step: how the tool was used

1. **[00:11:30]** Setup order: connect emails → enable custom tracking domain → start warmup.
2. **[00:12:31]** Warmup ramp: Week 1 — limit 10/day, +1/day. Week 2 — limit 20/day, +2/day. Week 3 — limit 30/day, +3/day. After week 3, settings become permanent at a steady low frequency (warmup never fully stops).
3. **[00:16:40]–[00:17:43]** Monitor per-inbox **health score**; if it drops (example: ~199/200 from one spam placement caused by incomplete warmup), stop outreach on that inbox and resume/continue warmup until back to 100%.
4. **[00:20:52]–[00:21:56]** Keep ~3 mailboxes per sending domain (instructor's own account runs 5, flagged as a compromise). Below 80% health, pull the inbox from campaigns and re-warm.
5. **[00:29:12]–[00:34:26]** Campaign planning, worked live: count actual working days (Mon–Fri only, unlike HeyReach's 7 days); example used 22 days. Monthly capacity = working days × mailboxes × daily limit (22 × 10 × 50 = 11,000 emails/month). Leads/month = total emails ÷ emails-per-lead (11,000 ÷ 6 ≈ 1,833). A second example (55 mailboxes, 22 days, 5-email sequence) landed near ~1,000+ leads/month.
6. **[00:34:26]–[00:35:44]** Outreach ramp for a newly active mailbox: Week 1 = 20/day → Week 2 = 30/day → Week 3 = 40/day → cap at 50/day, via Instantly's **Campaign Slow Ramp** setting rather than setting the limit to 50 immediately.
7. **[00:39:50]–[00:48:26]** Connect a mailbox (Accounts → Add New): either (a) Gmail/Outlook **OAuth** (Google Workspace admin panel → Configure New App → generate client ID → approve → connect, no password needed), or (b) manual **IMAP + SMTP** for a registrar-bought account: IMAP username = email address, IMAP password = inbox password, IMAP host/port = provider-specific (GoDaddy = `imap.secureserver.net`; Outlook = `outlook.office365.com`; port standard 993). SMTP host is also provider-specific, choosing legacy port 465 or modern port 587 (587 = first choice).
8. **[01:02:54]–[01:06:58]** Enable a **custom tracking domain**: log into the registrar (e.g., GoDaddy) → DNS settings → add the record Instantly provides, including a TTL (don't overthink it — commonly ~30–60 min) → save. Demonstrated off-recording due to credential exposure.
9. **[01:04:56]–[01:16:30]** Settings tab: add a signature; tag mailboxes by client; set a campaign **Reply-To address** distinct from the sending address; configure per-inbox **warmup settings** (warmup filter tag, week-by-week ramp values, "only send on working days" for warmup traffic — paid-plan feature); confirm an active **unsubscribe/opt-out link** is on before launch.
10. **[01:20:43]–[01:24:51]** Configure DNS-level **SPF**, **DKIM**, and **DMARC** records at the registrar before any outreach begins — non-optional.
11. **[01:26:57]–[01:29:02]** Review **Analytics** (open/reply rates) and **Unibox** (replies categorized as interested, meeting booked, out-of-office, unsubscribed, bounced); share via download/view-only access instead of status meetings. Campaign settings also include: "stop sending on reply," open tracking, daily limit (= mailboxes × per-mailbox limit, e.g., 5 × 50 = 250/day), auto-reply detection, risky-email flag, CC/BCC.
12. **[01:30:02]–[01:32:07]** Build a **subsequence** branching on reply sentiment: negative → apology + removal confirmation; neutral/no reply → retry; positive → separate meeting-booking branch. Can trigger mid- or post-campaign.
13. **[01:32:33]–[01:34:11]** Team access: Settings → Workspace and Members → invite and assign a role (e.g., Viewer) so clients can self-check campaign status.
14. **[01:38:24]–[01:39:26]** Bulk-connect mailboxes: download Instantly's sample import sheet, populate email/IMAP/SMTP credentials + daily/warmup limits, then bulk-import.

## Instructor rules, opinions & decisions (always/never)

- Never stop warmup once an inbox is "ready" — it runs permanently alongside active sending.
- Never use an inbox for campaigns once health drops below 80% — re-warm to 100% first.
- Always ramp both warmup and campaign volume gradually; never jump to the target daily limit.
- Always count actual working days (Mon–Fri) for campaign-planning math — never multiply by 30.
- Never send email campaigns on weekends (unlike LinkedIn/HeyReach, which can run 7 days).
- Keep to ~3 mailboxes per sending domain (instructor's own 5-mailbox setup is a shortcut, not a recommendation).
- Always set up a custom tracking domain rather than relying on Instantly's shared default.
- Always configure SPF, DKIM, and DMARC before sending — non-negotiable and interview-tested.
- Always include an unsubscribe/opt-out link in every campaign.
- Warmup health/tagging is strictly per-email, never per-client — don't conflate the two.
- Mastering "boring" infra fundamentals (ports, DNS, IMAP/SMTP) is a bigger career differentiator than automating email tools without understanding the mechanics first.
- Students were told to publicly document what they learn (posts, Looms comparing the three tech/intent tools using their own chosen client company) but never to tag the real client companies used as examples.

## Numbers & benchmarks mentioned

- Warmup: ~2–3 weeks total to be fully complete ("ideal" is three weeks, though clients often push for faster).
- Warmup ramp: Week 1 limit 10/day (+1/day); Week 2 limit 20/day (+2/day); Week 3 limit 30/day (+3/day); then permanent low-frequency steady state.
- Outreach ramp: 20/day (week 1) → 30/day → 40/day → 50/day cap. Health threshold: below 80% = pull and re-warm; target = 100%.
- Recommended max ~3 mailboxes/domain (instructor runs 5, calling it not ideal).
- Example agency scale: ~10 domains × 5 mailboxes = 50 mailboxes/client; at 50 sends/mailbox/day that's 2,500/day per client (a later example reaching for a bigger number landed on "25,000/day" as the rough order of magnitude for agency-scale accounts, though the exact inputs used were inconsistent).
- Reply-rate benchmark: ~1% reply rate on high daily volume, with ~10% of those replies positive — the justification for why agencies lean on volume over personalization at scale.
- Worked example: 22 working days × 10 mailboxes × 50/day = 11,000 emails/month ÷ 6 emails/lead ≈ 1,833 leads/month. Second example: 55 mailboxes, 22 days, 5-email sequence ≈ ~1,000+ leads/month.
- IMAP port: standard 993. SMTP ports: legacy 465, modern 587 (default).
- Anecdote: a GTM engineer managing a $12,000/month client retainer while earning $4,000/month himself got the infrastructure wrong for three months; deliverability collapsed, the client left, and the agency let him go.
- Instructor's own origin story: ran an email-outreach agency pre-GTM-engineering, signed 4 clients, got Instantly setup wrong, all 4 complained, and he refunded them — why he now teaches infra rigorously.
- Lemlist: 30-day free trial, per a student's report.

## Q&A worth remembering

- **Could the Sales Nav export tool ("Visa") replace Sales Navigator itself, since it claims its own database?** No — it's only an extension for pulling data out of Sales Navigator, not a standalone lead database.
- **A separate paid plan needed for the export extension, on top of Sales Navigator?** Yes for most — the one named here allowed only 3 exports/day on a paid plan. A different unnamed tool offered 100 free exports (~2,500 leads) at no cost.
- **LinkedIn-only outreach — still need to export Sales Nav data?** Yes — LinkedIn restricts native export, so anything used outside its UI needs an export step.
- **A job posting asks for Smartlead — a blocker if you only know Instantly?** No — infra setup, warmup, SPF/DKIM/DMARC, and campaign planning transfer across tools; the brand matters less than the mechanics.
- **Difference between "opt out" and "unsubscribe"?** Functionally the same — a clean exit for an annoyed recipient instead of a spam report, which damages domain health far more.

## What this means for the Saffron build

- Before any Saffron cold-email send to prospects (CTO/VP Eng/hiring-manager targets), the infra stack must exist first: dedicated sending domain(s) separate from the main trysaffron.ai brand domain, ≤3 mailboxes per domain, SPF/DKIM/DMARC at DNS, and a custom tracking subdomain — none of this can be skipped even for a small first batch.
- Warmup lead time is a hard planning constraint: since warmup takes 2–3 weeks minimum and never fully stops, domains/mailboxes need to be warming at least 2–3 weeks before the first real Saffron send — a lead-time item for her GTM plan, not a launch-week task.
- Run the campaign-planning formula before committing to a prospect-list size: with N mailboxes and a chosen sequence length, she can calculate how many Saffron prospects she can safely cover per month, which determines whether her Sales-Nav-sourced target list needs staging into batches rather than one blast.
- Given the $12K-MRR-client anecdote, any Saffron outbound test batch should start conservative (20/day ramp, ≤50/day ceiling) rather than maximizing volume on day one — a spam-flagged domain risks damaging trysaffron.ai's own sender reputation if not isolated on a separate outbound domain.
- Decide a reply-to strategy upfront — e.g., a recognizable founder/GTM persona as sender, replies routed to a shared team inbox rather than one person's personal inbox.
- Account-based intent tools that flag "a company evaluating new tools" are a plausible buying-signal layer to combine with Sales Nav people-data for Saffron's ICP — e.g., flagging companies newly adopting AI-coding or hiring tools before running the sequence above.

## Resources mentioned

- Instantly — the cohort's primary cold-email tool (paid "Growth" plan), including its CSV bulk-import template for connecting many mailboxes at once.
- HeyReach, Dripify, PhantomBuster — LinkedIn-outreach counterparts to Instantly/Smartlead.
- Smartlead — named alongside Instantly as a popular tool (and directly in a real job description a student was interviewing against).
- Sales Navigator export tools heard as "Visa" (possibly Wiza) and "EVAboard" (possibly Evaboot) — both unclear in transcript.
- BuiltWith; an intent/spend tool heard as "at the inside" (unclear, possibly HG Insights); a combined tool heard as "sambal"/"someball" (unclear, possibly Slintel/6sense) — trending for account-based signal work.
- Clay — where a student tried (unsuccessfully, due to an outage) running these lookups on a chosen client company for homework.
- Lemlist — multi-channel tool with a 30-day free trial. Anetone (spelling uncertain) — a tool some companies use to build outreach automations.
- YouTuber Tim Jacobsen — recommended for outreach-tooling content.
