"""Course content for "GTM Engineering, from zero: the Saffron course" (v3).

Each scene: kind, module (0-8), eyebrow, title, items (visual elements revealed one per beat), beats (narration per beat).
Beat i shows the scene's visual state i. Narration is written for Piper TTS: acronyms spelled with spaces.
Kinds: title, chapter, bullets, diagram:<name>, shots, tip, real, mistake, quiz, recap.
"""

MODULES = [
    "Start", "Foundations", "Strategy", "Data", "Clay", "Signals & AI",
    "Data out", "Sending", "Career",
]

S = []


def scene(kind, module, eyebrow, title, items, beats, **kw):
    S.append(dict(kind=kind, module=module, eyebrow=eyebrow, title=title, items=items, beats=beats, **kw))


# ───────────────────────────── 0 · START ─────────────────────────────
scene("title", 0, "A COURSE IN 8 CHAPTERS · DAYS 1–36", "GTM Engineering, from zero",
      ["The Saffron course"],
      ["Welcome. This is the whole G T M engineering course so far, days one to thirty six, rebuilt as one guided course. "
       "You'll learn every idea from class, plus the tips and traps we hit while building a real pipeline for Saffron, your portfolio company."])

scene("bullets", 0, "HOW THIS WORKS", "One brief, eight chapters",
      ["The brief: who will buy this quarter, and who do we talk to?",
       "Each chapter answers part of it, using real Saffron screenshots",
       "Watch for: Pro tips · In the real world · Common mistakes",
       "Quick checks: pause the video and answer before the reveal"],
      ["Here's the story. You've just joined Saffron as its first G T M engineer, and the founders give you one brief: "
       "find the companies most likely to buy from us this quarter, and the right person to talk to at each one.",
       "Each chapter answers part of that brief, and every step is shown with real screenshots from the build.",
       "Along the way you'll see three kinds of cards: pro tips from class, real world scenarios, and common mistakes to avoid.",
       "And every so often there's a quick check. When you see one, pause the video and answer it before the reveal."])

# ───────────────────────────── 1 · FOUNDATIONS ─────────────────────────────
scene("chapter", 1, "CHAPTER 1 · DAYS 1–4", "Foundations",
      ["What a GTM engineer actually does", "The revenue funnel and where it leaks",
       "The seven-layer map of the whole course"],
      ["Chapter one. Foundations. What the job really is, how revenue flows, and the map that the rest of the course follows."])

scene("bullets", 1, "DAYS 1–2 · THE ROLE", "What a GTM engineer does",
      ["GTM = go-to-market: everything a company does to win customers",
       "GTM engineer: builds the systems that turn strangers into pipeline",
       "Not RevOps (reports on the pipeline) · not an SDR (works the list)",
       "Measured on pipeline generated, not tools operated"],
      ["G T M means go to market: everything a company does to find customers and turn them into revenue.",
       "A G T M engineer builds the systems that do that at scale: finding the right companies, spotting why they need you now, "
       "finding the right person, and handing a qualified list to sales or to an outreach tool.",
       "It's often confused with two other roles. Rev Ops looks backward and reports on the pipeline. An S D R works the list and has the conversations. "
       "The G T M engineer builds the machine that produces the list in the first place.",
       "And the measure of the job is pipeline generated, not how many tools you can operate. "
       "In class, today's work was described as about ninety percent outbound, with data being eighty percent of the effort."])

scene("diagram:funnel", 1, "DAYS 1–2 · THE FUNNEL", "How a stranger becomes revenue",
      ["Unknown", "Lead", "MQL", "SQL", "Opportunity", "Closed"],
      ["Every customer moves through a funnel. It starts with unknown: every company in the market that has never heard of you.",
       "A lead is a person you know about.",
       "A marketing qualified lead, or M Q L, looks like a good fit, or has shown interest.",
       "A sales qualified lead, or S Q L, is someone sales agrees is worth a real conversation.",
       "An opportunity is an active deal with a dollar value.",
       "And finally, closed: won or lost. Here's why the G T M engineer matters. Losses compound. "
       "If half the people drop out at each of four steps, only about six percent are left. Every leak at the top costs you everything below it."])

scene("diagram:layers", 1, "DAYS 3–4 · THE MAP", "The seven layers",
      ["L1 Data & sourcing", "L2 Enrichment", "L3 Signals & intent", "L4 Orchestration",
       "L5 Execution", "L6 CRM & reporting", "L7 AI & agents"],
      ["Days three and four gave the map for the whole course: seven layers. Layer one, data and sourcing: where prospects come from, using tools like Apollo, Prospeo and LinkedIn Sales Navigator.",
       "Layer two, enrichment: turning a name into a verified email and useful facts. This is where Clay lives.",
       "Layer three, signals and intent: the why now.",
       "Layer four, orchestration: moving data between tools with things like n8n and webhooks.",
       "Layer five, execution: the outreach itself, with tools like Instantly and HeyReach.",
       "Layer six, the C R M and reporting: the source of truth, like HubSpot or Attio.",
       "And layer seven, A I and agents: Claude, Claude Code and Clay's own A I researcher, which multiply everything else."])

scene("tip", 1, "PRO TIP", "Value is lost at the handoffs",
      ["A perfect list that never reaches the outreach tool is worth nothing",
       "When something breaks, ask: which layer, and which handoff?"],
      ["The most important idea from day three: value is created inside each layer, but it's lost at the handoffs between them. "
       "A perfect enriched list is worthless if it never reaches the outreach tool.",
       "So when something breaks in a real job, don't start by blaming the copy. Ask which layer failed, and which handoff."])

scene("bullets", 1, "DAY 4 · YOUR WORKSPACE", "Set up like a professional",
      ["A dedicated email and browser profile for all GTM tools",
       "Free tiers first: Clay, Prospeo, Apollo, Claude",
       "Data vendors reject Gmail sign-ups → a company domain fixes it",
       "LinkedIn and Loom stay on your real account"],
      ["Day four was about the workspace. Use a dedicated email and browser profile for all your G T M tools, so credits, trials and cookies never mix with personal accounts.",
       "Start on free tiers: Clay, Prospeo, Apollo and Claude are enough to learn everything in this course.",
       "One thing we hit straight away: data vendors like Apollo and Ocean dot I O reject Gmail sign ups. A cheap company domain with its own mailbox fixes that, and it teaches you the email setup you'll need later anyway.",
       "But identity platforms stay on your real account. LinkedIn allows one profile per person, and your posts and connections only matter on your own profile."])

