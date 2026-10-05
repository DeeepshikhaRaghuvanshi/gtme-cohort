# D15+D16_ Ship_ a 50-account target list + Clay orientation - 2026_09_17 08_54 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D15+D16: Ship: a 50-account target list + Clay orientation

Sep 17, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Account list building and Clay workspace setup with AI enrichment and scoring strategies.

Account List Standardization

Targets must consist of 50 companies, not individuals, to ensure accurate GTM engineering data.

Standardized list format requires only company name, domain, and LinkedIn URL.

Rithika proposed identifying companies transitioning from PLG to SLG motions by using sales headcount as a proxy.

Yogesh noted that companies lacking specific GTM signals remain viable, but signals effectively serve as account qualification markers.

Clay Platform Operations and Best Practices

Disable the 'auto run' feature globally to prevent unintended credit consumption.

Use 'hide' instead of 'delete' for columns to preserve data integrity and avoid unrecoverable data loss.

Utilize 'Prompter' to generate AI instructions and leverage JSON schemas for consistent, structured data output.

Use 'Helium' for web-based search tasks; resort to 'Neon' or 'Argan' models only if Helium fails.

Prioritize high-confidence (green) data; avoid using medium or low-confidence results.

Employ 'contains' and 'not empty' filters for efficient data segmentation and outlier removal.

GTM Engineering and Signal Scoring Strategy

Implement a 1-10 scoring model: 7-10 triggers immediate outreach, 4-6 initiates nurturing, and 1-3 dictates exclusion.

Apply 3-month windows for funding and hiring signals; extend to 6 months only if account volume is insufficient.

Clay is the preferred tool for technographic data via BuiltWith integration, while Prospio and Apollo are cost-effective for general filtering.

Strategic Messaging Principles

Yogesh emphasized that outreach messaging must leverage signals to identify company needs rather than simply stating known facts.

Avoid explicitly reciting specific data points like recent funding rounds or exact hiring numbers to prevent irrelevant or cold outreach.

Frame outreach around providing value based on inferred company growth, such as team expansion or new product developments.

The strategy document remains the primary driver of execution, with Clay serving exclusively as a tool to implement that strategy.

Clay Platform Workflow and Best Practices

The established workflow involves running basic company enrichment and funding date lookups.

Best practices include disabling auto-run features and testing enrichment on a 10-row sample using Helium before scaling.

Users should maintain column integrity and utilize AI capabilities to enhance data processing.

The account currently holds 1,000 available credits.

Next steps

[Yogesh Jaiswal] Provide trigger feedback: Review the Mutiny company details and provide feedback on the proposed signal-based outbound triggers.

[sampath vemulapati] Re-create company list: Refine the search filters to generate a list of 50 companies instead of individuals.

[The group] Create Company List: Prepare a list of 50 target companies for the outbound campaign.

[The group] Upload And Enrich: Upload the company list into Clay and initiate basic enrichment processes for company details and funding dates.

[The group] Test Enrichment: Execute enrichment on a sample of 10 rows using Helium to verify functionality before scaling.

[Alok] Check Credits: Confirm the current balance of available account credits.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 17, 2026

### D15+D16: Ship: a 50-account target list + Clay orientation

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D15+D16: Ship: a 50-account target list + Clay orientation

Meeting records Transcript Recording

#### Summary

Account list building and Clay workspace setup with AI enrichment and scoring strategies.

Account List Preparation
Participants built company account lists of 50 accounts using Prospo. Yogesh instructed everyone to clean spreadsheets by keeping only company name, domain, and LinkedIn URL before importing into Clay.

Clay Setup and Enrichment
Yogesh demonstrated workspace setup, auto-run deactivation, and column hiding rules in Clay. Participants configured AI prompts using Helium models and JSON schemas to check funding rounds.

Scoring and Outreach Strategy
Yogesh introduced account scoring thresholds and signal-based outreach strategies. Participants were assigned to build account lists and run basic company enrichments in Clay.

#### Decisions

Aligned

Company list data field standards Team members must restrict their initial company data lists to only include company name, company domain, and company LinkedIn URL.

Auto-run deactivation standard for Clay tables The team must keep auto-run disabled in all non-webhook Clay tables for the next four to six months to avoid accidental charges.

Column deletion restrictions in Clay Team members must hide columns instead of deleting them in Clay for at least three months to prevent permanent data loss.

#### Next steps

[Yogesh Jaiswal] Provide trigger feedback: Review the Mutiny company details and provide feedback on the proposed signal-based outbound triggers.

[sampath vemulapati] Re-create company list: Refine the search filters to generate a list of 50 companies instead of individuals.

[The group] Create Company List: Prepare a list of 50 target companies for the outbound campaign.

[The group] Upload And Enrich: Upload the company list into Clay and initiate basic enrichment processes for company details and funding dates.

[The group] Test Enrichment: Execute enrichment on a sample of 10 rows using Helium to verify functionality before scaling.

[Alok] Check Credits: Confirm the current balance of available account credits.

#### Details

Account List Status and Tool Usage: Alok reports completing a list of 50 accounts using Prospol (Prospo) because department headcount filters are locked, while Gagan Bhaisa and Rithika Murthy are still working on their lists, with Gagan rebuilding in Prospo and Rithika experiencing delays. Yogesh Jaiswal instructs Alok to push the CSV file into a Google sheet (00:06:40).

Signal-Based Outbound and PLG-to-SLG Transitions: Rithika Murthy asks about signal-based outbound strategies for their portfolio company, Mutiny, which offers an AI agent for personalized landing pages and customer-facing GTM, targeting account executives, product marketing, ABM teams, and in-house GTM engineers and strategists. Rithika inquires how to identify companies transitioning from pure product-led growth to sales-led growth or hybrid motions, and whether compliance certifications like SOC 2 and DPDP serve as valid triggers (00:08:05). Yogesh Jaiswal explains that detecting high hiring rates for sales personnel using a Clay formula can indicate a sales-led growth transition, citing examples like PhonePe versus Razorpay (00:09:52).

Company Selection and Review for Mutiny: Yogesh Jaiswal asks Rithika Murthy about the selected company and notes that enterprise up-market targeting typically involves increased compliance and certifications. Yogesh Jaiswal states they will check Mutiny in the sheet and provide feedback after class. Yogesh Jaiswal then checks on other participants—Shubham, Khushboo, Deepshikha, and Sat—regarding their 50-account lists, with sampath vemulapati confirming completion (00:11:04).

Account List Filters for Goji Berry AI: sampath vemulapati shares their screen to present an account list for Goji Berry AI, a company helping B2B SaaS firms conduct sales when they cannot afford SDRs (00:12:11). Sampath explains their Prospo filters, which targeted heads of sales, VPs of sales, and co-founders in the US, UK, France, Germany, and Netherlands, with verified emails, AI/ML, data analytics, and SAS company types, and department headcounts of no more than 11 people, yielding 1,625 results. Yogesh Jaiswal clarifies that the task requires a list of 50 companies rather than individuals, and Sampath agrees to reset their filters (00:13:30). Yogesh Jaiswal emphasizes that GTM engineering requires company accounts rather than individual contacts at this stage (00:14:42).

Industry-Agnostic Account Selection for Oxen: Khushboo shares that their selected company, Oxen, sells an AI cost-monitoring and ROI tool that is industry-agnostic, raising questions about how to filter target accounts (00:14:42). Yogesh Jaiswal advises Khushboo to review company websites to identify top enterprise targets that utilize numerous AI tools, explaining that while the current exercise uses a sample of 50 companies, real GTM engineering typically scales to 500 or 1,000 companies (00:15:40).

Cleaning and Formatting the Company Account List: Alok shares their screen showing a completed list of 50 companies for their in-house legal team AI tech solution. Yogesh Jaiswal instructs Alok to simplify the spreadsheet by retaining only the company name, company domain, and company LinkedIn URL, while deleting all other columns including the industry column (00:16:51). Yogesh Jaiswal instructs all participants to structure their sheets similarly and rename the sheet to "company sheet" in preparation for importing into Clay (00:18:14).

