# Video script: "Saffron: the GTM Engineering course so far" (v2)

Storyline: you've just joined Saffron as its first GTM engineer, and the founders hand you a one-line brief. Every stage of the course (Days 1–28) answers part of that brief. Each term is explained in plain words when it first appears, then we show what we did for Saffron and why it matters in a real job.
Target: about 11 minutes, 25 scenes. Voice: Piper (local). Acronyms are spelled out for the voice.

---

## Scene 1: The brief
Visual: title card with the brief
Narration: Imagine you've just joined Saffron as its first G T M engineer. The founders give you a one line brief: find the companies most likely to buy from us this quarter, and the right person to talk to at each one. The first twenty eight days of this course are all about answering that brief. In this video we'll go through each stage, what it means, and what we actually built for Saffron.

## Scene 2: What a GTM engineer does (Days 1–2)
Visual: card: GTM definition + funnel stages with meanings
Narration: First, the words. G T M means go to market: everything a company does to find customers and turn them into revenue. Every customer moves through a funnel. A lead is a person you know about. A marketing qualified lead looks like a fit. A sales qualified lead is someone sales agrees is worth a real conversation. Then an opportunity, a deal with a dollar value, and finally closed. A G T M engineer owns the top of that funnel. In a real job, a sales team of three can't research a thousand companies by hand. Your systems do that research, so they spend their day in conversations.

## Scene 3: The seven layers (Days 3–4)
Visual: card: seven layers + the handoff idea
Narration: Days three and four gave the map for the whole course: seven layers. Data is where prospects come from. Enrichment adds facts to them. Signals tell you why now. Orchestration moves data between tools. Execution is the outreach itself. The C R M is the record of every conversation. And A I agents multiply all of it. The key idea: value is created inside each layer and lost at the handoffs. A perfect list is worth nothing if it never reaches the outreach tool. When something breaks in a real job, the first question is always: which layer, and which handoff?

## Scene 4: Saffron and its ideal customer (Days 5–6)
Visual: card: Saffron, pricing, ICP, decision maker vs champion
Narration: Days five and six: pick one real company and build everything for it. Saffron runs technical interviews for the A I era: a candidate builds a real feature in the hiring company's code with Claude Code, and A I reviewers score how they worked. It costs two hundred to five hundred dollars a month, paid by card. That price tells you who buys: companies small enough that one engineering leader can say yes without a procurement process. That description is the I C P, the ideal customer profile: US tech companies of fifty to five hundred people that hire engineers regularly. Inside each one there are two people. The decision maker, a C T O or V P of engineering, signs. The champion, an engineering manager or recruiter, is the one grading take home tests at midnight, and will push for the tool.

## Scene 5: TAM
Visual: TAM filters + results
Narration: Before building any list, you need to know how big the market is, because a founder or an investor will ask. T A M, the total addressable market, is every company that could ever buy Saffron in principle. A G T M engineer doesn't guess this on a slide. You apply filters in a data tool and read the count. Tech, fintech and health companies of fifty to five thousand people, in the US, Canada and Western Europe: about fifty four thousand companies.

## Scene 6: SAM
Visual: SAM filters + results
Narration: S A M, the serviceable addressable market, is the part of that universe Saffron can actually serve. A company needs a real engineering team, and it needs to be growing, or there is nothing to assess. Adding at least twenty engineers and a growing headcount cut the list to about twelve thousand. It also removed the hospitals that the healthcare filter had pulled in. That's a very normal moment in real work: a filter that sounds right lets in noise, and the next filter cleans it up.

## Scene 7: SOM
Visual: SOM filters + results
Narration: S O M, the serviceable obtainable market, is the slice Saffron can realistically win in the next year. It's partly a filter and partly an argument you write down. US only, because the founders sell from San Francisco. Fifty to five hundred people, because one leader can buy with a card. Younger companies, because they adopt new tools faster. That leaves two thousand nine hundred and twenty one companies. In a real job, this is the number that decides how big the outbound effort should be, and each count goes into the strategy doc as a screenshot, because clients want evidence, not claims.