scene("recap", 1, "CHAPTER 1 · RECAP", "Foundations in four lines",
      ["GTM engineers build the machine that produces pipeline",
       "Losses compound down the funnel, so fix leaks at the top",
       "Seven layers; value is lost at the handoffs",
       "Dedicated workspace; real identity for LinkedIn"],
      ["Chapter one in four lines. G T M engineers build the machine that produces pipeline. Losses compound, so fix leaks at the top. "
       "Seven layers, and value is lost at the handoffs. And a dedicated workspace, with your real identity for LinkedIn."])

# ───────────────────────────── 2 · STRATEGY ─────────────────────────────
scene("chapter", 2, "CHAPTER 2 · DAYS 5–10", "Strategy before tools",
      ["Adopt one company and define its ideal customer", "Size the market: TAM, SAM, SOM",
       "Signals, the offer, and the one-page brief"],
      ["Chapter two. Strategy before tools. In class this was repeated again and again: Clay exists to execute a strategy document, not to be explored feature first."])

scene("bullets", 2, "DAYS 5–6 · ADOPT A COMPANY", "Saffron, your portfolio company",
      ["YC Spring 2026 · AI-native technical interviews",
       "Candidates build a real feature with Claude Code; AI reviewers score how",
       "$199–$499 a month, paid by card",
       "Price tells you the buyer: one leader can say yes"],
      ["Every project in this course targets one real company, so your portfolio tells one coherent story. You picked Saffron, from the Y C startup directory.",
       "Saffron runs technical interviews for the A I era. A candidate builds a real feature in the hiring company's own codebase with Claude Code, "
       "and more than ten A I reviewers score how they worked, including how they used A I.",
       "It costs two hundred to five hundred dollars a month, paid by card.",
       "And that price is a clue. It tells you the buyer is a company small enough that one engineering leader can say yes, with no procurement process."])

scene("bullets", 2, "DAYS 5–6 · THE ICP", "Who exactly is the customer?",
      ["ICP = ideal customer profile: the company that gets the most value",
       "Firmographics · technographics · situation",
       "Saffron: US tech, 50–500 people, hiring engineers",
       "Decision maker signs (CTO, VP Eng) · champion pushes (EM, recruiter)"],
      ["The I C P, or ideal customer profile, describes the company that gets the most value from the product.",
       "It has three kinds of facts. Firmographics: size, industry, location, funding. Technographics: the software they use. And situation: what's happening there right now.",
       "For Saffron: US tech companies of fifty to five hundred people that hire engineers regularly.",
       "Inside each company there are two people. The decision maker, a C T O or V P of engineering, signs. "
       "The champion, an engineering manager or recruiter, is the one grading take home tests at midnight, and will push for the tool."])

scene("tip", 2, "PRO TIP · FROM CLASS", "Search like a GTM engineer",
      ["Keep title keywords and seniority as separate filters",
       "Always add exclude keywords (\"production\" when you mean \"product\")",
       "Tight beats broad: you can always widen later"],
      ["Three search habits from day six. Keep title keywords and seniority as separate filters. Search engineering plus seniority V P, never the string V P of engineering.",
       "Always add exclude keywords. The class example: exclude production when you're searching for product, or you'll get factory managers.",
       "And tight beats broad. A narrow I C P lets you write sharper messages and waste fewer credits. You can always widen later."])

scene("diagram:tam", 2, "DAYS 7–8 · MARKET SIZING", "TAM, SAM, SOM",
      ["TAM", "SAM", "SOM"],
      ["Before building any list, you size the market, because a founder or investor will ask. Three nested numbers. "
       "T A M, the total addressable market: every company that could ever buy, in principle.",
       "S A M, the serviceable addressable market: the part you can actually serve, given your product, geography and price.",
       "S O M, the serviceable obtainable market: the slice you can realistically win in the next year. "
       "It's partly a filter, and partly an argument you write down. A G T M engineer doesn't guess these on a slide. You apply filters in a data tool, and read the count."])

scene("shots", 2, "DAYS 7–8 · SAFFRON'S NUMBERS", "From 54,000 to 2,921",
      [("02-tam-filters.png", (0, 0, 300, 340), "TAM ≈ 54,000"),
       ("03-sam-filters.png", None, "SAM ≈ 12,000"),
       ("04-som-filters.png", (0, 445, 262, 895), "SOM = 2,921")],
      ["Here's Saffron in Prospeo. Tech, fintech and health companies of fifty to five thousand people, in the US, Canada and Western Europe: about fifty four thousand companies. That's the T A M.",
       "Adding at least twenty engineers and a growing headcount cut it to about twelve thousand, and removed the hospitals the healthcare filter had pulled in. That's the S A M.",
       "Then US only, fifty to five hundred people, founded after twenty twelve: two thousand nine hundred and twenty one companies. "
       "Each count goes into the strategy doc as a screenshot. Clients want evidence, not claims."])

scene("bullets", 2, "DAY 8 · WHY NOW", "Signal, intent, trigger",
      ["Signal: a public fact about the company (12 engineering jobs open)",
       "Intent: a person engaging with you (visited your pricing page)",
       "Trigger: the action you take in response",
       "Rank signals by how cheap they are to detect"],
      ["Knowing who could buy isn't enough. You need to know who needs Saffron now. A signal is a public fact about a company. "
       "If it's posting twelve engineering jobs, it faces dozens of interviews in the coming months: exactly the pain Saffron removes.",
       "Intent is a person doing something toward you, like visiting your pricing page or liking the founder's post. It's the warmest kind, but it needs tools like R B two B, which only works in the US for privacy reasons.",
       "A trigger is what you do in response.",
       "And rank your signals by how cheap they are to detect. Job posts are cheap. Website visitors need a paid tool. Always start with the highest intent signal you can detect cheaply."])

