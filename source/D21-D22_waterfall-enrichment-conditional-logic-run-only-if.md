# D21+D22_ Waterfall enrichment + Conditional logic & _run only if_ - 2026_09_22 08_56 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D21+D22: Waterfall enrichment + Conditional logic & 'run only if'

Sep 22, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Data enrichment strategies and Clay workflows with pipeline building insights.

Clay platform setup and enrichment workflows

Yogesh demonstrated extracting company lists from Prosperia and enriching data within Clay.

Filtered companies by SDR and BDR headcounts using entry and mid-level job criteria.

Checked technographics using HG Insights to identify outbound tools like Apollo and Lemlist.

Targeted ICP personas including founders, CEOs, and VPs of sales using specific search filters.

Validated emails through waterfall enrichment and differentiated between valid, invalid, and catch-all statuses.

Explored AI model selection, using Helium for single-page lookups and Neon for complex multi-page tasks.

Clay run conditions and operational troubleshooting

Yogesh explained that run conditions save credits by executing enrichments only when criteria are met.

Implemented basic run conditions ensuring enrichments run exclusively when work email fields remain populated.

Warned against modifying column names after establishing run conditions to prevent breaking table configurations.

Proposed using multiple workflows for judgment calls when targeting small and highly specific markets.

GTM engineering portfolio and industry benchmarks

Yogesh advised building a portfolio featuring strategy documents, Clay tables, and 5 Loom videos.

Outlined benchmarks including a 70% LinkedIn acceptance rate and a 3% to 5% reply rate.

GTM engineering costs and market entry strategy

Yogesh Jaiswal stated that the complete GTM engineering stack costs up to 1,000,000 rupees monthly.

Yogesh Jaiswal advised starting slowly as a lead list builder before managing full campaigns.

Yogesh Jaiswal highlighted that a fresher secured a role at $45,000 monthly after portfolio preparation.

AI agent adoption and market limitations

Yogesh Jaiswal noted that data compliance restricts European and US companies from using AI agents.

Yogesh Jaiswal cautioned that LinkedIn posts showcasing AI agents serve as promotional traction gimmicks.

Clay table evaluation and professional growth

Yogesh Jaiswal emphasized that a well-constructed Clay table directly reflects a GTM engineer's capability.

Yogesh Jaiswal noted that professional growth in GTM engineering progresses gradually over time.

Next steps

[Yogesh Jaiswal] Share Documentation: Send the documents regarding clay run conditions, waterfall logic, and email catch-all definitions to the WhatsApp group.

[The group] Build Clay Table: Construct the clay data tables by implementing the discussed qualification filters, enrichment steps, and run conditions.

[The group] Build Clay Table: Select 50 companies and define qualification parameters. Identify contact persons, source work email addresses, and validate those emails.

[The group] Expand LinkedIn Network: Add individuals from the provided contact list to LinkedIn.

[The group] Build Portfolio: Create a strategy document and supporting Clay table for a selected company. Execute a campaign and record 5 Loom videos to demonstrate the process.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 22, 2026

### D21+D22: Waterfall enrichment + Conditional logic & 'run only if'

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D21+D22: Waterfall enrichment + Conditional logic & 'run only if'

Meeting records Transcript Recording

#### Summary

Data enrichment strategies and Clay workflows with pipeline building insights.

Clay Data Enrichment Setup
Participants configured Goji Berry strategy filters and added technographics columns using HG Insights. Optimization of artificial intelligence prompts and lead generation qualification removal streamlined the pipeline.

Workflow Models and Credits
Run conditions saved workflow credits by executing enrichments conditionally. Different artificial intelligence models in Claygent were evaluated for specific multi-page and single-page lookup tasks.

Market Entry Strategy
Participants built Go-To-Market qualification pipelines and developed professional portfolios before seeking clients. Industry metrics and benchmarks established realistic campaign performance expectations.

#### Next steps

[Yogesh Jaiswal] Share Documentation: Send the documents regarding clay run conditions, waterfall logic, and email catch-all definitions to the WhatsApp group.

[The group] Build Clay Table: Construct the clay data tables by implementing the discussed qualification filters, enrichment steps, and run conditions.

[The group] Build Clay Table: Select 50 companies and define qualification parameters. Identify contact persons, source work email addresses, and validate those emails.

[The group] Expand LinkedIn Network: Add individuals from the provided contact list to LinkedIn.

[The group] Build Portfolio: Create a strategy document and supporting Clay table for a selected company. Execute a campaign and record 5 Loom videos to demonstrate the process.

#### Details

Accessing Meeting Recordings: Yogesh Jaiswal explains to sampath vemulapati that meeting recordings are stored directly in Google Workspace rather than in a separate folder, clarifying that the Google folder found in the WhatsApp description serves only as a backup (00:08:04).

Clay Data Enrichment Strategy and Mindset: sampath vemulapati shares their screen to discuss difficulties with data enrichment using company data extracted from Prosper (00:09:00). Yogesh Jaiswal advises that the proper mindset is to use Clay to support the strategy document successfully rather than attempting to use Clay for everything, emphasizing that artificial intelligence performs better with per-row searches (00:10:03).

Configuring Sales and Business Development Headcount Filters in Clay: Yogesh Jaiswal guides sampath vemulapati through adding an enrichment column in Clay for the Goji Berry strategy to find companies with sales development representative and business development representative headcounts using entry-level and mid-level seniority filters (00:13:40) (00:17:15). Yogesh notes that a skilled Go-To-Market engineer must recognize when default search settings fail and adjust parameters accordingly (00:18:38).

Checking Outbound Tech Stack Using HG Insights: Yogesh Jaiswal instructs sampath vemulapati to add a technographics column using HG Insights to verify the usage of outbound tools such as Apollo, Lemlist, Instantly, and Clay (00:19:35). Following the search execution, sampath vemulapati extracts the product installation names into a dedicated output column (00:21:26).

Testing and Removing Lead Generation Qualification: Yogesh Jaiswal has sampath vemulapati run an artificial intelligence prompt using Helium to check whether target companies provide lead generation or appointment setting services (00:24:46). After reviewing the installation counts, Yogesh discovers that none of the companies provide lead generation services and instructs sampath to delete the resulting columns (00:27:48).

Identifying Ideal Customer Profiles and Target Contacts: Yogesh Jaiswal demonstrates how to filter qualified companies and find target buyer personas—such as founders, chief executive officers, C-level executives, vice presidents, and directors within sales departments—using job title search filters and saving the results to a new table (00:30:22).

Setting Up Email Enrichment and Validation Waterfalls: sampath vemulapati and Yogesh Jaiswal add work email enrichment, configure full waterfall settings, and remove unwanted validation providers (00:35:15). Yogesh instructs sampath to add a run condition ensuring email verification only executes if the work email output is not empty (00:38:24). Yogesh explains the distinction between valid emails, invalid emails, valid catch-all emails (which can receive messages safely), and only catch-all emails (00:42:39).

