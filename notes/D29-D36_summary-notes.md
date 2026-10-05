# D29–D36: Intelligence tables → email deliverability → cold email (29 Sep – 2 Oct 2026)

Source: the Gemini summary and "Next steps" sections of the four session notes, shared as screenshots. The full transcripts couldn't be downloaded, because the owner disabled downloads on these files, so this is less detailed than the D01–D28 notes. Watch the recordings in the course Drive for the live demos.

## Where these sessions sit in the course
The course moves from **L1–L3** (data, enrichment, signals: everything built in the Saffron Clay table) into **L5 Execution**, meaning actually sending outreach. These four days cover what has to be in place *before* the first email goes out: the sending infrastructure, the mailbox maths, authentication, warm-up, and then how a campaign and its emails are structured.

---

## D29+D30: Writing data out + Ship: an intelligence table (29 Sep)

**TL;DR**
- Clay tables should be built as "intelligence tables": company and people tables kept separate, with mandatory keys and quality filters.
- Tier companies by size, then map each tier to the right persona with conditional formulas.
- Plan the logic in Claude before building in Clay.
- Claude Code (with MCP and CLI tools) is where GTM engineering is heading.

**Key points**
- **Mindset:** companies pay for business outcomes and revenue impact, not for knowing tools. Understanding the underlying problem matters more than tool count. Traditional lead-gen agencies are inefficient, which is why in-house GTM engineering pays off.
- **Table standards:**
  - Company domain and company LinkedIn URL are mandatory keys for enrichment.
  - Filter out LinkedIn profiles with under 100 followers (likely fake or inactive).
  - Keep company and people tables separate.
- **Writing data out:** connect Clay to Google Sheets and to Claude for automated quality control. A **CRM upsert** means "update the record if it exists, insert it if it doesn't", which is how data gets written into a CRM without creating duplicates.
- **Company tiering:** tier companies by scale, because the right persona differs by size (a founder at 60 people, a VP Engineering at 400). Separate people tables are linked to tiers via conditional formulas, and new companies added to a tier automatically trigger the people search for that segment.
- **Workflow:** write the execution logic and prompts in Claude first, then build in Clay. Practise Clay daily.
- **Claude Code:** demoed with MCP and CLI tools, including automated LinkedIn posting via Buffer. Yogesh's view: Claude, at about $20/month, will drive future GTM engineering work.

**Homework (group)**
- Practise Clay about 2 hours a day.
- Record a personal Loom video.
- Research and sign up for GTM tools daily, comparing each with the manual process it would replace.

**What this means for Saffron**
- The Saffron build already follows most of these standards: separate accounts and People tables, domain and LinkedIn URL as keys, and a ≥100-connection filter on people.
- **Tiering is the one gap.** The persona formula treats a 99-person and a 589-person company the same. A tier column (for example 50–200 vs 200–1,000) could route founders/CTOs at small companies and VP Engineering/Head of Talent at larger ones. It fits the segments S1 and S2 already in Strategy Doc v2.
- "Writing data out" is the next step for the delivery sheet: a Google Sheets push from Clay instead of a manual CSV export.

---

## D31+D32: Deliverability is infrastructure + Domains & mailbox math (30 Sep)

**TL;DR**
- Most cold-email failures come from infrastructure and data, not copy.
- Keep emails simple: first name and company placeholders only, with AI used only for the opening line.
- Never send cold email from the company's main domain. Use separate domains and mailboxes, authenticated (SPF/DKIM/DMARC) and warmed up for about 3 weeks.

