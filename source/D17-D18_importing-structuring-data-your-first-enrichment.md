# D17+D18_ Importing & structuring data + Your first enrichment - 2026_09_18 08_56 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D17+D18: Importing & structuring data + Your first enrichment

Sep 18, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Data enrichment workflow review and Clay automation setup for GTM engineering

Clay data import and deduplication methods

Yogesh demonstrated importing and mapping additional CSV files into Clay to manage data efficiently.

Yogesh explained that webhook tables used for automations typically do not require deduplication.

Company enrichment and domain discovery workflows

Yogesh reviewed waterfall models in Clay to find company domains and minimize credit usage.

Yogesh demonstrated using AI prompts to discover company domains when waterfall results are inaccurate.

ICP targeting and persona filtering

Yogesh demonstrated searching for ICP decision-makers in Clay using seniority and job function filters.

Yogesh showed how to apply formulas in Clay to categorize job titles into executive levels.

Email verification and MX domain optimization

Yogesh explained setting up run conditions in Clay to execute enrichments selectively and conserve credits.

Yogesh recommended using a separate email verifier instead of waterfall verifiers to reduce costs.

Yogesh explained that MX domain analysis identifies workspaces like Outlook or Google to optimize deliverability.

Yogesh advised against connecting Claude to Clay via MCP due to high Clay credit consumption.

Clay platform automation and feature training

Yogesh demonstrated automated enrichment workflows in Clay, including email validation and MX domain outputs.

Yogesh advised using the AI enrichment domain column instead of the company domain waterfall.

Yogesh recommended selecting the helium model first when running AI prompts in Clay.

Contact enrichment and data filtering strategies

Yogesh explained that filtering top decision-makers requires an additional enrichment step after finding company contacts.

Rithika noted that reaching out to multiple stakeholders improves response rates compared to single-contact outreach.

Portfolio project and weekend assignment planning

Yogesh announced a weekend portfolio task requiring participants to process company lists through Clay.

Sampath confirmed the team can use their existing dataset of 50 companies extracted from Crosspio.

Next steps

[Medha Das] Finish Training Task: Complete the remaining Clay training exercise by the end of the day.

[Medha Das] Perform Razorpay Enrichment: Find company domain, enrich business details, target the ICP, find professional emails, and validate contact information for Razorpay.

[Yogesh Jaiswal] Send MX List: Provide the list of restricted MX domains that should be excluded from outreach campaigns.

[The group] Enrich Company Data: Use Clay to process 50 company records. Perform enrichment for domains, identify target contacts, and validate email addresses.

[Yogesh Jaiswal] Assign Weekend Task: Provide specific instructions and guidelines for the weekend portfolio project. Create tasks that require applying multiple Clay features to company lists.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 18, 2026

### D17+D18: Importing & structuring data + Your first enrichment

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D17+D18: Importing & structuring data + Your first enrichment

Meeting records Transcript Recording

#### Summary

Data enrichment workflow review and Clay automation setup for GTM engineering

Clay Data Import and Enrichment
Yogesh Jaiswal guided Medha Das through importing company data via CSV, mapping columns, deduplicating entries, and running enrichment for employee counts and locations.

Email Waterfalls and Verification
Yogesh Jaiswal explained email waterfall configurations, run conditions based on seniority, and MX domain routing for deliverability while advising against direct Claude API usage.

Pipeline Exercise and Weekend Task
The team practiced end-to-end pipeline workflows using test companies like Razorpay, and Yogesh Jaiswal assigned a weekend portfolio task processing 10 companies.

#### Next steps

[Medha Das] Finish Training Task: Complete the remaining Clay training exercise by the end of the day.

[Medha Das] Perform Razorpay Enrichment: Find company domain, enrich business details, target the ICP, find professional emails, and validate contact information for Razorpay.

[Yogesh Jaiswal] Send MX List: Provide the list of restricted MX domains that should be excluded from outreach campaigns.

[The group] Enrich Company Data: Use Clay to process 50 company records. Perform enrichment for domains, identify target contacts, and validate email addresses.

[Yogesh Jaiswal] Assign Weekend Task: Provide specific instructions and guidelines for the weekend portfolio project. Create tasks that require applying multiple Clay features to company lists.

#### Details

Clay Platform Task Status and GTM Engineering Agency Plans: sampath vemulapati reports that they are still enriching company data on Clay, noting that they initially downloaded people data by mistake before rejecting it and downloading company data. Yogesh Jaiswal shares plans to launch their own GTM engineering agency and is currently figuring out client targets and documentation (00:05:26). sampath vemulapati offers assistance based on their prior experience registering a private limited company and managing compliance (00:06:50).

Screen Sharing Technical Issues: sampath vemulapati experiences technical difficulties and a heating laptop while trying to load Clay, prompting Gagan Bhaisa to offer their screen (00:06:50). Gagan Bhaisa opens a guest Clay account since they have not added companies yet, but also encounters technical issues due to being logged into two systems (00:07:52). Medha Das reports being midway through their Clay task and shares their screen after Yogesh Jaiswal instructs sampath vemulapati to close extra browser tabs (00:09:43).

Importing and Structuring CSV Data in Clay: Yogesh Jaiswal reviews Medha Das's screen and explains that when files from external sources like Apollo or Prospio are added to an existing sheet, columns must be manually mapped (00:11:03) (00:17:04). Yogesh Jaiswal guides Medha Das through the import tool via CSV, instructing them to map columns such as company name, domain, and LinkedIn URL (00:12:00). Yogesh Jaiswal demonstrates how to save the imported data without running it immediately and verifies that all 50 companies appear in the table (00:14:31).

Deduplicating Company Data and Handling Webhooks: Yogesh Jaiswal instructs Medha Das to delete duplicate company entries and ensure domain and LinkedIn URL columns are deduplicated (00:15:52). Gagan Bhaisa asks how to handle deduplication for live data or webhooks from website intent tracking (00:17:04). Yogesh Jaiswal explains that webhook tables are typically used for automations and are not deduplicated because new visits are treated as fresh information, though manual deduplication remains possible (00:18:05).

Company Enrichment Practice and Client Data Workflows: Yogesh Jaiswal instructs Medha Das to add an enrichment column to pull employee counts, industries, country locations, and annual revenues for 50 rows. Rithika Murthy questions why they are running enrichments on Clay when the data was already downloaded from Prospio, noting extra credit costs (00:19:12). Yogesh Jaiswal explains that this serves as a practice exercise because real clients typically provide only a list of company names rather than pre-enriched Prospio data, requiring practitioners to find domains and enrich details themselves (00:20:24).

Configuring ICP Contact Searches: Yogesh Jaiswal instructs Medha Das to add an ICP contact search enrichment to find relevant decision-makers within the same sheet (00:21:28). Medha Das and Yogesh Jaiswal configure the search filters, targeting C-suite to Vice President seniorities with exact matching, job function set to finance, and keywords related to accounting AI agents (00:22:32). Yogesh Jaiswal notes that search results are capped at 10 people to verify strategic decision-maker presence (00:24:55) (00:27:24).

Extracting and Categorizing Personas Using Formulas: Yogesh Jaiswal instructs Medha Das to output full names and job titles for returned contacts while explaining that Clay indexing starts at zero (00:26:07). To categorize titles, Yogesh Jaiswal guides Medha Das to insert a custom formula column that evaluates whether a title contains "chief" (outputting "C level") or "VP"/"vice president" (outputting "VP"), highlighting the role of basic mathematics and formulas in GTM engineering (00:27:24).