scene("mistake", 2, "COMMON MISTAKE", "Reciting the signal back",
      ["“We saw you raised funding…” sounds like surveillance",
       "Use signals as context for the message, not as the message",
       "Verify first: one class signal belonged to a subsidiary"],
      ["A common mistake: reciting the signal back. Opening with we saw you raised funding sounds like surveillance, and everyone else is sending it too.",
       "Use the signal as context for why the message matters now, not as the message itself.",
       "And verify it first. In class, a recent funding signal turned out to belong to an acquired subsidiary, not the target company. One wrong fact and the email is dead."])

scene("bullets", 2, "DAYS 9–10 · THE OFFER", "Value → pain → proof",
      ["Value: the outcome, in the buyer's words",
       "Pain: the problem they already feel",
       "Proof: a number, a similar customer, a credential",
       "Five-word test: “Your engineers ship with AI. Your interviews don't test it.”"],
      ["Days nine and ten turned all this into an offer. A good offer has three parts. Value: the outcome, in the buyer's words, not your feature list.",
       "Pain: a problem the buyer already feels. You're not convincing them it exists.",
       "Proof: a reason to believe. A number, a similar customer, or a credential. For Saffron, the status quo is three to four weeks and eight interviewer hours per hire.",
       "Then the five word test: would a busy buyer keep reading after five words? Openers about you fail. Openers about their world pass. "
       "Saffron's: your engineers ship with A I. Your interviews don't test it."])

scene("real", 2, "IN THE REAL WORLD", "The strategy doc is your spec",
      ["Interrogate the client first: readiness, channels, deal cycle, competitors",
       "One page: ICP, segments, TAM/SAM/SOM screenshots, signals, offer",
       "Test: could a stranger build the list from it alone?"],
      ["In a real job, the strategy doc comes before any tool. First you interrogate the client: is the product ready, which channels work today, how long is the deal cycle, who are the competitors? Vague questions lose client trust.",
       "Then one page: the I C P, two or three segments, the market sizing with screenshots, the top signals, and the offer per segment.",
       "The test: could a competent stranger read it and know exactly who to target, what to look for, and what to say? If it needs you to explain it out loud, it isn't done."])

scene("quiz", 2, "QUICK CHECK", "Pause and answer",
      ["Saffron's SOM is a narrower filter than its SAM. What else makes it a SOM?",
       "An argument: a 3-person team selling by card wins fastest with US startups of 50–500, where one leader decides"],
      ["Quick check. Pause the video. Saffron's S O M is a narrower filter than its S A M. But what else makes it an S O M, and not just a smaller S A M?",
       "The answer: it's an argument you write down. A three person founding team, selling by credit card, wins fastest with US startups of fifty to five hundred people, where a single engineering leader can decide. The filters just express that argument."])

scene("recap", 2, "CHAPTER 2 · RECAP", "Strategy in four lines",
      ["ICP: the company · persona: the person (decision maker + champion)",
       "TAM → SAM → SOM, measured with filters and screenshots",
       "Signals give the why-now; use them as context",
       "Offer = value → pain → proof; pass the five-word test"],
      ["Chapter two in four lines. The I C P is the company, the persona is the person, and you need both a decision maker and a champion. "
       "T A M, S A M and S O M are measured with filters, with screenshots as proof. Signals give the why now, used as context. "
       "And the offer is value, pain and proof, and it has to pass the five word test."])

# ───────────────────────────── 3 · DATA ─────────────────────────────
scene("chapter", 3, "CHAPTER 3 · DAYS 11–16", "The data layer",
      ["Where data comes from, and why one source is never enough",
       "Email quality: valid, catch-all, and the bounce trap",
       "Building the 50-account list"],
      ["Chapter three. The data layer. In class, data was called eighty percent of the job, and everything downstream inherits its quality."])

scene("bullets", 3, "DAYS 11–12 · BEFORE YOU BUILD", "Three questions before any list",
      ["Why are we building it? Outbound, event, webinar, partners",
       "Fresh, or a repeat? Repeat = reuse and re-enrich, don't re-download",
       "People-first or company-first?"],
      ["Before building any list, ask three questions. Why are we building it? A list for cold outbound looks different from a list for an in person dinner.",
       "Is it a fresh reach out or a repeat? For a repeat, you reuse and re-enrich the existing sheet. You don't download everything again.",
       "And is it people first, where you're given job titles and a city, or company first, where you're given specific companies or a size? Getting this wrong wastes everything downstream."])

scene("bullets", 3, "DAYS 11–14 · SOURCES", "No single source is complete",
      ["Apollo: huge and generous, but data lags",
       "Prospeo: clean company search, department filters",
       "Sales Navigator: freshest who-works-where, no emails, no API",
       "Use 3+ sources → merge → dedupe: LinkedIn URL → email → name + company"],
      ["No single database is complete or current, because people change jobs and companies grow. Apollo is huge with a generous free tier, but its location data can lag LinkedIn by up to thirty days.",
       "Prospeo has clean company search and handy department filters.",
       "Sales Navigator is the freshest view of who works where, because people maintain their own profiles. But it gives you no emails, has no A P I, and caps exports at one to two thousand.",
       "So the rule is: pull from three or more sources, merge, and remove duplicates with the most reliable key first. LinkedIn profile, then email, then name plus company. Never name alone, because two different Alex Johnsons are two different people."])

scene("diagram:emailstatus", 3, "DAYS 13–14 · DATA QUALITY", "Four kinds of email",
      ["Valid", "Valid catch-all", "Catch-all only", "Invalid"],
      ["Every email gets a verification status. Valid: the mailbox exists. Safe to send.",
       "Valid catch-all: the company's server accepts any address, but a verifier confirmed this one is likely real. Also safe.",
       "Catch-all only: the server accepts it, but nobody may ever read it. Don't send.",
       "Invalid: it bounces. Never send. And here's why it matters. Mail providers throttle senders whose bounce rate passes about two percent. "
       "A few dead addresses push your good emails into spam, and you'll blame the copy when the real cause was data."])

scene("tip", 3, "PRO TIP · DELIVERABILITY STARTS HERE", "Check the mail server, too",
      ["Skip companies behind Mimecast, Proofpoint or Barracuda",
       "Match sender to receiver: Google → Google, Outlook → Outlook",
       "Never trust one verifier; combine two or three",
       "Expect only ~60% of any raw list to survive cleaning"],
      ["Four data quality tips from class. Check each company's mail server. Companies behind security gateways like Mimecast, Proofpoint or Barracuda silently block outreach tools, so skip them.",
       "Match your sending provider to theirs: Google to Google, Outlook to Outlook.",
       "Never trust a single verifier. Combine two or three, like Enrichly, Bounceban and Million Verifier.",
       "And expect only about sixty percent of any raw list to survive cleaning. Plan your volumes around that."])