Introduction to Clay and Workspace Setup: Yogesh Jaiswal introduces Clay as an orchestration platform for GTM engineering that integrates native features and third-party data providers via a waterfall of email and enrichment providers (00:19:38). Alok shares their screen to sign up for a free trial on Clay.com using Google, skips the tutorial, and sets up a workspace folder and a new workbook named "company" (00:20:48). Alok then imports the edited CSV company list into Clay (00:24:34).

Essential Clay Best Practices: Auto-Run and Deletion Rules: Yogesh Jaiswal instructs all participants to turn off the "auto run" feature in Clay to prevent accidental credit consumption from automated background updates during testing (00:26:56). Yogesh Jaiswal also warns against deleting columns in Clay for at least three months, noting that data cannot be recovered without spending 50 credits, and recommends using the "hide" and "unhide" functions instead (00:28:04).

Finding People and Enriching Company Data in Clay: Yogesh Jaiswal explains that company-level enrichment requires a company domain or LinkedIn URL, while person-level enrichment requires a person's LinkedIn URL (00:29:01). Alok adds a "Find people" enrichment in Clay, mapping the company table and domain to search for legal professionals (00:31:16). Alok defines their ideal customer profile as in-house legal teams of 1 to 5 people, selects the "legal" job function yielding 79 results from 50 companies, and saves the output to a new table to test 10 rows with auto run turned off (00:32:11).

Company Enrichments and AI-Driven Funding Detection: Yogesh Jaiswal guides Alok back to the company sheet to add enrichments for employee count, size, industry, country, locality, and annual revenue, running the process across 50 rows (00:34:47). Yogesh Jaiswal then introduces Clay's AI agent feature ("use AI") to check whether target companies raised funds within the last 6 months (00:38:15). Alok writes a prompt using company domains, and Yogesh Jaiswal explains the prompter structure consisting of context, objectives, instructions, and examples (00:39:19).

Configuring AI Models and JSON Schemas in Clay: Yogesh Jaiswal explains that text-heavy tasks should use GPT, while web searches should use the Helium model (followed by Neon, and Argan which costs three credits) (00:40:25). Yogesh Jaiswal instructs Alok to select JSON schema output and generate it from the prompt to ensure compatibility with advanced software, then save and run the test on 10 rows (00:41:49). When Alok asks about using custom API keys, Yogesh Jaiswal responds that Clay's native AI models are sufficient (00:42:45).

Evaluating AI Confidence Scores and Extracting Data: Yogesh Jaiswal reviews the AI output confidence scores, explaining that green indicates high confidence, orange indicates medium confidence, and red indicates low confidence data that should not be used (00:44:43). Alok runs the AI prompt on the remaining 40 empty rows. Yogesh Jaiswal shows how to inspect "steps taken" to verify web searches and extract specific sub-fields like "notes" into dedicated columns before deleting duplicates and renaming the column to remove "use AI" (00:45:49).

Using Filters in Clay: Yogesh Jaiswal demonstrates various filter operations in Clay, explaining that "equal to" requires exact text matching including case sensitivity, whereas "contains" and "contains any of" are case-insensitive and allow multiple values (00:48:19). Yogesh Jaiswal also covers "does not contain", "does not contain any of", and "empty/not empty" filters (00:50:52). Alok filters for empty funding dates to isolate companies that have not raised funds in the last 6 months (00:51:55).

Rationale for Company-Level Search and Data Quality: Rithika Murthy asks why searches start at the company level via external tools rather than natively within Clay (00:51:55). Yogesh Jaiswal explains that Clay's data is scraped from LinkedIn and frequently contains fake or incorrect company profiles, making third-party data providers or starting with verified company accounts more reliable for initial qualification (00:53:18). Yogesh Jaiswal adds that initial company-level checks qualify accounts based on funding and hiring signals before outreach (00:55:38).

Account Scoring and Thresholds: Yogesh Jaiswal introduces account scoring, explaining that positive parameters like recent funding add points (e.g., +2 points), and accounts reaching a score of 10 are prioritized for immediate outreach (00:55:38). Gagan Bhaisa inquires about threshold-based scoring versus point systems, and Yogesh Jaiswal clarifies that a score of 7 to 10 warrants immediate outreach, a score of 4 to 6 requires nurturing, and a score of 1 to 3 should be avoided (00:56:29). Yogesh Jaiswal notes that signals serve as qualification metrics rather than strict predictors of buying behavior (00:57:46).

Signal Timeframes and Decaying Scores: Gagan Bhaisa asks about score decay when time passes without new signals in subsequent cycles (00:58:46). Yogesh Jaiswal explains that funding signals are typically evaluated over a 3-month window rather than 6 months, and open roles should not be excessively old (00:59:46). Yogesh Jaiswal notes that tightening signal parameters severely reduces account volume, so timelines can be adjusted, though signals remain secondary to overall account qualification (01:00:50).

Comparing Prospio and Clay for GTM Engineering: sampath vemulapati asks if Prospio's native filters for funding and other metrics provide qualitative data (01:02:04). Yogesh Jaiswal confirms that data providers are increasingly offering signals, but GTM engineering requires balancing ideal, cost-saving, and scalable methods. Yogesh Jaiswal notes that while Prospio can be used if its data is accurate to save Clay credits, Clay is superior for technographic filters due to its integration with BuiltWith, though advanced users can connect Prospio and Apollo APIs directly into Clay (01:03:11).

Messaging Strategy and Signal Usage in Outreach: Deepshikha sought clarification on whether messaging refers to strategy, which Yogesh Jaiswal confirmed. Yogesh Jaiswal explained that a strategy document dictates execution steps, such as targeting specific markets or industries like automotive for Razorpay, and that messaging must rely accurately on signals (01:05:26). Yogesh Jaiswal shared a past mistake where an outreach email incorrectly claimed a company raised funding in the last six months based on Prospio data, when actually an acquired subsidiary had raised the funds—an error caught by re-running enrichment in Clay (01:06:30). Yogesh Jaiswal emphasized that outreach should not awkwardly parrot raw data back to recipients (such as congratulating someone on marriage strictly to sell a honeymoon package, or bluntly stating a company is hiring ten salespeople) (01:07:38). Instead, signals should be integrated contextually; for instance, mentioning that a sales team is expanding in Delhi and referencing existing clients like Lambda Test and Service Now while offering a sales transformation tool. Yogesh Jaiswal noted that applying these insights requires sales knowledge that improves with practice (01:08:39).

Clay Platform Assignment and Best Practices: Yogesh Jaiswal assigned participants to build a top 50 company account list, upload it into Clay, and run a basic company enrichment alongside a funding round check for the last six months. Gagan Bhaisa remarked that the process feels focused. Yogesh Jaiswal outlined strict best practices for the exercise: turn auto-run off, test enrichments on the first 10 rows, select Helium, utilize artificial intelligence, and ensure no columns are deleted. Yogesh Jaiswal explained that this exercise represents only about 5 percent of Clay capabilities to prevent participants from feeling overwhelmed, stressing that Clay is merely a tool to execute the core strategy rather than the primary focus itself (01:09:44). Alok confirmed that their account currently holds 1,000 credits, down from previous allocations. Yogesh Jaiswal concluded by scheduling a follow-up session for the next day to cover advanced features such as formulas and run conditions (01:10:55).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 17, 2026

### D15+D16: Ship: a 50-account target list + Clay orientation - Transcript

#### 00:06:40

Yogesh Jaiswal: Hey, good morning Al.

Alok: Good morningish.

Yogesh Jaiswal: Have you created that list of 50 accounts?

Alok: Yeah,

Yogesh Jaiswal: Yeah. Oh, that's good. That's good. So, what you have used cross view or polo?

Alok: prospol because the uh head count by department filter is actually locked.

Yogesh Jaiswal: Okay. Okay. Sorry. Hey. Hey, how are you?

Gagan Bhaisa: Hey, morning. Morning guys.

Rithika Murthy: Hey, good

Yogesh Jaiswal: So, uh, Alok,can you share your screen and show the list? Is it in CSV or like Google sheet?