Understanding Run Conditions in Clay: Yogesh Jaiswal explains the mechanics of run conditions, noting they act as reverse formulas that execute enrichments only when specific criteria are met to save credits and actions (00:45:00). Yogesh details various use cases including industry filtering, lead score validation (such as scores above 80), customer relationship management uploads, round-robin assignments, and multi-parameter operators like equals, not equals, and or conditions (00:46:04).

Comparing Artificial Intelligence Models and Selection Strategy in Claygent: Yogesh Jaiswal breaks down the specific use cases and limitations of different Claygent models: Helium is designed for single-page lookups and struggles with multi-page navigation; Neon handles semi-complex tasks across multiple pages; and Argon is suited for multiple searches and information capture but wastes credits on simple single-field lookups (00:53:30). Yogesh advises starting with Helium in a waterfall approach before moving to Neon or Argon to conserve credits (00:56:37).

Cost Control and Debugging in Claygent Workflows: Yogesh Jaiswal advises on best practices for Claygent workflows, recommending that operators test prompts on five to ten rows before running full tables, use conditional runs on qualified rows, and deploy multiple Claygent columns for judgment calls and debugging when accuracy is critical (00:56:37). Yogesh mentions that agencies typically purchase professional plans with one hundred thousand credits, eliminating the need to worry about credit consumption (00:58:59).

Assignment for Building a Go-To-Market Qualification Pipeline: Yogesh Jaiswal assigns participants the task of building out their own Clay pipeline using their selected fifty companies, covering company qualification, finding people, obtaining work emails, and validating emails (01:00:31).

Portfolio Requirements and Skill Development for Go-To-Market Engineers: Alok asks about entering the Go-To-Market engineering field without prior experience and finding clients on Upwork and LinkedIn (01:00:31). Yogesh Jaiswal advises against rushing to find clients before mastering the skill, explaining that Go-To-Market engineering is a technical skill rather than a standard department (01:01:48). Yogesh states that a credible portfolio must include a strategy document, a Clay table, automated data pushing to platforms like Heyreach or Instantly, Claude code integration, Make or n8n automations, and at least five Loom videos demonstrating the full pipeline (01:02:48).

Industry Metrics and Benchmarks for Outreach Campaigns: Neeraj Sujan asks about expected performance metrics during client interviews, prompting Yogesh Jaiswal to share standard industry benchmarks: LinkedIn connection request acceptance rates should reach seventy percent with a thirty percent reply rate, while email opening rates should exceed ninety percent with a three to five percent reply rate (01:03:49). Yogesh notes that beginners can leverage these benchmarks while building practical experience (01:05:00).

Costs and Entry Strategy for Go-To-Market Engineering: Yogesh Jaiswal explained to Alok that Go-To-Market engineering is an advanced, expensive practice where mistakes carry high financial costs. Yogesh Jaiswal detailed that a Clay plan utilized by an engineering agency costs $3,000 a month (nearly three lakh rupees), while a complete stack including Harry, Chapolo, Claude, Deepline, Instantly, and Exa costs between 5 to 10 lakh rupees a month. Yogesh Jaiswal advised Alok that building professional trust requires concrete proof and connections, recommending that they start slowly as a lead list builder before moving on to campaigns (01:06:02).

Role and Viability of AI Agents in Go-To-Market Engineering: Alok asked Yogesh Jaiswal about the use of AI agents for orchestration instead of code and whether they genuinely improve performance metrics (01:06:02). Yogesh Jaiswal responded that AI agents are rarely utilized by companies—estimating only one out of 10,000 companies prefers them due to strict data compliance regulations in Europe and restrictions in United States insurance and consumer sectors. Yogesh Jaiswal asserted that representations of AI agents on LinkedIn are merely gimmicks for traction rather than reality, noting that they still rely on tools like Clay and Claude, and advised Alok to patiently learn all aspects of the stack (01:07:15).

Portfolio Development and Compensation Expectations: Yogesh Jaiswal shared an example of a fresher from a previous batch who had no prior background, spent two months building skills, and successfully joined an agency at a compensation of $45,000 a month. Yogesh Jaiswal emphasized to Alok that dedicating time to LinkedIn, skill development, and portfolio creation makes market entry significantly easier, while noting that they had reached $3,000 in earnings. Yogesh Jaiswal advised Alok to proceed slowly to achieve long-term growth in Go-To-Market engineering (01:08:14).

Clay Table Requirements and Meeting Conclusion: Yogesh Jaiswal instructed Alok to begin preparing a high-quality Clay table, explaining that the table itself demonstrates a Go-To-Market engineer's capabilities and dictates how much a company is willing to pay. Yogesh Jaiswal offered assistance to Alok if needed during the table-building process. Concluding the session, Yogesh Jaiswal instructed participants to connect again the following day, prompting closing remarks from sampath vemulapati and Yogesh Jaiswal (01:08:14).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 22, 2026

### D21+D22: Waterfall enrichment + Conditional logic & 'run only if' - Transcript

#### 00:08:04

Yogesh Jaiswal: Hey. Hi, Sad. How are you? Good morning.

sampath vemulapati: V good morning how are you?

Yogesh Jaiswal: I'm good. I'm good.

sampath vemulapati: Yeah actually I was um I could join yesterday I was just hoping uh if you can

Yogesh Jaiswal: Yeah.

sampath vemulapati: share the recording so that I'll just uh get caught up with the rest of the weeks as well.

Yogesh Jaiswal: Yeah. Recordings are already there. I'll show you how you can see. So, if you see my screen, let's set yesterday, right? So you just need to click on this and if you go there is a recording

sampath vemulapati: Okay.

Yogesh Jaiswal: here we use yeah I use Google workspace so uh

sampath vemulapati: Oh, okay. Okay.

Yogesh Jaiswal: there is no separate recording

sampath vemulapati: Got it. So, how I did was uh I uh I went to the u WhatsApp description and then from there onwards I just uh there's a Google folder. So there I was just scrolling and then I thought like you know the recordings will be there.

#### 00:09:00

sampath vemulapati: This will be super easy then.

Yogesh Jaiswal: Yeah. No, no, no, no, no. Google holders just to uh make sure like um Yeah.

sampath vemulapati: Yeah, like a backup of

Yogesh Jaiswal: Yeah. Yes. So, uh just want to understand I mean I think rest have not joined. Um where are you right now?

sampath vemulapati: Yeah.

Yogesh Jaiswal: I mean in terms of like have you covered clay? Have you started things in clay or like