Domain Waterfall Search and Alternative AI Methods: Yogesh Jaiswal outlines the outreach workflow starting from company names, finding domains, enriching company details, and identifying personas (00:30:55). Yogesh Jaiswal instructs Medha Das to use a waterfall domain search configured with prioritized, low-cost credit providers while removing Clearbit (00:32:11). Rithika Murthy notes discrepancies between Prospio domains and Clay waterfall results for certain companies, prompting Yogesh Jaiswal to demonstrate an alternative AI prompt method (`Find the company domain`) that successfully generates correct domains for companies like Premier Search (00:33:27).

Setting Up Email Waterfalls with Run Conditions: Yogesh Jaiswal introduces email waterfall configurations in Clay and instructs Medha Das to map fields like name and domain while disabling expensive providers like Smartlead (00:37:51). Yogesh Jaiswal guides Medha Das to establish a run condition ensuring the email waterfall executes only when the seniority level strictly matches "VP", thereby conserving credits (00:40:08).

Email Verification and Workflow Redundancy: Yogesh Jaiswal instructs Medha Das to add an external verification tool called Enrichly to a new column with a run condition checking if an email is available (00:43:21). Gagan Bhaisa questions why an additional verification layer is needed when the waterfall already includes a verifier. Yogesh Jaiswal clarifies that the built-in verifier was retained for learning purposes, but in practice, it is redundant and should be removed from the waterfall settings to avoid extra expenses (00:45:10).

Email Infrastructure and MX Domain Routing: Yogesh Jaiswal instructs Medha Das to output MX domain and validation result fields, distinguishing between valid and catch-all valid emails (00:47:10). Gagan Bhaisa asks about the purpose of the MX domain column, and Yogesh Jaiswal explains that MX domains identify email workspaces (Outlook versus Google) so outreach can be matched (e.g., sending from Outlook to Outlook) for higher deliverability (00:48:33). Yogesh Jaiswal and Gagan Bhaisa discuss security tags like Proofpoint and Mimecast, with Yogesh Jaiswal explaining that these tags help filter out domains protected by cybersecurity systems to prevent sequencer blocks (00:51:20). Rithika Murthy asks for clarification, and Yogesh Jaiswal shares their screen to demonstrate workspace output examples, promising to provide a list of restricted MX domains like Mimecast and Barracuda Networks (00:52:33).

Evaluating LLM Integrations with Clay: sampath vemulapati asks whether Claude can be directly connected to Clay to extract lists using commands. Yogesh Jaiswal advises against it, explaining that Clay credits are expensive (costing $190 for 2,000 credits) and direct API usage is much more efficient unless working with a heavily funded plan (00:55:23).

Practical Pipeline Exercise on Razorpay: Yogesh Jaiswal has Medha Das open a fresh sheet and input a test company name, "Razorpay", to practice the end-to-end pipeline (00:56:29). Yogesh Jaiswal guides Medha Das through company domain waterfalls, company detail enrichments, and ICP contact searches (00:57:56). Rithika Murthy asks about the difference between "find people at a company" and "find contacts", and Yogesh Jaiswal explains that the former creates a new table while the latter keeps data within a single sheet (01:01:07). Medha Das runs the ICP search, identifies seven finance contacts including a senior director of finance, extracts their full names, LinkedIn URLs, and job titles, and sets up work email enrichments after removing redundant validation providers (01:02:44).

Clay Tool Demonstration and Automation Setup: Yogesh Jaiswal guided Medha Das through running integrations, including email bison, and performing email validation within Clay (01:04:26). Yogesh Jaiswal demonstrated how to establish automations by adjusting row ranges and inputting company names like PhonePe, while Rithika Murthy confirmed the functionality of the auto-run feature and client workflows (01:06:49).

Filtering and Contact Selection: Medha Das asked how to select specific individuals among seven contacts for various companies, and Yogesh Jaiswal explained that an additional enrichment step for filtering top personnel was omitted during this initial learning phase (01:07:57). Rithika Murthy raised concerns about low email reply rates of 2 percent and suggested reaching out to multiple stakeholders volumewise, prompting Yogesh Jaiswal to note that domain errors required the AI enrichment domain column and that they were conducting a test run before scaling up to 50 companies (01:08:57).

Domain Enrichment and Model Selection Troubleshooting: Yogesh Jaiswal instructed Medha Das to bypass the company domain waterfall due to performance issues and instead use the "Find the company domain" tool, selecting the helium model first before trying alternatives (01:09:59). After addressing processing delays attributed to similarly named companies, Yogesh Jaiswal directed Medha Das to stop screen sharing and disable the auto-run feature (01:13:15).

Weekend Portfolio Task and Dataset Management: Yogesh Jaiswal outlined a weekend portfolio task requiring the team to process 10 company names by finding domains, checking ideal customer profiles, locating appropriate contacts, and validating emails (01:14:11). When sampath vemulapati inquired about the existing 50 companies extracted from Crosspio, Yogesh Jaiswal clarified that they could utilize that dataset but restricted the specific assignment to 10 companies to prevent errors in Clay (01:15:21). Yogesh Jaiswal committed to finalizing the detailed task instructions, and the participants agreed to reconvene on Monday (01:16:11).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 18, 2026

### D17+D18: Importing & structuring data + Your first enrichment - Transcript

#### 00:05:26

sampath vemulapati: Hi everybody.

Yogesh Jaiswal: Good morning sampath.Uh sampath,you have done with the clay thing.

sampath vemulapati: Yeah, I'm still doing it actually. So I'll be showing I think by towards the end it's still getting enriched.

Yogesh Jaiswal: Okay. Okay. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: But you have signed up in play,

sampath vemulapati: Yeah,

Yogesh Jaiswal: right?

sampath vemulapati: I have signed up. I signed up with Clay and then I'm uh I did go through certain uh just things actually.

Yogesh Jaiswal: Got it.

sampath vemulapati: Yeah,

Yogesh Jaiswal: And you also download the company data, right?

sampath vemulapati: complete data has been downloaded. Yes.

Yogesh Jaiswal: Perfect.

sampath vemulapati: So yesterday I actually got confused and I downloaded uh this thing actually uh people data uh but got to know that this company

Yogesh Jaiswal: The people data.

sampath vemulapati: so I rejected it.

Yogesh Jaiswal: Yes.

sampath vemulapati: But how are things otherwise all okay?

Yogesh Jaiswal: Yeah, perfect. Perfect. All good.

sampath vemulapati: So which are the exciting projects you're working these days?

Yogesh Jaiswal: Uh, so I'm planning to open my own agency uh for GTM engineering.

#### 00:06:50

sampath vemulapati: Oh, nice.

Yogesh Jaiswal: So that's that's the only thing I'm working on. And uh yeah, figuring out like what kind of clients to work for and documentations and everything.

sampath vemulapati: Okay, let me know. I mean, if you need any help because uh I have a I mean I registered a private limited earlier and

Yogesh Jaiswal: Oh,

sampath vemulapati: it's a compliance.

Yogesh Jaiswal: nice.

sampath vemulapati: So, it's just that uh you know have to be very careful.

Yogesh Jaiswal: Oh, that's good. Yes. Yes. Hey. Hi, Gagan.Good morning.

Gagan Bhaisa: Hey you guys.

sampath vemulapati: Hi.

Gagan Bhaisa: Hey,

Yogesh Jaiswal: Okay.

Gagan Bhaisa: how's it day guys? Add morning copy.

sampath vemulapati: No, no, not yet. Still have to.

Gagan Bhaisa: Uh no,

sampath vemulapati: What about you?

Gagan Bhaisa: I just uh read from a run and then yeah,

sampath vemulapati: Oh, nice,

Gagan Bhaisa: straight to the system.

sampath vemulapati: nice,

Yogesh Jaiswal: Oh,

sampath vemulapati: nice.