Alok: It's in CSV.

Yogesh Jaiswal: Uh, can you push to Google sheet and show it?

Alok: Yeah. Yeah. Just a second.

Yogesh Jaiswal: Uh Rita, you and uh Gagan, you you both have like created that list of 50 accounts.

Gagan Bhaisa: Yes, I did it. Uh, but struggling to get into a sheet. So, I'm just trying to build in a prospect once again.

Yogesh Jaiswal: Perfect. That's that's nice. Uh you have

Rithika Murthy: Uh I am just working on it.

#### 00:08:05

Rithika Murthy: Uh there's a few things I was held up in yesterday so I couldn't complete it.

Yogesh Jaiswal: Okay.

Rithika Murthy: I'm just working.

Yogesh Jaiswal: Yes, you can use procure. It's it's going to be easy.

Rithika Murthy: Yeah, sure.

Gagan Bhaisa: Okay.

Rithika Murthy: Um so I actually had a quick question. I wanted to uh sort of take a different approach with like the signal based outbound.

Yogesh Jaiswal: Okay.

Rithika Murthy: Um my portfolio company is essentially Mutiny. Uh they they have like an AI agent which helps you in creating like personalized

Gagan Bhaisa: Jesus.

Rithika Murthy: landing pages and any anything customerf facing for GTM.

Yogesh Jaiswal: Okay.

Rithika Murthy: Um I've identified the ICP as like account executives, uh product marketing and ABM teams. Uh I've also included like GTM engineers and strategist. is specifically people who are in-house and not like agencies for this. Um,

Yogesh Jaiswal: Huh?

Rithika Murthy: and my understanding is they're essentially helping GTM teams get to yes faster. Um, now in terms of like triggers, right? uh like beyond like hiring signals and events I'm thinking uh is there any signal that I can identify when a company goes from pure PLG to like an SLG or a hybrid motion uh so that you know it's uh very representative of uh the product and as well as uh things like compliance like certification like your certifications will typically uh become higher as you move from SLG motions because you're uh reaching out to enterprise customers.

#### 00:09:52

Rithika Murthy: So like sock uh type 2 and DPDP things like that. So uh is there any triggers like that you can think of?

Yogesh Jaiswal: So you want to check if the company is moving from PLG to SLG right this the first small

Rithika Murthy: Yeah. Yeah.

Yogesh Jaiswal: check see it's very easy I mean if any company is high on hiring sales people they are doing going SLG only like salesled growth

Rithika Murthy: Mhm.

Yogesh Jaiswal: because why like if you see good companies um they don't have like lot of sales people if the product is really good like phone pay right they don't have so many sales

Rithika Murthy: Mhm.

Yogesh Jaiswal: people but if you see razor pay they have like so many sales people doing sales. So very easy I think you just detect you can create a formula in clay and detect that if uh people are more in the sales team and directly it's a sales company.

Rithika Murthy: Okay.

Yogesh Jaiswal: Uh yes but we we can do that. I think that's not a problem.

Rithika Murthy: Okay. Uh can certifications and like compliance become a trigger uh like if they're applying for like soft type 2 and things like that.

#### 00:11:04

Yogesh Jaiswal: So what does your company does which you selected?

Rithika Murthy: So essentially my thought process here is we are reaching out to enterprise customers not like startups or like um mid-level companies.

Yogesh Jaiswal: Okay. Okay.

Rithika Murthy: So typically uh if they're going enterprise, if they're if they're moving up market means they would also uh go for a lot more compliance and certifications, right?

Yogesh Jaiswal: Okay, I'll check on this. I don't understand the company which you have selected.

Rithika Murthy: Okay.

Yogesh Jaiswal: So maybe I have to check it properly because I think you have not even mentioned in the sheet that's why I've not checked or maybe you have yeah mutiny

Rithika Murthy: Okay.

Yogesh Jaiswal: right customer okay I'll check this and maybe

Rithika Murthy: Yeah.

Yogesh Jaiswal: like give you after this class only the response okay uh All right.

Rithika Murthy: All right. Yeah. Yeah.

Yogesh Jaiswal: Yeah. So, uh others Shubham,Khushboo,Deepshikha,Sat, you have created a list of 50 accounts.

sampath vemulapati: Yeah. Yes. You wish.

Yogesh Jaiswal: Wow, that's good.

#### 00:12:11

Yogesh Jaiswal: Okay. Uh so, yes. Uh is this in a Google sheet or a CSV file?

sampath vemulapati: Uh mine is in a Google sheet. I'll be sharing uh in a while, but I would also want to take you through my logic behind putting the filters and prospo. Will that be okay?

Yogesh Jaiswal: Yes. Yes, that's fine.

sampath vemulapati: Yeah. Um you want me to?

Yogesh Jaiswal: So, can you share your screen and

sampath vemulapati: Yeah. Yeah, that's it. Yeah. Just give me a second.

Rithika Murthy: Uh this is

sampath vemulapati: Uh is my screen visible?

Yogesh Jaiswal: Yes.

Rithika Murthy: Oops.

sampath vemulapati: Yeah, this is the filters I've taken. So, first of all, I'll take tell you what my companies. The company I've chosen is um Goji Berry AI. So they basically help the companies B2B SAS companies or any other companies to uh to do more of sales and my thing was if they help uh their target customers are companies who have who cannot afford SDRs right so I I searched

#### 00:13:30

Yogesh Jaiswal: Oh s***.

sampath vemulapati: for uh people who are head of sales VP sales co founders uh And since this company's founder is from their addressible market is uh US, UK, France, Germany, Netherlands only not any other country. So I've created the personal location and company location like that. And then of course put in the verified emails only. And then company type I put it as a IML, data analytics and SAS. Um and further the industry I've given as like these both um and after that I kept the head count in the department as not more than 11 people so that like they may need an automation in that and then uh basically this company uh goji berry uh finds the right leads for them and then does the automation and sales. So I thought I'll just uh keep it this way. And this is how I um I got around uh some,000 72 uh sorry 625 results.

Yogesh Jaiswal: No, no. So, sorry. We need companies, not people. I think you got confused.

#### 00:14:42

Yogesh Jaiswal: We need top 50 pe company list.

sampath vemulapati: Okay.

Yogesh Jaiswal: Yes.

sampath vemulapati: Uh okay.

Yogesh Jaiswal: Not people we would find in clay itself I think. Yeah. If you click on click on company.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. We need companies.

sampath vemulapati: Got it. Got it.

Yogesh Jaiswal: here.

sampath vemulapati: I'll set my filters again the same and I'll get back to you then.

Yogesh Jaiswal: Yes. Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. For others also we need accounts means companies in GTM engineering. Account and companies are same. Uh not people. Okay. Yeah. Alokyou have also you have not done people right? Only companies.

Alok: Yeah, companies.

Yogesh Jaiswal: Uh is it done ready for you?

Alok: Yeah. Yeah. Done. I push it into Google Sheets.

Yogesh Jaiswal: Okay. Okay. Yeah.

Khushboo: So my company is Oxen. Uh they uh they sell to anyone who use AI tools like any company that is like they basically monitor um where your cost is going uh is it like uh what

#### 00:15:40

Yogesh Jaiswal: Mhm.

Khushboo: your spending are you getting like ROI but then it's very industry agnostic was a logic. So I'm like how to then filter like cuz every company like a lot of them use AI tools but there's no specific sector they cater

Yogesh Jaiswal: So try to uh go through the website and understand that if you are reaching out for the first time, what are the top 50 companies you're going to reach out? Very easy.

Khushboo: Okay. So like big enterprises that must be having a lot of AI tools,

Yogesh Jaiswal: Yes,

Khushboo: right?

Yogesh Jaiswal: no need to worry about selecting like downloading a 50 company list but it should be valid companies when you reach out.

Khushboo: Okay.

Yogesh Jaiswal: So the reason is I'll tell you what what's the reason behind right now you're only keeping 50 companies when you do in like uh when you do real GTM engineering this 50 increases to 500 or,000. So then it gets uh like easy for you to understand that we are just working on a sample 50 data but in reality that there is no 50 company data.

