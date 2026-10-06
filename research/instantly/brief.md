# Research brief: Saffron × Instantly cold-email homework (D29–D36)

Shared by both research tracks (Claude and Gemini). Today is 6 Oct 2026. Use current (2025–2026) sources. **Every factual claim needs a source URL** (or a repo file path for class content) and a confidence level (high / medium / low). Say "not found" rather than guess. Where a source disagrees with the class instructor (Yogesh), say so explicitly.

## Who it's for
Deepshikha ("Deepu") is an experienced full-stack/data engineer in a 12-week GTM Engineering cohort (Stable GTM, instructor Yogesh Jaiswal). Her portfolio company is **Saffron** (YC S26, trysaffron.ai): an AI-native technical-assessment platform. Candidates build a real feature on the hiring company's own codebase in a browser IDE with Claude Code; Saffron records the process, attributes each line to human or AI, and 10+ AI reviewers score it. Results in hours, zero interviewer hours. Pricing: $199/mo (5 assessments), $499/mo (15), Enterprise custom. First assessment free. Competitors: HackerRank, CodeSignal, CoderPad, Karat, Rounds.so, HackerEarth, micro1, in-house take-homes.

**She missed classes D29–D36**, so the guide has to teach them in depth, not just give the assignment steps.

## The assignment
1. **D33–34 homework:** plan 10 distinct campaigns for your company (segments/territories).
2. **D35–36 homework:** set up the campaign in **Instantly**, add **B variants**, upload leads, record a **Loom** of the campaign creation. Also research **email tracking and open-rate best practice**.
3. **Deliverability prerequisites** from D31–34: a separate sending domain, SPF/DKIM/DMARC, warm-up, an opt-out P.S., plain text, tracking off, Google→Google.
Like the HeyReach homework: **configure but don't launch.** No sending domain has been bought yet.

## Saffron facts to use (from the repo)
- Strategy: `strategy/strategy-doc-saffron-v2.md` covers segments S1 (AI-native/DevTools, 50–200), S2 (growth SaaS/Cloud/Cyber, 200–1,000), S3 (FinTech/HealthTech regulated). Personas: decision maker (CTO/VP Eng, Head of TA) and champion (Eng Manager, Technical Recruiting Lead). Top signals: SWE hiring surge, recent funding, new eng/talent leader, AI coding tools in JDs, AI-hiring discussion. Messaging one-liners per segment.
- Data: `data/saffron_people_export.csv` has 50 people at 17 companies, **40 with a verified work email**; 26 decision makers, 19 champions. Clay table "Saffron | Qualified Pipeline".
- Clay build: `clay/build-sheet.md`.
- LinkedIn campaign already drafted for CHROs: `homework/D37-D38_heyreach-chro-campaign.md`.

## Class material (read these)
- `notes/D29-D36_summary-notes.md`: the four sessions (summaries only; transcripts were download-locked).
- `notes/X3_instantly-training.md` and transcript `source/X3_instantly-training.md`: Instantly training video.
- `source/REF_learning-guide.md` lines ~1412–1900: D30 and D31–D40 of the official learning guide.
- `notes/00-cohort-master-notes.md`, `notes/D03-D04_*.md` (7-layer model, Instantly demo), `notes/D21-D22_*.md` (benchmarks, portfolio).

## Questions
1. **Instantly as of Oct 2026:** plans and pricing (Outreach vs. Lead/SuperSearch vs. CRM add-ons), the free trial, and whether a campaign can be fully built (sequence, variants, leads, schedule) **before any mailbox is connected**, and saved without launching. Lead CSV import and custom-variable mapping. Sequence editor: steps, delays, A/Z variants per step, spintax. Schedule and timezone. Daily limit per campaign and per account. Stop on reply / stop on auto-reply. Open and link tracking toggles. Text-only / plain-text mode. Unsubscribe header / list-unsubscribe. Warm-up (pool, health score, slow ramp). Inbox placement tests. Subsequences. Unibox. Custom tracking domain. "Done-for-you" mailboxes and domains (pre-warmed): cost and the trade-offs.
2. **Deliverability in 2026:** Gmail, Yahoo and Microsoft (Outlook.com, May 2025) bulk-sender rules: SPF/DKIM/DMARC alignment, one-click unsubscribe (RFC 8058), spam-rate thresholds (0.1% / 0.3%). Do they apply to cold B2B senders below 5,000/day? Lookalike-domain practice (.com vs. other TLDs, naming), mailboxes per domain, safe daily caps per mailbox, warm-up length, Google Workspace vs. Microsoft 365 mailboxes, and the cost of Saffron's minimal setup. Example DNS records for SPF, DKIM and DMARC (p=none → quarantine), and the DMARC rua reporting address. MX check / catch-all handling.
3. **Tracking:** Apple Mail Privacy Protection and the unreliability of open rates. Do tracking pixels and link tracking hurt deliverability in 2026? The custom tracking domain (CNAME): what it fixes and what it doesn't. Recommended practice for cold email. Resolve the class contradiction: D33 taught "set up a custom tracking domain" and D35 said "turn tracking off".
4. **Cold-email copy in 2026:** length (word count), subject lines, the 6-step cadence and gaps, follow-ups as replies in thread vs. new threads, the "options"/breakup close, A/B test design (one variable, sample size per variant before declaring a winner), benchmarks for reply and positive-reply rates (Instantly's own benchmark report if one exists), soft CTA vs. meeting ask, using the AI opener only.
5. **Saffron's buyers:** engineering leaders (CTO, VP Eng) and talent/recruiting leaders at 50–1,000-person tech companies. Their 2025–26 pain in AI-era technical hiring (AI cheating in take-homes, interviewer hours, AI-fluency assessment), with any data (surveys, reports). How competitors position themselves now (HackerRank, CodeSignal, CoderPad, Karat), so Saffron's copy stands apart.
6. **Compliance:** CAN-SPAM requirements (physical address, opt-out), GDPR/PECR legitimate interest for UK/EU B2B cold email, Canada CASL (stricter), and whether India's DPDP Act matters (the sender is in India, the prospects in the US).
7. **Class-topic depth:** for each D29–D36 topic, the authoritative explanation, a worked example and current numbers:
   - intelligence tables, company tiering → persona mapping, CRM upsert
   - email infrastructure: domains, mailboxes, OAuth vs. SMTP/IMAP
   - SPF, DKIM and DMARC mechanics and alignment
   - warm-up mechanics and health score, slow ramp, mailbox maths
   - behavioural subsequences, multichannel cadence (email + LinkedIn + phone)
   - Instantly vs. Smartlead vs. Email Bison
   - cold-email frameworks, A/B testing, micro-campaigns vs. AI personalisation

## Output format
Markdown. One section per question (1–7). For each, a bullet per finding: **claim** · source URL · confidence. Finish with a section "Where sources disagree with the class", then a section "Open questions I could not resolve".
