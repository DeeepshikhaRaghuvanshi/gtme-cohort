# LinkedIn Sales Navigator Walkthrough (2026-07-21)

## TL;DR

- Sales Navigator is the "source of truth" for **precision lists** — lists under ~1,000 people where every lead matters (all CTOs in New York, an event invite list, an advisory-board list). Apollo/Prospeo undercount these because senior people often opt out of third-party databases but can't opt out of LinkedIn itself.
- Sales Nav has no native CSV export. You need a separate export extension (heard as "Visa" in transcript, likely **Wiza** — unclear in transcript) or route through Clay's "external search" via a copied Sales Nav search URL.
- Seniority filtering in Sales Nav doesn't match a standard title ladder. There's no "Head" filter — build it by selecting CXO + Director + VP, then adding "head" as free text.
- Always tick **"Strategic"** on senior-people lists — it catches decision-makers with nonstandard titles ("Digital Asset Technology Leader," "Field CTO") who don't hold a clean C-level title but do make the calls.
- HeyReach ("Hairies"/"hair each" in transcript — clearly **HeyReach**) beats Dripify for LinkedIn outreach because its basic plan allows ~40/day sends vs. Dripify's 20/day (needing two Dripify seats to match one HeyReach seat).
- LinkedIn replies stay manual — no AI auto-reply, because the sending profile is a real person's identity. LinkedIn also detects and bans automation aggressively, so sending accounts were never connected during this training.

## Key concepts

- **Precision list**: a sub-1,000-person list where quality/coverage matters more than volume — events, advisory boards, narrow senior outreach — vs. high-volume Apollo-style prospecting lists.
- **Coverage**: the % of the true matching universe a source actually surfaces. Sales Nav approaches 100% since people can't remove themselves from LinkedIn; Apollo/Prospeo coverage is lower because people can request removal from those databases.
- **Account list vs. lead list**: an account list is a CSV of target companies uploaded into Sales Nav. Once filtering off an uploaded account list, Clay's URL-based export trick stops working — you need a dedicated export tool.
- **Strategic filter**: Sales Nav's tag for people who influence/make decisions despite lacking a matching formal title.
- **LinkedIn senders**: the individual profiles (client/founder, never a company page) connected into HeyReach to run outreach.
- **Infinite login vs. credentials login** (HeyReach): infinite login = you authorize once and it persists; credentials login = the client hands you their LinkedIn username/password directly (typical agency setup).
- **Exclusion list**: a per-client blacklist (current customers, active pipeline, competitors) supplied by the client and uploaded before a campaign runs.

## Step-by-step: how the tool was used

1. **[00:07:49]** Set Sales Nav filters: Geography (e.g., New York), Current job title (e.g., CTO), Company employee count (e.g., 10,000+).
2. **[00:11:03]** Compare tools on the same filter: Prospeo returned 126 matching CTOs vs. Sales Navigator's 464 — the coverage gap, live.
3. **[00:12:07]** Save matches by checkbox → "Add to list" (25 people/page, no native export — repeat per page).
4. **[00:13:14]** Install a Sales Nav export extension (heard as "Visa," likely **Wiza** — unclear) to get an in-UI "Export" button. Exports are "expensive and limited."
5. **[00:15:21]** Note Sales Nav has no funding-related filters (that data lives in Apollo).
6. **[00:16:26]–[00:17:27]** Seniority labels in Sales Nav: Entry Level, Director in Training, Experienced Manager, Owner, Partner, Entry-Level Manager, Chief Officers (CXO), VP, Strategic, Senior.
7. **[00:17:27]** For "Head of X" (no native filter): select CXO + Director + VP, then type "head" into the filter search box.
8. **[00:18:31]–[00:19:38]** Always add **Strategic** to senior lists to catch nonstandard titles like "Field CTO."
9. **[00:19:38]–[00:20:42]** Uncheck "In Training" and "Entry-level" to remove junior title-holders that slip into senior-title searches.
10. **[00:24:57]–[00:25:44]** Export via Clay instead of a paid tool: Sales Nav → **External Search** → copy search URL → paste into Clay's external search → submit. Works only for URL-based searches, not uploaded account lists.
11. **[00:25:44]–[00:27:04]** Enable Sales Nav's **"posted on LinkedIn in last 30 days"** filter before uploading a list into LinkedIn automation — checking the same signal in Clay burns heavy credits.
12. **[00:27:04]–[00:28:12]** Save recurring filter combos as **Custom Personas**.
13. **[00:27:49]–[00:28:59]** US geography rule: where a name is both state and city (e.g., New York), pick the **state**-level entry — it covers the city too; narrower entries under-cover.
14. **[00:41:58]–[00:43:06]** In HeyReach: New Campaign → unique name → upload **Exclusion list** → tick "exclude leads from other campaigns/senders/same sender."
15. **[00:43:06]** Build a **Lead list** (manual, or import from LinkedIn search, Sales Nav, Recruiter, events, post engagement, CSV, HubSpot).
16. **[00:43:06]–[00:47:18]** Build the **sequence from scratch** (never templates). Example: view profile → like post (<1 month) → send connection request (A/B: text note vs. blank) → if not accepted, like post again (<3 weeks) → if accepted, message → if no reply, like post (<1 week) + message again → if still no reply, react/support latest post (<1 week) → if still no reply, push the lead to Instantly/Smartlead referencing the failed LinkedIn touches.
17. **[00:48:19]** Schedule: start today, no end date, set time zone/active hours, and — unlike email — **include Saturday and Sunday**.
18. **[00:52:31]–[00:53:34]** Connect a LinkedIn account in HeyReach's Senders tab via **Infinite login** (self-owned) or **Credentials login** (client-supplied, agency norm).