Yogesh Jaiswal: that's good. Cool. Uh, so sampath,can you share your screen to Clay if possible?

#### 00:07:52

sampath vemulapati: Uh just you'll have to give me a second because you know it's still going.

Yogesh Jaiswal: Hello.

sampath vemulapati: In the meantime uh if you Gaganif you want to share I'll have to u I think it's still getting enriched and then the screen is blank right now.

Gagan Bhaisa: Yeah.

sampath vemulapati: I don't know what's maybe it's something wrong with my laptop.

Yogesh Jaiswal: Oh,

Gagan Bhaisa: Yeah. Do you want me to share Yogesh?

Yogesh Jaiswal: yeah. Yeah. Sure. Sure. Yes. Yes. Yes. If you can to play.

Gagan Bhaisa: Yeah. But the bad thing is I have not added those uh companies.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Yeah. Uh bear with me. This is my company's part. The clear system.

Yogesh Jaiswal: Oh, can you sign up a free clay account like uh Yeah.

Gagan Bhaisa: I I think I do have just

Yogesh Jaiswal: Yeah. I mean it will just be safe for you to like use it.

Gagan Bhaisa: Yeah. Continue the guest.

#### 00:09:43

Yogesh Jaiswal: Hey. Hi. Good morning, Medha.

Medha Das: Hey. Hi everyone.

Yogesh Jaiswal: Hi. Uh,

Gagan Bhaisa: Just Give me

Yogesh Jaiswal: yeah. Yeah, please. Please. Uh, Ma, you have done the clear task.

Medha Das: Uh no Yogeshis that is uh pregnant for me. I mean I started with but then I'm just mid way through it. I I'll complete it today.

Yogesh Jaiswal: Okay. Okay. No problem.

Gagan Bhaisa: uh guys anyone can uh share the screen. I think mine is getting into trouble. I mean I have two system logged in into one uh system. So that's a problem.

Yogesh Jaiswal: Uh Medhacan you share your screen to play if possible?

Medha Das: Uh yes, just give me one second.

Yogesh Jaiswal: Yeah. Yeah. Then you can stop share.

Gagan Bhaisa: Yeah, sure. Sure.

sampath vemulapati: Mine is still not working because I don't know must like my laptop is also heating up.

Yogesh Jaiswal: for clay.

sampath vemulapati: Uh yeah well I have other tabs also open any which

#### 00:11:03

Yogesh Jaiswal: Okay. I think that uh it's not a problem with clay. Maybe something else.

sampath vemulapati: clay should not be a problem right okay like I have like almost 20 tabs open

Yogesh Jaiswal: Yeah.

sampath vemulapati: for Excel actually in some other

Yogesh Jaiswal: Yeah. I think Yeah. You need to close that and only keep it to play.

sampath vemulapati: so Yeah.

Yogesh Jaiswal: Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. Cool. Uh so yes I think we I'll help you out s but no need to worry with that. So cool.

Gagan Bhaisa: It's still

Yogesh Jaiswal: Uh so you can see that while uploading the data Medhahave uploaded the data and you know these are the three columns right now there is one more thing uh which we need to keep in mind that sometimes we don't have claw right and we have other files also that needs to be put into the same file. Okay that structuring the data is uh very difficult because you need to map columns one by one. Okay.

#### 00:12:00

Yogesh Jaiswal: So, uh, MedhaCan you close this company LinkedIn URL tab?

Medha Das: Uh, which one? Sorry.

Yogesh Jaiswal: Yeah, the company LinkedIn URL. The right tab. Can you close it?

Medha Das: Oh, this one.

Yogesh Jaiswal: No. Cannot see your mouse cursor. Yeah. Can you close? Yes. Yes. Click on this one. Yes. the box next to the pencil.

Medha Das: Yeah. Yeah, it it was not loading. Let me just uh put into it.

Yogesh Jaiswal: Oh. Mhm. Okay. Yeah. Can you go to tools now? Yes. Click. Yeah. Click on import. Yes. So this is where you can add more files to the same file. Okay. Now click on import from CSV. Yes. Yes. Now, now select the file again which you have selected. Okay. Now just wait. Uh yes. Click on continue.

#### 00:13:37

Yogesh Jaiswal: Yes. Now just stop here. Okay. So whenever you add a new file to the same Okay. New sheet to the same sheet you need to map out the columns.

Gagan Bhaisa: Sorry.

Yogesh Jaiswal: Yeah. So uh Medhacan you click uncclick on select all?

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes. So now there are two options here. Okay. One is the file you one is the sheet you have right now and one you uploaded.

Medha Das: Listen.

Yogesh Jaiswal: Okay. So the one you uploaded you can see the columns right. Now click on company name.

Gagan Bhaisa: There you go.

Yogesh Jaiswal: Select company name. Okay. Now go to the right and yeah drag down the column. Yes. Pick the right one. The right one. Yes. Click on Yes. Click on this. Okay. Can you see company name, company domain, company LinkedIn URL? Okay. Now, click on new column. Yes.

#### 00:14:31

Yogesh Jaiswal: No. Click on this again. Yeah. Click on new column. Oh, no. Go back to it again.

Medha Das: Yeah,

Yogesh Jaiswal: I think you've missed it. Yeah.

Gagan Bhaisa: Quick.

Yogesh Jaiswal: Yes. Click on continue. Okay. Yeah, no problem. So just just click on company name. Okay. Now select company name. Okay. Yes. So this means that you are now mapping the sheets to the same sheet. Okay. Now select all. Yes. And click add to table. Okay. Yes. Save and don't run. Yes. So now you will see that. Okay. See on the left. Yeah. Scroll down. Okay. Just just go to company name column just the top one. Yes. Yes. Click on this and click on did you go down? Yeah. Click on this. Now can you see now you have all of the companies in this table also.

#### 00:15:52

Yogesh Jaiswal: Now click on value. Yeah. Click on the up one. Yes. How many companies do you see?

Gagan Bhaisa: s***.

Yogesh Jaiswal: 50 right? Yes. Now click on delete. Yes.

Gagan Bhaisa: s***.

Yogesh Jaiswal: Yes.

Medha Das: Okay.

Yogesh Jaiswal: Yeah. Delete it. So this is how you ded click. Okay.

Medha Das: Okay.

Yogesh Jaiswal: So whenever you add another and you have to do it for both of the things domain and LinkedIn URL also. Yeah. Now did you for domain and LinkedIn URL both? Yes. Okay. For domain it's not there. Check for LinkedIn URL. Okay. Okay. No problem. Yes. You can close this. You can close the right one. Yes. Okay. Now uh now whenever you need to add more data to the same sheet it's very easy. You just need to go to tools import and add more sheets to it.

#### 00:17:04

Yogesh Jaiswal: Okay. Now this typically happens when you have data from Apollo and then you need more data from Prospio right and your sheet is almost ready. So you cannot like move to a new sheet and create everything again. So what you do you go to tools you go to import and add more data again. Okay. Uh now have you enriched these companies you've not enriched right?

Medha Das: No, no, no. I just started and then I couldn't complete it.

Yogesh Jaiswal: Okay. Okay. So first enriched these companies. Add column enrich company. Yes. Add enrichment.

Gagan Bhaisa: you you guys I have I have a question here.

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: Yeah. So uh this uh pretty straightforward like when you have a different CSV format how about a live data like look at the web hook how do you ddoop them? So let's say uh I mean maybe this sound more advanced. Uh let's say we have a web intent website coming up and then you have same company

#### 00:18:05

Yogesh Jaiswal: Huh?

Gagan Bhaisa: visited your uh website twice maybe tomorrow uh sorry I mean yesterday and today how do you dilute them?

