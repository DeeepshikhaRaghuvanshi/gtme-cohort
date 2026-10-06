# Verification: Claude × Gemini cross-check (6 Oct 2026)

Inputs: `brief.md` → `claude-findings.md` (Claude Opus, 161 cited findings) and `gemini-findings.md` (Gemini 3.1 Pro High via agy, ~70 findings, mostly cited to bare domains). Then `gemini-review-of-claude.md` (Gemini 3.1 Pro reviewing Claude's findings adversarially), plus my own spot checks of each high-impact claim against the primary page with WebFetch.

Status key: **AGREED** (both tracks, or one track plus my primary-source check) · **RESOLVED** (the tracks conflicted; the primary source decided) · **FLAGGED** (unverified; the guide tells Deepu to check it in the tool).

## Instantly product
- **Outreach pricing: Growth $47 (5,000 emails, 1,000 contacts), Hyper Growth $97, Light Speed $358.** RESOLVED. Gemini said Hyper Growth = 100k emails; the pricing page (fetched) says **125,000**. Claude was right.
- **Free trial: 14 days, no card, 2 accounts, 250 leads, 1,000 emails; an un-upgraded account is deleted at the end.** AGREED (Claude + my fetch of help 13941298). Gemini had the 14 days but missed the limits and the deletion.
- **A/Z testing not on the trial.** RESOLVED → "No". Gemini's review claimed the trial includes A/Z, citing the free-trial article, but that article doesn't mention A/Z at all (fetched). The plan-comparison table (help 7920548, fetched) says Trial A/Z = **No**. The guide gives a trial route and a Growth route, plus "if Add variant works, use it".
- **Subsequences need Hyper Growth and appear only after launch.** AGREED (Claude; plan table fetched: Trial No, Growth No, Hyper Growth Yes; Gemini's review accepted it).
- **A campaign can be built and saved as a draft with no mailbox.** FLAGGED (medium). Both tracks infer it from the docs: the errors only occur at launch (help 7907713, 6222212). It hasn't been tested, so Step 8 of the guide tells Deepu what to do if it fails.
- **Campaign Options names and the recommendation of 30 campaign + 10 warm-up per mailbox a day.** AGREED (Claude + my fetch of help 6222396).
- **Stop on auto-reply.** RESOLVED. Gemini's review raised it; its description was muddled, but it pointed at a real gap. Help 9713093 (searched): unchecking "Stop on auto-reply" plus auto-tagging enables AI Smart Pause (pause until the return date, then resume). The guide now says OFF + Smart Pause.
- **Health score: ready at >90% after ≥2 weeks; Campaign Slow Ramp +2/day.** AGREED (Claude; Gemini's review accepted it). Conflicts with the class's 80% and 20/30/40/50, which the guide shows side by side.
- **DFY / pre-warmed: Instantly keeps domain ownership.** AGREED (Claude; Gemini's review accepted it).
- **Variable tokens `{{firstName}}`, `{{companyName}}`, `{{personalization}}`.** AGREED (my search: Instantly blog + third-party docs). The help article doesn't spell them out, so the guide says to insert them with the Variables button.
- **"Duplicate campaign".** FLAGGED: not documented in the help center; the guide says "if you see a Duplicate option".
- **CSV headers limited to 20 characters.** Claude only (help 6254215). Accepted; the guide exports a trimmed column set.

## Deliverability rules
- **Google's requirements don't apply to mail sent to Workspace accounts.** AGREED (verbatim on support.google.com/a/answer/14229414, fetched). Gemini's review called this "dangerously overstated" as advice. Fair point, and already handled: the guide says to treat the rules as the minimum because Workspace and gateways still filter.
- **Gmail enforcement since Nov 2025: temporary and permanent rejections.** AGREED (same page, fetched).
- **RFC 9989 (May 2026) obsoletes RFC 7489 and removes `pct`, adding `t=y`.** RESOLVED. Gemini's review said `pct` is only "deprecated"; the RFC itself (fetched) lists "Removal of the 'pct' tag" in Appendix A.6. The guide says removed, and that existing records keep working in practice. Gemini's two cited URLs (mxtoolbox / dmarcwise "rfc-9989" pages) weren't verifiable.
- **Thresholds: complaints <0.3% (aim <0.1%), bounces <2% (industry practice), Instantly auto-pause ~5%.** AGREED (Gemini + Claude; Google page).
- **Microsoft 5 May 2025 rules and the 550 5.7.515 error.** AGREED by both tracks, medium confidence (the Microsoft page wouldn't render for Claude; snippets + Microsoft Q&A).
- **Lookalike .com, ~3 mailboxes per domain.** AGREED (class + both tracks).
- **Saffron cost estimate.** RESOLVED. Gemini said ~$30/mo infrastructure (excluding Instantly); Claude said ~$64–81/mo including Instantly Growth. The guide uses ~$75–81/mo for 4 mailboxes + Instantly, which is consistent with both once you include the $47 plan.

## Tracking
- **Apple MPP inflates opens; security gateways pre-click links.** AGREED. Gemini's review rightly separated the two mechanisms (MPP = opens, gateways = clicks); the guide's A7 already separates them.
- **Hunter 7.4% vs 4.4% reply rates with open tracking off/on.** AGREED (Claude cited; Gemini's review accepted it). Labelled as vendor data and correlational.
- **D33 vs D35 resolution: tracking off, CTD optional insurance.** AGREED (both tracks reached the same synthesis independently).

## Copy and benchmarks
- **Instantly 2026 benchmark: 3.43% average reply rate; 58% of replies from step 1; under 80 words.** Claude only, from Instantly's report. Gemini also had "Instantly's average ~3.4%". AGREED.
- **A/B sample size: ~750 per variant for 3% vs 6%; ~12,100 for a 20% lift.** AGREED (Claude's maths; Gemini's review accepted it). Gemini's own "200+ per variant" is too low; the guide uses Claude's figures.
- **Gong interest-CTA study; Ashby's 23.3 interview hours per technical hire; HackerRank's 76%.** Claude only, cited to primary pages; Gemini's review accepted Ashby. Used in the copy with their sources noted in the guide.
- **Gemini's "60–80% fraud rate in unmonitored take-homes".** REJECTED: from a vendor blog (fabrichq), unsupported. Not used.

## Compliance
- **CAN-SPAM: postal address, opt-out within 10 business days, reply-based opt-out allowed, no B2B exemption.** AGREED (both tracks; FTC guide).
- **CASL consent; Germany UWG §7; UK PECR corporate subscribers.** Claude only, cited to the statute or regulator pages. Gemini had CASL and GDPR. Accepted.
- **DPDP Act.** RESOLVED. Gemini said "Saffron is in India", which is **wrong**: Saffron is in San Francisco, and only the student is in India. Claude's version (core duties from May 2027; s.17(1)(d) contract exemption) is used.

## Where the class disagrees with sources
Both tracks independently flagged: 50 vs 30 emails a day, the tracking contradiction, "avoid software companies", and LinkedIn-first for small lists. Claude added 16 more (A10 of the guide). Gemini argued that email micro-campaigns are viable even under 2,000 leads; the guide keeps Yogesh's LinkedIn-first order for a real launch and builds the email side for the homework.

## Still open (flagged in the guide)
1. Can a draft be saved with no mailbox on the trial? (Test in Step 8.)
2. Does "Add variant" really not work on the trial? (Catch 1.)
3. Does Instantly's List-Unsubscribe header include the RFC 8058 `List-Unsubscribe-Post`? (Only matters when live.)
4. Is the "Duplicate campaign" option available? (Step 9.)
5. Saffron's approval and postal address before any real send.