## Instructor rules, opinions & decisions (always/never)

- Always use Sales Navigator, not Apollo/Prospeo, for precision lists (<1,000 people).
- Never try to build advisory-board lists (retired-but-senior, "in role >10 years then retired") outside Sales Navigator — Apollo/Prospeo "didn't work" for this per his own client experience.
- Always tick "Strategic" for senior lists; build "Head" via CXO+Director+VP+free text since no native filter exists.
- Always pre-check the "posted in last 30 days" filter in Sales Nav (not Clay) before any list feeding a "like their post" automation step.
- Never build LinkedIn sequences from templates — always from scratch.
- Always connect the actual person's profile to HeyReach, never a company page.
- Never connect real/practice LinkedIn accounts to HeyReach during training — one automation tool per account, and LinkedIn bans aggressively.
- Never automate LinkedIn replies with AI — replies are handled manually since the sender is a real identity.
- Don't trust "best practice" claims (e.g., "never send a note with a connection request") — A/B test blank vs. noted requests per market/profile.
- Personal safe LinkedIn sending limit: ~25/day, even though the platform technically allows more.

## Numbers & benchmarks mentioned

- Prospeo: 126 CTOs (NY, 10,000+ employees) vs. Sales Navigator: 464 for the same filter (~3.7x more coverage).
- Precision list = under ~1,000 people; Sales Nav paginates 25 people/page.
- LinkedIn native daily limit: up to ~40 connections/messages/InMails; instructor's safe number: 25/day.
- HeyReach basic plan: up to 40/day. Dripify basic plan: only 20/day (needs 2 seats to match HeyReach).
- HeyReach dashboard example: 122 requests sent over 7 days (~17/day).
- Real incident: HeyReach showed 0 requests sent for 2 days on an active campaign — turned out to be a front-end display bug, confirmed and fixed after escalating to HeyReach support.

## Q&A worth remembering

- **Is dedup done with Clay code?** No, not at this stage — too advanced. Use native dedup: LinkedIn URL first, then email, then full name + company (common names like "Shreyas GV" repeat across companies).
- **If someone posts a public Calendly link for an event, why still run a LinkedIn sequence at them?** Because the people you cold-outreach (not yet connected) are a different set from the people who see your organic posts (mostly existing connections) — a senior CEO's public link won't be found by your specific cold target at scale.
- **Can Sales Nav find companies using Workday (an install-base question)?** No — Sales Nav is people-first, not company/technographic. That needs Clay with a technographic source, not Sales Navigator.
- **Should connection requests always be blank?** Don't assume — test blank vs. noted as two campaign variants and let your own data decide.
- **Can one LinkedIn account be connected to two automation tools at once?** No — only one at a time.

## What this means for the Saffron build

- Saffron's ICP (US AI/devtools startups, 51–200 employees, hiring engineers) is a textbook precision-list case per this framing — likely well under 1,000 qualifying accounts, so Sales Navigator should be the primary source for the actual decision-maker (CTO/VP Eng/Head of Eng), cross-checked against Apollo/Clay for filters Sales Nav lacks (funding stage, tech stack).
- Filter recipe to replicate: Geography = US, headcount ≈ 51–200 (verify closest Sales Nav bucket), seniority = CXO + Director + VP + **Strategic** (to catch "Founding Engineer"-type roles that actually own hiring), plus free-text "eng"/"engineering" to surface Head-of-Eng titles the seniority filter misses.
- Before any LinkedIn outreach to Saffron prospects, run the "posted in last 30/90 days" filter in Sales Nav (not Clay) to avoid wasted credits and dead "like their post" sequence steps.
- "Hiring engineers" as a buying trigger isn't a native Sales Nav filter — that signal needs a separate source (job-post scraping, Apollo, intent tool), with Sales Nav used afterward to find the named decision-maker at flagged companies.
- Given LinkedIn's aggressive automation detection, any Saffron hiring-manager outreach should stay conservative (~25/day cap) rather than blast, especially since the target list size fits the "precision list" mold.
- Save a Custom Persona for "Saffron ICP: US AI/devtools 51-200, CTO/VP Eng/Head Eng, Strategic" so this filter doesn't need rebuilding each session.

## Resources mentioned

- Sales Navigator — instructor's view: doesn't need deep study/practice; a personal login is "not needed" for this cohort.
- Export extension heard as "Visa," likely **Wiza** (unclear in transcript); credentials to be shared separately.
- Prospeo — used for the live coverage comparison against Sales Navigator.
- Apollo — for company/firmographic/funding filters Sales Nav lacks; full re-cover deferred since already taught (D11–D12).
- Clay — used for the URL-based external-search export trick; costly in credits for post-activity checks.
- HeyReach — the cohort's primary LinkedIn automation tool (instructor has a paid seat); homework was building a from-scratch sequence.
- Dripify — HeyReach's main competitor, positioned as better for personal-brand/network growth than lead-gen at scale.
- Instantly and Smartlead — the email tools a LinkedIn sequence hands non-responsive leads to.
- The cohort's shared learning-guide/curriculum roadmap, reviewed at [00:57:53]–[01:01:04]: Days 1–2 GTM engineering intro, Day 3 seven-layer model, Day 4 workspace setup, Day 5 company adoption/ICP, Days 7–8 signals/triggers, Days 9–10 GTM strategy brief, data layer (Apollo, then this Sales Nav session), next up: data-quality fundamentals, shipping an account list, then Clay (weeks 4–6).