#### 00:16:51

Yogesh Jaiswal: You often reach out to 500,000 companies if they are small companies.

Khushboo: Okay. Okay. I think I'm done. Thank you.

Yogesh Jaiswal: Got it. Uh yes, can you share your screen and show it?

Alok: Yeah. Can you all see my screen?

Yogesh Jaiswal: Yes. Yes.

Alok: So uh as you said I have uh selected like the 50 companies uh in case you all don't know my company sells

Yogesh Jaiswal: Okay.

Alok: an AI tech AI solution for in-house legal teams.

Yogesh Jaiswal: Okay.

Alok: Yeah. And

Yogesh Jaiswal: Can you scroll to the right? Okay. Okay. Can you scroll more? Okay. Uh, I'll tell you what you need to keep and you can remove the rest.

Alok: f***

Rithika Murthy: I don't know.

Yogesh Jaiswal: Only keep.

Alok: them.

Yogesh Jaiswal: Yeah. Only keep company name, company domain. main company LinkedIn and URL and you can remove everything.

Alok: company name, domain and company URL.

Yogesh Jaiswal: Yes. Can you push it like company name is at this front now slide company domain to the second G g.

#### 00:18:14

Alok: Where is company domain? Okay.

Yogesh Jaiswal: Yeah. Yes. Slide it. Yes. only company doain.

Alok: Yeah.

Rithika Murthy: Yeah.

Yogesh Jaiswal: Yes.

Alok: Yeah.

Yogesh Jaiswal: And also company LinkedIn URL. Yes.

Rithika Murthy: Hello.

Yogesh Jaiswal: Now delete everything after industry.

Alok: everything.

Yogesh Jaiswal: Yes. Go to industry. Wait, I'll show you. Go to industry.

Alok: Yeah. Yeah,

Rithika Murthy: Speech. Speech.

Alok: I think.

Rithika Murthy: Speech.

Yogesh Jaiswal: Huh? Delete it. Yes.

Alok: Yeah.

Yogesh Jaiswal: So you have company name. Yeah. Also delete the industry.

Alok: Okay.

Yogesh Jaiswal: Yes. Yes. For everyone we need a list like this. Okay. Because we are going to do everything in clay. Uh so we would enrich it more. Okay.

Alok: That's

Yogesh Jaiswal: Now uh name name the sheet as company sheet.

Alok: okay.

Yogesh Jaiswal: Yeah. Yes. Come company sheet. Okay. Cool. Okay. Got it.

#### 00:19:38

Yogesh Jaiswal: Yes. Now just stay there. Yeah. So uh for others we have to come to this part and the next part is moving that data into clay. Okay. So before even we logging into clay from here whatever I'll be teaching into clay you will be doing it okay I'll be just guiding you because it becomes very easy for you to learn if you do it so you just have to do it uh the way I'm going to guide second clay is again uh okay sorry to cut you uh sorry to cut here but anyone here have used clay earlier or like everyone is learning for the first Okay. Okay. Three have used. Okay. Got it. Perfect. No worries. So um as you have used if you understand it's a very easy to go use tool. Uh okay. Also in clay we just want to mention that it is an orchestration platform where anything and everything you do is GTM engineering either clay will have that feature or clay will have a third party company which is linked to clay.

#### 00:20:48

Yogesh Jaiswal: Okay. So that means this is the reason everything is possible in clay. You can understand it's a place or it's a software where everything is possible and if it's not possible by clay Clay have enrichments or uh uh connections like like for example we need email right so if clay will not have emails clay have a waterfall of other providers okay so yes uh so uh yeah Alokcan you open clay just just open clay I'll guide you how to sign up yes just say open a new tab and share the screen and uh open clay.com Yeah.

Alok: Just a second. Oops.

Yogesh Jaiswal: Yes. Click on start free trial. Yes. For others also you just need to follow this process. Okay. We start free trial. Sign up with Google. Yes. Yes. continue. You can just select anything. No problem. Okay. Click on skip video. Yes. Yes, you can just click anything and click on start building.

#### 00:23:00

Alok: Oops.

Yogesh Jaiswal: Yeah. Now click on the first. Yes. And click on start building this. Okay. Now click on back. Yes. Now wait here. Okay. So for others this is the process to enter cla. Okay. Now I'm going to give you several steps for you to understand that whenever you use clay these are the basic things you need to make it right. Okay. Now first is the client folder. Right. So right now we are learning. So can you create a folder? Uh hello go to new.

Alok: Yeah.

Yogesh Jaiswal: Yeah. Okay. Just stop when you click on new. Yes. Wait. Uh no no. Can you click on new again and just show the options?

Alok: Yeah.

Yogesh Jaiswal: Yes.

Alok: So there are two options workshop workbook and folder.

Yogesh Jaiswal: Yes. So workbook means there. Okay, just a second. Yeah, workbook means that okay, you know Google sheet right how a Google sheet works you have one sheet and there are multiple sheets inside a Google sheet okay the same way workbook also works okay now you have folder which contains multiple workbooks okay so click on the folder yes name it okay yes Now again click on new and new workbook and name it company.

#### 00:24:34

Yogesh Jaiswal: New workbook name it as company. Okay. Yes. So now you have a list of uh the companies you have downloaded. Right.

Alok: Yeah.

Yogesh Jaiswal: Okay. Is it in a CSV file?

Alok: CSV.

Yogesh Jaiswal: The the same one which we have edited.

Alok: CSV. Yeah, it's in CSV.

Yogesh Jaiswal: Okay. Okay. Which we have edited. Right. the only three columns that one.

Alok: No, no, no. Wait. I I will just download it again.

Yogesh Jaiswal: Okay. Okay. Yeah.

Alok: Uh, should I download it as a CSV?

Yogesh Jaiswal: Yeah. Okay. Wait, wait, wait. No, close this. Yes. Close this. Yeah. Click on add. Yeah. Click. No. No. Add. Add. Down. Down.

Alok: Okay.

Yogesh Jaiswal: Yeah. Yeah. Stop here. So we have several methods of pushing data to clay. Okay. First is import CSV.

#### 00:25:54

Yogesh Jaiswal: Okay. Uh I click just type web hook.

Alok: Okay.

Yogesh Jaiswal: Okay.

Alok: Should

Yogesh Jaiswal: Web hook is a live table where you will not open clay. Clay will automatically work the way you set it up. So web hook means if I have a team of 20 people and I don't want to create new tables again and again, I would sit down create tables. It's a web hook table. Webbook is a live table. Okay. Everything would be automated. Yeah. Uh yeah, you can close uh close this. Yes. Now.

Alok: I import?

Yogesh Jaiswal: Yeah. Yeah. Click on import. Okay. Select the sheet. Yeah. Browse files and select the sheet. Yes. Click complete. Complete. Yes. Okay. Yes. Now close the right option. Yes.

Alok: Which option?

Yogesh Jaiswal: The right panel. Close it.

Alok: Okay. Okay.

Yogesh Jaiswal: Yeah.

Alok: Got it.

#### 00:26:56

Yogesh Jaiswal: Okay. Now, the first thing that you need to do in clay. It It's going to be important for the next at least 6 months of GTM engineering. Go to auto run and turn it off. Good.

Alok: Where is

Yogesh Jaiswal: Yeah. Click on this. Okay. Turn it off. Okay. See, auto run means that whenever you do anything in clay,

Alok: that?

Yogesh Jaiswal: there is an enrichment, okay? Or there is a process. And anything you do is going to be charging you right now. Auto run means that when you create a table and it works perfectly but suddenly you do some changes it will start uh charge auto working automatically. Okay, running automatically that's why we don't use auto run. Okay. So first basic thing to note at least for the next not six at least four to 6 month auto run should be off. Okay, unless it's a web hook table, auto run should be always off. Okay, because you if you still make a mistake, that's not a problem.

#### 00:28:04