Yogesh Jaiswal: So you have one live sheet and one normal sheet, right?

Gagan Bhaisa: No,

Yogesh Jaiswal: Right.

Gagan Bhaisa: I have a live sheet.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: I have a live sheet. So I just want to make sure on a live sheet I don't uh make sure add

Medha Das: Okay.

Gagan Bhaisa: another column as X as a two companies.

Yogesh Jaiswal: Okay. On a web hook table typically we don't deduke it like it's it's a web hook,

Medha Das: Hold on.

Yogesh Jaiswal: right?

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: So any new information will be considered as a new information even though it was previously used. So web hook table generally is used for automations.

Medha Das: All

Yogesh Jaiswal: So we don't typically consider deduping it.

Gagan Bhaisa: Got it.

Yogesh Jaiswal: Yes. Yes. Uh but you can manually ddup whenever you want like but there's no need to it like best way to create a normal table if you don't want duplicates.

#### 00:19:12

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes. Uh yeah. Medha,can you click on enrich company?

Medha Das: right. Yeah.

Yogesh Jaiswal: Yes. Now, yeah. Lendon, you are continue to add fields. Yes. Now, output the information which is needed. Yeah. So, remove the first two because we already have the name and website. Yeah. Output the employee count size. Industry. Yes. Scroll down. Yes. Country location. Country location. Yes. Scroll down. Yeah. Go to the last. Yeah. Annual revenue and enrich it. Save and run for 50 rows. Uh yeah. Yes.

Rithika Murthy: Uh this data was available when we downloaded it from Prospio as well.

Yogesh Jaiswal: Yes.

Rithika Murthy: Uh why are we deleting it and again running it on Clay because it's going to cost extra extra credits, right?

Yogesh Jaiswal: Yes. Yes. That's right. So we are just doing practice.

#### 00:20:24

Yogesh Jaiswal: That's why we are doing it. I mean generally when we work with a client we don't get like okay I'll tell you how will will I get how will we get the data. You will just get a set of companies. That's it.

Rithika Murthy: Yes.

Yogesh Jaiswal: Generally, we don't get company data from client from prospio. We just get the names of the company that set up the outbound for these companies. So, we need to find the domain. We need to find everything.

Rithika Murthy: Okay. Um, I don't get it because uh we are getting this information from prosp right.

Yogesh Jaiswal: Yes. Yes. I'll I'll let you know. We are getting this information from Prospio. But right now in this exercise, we are not keeping from Prospio because for a very simple reason when you do GTM engineering for a client, most of the times when you reach out to a company, these companies would be given by the client. Okay? And client will only give you the names of the companies.

#### 00:21:28

Yogesh Jaiswal: So client will not go to Prospio and search a company list and give it to you. Okay. So you need to do the all of the enrichment. That's why you're practicing it. I mean rest if you want to use prospectio companies you don't need to do this. That's completely right. But for now for the practice purpose we are doing it.

Rithika Murthy: Okay. Okay.

Yogesh Jaiswal: Yeah. Okay. Uh now go to add column. Uh Medhaadd column. Yes. Now you know the ICP of it, right? Your company.

Medha Das: Uh yes.

Yogesh Jaiswal: Okay. Yeah. Click on add enrichment. Okay. So now we are going to find the ICP in the same sheet. Okay. Click on find contact at a company. Like search find contacts. Yes. The second one. Yes. uh in this in this table. Yes. Okay. Now in this table means you select save the result in this table.

#### 00:22:32

Yogesh Jaiswal: If a new table you can create a new table. Okay. Now scroll down. Okay. Now yes. No no no. Just go up. Go up. Okay. Now can you match your ICP here? Keywords seniority everything. Yes. What is your ICP?

Medha Das: So seniority level would be like director to see suit.

Yogesh Jaiswal: Yes. So, select H. Okay. Select the most senior one right now. Don't select everything. Let's get the top 10 uh ones. You can remove the director. Yes. Okay. And what? Yeah. Scroll down. You have job title also. Yes. Job title keywords. Okay. What are the keywords?

Medha Das: It would be uh CFO and like all the finance.

Yogesh Jaiswal: No. So wait, you cannot write CFO because you already have se right. So keyword would contain finance.

Medha Das: Oh okay.

Yogesh Jaiswal: Yes.

#### 00:23:46

Yogesh Jaiswal: Finance only finance roles.

Medha Das: Yeah. This because it's like a accounting uh AI agents for accounting. So mostly the finance leads would be the uh

Yogesh Jaiswal: Okay. Yeah. Now, yes. Now click on senior. Top. Yes. The top one. Top one.

Medha Das: Uh,

Yogesh Jaiswal: No.

Medha Das: which one?

Yogesh Jaiswal: Go. Go up. Seniority match mode.

Medha Das: Okay.

Yogesh Jaiswal: Yes. Now this means you want exact seniorities or like uh less and more. So select exact. Yes. Exactly. Okay. Now select floor level. Yes. Select floor level. Select as DP. Okay, that means you don't want to go less than VB. Okay, now scroll down. Yes. Now click on job functions. Functions. Yes. Select finance. Yes, it's up there. Okay. Okay. So, can you see you have more information now?

#### 00:24:55

Yogesh Jaiswal: Minimum number of months since start of the current role. That means when he started working as a CFO or a VP of finance, right? So you can get more information. Now scroll down. Yes. Now continue to add fields. Yeah. Click on continue. Yes. Okay. Save and run it for 50. Okay. Yes. So this is what you're doing. uh so what you're doing right now is searching people inside clay okay inside the companies this is generally used for strategical purposes okay so that means you have a set of companies and you want to check how many companies I have the right decision makers okay now click on return one people any anyone go up go up first go up yeah click on return two people to first

Medha Das: Oh,

Yogesh Jaiswal: one okay now this Just just understand Prospio and Apollo and clay, right? This is what is happening. Now click on people.

Medha Das: heat.

Yogesh Jaiswal: Yes. Click on zero.

#### 00:26:07

Yogesh Jaiswal: Okay. So clay will always have zero and one, not one or two. Okay. It starts from zero. Right. Now output the full name. The first the name. Go to name and add to column. Name. Name. N name. Yeah. Add to column.

Medha Das: Okay. Right.

Yogesh Jaiswal: Yes. Okay. Now output the job role as well. Title. Yes. Yes. Output it. Okay. Now close the 01. Yeah. Close zero and output for one also. Name and title. Yes. Okay. Now you can close the window. Okay. Now if you see the found people uh can you go left a bit left. Okay. When you see this return two people return one people. So whatever search filteration we have done right now this is only limited to 10 people. Okay. So,

#### 00:27:24

Medha Das: Okay.

Yogesh Jaiswal: whatever filters you add, it will only give you 10 people, okay? Not more than 10, right? That's why we are always conservative about the filters. That means we just want to check from a strategical point of view if we have the decision makers or not. Okay. So, can you see how many companies have the decision makers? You have chief financial officer, you have VP of finance. Now scroll down. Okay. So you have lot of companies with decision makers. Okay. Now go up. Okay. So it's very easy to understand that from the first name and title these are the prime matches. Okay. For whatever information you have given these are the top matches. Right now let's say if you have these matches but you want to separate companies where there are no people. Okay. Now go to title. Yeah. Yeah. Yes. Click on this. Add column to the right.

#### 00:28:35

Yogesh Jaiswal: Insert column to the right. Yes. Go to formula. Okay. Yes. Now this is where it becomes interesting. Okay. Uh this basically means that you can now control the information with formulas. Okay. So just write if if now click slashinsert to column. Yeah. Title is chief. Okay. Just write if title contains chief. Contains chief then output. Yeah. Then output C level and make it in comma. Yes. And if Yes. And if title contains VP. B. or vice president. Yeah. Then output VP VP. Yeah. Now click on generate. Yes. Save column. Okay. Now, can you see what is happening? Now, this is how you control the information in clay with formulas. Okay. That's why in GTM engineering, you need to have be a bit better in mathematics as well. This is very basic formula.