sampath vemulapati: Yeah. So, so clay I did cover uh but unfortunately I'm not getting the enrichment that I have to do because uh I missed out on few details on like you know the other day I did extract the thing from prospure that is all there and then I also tried putting the data in clay uh but you know while enriching I'm not getting the nitty-g gritties of like you know which um I'll tell you a few details actually

Yogesh Jaiswal: Mhm.

sampath vemulapati: Just opening my Yeah.

Yogesh Jaiswal: Yeah, you can share your screen and show also.

sampath vemulapati: Yeah.

#### 00:10:03

Yogesh Jaiswal: See, I mean, I just want to clear this thing out. If you can even clear this in your mind as well.

sampath vemulapati: Yeah.

Yogesh Jaiswal: We use clay to make our thing successful, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Uh that should be the only mentality you should have. I mean, we have a strategy document and we use clay to make it successful rather than we use clay for

sampath vemulapati: Makes

Yogesh Jaiswal: everything. That gets difficult.

sampath vemulapati: sense. Yeah.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Yeah. Uh this is the data I extracted from Prosperia the other day and I was actually trying

Yogesh Jaiswal: Mhm.

sampath vemulapati: to uh enrich this. Uh but you know I I was still looking at like you know which filters to choose, how to how do I enrich? But uh pretty much it it's it's usable. Um but some somewhere I I feel that like I'm missing out on few few more details like you know there are so many uh options in play and then I'm just a little um concerned that like if I'm missing out on something that that you know

#### 00:11:07

Yogesh Jaiswal: No no no that's that's not a problem. See you have a list of companies right now we need to understand one basic thing that

sampath vemulapati: Yeah. This is the

Yogesh Jaiswal: today AI works better when we do per row search. Okay that's why clay is a very good tool. Now if you put this data in claude and if you search Claude will miss few things right.

sampath vemulapati: correct. Yeah.

Yogesh Jaiswal: So what we we are going to do now is we going to understand that what do we need from this company. Okay. So go to your strategy document.

sampath vemulapati: Um, just a sec. I actually created this and then um there are so many tabs in in my device actually. So sorry. It's just I actually pasted it on the sheet. Actually, I'm trying to get that sheet where I paste it.

Yogesh Jaiswal: Uhoh. I think I have your strategy sheet. No problem.

sampath vemulapati: Uh you have it because mine is uh I've created two strategy documents.

#### 00:13:40

sampath vemulapati: One is for that goji berry and other one is for saffron. So I have it open. You want me to open still?

Yogesh Jaiswal: No, no. You need to open play.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay, let's do it for Goji Berry. You have it for Goji Berry, right? The list.

sampath vemulapati: Yeah, I have it.

Yogesh Jaiswal: Okay. Okay. So for Goji Berry, your signal is STR or BDR headcount on staff. Okay.

sampath vemulapati: Yeah,

Yogesh Jaiswal: So can you open clay?

sampath vemulapati: share my screen.

Yogesh Jaiswal: Only clay you can share. Just share clay.

sampath vemulapati: Yeah. Okay.

Yogesh Jaiswal: Okay. Add a new column.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. Now you want to check if the company have like you want to check the number of the SDR and BDR headcount. Okay. Add a new column. Add enrichment. Uh yes. Now search find contacts at a company. Yes. Yes. The first one.

#### 00:14:50

Yogesh Jaiswal: Okay. So,

sampath vemulapati: Yes.

Yogesh Jaiswal: you need to understand you just need a mathematical number, right? How the head count. Okay. So,

sampath vemulapati: Yeah.

Yogesh Jaiswal: say save results in this in this table. In this table.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. Okay. Now, uh wait, you need to uh go to job title keywords. Job title keywords. Go down. Go down. Job title keywords. Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. Mention SDR sales development representative.

sampath vemulapati: This is the one, right?

Yogesh Jaiswal: Yes. And business development representatives and also mention SDR and BDR. SDR no like SDR enter and then BDR H and BDR. Okay. Uh yeah, that's fine. Now you can click on continue and run it. Yeah. Yeah.

sampath vemulapati: Seriously 10 is

Yogesh Jaiswal: Save and run it. 10 rows.

sampath vemulapati: effective.

Yogesh Jaiswal: Yes. So this is going to give you the head count.

#### 00:16:17

Yogesh Jaiswal: Okay. See. Can you see now?

sampath vemulapati: Yeah. No profile.

Yogesh Jaiswal: Yeah. Now go to the top one.

sampath vemulapati: This one.

Yogesh Jaiswal: No. No. The top. Find contact.

sampath vemulapati: This

Yogesh Jaiswal: That arrow, the column arrow. No, go up. Go up the upper one. Yes. Yes. This one. Uh, find contacts at a company. And then the arrow, right? This one.

sampath vemulapati: I'm not being able to see this.

Yogesh Jaiswal: No. No. Can you see the find the column? Go to the column.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Can you see an arrow?

sampath vemulapati: Yeah,

Yogesh Jaiswal: Triangle. Triangle. Yeah. Click on the triangle. Yes. Click on run 40 MT out of date. Yes.

sampath vemulapati: here.

Yogesh Jaiswal: Okay. So you can easily qualify the companies who have uh salespeople, right?

sampath vemulapati: Got it. Okay.

Yogesh Jaiswal: Okay.

#### 00:17:15

Yogesh Jaiswal: Now there is a better way out. Go to the edit. Go to edit. Find contacts at a company. Edit.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. Edit. No. No. Click on the Yes. Edit column. Yes. Uh go down. Yeah. Can you click on job functions?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Job functions.

sampath vemulapati: Yeah.

Yogesh Jaiswal: No. No. Job functions.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. Click on sales. Yes. Also select business development H. Okay. Go up. Go up. Remove SDR, PDR. All of these things. Yes. Go to job title, seniority level. Go up. Yes. Select uh entry and mid level. So do you understand right? Entry and mid level are SDR and BDRs.

sampath vemulapati: correct.

Yogesh Jaiswal: Okay.

sampath vemulapati: Correct.

Yogesh Jaiswal: And you no need to select anything.

sampath vemulapati: Yes.

Yogesh Jaiswal: Uh yeah, also select floor level.

sampath vemulapati: Here

#### 00:18:38

Yogesh Jaiswal: Okay. Yes. Again.

sampath vemulapati: also entry and mid level right

Yogesh Jaiswal: Yeah. No, no. Flow level would be one. We don't want to go below uh entry, right? Yeah. Entry is fine.

sampath vemulapati: entry is fine.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Okay.

Yogesh Jaiswal: Okay. Uh now go to max mode. Job title match mode the Yes. Exactly. Exactly. Yes.

sampath vemulapati: Yeah,

Yogesh Jaiswal: Now save and run for 30 for 50 whatever it is. Yeah. 50. This is a better way of searching because the other one didn't worked right.