Yogesh Jaiswal: If auto run is off, there can be no mistakes. Okay, one more thing. Uh can you go to any column and try to delete it? Don't delete it. Just click on this. Yeah, can you see an option? Go down. Delete option. Don't click on this. But yeah, so one more thing that for the next at least 3 months, whatever you do in clay, don't delete anything because you cannot get data back in clay the way you get in Google sheet. So if you delete a column, the data is gone. There can it cannot come back, right? So always hide and unhide. So click on hide. A look. Yes. Click on hide. Yes.

Alok: Oh,

Yogesh Jaiswal: So you Yeah. And now if you want to get it back, go to the col uh 25 columns, click on this. Yes.

Alok: okay.

Yogesh Jaiswal: Yes. Now go to LinkedIn URL. Click on this.

#### 00:29:01

Yogesh Jaiswal: Okay. That's how you get it back. Okay. So for the next at least 3 months, whatever you do in clay, don't delete anything. Okay. Many people screw up their entire play account or play re u features when they uh do delete it because you if you delete the column you need 50 credits to get the data back. Okay,

Alok: I don't think

Yogesh Jaiswal: cool. So now we have company name, company domain and company LinkedIn URL, right? Uh from a company point of view, if you need to do anything related to company, you need company domain or a LinkedIn URL. Okay, for a person point of view, if you need anything for the person, you need the person LinkedIn URL. Okay, now we have the company and now we have everything. Okay, now uh yes, click on add column. Yeah. So now I'll show you how you can find people in uh this click. Okay. Yes. Uh click on add column.

#### 00:30:10

Yogesh Jaiswal: No. No.

Alok: Yeah.

Yogesh Jaiswal: Yeah. Scroll down. Click on uh add enrichment. Sorry. Yes. Yeah. Just stop here. Yes. So if you see these are the enrichments which are endless in play. Okay. Can you scroll down?

Alok: Okay.

Yogesh Jaiswal: Okay. So okay just stop here. Yeah. So you you are you can easily understand right if a company total funding means what is the total funding of a company right? Company latest funding means latest funding of a company. Click on latest funding. Alokjust for a sample. Okay. Waterfall means you use several providers. So go to full configuration. Yeah.

Alok: Okay.

Yogesh Jaiswal: Now waterfall means that Clay is definitely not here to give you the data. Clay has partnered with these companies and will give you the data. Okay.

Alok: You know Let me

Yogesh Jaiswal: So waterfall means Clay will not have individual data provider, right?

#### 00:31:16

Yogesh Jaiswal: They would have multiple and you can use accordingly. Okay. Now you can close this uh tab. I look. Yes. Yes. Now click on add. So now I'll show you how you can No. No. Add. Down. Add. Okay. No. No.

Alok: Okay.

Yogesh Jaiswal: Down. No. Yeah. Add. Find people. Yes. Click on this. Find people. Now I'll show you how you can find people in clay itself. Okay. So left go down. Okay. Now you need to select the company list which you have created. Okay. So click on uh company identifier.

Alok: Yeah. Okay.

Yogesh Jaiswal: Yes. Okay. Wait. So when you need to search people on clay, you need to map three things. Okay. First is the sheet. So see the sheet company sheet. Sheet one. Can you see the first one company table?

#### 00:32:11

Alok: Yeah.

Yogesh Jaiswal: Okay. The sheet is mapped. Second is the view. It should be default view. Okay. Third, select the company domain. Okay. Now, Apollo uh it will act as a data provider for you. Okay. Now, let's say what what is your ICP of the company.

Alok: My ICP would be any company which would have a very small uh in-house legal team preferably from 1 to five.

Yogesh Jaiswal: Okay. So, you you will sell to legal people, right?

Alok: Yeah. Yeah. In-house legal teams.

Yogesh Jaiswal: Okay. Now left, go up. Yeah. Click on left. Go up. Go to job title. Yes. Now in the Job title. Yeah. Click on job functions. Okay. Select legal. Yes. Okay. Just stop here. Yes. There are 79 legal people in your uh TAM with 50 companies, right?

Alok: Yeah.

Yogesh Jaiswal: So for a sample, just click on continue.

#### 00:33:25

Yogesh Jaiswal: Okay. Save to a new table. Okay. Yes. Click on save and run. Yeah. Can you can you turn this off? Enrich person if possible. Left. Yeah. Tick mark that one. Yes. Okay. You cannot. Okay. Okay. No. Fine. Click on save and run 10 rows. Yeah, you can close the left panel. Yes. Now turn turn off the auto run.

Alok: Where is Okay, here it is.

Yogesh Jaiswal: Yes. Again any new tab tab table anything auto run should be off. Okay. Now you understood that how you source people in clay itself. Okay.

Alok: Yeah.

Yogesh Jaiswal: So can you see you have a list of people connected to a company right? Okay. So whenever you run an enrichment in clay right uh the enrichment will only run on one row or 10 rows. Okay or all rows right? So whenever we test something we test on 10 rows okay not one row.

#### 00:34:47

Yogesh Jaiswal: Got it? Because how can you come up to a conclusion that first enrichment is right? You need to run 10. Okay. Now go to the left sheet again. Left sheet. Company sheet again.

Alok: Come finish it.

Yogesh Jaiswal: Yes. Okay. Close this. Yeah.

Alok: I can stop screen sharing

Yogesh Jaiswal: No, no, no. Close the tab. Right. Right tab.

Alok: the great app.

Yogesh Jaiswal: No, no. The right tab which you open tools tab.

Alok: Okay.

Yogesh Jaiswal: Yeah. You will never close the clay tab. Right. I mean we are working clay. So uh hide this update people sheet. Yeah. Hide it. Okay. Now I'll show you how you can get the company details in clay. Right. So I'm going to start from basic enrichments. Okay. We will then move to complex enrichments. Okay. Now let's assume that you have these companies to sell.

#### 00:35:56

Yogesh Jaiswal: Right? This is the only data you have. Right? So how would you go about it? So click on add column and click on enrich company. Okay. Yes. Add enrichment. Enrich company. It's down. Yeah. Okay. Now what is wait what is company identifier means? Company identifier means when you run an enrichment the enrichment will use certain information.

Alok: What's this?

Yogesh Jaiswal: Go to I button. Yes. What is what does it what's it uh what's written company LinkedIn URL company domain sales

Alok: Um

Yogesh Jaiswal: navigator URL. So you have LinkedIn URL right? Okay. Now click on continue to add fields. Okay. Now you can output more information. Right. So output the employee account. See you already have the name and website. Don't output that. Yes, you already have that information. Okay. Now, output employee count, size, industry. Okay.

#### 00:37:00

Yogesh Jaiswal: Scroll. No, no, not this. Scroll down. Type also the type. Country, locality. Yes, we don't need founded information. Yes. Scroll down. Yeah. Annual revenue. Okay. Yes. Now click on save. Save and run 50. Okay. So wait wait wait. Can you see that it tells save and run 10 rows and 50 rows. So in clay it will always be 10 rows or or all rows. Okay. It will never give you one row. So now click on 50 rows.

Alok: Okay.

Yogesh Jaiswal: Yes. So it will now start giving you the information you need. Okay. So now the company list is ready. Okay. So this basically means that whenever you are doing something in clay, you don't need to worry about the data part. Okay. You can fill all the missing information. Right? So these 50 companies now even have more information.

#### 00:38:15

Yogesh Jaiswal: Okay? Now I'm going to show you more things here. Okay? Now go to the right. Enrichment.

Alok: Sorry. Where?

Yogesh Jaiswal: Uh enrichment. Add last column. Go to the last column. Yes. Yes. Now wait. Now you have more options. Company funding, company latest funding, right? But when you you know when you have a feature called AI, it becomes very easy for you to um use anything in in AI,

Alok: That's a

Yogesh Jaiswal: right? with AI uh searching any company. So there is a thing called agent. Okay.

Alok: Miss

Yogesh Jaiswal: Now click on use AI. case. Okay. Now, yeah. Now, this is a very powerful thing, right? It it basically acts as an AI on top of everything you do in play. Okay. Now, let's assume we want to check if these companies have raised funds in the last 6 months or not. Okay. So, it's very easy.