#### 00:30:55

Yogesh Jaiswal: But can you scroll down and check everything? Like if VPs are VPs, chief are chief. Okay, got it. Now let's do the same for the other title.

Medha Das: Okay. Like uh you mean like executive director?

Yogesh Jaiswal: Yes. Yes. So you have director as well. Okay. Yeah. No,

Medha Das: Yeah.

Yogesh Jaiswal: no problem. I think this is fine. Okay. So now we have an information. Okay. I just want to give you the broader view of it. Just imagine you starting the outreach. You all start the outreach when you just have a list of companies. Okay. Then you find company domain and then you enrich the company. Go at the starting ma starting column. Yes. Okay.

Medha Das: Goodbye.

Yogesh Jaiswal: In generally when you do GTM engineering you will only get the company names. Okay. Now any startup have consultants and partners they suggest that okay you sell to these companies right.

#### 00:32:11

Yogesh Jaiswal: So initially you will I mean as I said that prosp gives everything. Uh most of the times we get company's name from the client itself. Okay. So go to company name. Yes. Add call up to the right. Yes. Add enrichment. Yes. Now just imagine uh you guys don't have a domain. Right. Now click on domain. Yeah. Search domain.

Medha Das: Come on.

Yogesh Jaiswal: Yes. Yes. Company domain. Yes. Okay. Yeah. Go to quick setup. No, sorry.

Medha Das: Yeah.

Yogesh Jaiswal: Full configuration. Yeah. I'm And uh okay, whenever you use a waterfall, make sure you use the less charges credits top. So drag it. Drag Google to top. Yeah. Drag it. Yes. Now then company U. This one. H. Then snow view. Then edg insights. Delete clear bit. Yeah.

#### 00:33:27

Yogesh Jaiswal: Okay. Now save and run for five rows. No, sorry, 10 rows. 10 rows, not 50. Yes. So can you see you got the company domains?

Medha Das: All right.

Yogesh Jaiswal: Okay. So just imagine whenever you do outreach and you don't have anything, you just have a company name, right? The process is finding the domain, finding enriching the company. Okay, enriching the company will also give you LinkedIn URL. Okay, now you can delete the you can delete the domain tab.

Medha Das: Uh one quick question. So I see like we have couple of companies with different domain from like I took this data from crossview and if you see the domain is different for this company. So which one should we like refer to? I mean for like future

Yogesh Jaiswal: Yes. Uh can you okay just want to give you a heads up here that the company domain waterfall and clay is not better than prospio right prosper uh that's why if you see the domains like this premier search okay it's giving you mariambster.com I am doubting that this is not the right LinkedIn right right company URL there is one more way out go to

#### 00:34:56

Medha Das: Awesome.

Yogesh Jaiswal: company name. Yeah. Go to company name. No, the the first one.

Medha Das: Yeah.

Yogesh Jaiswal: Yes. Add column to the right. Use AI. Yes. Just prompt that find the company name. So the find the company domain. Yes. And enter into a new new line. No, no, no, no, no, no, no.

Medha Das: Oh.

Yogesh Jaiswal: Yes. Yes. Go to a new line. Yes. Write company name and map the company name. No. No. First write company name. Yes. So this is a prompter. You just need to make it easy.

Medha Das: Oh.

Yogesh Jaiswal: Yeah. Yeah. And map the company domain. Yeah. Company name. N name name. Sorry. Yes. Click on generate. Yes. Yeah, just select helium. Helium top. Yes. Just click on save and run for 10 rows.

#### 00:36:23

Yogesh Jaiswal: Now this will give you the right one. Can you see now? So it's right for premier uh search also. And for which one it was wrong?

Medha Das: Uh, let's Association for Medicine.

Yogesh Jaiswal: Yeah. See you have Yes. Okay. Okay. So there are these two ways of finding domains. Okay. Generally when you do waterfall it's right but sometimes you know if you validate and you consider it is wrong you can again do it like this way.

Medha Das: All right.

Yogesh Jaiswal: Okay. So if I give you to outreach 10 companies and if I just give you the company name can you take it from company name to in enrich domain to enrich company details to enrich personas you can do it right now.

Medha Das: Uh, yes. Here.

Yogesh Jaiswal: Okay now go to the right complete right okay now I'll uh explain you how to use a run condition. Okay. So, uh run condition means that Yeah. Just go to the add column.

#### 00:37:51

Yogesh Jaiswal: Yes. Okay. Now, click on add enrichment. Okay. Now, click on Yeah. Click on work email. Okay. Uh we are not going to use work email. I'm just going to show you now. Okay. Con full configuration. Yes. Scroll down. Okay. Now, this is a main um feature that we use Clay for. Okay. Because finding email is difficult and there are so many providers out there. Clay have a partnership with them. Okay. And uh you can just do a waterfall in uh Clay work email and you can find emails right now. Yeah. Uh go to the Yeah.

Medha Das: Okay.

Yogesh Jaiswal: Yeah. Can you can you map this waterfall properly? Arrange this.

Medha Das: Yeah.

Yogesh Jaiswal: Okay. And also try not to use smart key because it's expensive. So you can just uh close it. Yeah. Just turn it off.

#### 00:39:10

Yogesh Jaiswal: Okay. No, no problem. No problem. Okay. Now go to the uh go up. Yeah. Go to quick setup. Yes. Okay. Now scroll down. Okay. Now, this is where you need to do the mapping, right? So, check the go to the name and don't click anything. Yeah. Just stay here. Okay. Can you see the names up here? It's right.

Medha Das: Yeah.

Yogesh Jaiswal: Okay. Go to the domain. Check everything. Domains up here. Right. Okay. Uh for domain. Okay. Okay. It's it's right. Okay. Yeah. Check LinkedIn URL. Okay. We don't have the LinkedIn URL, right? H uh close this one. Let's output the LinkedIn URL as well. Or can you?

Medha Das: And you wish one quick question. So for domain we have like multiple columns in which

#### 00:40:08

Yogesh Jaiswal: Yeah. Select it. Open. Open this. Okay. Yeah. Click check. Click company domain. Yes. The earlier one we had. Yes. Now go to social profile URL. Yes. Yeah. Just just click on this. Oh, it's selected. Okay. Okay. Yes. H. Yes. Okay. Now go to the run settings. No. No. Run settings.

Medha Das: Okay. Okay.

Yogesh Jaiswal: Yeah. Okay. Okay. This means now you set up a parameter to run. Okay. like you will only run this when there are certain conditions which are met. So add run condition. Yes. Uh now add run only write run only if now select seniority level. Yes. is in bracket VP. Oh, sorry. No, in commas VP. Yeah. Generate. Okay. Click on save.

#### 00:41:38

Yogesh Jaiswal: Yes. And 50 50 rows. Yes. Okay. So it will only run for VPs if you see and click click on this arrow uh maida the arrow next to work email. Yes.

Medha Das: This way.

Yogesh Jaiswal: Yes. So this will open the waterfall. You can go to complete right and see. So waterfall is finding email and validating email. Okay, it's find and validate. If it doesn't validate then move to the other other provider. Okay. Now go to the top right. Yes. Go to right. H. Yes. Can you see you have those emails right now?

Medha Das: Thank you.

Yogesh Jaiswal: Okay. Now go to the left. Yes. Close the waterfall. Okay, scroll down. So, can you see it only ran for VPS?

Medha Das: Yes.