## Scene 8: Why now, and what to say (Days 8–10)
Visual: card: signal / intent / trigger + the offer
Narration: Knowing who could buy isn't enough. You need to know who needs Saffron now. A signal is a public fact about a company. If it's posting twelve engineering jobs, it's facing dozens of interviews in the next few months, exactly the pain Saffron removes. Intent is a person doing something toward you, like visiting your pricing page. A trigger is what you do in response. Days nine and ten turned all of this into a one page strategy brief, with a short offer for each group of buyers. The test is whether a busy C T O keeps reading after five words. Your engineers ship with A I. Your interviews don't test it.

## Scene 9: Where the data comes from (Days 11–14)
Visual: card: sources → merge → dedupe → verify
Narration: Now you need actual companies and people. No database is complete or current, because people change jobs and companies grow, so you pull from several sources and merge them. Duplicates are removed using the most reliable key first: the LinkedIn profile, then the email, then name plus company. And every email is verified before anything is sent. The real world reason: send to a handful of dead addresses, and email providers start treating your domain as spam, so even your good emails stop arriving.

## Scene 10: The first list (Days 15–16)
Visual: Clay filters + Clay results
Narration: The first real deliverable is fifty target companies. In a real job, this is often how an engagement starts: here's our market, give us a first list. Apollo wouldn't accept a Gmail sign up, so we used Prospeo and Clay's own company search. Clay could filter on engineers on staff and open engineering roles, which cut thirty one thousand companies down to under two hundred good fits. Then every row was checked by hand, and competitors like HackerRank, outsourcing firms and possible partners were removed, each with a written reason. Filters narrow a list. Judgement finishes it.

## Scene 11: Clay, the workbench (Days 15–16)
Visual: card: what Clay is + house rules
Narration: Clay is where the list becomes a pipeline. Think of it as a spreadsheet where each column can call an outside service: a data provider, an A I researcher, or a free formula. Every call costs credits, and failed calls can cost too. That's why the course is strict about a few habits. Turn auto run off. Hide columns instead of deleting them. Test every column on ten rows before running the rest. And use free formulas wherever the logic is fixed.

## Scene 12: Starting from almost nothing (Days 17–20)
Visual: Clean Domain formula
Narration: A real client usually hands you little more than a list of company names. So the table started with just three columns: name, website and LinkedIn page. The first column we added was a free formula that cleans the website into a plain domain, because every later lookup depends on it. You describe the formula in plain English and Clay writes it, in JavaScript.

## Scene 13: Enrichment
Visual: run menu → enriched table → credit balance
Narration: Enrichment means adding facts to each row from outside sources. Enrich company filled in size, industry, country and founding year, at half a credit a row. We ran it on ten rows, checked them, then ran the other forty. One habit worth copying: choosing run empty rows only processes rows that aren't done yet, so you never pay twice. Fifty companies cost twenty five credits.

## Scene 14: Turning signals into columns (Days 21–22)
Visual: card: openings → recruiting team → run condition
Narration: Now the signals from the strategy. First, how many engineering roles each company has open. That's the hiring pain. Second, whether it has a recruiting team, because companies without one hire through agencies, and agencies don't buy tools like Saffron. The second check used a run condition: a rule for each row that says, only run this if the company has at least one opening. Rows that fail the rule are skipped, and cost nothing. This is the everyday lever that keeps your spend tied to good leads.

## Scene 15: When the answer isn't in any database (Days 25–26)
Visual: AI research column
Narration: Some questions aren't in any database. Do this company's engineering job ads mention Cursor or Claude Code? If they do, the team already writes code with A I, and "how do you test that in interviews?" lands immediately. Clay's A I researcher can read the careers page and answer. It's the most expensive kind of column, so it only ran on the sixteen companies where the answer could change the decision, using the cheapest model. When the first answers came back in the wrong format, tightening the output fixed it. No need for a pricier model. Nineteen credits, instead of about a hundred and fifty.