sampath vemulapati: other one can.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Oh,

Yogesh Jaiswal: Now can you see?

sampath vemulapati: this showed a different result then.

Yogesh Jaiswal: Yes.

sampath vemulapati: Oh.

Yogesh Jaiswal: So you always have to understand that a good GTM engineer is not the one who is using things right. who is able to understand if things are not working perfectly or not. Okay.

sampath vemulapati: Next.

Yogesh Jaiswal: Now your your qualification worked.

#### 00:19:35

Yogesh Jaiswal: They have HDR and uh hi. Hi Nage.

Gagan Bhaisa: Hey, you wish.

Yogesh Jaiswal: Hi. Hi. So your qualification worked. Uh Sat right? You have checked that these guys are having SDR and BDR right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Now we need to check one more thing if they have outbound tools in the stack.

sampath vemulapati: Right.

Yogesh Jaiswal: Okay. Now go to a new column. Add a new column. Yes. Okay. Click on technographics. Search technics.

sampath vemulapati: Motion

Yogesh Jaiswal: Yes. Okay. Wait, wait, wait.

sampath vemulapati: Oh, sorry.

Yogesh Jaiswal: No, that's fine. You can close this. Mhm. Yeah. Just search HG Insights. HG HG HG Space Insights. Yes. Just a second. Huh. Okay. Uh verify technology usage. Yes. This one. H. Okay. Go down.

sampath vemulapati: products. We should

Yogesh Jaiswal: Yeah. Now select uh wait let me show you Apollo limb list yeah apollo.io IO lem list.

#### 00:21:26

Yogesh Jaiswal: L E L L E L list. Lamb list. Yeah, it's at the top. Instantly clay. Yes. Clay. Yes. Expand. expi. Yes, the top one. Okay.

sampath vemulapati: Yep.

Yogesh Jaiswal: Yeah. Now go down. Yes. Wait. Uh, make the limit four. Yeah.

sampath vemulapati: Oh.

Yogesh Jaiswal: The limit limit limit up up. Yeah. The limit four. Yeah. Now continue to add fields. Yes. Now save and run the first 10.

sampath vemulapati: No, they don't have anything.

Yogesh Jaiswal: Can you run for all? Yeah. Run for all. Yeah, run. Go down. Okay. Okay. H. Yeah.

sampath vemulapati: Yeah,

Yogesh Jaiswal: Now click on this one. Install fonts.

sampath vemulapati: this one.

Yogesh Jaiswal: No, go to the right. Right. Go to the right. Yes, we have more columns. No, no.

#### 00:23:16

sampath vemulapati: Um, no.

Yogesh Jaiswal: Click on the one install found. Yes. Click on the one install. One install found. Yes.

sampath vemulapati: Yeah,

Yogesh Jaiswal: Now installs. Okay. All output the all product names. Output the first column. Yes. First column.

sampath vemulapati: this one.

Yogesh Jaiswal: First first T. Yes. Add to column. Yes. Create column. Yes. Now close this. Yeah. You you have to remove this Apollo sign that's why it's not closing. Yeah, it's behind this. Okay. Okay. Yeah, just press this button. Okay. Now, the third qualification is agency selling outbound. Okay. Okay. Now run a qualification. Run an AI prompt. Add enrichment. Yes. Check if the uh Yeah. Use AI. Use AI. Yes. Yeah. Right. Check if the company is providing lead generation services or not.

#### 00:24:46

Yogesh Jaiswal: Lead generation or appointment setting services. Huh?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Wait. or not. New line. New line. Company details. Company details. Map the company name and domain. No, no, no, no. Just map it. Just insert the slash and you will map it. Remove. Remove map. Yeah.

sampath vemulapati: Oh yeah.

Yogesh Jaiswal: Remove. Yeah. Yeah. Do it here. Company name and website. Yeah. Click on the company name and the website again. No slash website. Okay. Generate. Yes. So we have done three qualifications and this is the last

sampath vemulapati: Yeah.

Yogesh Jaiswal: one. Okay. Change neon to helium. Go up. Go up. Neon to clay. Neon. Yeah. Change it to helium. Go up. Up. Up. Up. Yes. Helium.

#### 00:26:17

Yogesh Jaiswal: Yeah. Yeah. Click on save and run. 50 rows. Yes.

sampath vemulapati: But uh also we had the company website uh here like in the list itself I I created the company website and uh LinkedIn URL as well.

Yogesh Jaiswal: Mhm. Yeah, that's fine. Not a problem. Uh, go to the left. Yes. Now I'll filter the companies here. Left. Go from where we started. Yes. Okay. Wait, wait, wait. No, no, no. Find contacts at a company. Yes. Now, click on that and filter. I'm going to show you an easy way to qualify it, right? Filter the column. Filter down. Filter. Yes. Filter has. Yeah. Click on this. Has. Yes. as result. Okay, fine. Leave it. Yeah. Yeah. Go to install counts. Install counts.

sampath vemulapati: What the?

#### 00:27:48

Yogesh Jaiswal: The third the next column. Install counts.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. Filter is not empty. changed equal to. No, no, no, no, no, no. Don't click here. Yeah, yeah, it's not empty.

sampath vemulapati: Oops.

Yogesh Jaiswal: H. Yes. Now go to the right h go right. Okay. So, we cannot use the third qualification parameter because none of the companies providing lead generation services. So you can delete this. Yeah, you can remove this lead and appointment setting. Go to the lead and appointment setting.

sampath vemulapati: this one.

Yogesh Jaiswal: No, no, no, no. Where you started? Lead an appointment setting. The enrichment. Yes, this one. Yes. Delete this.

sampath vemulapati: Uh, delete this entire column.

Yogesh Jaiswal: Yeah, you need to control and select the others also. Yes. Now delete the other also which are which are in red control. You can control and select all.

sampath vemulapati: Um, this one.

#### 00:29:20

Yogesh Jaiswal: Yeah.

sampath vemulapati: This

Yogesh Jaiswal: Click on this. Yes. And controlclick on others also. Don't delete one. Oh yeah.

sampath vemulapati: actually not working for some reason.

Yogesh Jaiswal: Okay. Fine. I think it's it's okay. No problem. Leave it. Leave it. Leave it. Yeah. Go to add. So now your companies are qualified, right? You can you need to just delete this. Okay.

sampath vemulapati: Yeah, this one I'm just defeating.

Yogesh Jaiswal: Go to the left. Yeah. Leave this part. Go to the left. left. Yes, stick here. Yeah. So, you have the first qualification parameter if they're using if they're having a entry- level sales team and if they're using tools. So, you have both the details, right?

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: You have people who are there and they are companies were using tools. Now, go to add. Now, I'll show you.

#### 00:30:22

