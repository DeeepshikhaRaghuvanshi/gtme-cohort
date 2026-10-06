# Claude research findings: Saffron × Instantly cold-email homework (D29–D36)

Researched 6 Oct 2026 for the brief in `research/instantly/brief.md`. Format: **claim** · source · confidence (high / medium / low). Instantly product facts come from the help center (help.instantly.ai) or instantly.ai product pages, with the article's "last updated" date where the page showed one. Vendor blogs are used only for benchmarks and are labelled **[vendor blog]**. "Not found" means I looked and couldn't confirm it.

---

## 1. Instantly as of October 2026

### Plans, pricing, trial
- **Instantly sells four separately billed products: Email Outreach plans, Instantly Credits (leads, enrichment, AI agents, website visitors), CRM, and Inbox Placement. Domains and mailboxes are billed separately again.** · https://help.instantly.ai/en/articles/10273259-instantly-plans-overview (updated "this week") · high
- **Outreach plans: Growth $47/mo (1,000 uploaded contacts, 5,000 emails/mo); Hyper Growth $97/mo (25,000 contacts, 125,000 emails); Light Speed $358/mo (100,000 contacts, 500,000 emails). Annual billing: $37.60 / $77.60 / $286.30 a month. Enterprise is custom.** · https://instantly.ai/pricing and https://help.instantly.ai/en/articles/10273259-instantly-plans-overview · high
- **"Uploaded contacts" is a fixed pool across all campaigns, not a monthly allowance.** · https://help.instantly.ai/en/articles/10273259-instantly-plans-overview · high
- **Outreach add-on: $87/mo for +25,000 contacts, +125,000 emails and +500 SMTP accounts for the standard warm-up pool. Hyper Growth and Light Speed only, and stackable.** · https://help.instantly.ai/en/articles/7917050-add-on-pricing · high
- **Every paid plan has unlimited email accounts and unlimited warm-up. The difference is the SMTP-account cap for the standard warm-up pool: 100 (Growth), 500 (Hyper Growth), 1,000 (Light Speed).** · https://help.instantly.ai/en/articles/7920548-email-outreach-plans-comparison (updated 13 Jul 2026) · high
- **Features by plan: A/B (A/Z) testing is on every paid plan but not the trial. Subsequences, Slack and webhooks, Agency View, team members, extra workspaces, and *replying* from Unibox need Hyper Growth or above. API access starts at Growth.** · https://help.instantly.ai/en/articles/7920548-email-outreach-plans-comparison · high
- **Credits plans: Nano $9 (150 credits), Growth $47 (1,500), Supersonic $97 (5,000), Hyper $197 (10,000). Add-on $425 for 50,000 credits. Credits pay for SuperSearch (the lead database), enrichment, verification, AI agents and website visitors.** · https://help.instantly.ai/en/articles/10273259-instantly-plans-overview · high
- **Credit costs: lead verification 0.25 credits per lead; a verified work email found in SuperSearch 1 credit (2 if it comes from a data partner); fully enriched profile 0.5; AI Reply Agent 5 credits per reply; website visitor 3 credits per resolved profile.** · https://help.instantly.ai/en/articles/11381241-instantly-credit-system · high
- **CRM: the plans overview lists Growth CRM $47/mo and Hyper CRM $97/mo, but the CRM article says $97/mo flat with unlimited seats. The two pages conflict.** · https://help.instantly.ai/en/articles/10273259-instantly-plans-overview vs https://help.instantly.ai/en/articles/9064527-instantly-crm · medium
- **Inbox Placement is its own subscription: Growth $47/mo (unlimited one-time tests), Hypergrowth $97/mo (adds automated tests). Every account gets 2 free one-time tests.** · https://help.instantly.ai/en/articles/10273259-instantly-plans-overview and https://help.instantly.ai/en/articles/10147177-inbox-placement-feature · high
- **The pricing page now has Bundles, Outreach, Credits and VIP tabs. The bundles combine outreach and credits: Starter $94/mo (5,000 emails, 1,000 contacts, 1,500 credits), Scale $194/mo (100,000 emails, 25,000 contacts, 5,000 credits), Agency $555/mo (500,000 emails, 100,000 contacts, 10,000 credits).** · https://instantly.ai/pricing · medium (read through a page renderer; check in a browser)
- **Free trial: 14 days, no credit card, starts on sign-up. Up to 2 email accounts, 250 uploaded leads, 1,000 emails, 100 credits, 50 website-visitor emails plus 200 LinkedIn resolutions, and 2 inbox placement tests.** · https://help.instantly.ai/en/articles/13941298-instantly-free-trial (updated 24 Jul 2026) · high
- **When the trial ends: dashboard access is lost, warm-up, accounts and campaigns pause, and a trial account that hasn't been upgraded is automatically deleted. Any Loom of the build has to be recorded inside the 14 days.** · https://help.instantly.ai/en/articles/13941298-instantly-free-trial · high
- **The trial has no A/B testing and no subsequences (both "No" in the trial column), so "add B variants" needs at least the Growth plan.** · https://help.instantly.ai/en/articles/7920548-email-outreach-plans-comparison · high

### Building a campaign without a mailbox, and without launching
- **The campaign flow is: name it → Continue → add leads → write the sequence (steps and variants) → Schedule tab → Options tab → Launch. A campaign stays in Draft status until you click Launch.** · https://help.instantly.ai/en/articles/6386134-how-to-create-a-campaign-complete-setup-guide (updated 3 Aug 2026) and https://help.instantly.ai/en/articles/5975337-campaign-not-sending-complete-troubleshooting-guide · high
- **Sending accounts are assigned in Options → "Accounts to use". The documented errors ("No sending accounts assigned", "the campaign won't send if no accounts are assigned") happen at launch or send time, so a Draft can be built and saved with no mailbox attached.** · https://help.instantly.ai/en/articles/7907713-campaign-error-troubleshooting-guide and https://help.instantly.ai/en/articles/6222212-pre-launch-campaign-checklist · medium (inferred from the docs, not tested; check in the trial)
- **Sequence emails don't auto-save. Click "Save" after each step.** · https://help.instantly.ai/en/articles/6222212-pre-launch-campaign-checklist (updated 15 Jul 2026) · high
- **Preview works on lead data without a mailbox, but "Send test email" needs a "Send from" account. With no mailbox connected, the Loom can show Preview but not a test send.** · https://help.instantly.ai/en/articles/7002900-preview-and-send-test-emails (updated 29 Jun 2026) · high
- **Schedule tab: the start date defaults to "Now" and can be set to a future date (Apply, then Save), followed by Launch. A future start date is a second safeguard against accidental sending.** · https://help.instantly.ai/en/articles/6756707-campaign-start-end-date · high
- **The Subsequences tab only appears after launch, and subsequences only fire for leads labelled after launch. A "configure but don't launch" homework can't show a subsequence, which also needs Hyper Growth.** · https://help.instantly.ai/en/articles/7251329-subsequences (updated 8 Jul 2026) · high

### Leads: CSV import and variables
- **CSV import: campaign → Leads → CSV → map columns (Email is mandatory; predefined fields; "Custom variable"; "Do Not Import") → choose dedupe and verify options → "Upload all".** · https://help.instantly.ai/en/articles/6254215-how-to-import-leads-via-csv · high
- **Import limits: at most 50 variables per upload, UTF-8, headers in the first row, each header at most 20 characters.** Saffron's export has a header `Rows from: saffron_50_accounts` (30 characters): map it to Do Not Import or rename it. · https://help.instantly.ai/en/articles/6254215-how-to-import-leads-via-csv · high
- **Upload options: "Check for Duplicates Across All Campaigns/Lists" (recommended) and "Verify Leads" (0.25 credits per lead).** · https://help.instantly.ai/en/articles/6254215-how-to-import-leads-via-csv · high
- **Predefined lead fields: Email, First name, Last name, Job title, Company name, Personalization, Phone, Website, Location, LinkedIn. Anything else is a custom variable referenced as `{{columnName}}`, case-sensitive.** · https://help.instantly.ai/en/articles/6135930-how-to-add-and-use-variables-in-campaigns · high
- **Fallback syntax is `{{variableName | fallback text}}`.** · https://help.instantly.ai/en/articles/6384663-how-to-use-spintax · high
- **Mapping for Saffron's CSV:** `Work Email`→Email; `First Name`→First name; `Company Name`→Company name; `Job Title`→Job title; `Linked In Url`→LinkedIn; `Clean Domain`→Website; `Qualification Reason`→Personalization (or a custom variable); `Jobcount`→custom `jobCount`. Everything else (the waterfall `Find Work Email (n)` and `Validate …` columns) → Do Not Import. The CSV has 50 rows and `Work Email` is filled on 40 of them, so filter to those 40 first. · repo `data/saffron_people_export.csv` (header checked) · high

