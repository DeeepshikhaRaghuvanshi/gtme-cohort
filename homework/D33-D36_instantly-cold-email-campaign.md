# Homework (D33–D36): Saffron cold-email campaign in Instantly, plus the classes you missed

**For:** Deepu · **Written:** 6 Oct 2026 · **Rule (same as HeyReach):** build everything in Instantly, but **don't launch**.

**What's in here**
- **Part A** teaches D29–D36 and the Instantly training video in depth, because you missed those classes: what each topic is, why it matters, how it works, Yogesh's rules and numbers, what current sources say, and what it means for Saffron. Each topic ends with "be able to explain", which are the points Yogesh says come up in interviews.
- **Part B** is the homework itself: the 10-campaign plan (D33–34), the deliverability plan for Saffron, the lead prep in Clay, the Instantly build step by step (D35–36), every email ready to paste, the Loom outline and a checklist.

**How this was researched.** Two independent tracks: Claude (class notes, transcripts, the official Learning Guide, plus web research on primary sources: Instantly's help center, Google, Yahoo, Microsoft, the IETF, the FTC) and Gemini 3.1 Pro (same brief). Each track checked the other, and the conflicts were resolved against primary sources. Instantly facts come from its help center as of Oct 2026. Where current sources disagree with what was said in class, the guide says so with a **Research says** line, so you can raise it with Yogesh rather than be surprised. The research files are in the repo under `research/instantly/`.

---

# Part A: the classes you missed (D29–D36)

## A0. Where these classes sit

The course follows the **7-layer GTM stack** (D03–D04). Everything you built so far in Clay is layers 1–3: **data** (Apollo, Prospeo, Sales Nav), **enrichment** (waterfalls, Claygent) and **signals** (hiring surges, AI tools in job ads). D29–D36 move into **L5 Execution**: actually reaching people. HeyReach (D37–38) is the LinkedIn half of L5; Instantly is the email half.

The chain you're now completing:

**Clay intelligence table** (who to contact, why now, one insight per person) → **write the data out** (CSV, Sheets or a webhook) → **sending infrastructure** (domains, mailboxes, DNS, warm-up) → **Instantly campaign** (leads, sequence, variants, schedule, options) → **Unibox** (replies) → later, **CRM** (L6).

Yogesh's headline for these four days: **most cold-email failures come from infrastructure and data, not copy.** A brilliant email from a cold, unauthenticated domain lands in spam or gets rejected. A dull email from a healthy domain to the right person at the right moment still gets replies. That's why the course spends a week on plumbing before it lets you write copy.

## A1. D29–D30: Intelligence tables and writing data out (29 Sep)

**What it is.** An *intelligence table* is a Clay table that takes a company in and puts out one clean, outreach-ready row: who to contact, their verified email, why they qualify, and a one-line **insight** you can open an email with. The Learning Guide calls it "company in → scrape + Claygent research + waterfall email → one clean row with a personalized insight field" (portfolio deliverable #6).

**The mindset Yogesh opened with.** Companies pay for business outcomes and revenue impact, not for knowing tools. Understanding the underlying problem matters more than how many tools you can name. Traditional lead-gen agencies are inefficient, which is why in-house GTM engineering pays off. His claim (unverified): one GTM engineer can automate work that used to take up to 10 people, at around ₹2,000 a month in tools against about ₹8 lakh in salaries.

**Yogesh's table standards**
- **Company domain and company LinkedIn URL are the mandatory keys.** Every enrichment matches on one of them, so a row without them is dead weight.
- **Keep company and people tables separate.** One row per company in one table, one row per person in another, linked by domain. You already do this (`saffron_50_accounts` and the people table).
- **Filter out LinkedIn profiles with under 100 followers or connections.** They're often fake or inactive, and they hurt both acceptance rates and data quality.

**Company tiering → persona.** The right buyer changes with company size. Yogesh's example: at 60 people the founder decides; at 400 it's the VP Engineering. So you tier companies by headcount and map each tier to a persona with a conditional formula. New companies that land in a tier automatically trigger the people search for that tier's persona. For Saffron:
- **Tier S1, 50–200 employees:** CTO or co-founder decides alone, often interviews every candidate personally.
- **Tier S2, 200–1,000:** VP Engineering or Head of Engineering decides; Head of Talent / Engineering Manager is the champion who feels the pain daily.

This is the one gap in your current Saffron table: the persona formula treats a 113-person and a 589-person company the same. Part B adds a free Tier column.

**Writing data out.** Enrichment is worthless if the data stays in Clay. Three ways out: a **native integration** (Clay → HubSpot, Clay → a sequencer), a **CSV export**, or an **outbound webhook** that posts the row to any URL (this is how Clay talks to n8n later in the course). The professional habit is **conditional export**: only rows that are ready leave Clay (for example "verified email AND qualified"), and you **confirm the data landed**, because a handoff that silently fails is the most common and most expensive orchestration bug.

The class demo wrote Clay data out to **Google Sheets** (the next step for your delivery sheet, instead of a manual CSV export) and to **Claude for automated quality control**, so a model checks rows before they go anywhere.

**CRM upsert** means "update the record if it exists, insert it if it doesn't". It's how you write into a CRM without creating duplicates. HubSpot's API does it in batches of up to 100 records, matching on email or a unique ID property.

**Workflow tip from class:** plan the logic and prompts in Claude first, then build in Clay. Claude Code (with MCP and CLI tools) is where Yogesh thinks the role is heading.

**Homework from that class:** practise Clay about 2 hours a day; record a personal Loom; sign up for one new GTM tool a day and compare it with the manual process it replaces.

**Be able to explain:** why company and people tables are separate; what the two mandatory keys are and why; what tiering is and why the persona depends on company size; what an upsert is; why you confirm every handoff.

## A2. D31: Deliverability is infrastructure (30 Sep)

**What it is.** Getting an email *sent* is not getting it into the *inbox*. Gmail, Microsoft and Yahoo decide for every message whether it goes to the inbox, the spam folder, or is rejected outright. They decide mostly on **sender reputation**: a score they keep for your domain and sending IPs, built from your authentication, your bounce and complaint rates, and how recipients engage with your mail. The Learning Guide estimates that about **1 in 6 legitimate emails misses the inbox**.

**The three chains that send a campaign to spam** (be able to recite these as cause → effect):
- **No authentication:** missing or broken SPF/DKIM/DMARC → the provider can't prove you are who you say → mail is flagged or rejected.
- **Bad data:** an unverified list → bounces go above ~2% → your reputation drops → even your good mail starts landing in spam. Your Clay build already guards against this: the build sheet's **Sendable** rule only lets through Valid or Valid catch-all emails, and excludes addresses behind Mimecast, Proofpoint or Barracuda gateways.
- **Generic blast:** a templated message to the wrong people → recipients click "report spam" → complaints cross 0.3% → the provider stops delivering your mail.

**Yogesh's failure-severity ranking:** highest is infrastructure (wrong domains, no authentication) and data quality; lower is messaging, placeholders and campaign setup.

**His market view:** global cold-email reply rates are around **3%**, so plain B2B SaaS outbound performs poorly. Emerging verticals (travel, healthcare, manufacturing) and non-English-speaking regions respond better. He discouraged targeting software companies, because selling software to software companies is hard.

**Research says** (reply rates): Instantly's 2026 benchmark report (2025 data) puts the average reply rate at **3.43%**, the top quartile at 5.5%+ and the top 10% at 10.7%+. Hunter's 2026 report also has 3% for sales outreach. So Yogesh's 3% is right. Lemlist reports SaaS and software reply rates often below 2%, which backs his caution about software.

**What it means for Saffron.** Saffron's buyers *are* software companies, because they're the ones hiring engineers. Yogesh's warning doesn't remove the segment; it means the generic "we're a SaaS tool" pitch won't work. Saffron's angle is a pain these teams feel personally (interview hours, AI cheating), which is the kind of message that beats the average. It's still worth asking him (it's in the questions list).

**Messaging rules from this class** (they apply to every email in Part B):
- Placeholders: **first name and company name only**.
- AI writes **only the opening line**, from a real signal. Never let AI rewrite the whole email.
- **No "book a meeting" CTAs.** Cold recipients don't trust them.
- Add a plain **opt-out line** instead of relying on a footer unsubscribe link, because annoyed recipients don't hunt for the link; they hit "report spam", which hurts far more. Homework from that class: add a P.S. like "If this isn't relevant, just reply 'no' and I won't follow up." Also: review the 3 documents Yogesh shared after the session (in the course folder).

**Be able to explain:** the difference between sent and delivered; what sender reputation is built from; the three chains to spam; why infrastructure beats copy.

## A3. D32: Domains and mailbox maths (30 Sep)

**Never send cold email from the company's main domain.** If trysaffron.ai gets a bad reputation, Saffron's invoices, contracts, password resets and customer replies start landing in spam. Instead you buy **secondary domains** that look like the brand and are used only for outbound. If one burns, you retire it and the real domain is untouched.

**Naming.** Lookalikes of the brand, e.g. `trysaffronhq.com` or `getsaffron.com` style names (check availability, and Saffron must approve any domain that uses its name). Avoid hyphens and anything that pattern-matches spam. Set the new domain to **forward to the main website**, so anyone who checks it lands on trysaffron.ai.
- **Research says** (TLDs): the Learning Guide suggests alternate TLDs like .co or .io. Instantly's help center says **.com works best**, and its own done-for-you service only offers .com and .org. Prefer .com.

**Mailboxes per domain.** Yogesh's rule: about **3 mailboxes per domain** (he runs 5 on one domain and called that "not a good idea"). Instantly says at most 3–5. Spreading mailboxes over several domains limits the damage if one domain gets flagged.

**Where mailboxes come from.** Buy them through **Google Workspace** or **Microsoft 365** rather than a registrar's own email, which saves you manual server setup and gives you better reputation. Prices as of Oct 2026: Google Workspace Business Starter about ₹270 a user a month in India (about $7–8.40 in the US); Microsoft 365 Business Basic went up to $7 a user a month on 1 Jul 2026.

**Provider matching.** Send Google → Google and Outlook → Outlook. Mail between the same provider tends to land better. Instantly has a setting for this ("Provider Matching" / ESP matching), and it falls back to any mailbox if there's no match rather than waiting. Having one or two of each gives you coverage; for a small list, Google alone is fine.

**The mailbox maths.** Each mailbox can only send a limited number of cold emails a day, so volume decides how many mailboxes and domains you need:

**Emails needed per month = leads × steps in the sequence.**
**Capacity per mailbox per month = daily cold limit × working days (Mon–Fri, about 22).**
**Mailboxes needed = emails needed ÷ capacity per mailbox.** Then spread them over domains at ~3 per domain.

Yogesh's worked example (D33): 2,000 leads × 6 steps = 12,000 emails a month. At 50 a day × 22 days = 1,100 per mailbox → about 11–12 mailboxes over at least 3 domains.

**Research says** (daily limit): Instantly's own help center recommends **30 campaign emails + 10 warm-up emails per mailbox per day**, not 50. Its done-for-you AirMail mailboxes are capped at 20. The Learning Guide says 20–30. Redo Yogesh's example at 30 a day: 30 × 22 = 660 per mailbox → 12,000 ÷ 660 ≈ **19 mailboxes over 4–7 domains**. Say both in an interview: "Yogesh plans at 50; Instantly recommends 30, which needs more mailboxes but protects reputation."

**Count working days only.** Email campaigns don't send at weekends, so never multiply by 30 days. (HeyReach on LinkedIn can run 7 days.)

**The tools (D31–32 comparison, with Oct 2026 prices):**
- **Instantly:** suits one company sending for itself. Outreach plans: Growth $47/mo (5,000 emails, 1,000 uploaded contacts), Hyper Growth $97/mo (125,000 emails, 25,000 contacts), Light Speed $358/mo. Unlimited mailboxes and warm-up on every paid plan. **Research says:** it now also has agency white-labelling and workspace groups, so "single company only" is a bit outdated.
- **Smartlead:** suits agencies running many clients (client workspaces, white label). Base $39/mo, Pro $94, Smart $174, Prime $379.
- **Email Bison:** about $600/mo (it's $599 for 500,000 emails a month), with isolated sending infrastructure and dedicated IPs; popular with agencies. **Research says:** leads are unlimited but emails aren't (500,000 a month, more in paid buckets).
- Base plans of every sending tool are restrictive, so scaling means a higher tier.

**Pre-warmed and "done-for-you" (DFY) mailboxes.** Instantly sells mailboxes it sets up for you. Yogesh said pre-warmed accounts "save three weeks but make no sense" because they aren't your domains. The research backs him: with DFY and pre-warmed mailboxes **Instantly keeps ownership of the domain** and can't transfer it, the mailboxes only work inside Instantly, only .com/.org are offered, and if you cancel you lose access at once. All three carry $15 per domain a year, plus per mailbox: DFY $5 a month; pre-warmed $10 a month (you can't choose the domain name); AirMail $4 a month (20 a day max). For Saffron, a do-it-yourself setup you own is the better choice.

**Be able to explain:** why never the main domain; how to name secondary domains; mailboxes per domain and why; the mailbox formula, worked both at 50/day and at 30/day; when you'd pick Instantly, Smartlead or Email Bison.

## A4. D33: Authentication: MX, SPF, DKIM, DMARC (1 Oct)

These are **DNS records** you add at the domain registrar (GoDaddy, Namecheap, Cloudflare…). They prove to receiving servers that your mail is really from you. Yogesh says these three acronyms come up in **every email-outreach interview**. As an engineer, think of them as an allow-list, a signature and a policy.

**MX (Mail Exchange):** which servers *receive* mail for the domain. You need it so replies reach your mailbox. For Google Workspace it's a single record: host `@`, priority 1, value `smtp.google.com`.

**SPF (Sender Policy Framework): the allow-list.** A TXT record listing which servers may *send* mail for your domain. The receiver checks whether the server that delivered the message is on the list. Example for Google Workspace:

```
Type: TXT   Host: @   Value: v=spf1 include:_spf.google.com ~all
```

`include:` pulls in Google's list of sending servers; `~all` means "anything else is suspicious" (soft fail), which Google recommends. Rules: **only one SPF record per domain**, and at most 10 DNS lookups (includes) in it. A second SPF record or a typo silently breaks authentication.

**DKIM (DomainKeys Identified Mail): the signature.** Your mail server signs each message with a private key; you publish the public key in DNS; the receiver uses it to check that the message really came from your domain and wasn't altered on the way. In Google Workspace you generate it in the Admin console (Apps → Google Workspace → Gmail → Authenticate email), choose a 2048-bit key, and publish it as:

```
Type: TXT   Host: google._domainkey   Value: v=DKIM1; k=rsa; p=<long public key from Google>
```

Google only lets you generate the key 24–72 hours after Gmail is activated on the domain, and it can take up to 48 hours to start working. Then click "Start authentication".

**DMARC (Domain-based Message Authentication, Reporting and Conformance): the policy.** It tells receivers what to do when a message fails SPF and DKIM, and where to send reports:

```
Type: TXT   Host: _dmarc   Value: v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

- `p=none`: monitor only; nothing is blocked. Start here.
- `p=quarantine`: failing mail goes to spam. Move here after 2–4 weeks of clean reports.
- `p=reject`: failing mail is refused. The end state for a mature domain.
- `rua=`: the address that receives daily aggregate reports, so you can see who is sending as your domain.

**Alignment (the subtle part).** DMARC doesn't just check that SPF or DKIM passed. It checks that the domain that passed **matches the visible From address**. A message from `deepu@yourdomain.com` passes DMARC only if SPF passed for `yourdomain.com` (the envelope sender) or the DKIM signature's `d=` domain is `yourdomain.com`. "Relaxed" alignment, the default, accepts subdomains of the same domain. This is why "SPF passes but DMARC fails" happens: the wrong domain passed.

**Research says** (two updates since the course material was written):
- **DMARC is now an official standard: RFC 9989 (May 2026)**, which replaces RFC 7489. It removed the `pct` tag (the "apply the policy to only 25% of mail" rollout trick that older guides and Google's help page still show) and added `t=y` for test mode. Existing records with `pct` keep working in practice while receivers catch up. You don't need either for Saffron; just know the RFC number exists if an interviewer is current.
- The Learning Guide says "Gmail permanently rejects mail from senders without DMARC". That's overstated: Google formally requires DMARC only from **bulk senders** (5,000+ messages a day to personal Gmail addresses). Since November 2025 Gmail does reject (temporarily or permanently) mail that breaks its requirements. Either way, set up all three; they're free.

**What the big providers require in 2026** (from their own pages):
- **Gmail, every sender:** SPF *or* DKIM; valid forward and reverse DNS; TLS; a spam rate under 0.3% in Postmaster Tools. **Bulk senders** (5,000+ a day to personal Gmail; the count is per domain, and once you're a bulk sender you stay one) also need **SPF and DKIM and DMARC** (`p=none` is enough), From-domain alignment, and **one-click unsubscribe** for marketing mail, honoured within 48 hours.
- **Yahoo:** the same shape: SPF or DKIM, spam under 0.3%, valid DNS for everyone; for bulk senders, DMARC, alignment and one-click List-Unsubscribe honoured within 2 days.
- **Microsoft (Outlook.com, Hotmail, Live), since 5 May 2025:** domains sending 5,000+ a day must pass SPF, DKIM and DMARC (at least `p=none`, aligned). Non-compliant mail is now rejected with the error "550 5.7.515 Access denied".
- **One-click unsubscribe (RFC 8058)** is a pair of email headers (`List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`), not a DNS record. It lets the mail app show an "Unsubscribe" button. Instantly adds a List-Unsubscribe header if you tick "Insert unsubscribe link header" in campaign options.

**A surprise that matters for Saffron:** Google's page says its sender requirements "don't apply to messages sent to **Google Workspace accounts**", only to personal @gmail.com addresses. Saffron's prospects are on company domains, many of them on Google Workspace, so the formal bulk rules mostly don't apply. **That doesn't mean "skip it":** Workspace and Microsoft 365 still run their own spam filtering, and corporate security gateways (Mimecast, Proofpoint, Barracuda) are stricter still. Treat the rules as the minimum.

**Verify before you send.** Use **mail-tester.com** (send a test email, get a score out of 10 with each record checked) or **MXToolbox** (look up each record). Instantly's Email Accounts dashboard also shows whether MX/SPF/DKIM/DMARC are set for each mailbox, and its paid inbox placement test checks authentication and 94 blacklists.

**Be able to explain:** what MX, SPF, DKIM and DMARC each do, in one sentence each; why all three together; the DMARC p=none → quarantine → reject progression; what alignment means; who the bulk-sender rules apply to.

## A5. D34: Warm-up and sending discipline (1 Oct)

**Why warm-up exists.** A brand-new domain that suddenly sends 100 emails a day looks exactly like a spammer. Warm-up builds reputation gradually: your mailbox exchanges emails with thousands of other mailboxes in a warm-up network (Instantly's pool). Those emails get opened, a share get replies, and any that land in spam are moved to the inbox. To Gmail and Outlook, your mailbox looks like a real person with real conversations.

**Why warm-up never stops.** Cold outreach is almost all *sending*, with few replies. Providers read one-way sending as misuse. So warm-up keeps running at a low level alongside your campaigns, forever. Stopping warm-up once a mailbox is "ready" is a common, costly mistake.

**Yogesh's warm-up schedule** (from the Instantly training video, "what works for me"):
- Week 1: limit 10 a day, increase +1 a day.
- Week 2: limit 20 a day, +2 a day.
- Week 3: limit 30 a day, +3 a day.
- After week 3: a permanent, low steady level. Ideal total: **3 weeks** before any campaign.

**Research says:** Instantly's warm-up settings have a single profile, with defaults of **+1 a day, a daily limit of 10, and a 30% reply rate**, and Instantly advises keeping the defaults. It calls a mailbox **ready after at least 2 weeks of warm-up and a health score above 90%** (3 weeks for its own AirMail mailboxes). Its 2026 deliverability blog and the Learning Guide both say **4–6 weeks for a brand-new domain**. Practical answer: plan for 3 weeks minimum, 4 if you can.

**Health score.** Instantly's per-mailbox trust indicator: the share of warm-up emails that landed in the inbox over the last 7 days (inbox ÷ sent × 100). It's the "Health Score" column on the Email Accounts page.
- **Yogesh:** below **80%**, pull that mailbox out of campaigns and let it re-warm until it's back at 100%.
- **Research says:** Instantly says aim for **above 90%**, and treats 90% as the readiness line. Use 90% as "safe to send", and below 80% as "stop now".
- Health drops when outreach starts before warm-up is finished, when you send to bad addresses (bounces), and when you blast volume.

**Warm-up filter tag.** Tag mailboxes by their state ("week 1", "week 2", "red alert"), **never by client**, because health is a property of each mailbox, not of the client it serves.

**The campaign ramp.** Even after warm-up, a mailbox shouldn't jump to its full daily limit. Yogesh: 20 a day in week 1 → 30 → 40 → cap at 50, using Instantly's **Campaign Slow Ramp**.
- **Research says:** Instantly's Campaign Slow Ramp setting (per mailbox: Email Accounts → the account → Settings → Campaign settings) starts at **2 emails on day 1 and adds 2 a day** until it reaches the mailbox's limit. Yogesh's weekly 20/30/40/50 steps are a manual practice, not what the toggle does.

**Thresholds you must not cross** (drill these numbers):
- **Spam complaints under 0.3%**, and aim under **0.1%**. Above 0.3%, Gmail won't help you with delivery problems until you've been back under for 7 days in a row.
- **Bounces under 2%.** Instantly auto-pauses a campaign at about 5% bounces.
- Watch the **slope**, not just the line: a complaint rate climbing week over week is a problem even below 0.3%.
- **Google Postmaster Tools** shows your domain's spam rate at Gmail. **Research says:** it may show nothing for a low-volume sender mailing mostly company domains, and Google retired its domain/IP reputation dashboards in Postmaster v2. For Saffron, Instantly's health score and inbox placement tests are the practical monitors.

**Connecting mailboxes to Instantly.**
- **Google and Microsoft: OAuth.** No password is stored. For Google Workspace you approve Instantly as a trusted app in the Admin console (Security → Access and data control → API controls → Manage app access → Configure new app → search for Instantly's client ID → "Instantly OAuth Email v1" → All users, Trusted), then log in from Instantly.
- **Anything else: IMAP + SMTP.** IMAP is *receiving* (Instantly reads replies), SMTP is *sending*. You enter the mailbox address and password plus each server's host and port. IMAP is almost always port 993. SMTP is 587 (STARTTLS, Yogesh's first choice) or 465 (SSL). Examples: GoDaddy `imap.secureserver.net` / `smtpout.secureserver.net`, Namecheap `mail.privateemail.com`. Use whatever the provider documents.
- **Many mailboxes at once:** Instantly's bulk-import CSV template (Email Accounts → Add New → Any Provider → Bulk import from CSV). Microsoft 365 mailboxes can't be bulk-imported.

**Custom tracking domain (CTD).** If you track opens or clicks, Instantly rewrites your links and adds a tracking pixel that point at a tracking domain. By default that's a domain shared with every Instantly customer, so you inherit everyone's reputation. A CTD (a CNAME record such as host `inst` → `prox.itrackly.com`, then set per mailbox as `inst.yourdomain.com`) gives you your own. Yogesh's analogy: one security guard for the whole mall versus your own guard for your own shop. Whether you should track at all is A7.

**Behavioural subsequences.** Branches that fire based on what the recipient did: replied positively, negatively, out of office, clicked, or finished the sequence without replying. Yogesh's example: of 100 sends, 50 don't reply, 20 are neutral, 10 positive, 10 negative. Negative → apologise and confirm removal; positive → a meeting-booking track; neutral or no reply → retry later. **Research says:** in Instantly, subsequences need the **Hyper Growth plan ($97)** and their tab only appears **after a campaign is launched**, so you can't build one in this homework. Describe it in your Loom instead.

**Stagger follow-ups** (vary the gaps: 2, 3, 4, 5 days) so the sequence doesn't look robotic. Instantly also adds a random gap between individual sends (default 9 minutes + up to 5 random).

**Multichannel.** For prospects who don't respond, combine email + LinkedIn + phone in a repeating pattern over 3–4 months. The Learning Guide's 2-channel example: day 1 email, day 2 LinkedIn connect, day 4 email follow-up, day 6 LinkedIn message (4–6 touches over about 10 days).

**LinkedIn first for small lists.** Yogesh: under about **2,000 leads a month, prioritise LinkedIn** (about 30% reply rate vs 1–4% for email). Saffron's list is 40 verified contacts, so in a real run the engineering leaders would get a LinkedIn touch first and email as the second channel. The homework still builds the email side, because the portfolio needs both.

**GTM engineering vs demand generation** (a D33–34 interview point). Demand gen focuses on nurturing and creative campaigns: content, events, ads, brand. GTM engineering focuses on data, list building, sending infrastructure and automated multichannel sequences that hand off to sales. Same goal (pipeline), different toolkit: one builds the audience's interest, the other builds the machine that finds and reaches the right people at the right moment.

**Campaign planning, the order:** pick the segment → build the lead list → warm up the infrastructure (which takes the longest, so start it first in real life).

**Be able to explain:** how warm-up works and why it never stops; the 3-week schedule; health score and what you do at 80% and 90%; the complaint and bounce thresholds; OAuth vs IMAP/SMTP; what a CTD is for; what a behavioural subsequence is.

## A6. D35–D36: Cold-email frameworks (2 Oct)

**The worked example.** Yogesh reviewed a classmate's live Instantly campaign aimed at US biotech companies. Study the *shape*, because Part B copies it for Saffron:
- **Segment:** US biotech and life-science companies, 51–1,000 employees.
- **Prioritisation:** lean finance teams, or companies hiring for finance roles (a signal).
- **Tech-stack filter:** NetSuite or QuickBooks users.
- **A signal that can't be used:** "uses Excel", because there's no public data source for it. Lesson: a signal is only useful if you can detect it at scale.
- Example signals for that market: finance hires, a new CFO, press and funding news.

**The sequence structure:**
- **6 emails**, with follow-ups **2–5 days apart**.
- **Email 1:** the signal-led opener plus the offer.
- **Emails 2–5:** a different proof point or angle each time, so every follow-up adds something rather than "just bumping this".
- **Email 6: the "options" close.** Give an easy way to reply: "Is it the wrong timing, the wrong budget, or not relevant?" A one-word answer is easy to send, and a "not relevant" is useful data.

**A/B testing.** Two variants per email, testing one idea at a time. The class example: an *industry-pain* angle against an *integration* angle. Instantly calls this A/Z testing (up to 26 variants per step).
- **Research says** (sample size): with small lists A/B results are anecdotes, not evidence. Telling a 3% reply rate apart from 6% needs about **750 sends per variant**; telling 3% from 9% needs about 240 (standard two-proportion test, 95% confidence, 80% power). Saffron's 40 leads give 20 per variant. So present your variants as **message exploration** and judge them on replies across several micro-campaigns over time. Never judge on opens, and don't let Instantly's "auto optimize" pick a winner by open rate.
- Put the B variant on **email 1**. Instantly's 2026 benchmark found 58% of replies come from the first email.

**Micro-campaigns beat AI personalisation.** Narrow segments (a few dozen people sharing one situation) with one tailored message outperform a big list where AI rewrites every email. You can see which message worked, and you can copy what works. **Research says:** Hunter's 2026 data agrees: campaigns of 21–50 recipients got 6.2% replies against 2.4% for 500+, and 69% of recipients dislike obviously AI-written emails.

**Non-responders** get a follow-up sequence based on their engagement once the first campaign ends (in practice, a later campaign or a subsequence).

**Tracking off.** Disable open and link tracking: corporate security software flags them (A7 explains why).

**Provider matching:** Google → Google, Outlook → Outlook.

**Copy rules** (Learning Guide D36, plus the research):
- **Structure:** an opener about *them* (tied to a signal) → the problem in their words → light proof (a number) → a **soft CTA**.
- **Length:** readable in under 10 seconds. **Research says:** Instantly's top performers write first emails under 80 words.
- **Subject lines:** short, specific, lowercase-ish, human. No hype, no "free", no "act now", no fake "RE:".
- **Soft CTA beats a meeting ask.** "Worth a look?" or "Is this a priority this quarter?" lowers the cost of replying. **Research says:** Gong's study of 304,174 emails found an interest CTA was more than twice as likely to book a meeting as asking for time.
- **What kills replies:** walls of text, hype, jargon, several asks in one email, spam-trigger words (which also hurt deliverability). Instantly has an "AI Spam Words Checker" in the sequence editor.
- **AI opener only** (D38 preview): one sentence, under 20 words, no greeting, built from real data, with a QC check.

**Homework from that class:** the hands-on part (set up the campaign, add B variants, upload leads, record a Loom of the build) was assigned to the classmate whose campaign was reviewed. You're doing it as your own portfolio build in Part B (it covers Learning Guide deliverables #7 and #8). Everyone was asked to research email tracking and open-rate best practice (A7) and keep improving their Clay tables, because Yogesh will review each person's table.

**Be able to explain:** the 6-email structure and why each follow-up adds something new; the options close; why micro-campaigns; why 40 leads can't produce a statistically valid A/B result; the soft-CTA logic.

## A7. Tracking and open rates (the D35–36 research homework)

**How tracking works.** *Open tracking* adds an invisible 1×1 image (a pixel) to the email; when the mail app loads it, the tool records an "open". *Link tracking* rewrites every link to go through a redirect that records the click.

**Why open rates are no longer reliable:**
- **Apple Mail Privacy Protection** loads remote content, including tracking pixels, privately and automatically, so Apple Mail users register "opens" whether or not they read anything.
- **Corporate security gateways** (for example Microsoft Defender Safe Links) scan and "detonate" links before delivery, which creates fake clicks and fetches images.
- **Research says:** the D21–22 benchmark of "90%+ email opens" is out of date. Instantly's 2026 average open rate is about 28%, and even that is inflated.

**Why tracking can hurt delivery:** the pixel makes the message HTML, and redirect links (especially through a shared tracking domain) look like phishing to strict filters. **Research says:** Hunter's 2026 data (31M emails) showed a 7.4% reply rate with open tracking off against 4.4% with it on; Snov.io (44M emails) found turning it off more than doubled replies. Both are correlations, but they point the same way. Instantly itself includes "send as text-only" and "disable open tracking" among its deliverability tools.

**Resolving the class contradiction** (D33 "set up a custom tracking domain" vs D35 "turn tracking off"): they don't really conflict. D33 taught how to track *safely if you track* (with a CTD). D35 taught that for cold email you *shouldn't track*. The 2026 best practice:
- Open tracking **off**, link tracking **off**.
- First email **text-only**, with **no links**.
- Measure **replies, positive replies and meetings**, plus **bounce rate** and the **health score** for deliverability, and run an **inbox placement test** before launch.
- Setting up a CTD is still cheap insurance (one CNAME record) in case a later email includes a link or the team later turns tracking on.

## A8. The Instantly training video, condensed

The cohort's bonus Instantly training (Yogesh with two students). It's the most hands-on source for the homework.

**Setup order (2–3 hours done properly):** connect mailboxes → set up the custom tracking domain → start warm-up → add SPF/DKIM/DMARC at the registrar. (DNS first is safer in practice, since warm-up from an unauthenticated domain wastes days.)

**Rules he gave:**
- Warm-up never stops.
- Below 80% health, pull the mailbox from campaigns and re-warm.
- Ramp both warm-up and campaign volume; never start at the target limit.
- Count working days only.
- About 3 mailboxes per domain.
- Always configure SPF/DKIM/DMARC; always include an unsubscribe or opt-out.
- Tag warm-up by mailbox, never by client.

**Campaign planning formula, worked live:** 22 working days × 10 mailboxes × 50 a day = 11,000 emails a month ÷ 6 emails per lead ≈ **1,833 leads a month**. At Instantly's recommended 30 a day it's 6,600 emails ≈ 1,100 leads.

**Reply-to.** You can send from one person's mailbox and route replies to another (send from the founder, replies go to the head of sales). **Research says:** in current Instantly this is a **per-mailbox** setting (Email Accounts → account → Settings → Reply-to), not a campaign setting, and the reply-to address must itself be connected to Instantly.

**Unibox.** Every reply from every mailbox in one inbox, labelled by AI (interested, meeting booked, out of office, not interested…). Analytics can be shared with a client by download or view-only access. **Research says:** replying from Unibox needs Hyper Growth.

**Campaign options he walked through:** stop on reply, open tracking, daily limit (mailboxes × per-mailbox limit, e.g. 5 × 50 = 250 a day), stop on auto-reply / out-of-office, unsubscribe, "risky" (invalid) emails off, CC/BCC.

**Team access:** Settings → Workspace and Members → invite as Viewer, so a client can check status without a meeting.

**Why agencies run volume and you run micro-campaigns.** Yogesh's agency numbers: about 1% reply rate at high volume, with about 10% of those replies positive, so agencies give each client around 10 domains × 5 mailboxes and send thousands a day. With 40 leads you can't play the volume game, so relevance (signal-led micro-campaigns) is the only lever you have.

**Other things from the video:**
- **Warm-up "Weekdays only" mode** (paid plans) keeps warm-up traffic to working days, matching how a real person emails.
- **Sending window:** Yogesh sends 10:30–17:30.
- **Technographic and intent tools:** BuiltWith (scans a site's front end for its tech stack: broad, surface-level), HG Insights (spend and product ownership; flags companies evaluating new tools), and 6sense/Slintel-style tools that combine both with team data. These are signal sources for account-based work (the names were unclear in the recording).
- **Sales Navigator export tools** (Wiza- and Evaboot-style extensions) only pull data out of Sales Nav; they aren't lead databases themselves.
- **Document publicly, but never tag the real client companies** you used as practice examples.

**Two stories to remember:**
- A GTM engineer on a $12,000/month client retainer got the infrastructure wrong for three months; deliverability collapsed, the client left, and he was let go.
- Yogesh's own first agency: four clients, Instantly set up wrong, all four complained, and he refunded them. That's why he teaches infrastructure so hard.

**Career point:** the mechanics (DNS, ports, IMAP/SMTP, warm-up) transfer across tools. A job ad that asks for Smartlead isn't a blocker if you know Instantly.

## A9. Compliance: what makes a cold email legal

Not covered much in class, but you need it before anything is ever sent, and interviewers increasingly ask.

- **US (CAN-SPAM)**, which covers Saffron's US prospects: cold B2B email is legal without prior consent, but every message needs accurate sender headers, a non-misleading subject, a **valid physical postal address**, and a clear way to opt out, honoured within 10 business days. A **reply-based opt-out is allowed**, so Yogesh's "reply 'no'" P.S. works, as long as the postal address is also there. The sender must be accurately identified, so **you can't send as Saffron without Saffron's permission**. That's another reason this homework stops at "configure, don't launch".
- **UK (PECR + UK GDPR):** emailing employees of companies is allowed without consent if you identify yourself and offer an opt-out, with "legitimate interests" as the lawful basis.
- **EU (GDPR):** you must tell the person where you got their data, at the latest in the first message (a short privacy line or link). **Germany** is stricter: cold email advertising needs prior consent even B2B (UWG §7), so don't cold-email German prospects.
- **Canada (CASL):** needs express or implied consent. An address found through an enrichment waterfall doesn't count as implied consent, so don't cold-email Canadian prospects.
- **India (DPDP Act):** it governs how *you* handle the data in India, but its core duties only start in May 2027, and work done under contract for a foreign client is largely exempt. The working rule already in this repo applies: keep prospect data private and minimal.

## A10. Where class and current sources disagree (and what to do)

- **Daily cold emails per mailbox:** class 50. Instantly 30 (+10 warm-up). **Use 30** for planning, mention 50 as the ceiling.
- **Health score line:** class 80%. Instantly 90%. **Send above 90%, stop below 80%.**
- **Campaign slow ramp:** class 20→30→40→50 weekly. Instantly's toggle is +2 a day. Both are ramps; know which is which.
- **Warm-up length:** class 3 weeks. Instantly at least 2 weeks with a 90% score; Learning Guide and Instantly blog 4–6 weeks for new domains. **Plan 3–4 weeks.**
- **Tracking:** D33 vs D35 contradiction resolved in A7: **off** for cold email; CTD as insurance.
- **TLDs:** Learning Guide .co/.io; Instantly .com. **Prefer .com.**
- **"Gmail rejects mail without DMARC":** only for bulk senders, and Google's rules don't cover mail sent to Workspace accounts. **Set up DMARC anyway.**
- **"2% bounce is a provider hard limit":** it's industry practice, not a published provider rule. Instantly pauses at ~5%. **Keep under 2%.**
- **Email opens "90%+" (D21–22):** about 28% on average in 2026, and inflated. **Ignore opens.**
- **Email Bison "unlimited emails":** 500,000 a month for $599. **Instantly "single company only":** now also does agency features.
- **Reply-to:** per mailbox in current Instantly, not per campaign.
- **Subsequences:** need Hyper Growth and only appear after launch, so they're out of scope for a no-launch homework.
- **A/B testing:** fine to build, but 40 leads can't prove a winner.
- **Footer unsubscribe vs P.S.:** use both mechanisms: the reply-based P.S. in the body plus Instantly's List-Unsubscribe header, plus the postal address.
- **"Avoid software companies":** unresolved for Saffron; ask Yogesh.

## A11. Glossary

- **A/Z testing:** Instantly's name for A/B testing with up to 26 variants per email step.
- **Alignment:** DMARC's check that the domain that passed SPF or DKIM matches the visible From domain.
- **Bounce rate:** share of emails that couldn't be delivered (bad address). Keep under 2%.
- **Bulk sender:** in Gmail's and Microsoft's rules, a domain sending 5,000+ messages a day to their consumer addresses.
- **Catch-all:** a domain that accepts mail to any address, so a verifier can't confirm the person exists. The class rule: send only to Valid and "Valid catch-all".
- **Complaint (spam) rate:** share of recipients who click "report spam". Under 0.3%, aim under 0.1%.
- **CTD (custom tracking domain):** your own subdomain for tracking pixels and links, set with a CNAME record.
- **DFY / pre-warmed / AirMail:** mailboxes Instantly sets up and owns for you.
- **DKIM:** cryptographic signature on each message, verified with a public key in DNS.
- **DMARC:** DNS policy for failing mail plus reporting (RFC 9989 since May 2026).
- **ESP / provider matching:** sending Google → Google and Outlook → Outlook.
- **Health score:** Instantly's per-mailbox inbox rate for warm-up emails over 7 days.
- **IMAP / SMTP:** the protocols for reading (IMAP, port 993) and sending (SMTP, 587 or 465) mail.
- **Inbox placement test:** a test send to seed mailboxes that reports inbox vs spam per provider.
- **List-Unsubscribe / one-click (RFC 8058):** email headers that make the mail app show an unsubscribe button.
- **Lookalike / secondary domain:** a domain bought only for outbound so the main domain is protected.
- **Micro-campaign:** a small campaign for one narrow segment with one message.
- **MX:** DNS record naming the servers that receive mail for a domain.
- **OAuth:** login by approval (no stored password), used for Google and Microsoft mailboxes.
- **Options close:** a final email that offers easy one-word answers (timing, budget, not relevant).
- **Slow ramp:** gradually raising a mailbox's daily campaign volume.
- **Soft CTA:** a low-commitment question ("worth a look?") instead of a meeting ask.
- **SPF:** DNS allow-list of servers that may send for a domain.
- **Spintax:** `{{RANDOM | Hi | Hello}}` syntax that varies wording per send.
- **Subsequence:** a branch triggered by a lead's reply or status.
- **Unibox:** Instantly's combined inbox for all replies.
- **Upsert:** update if the record exists, insert if not.
- **Warm-up:** automated exchange of engaged emails that builds a new mailbox's reputation.

---

# Part B: the homework

## B0. What you're building and what you hand in

**The assignment, from class:**
- **D33–34:** plan 10 distinct campaigns for Saffron.
- **D35–36:** set up the campaign in Instantly, add B variants, upload the leads, record a Loom of the build. (In class this was assigned to the classmate whose campaign was reviewed; you're doing it as your portfolio build.)
- **D31–34 prerequisites:** a separate sending domain, SPF/DKIM/DMARC, warm-up, an opt-out P.S., plain text, tracking off, Google → Google.

**What you hand in:**
- The 10-campaign plan (B1; this doc is your write-up, paste it into your portfolio).
- The deliverability plan for Saffron (B2): it's on paper, because no sending domain has been bought.
- Three micro-campaigns built in Instantly with the full 6-email sequence and B variants, leads uploaded, **saved as drafts, not launched** (B3–B5).
- Screenshots in Drive → Build Evidence, and a 5-minute Loom (B6).

**Time:** about 4–5 hours: Clay prep 1 h, Instantly build 2 h, Loom and screenshots 1 h.

**Ethics, as with HeyReach:** Saffron hasn't hired you; this is a portfolio exercise. Nothing is sent. A real send would need Saffron's approval, a domain Saffron owns, and their name and postal address in the email.

**How this fits the LinkedIn homework.** HeyReach (D37–38) targets **CHROs** on LinkedIn. This Instantly build targets the **engineering leaders and talent champions** already in your people table. In a real launch the two channels combine: a LinkedIn profile view and connection request first (Yogesh's "under 2,000 leads → LinkedIn first"), then email 2–3 days later, so the prospect sees you in two places (the "wall of sound").

## B1. The 10-campaign plan (D33–34 homework)

**The logic.** A campaign = one **segment** (company type and size, from Strategy Doc v2) × one **persona** (decision maker or champion) × one **signal** (the "why now"). Keep each campaign narrow enough that one message fits everyone in it. That's the micro-campaign rule from D35–36.

| # | Campaign | Segment | Persona | Signal / trigger | Angle |
|---|---|---|---|---|---|
| 1 | AI-in-JDs · leaders | S1 + S2 | CTO / VP Eng / Head of Eng | Job ads mention Cursor, Claude Code, Codex or Copilot | "You hire for AI fluency; your interviews can't see it" |
| 2 | Hiring surge · leaders | S1 + S2 | CTO / VP Eng / Head of Eng | 10+ open engineering roles | Interview hours × number of hires |
| 3 | Growing team · leaders | S1 + S2 | CTO / VP Eng / Head of Eng | 5–9 open engineering roles | Take back engineers' interview time before the team grows |
| 4 | Hiring surge · talent champions | S2 | Head of Talent / TA lead | 10+ open engineering roles | Time-to-hire and consistent scoring across many loops |
| 5 | Growing team · eng managers | S1 + S2 | Engineering Manager / Director | 5–9 open roles | "You're the one running the loops" |
| 6 | New leader, first 90 days | S1 + S2 | New CTO / VP Eng / Head of TA (in role ≤180 days) | Leadership change | New leaders redesign the interview loop early |
| 7 | Just funded | S1 | Founder / CTO | Seed–Series B in the last 180 days | The hiring plan that follows a raise (tiebreaker signal, so pair it with hiring) |
| 8 | Regulated · leaders | S3 FinTech / HealthTech | CTO / VP Eng | Regulated industry + hiring | Auditable, consistent evaluation; prove a take-home wasn't AI-written |
| 9 | Regulated · talent | S3 | Head of TA / Technical Recruiting | Regulated industry | Fairness and an audit trail for every technical decision |
| 10 | People leaders | S1–S3 | CHRO / CPO / VP People | Hiring surge or AI-in-JDs | Cost, fairness, candidate experience (the HeyReach campaign; email is its second channel) |

**Which ones your current data supports.** Your people table has **40 contacts with a verified email at 17 companies** (22 decision makers and 18 champions; 10 of the 50 rows have no verified email). Split by signal they fall cleanly into three micro-campaigns, and those are what you build in Instantly:

- **Campaign 1, AI-in-JDs:** 10 contacts at 4 companies (HeyGen, ITILITE, Kalshi, ButterflyMX).
- **Campaign 2, Hiring surge (10+ roles):** 14 contacts at 6 companies (Fireworks AI, Gigs, LawnStarter, Pave, SandboxAQ, Topsort).
- **Campaign 3, Growing team (5–9 roles):** 16 contacts at 7 companies (AssemblyAI, AuditBoard, Circle, DataVisor, Deepgram, Gamma, Level AI).

Each campaign mixes engineering leaders with a few talent leaders (6 of the 40 are Heads of Talent/TA), which is why the campaigns are named "Eng + talent"; the copy is about interview load and assessment quality, which both care about. Each contact sits in exactly one campaign (AI-in-JDs wins over job count, because it's the sharper signal). Campaigns 4–9 need data you haven't pulled yet (leader start dates, funding dates, more champions) or a narrower cut of what you have: the Industry column exists in `saffron_50_accounts` (the HeyReach Segment formula uses it), but only one or two of these 17 companies are clearly regulated, too few for their own email campaign, so here they stay in their hiring-signal campaign. Campaign 10 is the HeyReach work. In the write-up, say that for each one.

**Why not one campaign of 40?** Because then you can't tell which message worked. Three campaigns with three different "why now" openers give you a comparison even at this size.

## B2. Saffron's deliverability plan (on paper)

Write this up as part of the homework (it's also the Learning Guide's D35 "deliverability runbook", portfolio deliverable #7). Nothing here needs buying for the homework.

**Domains.** 2 lookalike .com domains (for example in the style `trysaffronhq.com` / `getsaffron.com`, availability not checked, and Saffron has to approve them). Each one forwards to trysaffron.ai. Never trysaffron.ai itself.

**Mailboxes.** 2 Google Workspace mailboxes per domain, named like real people (e.g. firstname@ and firstname.lastname@), 4 in total. Google only is enough at this volume; add a Microsoft 365 mailbox later for Outlook → Outlook matching.

**DNS for each domain** (Google Workspace, placeholder domain):

```
MX     @                  smtp.google.com   (priority 1)
TXT    @                  v=spf1 include:_spf.google.com ~all
TXT    google._domainkey  v=DKIM1; k=rsa; p=<key from Admin console>
TXT    _dmarc             v=DMARC1; p=none; rua=mailto:dmarc@<domain>
CNAME  inst               prox.itrackly.com   (optional custom tracking domain)
```

After 2–4 weeks of clean DMARC reports, change the policy to `p=quarantine`. Check everything with mail-tester.com and MXToolbox.

**Warm-up (21 days, per mailbox).** Instantly defaults (+1 a day, cap 10, reply rate 30%) or Yogesh's staged version:
- Days 1–7: start at 1 and add 1 a day, toward a cap of 10.
- Days 8–14: add 2 a day, toward a cap of 20.
- Days 15–21: add 3 a day, toward a cap of 30; then drop back to a permanent ~10 a day.
- Start campaigns only when the health score is **above 90%**. Campaign Slow Ramp on.

**Capacity maths for Saffron.** 40 leads × 6 emails = **240 emails**. One mailbox at 30 a day sends that in 8 working days; 4 mailboxes give plenty of headroom and room to grow to about 2,600 emails a month (4 × 30 × 22).

**Monthly cost (if bought):** 2 domains ≈ $20–30 a year; 4 Google Workspace mailboxes ≈ $28–34 a month (US pricing, as Saffron is a US company); Instantly Growth $47 a month. Total **about $75–81 a month**, plus the domains. Weekly inbox placement tests need Instantly's separate Inbox Placement plan ($47 a month; every account gets 2 free one-time tests). Instantly's DFY mailboxes would be cheaper ($15 per domain a year + $5 per mailbox a month) but Instantly would own the domains.

**Monitoring checklist (when live):**
- Daily: health score per mailbox. Above 90% → fine; 80–90% → lower that mailbox's limit; below 80% → pull it and re-warm.
- Weekly: bounce rate under 2% (find out which source produced the bad emails); complaints under 0.1%; an inbox placement test.
- When a number goes red: pause the campaign, check DNS with MXToolbox, check the list's verification results, and re-warm before resuming.

**Opt-out and legal (in every email):** the P.S. opt-out line, Instantly's "Insert unsubscribe link header" on, and Saffron's postal address in the signature.

## B3. Prepare the leads in Clay (≈1 hour, a few credits)

Work in the people table of **"Saffron | Qualified Pipeline"** (deepshikhagtme account). House rules as usual: auto-run off, test on 10 rows, cheapest model first, hide columns rather than delete.

**Step 1 · Tier column (free formula; fixes the D29–30 gap).** It isn't used to split these three campaigns. It goes into Instantly as a custom variable so you can show persona routing in the Loom, and it's the column campaigns 4–9 will route on later (S1 → founder/CTO, S2 → VP Eng + talent champion). Paste into Clay's formula helper:

**Formula helper: Tier**

---

If Employee Count is less than 200, return S1. If it is 200 to 1,000, return S2. Otherwise return Out of scope.

---

**Step 2 · Campaign column (free formula).**

**Formula helper: Campaign**

---

If Tools is not empty, return AI-in-JDs. Otherwise, if Jobcount is 10 or more, return Hiring surge. Otherwise return Growing team.

---

**Step 3 · Opener column (Use AI, Helium).** Run condition: Work Email is not empty. The prompt changes what it says by campaign, because email 1 of the AI-in-JDs campaign follows on from the AI tools, while the other two follow on from the number of open roles ("At that pace…").

**Use AI prompt: Opener**

---

Write one opening sentence for a cold email to {{First Name}}, {{Job Title}} at {{Company Name}}.
Use only these facts: {{Qualification Reason}}. AI coding tools in their job ads: {{Tools}}. Campaign: {{Campaign}}.
If Campaign is AI-in-JDs, name the AI coding tools their engineering job ads ask for. Otherwise, state the number of open engineering roles.
Include {{Company Name}} exactly as written.
Rules: under 20 words; no greeting; no flattery; no exclamation marks; do not mention Saffron; do not invent anything that isn't in the facts.
Return JSON: {"line": string}

---

In Clay, insert each {{column}} with the / menu rather than typing it, so it links to the real column. Examples of good outputs: "Saw HeyGen's engineering roles ask for Cursor, Claude Code and Codex experience." / "Noticed Topsort has 13 engineering roles open right now." Test on 10 rows, read every line, then run the rest. Only escalate to Neon for rows Helium gets wrong.

**Step 4 · Pull the line out of the JSON.** Click a result cell → on the `line` field choose **Add as column** and name the new column **Opener**. This is what gets exported. If you export the AI column itself, Instantly's Personalization field receives raw JSON.

**Step 5 · Opener QC column (free formula).** Then hand-check 10 lines against the source columns (Learning Guide D38: never send AI copy unreviewed), and fix any CHECK rows by hand.

**Formula helper: Opener QC**

---

Return CHECK if Opener is empty, has more than 22 words, contains an exclamation mark, or does not contain Company Name. Otherwise return OK.

---

**Step 6 · Export three CSVs.** Clay can't split one export, so filter the view three times (Work Email is not empty AND Opener QC = OK AND Campaign = each value) and export each one: **Tools → Export → Download CSV**. Export **only** these columns, because Instantly rejects headers longer than 20 characters and your raw export starts with `Rows from: saffron_50_accounts`:
- Work Email, First Name, Full Name, Company Name, Job Title, Linked In Url, Clean Domain, Opener, Campaign, Tier, Jobcount.

Name the files `saffron_c1_ai_jds.csv` (10 rows), `saffron_c2_hiring_surge.csv` (14) and `saffron_c3_growing_team.csv` (16). Those counts are your check.

## B4. Build in Instantly (≈2 hours)

**Account and plan.** Sign up at instantly.ai with **deepshikhagtme@gmail.com**. The free trial is 14 days, no card, with 2 mailboxes, 250 leads and 1,000 emails.
- **Catch 1:** Instantly's plan comparison table lists **A/Z testing as "No" on the trial**, so expect not to be able to add B variants on it. (If "Add variant" does work on your trial, use it, and tell the cohort.) Two options:
  - **(a) Recommended:** build everything on the trial first (Steps 1–6 below), then upgrade to **Growth ($47, one month)** only to add the variants and record the Loom. Cancel afterwards if the course doesn't need it.
  - **(b) Free:** build on the trial without variants, write the B variants into the Loom script and this doc, and ask Yogesh whether that's acceptable.
- **Catch 2:** when the trial ends, an account that hasn't been upgraded is **deleted**. Take every screenshot and record the Loom within 14 days.
- Ask Yogesh which plan the cohort uses (the training video used the paid "Growth" plan).

Instantly's screens change; if something isn't where this says, look for the closest match and screenshot it.

**Step 1 · Create Campaign 1.** Campaigns → Add new → name it `Saffron · Eng + talent · AI-in-JDs · v1` → Continue.

**Step 2 · Upload the leads.** Leads tab → CSV → upload `saffron_c1_ai_jds.csv`. Map:
- Work Email → **Email**
- First Name → **First name**
- Company Name → **Company name**
- Job Title → **Job title**
- Linked In Url → **LinkedIn**
- Clean Domain → **Website**
- Opener → **Personalization**
- Full Name, Tier, Campaign, Jobcount → **Custom variable**
- anything else → **Do not import**

Tick "Check for duplicates across all campaigns". Don't tick "Verify leads" (it costs credits, and your list is already verified in Clay). Click **Upload all**. 📸 the mapping screen and the lead count (10).

**Step 3 · Write the sequence.** Sequences tab. Paste email 1 (B5) into step 1, then **Add step** for each follow-up with these waits ("Send next message in…"):
- Step 1: email 1.
- Step 2: wait **3 days**, email 2.
- Step 3: wait **3 days**, email 3.
- Step 4: wait **4 days**, email 4.
- Step 5: wait **4 days**, email 5.
- Step 6: wait **5 days**, email 6.

That's about 19 days end to end. Leave the **subject blank on steps 2–6** so they thread under email 1 as replies. Insert variables with the **Variables** button rather than typing them, so the syntax is right. **Sequences don't auto-save: click Save after every step.** Run the **Spam Words Checker** on each email. 📸 the full sequence.

**Step 4 · Add the B variants.** On step 1, click **Add variant** and paste email 1 B. Make sure both variants are toggled on (blue). You can add a B on step 6 too if you want a second test (the options close vs a "should I close your file?" version). 📸 the variants.

**Step 5 · Schedule.** Schedule tab: Monday–Friday, 10:30–17:30 (Yogesh's sending window) in the **prospect's** time zone (ET for most of this list; Instantly recommends a separate campaign per time zone if you have both coasts). Set the **start date a month ahead** as a second safety net against an accidental launch. Save. 📸

**Step 6 · Options.** Options tab, with these settings and the reason for each (say the reasons in the Loom):
- **Accounts to use:** leave empty (no mailbox yet). In a real run, the 4 warmed Google mailboxes.
- **Stop sending emails on reply:** ON.
- **Open tracking:** OFF. **Link tracking:** OFF (A7).
- **Delivery optimization:** "Send emails as text-only (no HTML)" (the other choice is "Send first email as text-only").
- **Daily limit:** 120 (4 mailboxes × 30). It only matters once mailboxes are attached.
- **Advanced → Stop campaign for company on reply:** ON (your list has about 3 people per company; once one replies, stop the others).
- **Stop sending emails on auto-reply:** OFF, and in Settings → Preferences turn on "Automatically tag interest status in replies". Together these switch on **AI Smart Pause**: an out-of-office reply pauses that lead until the return date it states, then the sequence resumes. With the toggle ON, an out-of-office would end the sequence for that person.
- **Provider matching:** ON.
- **Insert unsubscribe link header:** ON.
- **Allow risky emails:** OFF.
- **Auto optimize A/Z testing:** OFF (40 leads can't produce a valid winner, and opens are unreliable).
- Save. 📸 each Options section.

**Step 7 · Preview.** Use **Preview** on 2–3 leads to check that the variables and the opener fill in correctly. ("Send test email" needs a connected mailbox, so skip it.) 📸 one preview.

**Step 8 · Do NOT click Launch.** The campaign should show as **Draft**. If Instantly won't save a draft without a sending account, write that down and screenshot it. It's a useful finding for the Loom and a question for Yogesh.

**Step 9 · Campaigns 2 and 3.** Repeat Steps 1–8 with `Saffron · Eng + talent · Hiring surge · v1` (14 leads) and `Saffron · Eng + talent · Growing team · v1` (16 leads). Emails 2–6 are the same; only email 1 (A and B) changes (B5). If you see a Duplicate option in the campaign's menu, use it and swap step 1 and the leads.

**Step 10 · Evidence.** Put all screenshots in Drive → Build Evidence → `instantly/`, named by step.

**Optional, if you want the infrastructure on camera:** show the Email Accounts page and the warm-up settings screen (empty, with the default values) and explain the 21-day plan from B2. Don't buy a domain for the homework.

## B5. The emails

The rules they follow:
- **Variables:** `{{firstName}}`, `{{companyName}}`, plus `{{personalization}}` (the Clay opener) in email 1 only.
- **Length:** email 1 under 80 words. **Soft CTA**, no meeting ask, plain text, no links.
- **Opt-out P.S.:** on every email.
- **Each follow-up adds one new proof point:** interviewer hours, AI-written code, session replay, own codebase plus the free first assessment, then the options close.
- **The signature** is the sender's name, "Saffron", and Saffron's postal address. The address is a placeholder until Saffron gives you one.

### Campaign 1 · AI-in-JDs · Email 1

**Variant A (pain angle)**
Subject line: ai fluency in interviews

---

Hi {{firstName}},

{{personalization}}

Many technical interviews still ban AI, so they can't show how a candidate actually works with it. Saffron has candidates build a real feature on your own codebase with Claude Code, then shows which lines they wrote and which came from AI.

Worth a look before your next engineering hire?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

**Variant B (outcome angle)**
Subject line: your jds vs your interviews

---

Hi {{firstName}},

{{personalization}}

What if your first technical round took none of your engineers' time, and still tested how candidates use AI? With Saffron, candidates build on your own codebase, 10+ AI reviewers score the work against your rubric, and you get a replay and report the same day.

Is that worth exploring for {{companyName}}?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

### Campaign 2 · Hiring surge (10+ roles) · Email 1

**Variant A (pain angle)**
Subject line: interview load at {{companyName}}

---

Hi {{firstName}},

{{personalization}}

At that pace, technical interviews start eating your senior engineers' weeks. Saffron replaces the take-home and first technical round with a short build on your own codebase, scored the same way for every candidate, with no interviewer time.

Is interview load a problem for you this quarter?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

**Variant B (outcome angle)**
Subject line: same-day technical signal

---

Hi {{firstName}},

{{personalization}}

Teams hiring at that pace use Saffron to get a scored technical report on every candidate within hours: a real feature built on their own codebase, reviewed by AI against their rubric, with a full replay of how the candidate worked.

Worth a look for {{companyName}}'s next few hires?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

### Campaign 3 · Growing team (5–9 roles) · Email 1

**Variant A (pain angle)**
Subject line: engineers interviewing engineers

---

Hi {{firstName}},

{{personalization}}

As the team grows, the same few engineers run every technical loop. Saffron gives that time back: candidates build a real feature on your codebase and AI reviewers score it, so nobody sits in the first round.

Is that a problem you're feeling yet?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

**Variant B (outcome angle)**
Subject line: a better first technical round

---

Hi {{firstName}},

{{personalization}}

Saffron replaces the take-home with a short build on your own codebase. You see how each candidate works with AI tools, line by line, with results the same day and zero interviewer hours.

Would it help {{companyName}} to try it on one candidate?

Deepshikha
Saffron · [postal address]

P.S. If this isn't relevant, just reply "no" and I won't follow up.

---

### Emails 2–6 (the same for all three campaigns; subject left blank so they thread)

**Email 2 · proof: interviewer hours (wait 3 days)**

---

Hi {{firstName}},

One number that stuck with me: Ashby's hiring data puts the average technical hire at about 23 hours of interviewing. Multiply that by every engineering role {{companyName}} is filling.

Saffron takes the first technical round off your engineers' calendars entirely. Would a sample report help you judge it?

Deepshikha
Saffron · [postal address]

P.S. Not relevant? Reply "no" and I'll stop.

---

**Email 3 · proof: AI-written code (wait 3 days)**

---

Hi {{firstName}},

In HackerRank's 2025 survey, 76% of developers said AI makes it easier to game coding assessments. A take-home alone can't show which parts were AI-written.

Saffron attributes every line a candidate submits as written by them, generated by AI, or AI-generated and then edited, so you see the judgment behind the code, not just the result.

Curious how you're handling this today?

Deepshikha
Saffron · [postal address]

P.S. Not relevant? Reply "no" and I'll stop.

---

**Email 4 · proof: the replay (wait 4 days)**

---

Hi {{firstName}},

The part I'd look at first: a full replay of the session. Every prompt, edit and decision the candidate made, in order, so you can see how they think when the AI gets it wrong.

Would that be useful for {{companyName}}'s engineering interviews?

Deepshikha
Saffron · [postal address]

P.S. Not relevant? Reply "no" and I'll stop.

---

**Email 5 · offer: try it free (wait 4 days)**

---

Hi {{firstName}},

The simplest way to judge Saffron is to run one real candidate through it. The first assessment is free, it runs on your own codebase, and you get the scored report and replay the same day.

Want me to set one up for your next engineering candidate?

Deepshikha
Saffron · [postal address]

P.S. Not relevant? Reply "no" and I'll stop.

---

**Email 6 · the options close (wait 5 days)**

---

Hi {{firstName}},

I'll close the loop here. If it's not a fit, a one-word reply helps me a lot:

1, wrong timing
2, no budget
3, not relevant for {{companyName}}

Thanks either way.

Deepshikha
Saffron · [postal address]

P.S. Or just reply "no" and you won't hear from me again.

---

**Two notes on the copy:**
- Email 4 is written in your own voice. If Saffron confirms that hiring managers use the replay most, you could change its opening to "The part hiring managers tell us they use most", but only with that confirmation.
- The numbers in emails 2 and 3 come from Ashby's talent-trends data (23.3 interview hours per technical hire, Jan 2021–Mar 2026) and HackerRank's 2025 Developer Skills Report (76%). Keep the sources in your notes in case a prospect asks.

## B6. Loom outline (about 5 minutes)

- **0:00–0:30 · Context.** Saffron, the buyer (engineering leaders at 50–1,000-person US tech companies), why email is the second channel after LinkedIn for a 40-lead list.
- **0:30–1:15 · The 10-campaign plan.** Segment × persona × signal; the three you built and why the data supports only those today.
- **1:15–2:00 · Infrastructure (on paper).** Lookalike domains, 4 mailboxes, SPF/DKIM/DMARC, 21-day warm-up to a 90% health score, capacity maths (240 emails, 30 a day). Why not DFY.
- **2:00–3:30 · The Instantly build.** Lead mapping (Opener → Personalization), the 6-step sequence and its waits, the B variants and what each one tests, the schedule.
- **3:30–4:30 · Options and why.** Tracking off and text-only (Apple MPP, security scanners, Hunter's data), stop on reply and stop for the company, AI Smart Pause for out-of-office replies, unsubscribe header, provider matching, auto-optimise off (sample size).
- **4:30–5:00 · What you'd measure and what's next.** Reply and positive-reply rates per campaign, bounce under 2%, health above 90%; after 2–4 weeks keep the winning opener, rewrite the weakest; subsequences on Hyper Growth after launch.

## B7. Checklist

- [ ] Clay: Tier, Campaign, Opener (Helium) and Opener QC columns; 10-row check; three CSVs (10 / 14 / 16 rows).
- [ ] 10-campaign plan written up (B1 table plus a line on what data campaigns 4–9 still need).
- [ ] Deliverability plan written up (B2: domains, DNS, warm-up, capacity, cost, monitoring).
- [ ] Instantly: 3 campaigns, leads mapped, 6 steps each, B variant on step 1, schedule, options, previewed, **all in Draft**.
- [ ] Screenshots in Build Evidence → instantly/.
- [ ] Loom recorded (within the 14-day trial window).
- [ ] Build log Field notes updated with anything that surprised you in Instantly.

## B8. Questions for Yogesh

- Which Instantly plan does the cohort use? Does the trial-without-variants route (B4 option b) count?
- Planning at 50 emails a day per mailbox vs Instantly's own 30 a day: which should a runbook use?
- Health score: pull a mailbox at 80% (class) or treat 90% as the line (Instantly)?
- Tracking: confirm "off for cold email, CTD only if tracking". (The D33 vs D35 point.)
- "Avoid software companies": how does that apply when Saffron's buyers are engineering teams?
- For a 40-lead list, should email wait until the LinkedIn sequence has run, or go in parallel?
- One contact per company first (Hunter's data favours it) or all three at once with "stop for company on reply"?

## B9. How you'd measure it (once live, later)

- **Primary:** reply rate and **positive** reply rate per campaign and per variant. Benchmarks: 3.4% average reply rate, 5.5%+ top quartile (Instantly 2026); Yogesh's ~3%.
- **Health:** bounce rate under 2%, complaints under 0.1%, mailbox health above 90%, inbox placement test before launch and weekly.
- **Not used:** open rate (unreliable, and tracking is off anyway).
- **Iteration:** after 2–4 weeks keep the best-performing opener angle, rewrite the weakest, and roll the winner into campaigns 4–9 as you add their data. Expect real learning over 2–3 months, as with LinkedIn.

---

# Sources

**Class material (repo):** `notes/D29-D36_summary-notes.md`; `notes/X3_instantly-training.md` and `source/X3_instantly-training.md` (training transcript); `source/REF_learning-guide.md` (D29–D40); `strategy/strategy-doc-saffron-v2.md`; `clay/build-sheet.md`; `data/saffron_people_export.csv`; `homework/D37-D38_heyreach-chro-campaign.md`. Research files: `research/instantly/` (brief, Claude findings, Gemini findings, cross-review, verification).

**Instantly (help center and site, Oct 2026):**
- Pricing: https://instantly.ai/pricing
- Free trial: https://help.instantly.ai/en/articles/13941298-instantly-free-trial
- Plan comparison (A/Z, subsequences by plan): https://help.instantly.ai/en/articles/7920548-email-outreach-plans-comparison
- Campaign options: https://help.instantly.ai/en/articles/6222396-campaign-options
- Pre-launch checklist: https://help.instantly.ai/en/articles/6222212-pre-launch-campaign-checklist
- CSV import: https://help.instantly.ai/en/articles/6254215-how-to-import-leads-via-csv
- A/Z testing: https://help.instantly.ai/en/articles/6661549-a-z-testing-how-to-create-email-variants
- Subsequences: https://help.instantly.ai/en/articles/7251329-subsequences
- Warm-up settings: https://help.instantly.ai/en/articles/7988514-warmup-settings
- Health score: https://help.instantly.ai/en/articles/13939939-warmup-health-score
- Campaign Slow Ramp: https://help.instantly.ai/en/articles/10056946-campaign-slow-ramp-system
- Custom tracking domain: https://help.instantly.ai/en/articles/6984188-custom-tracking-domain-ctd
- Text-only delivery: https://help.instantly.ai/en/articles/6531595-delivery-optimization-tool-send-emails-as-text-only
- Done-for-you Google setup: https://help.instantly.ai/en/articles/9361043-done-for-you-google-email-setup
- 2026 benchmark report: https://instantly.ai/cold-email-benchmark-report-2026

**Email providers and standards:**
- Google sender requirements and FAQ: https://support.google.com/a/answer/81126 and https://support.google.com/a/answer/14229414
- Google Workspace SPF / DKIM / DMARC setup: https://knowledge.workspace.google.com/admin/security/set-up-spf (and the set-up-dkim and set-up-dmarc pages)
- Yahoo sender best practices: https://senders.yahooinc.com/best-practices/
- Microsoft high-volume sender requirements (May 2025): https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%e2%80%99s-new-requirements-for-high%e2%80%90volume-senders/4399730
- DMARC, RFC 9989 (May 2026): https://www.rfc-editor.org/rfc/rfc9989.html
- One-click unsubscribe, RFC 8058: https://datatracker.ietf.org/doc/html/rfc8058

**Tracking, copy and buyer data:**
- Apple Mail Privacy Protection: https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios
- Microsoft Safe Links: https://learn.microsoft.com/en-us/defender-office-365/safe-links-about
- Hunter, State of Cold Email 2026: https://hunter.io/the-state-of-cold-email
- Gong, interest-CTA study: https://www.gong.io/blog/this-surprising-cold-email-cta-will-help-you-book-a-lot-more-meetings
- Ashby talent trends (interview hours): https://www.ashbyhq.com/talent-trends-report/reports/2023-recruiter-productivity-trends-report
- HackerRank Developer Skills Report 2025: https://www.hackerrank.com/reports/developer-skills-report-2025

**Compliance:**
- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- ICO, electronic mail marketing (PECR): https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/
- CRTC, CASL guidance: https://crtc.gc.ca/eng/com500/guide.htm