Yogesh Jaiswal: So, the companies are qualified, right? No, no,

sampath vemulapati: Yeah.

Yogesh Jaiswal: add down ad down. No, no, no, no, no, no. Not this ad. the down.

sampath vemulapati: Okay. Okay.

Yogesh Jaiswal: Yes.

sampath vemulapati: Okay.

Yogesh Jaiswal: Yes. Don't click on clay because it's one mistake can literally ruin everything.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So be very careful on what to click.

sampath vemulapati: Yeah.

Yogesh Jaiswal: And that ad was add rows. We don't need to add rows.

sampath vemulapati: Right. Right.

Yogesh Jaiswal: Yeah, no problem.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Click on find people. Okay. So this is a fast way when you work in an agency uh you don't have time to qualify and disqualify. So you qualify and just filter it. Okay. Yeah.

sampath vemulapati: You got it.

Yogesh Jaiswal: Now left. Go to the left. Go down.

sampath vemulapati: Oh,

Yogesh Jaiswal: Yeah. Left. Go down. Left. Left. Left part.

#### 00:31:16

Yogesh Jaiswal: Yes. Yeah. Click on company identifier. The left side. Yeah.

sampath vemulapati: this one.

Yogesh Jaiswal: So let's click on this company domain. No, no, no. Don't type it. It's down there. Company domain. Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Uh text inputs also cannot work because you need to map it.

sampath vemulapati: Right.

Yogesh Jaiswal: Uh now go up up up.

sampath vemulapati: Right.

Yogesh Jaiswal: Yeah. Now click on the job title. Yes. Okay. Now, whom are you going to sell? Goji Berry. What are the personas?

sampath vemulapati: to the head leads uh to the head sales people or VP salespeople.

Yogesh Jaiswal: Okay. Now, click on the search filter. No, no, no. Go. Can you see the top below criteria? Search filters. No, no. Left top. Go to Yeah. Click on the search filters. Search filters.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes.

sampath vemulapati: Yeah.

#### 00:32:32

Yogesh Jaiswal: Click. Yeah. Go to people. Yeah. Go down. Down. Can you see a department search? Can you search department? Yeah. Can you search department up? Yeah, search department. Oh, I think I don't have Okay,

sampath vemulapati: Oh no.

Yogesh Jaiswal: leave it. Yeah, just go to job title. Yeah. Job title. Yes. Select sales, right? Sales. S A L E S. Yes. Yes. Enter. And select. Okay. No, no, no, no. Don't click. Go to similar to and select contains. Yes. And go to seniority left. Left. Seniority down. Yes. And select found. Yeah. Uh yeah.

sampath vemulapati: Oh no.

Yogesh Jaiswal: Click on this. Click on this. No. No. Ah. Okay. Okay. Fine. Fine. Yeah. Founder, CEO, Cale, Cuit, VP.

#### 00:33:54

Yogesh Jaiswal: Yes. Also director. Uh yeah. Now confirm filter. Continue.

sampath vemulapati: Yep.

Yogesh Jaiswal: Yeah. Save to a new table. Yeah. Save and run nine rows. Left, left, left, left. Yes. H. Now close this. Right tab. Okay. So now you qualified the companies and you got called the people. Okay.

sampath vemulapati: people as well.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: These are your ICPS. Okay.

sampath vemulapati: Right.

Yogesh Jaiswal: Go to the right because we are going to learn waterfall today. So I'll teach you waterfall as well for others as well. Yeah. Add column.

sampath vemulapati: And you can also get the email here.

Yogesh Jaiswal: Yeah. Yeah. We'll get we'll find the email. Add enrichment. Yeah, work email. Down, down, down. Okay, some enrichments will always be suggested. No need to type it because these are the popular ones. Okay, go down.

#### 00:35:15

Yogesh Jaiswal: Yeah, see if everything is mapped. You can just see easily. Go to company name and don't click anything. Go to company name. Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. If you go there, don't click anything. You will see that it's going to pop up.

sampath vemulapati: RG. Yes. Yes.

Yogesh Jaiswal: No, no. Go to RG. Yeah. Now go to org. Okay. Fine. Fine. Leave it. I think it's already mapped. Leave it. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Now go up. Go up. Yeah. Click on save. Yeah. Go to full sorry full configuration. Sorry. Full configuration.

sampath vemulapati: Yeah. pure.

Yogesh Jaiswal: Yes.

sampath vemulapati: can use the findings.

Yogesh Jaiswal: Now you know how to set this up.

sampath vemulapati: Yeah, I have to get the lowest one on top or

Yogesh Jaiswal: Yes. Yes. Yes.

sampath vemulapati: maybe So, I should delete this.

#### 00:36:15

Yogesh Jaiswal: Yeah. Yeah. You can delete this. No, no, no, no, no. Don't delete others.

sampath vemulapati: Yeah. Yeah, I'm not deleting. Um

Yogesh Jaiswal: Move in row to top in row ICPS. Just drag them. Yes. H no no just

sampath vemulapati: Prosperity also took down.

Yogesh Jaiswal: understand 0.2 0.3 like that H yes

sampath vemulapati: Yeah.

Yogesh Jaiswal: H. Good. Go down. Go down. Yes. Down. Down. Yeah. Go down. Go to validation provider. You see a setting option. Setting. Setting button. No, no, no, no. Go.

sampath vemulapati: him.

Yogesh Jaiswal: Yeah. Click on this. remove provider. Yes. Save and run nine rows. Okay, go to the right add column

sampath vemulapati: Yeah.

Yogesh Jaiswal: add enrichment. Now we need to validate this email, right? So search enrichly enrich. Yes. Verify email. Yes.

#### 00:38:24

sampath vemulapati: Yeah.

Yogesh Jaiswal: Go down. Continue to add fields. Okay. Wait. Go back. Up. Up. Up. Yeah. Go back. Okay. Go down. Okay. Click on run condition. So run condition means that it will only run when the condition is met. Okay. Now write run condition.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Only run. only run if if slash select what uh select the email. Go down. No, no, no, no. Go down. Scroll. Yeah. Go down. Completely down. Yeah. Down. Go completely down.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. Wait. Wait.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Wait. Wait. Go up.

sampath vemulapati: Yeah. I just Yeah.

Yogesh Jaiswal: No, no. Go down. Sorry, not this one. Go down. No, no. Down, down. You're going up.

#### 00:39:43

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes. Go down. Yeah. Keep going down.

sampath vemulapati: Morning.

Yogesh Jaiswal: Yeah. You want to when you work on the latest columns, it's always going to be down.

sampath vemulapati: Got it.

Yogesh Jaiswal: Go down.

sampath vemulapati: I think this is the last. It's not getting scrolled.

Yogesh Jaiswal: Go to email. Don't click on it. Okay. Go to email.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Go up. Okay. Just type work email. work email. I think your clay is very Yeah. Go up.