**Key points**
- **Market context (Yogesh's view):** global cold-email reply rates are around 3%, so plain B2B SaaS outbound performs poorly. Emerging verticals (travel, healthcare, manufacturing) and non-English-speaking regions respond better. He also discouraged targeting software companies, since selling software to them is hard.
- **Failure severity:**
  - Highest: infrastructure (wrong domains, no authentication) and data quality.
  - Lower: messaging, placeholders and campaign setup.
- **Messaging rules:**
  - Placeholders limited to first name and company name.
  - Don't let AI rewrite whole emails; only the opening line, using a signal.
  - Avoid "book a meeting" CTAs: cold recipients don't trust them.
- **Infrastructure:**
  - Set up SPF, DKIM and DMARC on every sending domain (they prevent spoofing and spam-folder placement).
  - Warm up for about 3 weeks, ramping from 10 to 30 emails a day per mailbox.
  - Buying mailboxes through Google Workspace or Outlook avoids manual server setup.
- **Never use the company's main domain** for outbound, so its reputation is protected if campaigns get spam complaints.
- **Campaign planning maths:** total leads × steps per sequence → emails per month → mailboxes needed.
- **Tools:**
  - Instantly suits one company sending for itself.
  - Smartlead suits agencies running many clients.
  - Email Bison: about $600/month, unlimited leads and emails, popular with agencies.
  - Base plans of sending tools are restrictive, so scaling needs a higher tier.
- **Footer links:** recipients rarely click standard unsubscribe links and report the email as spam instead. Add a plain opt-out line instead.

**Homework (group)**
- Add an opt-out P.S. to outgoing emails (e.g. "If this isn't relevant, just reply 'no' and I won't follow up").
- Review the 3 documents Yogesh shared.

**What this means for Saffron**
- Saffron would need **separate sending domains** (e.g. a lookalike of trysaffron.ai), never trysaffron.ai itself. This is the same custom-domain setup that the Apollo sign-up needs.
- **"Avoid software companies" vs Saffron's ICP:** Saffron's buyers *are* software companies, since that's who hires engineers. Ask Yogesh how this advice applies when the product itself is for engineering teams. Saffron's pain-led angle (interview load, AI-era hiring) is not a generic software pitch, which helps.
- The "AI only for the opening line" rule matches the personalization line already planned in the build sheet: one sentence using the qualification reason.

---

## D33+D34: Authentication (SPF, DKIM, DMARC) + Warm-up & sending discipline (1 Oct)

**TL;DR**
- Mailbox maths: 2,000 leads × a 6-step sequence = 12,000 emails a month. At 50 emails a day per mailbox over 22 working days, that's about 1,100 per mailbox, so roughly 11–12 mailboxes spread over 3+ domains.
- Under about 2,000 leads a month, prioritise LinkedIn over email.
- Warm-up never stops: start at 10 a day and keep a warm-up running alongside campaigns.

**Key points**
- **Infrastructure over copy:** deliverability comes first.
- **Capacity maths (worked example):**
  - 2,000 leads × 6 steps = 12,000 emails a month.
  - 50 a day × 22 days = 1,100 per mailbox.
  - Result: ~12 mailboxes across at least 3 domains.
- **Campaign planning** = pick the segment → build the lead list → warm up the infrastructure.
- **Behavioural subsequences:** automatic follow-ups that branch on what the recipient did (opened, clicked, replied).
- **Stagger follow-up intervals** so the sequence doesn't look robotic.
- **Connecting mailboxes:**
  - Google and Outlook connect through OAuth/API (client IDs).
  - Other providers use SMTP/IMAP host, port and encryption settings, which Yogesh suggests getting from an AI prompt.
- **Custom tracking domain:** a CNAME record so open and click tracking uses your own domain rather than the tool's shared one.
- **Plain text with no links** gets through strict corporate security filters more reliably.
- **Multi-channel:** email + LinkedIn + phone in a 3–4-month repeating pattern for unresponsive prospects.
- **Example signals for a biotech target:** finance hires, new CFOs, press and funding news.
- **GTM engineering vs demand generation:** demand gen focuses on nurturing and creative campaigns. GTM engineering focuses on data, list building, infrastructure and automated multi-channel sequences that hand off to sales.
- **Yogesh's claims on economics (his figures, not verified):** one GTM engineer automates work that used to take up to 10 people, at around ₹2,000/month in tools versus about ₹8 lakh in salaries.

**Homework (group)**
- **Plan 10 distinct campaigns for your company**, researching which segments or territories to target.

**What this means for Saffron**
- **Saffron's numbers are small:** 40 verified contacts × 6 steps = 240 emails. One or two mailboxes would cover that. By Yogesh's rule (under 2,000 leads → LinkedIn first), Saffron's first touch should be **LinkedIn**, with email as the second channel.
- **The 10-campaign homework maps onto what's already built:**
  - 3 segments: S1 AI-native startups, S2 growth SaaS, S3 FinTech/HealthTech
  - × 2 personas: decision maker, champion
  - × the strongest signals: hiring surge, AI coding tools, new engineering leader

  That's 10 campaigns that are easy to defend.

---

## D35+D36: Ship: a deliverability runbook + Cold email frameworks (2 Oct)

**TL;DR**
- The worked example was a classmate's live campaign for a biotech target in Instantly: a 6-email sequence, A/B tests, and micro-campaigns instead of heavy AI personalisation.
- Turn off open and link tracking: corporate security tools flag them.
- Data sourcing and Clay tables remain *the* core GTM engineering skill.

**Key points**
- **Segmentation example:**
  - US biotech and life-science companies, 51–1,000 employees.
  - Prioritised companies with lean finance teams or hiring for finance roles.
  - Tech-stack filter: NetSuite or QuickBooks users.
  - Some signals can't be tracked, like "uses Excel", because no public data exists.
- **Sequence structure:**
  - 6 emails, follow-ups 2–5 days apart.
  - The final email offers options (wrong budget, wrong timing, or not relevant) so a reply is easy.
- **A/B testing:** run two variants per email, e.g. an industry-pain angle vs an integration angle.
- **Micro-campaigns:** narrow, niche segments with a tailored message beat complex AI personalisation of every email.
- **Non-responders** get a follow-up sequence based on their engagement once the first campaign ends.
- **Tracking:** disable open and link tracking, because corporate cybersecurity software flags them.
- **Provider matching:** send Google→Google and Outlook→Outlook.

**Homework**
- Mostly individual, for the classmate whose campaign was reviewed: set up the campaign, add B variants, upload leads, and record a Loom of the campaign creation.
- For everyone: research email tracking and open-rate best practice, and keep improving Clay tables. Yogesh will review each person's table.

**What this means for Saffron**
- The cold-email framework maps directly onto the Saffron one-liners in Strategy Doc v2:
  - **Email 1:** the signal-led opening line plus the S1 offer.
  - **Emails 2–5:** a different proof point each time: interview hours saved, AI-fluency evidence, session replay, fairness/auditability.
  - **Email 6:** the "options" close.
- A/B pair idea: "your interviews don't test AI use" (pain) vs "results in hours, zero interviewer time" (outcome).
- **Expect Yogesh's table review:** the Saffron table and the delivery sheet are ready to show.

---

## Contradictions and questions for Yogesh
1. **Tracking:** D33 covers setting up a custom tracking domain, while D35 says to disable open and link tracking. Is the advice "tracking domain only if you track at all, and default to no tracking"?
2. **Software companies:** D31 discourages targeting software companies, but Saffron's buyers are by definition engineering-led software teams. How should that advice apply here?
3. **Volume:** with 40 contacts (under 2,000), should Saffron's first campaign be LinkedIn-only, with email held back until the custom domain is warmed up?

## Updated to-do items for Deepu
- **10 campaigns for Saffron:** the D33–D34 homework. Use segments × personas × signals as above.
- **Personal Loom:** the D29–D30 homework, which overlaps with the 5 portfolio Looms already on her list.
- **Before any email is sent:**
  - a separate sending domain
  - SPF/DKIM/DMARC
  - 3 weeks of warm-up
  - an opt-out P.S.
  - plain text
  - tracking off
  - Google→Google matching
  - the existing MX check
- **Clay:** practise daily, and consider adding a company-tier column (D29–D30).