### Sequence editor
- **UI labels: "Add step", "Add variant", "Send next message in X days/hours/minutes". Leave a follow-up's subject blank to reuse the previous subject. The bolt icon inserts variables into subjects. The toolbar has AI tools (AI Sequence Writer, Spintax Writer, Spam Words Checker), templates, Variables, and an unsubscribe-link insert.** · https://help.instantly.ai/en/articles/11967303-getting-started-with-sequences-section · high
- **Up to 26 variants per step (A–Z). Each variant has an on/off toggle (blue = on). Usage balances across variants over the campaign's lifetime. Auto-optimise is in Options → Advanced → "Auto optimize A/Z testing" and can pick the winner on reply, click or open rate.** · https://help.instantly.ai/en/articles/6661549-a-z-testing-how-to-create-email-variants (updated 7 Aug 2026) · high
- **Instantly gives no minimum sample size before auto-optimise declares a winner.** · same · high (not found)
- **Spintax: `{{RANDOM | Hi | Hello | Hey}}`. Variables can be nested inside.** · https://help.instantly.ai/en/articles/6384663-how-to-use-spintax · high
- **Wait times count calendar days, weekends included, per lead from that lead's previous step. If the due time falls outside the schedule, the email queues for the next sending window. Use at least 1 day between steps.** · https://help.instantly.ai/en/articles/7916860-time-to-wait-between-steps (updated 8 Jul 2026) · high
- **Threading: a blank (or identical) follow-up subject keeps the email in the same thread, and follow-ups go from the same sending account by default. Some providers add "RE:" themselves.** · https://help.instantly.ai/en/articles/7914807-keep-email-sequences-in-the-same-thread · high

### Schedule, limits, stop rules, tracking, plain text, unsubscribe
- **Schedule layers apply to the whole campaign. For leads in different time zones, Instantly recommends separate CSVs and separate campaigns rather than several schedules in one campaign.** For Saffron's US list that means one ET campaign and one PT campaign if both coasts are in the list. · https://help.instantly.ai/en/articles/6573695-multiple-sending-schedules · high
- **Options tab (verbatim names): Accounts To Use; Stop Sending Emails on Reply; Open Tracking; Link Tracking; Delivery Optimization (text-only); Daily Limit; then Advanced: CRM Campaign Owner, Custom Tags, Minimum Time Gap (default 9 min), Random Additional Time (default 5 min), Max New Leads, Prioritize New Leads (Hyper Growth+), Auto Optimize A/Z, Provider Matching, ESP Routing, Stop Campaign for Company on Reply, Stop Sending Emails on Auto-Reply, Insert Unsubscribe Link Header, Allow Risky Emails, Add CC and BCC, Limit Emails Per Company (Hyper Growth+).** · https://help.instantly.ai/en/articles/6222396-campaign-options (updated 8 Jul 2026) · high
- **Instantly's recommended volume: "30 campaign emails + 10 warmup emails per day per email account."** · https://help.instantly.ai/en/articles/6222396-campaign-options · high
- **Two separate limits: the account limit caps one mailbox across all campaigns; the campaign Daily Limit caps the whole campaign across all its mailboxes. Recommended 30 a day for standard mailboxes, at most 20 for AirMail.** · https://help.instantly.ai/en/articles/6248612-account-and-campaign-limits (updated 1 Jul 2026) · high
- **Campaign Slow Ramp is set per account (Email Accounts → account → Settings → Campaign settings). It starts at 2 campaign emails on day 1 and adds 2 a day until it reaches the account's limit. After a pause it resumes from the last limit.** · https://help.instantly.ai/en/articles/10056946-campaign-slow-ramp-system (updated 8 Jul 2026) · high
- **"Stop Campaign for Company on Reply" stops emails to every lead at a company once any of them replies.** This matters for Saffron, whose list has about 3 contacts per company (50 people at 17 companies). · https://help.instantly.ai/en/articles/6222396-campaign-options · high
- **Open tracking uses a pixel; open rate = opens ÷ sequences started. Instantly says to set up a custom tracking domain before turning it on, and offers settings that disable tracking to improve inbox placement.** · https://help.instantly.ai/en/articles/12114788-open-tracking (updated 29 Jun 2026) · high
- **Link tracking counts unique clickers, through the custom tracking domain if there is one, otherwise Instantly's default shared domain.** · https://help.instantly.ai/en/articles/8030866-link-tracking · high
- **Delivery Optimization ("Send all emails as text-only" or "Send first email as text-only") strips HTML, removes images, turns links into plain URLs and disables open tracking. Instantly: "Plain-text emails have a higher chance of reaching the inbox."** · https://help.instantly.ai/en/articles/6531595-delivery-optimization-tool-send-emails-as-text-only · high
- **Workspace-level Settings → Advanced Deliverability has "Disable Open Tracking" (all campaigns), ESP Matching, "Text-Only First Email", SISR, Company Send Limits (Hyper Growth+), and AI lead filtering for low-response or hostile leads (Hyper Growth+).** · https://help.instantly.ai/en/articles/10355896-advanced-deliverability (updated 9 Jul 2026) · high
- **ESP matching sends Google→Google and Outlook→Outlook. If no matching mailbox exists it sends from what it has instead of waiting.** · https://help.instantly.ai/en/articles/7044069-email-service-providers-matching · high
- **List-Unsubscribe header: Options → Advanced → "Insert unsubscribe link header" adds a header that "supported email providers" show as one-click unsubscribe. The article doesn't name RFC 8058.** · https://help.instantly.ai/en/articles/8860388-list-unsubscribe (updated 29 Jun 2026) · medium (one-click per the vendor; RFC 8058 compliance not stated)
- **Body unsubscribe link: Sequence → step → "+" → "Insert unsubscribe link" (default text "Click here to unsubscribe"). A click sets the lead to "Unsubscribed". The link does not work in test emails.** · https://help.instantly.ai/en/articles/6191077-how-to-add-unsubscribe-link · high
- **Instantly auto-pauses a campaign when the bounce rate passes about 5% (adjustable in Preferences). Invalid and "Risky" leads are skipped unless "Allow risky emails" is on.** · https://help.instantly.ai/en/articles/7907713-campaign-error-troubleshooting-guide and https://help.instantly.ai/en/articles/9662611-catch-all-email-verification · high
- **Catch-all verification costs 0.25 credits per lead and, by Instantly's claim, recovers 300–400 extra contacts per 1,000.** · https://help.instantly.ai/en/articles/9662611-catch-all-email-verification · medium (vendor claim)
- **SEG detection flags leads behind Barracuda, Mimecast, Proofpoint or Cisco gateways as hard to reach.** · https://help.instantly.ai/en/articles/12304847-seg-detection-secure-email-gateways · high

### Warm-up, health score, pools
- **How warm-up works: your mailbox exchanges emails with other mailboxes in Instantly's pool. Warm-up emails are opened automatically, a share get positive replies, and any that land in spam are moved to the inbox.** · https://help.instantly.ai/en/articles/5975329-how-warm-up-works-and-why-it-s-important · high
- **Warm-up defaults for new accounts: Increase per day 1, Daily warmup limit 10, Reply rate 30%. Other settings: warmup filter tag, Disable slow warmup ("don't enable it for new accounts"), Weekdays only, Read Emulation, Open Rate, Spam Protection, Mark Important, Warm custom tracking domain. Instantly advises keeping the defaults.** · https://help.instantly.ai/en/articles/7988514-warmup-settings (updated 21 Aug 2026) · high
- **Health score = warm-up emails in inbox ÷ warm-up emails sent × 100, over a rolling 7 days. It's the "Health Score" column in the Email Accounts dashboard. Aim above 90%.** · https://help.instantly.ai/en/articles/13939939-warmup-health-score (updated 24 Aug 2026) · high
- **An account is ready for campaigns after at least 2 weeks of warm-up (3 weeks for AirMail) and a health score above 90%. Pre-warmed accounts can send at once.** · https://help.instantly.ai/en/articles/13938078-when-your-email-account-is-ready-for-campaigns · high
- **Instantly's 2026 deliverability blog gives a longer window for brand-new domains, "run 4–6 weeks", and a start of about 5–10 emails a day.** · https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/ (updated 4 Sep 2026) **[vendor blog]** · medium
- **Pools: Standard (green flame: a mix of Google, Outlook and SMTP) and Basic (yellow flame: mostly SMTP, weaker). Going over the plan's SMTP cap moves every account in the workspace, Google and Outlook included, down to Basic. Reassignment runs daily at 00:00 UTC.** · https://help.instantly.ai/en/articles/11118071-standard-basic-warmup-pool · high
- **Premium pool: $500/mo per workspace, aged Google/Microsoft accounts, claimed "9% more replies"; DFY and pre-warmed accounts are included automatically. Private pool: $1,000/mo, and you supply the accounts.** · https://help.instantly.ai/en/articles/10189418-premium-private-warmup-pool · high for prices, low for the 9% claim