sampath vemulapati: I found work even somewhere.

Yogesh Jaiswal: Yeah. Yeah. Even I have go up. I think it's up now.

sampath vemulapati: Yeah.

Yogesh Jaiswal: 3 2 Yeah. Go up. I think it's Yeah. Yeah. Click on output column. Output.

sampath vemulapati: This one right

Yogesh Jaiswal: No. No. No. No. Output. Yes. Click on this. Yes. It's not.

#### 00:41:10

Yogesh Jaiswal: No. No. Don't click anything. Write. Complete the prompt. Only run if work email output is not empty.

sampath vemulapati: garbage. Thank you.

Yogesh Jaiswal: Empty. PT. Yeah. Yes. Now generate. It's very easy. Just keep if you keep on using clay,

sampath vemulapati: Yeah.

Yogesh Jaiswal: it becomes very easy, right? Uh click on continue to add fields. Save and run. Yes. So you just added a run condition that if work email is not available then it will not run. Okay.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: Okay. Now click on validate or catch all anything. Yeah. Click on this. Yes. Click and output the MX domain. Yes. Output means add to the column. Yes. Create column. and also output uh result.

sampath vemulapati: resulted.

Yogesh Jaiswal: Yes, because result will give you information. Uh the valid output column is a tick mark.

#### 00:42:39

Yogesh Jaiswal: You don't need the tick, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. Okay. You can close this.

sampath vemulapati: So what do you mean the catch all invalid? What is the difference actually?

Yogesh Jaiswal: Yeah. So catch all means Okay. There are three things. Valid. Okay, there are four things actually. Valid email, invalid email, you know that valid is a valid email.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Invalid is an invalid email. Then now there are two catch alls. Valid catch all and only catch all, right? Valid catch all means you can send email to that person. Okay, that person is receiving emails but not replying. Right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: He's receiving emails. Catch all means the email is just delivered. he's not even receiving it. Okay.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: So basically if you want to generate a list of people to reach out you cannot reach out to only catch all people.

sampath vemulapati: Understood.

#### 00:43:34

Yogesh Jaiswal: You should reach out to valid and valid catch all.

sampath vemulapati: You got it. Yeah.

Yogesh Jaiswal: In catch all there are two things you can easily I'll send you one document you can easily understand what it is. Uh okay. So yes. So what we just did right now we qualified the companies and we found people we also added

sampath vemulapati: Yeah.

Yogesh Jaiswal: a run condition that only run for the um only run for the emails which are available right cool I think this is

sampath vemulapati: Yeah.

Yogesh Jaiswal: it yeah others um did you got what we are doing nj alok okay

Neeraj Sujan: Yes.

Yogesh Jaiswal: Um cool I think. Yes. So we are going to learn more about the run condition today. Okay. Let me share you my screen. Let me share my screen. I think I have a run condition document. Okay. Right. So, so you you all understand where you need to use run condition. Okay. It's it's in every enrichment column.

#### 00:45:00

Yogesh Jaiswal: If you go down, there is a run condition. Okay. Now. I'll show you what is a uh how do you efficiently use run condition right run conditions are um if a condition is met then run okay it's easy you can check it here if the condition is met you run the enrichment else you skip it okay so this is used to save credits and actions okay so clay builds you on two parameters on credits and on actions Right? If run condition doesn't met, you save the credits and actions. Right? Uh you know where to find in the UI any column when you run agent go down run conditions and you can see the only run if field. Okay. You have two ways to put a run condition. You have a manual method and you have a use AI method. Right? No one is perfect to use the manual method. Honestly like it's very difficult unless like you put in at least 6 7 months to learning play.

#### 00:46:04

Yogesh Jaiswal: So it's better that you always use AI. So you type the prompt of what the run condition should be and it will run it. Okay. Now there are more use case to run condition right referencing data like we just did sat right email is not empty this is what we did okay we just did a very basic run condition but we have more set of run conditions equals so now if you're running a enrichment and uh you only need need to reach out to SAS companies then You add a run condition that the industry should be SAS. Okay. Equals to then you have not equal to. Okay. If you have a list of column where status is open and closed and you need to remove the closed ones. So not equal to. Okay. These are the signs. In clay we call this as operator value. Okay. Then you have greater than less than. Okay. So just understand run condition also acts like a formula.

#### 00:47:16

Yogesh Jaiswal: Okay, you can consider it as a reverse formula where um where if the parameter is met the enrichment will happen. If the parameter is not met enrichment will not happen. Okay. Now this is an important thing lead score. Okay. Now what we are doing right now in terms of clay we can make it much better right. We can completely make one table where if the lead or account score is less than 80 is more than 80 then it will run. Okay. And if it's less than 80 it will not run. Okay. Now check for the blank output. So can you see if work email is empty it will not run or if it's not empty it will not run. Okay. Now we have operators. You can add multiple run conditions also, right? You can add company size is 500 and industry size. Okay? And trust me, uh this looks easy, but it's a very difficult thing to learn because you need perfection here, right?

#### 00:48:23

Yogesh Jaiswal: Anyone can use clay and run things but you need to understand that if you are a perfectionist then it becomes very easy for you to use it. Okay. So you can add more run conditions in one condition. You can also add or if the title is founder or title is CEO. Okay. You can also add if the status is not closed. Okay. So this is for two parameters. If the status is closed then you don't run it. But if it's not closed then we can also add a reverse condition. You can do more things with one information. Okay. Again a real example work email is not empty. Right? But now I'm give showing you the important use cases. Okay. Upload to CRM. Um people who are going to go advanced in GTM engineering you you will also use CRM connectors like add lead to HubSpot add lead to Zoho add lead to Salesforce. So you need to understand when a company gets you as a GTM engineer they don't want false information.

#### 00:49:34

Yogesh Jaiswal: So you can add an condition that if the email is not empty only push the lead if the email is not empty right then you have a lead score. So when you want to upload the leads to hair reach or instantly the lead score is 80 and industry says okay good GTM engineers are just creating one good table with good formulas and run conditions and it's running on autopilot. Okay. Again, region, North America, right to table. Okay. Round robin. Uh, Gagan, you might know what is round robin, right? Uh, or others. Do you know?

Gagan Bhaisa: I I know about that.

Yogesh Jaiswal: Okay. So, you won't believe, but there are so many tools to roundroin. But today, you can even do roundroin in clay itself. Can you see this? Assignment rep is curry. So that's why I mean today the GTM engineering thing is very narrow but if you see in future one clay operator will replace all the marketing and sales people. They would have very few people who are doing the job.

#### 00:50:45