scene("shots", 3, "DAYS 15–16 · THE FIRST LIST", "50 target companies",
      [("05-clay-filters.png", (0, 0, 350, 300), "Clay: hiring filters"),
       ("05-clay-filters.png", (0, 280, 350, 580), "20+ engineers · 5+ open roles"),
       ("05-clay-results.png", None, "196 good fits → screened by hand")],
      ["The first real deliverable is fifty target companies, with just three columns: name, domain and company LinkedIn page. Clients usually hand you a bare list, so you practise starting from almost nothing.",
       "For Saffron we used Prospeo and Clay's company search. Clay has free filters for engineers on staff and open engineering roles. Together they cut thirty one thousand companies to under two hundred good fits.",
       "Then every row was checked by hand. Competitors like HackerRank and micro one, outsourcing firms, and possible partners were removed, each with a written reason. Filters narrow a list. Judgement finishes it."])

scene("mistake", 3, "COMMON MISTAKE", "Trusting the filter",
      ["Healthcare filter → hospitals and therapy clinics",
       "“US location” in Clay = any US office, not HQ",
       "Company size band in search ≠ real headcount"],
      ["Three filters that lied to us during the build. The healthcare industry filter pulled in hospitals and therapy clinics, which employ almost no engineers.",
       "Clay's US location filter matched any company with a US office, not just US headquarters, so Indian and British companies slipped through.",
       "And the size band in search said fifty one to two hundred, while the enrichment later found Hugging Face at over eleven hundred people. Always re-check facts before you rely on them."])

scene("recap", 3, "CHAPTER 3 · RECAP", "Data in four lines",
      ["Ask why, fresh-or-repeat, people-or-company first",
       "3+ sources, dedupe by LinkedIn → email → name + company",
       "Send only to valid and valid catch-all; skip security gateways",
       "Filters narrow, judgement finishes"],
      ["Chapter three in four lines. Ask why, fresh or repeat, and people or company first. Use three or more sources and dedupe with the right keys. "
       "Send only to valid and valid catch-all, and skip security gateways. Filters narrow the list, and judgement finishes it."])

# ───────────────────────────── 4 · CLAY ─────────────────────────────
scene("chapter", 4, "CHAPTER 4 · DAYS 15–24", "Clay, the workbench",
      ["How Clay thinks, and the house rules", "Formulas, enrichment and waterfalls",
       "Run conditions: the cost lever"],
      ["Chapter four. Clay, the workbench at the centre of the course."])

scene("bullets", 4, "DAYS 15–16 · ORIENTATION", "What Clay is",
      ["A spreadsheet where every column can call a service",
       "Data providers, an AI researcher, or a free formula",
       "Every call costs credits, and failed calls can cost too",
       "Clay is an orchestration tool, not a data source"],
      ["Think of Clay as a spreadsheet where every column can call a service.",
       "A column can be a data provider lookup, an A I researcher that reads the web, or a free formula.",
       "Every call costs credits, and some cost even when they fail. That single fact explains every house rule.",
       "And in class, Clay was described as orchestration, not a data source. Its own company data is noisy. Its power is chaining a hundred providers together."])

scene("diagram:rules", 4, "THE HOUSE RULES", "Five rules that save your credits",
      ["Auto-run OFF", "Hide, never delete", "Test on 10 rows", "Formulas are free", "Cheapest model first"],
      ["Five house rules. One: turn auto run off on every table that isn't fed by a webhook. Otherwise every edit re runs, and re charges, your columns.",
       "Two: hide columns, never delete them. Deleted results are gone, or cost around fifty credits to recover.",
       "Three: test every column on ten rows before running the rest.",
       "Four: formulas are free. Use them for anything deterministic: splitting names, cleaning domains, bucketing titles.",
       "Five: always start with the cheapest A I model, and escalate only the rows that fail."])

scene("shots", 4, "DAYS 17–20 · BUILDING", "Formula, then enrichment",
      [("06-clean-domain-formula.png", None, "Free formula: clean the domain"),
       ("06-run-menu.png", None, "Run empty rows: never pay twice"),
       ("06-enrich-all-50.png", (0, 0, 722, 380), "Enrich company: 0.5 credits a row")],
      ["The Saffron table started with a free formula that cleans the website into a plain domain, because every later lookup depends on it. You describe the formula in plain English, and Clay writes it, in JavaScript.",
       "Then the first paid column, tested on ten rows. A useful habit: when running the rest, choose run empty rows. Force run all would charge the ten test rows again.",
       "Enrich company filled in size, industry, country and founding year at half a credit a row. Fifty companies, twenty five credits."])

scene("diagram:waterfall", 4, "DAYS 21–22 · WATERFALLS", "Try A, then B, then C",
      ["Provider A", "Provider B", "Provider C", "✓ First valid answer wins"],
      ["A waterfall chains providers. Clay asks provider A first.",
       "If A finds nothing, it asks provider B.",
       "Then C, and so on.",
       "And it stops at the first valid answer, so later providers only run, and charge, for rows still empty. "
       "The class rule: order providers cheapest and most reliable first, and remove the expensive or unreliable ones. Clearbit and Smartlead were removed in class."])

scene("diagram:runcond", 4, "DAYS 21–22 · RUN CONDITIONS", "The cost lever",
      ["Row qualifies?", "Yes → run the column", "No → skip, 0 credits"],
      ["A run condition is a rule for each row: only run this column if something is true. Think of it as a guard clause.",
       "If the row qualifies, the column runs.",
       "If not, it's skipped, and costs nothing. For Saffron, the recruiting team lookup only ran for companies with at least one engineering opening. "
       "This is the lever that keeps spend tied to good leads instead of list size."])

scene("tip", 4, "PRO TIPS · RUN CONDITIONS", "Three habits from class",
      ["Lock column names before writing conditions",
       "Write conditions with Clay's AI builder, then read the preview",
       "Gate every CRM or sequencer push behind a condition"],
      ["Three habits. Lock your column names before writing conditions, because renaming a column later silently breaks every rule that refers to it.",
       "Write conditions with Clay's A I builder, then read the preview before saving. The preview shows will run or will not run for every row.",
       "And gate every push to a C R M or sequencer behind a condition, so incomplete or wrong records never reach a client's system."])