#### 00:39:19

Yogesh Jaiswal: Can you can you prompt it? Can you write a prompt? Check if the company Yeah.

Alok: Can you repeat?

Yogesh Jaiswal: Check if the company have raised funding in the last 6 months or not. In the last 6 months or not? Now stop. Yeah. No, no,

Alok: I forgot.

Yogesh Jaiswal: no. Now a new new new column. Oh, sorry. New line. Yeah. Click on company like right company. Yes. Now insert the column. Now can you see that sign of type? Yeah. Now se insert company domain. Okay. Yes. Now okay. Wait. This area is called a prompter. Okay. Prompter is used to write prompts. Okay. The reason you don't write complete prompts is we don't know how you write the prompts and which will work on clear or not. Okay. So use prompter.

Alok: Yeah.

Yogesh Jaiswal: Now click on generate.

#### 00:40:25

Yogesh Jaiswal: Now this is a this was a prompter. Now prompter will write a prompt. Okay. Okay. Wait. Now can you read this like give a slight read?

Alok: Um like we are using providing it context, objective and instruction like the entire prompt is divided into three sections.

Yogesh Jaiswal: Yes. Now, can you go down one thing? You just need to check one thing. Okay. Go to the Go down. Go to examples. Yes. Now, check the example. See, every prompt you write will will have an example outcome. Okay. So, can you see an example? If funding is found, this information you will get. If funding is not found, you will get that information. Okay. Now go up. Okay. Anything you do in clayent. Okay. Click on model. Yes. Anything you do in clayent cleaggent is also having separate different models. Okay. Anything which is textheavy use GPT.

#### 00:41:49

Yogesh Jaiswal: You can use your own plugins. Okay. GPT you can use your own plugins. Claude you can use your own plugins. Okay. But anything you would be doing related to web search Always use helium. So now go up. Yeah, helium. So the method is if helium doesn't work then use neon. If neon doesn't work use argan. Okay. Right now you see recommended is argan. Right. But argan cost three credits. Okay. Now select helium. Okay. Yes. Now go down. No. No. Go down. Okay. Yes. Wait. In the output format there are two options. Uh click on fields. Uh hello. Yes. Click on field. Okay. Just click the click here.

Alok: No, I'm not able to

Yogesh Jaiswal: Okay. Okay. No problem. So we have two options fields and JSON schema. Right.

#### 00:42:45

Yogesh Jaiswal: Because we are going to also learn advanced ETM engineering. We are going to connect clay to multiple AI tools. Okay. Or multiple code bases. So JSON is a language which is understood by any technical software right. So whenever you create a prompt give like make this a habit uh click on JSON schema and click on generate from prompt. Click on generate from prompt. Yes. Click on this. Okay. Now it will generate a JSON schema output prompt for you. Right. Go down. Yeah, just click on save and run 10

Alok: save.

Yogesh Jaiswal: rows.

Alok: Okay.

Yogesh Jaiswal: So you will run on 10 rows and see how it's working. Okay. Hey, You see it's working right? You have two companies which raised funds in the last 6 months. Okay.

Alok: By the way, can I bring in my own API key for this?

Yogesh Jaiswal: What you need to do here like with an API? Which API?

#### 00:44:43

Alok: like rather than like for the models.

Yogesh Jaiswal: No, no, no. Clay there is their own AI model.

Alok: Okay.

Yogesh Jaiswal: Yeah. And it's very good. So you don't need to worry. Okay. So click on the response the green one First the green one. Okay. Now wait after clicking. Okay. Uh can you see confidence? Confidence high.

Alok: Yeah.

Yogesh Jaiswal: Okay. The reason it's green because the confidence is high. Right. So you can use this information. Okay. Now click on the orange one. The triangle one. Yes. Now you will see the confidence is medium. Okay. That's why it's orange. you can use it but whenever the confidence is low or red color you cannot use that data. Okay, this is just a suggestion for now. You don't have any uh red one, but don't use anything where the confidence is low. Right now, run everything.

#### 00:45:49

Yogesh Jaiswal: Go to the um yeah, click on the uh triangle button. Recent funding. This this button. No, recent funding. Yeah, the the Yeah, this button. Yes. Run empty rows.

Alok: run 40 empty rows,

Yogesh Jaiswal: Yes.

Alok: right?

Yogesh Jaiswal: Yes. Okay. Now stay here on the green one. Can you see that you got some outputs here? Notes, amounts, reasoning. Okay. Now you also got steps taken. Click on steps taken. Yes. Can you see? It means it has visited the website and got the information. Okay. So you can always output these as column. Click click on notes. Yeah. And see you have an out add to column option. Don't click anything without uh Yeah. Can you see you have an add to column option. Okay. So if you want nodes as a column, click on add to column. Add add to column.

#### 00:46:53

Yogesh Jaiswal: Yes. See you can create column. So this column will come here. Okay, now you can delete this nodes because you already have nodes. Yes, you can delete the nodes column. Okay, now whenever you run an enrichment, the first thing you need to do is change the names. Okay, the names are not right of the column. So change the use AI use remove the use AI. Okay. Click on this. Double click on this. It will pop up as a rename. Okay. Yes. Yes. H.

Alok: Okay. So like if we have used AI so it gives use here.

Yogesh Jaiswal: Yeah. Yes. And whenever you use clay, I advise don't use it like click anywhere, click like that. Okay. Always be careful because everything is expensive here. Okay.

Alok: There he is.

Yogesh Jaiswal: Yeah. Cool. So you can close this last funding date tab. Okay. Now you got that information.

#### 00:48:19

Yogesh Jaiswal: Okay. Where where companies have raised funds. Okay. Now scroll down. Okay. Yes. So go to raised in last 6 months. Click on the race. Yes. Click on filter. Filter on this column. Yes. Okay. Wait. So whenever we use filters in clay the filters are same as we use in any we use in superbase or we use in any uh tech

Alok: Can't open.

Yogesh Jaiswal: uh any tech platform. Okay. Cursor or anything. So you need to understand several things what it means. Okay. Click on equal to. Yeah. Yeah. Wait. Equal to means the information is exactly equal to what you write. Okay. Even upper case and lower case is a problem. Okay. So it needs to be exactly same. So for an example uh I look right true but t capital enter see it is not working right now.

#### 00:49:30

Yogesh Jaiswal: Why? Because t is capital. Now make t small. So it worked right? So equal to means everything should be exact even upper case and lower case. Okay. Now click on not equal to. Yes. Again write true. Not equal to means it will exclude true. So you have all the false. Okay. Now go to again uh the column the filters. Yes. You have contains.

Alok: Whoops.

Yogesh Jaiswal: Okay. Go to contain. Yeah. Write true. So contains means. Yeah. Now you can even write capital true. Write capital true and it no. Yeah. Now it will work. Can you see it works? So contains will not have a problem with anything. any text contains capital true or uh anything it will work. Okay. Now click on contains any of yes. Now you can add more values here. Now write true.

#### 00:50:52

Yogesh Jaiswal: Enter. Now you can write false also. White falls. Okay. So, contents any of can add more values, unlimited values. Okay. Now, close this. No, no. Stay on the filters. Don't close the filters. Okay. Yes. Click on open that. Yeah. Now you have does not contain. Okay. That exactly means equal to not equal to and does not contain any of also have multiple filters. Clip one does not contain any of you can add multiple filters. True and false. Okay. Yes. Yes. No need to add. No problem. Close this. Yeah. Don't close. Yeah. Just Yeah. Open this. Okay. Now you have empty and not empty. Right. This is a very easy to easy thing for you to use it because it it it makes your work easy. Okay.

#### 00:51:55

Yogesh Jaiswal: So, close this. Yeah. Remove the filter. Yeah. Go to last funding date. Yes. Filter it as not empty. Filter not empty. So all the columns which were empty, you have filtered it. Okay. So see the data is now easy for you to use. Okay. Let's say you want to reach out to companies which have raised funding in the last 6 months. You just do this. Now click on click to empty.

Alok: What's

