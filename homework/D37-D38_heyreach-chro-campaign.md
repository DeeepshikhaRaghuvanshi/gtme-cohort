# Homework (D37–D38): Saffron × CHROs: a HeyReach LinkedIn campaign

**For:** Deepu · **Due:** before the next class · **Rule from class:** configure everything in HeyReach, but **don't take it live**.

## What you're building, and why
Yogesh asked you to build a full outreach campaign for **Saffron targeting Chief Human Resources Officers (CHROs)**, run on LinkedIn through **HeyReach**. Everything else in your build so far targeted engineering leaders (CTO, VP Eng). The CHRO is a new buyer for Saffron with different pains:
- **Cost and time-to-hire:** engineering hires take weeks, and every loop costs engineer hours.
- **Fairness and consistency:** different interviewers score differently, which is a legal and DEI risk.
- **AI on take-homes:** candidates use ChatGPT, and nobody can tell how much.
- **Candidate experience and employer brand:** long processes lose good candidates.

Saffron's answer, in CHRO language: **one consistent, auditable technical assessment on the company's own codebase, scored the same way for every candidate, with results in hours and no engineer interview time.**

The class principles this applies:
- **Micro-campaigns, not mass AI personalization:** small segments, one message each, so you can see what works.
- **Segment by context (a situation or event), not by title.** Every person in these campaigns is a CHRO; the segment is *what's happening at their company*.
- **LinkedIn first:** about 30% replies versus 1–4% for email, and your list is small (D33–34: under ~2,000 leads, lead with LinkedIn).
- **Safe limits:** at most **25 connection requests and 40 messages a day** per LinkedIn account; about **750 requests a month, split across 4 campaigns**.
- **Placeholders: first name and company only.** Short messages, no "book a meeting" ask, and an easy way out.

> Ethics note: Saffron hasn't hired you. This is a portfolio exercise, so keep it in draft. If you ever run it for real, it has to be with Saffron's approval, sent as Saffron or on their behalf.

## Part 1: Your LinkedIn profile, before anything else (20 min)
Prospects look you up before they accept a request. Yogesh's checklist:
1. **Photo:** clear, professional, face visible.
2. **Headline:** say what you do, e.g. *"GTM Engineer · outbound systems with Clay, data pipelines & AI · ex-full-stack"*.
3. **About:** 3–4 lines on the problems you solve (finding the right accounts, enriching and qualifying them, running signal-based outreach), plus your engineering background.
4. **Education** filled in.
5. **Featured:** pin the credit-efficiency LinkedIn post once it's live (that's also your thought-leadership start). Buffer can schedule future posts (about $23 a month), but it's optional.

## Part 2: Build the CHRO list in Clay (30 min, about 3–5 credits)
You already have 30 qualified Saffron companies in Clay (workbook **Saffron | Qualified Pipeline**, table `saffron_50_accounts`, Outreach Eligibility = Outreach). Add their people leaders:

1. In `saffron_50_accounts`, go to **Tools → Enrich → "Find people at company" (Surfe, 0.1 credits per person)**. It's the same enrichment we used for the engineering leaders.
2. **Company domain:** Clean Domain.
3. **Job titles** (small companies rarely use the word "CHRO"):
   - Chief Human Resources Officer
   - CHRO
   - Chief People Officer
   - VP People
   - VP Human Resources
   - Head of People
   - Head of HR
   - Director of People
4. **Seniorities:** C-Level, VP, Head, Director. **Limit: 1** (one people leader per company).
5. **Auto-run off.** **Run condition:** `{{Outreach Eligibility}} == "Outreach"`. Use the `/` menu to insert the column. Then check the preview shows "Will run" only on Outreach rows.
6. Test on 10 rows, check the titles are really HR or people leaders, then run the rest.
7. Click a result cell → **"Write each item to new row in other table"** → new table **"Saffron CHROs"**. Carry over: Company Name, Clean Domain, Employee Count, Industry, Jobcount, Tools, Staffing Summary. Auto-run off.
8. In "Saffron CHROs": pull out **Full Name, First Name, Job Title, LinkedIn URL** with *Add to column* (free). Keep only rows with a LinkedIn URL, since HeyReach works from LinkedIn profiles.
9. Add a free formula column **Segment**. Paste this description into Clay's formula helper:
   > If Industry contains "Financial" or "Health", return "Regulated". Otherwise, if Tools is not empty, return "AI-in-JDs". Otherwise, if Jobcount is 10 or more, return "Hiring surge". Otherwise return "Growing team".
10. Export to CSV: **Tools → Export → Download CSV**.

Expect roughly 20–30 people, so each campaign gets 5–8. That's right for a portfolio test. At real scale, the same structure takes the full ~750 requests a month.