Yogesh Jaiswal: Okay. So even round robin assignment can be perfectly done in uh clay. That means round dropping will happen enrichment will also happen. So now the SDR or BDR will not just get the lead information but will also get the complete details of the lead right now you have waterfall email is not empty try the other provider you know what is a waterfall right the waterfall automatically runs on a run condition now you have web search uh again it's a very easy thing you need to only run a cleent web search when certain conditions are met okay now you have intermediate conditional run these are like the mid difficult ones so it's easy I mean if you see the clay waterfall It's also a run condition and a formula mixture. Okay. Okay. Then you have advanced run conditions. Okay. Um yes. So it's see it's it's basically where you have multiple set of informations and then you okay then you combine other set of information. If you see that they are hiring engineer and a text stack is AWS.

#### 00:52:06

Yogesh Jaiswal: So this is actually two separate information. Definitely there would be two separate columns for this and we are combining these two uh two information. Okay. Now the title is founder or title is CEO and not industry is nonprofit. Right. By the way we use this a lot. This one if you fetch data from Apollo or Prosper you will always get an information of industry uh of the company type if it's a private or a nonprofit we always have an uncondition that we because we don't sell to a nonprofit company right they will not buy okay now troubleshooting is also important in run condition um you cannot just run something and expect it to run perfectly because you need to also understand one I mean I'll give you a cheat code only use run conditions when the play table is properly built okay that means you are not going to change the names of the columns because the moment you have a run condition the run condition depends on a column right and you cannot change the column name so if you have a run condition on the column which is industry you cannot not make it industry with I capital now or I small it's going to impact your whole clay table.

#### 00:53:30

Yogesh Jaiswal: Okay. Now these are some conditions that you can I'll also send this uh document file in the WhatsApp group for everyone so that you can take a look. Um any questions in run condition? Okay. Uh I will also show you something. Okay. Yes. Now this is a very important thing. I think we have not discussed it earlier but I want to show you why we use clayent um starting from helium. Okay. If you need to understand this in a very in-depth manner. Helium is used for single page lookups. Okay. If you want to go to a website, if you want to only capture information from a single page, then you use Helium. Where it struggles, multi-page navigation, ambiguous content, and multi-step reasoning. Okay. Neon two credits semicmplex task. That means you need to go to multiple pages. Okay. or you need to go to one page and get multiple information. You need to go to the contact page, you need to get like uh phone number, email and everything.

#### 00:55:09

Yogesh Jaiswal: So that is for um neon right now where it struggles, it struggles on doing a deep research. Okay. Yes. Now we have argon. Argon is important for multiple searches and multiple uh information capture. Okay. And if you see where it struggles, if you use argon for simple single field lookup, it will kill the uh waste credits. Okay. So this is the thing. Now you have more models. You have GPT, GPT, advanced reasoning models. But see the agent is a web search agent. It works perfectly right. So there is no replacement. I think Gemini can replace it but Clayent itself is a very good thing. Okay. Now I want to show you something. Uh I think Okay. Yes. If you see this is called a clayent mo waterfall. Okay. Now even though you can be perfect in using clayent but you can never use anything at the first, right? I mean you cannot use neon at the first.

#### 00:56:37

Yogesh Jaiswal: Okay. You want to use helium first. But because if helium doesn't work then you move to neon. If neon doesn't work then you move to argon. Right? We need to understand that agent is going to be used on thousands of columns. Right? So if you are clear from day one what to use, you are going to save credits. Okay? Now there's one more thing which is very um okay this is like I mean this is a very uh uh like very interesting question and uh whenever you talk to a company who is a GTM engineering agency they will ask you this question right how would you confirm if client information is correct I mean if you run a clientent column that if the company is hiring 10 SDRs now how will will you confirm if it's correct or not right so you run another client column for judgment. Okay, so you run one column to get information and one column to validate information, right? So you can also do debugging in the other prompt rather than one prompt doing everything.

#### 00:57:51

Yogesh Jaiswal: Okay, this is a very interesting thing when you work with companies who have less companies to reach out to. I mean see if a company in India is selling to a bank there are only 100 banks or 200 banks in India right the good ones. Now you need to qualify the banks properly. So if a company is selling to Indian banks you need to do multiple cleent columns and it needs to be correct. Okay. So that's why you need to need use multiple client workflow for judgment calls. Okay. Again, cost control. Never run a clientent prompt into a full table. Okay? Test to 5 10 rows and then run it. Always default to helium. Okay? Don't use uh don't use the neon or argan because if if helium fails then you need to use okay. Also use conditional runs as we discussed. So only run on qualified rows. Okay. Use the meta prompter. So the prompter that you use to write a prompt is called a meta prompter.

#### 00:58:59

Yogesh Jaiswal: Okay, cool. Are you guys clear with cleent now? Does that helped you?

Alok: Yeah.

Yogesh Jaiswal: Okay, we need to also understand there is no need of an API key here. Cleaggent is itself is very good. Okay, it's a web search agent. Okay, it follows the instructions. It goes to pages and it works perfectly. And honestly um a good company or an agency have at least 100,000 clay credits. They always purchase the pro plan. So you don't even need to worry about um like spending a lot of credits also. Okay. So I've shared both of the documents on the WhatsApp group. uh please go through it and uh I think waterfall is also clear but let me see if I have a document for waterfall. Yes, I don't think I have it. Okay, cool. is So any questions in clientent run condition waterfall logics anything. Okay no problem. So now you need to start building what we are doing in clay.

#### 01:00:31

Yogesh Jaiswal: Okay. So as you have the list of 50 companies uh we have done this with samput right now u we validated the qualified the companies and then we moved to finding the people. So also start building the same thing in your clay because we are also going to build a portfolio out of it. Um go to your clay in the 50 companies you have selected qualify those companies uh make a qualification parameter and then find people find work emails and then um validate the emails. Okay, tomorrow we are going to cover validating LinkedIn URLs. Okay, and we are also going to cover few important stuff. So yes. Okay. Any questions? Anything?

Alok: Um hi, I had a few questions.

Yogesh Jaiswal: Yes. Yes. Hello.

Alok: Uh this is not regarding today's session by the way like uh like

Yogesh Jaiswal: Yeah. No, not problem.

Alok: uh like so I don't have any experience as a GTM engineer. Okay.

Yogesh Jaiswal: Mhm.

Alok: So like uh let's say if I want to get clients then how do I and also like a lot of people say suggest to uh get clients from Upwork.

#### 01:01:48

Alok: So how is that platform for GTM engineering?

Yogesh Jaiswal: See you need to understand that now leave the GTM engineering thing aside. Okay. Uh hospital have an operation theater right and someone is going to automate that. Okay. So anyone will not automate that. You need to be the perfectionist to reach that level to automate that. Okay. So you need to understand that when you don't even understand everything how it works even if you get a job you will lose that in a week.

Alok: Yeah.

