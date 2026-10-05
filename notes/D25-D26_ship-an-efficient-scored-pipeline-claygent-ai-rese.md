# D25-D26: Ship an efficient scored pipeline + Claygent — AI research at scale (2026-09-24)

## TL;DR
- Yogesh's core rule: qualification signals are usually *enough* — don't stack disqualification signals just because "the industry says so"; check TAM size first, because in a small market signals just disqualify companies you can't afford to lose.
- Live build: the cohort built a Clay prospecting table for a real company, **Lantern AI** (YC, AI hiring manager/staffing platform), targeting Germany/Netherlands software companies.
- Qualification logic converged on two signals: (1) job postings open >30 days (proxy for hiring pain) and (2) company has an internal recruitment/HR team of 1+ (proxy for "would buy a tool" vs. "relies on an agency").
- Gagan's cautionary tale: Claygent gave contradictory/fabricated compliance data (SOC2/HIPAA) across runs; the fix was a manual formula cross-checking evidence fields rather than trusting the AI's true/false verdict directly.
- Common Claygent failure mode demoed live: deleting a column's JSON schema/fields when editing a prompt silently breaks the output — always regenerate the schema from the prompt after editing.

## Key concepts
- **Qualification vs. disqualification logic**: build one clear rule ("qualify when X AND Y, else disqualify") rather than an unstructured pile of signals. Yogesh's rule for Lantern: qualify if job postings open >30 days AND recruitment/HR team size ≥1; disqualify otherwise (00:44:35, 01:06:13).
- **Signal strategy is downstream of TAM**: if the addressable market is small, don't add disqualifying signals — you can't afford to filter out real prospects (00:02:22–00:04:10).
- **Hooks vs. qualification**: qualification signals decide *who* to target; hooks (funding news, M&A, product launches, market expansion) are separate — they feed messaging, not targeting (00:08:58–00:10:01).
- **Claygent reliability**: it's an LLM with real limitations — it can produce inconsistent answers to the same question across runs, especially on judgment calls like compliance status (00:10:01).

## Tools shown & how they were used (with timestamps)
- **Google Sheets manual formula** (00:05:08–00:07:47): Gagan pulled AI-generated compliance "evidence" text into a sheet and wrote a formula checking for keyword mentions (SOC2/HIPAA/ISO) directly in the evidence, instead of trusting Claygent's own true/false/medium compliance flag — because the flag and the evidence text contradicted each other. Result: 32/50 companies flagged compliant by formula vs. Claygent's own inconsistent flag.
- **Clay — Search Filters / company search** (00:21:33–00:30:41): Neeraj/Gagan built a new Clay workbook, filtered by industry (Software Development, IT Services), country (Germany, Netherlands — chosen to avoid US competition), company size (51–200 and 200–500 employees), and funding raised ($1–5M, $5–10M). Annual revenue and company-type filters were tested and then removed because they narrowed results too much on Clay's free plan.
- **Claygent column — job posting duration check** (00:32:39–00:40:19): Prompt checks, per company domain, whether job postings have been open >30 days. Ran on a 10-row test first. Output fields: job title, posted date, open status.
- **Find Contact at a Company enrichment** (00:37:46–00:41:31): used to size each company's HR/recruitment team — filtered by job function = "Human Resources and Recruitment," identifier = company domain, output = people count. Revealed some companies (e.g., TL;DV) have zero recruitment headcount, meaning they'd rely on an agency rather than buy Lantern.
- **Claygent qualify/disqualify column** (00:44:35–01:02:09): a single AI-response column that takes the earlier job-posting output plus the Find Contacts output and outputs "Qualify"/"Disqualify" plus reasoning, open-role duration, and a one-line HR team summary.
- **JSON Schema "Generate from Prompt"** (00:46:49–00:49:41): regenerates the column's output schema/fields directly from the prompt text — the fix for when someone accidentally deletes fields while editing.
- **Model picker — OpenAI GPT-5 mini** selected for the qualify/disqualify Claygent column (00:48:23), with Yogesh's framing: "these kinds of things are easy on ground because you can use GPT ... and it's not going to cost you anything" — i.e., default to a cheap, fast model for a yes/no + short-summary task.
- **Find Active Job Postings enrichment (LinkedIn-scraping-based)** (01:02:40–01:06:13): a non-Claygent, provider-based job-posting enrichment that Yogesh judged as *more reliable* than the Claygent job-posting prompt ("this uses LinkedIn scraping that's why it's giving better data").