**Exclusion list:** before importing, remove competitors (HackerRank, CodeSignal, Rounds.so, CoderPad, Karat, HackerEarth, micro1) and anyone already contacted. Class rule: refresh exclusion lists with the client every week.

## Part 3: The four micro-campaigns

| # | Campaign (segment) | Who | The "why now" |
|---|---|---|---|
| 1 | **Hiring surge** | 10+ open engineering roles | Dozens of interview loops coming |
| 2 | **AI-in-JDs** | Job ads mention Cursor, Claude Code or Copilot | They want AI fluency but probably can't test it |
| 3 | **Regulated** | FinTech or HealthTech | Fair, auditable hiring decisions matter more |
| 4 | **Growing team** | 5–9 open engineering roles | Engineer interview hours are the hidden cost |

### The sequence (same shape for all four)
1. **Day 0:** view profile.
2. **Day 0:** follow (optional; it warms them up).
3. **Day 1:** connection request. **Send it without a note** unless you have LinkedIn Premium or Sales Navigator. Free accounts can add notes to very few invitations a month, so check yours.
4. **If accepted:** wait 1 day, then **Message 1** (segment-specific, below).
5. **No reply after 3 days:** **Message 2** (proof).
6. **No reply after 5 more days:** **Message 3** (options close).
7. **Not accepted within ~2 weeks:** end the sequence for that person (withdraw the request if HeyReach offers it).

### Message 1, one per campaign (keep each under ~300 characters)
**1 · Hiring surge**

---

Thanks for connecting, {first_name}. {company} is hiring a lot of engineers right now. How is your team keeping technical interviews consistent across that many loops without burning out the engineers who run them?

---

**2 · AI-in-JDs**

---

Thanks for connecting, {first_name}. I noticed {company}'s engineering roles ask for experience with AI coding tools. How are you checking that in interviews today? Most processes I see still ban AI in the technical round.

---

**3 · Regulated**

---

Thanks for connecting, {first_name}. In teams like {company}'s, I hear a lot about keeping technical hiring fair and auditable, especially now that candidates use AI on take-homes. How are you handling that today?

---

**4 · Growing team**

---

Thanks for connecting, {first_name}. As {company} grows its engineering team, roughly how many hours a week do your engineers spend interviewing? Most people leaders I talk to want that time back.

---

### Message 2, proof (shared; add one segment line if you like)

---

One pattern I'm seeing: teams replace the take-home and first technical round with a short build on their own codebase, scored the same way for every candidate. Saffron (YC) does this with AI reviewers and a full replay of how the candidate worked, so results come back in hours with no interviewer time. Would that be useful at {company}?

---

### Message 3, options close (shared)

---

Last note from me, {first_name}. If it isn't a priority, is it timing, budget, or just not relevant for {company}? A one-word reply helps me a lot.

---

## Part 4: Set it up in HeyReach (without going live)
HeyReach screens change, so look for the closest match and screenshot anything unclear.
1. **Account:** sign up and check whether there's a free trial before paying; ask Yogesh which plan the class uses. **Connect your own LinkedIn** as the sender, then set the daily limits to **25 connection requests** and **40 messages**.
2. **Lead lists:** create 4 lists, one per segment. Import from your CSV (filter it by Segment first). Map **LinkedIn URL**, **First Name** and **Company Name**.
3. **Campaigns:** create 4 campaigns, one per list. Build the sequence above with its conditions and delays, and paste the messages using HeyReach's variable buttons for first name and company.
4. **Name them clearly,** e.g. `Saffron · CHRO · Hiring surge · v1`, so results are easy to compare later.
5. **Save as draft / don't start.** That's the class instruction for this week.
6. **Screenshot** each campaign's sequence and lead count, and add them to your Drive folder (Build Evidence) for the review and your portfolio Loom.

## Part 5: Before next class
- [ ] Profile updated (photo, headline, About, education)
- [ ] "Saffron CHROs" table built, with Segment, and the CSV exported
- [ ] 4 lead lists + 4 campaigns configured in HeyReach, **not live**
- [ ] Screenshots saved
- [ ] Watched last week's recordings (D29–D36 notes are in Drive → Session Notes), paying particular attention to how targeting and segmentation were done
- [ ] Questions ready for Yogesh:
  - Which HeyReach plan or trial does the class use?
  - Connection notes on or off?
  - For Saffron's 30 accounts, is it OK to go CHRO-first, or should the engineering leaders come first?

## How you'll measure it (once it's live, later)
- **Acceptance rate per campaign** (the class benchmark is ~70%), **reply rate** (~30%) and **positive replies**.
- Compare the four segments after 2–4 weeks, keep the winner, and rewrite the weakest. Yogesh: results show within about a month; getting it right takes 2–3 months of iteration.