## Scene 16: Qualification: a decision, with a reason
Visual: formula preview before → after
Narration: Qualification turns all of this into a decision: outreach, or don't outreach. Never a vague score for a company, and always with the reason written down, so a salesperson can see why. The rule: skip companies with no recruiting team, the wrong size, outside the US, or not hiring engineers. Otherwise reach out if they have five or more openings, or fewer openings but already use A I coding tools. The preview caught a bug before it cost anything. The A I answer was stored as the word true, not the value true, so every A I positive company was being rejected. After the fix, thirty of fifty qualified.

## Scene 17: Finding the right people
Visual: card: before / fix / after
Narration: Next, the people. For each qualified company we want the decision maker who signs, and the champion who feels the pain. The first search returned founders and a recruiting coordinator: real people, wrong buyers. Removing co founder and filtering by seniority returned vice presidents of engineering instead. Twenty seven companies, seventy nine people, about nine credits.

## Scene 18: Decision maker, champion, or skip
Visual: persona preview
Narration: A free formula then labelled each person as a decision maker or a champion, and left sales facing titles blank: sales engineers, account managers, a field C T O. In a real job, this is the difference between a message reaching the buyer and reaching someone who sells for a living.

## Scene 19: Read the preview before you save
Visual: broken preview → broken rule → fixed rule → fixed preview
Narration: One more lesson from the preview. Clay had quietly named the persona column job seniority, so a rule written with the old name pointed at nothing, and every row said will not run. Inserting the column from the menu fixed it. The habit that saves you: always read the preview before you save.

## Scene 20: Verified work emails
Visual: waterfall columns
Narration: Finally, work emails. A waterfall tries one email provider, and if it finds nothing, tries the next: eleven in total, each followed by a validation check. Forty of forty five eligible people now have verified work emails. One address was found but failed validation, so it was left out. Better no email than a bounce. And the first, cheapest provider found thirty nine of the forty.

## Scene 21: What it cost (the bonus point)
Visual: card: credits breakdown + four habits
Narration: Add it up: fifty companies screened, thirty qualified, forty verified contacts, for a hundred and eighteen point six credits. The savings came from four habits: the cheapest model that does the job, run conditions so expensive steps only run where they matter, comparing providers before choosing one, and testing on ten rows first. That's the bonus point, and it's the story of your LinkedIn post.

## Scene 22: The deliverable
Visual: card: client delivery sheet
Narration: Everything lands in a client delivery sheet, the thing a founder or a sales team would actually use on Monday morning: forty contacts with verified emails and the reason their company qualified, all fifty accounts with their decision, and a follow up list of people to reach on LinkedIn and companies still to process.

## Scene 23: Yesterday's class (Days 27–28)
Visual: card: HTTP API column + scraping ladder + 70% bar
Narration: Yesterday's class added two tools for when data isn't in any database. The H T T P A P I column lets Clay call any outside A P I, like a REST client inside the spreadsheet. Web scraping pulls data straight from websites. The rule mirrors the credit rule: start with the cheapest tool that can do the job, and only use the A I researcher when a page needs interpreting. The bar also went up: at least seventy percent of a list should now qualify, so ask Yogesh about the sixty percent here.

## Scene 24: What's next
Visual: card: to-do + where the course goes next
Narration: What's left is yours. Share the strategy doc with Yogesh, post the LinkedIn post, record five short walkthroughs of this build for your portfolio, connect with the G T M agencies on LinkedIn, and work through the follow ups, including a mail server check before any email is sent. The course now moves on to outreach tools, automation and A I agents, and this table is what they will run on.

## Scene 25: Back to the brief
Visual: card: the brief, answered
Narration: So, back to the founders' brief: which companies are most likely to buy this quarter, and who do we talk to? You now have thirty qualified companies, forty verified decision makers and champions, and the reasoning behind every one. Everything is in the G T M Cohort Catch up folder in your Drive. Good luck in today's class.