Yogesh Jaiswal: Okay, so this is where we we use run conditions to set up um the entire outreach. Okay, so we don't uh we don't burer credits.

#### 00:43:21

Yogesh Jaiswal: Okay, this is just smart view of using uh plane. Okay, now go to the right complete. Right. Yeah.

Medha Das: Yeah,

Yogesh Jaiswal: Add column.

Medha Das: this

Yogesh Jaiswal: Yes. Add column. Add enrichment. Okay. There is a famous tool called Enrichley. Okay. Just search enrichly. E N R I C H L Y. Yes. Click on verify email. This is enrichly. Okay. Select work email. Inputs. Inputs. Yeah. Work email. Okay. Yes. Yes. Scroll down. Continue to add fields. Yes. Uh now click on okay just go back scroll down now add a run condition that only run if the email is available only run if the select email. Yeah. Click on two items. Yes. Yes. Yes. Is available. Yeah. Click on generate. Yeah. Continue to add fields.

#### 00:45:10

Yogesh Jaiswal: Yeah. Save and run. Yeah. 50. Okay. So first of all from now if I ask you to run columns only when a parameter is met you can handle it right.

Medha Das: Oh yeah.

Yogesh Jaiswal: Okay. Uh now yes any questions? Yes. Yes.

Gagan Bhaisa: Uh since uh we use waterfall model and we have a verifier for every other uh data provider. Why and why we are using another layer of verifying email?

Yogesh Jaiswal: H Yeah. So we just added like we have not removed that verifier from the waterfall just because we are learning right now. I mean typically you should remove it. That's right.

Gagan Bhaisa: Uh, sorry. I didn't I didn't get quite get that one.

Yogesh Jaiswal: Yeah. So we have a verifier in the waterfall.

Gagan Bhaisa: Uh-huh.

Yogesh Jaiswal: We have not removed it because we are learning right now. I mean in in reality I will also give you best practices like

Gagan Bhaisa: No, no, no, no.

Yogesh Jaiswal: this.

#### 00:46:17

Gagan Bhaisa: But what I'm trying to understand since we have a verifier email verifier for each of the uh data

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: provider why we are using an additional plus verify email for from end.

Yogesh Jaiswal: Okay. We are just using it because if we don't use the verifier earlier,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: I mean we are just using it uh in the waterfall because I mean not a big problem.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: We are just practicing right now.

Gagan Bhaisa: I mean kind of putting it a guard.

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes. But in in generally we don't use it. So uh yeah uh maida go to work email. I'll show you how you can remove it. Yeah. Go to work email edit column. Okay. Full full configuration. Yeah. Go down. You'll find a verifier. Yeah. Go down. Yes. Yeah. Stop here. Validation. Yeah. Go to settings.

#### 00:47:10

Yogesh Jaiswal: Yeah. And just remove the provider. Okay. So you you can click on save and don't run. Yes. So basically when we were finding emails through a waterfall it is automatically validating but generally we don't use that model we use a separate verifier because it's expensive. Okay. So yeah click on catch all valid any anything click on it. Yes. Yeah. Now we need to output some important information always. Okay. Output MX domain and output valid. No result result. Sorry result result. Sorry. Yes. Yes. Result. Okay. So you can close this window. The right one. Okay. So now for every email you have a information that the uh result is catch all valid. Now scroll down. Yes. So can you see for valid you have a okay right? These are valid emails but some are cats. All valid. Okay.

#### 00:48:33

Yogesh Jaiswal: So you can even reach out to catch all valid. But do you have any invalid emails? No. Right. Okay. No. Because we already use the validation provider and work email. Okay. Got it. Cool. Yes. Gag. Yes.

Gagan Bhaisa: Yeah. What is the way around of adding a MX domain as a column?

Yogesh Jaiswal: What is the reason around it?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: So uh generally in uh generally in outreach for emails we use smart lead or email bison and uh or wait let me show you this.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: I can give you an answer. Okay, you can see my screen, right? Yes.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Uh can you see this this part?

Gagan Bhaisa: Yeah. Yes.

Yogesh Jaiswal: So generally when we do outreach we use certain outlook emails and certain Gmail emails, Google emails. Okay. Now for Outlook we will have our Outlook emails to send and for Gmail we will use a Gmail one.

#### 00:49:56

Yogesh Jaiswal: So the deliverability is very high.

Gagan Bhaisa: Okay. I mean what may uh uh you say I mean what I'm understanding uh you saying if somebody has a outlook as a domain provider we would use a outlook email created in outlook.com and then send the do a outreach from there

Yogesh Jaiswal: Yes. Yes, that's right.

Gagan Bhaisa: and why We cannot do from Google to Outlook.

Yogesh Jaiswal: See, we can do but generally it's not practiced.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: Uh So an Outlook to Outlook email deliverability is also

Gagan Bhaisa: Okay.

Yogesh Jaiswal: fast rather than Gmail to Outlook because see uh understand it's a se it's a

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: same uh same email provider. Okay,

Gagan Bhaisa: Okay.

Yogesh Jaiswal: that's why this is considered also as But uh and also when you purchase so many domains from Gmail or something it's very difficult to manage from one provider right so you can have two providers and uh this has been a practice from too long I can share you a article about it and maybe get more idea but right now in

#### 00:51:20

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: email infrastructure this is a practice that is being followed.

Gagan Bhaisa: Got it. Got it. Yeah. And also I see a proof point as a tag. Okay. Uh what I understood proof point is actually a uh cyber detection company.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: How does that link to the email infrastructure?

Yogesh Jaiswal: So we can even eliminate if we get proof point or mimcast here.

Gagan Bhaisa: Uh-huh. Okay.

Yogesh Jaiswal: So we don't do it manually.

Gagan Bhaisa: Okay. Got it.

Yogesh Jaiswal: So just imagine you have a list that you upload to any sequencer which contains a MX domain tag right now MX domain tag

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: will come into the tags and we'll start removing it uh removing time cast

Gagan Bhaisa: Okay.

Yogesh Jaiswal: removing proof point if it's Google or Outlook then outlook doing the outreach from Google or Outlook domains.

Gagan Bhaisa: Mhm. Gotcha.

Yogesh Jaiswal: Yeah.

Rithika Murthy: Uh could you explain what the what this MX point is like? Is it a different provider like Google and Outlook or um what exactly is it?

#### 00:52:33

Yogesh Jaiswal: Which one? Proof point.

Rithika Murthy: The MX uh point.

Yogesh Jaiswal: Yeah. Sorry. Uh MX domain is just to catch which email workspace you're using.

Rithika Murthy: Okay.

Yogesh Jaiswal: Yeah. So just an example uh if you see on the screen it says

Rithika Murthy: Mhm.

Yogesh Jaiswal: joshhsand.com is outlook right.

Rithika Murthy: Yeah.

Yogesh Jaiswal: So that means they are using outlook Microsoft outlook and

Rithika Murthy: Yeah, that I understood. Um I know that for Google and Outlook, but what is like MX point here?

Yogesh Jaiswal: MX domain is the technical term for it in uh email validation.

Rithika Murthy: Okay. So under MX is Outlook and uh Google is in Okay.

Yogesh Jaiswal: Yes. Yes. Yes.

Rithika Murthy: Okay.

Yogesh Jaiswal: Yes.

Rithika Murthy: Understood.

Yogesh Jaiswal: Yes. Uh so under MX domain you have several things. You have uh Okay. Let me show you if you want to see. Let me show you a bigger sheet that will give you some clarity. See the main goal is I don't want to complicate it for you.

#### 00:53:41