scene("shots", 4, "A BUG WORTH REMEMBERING", "Read the preview before you save",
      [("raw-147.png", (30, 100, 400, 520), "Every row: “Will not run”"),
       ("raw-147.png", (440, 700, 910, 1180), "Rule referenced a column by an old name"),
       ("raw-148.png", (75, 80, 425, 520), "Inserted from the menu → fixed")],
      ["Here's a real bug from the Saffron build. The preview showed will not run on every single row.",
       "Clay had quietly auto named the persona column job seniority, so a rule that referred to persona pointed at nothing, and was always false.",
       "Inserting the column from the slash menu fixed it, and the preview flipped to will run. Saving without reading that preview would have found zero emails."])

scene("bullets", 4, "DAYS 23–24 · LOOKUPS & DEDUPE", "Keeping lists clean",
      ["Blacklist = never contact (competitors) · exclusion = not now (clients, open deals)",
       "Lookup against a reference table → keep “has no results”",
       "Dedupe in Claude, not Clay: LinkedIn → email → name + company",
       "Job titles: “similar to” finds up to ~60% more than “contains”"],
      ["Days twenty three and twenty four. Two do not contact lists. A blacklist is permanent: competitors. An exclusion list is temporary: current clients and open deals.",
       "Both are enforced with a lookup against a small reference table, keeping only rows where the lookup has no results.",
       "Final deduplication happens in Claude, not Clay, using the same key order as before.",
       "And when searching people, use similar to, not contains. Contains is a rigid text match, and in class it missed up to sixty percent of valid people."])

scene("tip", 4, "PRO TIPS · PEOPLE QUALITY", "Filter out the noise",
      ["≥100 LinkedIn connections screens out fake and empty profiles",
       "≥6–12 months in role = can actually buy",
       "Missing LinkedIn URL? Find it before any person enrichment",
       "Use Sculptor in Analyze mode to QA, never Build"],
      ["Four people quality filters. At least a hundred LinkedIn connections screens out fake and empty profiles.",
       "Six to twelve months in the role suggests the person has the authority to buy.",
       "If a person has no LinkedIn URL, find it first. Everything else depends on it.",
       "And Clay's assistant, Sculptor, can check a finished table for gaps. Keep it in analyze mode. Build mode starts changing your table."])

scene("quiz", 4, "QUICK CHECK", "Pause and answer",
      ["Your AI column costs 3 credits a row. Half your list has no open engineering roles. What do you do?",
       "Add a run condition (openings ≥ 1), and test the cheapest model on 10 rows first"],
      ["Quick check. Pause the video. Your A I column costs three credits a row, and half your list has no open engineering roles. What do you do?",
       "Add a run condition so the column only runs where openings are at least one, which halves the cost straight away. Then test the cheapest model on ten rows before paying for a bigger one."])

scene("recap", 4, "CHAPTER 4 · RECAP", "Clay in four lines",
      ["Every column calls a service; every call costs",
       "Auto-run off · hide don't delete · test 10 · formulas free · cheap model first",
       "Waterfalls: cheapest first, stop at the first valid answer",
       "Run conditions + the preview = control over cost and bugs"],
      ["Chapter four in four lines. Every column calls a service, and every call costs. Follow the five house rules. "
       "Waterfalls run cheapest first and stop at the first valid answer. And run conditions, checked in the preview, give you control over both cost and bugs."])

# ───────────────────────────── 5 · SIGNALS & AI ─────────────────────────────
scene("chapter", 5, "CHAPTER 5 · DAYS 19–26", "Signals, AI and qualification",
      ["Turning the strategy's signals into columns", "Claygent: AI research at scale",
       "Outreach or don't: a decision with a reason"],
      ["Chapter five. Turning the strategy into a decision for every company."])

scene("diagram:pipeline", 5, "THE SAFFRON TABLE", "Column by column",
      ["Import", "Clean domain", "Enrich", "Openings", "Recruiters", "AI tools", "Qualify"],
      ["Here's the Saffron accounts table, column by column. Import the fifty companies.",
       "Clean the domain with a free formula.",
       "Enrich company: size, industry, country.",
       "Open engineering roles: the hiring pain. This one only charged for companies where jobs were found.",
       "Recruiting team size, run only for companies with openings. Companies without recruiters hire through agencies, and agencies don't buy tools like Saffron.",
       "An A I research column for companies with one to four openings: do their job ads mention A I coding tools?",
       "And finally qualification: outreach, or don't outreach."])

scene("diagram:models", 5, "DAYS 21–26 · CLAYGENT", "Pick the cheapest model that works",
      ["Helium · 1 credit", "Neon · 2 credits", "Argon · 3 credits"],
      ["Clay's A I researcher, Claygent, reads the web for each row and answers in a structured format. It has model tiers. Helium costs one credit and handles single page lookups.",
       "Neon costs two and handles multi page research.",
       "Argon costs three, and Clay pre-selects it as recommended. The class rule: start with Helium, and escalate only the rows that fail. "
       "For Saffron, Helium on sixteen companies cost nineteen credits. Argon on all fifty would have been around a hundred and fifty."])

scene("tip", 5, "PRO TIPS · AI COLUMNS", "Getting reliable AI answers",
      ["Use day counts (“last 180 days”), never months",
       "Say what the company is (“these are tech companies”)",
       "Strict output types; regenerate the JSON schema after edits",
       "Trust green confidence; double-check orange; never red"],
      ["Four A I tips from class. Write time windows as day counts, like the last one hundred and eighty days. Month based wording returned stale results.",
       "Tell the A I what the company is. Adding these are tech companies fixed bad domain lookups for generic names.",
       "Use strict output types, and regenerate the J SON schema after every prompt edit. In the Saffron build, a loose text field let Helium answer in full sentences, and changing it to true or false fixed it without a pricier model.",
       "And read the confidence colours. Trust green, double-check orange, and never use red. For high stakes calls, run a second column that independently checks the first."])