Yogesh Jaiswal: Okay. So the best method is to learn everything perfectly. There is a learning curve for GTM engineering and also it's a skill. GTM engineering is a skill. It's not a department in a company. So if you learn GTM engineering you can always have freelance clients. You can have jobs. This is an ever going evergreen field for next two years at least. So you need to build a good portfolio and then reach out. That's my advice.

#### 01:02:48

Alok: Okay. So like what does my portfolio need to have? Like uh what what uh portfolio pieces put me as a

Yogesh Jaiswal: Yeah,

Alok: credible GTM engineer who will get hired?

Yogesh Jaiswal: you need to have a portfolio where you select a company, you Build a strategy document. You build a clay table. You show in clay table that how you have used clay in that. Then you push data to hair reach instantly. Build a successful campaign. Then you use cloud code to make it much better. Then you use nit to do certain automations at least five loom videos to show that you are a good GTM engineer.

Alok: Okay. through like the entire pipeline.

Yogesh Jaiswal: Yes.

Alok: I mean

Yogesh Jaiswal: Yes. No one will hire a person.

Neeraj Sujan: So Yog sorry will they also like I I have been interviewing and they have

Yogesh Jaiswal: Yeah.

Neeraj Sujan: been asking some metrics what was the reply rate how successful was the campaign so with the portfolio we are going to build we wouldn't have any numbers right so what to do about

#### 01:03:49

Yogesh Jaiswal: Yes, we need to also be uh clear that how the world works today because no one can start learning GTM engineering have a metric because we just started it out right we don't work we have not worked with a real client So very easy if you want to make the conversation better you can say that you have worked with some clients and there was a reply rate um and uh which you cannot share okay you can do a white lie or if you want to be honest you can say that I have not ran any campaigns but that will not give a good look so I'll give you some metrics okay for you to

Alok: Okay.

Neeraj Sujan: Hey,

Yogesh Jaiswal: understand the industry metrics the LinkedIn metrics are connection request rate acceptance rate should be 70% sent. Okay. Out of 100 requests you shared sent, 70 should be accepted. Okay. On top of the 70 accepted,

Alok: What?

Yogesh Jaiswal: there should be a at least 30% reply rate. Okay, that's the good metrics. Now, in terms of email, the email opening rate should be 90 plus% and the reply rate should be 3 to 5%.

#### 01:05:00

Yogesh Jaiswal: So these are the metrics but unless you go on ground and work you can never really relate to a metric. So you can easily say that um because you're starting it out you don't have any real client or proof. So there is no metrics as such but this is the metrics you can aim for. You can say like that the

Alok: And al also like how is LinkedIn as a platform to get clients?

Yogesh Jaiswal: Yeah.

Alok: Like a lot of people say suggest LinkedIn. So like in order to get client from there like uh other than like uh you know my case studies and few like informative post of about GTM what else do I need to post or anything you have specific in your mind.

Yogesh Jaiswal: See uh one advice I want to give you at least for next month till next month mid don't think about getting a client think about being a perfectionist

Alok: Mhm.

Yogesh Jaiswal: okay uh also in on LinkedIn you know I have shared a sheet for people to reach

Alok: Yeah.

Yogesh Jaiswal: out add them all into a LinkedIn,

#### 01:06:02

Alok: Yeah.

Yogesh Jaiswal: don't talk to them. Okay?

Alok: Okay.

Yogesh Jaiswal: You need to be super clear that GTM engineering is a very advanced thing to practice and you cannot make mistakes. It's expensive.

Alok: Yeah.

Yogesh Jaiswal: The clay plan a engineering agency uses is of $3,000 a month, right? They will not give the $3,000 clay plan to anyone, right? It's it's almost three lakh rupees a month. Then you have Harry, Chapolo, Claude, Deepline, Instantly, uh, Exa the complete stack that a GTM engineer uses of 5 to 10 lakh rupees a month. So you need to be super clear that no one will trust you before you have a good proof. Okay? So the first thing is to build a proof and build connections. Okay? Then go slow in the market. You can go as a list builder. There's a thing called lead list building. You can go as a lead list builder and then you can move to campaigns and lot other things.

Alok: Okay. And uh another thing that I've been seeing a lot lately is like people using AI agents to like do things not cloud code to orchestrate thing but AI agent.

#### 01:07:15

Alok: So like what is that and is that actually adding to the metrics that we just talked about?

Yogesh Jaiswal: Yeah, honestly uh no, I would not agree that. See, there are very few companies, one out of 10,000 companies would prefer using an AI agent because companies in Europe will not use an AI agent. Okay, their data is compliant. Even in US, insurance companies will not use, consumer companies will not use. So try to be clear that if one company's using an AI agent doesn't mean everyone will use it. Okay, they are just what you see on LinkedIn is just a gimmick, right? Everyone is posting to get traction.

Alok: Yeah.

Yogesh Jaiswal: It's not real. I still use clay today. Okay.

Alok: Is that

Yogesh Jaiswal: Yeah, I used to use clay today. Uh and even I have worked with multiple good brands or names but we still use clay, right? But we have clawed also and everything. So don't just wait patiently and learn everything. That's my advice.

Alok: Okay.

#### 01:08:14

Alok: Okay.

Yogesh Jaiswal: So one of the person in the earlier batch have recently joined an agency and she put two months and I think today she joined and she's a fresher with no background. She joined at like $45,000 a month.

Alok: Wow.

Yogesh Jaiswal: So you can understand that if you patiently work on your LinkedIn, work on your skills and create a good portfolio, your entry becomes very easier. Or if you try from today, your entry becomes difficult. Just to be clear, go very slow and if you go slow, there is a long-term growth in GTM engineering.

Alok: Yeah.

Yogesh Jaiswal: Okay, because even I am not I have not reached that $5,000 $6,000, right? I have reached only till 3,000. So you can see that the grow is slow but it's growing. You don't go down here in GTM engineering.

Alok: Yeah, I got it.

Yogesh Jaiswal: Okay, cool. Uh, yes. Any questions? Anything? Cool. Then uh I think this is it. Um, yes. So, start preparing a good play table. Honestly, I don't want to like help you one on one because it's very easy to now go from uh selecting a company to building a good strategy table around it, clay table around it. Try to build a good clay table. If you need help then I am here. I'll help you out. But the table decides that what kind of GTM engineer you are honestly the table can itself tells that how much the company would be willing to pay you. So try to build a good clear table first and that's my advice. Okay, cool guys. Uh let's connect tomorrow to learn more and uh Yep. Have a nice day.

sampath vemulapati: Thanks.

Yogesh Jaiswal: Yes.

sampath vemulapati: Have a nice day.

Yogesh Jaiswal: Welcome. Welcome.

#### Transcription ended after 01:10:25

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.