Yogesh Jaiswal: Yes. Okay. Now these companies have not raised the funds in the last 6 months.

Alok: Jesus.

Yogesh Jaiswal: So it's very easy to use the filters for empty and not empty as well. Okay cool. Uh now clear filters. Okay just just a second. Uh others do you have any questions till this part? Anything or any uh are you understanding?

Rithika Murthy: I have a quick question. Um,

Yogesh Jaiswal: Yes.

Rithika Murthy: why are we starting with the company and then going to the person and why are we not doing that natively on clay?

#### 00:53:18

Yogesh Jaiswal: Uh, sorry, I don't like Are you saying we should move people data to Clay

Rithika Murthy: No, I'm asking why are we not doing the company level search on clay itself and why are we firstly starting with the with the company level search?

Yogesh Jaiswal: view with with Rosio or Apollo? This is that a question?

Rithika Murthy: Yeah. Yeah.

Yogesh Jaiswal: Okay. Um see if Rithikayou and me start a company today and we go on to LinkedIn and we mentioned it as a 500 to,000 employees company

Rithika Murthy: Mhm.

Yogesh Jaiswal: right this is what we do right and we would name it as a AI technology company okay but is that a valid company in the market no Eight. the domain is not opening.

Rithika Murthy: No.

Yogesh Jaiswal: Uh the employees are not right. So Clay data is scraped data.

Rithika Murthy: Mhm.

Yogesh Jaiswal: Clay just scraped LinkedIn data and the data is here. So if you search companies on on clay definitely most of the companies would be wrong.

Rithika Murthy: Okay.

Yogesh Jaiswal: So data provider will always be there apart from uh see clay will have the data but if you ask me from a strategical point of view you would not use that data.

#### 00:54:34

Yogesh Jaiswal: You would use the people data for sure. See,

Rithika Murthy: Okay. So,

Yogesh Jaiswal: no one can create Yeah,

Rithika Murthy: can you see?

Yogesh Jaiswal: no one can create multiple fake people accounts, right?

Rithika Murthy: Mhm.

Yogesh Jaiswal: But you might be shocked. There are so many people from India, small cities who mentioned we are CEO at Google, CEO at Microsoft and that will pop up in in clay.

Rithika Murthy: Okay.

Yogesh Jaiswal: Okay,

Rithika Murthy: Okay.

Yogesh Jaiswal: that's why right right now I think two years of working I have never used place data like just to be transparent never used but again I have seen people who use

Rithika Murthy: Got it.

Yogesh Jaiswal: it and uh they also do good so again that's a if you have a tool like cross apollo then no need to use it

Rithika Murthy: Okay, got it. And why did we start with company level search and not person level search?

Yogesh Jaiswal: okay Um we need to also understand that when we reach out right the first thing we check is at company levels right like the first qualifications we do is as per the company if the companies raise the funds if

#### 00:55:38

Rithika Murthy: Mhm.

Yogesh Jaiswal: they have hiring if they have a team then we come up to a conclusion that the company's right to reach

Rithika Murthy: Okay.

Yogesh Jaiswal: out okay so right now the 50 companies you have still I don't feel

Rithika Murthy: Got it.

Yogesh Jaiswal: it's valid Right. So it's just here because you thought it was good. Right. Now we need to do a QA.

Rithika Murthy: Yeah.

Yogesh Jaiswal: Okay. So we are just doing a QA here.

Rithika Murthy: Okay. Okay.

Yogesh Jaiswal: Okay.

Rithika Murthy: Got it.

Yogesh Jaiswal: Yes. Uh also just to make it easy. This is also called account scoring. Okay. If any account falls in a positive uh parameter, it's a score. So if company raised the funding in last 6 months, you can have a score of plus two. Okay. So this just keeps goes on and when an account reaches 10 then it's a high quality account and you might reach it out and we we would be learning that as well.

#### 00:56:29

Rithika Murthy: Okay.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: you you one question here you said uh if the number goes to

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: 10 it become a higher tire I mean but I've seen a different example on on uh basically threshold based scoring how that is different from uh you said a titanium scoring

Yogesh Jaiswal: So are you talking about like a score 1 to 10 and then you go upon on the score or like you create tires.

Gagan Bhaisa: Uh no I mean uh what I have seen the approach on scoring is quite different uh anything on femographic demographic and activity level. So the score you are talking about is it quite similar or that has a different uh meaning all al all Appreciate it.

Yogesh Jaiswal: Uh see honestly I think scoring is just the formulas we use. Okay. I think we need to understand that the parameters still are the same. So if we keep five parameters in signals like when you create the strategy sheet and the parameters are funding, hiring, recent expansion, expanding to new country and uh maybe open roles in tech, right?

#### 00:57:46

Yogesh Jaiswal: Let's see five signals. Now you have had that five signals in clay and some of the accounts like are falling into a positive parameter then you can just add a score of 1 to 10 no need to do even tiering 1 to 10 means then this is general amongst every account scoring 1 to 10 means if a account scores 7 to 10 then you should reach out immediately okay if a account score 4 to six then you should just nurture it just send warm emails, uh, stay connected with them on LinkedIn and don't sell them something, right? And one to three, you just avoid it because they don't have a positive score. This is what Yeah,

Gagan Bhaisa: Got it.

Yogesh Jaiswal: this is what I've seen. But honestly,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: uh, I don't think we should even judge a a company by its signals. Even companies with no signals like they can buy. So, uh, I think this is just a step that we do to understand that if account is Yeah.

Gagan Bhaisa: Got it.

#### 00:58:46

Gagan Bhaisa: Got it. Do you I mean on an extension to that do you also I mean do we also decay the score decay the

Yogesh Jaiswal: Do we also uh sorry like what does that

Gagan Bhaisa: score so so let's say someone who have

Yogesh Jaiswal: mean?

Gagan Bhaisa: got uh let's say we're looking for a data for last 6 months I would say past six month and within past

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: six month the threshold like this guys has raised a fund and then we scored them one and now the time has already passed 6 months. Do you also mark them zero from one to zero?

Yogesh Jaiswal: So you are saying that in the past 6 months if they have not any we don't have any

Gagan Bhaisa: Yeah. Yeah.

Yogesh Jaiswal: signals we move to more like 8 n months like that.

Gagan Bhaisa: Yes. Do you also let's say the score is now I mean technically looking everything the score is now 10. Uh but within next 6 month uh they would have not gone into any function. Nothing's happened.

#### 00:59:46

Gagan Bhaisa: No signal to catch. Okay. Do you also DK? Why? Because I'm saying uh since uh we studying about outbound strategy uh what I'm

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: thinking outbound strategy. So let's say one I am a GTM engineer I runs a outbound this time with this signal. So let's say I want to target the same account next cycle maybe after two or 3 months I would not catch all the signals and that's why the I mean the account would not come on the top line. So but since that's a uh I mean high ICP for me to sell how does that work on outbound strategy?

Yogesh Jaiswal: Got it. See there are several parameters which we will learn. First of all, we don't run funding recent funding on 6 months. We run on 3 months. Okay.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Uh second on the hiring point of view, we don't run open roles which are like posted one year ago, right? Because you you may find companies which are hiring for people and the roles are open from like 6 7 months.

#### 01:00:50

Yogesh Jaiswal: Okay. So there are parameters for every signals but when when we set up every parameter the problem is that the account becomes less. Now you have 100 accounts you run everything and you only get five accounts or 10 accounts which are right. So definitely we should extend the uh signal like move to 3 to 6 months. um make it more easy for the accounts because honestly signals are also not playing a very important role in selling something into the market.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: But we just use it to understand that the data we are using is correct or not because I have seen accounts with no signals are performing good. they are buying stuff and uh accounts with every signal they are not doing

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: really good. So let's keep signals as qualification methods to understand how qualified an account is. But definitely uh you can extend the timeline or you can even uh slow like make it more loosen to get better result.

Gagan Bhaisa: Gossip.

Yogesh Jaiswal: Yes. But definitely we would be going extensive in this.

#### 01:02:04

Yogesh Jaiswal: We just started it. But yes, uh a good question you have asked. Okay. Uh yeah. Yes. Aut.