scene("shots", 5, "QUALIFICATION", "A decision with a reason",
      [("07-formula-before.png", (0, 0, 880, 400), "Bug: “true” (text) ≠ true"),
       ("07-formula-after.png", (0, 0, 880, 400), "Fixed: 30 of 50 → Outreach")],
      ["Qualification in this course is binary: outreach, or don't outreach. No one to ten scores for companies; those are for people. And always with the reason written down. "
       "The preview caught a bug here: the A I answer was stored as the word true, not the value true, so every A I positive company was being rejected.",
       "After the fix, thirty of fifty qualified. Every row carries a reason like twelve engineering openings, recruiting team of three, Cursor in job ads, so a salesperson can see why at a glance."])

scene("real", 5, "IN THE REAL WORLD", "The 70% rule",
      ["A healthy qualifier passes most of a well-built list",
       "Class bar: at least 70% should survive (was 60–70%)",
       "Too few pass? Your rules are too strict or vague, so fix the rules",
       "Saffron passed 60%: ask the instructor"],
      ["How do you know your qualification rules are right? If your list was built well, most of it should pass.",
       "The class bar is now at least seventy percent surviving. It started at sixty to seventy.",
       "If only twenty or thirty percent pass, your rules are too strict, or too vague. Don't accept the loss. Fix the rules.",
       "Saffron passed sixty percent, which is a good question to raise with the instructor."])

scene("diagram:people", 5, "PEOPLE & EMAILS", "From companies to verified contacts",
      ["30 qualified companies", "79 people found · 0.1 credits each",
       "Persona: decision maker · champion · skip", "11-provider email waterfall",
       "40 verified emails"],
      ["Then people. For the thirty qualified companies,",
       "a people search at a tenth of a credit per person found seventy nine people. The first attempt returned founders and a recruiting coordinator: real people, wrong buyers. Filtering by seniority fixed it.",
       "A free formula labelled each person a decision maker or a champion, and skipped sales facing titles like sales engineers or a field C T O.",
       "Then an eleven provider email waterfall, each step followed by validation.",
       "Forty verified work emails. One address was found but failed validation, so it was left out. Better no email than a bounce."])

scene("recap", 5, "CHAPTER 5 · RECAP", "Qualification in four lines",
      ["Turn each strategy signal into a column",
       "Helium first; strict outputs; day counts",
       "Binary decision + written reason; aim for 70%+",
       "Persona filter → only real buyers get the paid email lookup"],
      ["Chapter five in four lines. Turn each signal into a column. Helium first, strict outputs and day counts. "
       "A binary decision with a written reason, aiming for seventy percent or more. And a persona filter, so only real buyers get the paid email lookup."])

# ───────────────────────────── 6 · DATA OUT ─────────────────────────────
scene("chapter", 6, "CHAPTER 6 · DAYS 27–30", "Getting data in and out",
      ["The HTTP API column", "The web-scraping ladder", "Intelligence tables and writing data out"],
      ["Chapter six. Getting data in from anywhere, and out to where it's used."])

scene("bullets", 6, "DAYS 27–28 · HTTP API COLUMN", "Call any API from Clay",
      ["Endpoint + method (GET / POST) + headers + JSON body",
       "Auth key in a header; pull fields out with a JSON path",
       "400 bad request · 401 not logged in · 403 not allowed · 404 wrong URL · 429 slow down"],
      ["When there's no built in integration, the H T T P A P I column calls any A P I from Clay. You set the endpoint, the method, the headers and the J SON body.",
       "Authentication usually goes in a header, and you pull fields out of the response with a J SON path. For an engineer, it's a REST client inside a spreadsheet.",
       "And know your error codes. Four hundred: bad request. Four oh one: not authenticated. Four oh three: not allowed. Four oh four: wrong endpoint. And four twenty nine: you're rate limited, so slow down."])

scene("diagram:ladder", 6, "DAYS 27–28 · WEB SCRAPING", "The scraping ladder",
      ["Native scraper", "Chrome extension", "Claygent", "Apify", "Zenrows"],
      ["When data isn't in any database, you scrape it. Climb the ladder only as far as you need. Clay's native scraper is cheapest.",
       "Then the Chrome extension.",
       "Then Claygent, which can interpret a page, but is expensive at scale: around two hundred dollars per thousand rows.",
       "Then Apify, around nineteen dollars a month.",
       "And Zenrows, for the hardest sites. Use Claygent only when a page needs interpreting, not for plain field extraction."])

scene("bullets", 6, "DAYS 29–30 · INTELLIGENCE TABLES", "Tables that think",
      ["Separate company and people tables; domain + LinkedIn URL are mandatory",
       "Tier companies by size → map each tier to the right persona",
       "Write data out: Google Sheets, or a CRM “upsert”",
       "Plan the logic in Claude first, then build in Clay"],
      ["Days twenty nine and thirty: intelligence tables. Keep company and people tables separate, with domain and LinkedIn URL as mandatory keys.",
       "Tier companies by size, because the right persona changes with scale: the C T O at sixty people, the V P of engineering at four hundred. New companies added to a tier can automatically trigger the right people search.",
       "Write the data out where it's used: a Google Sheet, or a C R M using an upsert, which updates a record if it exists and inserts it if it doesn't.",
       "And plan the execution logic and prompts in Claude before building in Clay. A table should take two to three hours, not days, and should end in outreach ready messaging, not just an email address."])

scene("real", 6, "IN THE REAL WORLD", "Where this is heading",
      ["Claude Code + MCP + CLI tools are joining Clay",
       "Don't dump thousands of rows into an AI chat",
       "Use scripts that stream, save and resume",
       "Keep Clay for its data providers and features"],
      ["Where is this heading? In class, Claude Code with M C P and command line tools was demoed alongside Clay, including automated LinkedIn posting.",
       "But the guest speaker, Kushagra, gave a sharp warning: don't dump thousands of rows into an A I chat and ask it to research them all. Past about half the context window, quality quietly collapses.",
       "Instead, use scripts that stream results, save as they go, and can resume after a crash, with the A I as the orchestrator.",
       "And keep Clay for what it does best: access to dozens of data providers, without rebuilding them yourself."])