## Clay build steps demonstrated (numbered, reproducible)
1. New Clay workbook → new table → "Find companies" via Search Filters.
2. Set Industry = Software Development / IT Services.
3. Set Country = Germany, Netherlands (deliberately avoiding the saturated US market).
4. Set Company size = 51–200 and 200–500 employees (11–50 was rejected: too small to afford a ~$10k/year hiring tool since they barely hire).
5. Add Funding raised filters ($1–5M, $5–10M); test and drop Company Type / Annual Revenue filters if they overly narrow results on the free plan.
6. Save and run on 10 rows first; delete unneeded default enrichment columns before adding your own.
7. Add a Claygent column referencing company domain: prompt = "check if job postings are open for more than 30 days." Save, test on 10 rows.
8. Add a Find Contacts column: job function = HR/Recruitment, identifier = company domain, output = people count. Test on 10 rows.
9. Add a qualify/disqualify Claygent column that consumes both prior outputs: prompt states the rule explicitly ("qualify when job posting open >30 days AND HR team has 1+ person, else disqualify"), select model (GPT-5 mini used here), click "Generate JSON Schema from prompt" (critical if you've hand-edited the prompt), save, run on 50 rows.
10. Add a job-posting enrichment (LinkedIn-scraping-based provider, not Claygent) as a cross-check/alternative to the Claygent job-posting prompt; compare quality.
11. (Homework, not yet built) Add a formula column: `job_count >= 10` → qualified, to replace the "30 days" heuristic with a volume-based one at the 50-row/territory-build stage.

## Instructor rules, opinions & decisions
- Qualification signals alone are sufficient if the TAM is small — stacking more signals only shrinks your pool (00:02:22–00:04:10).
- Recent funding (<12 months) is a weak/unreliable signal for security/AI software targets; prefer leadership hires (CEO, CTO, VP Eng, Director, Security) as a compliance-readiness proxy instead (00:06:29).
- Never delete a column's fields/JSON schema without regenerating — Yogesh flagged this live as "the fun mistake you did... you should never do this" (00:48:23).
- Company-size targeting should reflect ability to pay: 11–50 employee companies were excluded from Lantern's ICP because they hire too rarely to justify a ~$10k/year hiring tool.
- Role-type matters as much as company-size: care manager/customer-support roles (India ~₹30k/mo) and sales-exec roles (₹4–5 LPA) are too low-value to justify an expensive quality-of-hire tool, even if job postings are open and there's an HR team; technical/high-paying roles (QA engineer, BI dev manager, paid media account manager) are the right qualification target because *quality* of hire, not speed, is what buyers of Lantern care about (00:52:09–00:59:09).
- Companies with zero recruitment team are disqualified — they rely on agencies, and agencies partner with tools like Lantern rather than buying them directly (00:41:31–00:43:20).
- Claygent should not be trusted blindly for judgment calls (e.g., compliance); cross-check with a deterministic formula against the raw evidence text.

## Assignments / homework given
- [Gagan] Redo the Lantern Clay table with correct qualify/disqualify logic; preserve the AI response parameters/JSON schema (don't delete output fields).
- [Whole group — Medha, Neeraj, Gagan] Build a full Lantern company-qualification table: research Lantern's actual website/ICP, pick a territory (Germany, Netherlands, or one of their choosing), and encode qualify/disqualify logic (job posting >10 rule + recruitment-team check). Suggested to use Claude for help structuring it.
- [Yogesh] Will build his own reference version of the Lantern table over the weekend and share it as the ideal-format example.

## Deepu's questions & the answers she got
Deepshikha spoke once, early in the session (00:12:20): she said she'd missed Yogesh's question because she was commuting and joined by phone, and asked him to repeat it. Yogesh then asked Neeraj to share his screen instead so the live build could continue. She did not ask a substantive question in this session.

## What this means for the Saffron build
- Saffron's targeting logic should follow the same qualify/disqualify shape as Lantern: pick 1–2 structural signals that genuinely gate willingness/ability to buy (e.g., "actively hiring engineers" + "uses an AI coding tool in the hiring loop"), rather than a long signal stack.
- Given Saffron evaluates how engineers use AI coding tools in hiring, a Claygent research prompt is a natural fit for detecting "does this company's engineering hiring process mention AI coding tools / take-home assessments" — but per Gagan's experience, cross-check any yes/no verdict against the raw evidence text with a formula before trusting it at scale.
- Company-size / role-type filtering matters: for Saffron, exclude companies too small to have a dedicated technical hiring process, and focus qualification on roles/teams where hiring quality (not speed) is the buyer's stated concern — directly analogous to the Lantern care-manager-vs-QA-engineer distinction.
- Before scaling any AI-judgment column, test on 5–10 rows, regenerate the JSON schema after any prompt edit, and default to a cheap model (GPT-5 mini/Helium-equivalent) for simple qualify/disqualify decisions to control credit spend.

## Resources mentioned
- Lantern AI (trylanternai — YC company), its website, FAQ page, and YC page — used as the live research subject.
- No external reading/links were shared in this session (contrast with the two skills sessions, which had reading lists).