### Account connection, tracking domain, reply-to
- **Google OAuth: in Instantly go to Email Accounts → Add New → Connect existing accounts → Google → Option 1: oAuth and copy the Client ID. In the Google Admin console go to Security → Access and data control → API Controls → Manage App Access → Configure new app, search for the client ID, pick "Instantly OAuth Email v1", set scope to All users and access to Trusted, then Finish. Back in Instantly, click Login and Allow.** · https://help.instantly.ai/en/articles/6697278-how-to-connect-google-accounts-via-google-oauth-method (updated 8 Jul 2026) · high
- **IMAP/SMTP hosts: Gmail imap.gmail.com:993 / smtp.gmail.com:465 or 587; GoDaddy imap.secureserver.net:993 / smtpout.secureserver.net:465; Namecheap mail.privateemail.com (IMAP 993; SMTP 465 or 587).** · https://help.instantly.ai/en/articles/7889049-most-popular-imap-and-smtp-hostnames · high
- **Bulk import of sending accounts: Email Accounts → Add New → Connect existing accounts → Any Provider → Bulk Import from CSV. The template sets 30/day for campaigns and 10/day for warm-up, with a warm-up increment of at most 4. Microsoft 365 accounts (including GoDaddy-bought Outlook) can't be bulk-imported.** · https://help.instantly.ai/en/articles/6687763-bulk-import-sending-accounts-into-instantly (updated 15 Jul 2026) · high
- **Custom tracking domain: a CNAME with host `inst` pointing to `prox.itrackly.com`, then entered per account under Email Accounts → account → Settings → "Custom tracking domain" as `inst.yourdomain.com`.** · https://help.instantly.ai/en/articles/6984188-custom-tracking-domain-ctd (updated 31 Jul 2026) · high
- **Reply-To is set per account (Email Accounts → account → Settings → "Reply-to"), not per campaign, and the reply-to address must itself be connected to Instantly.** The class demo described it under campaign settings. · https://help.instantly.ai/en/articles/6990255-how-to-set-up-a-reply-to-address · high
- **Instantly's DNS example: SPF `v=spf1 include:_spf.google.com ~all`; DMARC `v=DMARC1; p=none; rua=mailto:…`.** · https://help.instantly.ai/en/articles/6222192-how-to-set-up-dns-records-mx-spf-dkim-dmarc-and-domain-forwarding · high

### Inbox placement, Unibox
- **Inbox placement tests check inbox vs spam at Gmail and Microsoft, scan content for spam triggers, check SPF/DKIM/DMARC, and check 94 blacklists.** · https://help.instantly.ai/en/articles/10147177-inbox-placement-feature (updated 19 Aug 2026) · high
- **Unibox is the shared inbox for all campaign replies, with a Primary folder (leads) and an Others folder, AI sentiment labelling, statuses such as Interested and Meeting Booked, bulk actions, and notes. Replying from Unibox needs Hyper Growth.** · https://help.instantly.ai/en/articles/8797578-unibox-v2 and https://help.instantly.ai/en/articles/7920548-email-outreach-plans-comparison · high