Yogesh Jaiswal: The main goal is to understand just let me share my full screen entire screen. Okay. Yeah. Can you see my screen? Yeah. Can you see MX domain gives me the output Outlook or even you can see from here, right? Outlook. This is all Outlook. Okay. And if I want to see Google, this is Google and Gmail. Okay. But if I want to see which are not Google, not Outlook. Okay. Can you see this? We can even send me uh mails to PP hosted. But to Mcast, it's not allowed.

Medha Das: Stop it.

Yogesh Jaiswal: Mcast blocks it. Okay, there's one more thing called uh Barracuda networks. If let me see. Okay, it's not there but we cannot even send to them as well. Okay, so I'll send you a list of MX domains which you cannot send. Okay, stop sharing. Okay, got it. Yeah. Uh Ma, can you share your screen?

#### 00:55:23

Yogesh Jaiswal: Yes.

Medha Das: Uh yes.

Yogesh Jaiswal: Yes. Okay. See um at this point I just want to mention that because we are learning we are using every feature in reality we might not use all of the features right as we discussed we will we our goal is to just use clay to make our strategy successful. Okay. Yes.

sampath vemulapati: Also I mean we can also connect claude with uh clay right I mean if for example if we have to extract some list so with few commands we can

Yogesh Jaiswal: H see uh

sampath vemulapati: also do

Yogesh Jaiswal: there is a claude clay MCP to claude but generally it's not advisable because clay is super expensive. uh clay gives you 2,000 credits for $190, right?

sampath vemulapati: Got it. Yeah.

Yogesh Jaiswal: So that's not a good way of using uh clay and generally people don't connect to

Medha Das: Okay.

Yogesh Jaiswal: cloud. Okay? So because if you want to connect to claude, you can get APIs, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: You can get APIs for verifying email in richly you can get an API, right?

#### 00:56:29

sampath vemulapati: Yeah.

Yogesh Jaiswal: So you can literally get everything that's not advisable. I mean until you have a good clay plan and you work with a good company which have like lot of clay credits

Medha Das: Okay. Awesome.

Yogesh Jaiswal: then it's a separate thing but it's always too good to be conservative in clay.

sampath vemulapati: Maybe.

Yogesh Jaiswal: Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. Yeah. A go to add go to a fresh column. No, no. Fresh uh sorry, fresh sheet. Add here. Okay. Blank table. Yes. Uh now I'm giving you a company name. Uh uh let's say Razer Pay, right? So in the new column, name the company name as Razer Pay. Rename it. Company name. No, no, make it company name.

Medha Das: Oh, okay.

Yogesh Jaiswal: Yeah.

Medha Das: Sorry.

Yogesh Jaiswal: No, no, that's fine. Okay. Yeah. Now yes now in one write razor be okay now you need to find the company domain enrich company enrich your ICP enrich the email and validate the email can you Right.

#### 00:57:56

Medha Das: Yeah. uh Yogeshuh I mean uh one quick question so when I

Yogesh Jaiswal: It's correct. It's correct.

Medha Das: uh run this one uh will it I'm assuming uh if uh Google is able to provide the data it won't

Yogesh Jaiswal: Yeah, either one will not run. Other one will not.

Medha Das: right Yeah.

Yogesh Jaiswal: Yeah, it will show you the entire credits but other one will not run the other provider.

Medha Das: Oh,

Yogesh Jaiswal: Yeah, that's what a waterfall is. Okay. Now, enrich company Yes. Continue to add fields. This is correct.

Medha Das: Oh yeah.

Yogesh Jaiswal: Okay. Now find your ICP.

Medha Das: Okay. Uh sorry from where

Yogesh Jaiswal: Five contacts at the company. in this table. Yes. So also there is one more enrichment called find people at a company. Don't get confused in that. Okay. It's always find contacts. H

Rithika Murthy: Is there any difference between the two?

Yogesh Jaiswal: Yeah, find people is a broader way of searching it.

#### 01:01:07

Yogesh Jaiswal: It directly moves to a new table. Uh, find contact is just to keep everything in one sheet.

Rithika Murthy: Oh, okay.

Yogesh Jaiswal: Yeah, we would we would practice that as well. Retika, we would check that as well.

Medha Das: uh you wish for a reason like uh who would be like the ideal profile I mean do we

Yogesh Jaiswal: That's you selected the right ones. Sees BP director is good. Yeah. And just add finance. Yeah, even you can select finance and no need to add finance and job title keywords. That's also fine.

Medha Das: I mean this is fine right like we are select function Okay.

Yogesh Jaiswal: Yeah, that's fine. That's fine. Now click on run. Let's see what we get. Yeah, save and run. Okay, we got we have seven people. So, no, click on the seven. Return seven people. Yes.

Medha Das: What?

Yogesh Jaiswal: So, see what you got from zero. Okay. You have business finance.

#### 01:02:44

Yogesh Jaiswal: Okay. Check the other ones. Senior director of finance. Okay, let's reach out to the senior director of finance. Yeah. So output name, title Full always full name in clay always full name. Okay. Yeah. Name LinkedIn URL and job title. Yes. LinkedIn URL is must for person enrichment. Okay. And job title. Yes. Now you can close this. Yeah. Now find email for this work email. No, no, no, no. Work email. It's always there down. Yes. Yeah. Set it up. Uh yes.

sampath vemulapati: So you can also add email by

Yogesh Jaiswal: Uh sorry uh just a second. Sampathuh uh Medhago down and remove the validation provider. Go down. Yeah. Delete the validation provider. Yes.

Medha Das: Oh yeah.

Yogesh Jaiswal: Yes. Yes. Yes. Yeah. Settings. Delete it.

#### 01:04:26

Yogesh Jaiswal: See, you need to always do it. So, please make it have it. Yes. Okay. Uh, you can run this. Yeah. Sampathwhat you said?

sampath vemulapati: Yeah. Can we also add email bison here uh for

Yogesh Jaiswal: Yes, we have all the integrations.

sampath vemulapati: Okay.

Yogesh Jaiswal: Yeah. Okay. Now validate the email. Yes. No need to add condition.

Medha Das: Oh, it's simply this.

Yogesh Jaiswal: Yeah. Direct. Direct. Yes. Yes. Yeah. Output the MX domain and result. No, no, don't click on this.

Medha Das: Okay, fine.

Yogesh Jaiswal: Yeah. Now wait. It will run again. Yeah. Click on captual valid. Yes. Now output the MX domain and result and result. Okay. Yes. Got it. You can close this. Now did go to the starting again. Yeah. Now can you see from one company name you got every detail right?

#### 01:06:49

Medha Das: Yeah.

Yogesh Jaiswal: So you can also build an automation here like you can build a okay I'll tell you show you how it works. Go to the starting. Okay. Now add move this 10 to two. Change the 10 to two. Yeah. Yeah.

Medha Das: Heat.

Yogesh Jaiswal: Make it two. Two. Yes. Now click on add. Yeah. Now write phone play. Enter. Now see everything will work automatically.

Rithika Murthy: Uh is this because auto run is on on this table?

Yogesh Jaiswal: Yes. Yes. Yes. Yes.

Rithika Murthy: Okay.

Yogesh Jaiswal: Yes. Yeah.

Rithika Murthy: Is this how uh like you do this when like a client gives you a number of these companies?

Yogesh Jaiswal: Yes. Yes.

Rithika Murthy: Okay.

Yogesh Jaiswal: Yes. Yes. Yes. Now go to the uh drag the uh Yeah. Medhago to the next rows, next columns. Yeah. Go to the right.

#### 01:07:57

Yogesh Jaiswal: Yes, see everything will work automatically. Okay. Now write uh after phone pay write PTM and it it will work.

Medha Das: Yogish one quick question. So you remember we selected like from the seven people we selected

Yogesh Jaiswal: Yes.