sampath vemulapati: Uh yoga I was also a little curious to understand uh even uh

Yogesh Jaiswal: Mhm.

sampath vemulapati: Prospio had um more filters right like if we can get the filters like funding and everything from prospia itself like can that data be more uh qualitative that way?

Yogesh Jaiswal: Yes, definitely. So, you may see Prospio even have filters, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Uh Prosp have funding filters and you won't you will be shocked that data providers are also focusing on coming with signals. Okay? So that means if data provider can give you information like recent funding, recent uh LinkedIn activity, uh open job roles and you know open job roles are also there in Apollo by the way in a you can see

sampath vemulapati: Yeah.

Yogesh Jaiswal: this now recent expansion. So we need to just understand here that databases can also do the work. Okay and clay can also do the work.

#### 01:03:11

sampath vemulapati: Yeah.

Yogesh Jaiswal: Now this is where the term GDM engineering comes in right engineering means from both the methods which is the most ideal method which is the most cost-saving method and which is the most scalable method. What if you download data from Prospio which tells that the funding is done in the last 6 months and the data is not correct. Okay, so your whole messaging goes haywire, right? But Clay's enrichments are at least correct. But again, we have not checked Prospio. So it's very easy. You pick up a sample 100 accounts start from Prospio and just recheck and claim if the information is correct. If the information is correct then you just keep on using it

sampath vemulapati: Understood. So I mean clay is better in that way like I mean we can still do a

Yogesh Jaiswal: I mean no one

sampath vemulapati: lot of working on clay then

Yogesh Jaiswal: yeah but clay is expensive and everyone is trying to eliminate usage in clay so if you feel that the funding filter is working perfectly in prospio then why don't we use prospio because uh makes no sense for us to do it again Right.

#### 01:04:26

sampath vemulapati: I didn't see.

Yogesh Jaiswal: And uh there is one more filter uh which is popular in data tools like technographic filters. Okay. So you can even go to prospin and check technographics. You can check if the company is using Salesforce or not or this or not. But we need to also be super clear that uh how efficient because those filters are not good. Okay.

sampath vemulapati: Okay.

Yogesh Jaiswal: Yeah. So the filters in Clayis better in terms of technographic. So that is for sure. I mean I want to give you a green flag that anything technographics don't use prospio or a polo. Okay.

sampath vemulapati: Mhm.

Yogesh Jaiswal: Uh clay is better because clay use builtwith and builtwith is a separate company who does technographics. Okay.

sampath vemulapati: Okay.

Yogesh Jaiswal: Now uh there is a way to use Apollo and Prospio inside clay with Apollo's and Prospio's API. Okay, that's a very advanced and high level thing which we would learn later. Okay, that there is a way out.

#### 01:05:26

Yogesh Jaiswal: There is a way to use Apollo and cross Q inside Claywith APIs. Okay, but it's a very advanced thing and I don't want to like teach you now because uh I mean you might get confused. So um yeah apart from that any questions.

Deepshikha: Uh,

sampath vemulapati: Okay.

Deepshikha: Yogesh when you said uh the whole messaging can go haywire, I believe by messaging you mean strategy.

Yogesh Jaiswal: Yes.

Deepshikha: Yeah.

Yogesh Jaiswal: See when you create a strategy where you are reaching out. Okay. So the statary document you've created is still not perfect right the strategy document will also contains a part called execution so if I'm selling razor pay in in the Indian market how will I execute it whom will I reach out first what messaging I will have let's say I'm selling razor pay I would reach out to Indian small businesses let's say I'll reach out to automotive industry first what messaging I'll use you are selling spare parts you are paying this amount uh with razor pay you can pay less premium or get better feedback, better process.

#### 01:06:30

Yogesh Jaiswal: So we have still not worked on the strategy document perfectly but the execution depends on signals and the signals are directly related to the messaging. Okay. So if you do a customized outreach everything should be on track. You cannot have a wrong in because see just imagine and I have even done that mistake. I have mailed a person that you have raised a funding round in the last six months. Right now that person replied that we have never raised a funding round. The company we acquired raised the funding in the last 3 months but we are the parent company. We have never raised the funding round. Okay. And that information came through Prospios uh Prospio's latest funding round detail. Okay. So that's where I again ran an enrichment in Clayand I got to know that that person never raised the funding round. But the company that they acquired raised the funding. So you need to be super clear that don't use signal. I mean it's like for a very uh easy example let's say if sat gets married tomorrow.

#### 01:07:38

Yogesh Jaiswal: I would not send him an email that congratulation on getting married uh now I'll sell sell you a honeymoon package like that. Okay. We need to use signals for um you know we need to use signals to understand that the company is on the right shape right now and we can sell something. Okay. So even if I send an email to sat that okay this is a uh honeymoon package I want to sell you from make my trip and I feel it's a right time you would sat will still have a look into it rather than I'm going sad and giving the same information which is there with him okay so same with the company you cannot just go to the company and say oh you have raised a funding round in the last 6 months I mean they know that right and they don't care also if you know it so you need to be clear that the messaging will contain the information but will not contain the exact information. If they are hiring for 10 sales per people, you cannot say that oh we saw you're hiring for 10 salespeople.

#### 01:08:39

Yogesh Jaiswal: I want to sell you a sales tool. No, we can use that information is like is uh in the way like we saw your sales team is expanding. Okay, now let's say you want to make it much better. We saw your sales team is expanding in Delhi, right? We are already working with several companies in Delhi like Lambda Test and Service Now. Okay. We offer a sales transformation uh tool uh which we want to show you and how we can help your team as well because I saw recently in the news you are also expanding into new products and new features where you need my help. Okay. So you need to understand the messaging should contain signals but should not contain signals in such a way that you are just giving information back to them. Okay. And this is where you need a lot of sales knowledge. But honestly it's just it comes very easy when you keep on doing it. Okay. Cool. Uh any questions?

#### 01:09:44

Yogesh Jaiswal: Any other people? Uh KhushbooAlokGagan sampathShabazDeepshikhaany other thing? Okay. So very easy. I would ask you to just uh do what we have done till now. Create a top 50 account list which is a company list. Upload it into clay and run a basic enrichment of Yeah.

Gagan Bhaisa: It feels focused.

Yogesh Jaiswal: Run a basic enrichment of enriched company and run another enrichment of uh last funding date. Okay, last funding round funding round in the last 6 months. But follow the best practices. Auto run off. Run an enrichment on 10 rows first. Always select Helium and see how it's working. Change the names of use AI, use AI and don't delete any column. Um yeah, I think this is it. Cool. So try doing this uh and tomorrow we would again go more extensive. See what we have done is just 10% in clay. Not even 10 like 5% in clay. Okay.

#### 01:10:55

Yogesh Jaiswal: But I just want to make sure you it becomes very easy for you to use clay. So you use you whenever there is a clay task you will not get uh overwhelmed by it. Okay. So this is where we have to reach but again the core remains same. The strategy document you have created should be the strategy you will follow. You will just use clay to execute the strategy. Okay? I mean there is a thing going on online where people are more focused on tools. They just talk about tools tools tools. Okay? We don't need to do that. We are going to use Clayto make our strategy successful. Okay. So that should be the prime goal. Okay. Cool guys. So uh be ready with this part in play. Uh you can sign up. Uh Alokcan you see how many credits you got? I think you got 1,000 credits. Yes. Yes. So Clay was giving 5,000 credits. Now 2,000. Not today. It It's at 1,000. Okay. No, that's not a problem. So cool. U yeah. So please come till here do till here and um let's connect uh tomorrow for more extensive task like formulas and run conditions and other things. Okay, any questions or we can end this. Cool guys. Uh have a nice ahead and uh let me know if you need any help. Okay, again keep the context same. Play is only used as a tool to make your strategy successful. Okay, we don't need to go into clay as play some revolution and something like that. Okay, it's just going to make your strategy successful. Okay, cool. Cool. Guys, have a nice day. Have a nice day.

#### Transcription ended after 01:25:05

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.