scene("recap", 6, "CHAPTER 6 · RECAP", "Data in and out, in four lines",
      ["HTTP API column = any API; know your error codes",
       "Scrape with the cheapest rung that works",
       "Intelligence tables: tiers → personas; write out with upserts",
       "Plan in Claude; use scripts, not giant chats"],
      ["Chapter six in four lines. The H T T P A P I column reaches any A P I. Scrape with the cheapest rung that works. "
       "Intelligence tables map tiers to personas and write out with upserts. And plan in Claude, using scripts rather than giant chats."])

# ───────────────────────────── 7 · SENDING ─────────────────────────────
scene("chapter", 7, "CHAPTER 7 · DAYS 31–36", "Sending email that lands",
      ["Deliverability is infrastructure", "Authentication, warm-up and mailbox maths",
       "Cold email frameworks"],
      ["Chapter seven. Sending email that actually lands in the inbox. In class, email infrastructure was called eighty percent of email success, and copy only twenty."])

scene("bullets", 7, "DAYS 31–32 · DELIVERABILITY", "What really breaks campaigns",
      ["Highest risk: infrastructure and data quality",
       "Lower risk: copy, placeholders, campaign setup",
       "Never send cold email from the company's main domain",
       "Buy mailboxes on Google Workspace or Outlook; separate sending domains"],
      ["Days thirty one and thirty two. When cold email fails, the usual causes are infrastructure and data quality: wrong domains, missing authentication, bad lists.",
       "Copy, placeholders and campaign setup matter, but they're lower risk.",
       "Rule one: never send cold email from the company's main domain. If the campaign draws spam complaints, the real business email suffers. Use separate sending domains.",
       "And buy the mailboxes on Google Workspace or Outlook, which removes most of the manual server setup."])

scene("diagram:dns", 7, "DAYS 33–34 · AUTHENTICATION", "Proving your email is really you",
      ["SPF · who may send for this domain", "DKIM · a signature on every email",
       "DMARC · what to do when checks fail"],
      ["Three D N S records prove your email really comes from you. S P F lists the servers allowed to send for your domain.",
       "D KIM adds a cryptographic signature to every email, so receivers can check it wasn't forged.",
       "And D MARC tells receivers what to do when those checks fail. Without all three, Gmail and Outlook treat you as a likely spammer."])

scene("diagram:warmup", 7, "DAYS 31–34 · WARM-UP", "Earn trust slowly",
      ["Week 1 · 10/day", "Week 2 · 20/day", "Week 3 · 30/day", "Keep warm-up running"],
      ["A new mailbox has no reputation, so you warm it up. Week one: about ten emails a day.",
       "Week two: about twenty.",
       "Week three: about thirty.",
       "And the warm up never really stops. Keep it running alongside your campaigns, starting at around ten a day."])

scene("diagram:mailbox", 7, "DAYS 33–34 · MAILBOX MATHS", "How many mailboxes do you need?",
      ["2,000 leads × 6 steps = 12,000 emails/month",
       "50/day × 22 working days = 1,100 per mailbox",
       "12,000 ÷ 1,100 ≈ 11 → ~12 mailboxes",
       "Spread over 3+ domains"],
      ["Now the maths. Two thousand leads with a six step sequence is twelve thousand emails a month.",
       "One mailbox safely sends about fifty a day, over twenty two working days: about eleven hundred a month.",
       "Twelve thousand divided by eleven hundred is about eleven, so plan for roughly twelve mailboxes.",
       "Spread across at least three domains, so one bad domain can't sink the whole campaign. And the rule of thumb from class: under about two thousand leads a month, lead with LinkedIn instead."])

scene("tip", 7, "PRO TIPS · SENDING DISCIPLINE", "Small settings, big difference",
      ["Plain text; no links; open and link tracking off",
       "Placeholders: first name and company only",
       "AI rewrites the opening line only, using a signal",
       "Soft CTA + an opt-out P.S., not “book a meeting”"],
      ["Sending discipline. Plain text emails, with no links, and open and link tracking switched off. Corporate security tools flag tracking.",
       "Keep placeholders to first name and company. Every extra placeholder is a chance to break.",
       "Let A I write only the opening line, using a signal. Never let it rewrite the whole email.",
       "Skip book a meeting calls to action, because cold recipients don't trust them. And add a plain opt out P S, like reply no and I won't follow up. People who can opt out easily don't hit the spam button."])

scene("diagram:sequence", 7, "DAYS 35–36 · COLD EMAIL FRAMEWORK", "The six-email sequence",
      ["1 · Day 0", "2 · +2–3d", "3 · +3–4d", "4 · +4–5d", "5 · +5d", "6 · Options"],
      ["The framework from day thirty six: six emails, with follow ups two to five days apart. Email one: the signal led opening line and the core offer.",
       "Email two: a different proof point.",
       "Email three: another angle on the pain.",
       "Email four: social proof or a result.",
       "Email five: a short nudge.",
       "And email six, the options close: is it budget, timing, or just not relevant? It makes replying easy. Then run A B tests on every step, prefer narrow micro campaigns over heavy A I personalisation, and send non responders to a follow up sequence later."])

scene("bullets", 7, "TOOLS", "Choosing a sending tool",
      ["Instantly: one company sending for itself",
       "Smartlead: agencies running many clients",
       "Email Bison: ~$600/month, unlimited, agency favourite",
       "LinkedIn: HeyReach (many accounts) · Dripify (few)"],
      ["Which sending tool? Instantly suits one company sending for itself.",
       "Smartlead suits agencies running many clients.",
       "Email Bison costs around six hundred dollars a month, with unlimited leads and emails, and is popular with agencies. Base plans of most tools are restrictive, so scaling needs a higher tier.",
       "For LinkedIn automation, HeyReach suits many accounts, and Dripify suits a few. And combine channels: email, LinkedIn and phone, in a repeating three to four month pattern."])

scene("quiz", 7, "QUICK CHECK", "Pause and answer",
      ["1,000 leads × a 5-step sequence, 50 emails a day per mailbox. How many mailboxes?",
       "5,000 ÷ 1,100 ≈ 4.5 → 5 mailboxes, over 2+ domains (and LinkedIn first, since it's under 2,000)"],
      ["Quick check. Pause the video. One thousand leads, a five step sequence, and fifty emails a day per mailbox. How many mailboxes do you need?",
       "Five thousand emails divided by eleven hundred per mailbox is about four and a half, so five mailboxes, over at least two domains. And since that's under two thousand leads, LinkedIn should lead."])