Medha Das: which person we need right?

Yogesh Jaiswal: Yes. Yes.

Medha Das: So how does it work for the other companies?

Yogesh Jaiswal: Yeah. Okay. There is one more way out that after find contacts at a company you need to add one more enrichment that amongst all of these people select the top ones. Okay, we have skipped that part because we are just learning right now. It's it's a very like early days of clay. In future we would like go more uh perfe like build more perfection in a clay table. Right now we are just learning.

Medha Das: Okay.

Yogesh Jaiswal: Okay. Yeah.

Medha Das: All right.

Yogesh Jaiswal: But that's right. I mean we need to be very clear with the filters. Okay. Uh yeah.

#### 01:08:57

Yogesh Jaiswal: Now write PTM and see it will work.

Rithika Murthy: But isn't it better if we reach out to like multiple stakeholders in the company like

Yogesh Jaiswal: Yes.

Rithika Murthy: volumewise because email a lot of people does don't respond and like reply rates This is like 2%

Yogesh Jaiswal: So yeah.

Rithika Murthy: rate.

Yogesh Jaiswal: Yes. Yes. Yes. So uh yeah this domain is wrong. Okay. We need to use the in uh AI use AI enrichment domain column. Okay. We can do that later. No problem. Uh okay. So yes, we are just doing it a sample test run on one company and one person. Uh as you know you have 50 companies right now, correct?

Rithika Murthy: Yeah.

Yogesh Jaiswal: So we are going to go extensive on the 50 companies and you are going to correctly filter in people into a new table and get all of the information.

Rithika Murthy: Okay.

Yogesh Jaiswal: This is just the test run we did right now. Yeah.

Rithika Murthy: Okay.

#### 01:09:59

Yogesh Jaiswal: So for PTM uh yeah can you change the domain Medhajust

Medha Das: Yeah.

Yogesh Jaiswal: yes so let's not use the company domain waterfall I don't know it's not working good nowadays

Medha Das: Okay.

Yogesh Jaiswal: yeah you Use this. Find the company domain.

Rithika Murthy: Okay.

Yogesh Jaiswal: H save. Generate. Generate. Click on generate.

Medha Das: Oh,

Yogesh Jaiswal: Yes.

Medha Das: thanks.

Yogesh Jaiswal: Yes. This is a prompter.

Medha Das: Thank you.

Yogesh Jaiswal: So we we will reach a point well where we will not use so many credits and we will get the same output. Okay. After a few days. No no no no. Select helium. Yeah. Always select helium. Yes. Just like you select helium. If it doesn't work, then you move to a new model. Save and run. I think this is how you'll get the correct ones. Okay, PTM is taking time. I don't know why, but uh yeah, we'll sort it out.

#### 01:13:15

Yogesh Jaiswal: Okay. Uh yeah, we can sort it out. Medhanot a problem. I think it's just there might be other companies with the name and uh that's why it's getting confusing. Okay. So, just want to mention here that you can you Yeah, you've got it right.

Medha Das: here.

Yogesh Jaiswal: So you can stop sharing. Uh no problem. And turn turn off auto run.

Medha Das: Yeah.

Yogesh Jaiswal: You can stop sharing but turn off auto run. Okay. Uh yes. So right now the whole purpose was to understand that when we have a set of companies we can find a set of people and we can get those emails and we can also get the uh we can also validate the emails. Right? This was just the test run. Right now we would go more extensive. I would give you a task that you can do over the weekend. Right? And uh I'll just give you a company name. Okay?

#### 01:14:11

Yogesh Jaiswal: Maybe 10 company names. And uh you need to first find domains in which company and also check if this company are your right ICPS or not. Okay? And then find the right people, validate it and just move it. Okay. Uh but yeah, I mean at later point we would build more good tables, right? Right now we're just practicing. So our goal is to learn the features. Okay, any questions? Anyone?

Rithika Murthy: Is this like particular to the portfolio build we are doing or this

Yogesh Jaiswal: Mhm.

Rithika Murthy: different?

Yogesh Jaiswal: No, no, this is this is just at I mean at the point of learning clay. Okay. Uh it becomes very easy when you know every feature, right?

Rithika Murthy: Yeah.

Yogesh Jaiswal: So the method is learn every feature and then build a build something out of it, right?

Rithika Murthy: No, no.

Yogesh Jaiswal: That's why Yeah.

Rithika Murthy: I'm asking regarding like you mentioned over the weekend you'll give a task, right?

Yogesh Jaiswal: Yeah.

Rithika Murthy: Uh I'm asking about that task.

#### 01:15:21

Yogesh Jaiswal: This is for the portfolio. Yes. Yes. Yes. Yes. This is for the portfolio. Uh yes,

Rithika Murthy: Okay.

Yogesh Jaiswal: that's right. Yeah.

Rithika Murthy: Okay. Okay.

Yogesh Jaiswal: Yeah. I'll I'll just select your companies and go to claude and give you 10 10 companies and then you need to build something.

Rithika Murthy: Okay.

Yogesh Jaiswal: Are you you can do it right over the weekend.

Rithika Murthy: Yeah.

Yogesh Jaiswal: Okay. Okay. Yes. Yes.

sampath vemulapati: So what about the 50 companies that we have extracted from crosspio? So we should also go for that or like we should just leave it that now.

Yogesh Jaiswal: I mean I would check those 50 companies that you have selected because I don't want you to be wrong. So if you have those 50 companies ready I mean you can even do with that that sort of problem but only 10 from those ones because we are going to do so things in clay and we don't want to ruin yeah sorry I missed this part

#### 01:16:11

sampath vemulapati: Got it. Got it. Yeah.

Yogesh Jaiswal: that we already have 50 companies uh I missed okay

sampath vemulapati: No, I was just a little confused.

Yogesh Jaiswal: okay yeah no that's fine that's fine we already have the 50 companies okay so can you do this can you select those 50 companies is uh enrich the domains. I you already have the domain, right? So, enrich find the people, enrich the email ids and everything. Can you do it?

sampath vemulapati: Yeah, I can do for my selected companies. Yeah. And yeah, it my claud sorry uh my clay has also started.

Rithika Murthy: It's hard enough.

sampath vemulapati: Okay. Yeah.

Yogesh Jaiswal: Perfect. Okay. So give me some time like let me think about it because I want to make it difficult for you.

sampath vemulapati: Sure.

Yogesh Jaiswal: That's why I've said like uh uh like let let me give give me some time I'll give you the task properly. I mean just to make sure that you follow all the guidelines because in the 15 set of companies you already have those domains and LinkedIn URLs.

#### 01:17:13

Yogesh Jaiswal: So that's why.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. Okay. Cool.

sampath vemulapati: Sure.

Yogesh Jaiswal: Cool. Apart from that any questions?

sampath vemulapati: No, that's it.

Yogesh Jaiswal: Okay. Okay. Good. Any any uh like are you able to understand how clay works now? Like you you're getting rough idea about it.

sampath vemulapati: Yeah, I mean so far being able to

Medha Das: It's

Yogesh Jaiswal: Yeah. So it's very easy. We understand the features and we just we just make the work easy in clay, right? Because before clay it was very difficult. That's why uh clay is going to be a huge focus in this program. Okay. Cool. Uh yeah, I think this is it. Uh let's connect on Monday, but I'll give you a task that you can do over the weekend. uh and uh we can go ahead from there. Okay, cool. Cool. Guys, have a nice weekend. Let's connect.

sampath vemulapati: Thank you.

Medha Das: Thank you.

Yogesh Jaiswal: Yeah.

Medha Das: Thank you. Thank you.

sampath vemulapati: Thank you.

#### Transcription ended after 01:18:21

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.