### Done-for-you and pre-warmed mailboxes
- **DFY Google: $15 per domain per year and $5 per mailbox per month, at most 5 mailboxes per DFY domain. Warm-up starts automatically after setup.** · https://help.instantly.ai/en/articles/9361043-done-for-you-google-email-setup (updated 20 Aug 2026) · high
- **DFY catch: Instantly keeps ownership and admin access to the domain and can't transfer it. The mailboxes only work inside Instantly. Only .com and .org are offered (no .io or .ai). On cancellation, mailbox access goes immediately and Unibox conversations are deleted after 24 hours.** · same · high
- **Pre-warmed accounts: $10 per mailbox per month plus $15 per domain per year, Google only, sold in batches of 5. Domain names can't be chosen, Instantly keeps ownership, and the accounts can send at once.** · https://help.instantly.ai/en/articles/9969215-pre-warmed-domains-accounts (updated 20 Aug 2026) · high
- **AirMail (Instantly's own SMTP infrastructure): $15 per domain per year and $4 per mailbox per month, a strict 20 emails a day per mailbox, 3 weeks of warm-up recommended. Instantly suggests a 50/50 mix with Google mailboxes.** · https://help.instantly.ai/en/articles/14893942-instantly-airmail-done-for-you-email-setup (updated 10 Aug 2026) · high

---

## 2. Deliverability in 2026

### Mailbox-provider rules
- **Gmail rules for all senders: SPF or DKIM; valid forward and reverse DNS (PTR); TLS; RFC 5322 formatting; spam rate in Postmaster Tools under 0.3%.** · https://support.google.com/a/answer/81126 · high
- **Gmail bulk senders (over 5,000 a day to personal Gmail) must also publish DMARC (p=none is enough), align the From domain with SPF or DKIM, and offer one-click unsubscribe plus a visible unsubscribe link on marketing and subscribed mail.** · https://support.google.com/a/answer/81126 · high
- **The 5,000 count is per primary domain, subdomains included, and bulk-sender status is permanent once reached.** · https://support.google.com/a/answer/14229414 · high
- **Google's sender requirements "don't apply to messages sent to Google Workspace accounts", only to personal @gmail.com and @googlemail.com. Most of Saffron's prospects are on company domains, so the formal bulk rules mostly don't apply to Saffron. Workspace's own spam filtering still does.** · https://support.google.com/a/answer/14229414 · high
- **Spam-rate guidance: stay below 0.1% and never reach 0.3%. Above 0.3% a sender can't get mitigation support. Unsubscribe requests must be honoured within 48 hours. One-click unsubscribe applies only to marketing and promotional mail.** · https://support.google.com/a/answer/14229414 · high
- **Since November 2025 Gmail has stepped up enforcement: non-compliant mail now gets temporary and permanent rejections, not just spam-foldering.** · https://support.google.com/a/answer/14229414 · high
- **Yahoo, all senders: SPF or DKIM, spam rate under 0.3%, valid forward and reverse DNS. Bulk senders: SPF and DKIM, DMARC at least p=none, From alignment, one-click List-Unsubscribe (RFC 8058 POST "highly recommended"), unsubscribes honoured within 2 days. Yahoo publishes no numeric bulk threshold.** · https://senders.yahooinc.com/best-practices/ · high
- **Microsoft (Outlook.com, Hotmail, Live), effective 5 May 2025: domains sending over 5,000 a day must pass SPF and DKIM and have DMARC at least p=none, aligned with SPF or DKIM. Non-compliant mail first went to Junk; it is now rejected with "550 5.7.515 Access denied, sending domain does not meet the required authentication level".** · https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%e2%80%99s-new-requirements-for-high%e2%80%90volume-senders/4399730 (could only read search snippets, not the page) and https://learn.microsoft.com/en-us/answers/questions/5533131/how-to-fix-a-550-5-7-515-access-denied-error · medium-high
- **RFC 8058 one-click needs two headers, `List-Unsubscribe: <https://…>` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, both covered by a valid DKIM signature. The POST must work without cookies or extra steps.** · https://datatracker.ietf.org/doc/html/rfc8058 · high
- **Do the rules apply to a cold B2B sender under 5,000 a day? The all-sender rules (SPF or DKIM, PTR, TLS, spam under 0.3%) apply to everyone. The bulk rules (DMARC, alignment, one-click unsubscribe) formally don't. Because they cost nothing and protect against spoofing, configure all of them anyway.** · synthesis of the Google, Yahoo and Microsoft sources above · high

### DMARC standard (new in 2026)
- **DMARC became an IETF Standards Track RFC in May 2026: RFC 9989, which obsoletes RFC 7489 and RFC 9091 (reporting moved to RFC 9990 and 9991). It removes the `pct` tag and adds `t=y` (test mode), `np` and `psd`.** · https://www.rfc-editor.org/rfc/rfc9989.html · high
- **Google's help page still recommends rolling out with `pct` (e.g. 25% → 100%), going none → quarantine → reject, waiting at least 48 hours after SPF/DKIM before adding DMARC, and using a dedicated mailbox for rua reports.** · https://knowledge.workspace.google.com/admin/security/set-up-dmarc · high
- **dmarc.org's rollout order: SPF and DKIM first → check alignment → p=none to collect reports → analyse → quarantine → reject. Aggregate reports go to the address in `rua`.** · https://dmarc.org/overview/ · high

### DNS records for a Saffron sending domain (placeholder `getsaffronhq.com`)
- **MX (Google Workspace): host `@`, priority 1, value `smtp.google.com`.** · https://knowledge.workspace.google.com/admin/domains/set-up-mx-records-for-google-workspace · high
- **SPF: TXT at `@` = `v=spf1 include:_spf.google.com ~all`. Google recommends `~all`. Only one SPF record per domain, with at most 10 includes.** · https://knowledge.workspace.google.com/admin/security/set-up-spf · high
- **DKIM: Admin console → Apps → Google Workspace → Gmail → Authenticate email. Choose a 2048-bit key with selector `google` and publish TXT at `google._domainkey` = `v=DKIM1; k=rsa; p=<key>`. You can only get the key 24–72 hours after Gmail is activated, and it can take up to 48 hours to start working.** · https://knowledge.workspace.google.com/admin/security/set-up-dkim · high
- **DMARC, stage 1: TXT at `_dmarc` = `v=DMARC1; p=none; rua=mailto:dmarc@getsaffronhq.com`. Stage 2, after 2–4 weeks of clean aggregate reports: `v=DMARC1; p=quarantine; rua=mailto:dmarc@getsaffronhq.com`. Under RFC 9989 the testing flag is `t=y`, not `pct`.** · built from Google + RFC 9989 + dmarc.org above · high (syntax), medium (timing)
- **Custom tracking domain (optional, see §3): CNAME `inst` → `prox.itrackly.com`.** · https://help.instantly.ai/en/articles/6984188-custom-tracking-domain-ctd · high
- **Verify the records with mail-tester or MXToolbox, as the learning guide says.** · source/REF_learning-guide.md:1564 · high

### Domains, mailboxes, caps, warm-up
- **Domain naming: buy lookalikes of the brand. Instantly's examples are `Getshrimp.com`, `Tryshrimp.com` and `TastyShrimpApp.com`, it says ".com domains" work best, and its DFY service only offers .com and .org.** · https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy (updated 15 Jul 2026) and https://help.instantly.ai/en/articles/9361043-done-for-you-google-email-setup · high
- **Mailboxes per domain: Instantly's strategy article says "max 3–5", its DIY blog says 3, and DFY caps it at 5.** · https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy and https://instantly.ai/blog/diy-email-setup/ **[vendor blog]** · high
- **Per-mailbox cold sends a day: the help center says 30 (plus 10 warm-up); the strategy article says 30–50; AirMail allows at most 20; the learning guide says 20–30.** · https://help.instantly.ai/en/articles/6222396-campaign-options and source/REF_learning-guide.md:1520 · high
- **Google Workspace's hard limits (2,000 messages a day per user, 500 on trial accounts, 3,000 external recipients a day) sit far above cold-email-safe volumes. The binding limit is reputation, not quota.** · https://knowledge.workspace.google.com/admin/gmail/gmail-sending-limits-in-google-workspace · high
- **Microsoft cancelled its planned Exchange Online external-recipient limit (2,000 a day) on 6 Jan 2026.** · https://techcommunity.microsoft.com/blog/exchange/exchange-online-canceling-the-mailbox-external-recipient-rate-limit/4483498 · high
- **Prices: Google Workspace Business Starter costs ₹270 per user per month in India (Google's pricing page as seen from India) or about $7 (annual) / $8.40 (flexible) in the US. Microsoft 365 Business Basic went from $6 to $7 per user per month on 1 Jul 2026.** · https://workspace.google.com/pricing (high, INR), https://www.emailvendorselection.com/google-workspace-pricing/ (medium, USD), https://www.microsoft.com/en-us/licensing/news/2026-m365-packaging-pricing-updates (high) · as marked
- **Workspace vs Microsoft 365: Instantly's OAuth is simplest for Google. Microsoft 365 accounts can't be bulk-imported. ESP matching rewards having both, but a ~240-email programme only needs Google.** · https://help.instantly.ai/en/articles/6687763-bulk-import-sending-accounts-into-instantly and https://help.instantly.ai/en/articles/7044069-email-service-providers-matching · medium (recommendation)
- **Saffron's minimal setup (DIY): 1–2 .com lookalike domains (~$10–15/yr each) × 2 Workspace mailboxes = 2–4 mailboxes at ₹270 (or $8.40) each a month, plus Instantly Growth $47/mo. Total about $64–81/mo plus ~$30/yr. Capacity: 2 mailboxes × 30/day × 22 working days = 1,320 emails a month, against 40 leads × 6 steps = 240 needed. DFY alternative: $30/yr + $20/mo for 4 mailboxes, but Instantly owns the domains.** · calculated from the sources above · high (arithmetic), medium (registrar price)

### Data hygiene
- **Bounce rate: Instantly's 2026 benchmark says keep it under 2%, and Instantly auto-pauses at about 5%. The learning guide's "bounce > 2%" causal chain matches.** · https://instantly.ai/cold-email-benchmark-report-2026 and source/REF_learning-guide.md:1478 · high
- **Catch-all addresses: the class rule is to send to Valid + Valid-catch-all only (notes/D21-D22:57). Instantly skips Risky (catch-all) leads by default unless they pass its paid catch-all verification.** · https://help.instantly.ai/en/articles/9662611-catch-all-email-verification · high
- **Google retired the Domain and IP Reputation dashboards in Postmaster Tools v2. Other dashboards remain, plus a new compliance-status view.** · https://support.google.com/mail/answer/16594218 · high (that they were retired), medium (date details)

---

## 3. Tracking

- **Apple Mail Privacy Protection hides the reader's IP and stops senders from seeing whether a message was opened, by loading remote content (including tracking pixels) privately. Opens from Apple Mail users are therefore unreliable.** · https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios · high
- **In Litmus's 2026 client-share data Apple accounts for roughly 58–65% of tracked opens, and over half of opens come from MPP-enabled devices. That data is B2C-heavy; B2B inboxes skew towards Outlook and Gmail.** · https://www.litmus.com/email-client-market-share **[vendor data]** · medium
- **Microsoft Defender Safe Links scans URLs "prior to message delivery", rewrites them, and "detonates" URLs without a valid reputation in the background. Security gateways at corporate recipients therefore produce machine "clicks" (and image fetches), which pollute link and open stats and make tracked links look like phishing redirects.** · https://learn.microsoft.com/en-us/defender-office-365/safe-links-about (updated 22 May 2026) · high (scanning), medium (effect on stats)
- **Hunter's 2026 report (31M emails sent in 2025): campaigns with open tracking off got a 7.4% reply rate vs 4.4% with it on (+68%).** · https://hunter.io/the-state-of-cold-email **[vendor data, correlational]** · medium
- **Snov.io (44M emails): turning off open tracking more than doubled reply rates, from 1.08% to 2.36%.** · https://snov.io/blog/we-analyzed-44-million-emails/ **[vendor data, correlational]** · medium
- **Instantly itself presents tracking as a trade-off. Text-only mode (its deliverability tool) switches off open tracking, it has a workspace switch to "Disable Open Tracking", and its blog says to "disable link tracking temporarily" when spam placement spikes.** · https://help.instantly.ai/en/articles/6531595-delivery-optimization-tool-send-emails-as-text-only, https://help.instantly.ai/en/articles/10355896-advanced-deliverability, https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/ · high
- **What a custom tracking domain fixes: the pixel and rewritten links point at your own subdomain instead of a domain shared with every Instantly customer, so other senders' reputation doesn't rub off on yours.** · https://help.instantly.ai/en/articles/6984188-custom-tracking-domain-ctd and https://instantly.ai/blog/what-is-a-custom-tracking-domain/ **[vendor blog]** · high
- **What it doesn't fix: the HTML pixel still exists, MPP still inflates opens, gateways still pre-click links, and plain-text mode can't carry a pixel at all. Instantly's docs don't say a CTD is needed when tracking is off.** · synthesis of the Apple, Microsoft and Instantly sources · high (mechanics), "not found" on Instantly's position
- **Resolving the D33 vs D35 contradiction: they aren't really in conflict. D33 taught how to track safely if you track (use a CTD); D35 taught that for cold email you shouldn't track. Recommended practice: open and link tracking off, plain-text first email, no links in step 1, and measure replies and positive replies. Setting up a CTD is still cheap insurance (one CNAME) if a later step includes a link or the team later turns tracking on, and Instantly's warm-up can include the CTD ("Warm custom tracking domain").** · Instantly, Hunter and Microsoft sources above + notes/D29-D36_summary-notes.md:100,140,158 · high
- **Metrics to use instead of opens: reply rate, positive-reply rate, meetings booked per 100 leads, bounce rate, and the warm-up health score (deliverability proxy), plus an inbox placement test before launch.** · https://instantly.ai/cold-email-benchmark-report-2026 and https://help.instantly.ai/en/articles/10147177-inbox-placement-feature · high

---

## 4. Cold-email copy in 2026

- **Instantly 2026 benchmark (Jan–Dec 2025, "billions" of interactions): average reply rate 3.43%, top quartile 5.5%+, top 10% 10.7%+.** · https://instantly.ai/cold-email-benchmark-report-2026 · high (as Instantly's own figure)
- **58% of replies come from step 1 and 42% from follow-ups. The sweet spot is 4–7 touches, spaced 3–4 days apart.** · same · high
- **Top performers write first-touch emails under 80 words, with one CTA and a problem-first angle.** · same · high
- **Launch on Monday, Wednesday gets the most engagement, and auto-replies surge on Friday.** · same · medium
- **Instantly publishes no positive-reply rate, meeting rate or industry breakdown in that report.** · same · high (not found)
- **lemlist (citing Instantly): SaaS/software reply rates "often fall below 2%" despite high opens. Meetings booked run 0.5–2.5% of leads.** · https://www.lemlist.com/blog/cold-email-benchmarks **[vendor blog]** · medium
- **Hunter 2026: sales outreach averages a 3% reply rate. 21–50-recipient campaigns beat 500+ (6.2% vs 2.4%). One contact per company beats 3+ (5.1% vs 3.5%). Two custom attributes in the body lift replies (5.6% vs 3.6%). 69% of recipients dislike obviously AI-written emails, and 50.5% prefer LinkedIn for outreach (25% prefer email).** · https://hunter.io/the-state-of-cold-email **[vendor data]** · medium
- **That Hunter data backs the class's micro-campaign advice (narrow segments over mass AI personalisation) and argues against emailing all ~3 contacts per Saffron account at once: stagger them or use "Stop Campaign for Company on Reply".** · synthesis · medium
- **CTA: in Gong's study of 304,174 emails, an interest CTA ("Are you interested in…?") was more than 2× as likely to book a meeting as asking for time. Specific-time asks win only once a deal is active.** · https://www.gong.io/blog/this-surprising-cold-email-cta-will-help-you-book-a-lot-more-meetings **[vendor research]** · medium-high
- **Instantly's own framework is Personalization + Offer + CTA: low-friction asks ("Mind if I send more info?"), a 4-touch cadence (initial, bump after +2 days, value-add after +2, breakup after +3), and hand-written first lines over automated ones.** · https://help.instantly.ai/en/articles/6570131-cold-email-copywriting-framework-we-use-to-get-400-replies-monthly (updated 14 Jul 2026) · high
- **Instantly's strategy article recommends a 3-step sequence (cold email, quick bump, break-up) for the starter setup.** · https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy · high
- **Follow-ups in the same thread (blank subject) are Instantly's default mechanism. A new thread only makes sense for a deliberate change of angle.** · https://help.instantly.ai/en/articles/7914807-keep-email-sequences-in-the-same-thread · high (mechanism), medium (advice)
- **A/B sample size (my calculation, two-sided α=0.05, 80% power): detecting 3.43% → 4.12% (a 20% relative lift) needs about 12,100 sends per variant. Detecting 3% → 6% needs about 750 per variant; 3% → 9% about 240. Several vendor blogs quote "~1,560 per variant" for the 20% case, which understates it about 8×. With 40 leads Saffron's A/B results are anecdotal, not statistically meaningful.** · standard two-proportion formula; vendor figure at https://www.unifygtm.com/explore/cold-email-ab-testing-statistical-rigor · high (maths)
- **Test design: change one variable per test, put the B variant in step 1 (where 58% of replies happen), and judge on reply or positive reply, not opens. Opens are unreliable (§3) and Instantly's auto-optimise can pick by open rate if you let it.** · https://help.instantly.ai/en/articles/6661549-a-z-testing-how-to-create-email-variants + synthesis · high
- **Spam-trigger words: Instantly has an "AI Spam Words Checker" in the sequence editor toolbar.** · https://help.instantly.ai/en/articles/9921051-ai-spam-words-checker · high
- **AI opener only: Gartner found only 26% of job candidates trust AI to evaluate them fairly (a candidate-side figure, but it shows the AI-scepticism Saffron's copy should anticipate). Hunter's 69% "bothered by AI-written emails" supports keeping AI to a single, fact-checked opening line, as Yogesh teaches.** · https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them, https://hunter.io/the-state-of-cold-email · medium

---

## 5. Saffron's buyers: 2025–26 pain and how competitors position

- **Engineers spend more time interviewing: Ashby (Jan 2021–Mar 2026) puts the average technical hire at 23.3 interview-hours and 17.6 interviews, 52% more interviews than in 2021. A business hire takes 12.2 hours.** · https://www.ashbyhq.com/talent-trends-report/reports/2023-recruiter-productivity-trends-report (the page now shows Q1 2026 data) · high
- **HackerRank 2025 Developer Skills Report (13,732 respondents): 97% of developers use an AI assistant; 76% say AI makes gaming assessments easier; 73% feel it's unfair to lose out to candidates who use AI; 78% say assessments don't match real work; 66% want to be evaluated on real-world skills.** · https://www.hackerrank.com/reports/developer-skills-report-2025 · high
- **Stack Overflow 2025: 84% of developers use or plan to use AI tools, but only 29% trust AI output to be accurate (46% actively distrust it).** · https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/ · high
- **Gartner (31 Jul 2025): 6% of 3,000 candidates admitted interview fraud, 39% used AI during applications (including for assessment answers), and Gartner predicts 1 in 4 candidate profiles will be fake by 2028.** · https://www.hrdive.com/news/fake-job-candidates-ai/757126/ (reporting Gartner) and https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them · medium-high
- **Meta's response: since October 2025 an "AI-enabled coding" round replaces one onsite coding round for E4/E5 engineers, in CoderPad with an AI assistant. AI-allowed interviews are becoming normal.** · https://www.hellointerview.com/blog/meta-ai-enabled-coding and https://coderpad.io/blog/hiring-developers/ai-in-the-interview-is-not-cheating-it-is-the-job-according-to-meta/ · medium
- **HackerRank now leads with "Hire for the agentic era", its agentic interviewer "Chakra" (evaluates "AI fluency, not just correctness"), and an integrity pitch: "Integrity isn't about whether you use AI or not."** · https://www.hackerrank.com/ · high
- **CodeSignal leads with "Agentic skills validation & development": AI Interviewer, Agentic Assessments, AI Phone Screens, AI Video Avatars.** · https://codesignal.com/ · high
- **CoderPad leads with "Every role is technical now. Hire like it.": AI assistants in the pad with prompts captured, playback reports, and cheating alerts (products Qualify, Screen, Interview).** · https://coderpad.io/ · high
- **Karat leads with "Transform your organization for the Human + AI era": 600,000+ human-expert interviews, "Live AI-native scenarios", and AI Readiness (NextGen).** · https://karat.com/ · high
- **Where Saffron stands apart: every incumbent now says "AI fluency", so that phrase alone won't differentiate. Saffron's unique hooks are (1) the candidate works on *your own codebase*, not a sandbox problem; (2) line-level human/AI attribution plus a full session replay; (3) zero interviewer hours (against Ashby's 23.3 h per technical hire); (4) self-serve pricing at $199–$499/mo against enterprise-sales incumbents.** · competitor pages above + strategy/strategy-doc-saffron-v2.md:16,34 · medium (judgement)
- **Copy hooks with numbers: "23 interviewer-hours per engineering hire" (Ashby); "76% of developers say AI makes gaming assessments easier" (HackerRank). Both suit the S2 and S3 one-liners.** · sources above · high (numbers), medium (use)

---

## 6. Compliance

- **CAN-SPAM covers all commercial email, with "no exception for business-to-business". You need accurate headers, a non-deceptive subject line, identification as an ad, a valid physical postal address (a registered PO box or private mailbox is fine), a clear opt-out, opt-outs honoured within 10 business days, and an opt-out that keeps working for 30 days after sending. Penalties run up to $53,088 per email.** · https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business · high
- **A reply-based opt-out is legal under CAN-SPAM: "a return email address or another easy Internet-based way". You can't require more than a reply or one web page. Yogesh's "reply 'no'" P.S. satisfies the opt-out rule if it's honoured, but the physical address is still required.** · same · high
- **Header accuracy ("identify the initiator") means Deepu can't send as Saffron without Saffron's permission. That's one more reason the homework stops at "configure, don't launch".** · same · medium (application)
- **UK PECR: you can email corporate subscribers (companies, LLPs) without consent, but you must identify yourself and give an opt-out address. Sole traders and partnerships need consent or the soft opt-in. The ICO notes the page is under review after the Data (Use and Access) Act 2025.** · https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/ · high
- **UK GDPR still applies to named employees' personal data, so the lawful basis is legitimate interests (with a balancing test). The DUAA 2025 adds Art. 6(11) naming direct marketing as an example of a legitimate interest; it is not a "recognised legitimate interest" that skips the balancing test.** · https://www.farrer.co.uk/news-and-insights/data-use-and-access-act-2025-five-key-changes-for-businesses/ and https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/ · medium
- **EU GDPR Art. 14: when data didn't come from the person, you must tell them at the latest at the first communication, including where the data came from (Art. 14(2)(f)). A cold email to an EU prospect therefore needs a short privacy notice or link.** · https://gdpr-info.eu/art-14-gdpr/ · high
- **Germany is stricter: UWG §7(2) No. 2 requires prior express consent for email advertising, B2B included. Phone calls to businesses only need presumed consent. Don't cold-email German prospects.** · https://www.gesetze-im-internet.de/uwg_2004/__7.html · high
- **Canada (CASL): you need express or implied consent. Implied consent covers a conspicuously published business address with no "no CEMs" statement, and only if the message relates to the person's role. An address found through an enrichment waterfall is not "conspicuously published". Unsubscribes must be honoured within 10 business days, and the link must stay valid for 60 days. Penalties reach C$10M per violation for businesses.** · https://crtc.gc.ca/eng/com500/guide.htm and https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/getting-consent-send-email · high (the CRTC FAQ returned 403, so this comes from search snippets of CRTC pages)
- **India's DPDP Act: s.17(1)(d) exempts most obligations when data of people outside India is processed "pursuant to any contract" with a person outside India by someone based in India. Security safeguards (s.8(5)) and accuracy (s.8(1)) still apply.** · https://indiankanoon.org/doc/180784190/ · high (text)
- **The DPDP Rules 2025 were notified on 13–14 Nov 2025 and phase in: Board provisions immediately; consent managers from 13 Nov 2026; the core obligations from 13 May 2027.** · https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025 and https://dpdpa.dcomply.in/rules/ · medium
- **Does DPDP matter for Saffron? For a US company emailing US prospects, the US rules (CAN-SPAM) govern. DPDP mostly matters if Deepu processes the data in India without a contract with Saffron; even then most duties are exempted or not yet in force. Keep the data secure and minimal (CLAUDE.md already says this).** · synthesis · medium

---

## 7. Class-topic depth

### Intelligence tables, tiering, CRM upsert
- **"Upsert" in practice: HubSpot's batch upsert endpoint (`POST /crm/objects/…/contacts/batch/upsert`) updates a contact when the `idProperty` (email or a custom unique property) matches and creates it otherwise, up to 100 records per call. This is what "write out to CRM without duplicates" means.** · https://developers.hubspot.com/docs/api-reference/latest/crm/objects/contacts/batch/upsert-contacts · high
- **The learning guide's D29 adds conditional export: push only rows that meet a condition (score ≥ threshold and verified email) through a native integration or an outbound webhook, then confirm the record actually arrived.** · source/REF_learning-guide.md:1382–1388 · high
- **Company tiering → persona: Yogesh's example is a founder at 60 employees and a VP Engineering at 400. For Saffron that maps to S1 50–200 → CTO/founder; S2 200–1,000 → VP Eng or Head of TA plus an Eng Manager champion.** · notes/D29-D36_summary-notes.md:25,36; strategy/strategy-doc-saffron-v2.md:122–123 · high

### Infrastructure and authentication
- **OAuth vs SMTP/IMAP: OAuth (Google, Microsoft) means no stored password and admin-approved app access. SMTP/IMAP is for other providers (GoDaddy, Namecheap, Zoho), uses the mailbox password and needs a host and port. IMAP 993 is universal; SMTP is 465 (implicit TLS) or 587 (STARTTLS).** · https://help.instantly.ai/en/articles/6697278-how-to-connect-google-accounts-via-google-oauth-method and https://help.instantly.ai/en/articles/7889049-most-popular-imap-and-smtp-hostnames · high
- **Alignment explained: DMARC passes when the visible From domain matches (aligns with) the domain that passed SPF (the envelope sender) or the DKIM `d=` domain. Relaxed alignment (the default) accepts subdomains of the same organisational domain.** · https://support.google.com/a/answer/14229414 and https://www.rfc-editor.org/rfc/rfc9989.html · high

### Warm-up and mailbox maths (worked with Instantly's current numbers)
- **Class formula: working days × mailboxes × daily limit ÷ steps = leads a month. At Instantly's recommended 30/day instead of the class's 50: 22 × 10 × 30 = 6,600 emails ÷ 6 = 1,100 leads a month (the class figure was 1,833).** · https://help.instantly.ai/en/articles/6222396-campaign-options + source/X3_instantly-training.md:69–71 · high (arithmetic)
- **D33 example redone at 30/day: 2,000 leads × 6 = 12,000 emails ÷ (30 × 22 = 660 per mailbox) ≈ 19 mailboxes over 4–7 domains (at 3–5 per domain), not ~12 over 3.** · same + notes/D29-D36_summary-notes.md:84 · high (arithmetic)
- **Saffron: 40 × 6 = 240 emails. One mailbox at 30/day covers that in about 8 working days; two give headroom and ESP diversity.** · calculation · high

### Subsequences and multichannel
- **Instantly subsequence triggers: lead-status changes (Interested, Meeting Booked, Meeting Completed, Won, Out of Office, Wrong Person, Not Interested, Lost, plus custom statuses), activity (link clicked, email opened, campaign completed without reply), or reply keywords (separated by `;`). The lead stays in the main campaign.** · https://help.instantly.ai/en/articles/7251329-subsequences · high
- **The learning guide's 2-channel example: Day 1 email, Day 2 LinkedIn connect, Day 4 email, Day 6 LinkedIn message, kept to 4–6 touches over about 10 days.** · source/REF_learning-guide.md:1826,1846 · high
- **LinkedIn caps invitations at roughly 100 a week for most accounts. This isn't confirmed on LinkedIn's own help pages; the figure comes from practitioner posts.** · https://www.linkedin.com/pulse/linkedin-new-weekly-invitation-limit-dan-porat · low

### Instantly vs Smartlead vs Email Bison (Oct 2026)
- **Smartlead: Base $39 (2,000 contacts, 6,000 emails a month), Pro $94 (30,000 / 90,000), Smart $174 (unlimited contacts / 150,000), Prime $379 (500,000 emails, 3 client workspaces included). Client workspaces and white label are add-ons at $29–39 per client, which is the agency fit. Unlimited mailboxes and warm-up on every plan.** · https://www.smartlead.ai/pricing · high
- **Email Bison: one plan at $599/mo for 500,000 emails a month (more in extra buckets), isolated network with dedicated IPs, unlimited leads, workspaces and seats.** · https://emailbison.com/pricing · high
- **Instantly suits one company (or a small agency) because of its built-in lead database, CRM and Unibox. It now also offers agency white-labelling and workspace groups, so "Instantly = single company only" is outdated.** · https://help.instantly.ai/en/articles/8678006-agency-white-labeling · medium

### Frameworks, A/B testing, micro-campaigns
- **The learning guide's D36 structure: a signal-tied opener, a problem/value line, light proof, a soft CTA, readable in under 10 seconds. Subject lines short, lowercase-ish, no hype or trigger words. D37 adds insight → implication → proof → soft ask.** · source/REF_learning-guide.md:1690–1696,1734 · high
- **D38's AI-opener rule: one sentence, under 20 words, no greeting, no hype, plus a QC column that flags long, generic, empty or unsupported lines and a 10-row hand check.** · source/REF_learning-guide.md:1776,1782 · high

---

## Class content extracted (file:line)

### D29–D30: intelligence tables (29 Sep)
- Build "intelligence tables": company and people tables kept separate, mandatory keys, quality filters. · notes/D29-D36_summary-notes.md:13,21–23
- Company domain and company LinkedIn URL are the mandatory enrichment keys. · notes/D29-D36_summary-notes.md:21
- Drop LinkedIn profiles with under 100 followers (likely fake or inactive). · notes/D29-D36_summary-notes.md:22
- CRM upsert = update if the record exists, insert if not. · notes/D29-D36_summary-notes.md:24
- Tier by scale (founder at 60 people, VP Eng at 400). People tables are linked to tiers by conditional formulas, and a new company in a tier triggers that tier's people search. · notes/D29-D36_summary-notes.md:25
- Write the logic and prompts in Claude first, then build in Clay. Claude Code (MCP/CLI, Buffer posting) is where the role is heading, at about $20/mo. · notes/D29-D36_summary-notes.md:26–27
- Homework: Clay about 2 h a day, a personal Loom, a new GTM tool daily compared with the manual process it replaces. · notes/D29-D36_summary-notes.md:30–32
- Saffron gap: no tier column (a 99- and a 589-person company are treated the same). · notes/D29-D36_summary-notes.md:36
- Learning guide D29: native integrations / CSV / outbound webhook, conditional export, confirm it landed. · source/REF_learning-guide.md:1382–1388
- Learning guide D30: company in → scrape + Claygent + waterfall email → one clean row with a source-grounded "insight" field. Portfolio deliverable #6. · source/REF_learning-guide.md:1426–1450

### D31–D32: deliverability is infrastructure; domains and mailbox maths (30 Sep)
- Most failures come from infrastructure and data, not copy. Severity: infrastructure and data highest; messaging, placeholders and setup lower. · notes/D29-D36_summary-notes.md:44,50–52
- Yogesh: global cold-email reply rates are about 3%; emerging verticals and non-English regions respond better; avoid targeting software companies. · notes/D29-D36_summary-notes.md:49
- Placeholders: first name and company only. AI writes only the opening line, from a signal. No "book a meeting" CTA. · notes/D29-D36_summary-notes.md:54–56
- SPF/DKIM/DMARC on every sending domain. Warm up about 3 weeks, ramping 10 → 30 a day per mailbox. Buy mailboxes through Google Workspace or Outlook. · notes/D29-D36_summary-notes.md:58–60
- Never send from the main domain. · notes/D29-D36_summary-notes.md:61
- Planning maths: leads × steps → emails a month → mailboxes needed. · notes/D29-D36_summary-notes.md:62
- Tools: Instantly for one company sending for itself; Smartlead for agencies; Email Bison about $600/mo, "unlimited leads and emails"; base plans are restrictive. · notes/D29-D36_summary-notes.md:64–67
- Recipients report spam rather than clicking footer unsubscribe links, so use a plain opt-out line. Homework P.S.: "If this isn't relevant, just reply 'no' and I won't follow up". · notes/D29-D36_summary-notes.md:68,71
- Learning guide: about 1 in 6 legitimate emails misses the inbox. Spam chains: no auth → distrust → reject; bad list → bounces > 2% → reputation drops; generic blast → complaints > 0.3% → delivery stops. · source/REF_learning-guide.md:1472,1478
- Learning guide: the bulk rules formally target 5,000+/day but treat them as universal. · source/REF_learning-guide.md:1484
- Learning guide: secondary domains (variations, alternate TLDs like .co or .io); reputable registrars; per-mailbox cap about 20–30/day; "200/day at 30/mailbox → ~7 mailboxes across 2–3 domains"; 3–8 domains per programme; rotation required above about 1,000 sends a month; buy a ~$10 test domain. · source/REF_learning-guide.md:1514–1540
- D03–D04 tool notes: Instantly for single-client, limited volume; SmartLead for high volume plus validation; Email Bison "top 1%", ~$600, infrastructure-focused. · notes/D03-D04_the-seven-layer-mental-model-stand-up-your-workspa.md:37–39
- D21–D22 benchmarks: email 90%+ open / 3–5% reply; LinkedIn 70% accept / 30% reply. Push to a sequencer only if score ≥ 80 and industry matches. · notes/D21-D22_waterfall-enrichment-conditional-logic-run-only-if.md:9,34
- Valid / Invalid / Valid catch-all / catch-all-only definitions; build lists from Valid + Valid catch-all only. · notes/D21-D22_waterfall-enrichment-conditional-logic-run-only-if.md:57,128

### D33–D34: authentication; warm-up and sending discipline (1 Oct)
- Worked capacity example: 2,000 leads × 6 steps = 12,000 emails a month; 50/day × 22 days = 1,100 per mailbox; about 11–12 mailboxes over 3+ domains. · notes/D29-D36_summary-notes.md:84,90–93
- Under about 2,000 leads a month, prioritise LinkedIn over email. · notes/D29-D36_summary-notes.md:85
- Warm-up never stops: start at 10 a day and keep it running alongside campaigns. · notes/D29-D36_summary-notes.md:86
- Campaign planning = segment → lead list → warm infrastructure. · notes/D29-D36_summary-notes.md:94
- Behavioural subsequences branch on opened / clicked / replied. Stagger follow-up intervals. · notes/D29-D36_summary-notes.md:95–96
- Google and Outlook connect via OAuth/API (client IDs); others via SMTP/IMAP host, port and encryption. · notes/D29-D36_summary-notes.md:98–99
- Custom tracking domain = a CNAME so tracking uses your domain. · notes/D29-D36_summary-notes.md:100
- Plain text with no links gets past strict corporate filters. · notes/D29-D36_summary-notes.md:101
- Multichannel: email + LinkedIn + phone in a 3–4-month repeating pattern for unresponsive prospects. · notes/D29-D36_summary-notes.md:102
- Biotech signals: finance hires, new CFOs, press and funding news. · notes/D29-D36_summary-notes.md:103
- GTM engineering vs demand gen. Yogesh's economics: one GTME replaces up to 10 people (~₹2,000/mo in tools vs ~₹8 lakh in salaries; unverified). · notes/D29-D36_summary-notes.md:104–105
- Homework: plan 10 distinct campaigns (segments or territories). Saffron map: 3 segments × 2 personas × top signals. · notes/D29-D36_summary-notes.md:108,112–117
- Saffron numbers: 40 × 6 = 240 emails; 1–2 mailboxes; LinkedIn first. · notes/D29-D36_summary-notes.md:111
- Learning guide D33: MX/SPF/DKIM/DMARC definitions; all three required together; DMARC p=none → quarantine → reject; custom tracking domains; verify with mail-tester or MXToolbox. · source/REF_learning-guide.md:1558–1564
- Learning guide claims: "Gmail permanently rejects mail from senders without DMARC"; DMARC published on >75% of large domains but enforced on only ~35%; RFC 8058 one-click is part of the bundle. · source/REF_learning-guide.md:1568–1570
- Learning guide D34: start at 5–10 a day, ramp over 4–6 weeks; write a 21-day day-by-day schedule from ~5 to ~50; inbox rotation; complaints under 0.3% (aim under 0.1%), bounce under 2%; over the line means 7 consecutive days to regain mitigation eligibility; monitor the slope in Postmaster Tools. · source/REF_learning-guide.md:1602–1612

### Instantly training video (X3, undated)
- Setup order: (1) connect emails → (2) custom tracking domain → (3) warm-up → (4) SPF/DKIM/DMARC; at least 2–3 hours. · source/X3_instantly-training.md:27,153; notes/X3_instantly-training.md:7
- Warm-up week 1: +1/day up to 10. Week 2: +2/day up to 20. Week 3: +3/day up to 30. Then permanent low frequency; "warmup never stops". · source/X3_instantly-training.md:29,35–37,57; notes/X3_instantly-training.md:33,65
- Why warm-up never stops: outreach is send-only and Google sees one-way sending as misuse. · source/X3_instantly-training.md:35
- Health score: one spam placement caused by starting outreach before warm-up finished; ideal warm-up is 3 weeks. · source/X3_instantly-training.md:37
- Health below 80% → pull from campaigns and re-warm to 100% ("if it's 70 you can go back to 100"). · source/X3_instantly-training.md:45–47,59–61
- Health drops from incomplete warm-up, sending to wrong addresses, and blasting volume. · source/X3_instantly-training.md:51–53
- About 3 mailboxes per domain is ideal; Yogesh runs 5 on one domain ("not a good idea"). · source/X3_instantly-training.md:45
- Agency scale: 10 domains and 50 mailboxes per client, 50 sends each. His spoken arithmetic went inconsistent (he said "500" mailboxes and "25,000 emails a day"). · source/X3_instantly-training.md:49–51,55
- Volume logic: about 1% reply at agency volume, about 10% of replies positive. · source/X3_instantly-training.md:55
- Campaign planning: the formula, outreach limit 50/day vs warm-up 10/day, count working days only (Mon–Fri, never ×30), sending hours 10:30–17:30. · source/X3_instantly-training.md:63–67
- Worked: 22 × 10 × 50 = 11,000 emails a month ÷ 6 ≈ 1,833 leads; second example 55 mailboxes / 22 days / 5-step ≈ 1,000+ (the arithmetic actually gives 12,100); 2,000 leads would need about 40 more mailboxes. · source/X3_instantly-training.md:69–79
- Outreach ramp: 20/day week 1 → 30 → 40 → cap 50, via "Campaign Slow Ramp". Wait time between emails 1 minute is fine; his own limit is 30 because he's in week 2. · source/X3_instantly-training.md:53,71–73
- Pre-warmed accounts "save three weeks but make no sense" (not your domains). DFY is the premium service with an assigned Instantly GTM engineer. · source/X3_instantly-training.md:83
- OAuth via Workspace admin → configure new app → client ID → approve. IMAP username = address, password = mailbox password; GoDaddy `imap.secureserver.net`; Outlook `outlook.office365.com`; IMAP 993; SMTP 587 first, 465 fallback. · source/X3_instantly-training.md:85–105
- Settings: signature, tags per client, Reply-To example (founder sends, head of sales receives; Razorpay example). · source/X3_instantly-training.md:127–131
- CTD: add the provided record at the registrar's DNS; TTL "one hour, sometimes half an hour"; analogy of one mall guard for all stores vs your own guard. · source/X3_instantly-training.md:131–141
- Warm-up filter tag: per email, never per client (the heart-rate analogy); create "red alert", "week 1" and "week 2" tags. · source/X3_instantly-training.md:141–145
- "Only send on working days" for warm-up is a paid-plan feature. · source/X3_instantly-training.md:147–149
- Unsubscribe: without it, angry recipients report spam and the domain is "done"; the link is in campaign settings. · source/X3_instantly-training.md:149–151
- The $12K/mo client anecdote: infrastructure wrong for 3 months, client left, engineer let go. · source/X3_instantly-training.md:155–157
- SPF = IP matching ("lists the exact IP address and service permitted"); DKIM = cryptographic signature proving content unchanged; DMARC "controls SPF and DKIM"; this is asked in every interview. · source/X3_instantly-training.md:159–165
- Email-infrastructure specialists earn about $2,000/mo; managing 500 mailboxes is "a daunting task". · source/X3_instantly-training.md:167
- Analytics can be shared (download or view access). Unibox categories: interested, meeting booked, won/lost, out of office. · source/X3_instantly-training.md:169–171
- Campaign options: stop on reply; open tracking; daily limit = mailboxes × per-mailbox (5 × 50 = 250); auto-reply/OOO; unsubscribe; risky emails (invalid; Instantly has a verifier); CC/BCC. · source/X3_instantly-training.md:171–175
- Subsequence: "a sequence within the sequence". Example of 100 sends: 50 no reply, 20 neutral, 10 positive, 10 negative. Negative → apologise and confirm removal (or offer options); positive → booking sequence; neutral/no reply → retry. Mid- or post-campaign; AI sentiment detection. · source/X3_instantly-training.md:175–181
- Team access: Settings → Workspace and Members → invite as Viewer (not on his plan). · source/X3_instantly-training.md:181–183
- Bulk-connect mailboxes via the sample CSV (email, names, IMAP/SMTP user, password, host, port, daily limit, warm-up limit). · source/X3_instantly-training.md:191–193
- Other: Lemlist 30-day trial (student report); follow Tim Jacobsen; brand-agnostic skills (Smartlead job ads). · source/X3_instantly-training.md:197–199; notes/X3_instantly-training.md:81

### D35–D36: deliverability runbook; cold-email frameworks (2 Oct)
- Biotech worked example (a classmate's live Instantly campaign): US biotech and life science, 51–1,000 employees, lean finance teams or hiring for finance, NetSuite or QuickBooks users; "uses Excel" can't be tracked because no public data exists. · notes/D29-D36_summary-notes.md:124,130–133
- Sequence: 6 emails, follow-ups 2–5 days apart; the last email offers options (wrong budget / wrong timing / not relevant). · notes/D29-D36_summary-notes.md:135–136
- A/B: two variants per email, e.g. industry-pain angle vs integration angle. · notes/D29-D36_summary-notes.md:137
- Micro-campaigns (narrow, niche, tailored) beat complex AI personalisation. · notes/D29-D36_summary-notes.md:138
- Non-responders get an engagement-based follow-up sequence after the campaign. · notes/D29-D36_summary-notes.md:139
- Disable open and link tracking (corporate security flags them). Match Google→Google and Outlook→Outlook. · notes/D29-D36_summary-notes.md:140–141
- Homework: set up the campaign, add B variants, upload leads, Loom of the build; research tracking and open-rate best practice. · notes/D29-D36_summary-notes.md:144–145
- Saffron map: Email 1 signal opener + S1 offer; 2–5 one proof point each (hours saved, AI-fluency evidence, replay, fairness); 6 options close; A/B "your interviews don't test AI use" vs "results in hours, zero interviewer time". · notes/D29-D36_summary-notes.md:148–152
- Learning guide D35 runbook contents: domains to buy, exact DNS, mailbox count and caps, day-by-day warm-up, one-click unsubscribe, monitoring checklist with "when a number goes red". Deliverable #7. · source/REF_learning-guide.md:1644–1668
- Learning guide D36: opener → problem/value → light proof → soft CTA; under 10 seconds to read; subject rules; soft beats hard; no demo ask in email 1. · source/REF_learning-guide.md:1690–1714
- Open questions already in the notes: tracking contradiction, "avoid software companies", LinkedIn first for 40 contacts. · notes/D29-D36_summary-notes.md:158–160
- Pre-send checklist for Deepu: separate domain, SPF/DKIM/DMARC, 3 weeks of warm-up, opt-out P.S., plain text, tracking off, Google→Google, MX check. · notes/D29-D36_summary-notes.md:165–173

---

## Where sources disagree with the class

1. **Health threshold.** Class: below 80% → pull and re-warm (source/X3_instantly-training.md:45–47). Instantly: aim above 90%, and an account is "ready" only above 90% after ≥2 weeks (help articles 13939939 and 13938078). Use 90%, not 80%.
2. **Per-mailbox daily cap.** Class: 50/day (D33 maths, X3:63–65). Instantly: 30 campaign + 10 warm-up (Campaign Options, Account Limits); AirMail at most 20; learning guide 20–30 (REF:1520). Redone at 30/day, the D33 example needs about 19 mailboxes, not 11–12.
3. **Slow ramp.** Class: 20 → 30 → 40 → 50 by week (X3:71–73). Instantly's Campaign Slow Ramp starts at 2/day and adds 2 a day (help article 10056946). The weekly ramp is a manual practice, not what the toggle does.
4. **Warm-up schedule and length.** Class: week-staged +1/10, +2/20, +3/30 over 3 weeks (X3:29,57). Instantly's UI has a single setting (default +1/day, limit 10, reply 30%) and says keep the defaults; bulk import caps the increment at 4. Readiness is ≥2 weeks (3 for AirMail), while the Instantly blog and the learning guide (REF:1602) say 4–6 weeks for brand-new domains. The instructor's staged values are his own ("this is just what works for me", X3:147).
5. **Tracking.** D33/X3 say always set up a custom tracking domain (X3 rule list); D35 says turn tracking off. Sources: tracking hurts or adds no value for cold email (Hunter +68% replies without open tracking; Apple MPP; Safe Links pre-clicking). A CTD only matters when tracking or links are on. Resolution in §3.
6. **Email Bison.** Class: "unlimited leads and emails, ~$600" (notes:66). Pricing page: $599/mo for 500,000 emails a month (extra in buckets); leads are unlimited.
7. **Instantly = single company only.** Class (notes:64, D03–D04:37). Instantly now has agency white-labelling, workspace groups and an Agency bundle; it targets agencies too.
8. **Alternate TLDs.** Learning guide suggests .co or .io (REF:1514). Instantly says .com works best and its DFY service only offers .com and .org (no .io or .ai).
9. **"Gmail permanently rejects mail without DMARC"** (REF:1568). Google requires DMARC only of bulk senders (5,000+/day to personal Gmail); since Nov 2025 non-compliant mail gets temporary or permanent rejections. Overstated for a low-volume sender, though DMARC is still free and recommended.
10. **"The rules apply to you regardless of volume"** (REF:1484). Partly true: the all-sender rules do; the bulk rules formally don't; and Google's requirements don't cover mail sent to Workspace accounts (Saffron's prospects).
11. **"2% bounce is a hard ceiling across Gmail/Yahoo/Microsoft"** (REF:1612). Not in any of the three published requirements. 2% is industry practice (Instantly's benchmark), and Instantly auto-pauses at about 5%.
12. **DMARC `pct`.** The class and Google's help page use `pct` for gradual rollout. RFC 9989 (May 2026) removed `pct`; use `t=y` for testing. Receivers may still honour `pct` for a while.
13. **Open-rate benchmark.** D21–D22 said email opens are 90%+ (notes/D21-D22:9). Instantly's 2026 average open is 27.7% (via lemlist) and Hunter's 30%, and both are inflated by MPP.
14. **Reply-To location.** X3 shows it under campaign settings (X3:127–131). In current Instantly it's an account-level setting (help article 6990255).
15. **Subsequences.** Taught as part of campaign setup (notes:95; X3:175–181). In Instantly they need Hyper Growth and only appear after launch, so they can't be built in a "configure, don't launch" homework or on Growth or the trial.
16. **A/B testing on small lists.** Class: two variants per email. Statistically, 40 leads (20 per variant) can't separate even a 3% vs 9% reply rate (about 240 per variant needed). Frame the B variants as message exploration, not a test.
17. **Pre-warmed accounts "make no sense".** Partly backed: you can't choose the domain and Instantly keeps ownership. But DFY (not pre-warmed) lets you pick brand-like .com names at $5/mailbox/mo, still owned by Instantly.
18. **Unsubscribe link vs opt-out P.S.** D31 prefers a plain P.S. over a footer link; X3 says always include the unsubscribe link. Both are compatible: CAN-SPAM accepts a reply-based opt-out, and Instantly's List-Unsubscribe header gives one-click without a visible link. Recommend P.S. plus header plus a postal address.
19. **SMTP port.** X3 says 587 is the default choice. Instantly's host table lists GoDaddy SMTP on 465 (SSL). Use whatever the provider documents.
20. **"Avoid software companies"** (notes:49). Lemlist reports SaaS reply rates often under 2%, which supports Yogesh's caution, but Saffron's ICP is by definition software teams. Not resolvable from sources; it needs Yogesh.

---

## Open questions I could not resolve

1. **Can a campaign be saved in Draft with zero connected mailboxes on the free trial?** The docs imply yes (errors only at launch) but don't say so. Test it in the trial before recording the Loom.
2. **Does Instantly's unsubscribe link or List-Unsubscribe URL use the custom tracking domain when tracking is off?** Not documented. This decides whether a CTD is needed for a no-tracking setup.
3. **Is Instantly's List-Unsubscribe header RFC 8058 compliant** (does it include `List-Unsubscribe-Post`)? Not stated. Check "Show original" on a real send later.
4. **CRM pricing** ($47/$97 two-tier vs $97 flat) and **bundle semantics** (do bundles replace separate outreach + credits subscriptions?). The help-center pages conflict.
5. **Whether A/B variants can be built on the trial at all.** The comparison table says "No"; untested.
6. **Positive-reply and meeting rates for engineering-leader or HR-tech audiences.** No primary benchmark found; Instantly's report has no industry breakdown.
7. **Official LinkedIn invitation limits.** LinkedIn's help pages don't publish a number.
8. **Exact Microsoft enforcement page text** (techcommunity post 4399730). The page wouldn't render; I relied on search snippets and Microsoft Q&A.
9. **Whether Postmaster Tools shows any data for a low-volume B2B sender** mostly mailing Workspace domains. Probably not, but not confirmed.
10. **DPDP applicability** when an India-based student processes US prospects' data without a contract with Saffron. The s.17(1)(d) exemption needs a contract; this is a legal question.
11. **Saffron's authorisation.** Whether Saffron's founders would approve a lookalike domain and sending in their name. Needed before any real send (CAN-SPAM header accuracy).
12. **Which trysaffron lookalike .com names are free.** Not checked; needs a registrar search.