scene("real", 7, "IN THE REAL WORLD", "Saffron's sending plan",
      ["40 contacts × 6 steps = 240 emails: tiny",
       "Start on LinkedIn; email once a lookalike domain is warmed",
       "10 campaigns = 3 segments × 2 personas × top signals",
       "Before sending: domain, SPF/DKIM/DMARC, 3-week warm-up, MX check"],
      ["Applied to Saffron. Forty contacts times six steps is just two hundred and forty emails.",
       "So by the course's own rule, start on LinkedIn, and add email once a separate lookalike domain is set up and warmed.",
       "The homework is ten campaigns. Combine three segments, two personas, and the strongest signals: hiring surge, A I coding tools, or a new engineering leader.",
       "And before a single email goes out: the domain, S P F, D KIM and D MARC, three weeks of warm up, and the mail server check from chapter three."])

scene("recap", 7, "CHAPTER 7 · RECAP", "Sending in four lines",
      ["Infrastructure and data first; never the main domain",
       "SPF + DKIM + DMARC; warm up 10 → 30 a day",
       "Mailboxes = leads × steps ÷ ~1,100; under 2,000 → LinkedIn",
       "6 emails, options close, plain text, tracking off"],
      ["Chapter seven in four lines. Infrastructure and data come first, and never the main domain. S P F, D KIM and D MARC, then warm up from ten to thirty a day. "
       "Mailboxes equal leads times steps divided by about eleven hundred, and under two thousand leads, LinkedIn leads. Six emails, an options close, plain text, and tracking off."])

# ───────────────────────────── 8 · CAREER & EFFICIENCY ─────────────────────────────
scene("chapter", 8, "CHAPTER 8 · THE BONUS POINT & GUESTS", "Efficiency and your career",
      ["The credit-efficiency story", "What a portfolio needs", "Advice from two GTM engineers"],
      ["Chapter eight. Doing more with less, and turning this course into a career."])

scene("diagram:credits", 8, "THE BONUS POINT", "118.6 credits for the whole pipeline",
      ["Enrich 25", "Openings 20", "Recruiters 19", "AI tools 19", "People 9.1", "Emails 26.5"],
      ["Here's what the whole Saffron pipeline cost: a hundred and eighteen point six credits, for fifty companies screened, thirty qualified, and forty verified contacts.",
       "The savings came from four habits. The cheapest model that does the job. Run conditions, so expensive steps only run where they matter. "
       "Comparing providers: people search was a tenth of a credit on one provider and up to three on others. And testing on ten rows first. "
       "One more surprise: not every enrichment charges per attempt. Some only charge when they find something. That's the bonus point, and the story for your LinkedIn post."])

scene("bullets", 8, "WHAT GETS YOU HIRED", "The portfolio checklist",
      ["Strategy doc + Clay table + push to a sequencer",
       "A Claude Code integration + a Make or n8n automation",
       "5 Loom walkthroughs of the whole pipeline",
       "Honest benchmarks: LinkedIn 70% accept / 30% reply · email 3–5% reply"],
      ["Hiring in this field is portfolio first, often with a paid trial project. The class checklist: a strategy doc, a Clay table, and data pushed to a sequencer like Instantly or HeyReach.",
       "Plus a Claude Code integration and an automation in Make or n8n.",
       "And five Loom walkthroughs of the whole pipeline.",
       "If you have no real campaign results yet, quote honest industry benchmarks instead of inventing numbers: about seventy percent LinkedIn acceptance with thirty percent replies, and three to five percent email replies."])

scene("bullets", 8, "GUEST · REJOICE", "Revenue engineer, not tool operator",
      ["Tool operators run tools; revenue engineers produce outcomes",
       "Skill order: fundamentals → systems thinking → tech → tools → communication",
       "Her best Clay build had one enrichment column",
       "Build, record a Loom, DM the founder; learn in public"],
      ["Two guest sessions, two practitioners. Rejoice split the market into tool operators, who just run Clay, and revenue engineers, who use it to produce a business result. Only the second kind lasts.",
       "Her skill order: G T M fundamentals, systems thinking, technical fluency, tools, and communication. Tools come fourth on purpose.",
       "Her best Clay build ever had one enrichment column. Complexity is not the goal.",
       "And her career advice: don't send cold résumés. Build a project, record a Loom of it, message the founder directly, and document your learning in public on LinkedIn."])

scene("bullets", 8, "GUEST · KUSHAGRA", "How to break in",
      ["Proof of work beats certificates and courses",
       "“Value bomb”: build and give away useful workflows",
       "Agencies are the fastest way to broad experience",
       "Use AI in learning mode, so you're not just a human wrapper"],
      ["Kushagra, a G T M engineer at Starbridge: proof of work beats certificates and courses every time.",
       "His strategy is value bombing: build useful tools and workflows, and give them away in communities like the Clay Slack. Reputation follows.",
       "Agencies are the fastest way to get broad experience, and easier niches, like local services, are a good place to earn first results.",
       "And use A I as a teacher, in learning mode, so you understand what it builds, instead of becoming a human wrapper around it."])

scene("bullets", 8, "WHAT'S NEXT", "Your next steps",
      ["Plan 10 Saffron campaigns (segments × personas × signals)",
       "Share Strategy Doc v2 with Yogesh · post the LinkedIn post",
       "Record your Loom walkthroughs · connect with GTM agencies",
       "Practise Clay ~2 hours a day; try one new tool a day"],
      ["Your next steps. Plan ten Saffron campaigns, from segments, personas and signals.",
       "Share the strategy doc with Yogesh, and post the LinkedIn post about credit efficiency.",
       "Record your Loom walkthroughs of this build, and connect with the G T M agencies on LinkedIn.",
       "And keep practising: about two hours of Clay a day, and one new tool a day, noting what manual work it replaces."])

scene("title", 8, "THE BRIEF, ANSWERED", "30 companies · 40 people · every reason written down",
      ["Everything is in Drive → GTM Cohort Catch-up"],
      ["So, back to the founders' brief. Which companies are most likely to buy this quarter, and who do we talk to? "
       "Thirty qualified companies, forty verified decision makers and champions, and the reasoning behind every one. "
       "Everything is in the G T M Cohort Catch up folder in your Drive. Good luck in class."])
