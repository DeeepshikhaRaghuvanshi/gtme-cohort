# D11+D12_ The data landscape + Apollo deep dive - 2026_09_15 08_54 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D11+D12: The data landscape + Apollo deep dive

Sep 15, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

GTM engineering session covering market sizing, list building, and data deduplication.

GTM Engineering Standards and SLAs

Data-related tasks require a same-day delivery SLA.

List building turnaround varies: simple tasks require under 2 hours, while complex builds take 6-8 hours.

ClickUp serves as the standard project management tool for GTM engineering task assignments.

Maintain data hygiene by separating city, state, and country columns and using standardized, single-word headers for placeholders.

Strategic List Building Methodology

Verify the purpose of the list (e.g., event invite, cold outreach) and confirm if the reach-out is fresh or a follow-up before initiating builds.

Distinguish between 'People First' searches (start with job title) and 'Company First' searches (start with firmographics).

Exclude companies with 1-10 employees, as they typically lack sufficient budget for these services.

Adjust parameters (e.g., widen location, shift seniority) if initial search volume is insufficient for campaign requirements.

Data Source and Tooling Strategy

Sales Navigator is mandatory for 'People First' lists to ensure high data accuracy.

Note that platforms like Apollo and Prospio may reflect data with up to 30 days of lag compared to real-time LinkedIn updates.

Avoid relying on a single data source; use at least 3 data providers to ensure robust and comprehensive lists.

Data Filtering and Segmentation

Exclude non-relevant departments, such as advertising, to improve list precision when filtering for specific personas.

Apollo ranks seniority as Director below Head; adjust filtering logic to avoid confusion with internal hierarchy expectations.

Partners often represent channel or enablement roles rather than decision-makers; review lists carefully before including them.

Data Sourcing and Deduplication

Utilize a minimum of 3 data sources, including Apollo, Prospeo, and Sales Navigator, for comprehensive coverage.

Perform combining and deduplication processes within Claude; avoid Clay, which functions as an orchestration platform rather than a data source.

Apply deduplication using a 3-step hierarchy: LinkedIn URL, then Email ID, then Full Name combined with Company.

Data Verification and QA

Flag false professional profiles by matching work email domains with listed company names to filter out contractors.

Implement QA parameters to verify that the company name on LinkedIn matches the associated email domain.

Strategic GTM Framework

TAM, SAM, and SOM filtration parameters rely on learned parameters from live market experimentation.

Reserve n8n automation for enterprise clients; startup builds should rely on manual processes.

RB2B personal visitor tracking is restricted to the US market due to privacy compliance.

Next steps

[Neeraj Sujan] Paste Apollo Data: Upload the Apollo prospection information to the system.

[Yogesh Jaiswal] Resolve Location Discrepancies: Research the most accurate method to handle LinkedIn location discrepancies and report the findings back to the team.

[The group] Build Client List: Download data from at least 3 providers to create a comprehensive list. Combine and remove duplicates to ensure a clean final output.

[Medha Das] Manage Partner Lists: Create a Google sheet of partner profiles if client data contains excess entries. Share this list with the client for verification.

[The group] Clarify Client Requirements: Reach out to clients to verify requirements when list results are insufficient or ambiguous. Ensure clear understanding before proceeding with data builds.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 15, 2026

### D11+D12: The data landscape + Apollo deep dive

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D11+D12: The data landscape + Apollo deep dive

Meeting records Transcript Recording

#### Summary

GTM engineering session covering market sizing, list building, and data deduplication.

Market Sizing and Search Criteria
Founders require total addressable market data pulled from multiple tools. Practitioners must identify whether to use people first or company first search criteria.

Data Quality and Hygiene
Sales Navigator provides accurate LinkedIn data for US targets. Extracted data must undergo deduplication using Claude before transfer to Clay.

List Building Methodology
List building requires determining outreach channels and using multiple data providers. Total addressable market parameters are defined after market experiments.

#### Next steps

[Neeraj Sujan] Paste Apollo Data: Upload the Apollo prospection information to the system.

[Yogesh Jaiswal] Resolve Location Discrepancies: Research the most accurate method to handle LinkedIn location discrepancies and report the findings back to the team.

[The group] Build Client List: Download data from at least 3 providers to create a comprehensive list. Combine and remove duplicates to ensure a clean final output.

[Medha Das] Manage Partner Lists: Create a Google sheet of partner profiles if client data contains excess entries. Share this list with the client for verification.

[The group] Clarify Client Requirements: Reach out to clients to verify requirements when list results are insufficient or ambiguous. Ensure clear understanding before proceeding with data builds.

#### Details

Purpose of Data and Market Sizing in GTM Engineering: Yogesh Jaiswal explains that founders frequently ask GTM engineers to determine market sizes such as the total addressable market and serviceable addressable market, requiring real numbers pulled from tools like Apollo and Prospio. Yogesh Jaiswal notes that combining data from multiple platforms provides a comprehensive view for clients looking to sell products in specific regions like Australia (00:04:51).

Project Management, Client Demographics, and SLAs: Yogesh Jaiswal introduces ClickUp as the primary project management tool used in GTM engineering, noting that while practitioners often operate from countries like India or Europe, clientele typically consists of high-paying United States companies (00:07:20). Yogesh Jaiswal explains that tasks assigned on ClickUp are bound by service level agreements, where data-related tasks and list building usually require same-day delivery ranging from 2 to 8 hours depending on complexity (00:08:40).

Campaign Purpose and Departmental Hierarchies: Yogesh Jaiswal emphasizes the importance of understanding the purpose behind a campaign and department structures before building lists, using the product department hierarchy (ranging from Chief Product Officer down to Associate Product Manager) as an example to illustrate how departments operate (00:09:52). Yogesh Jaiswal outlines key pre-build questions that must be asked, such as the reason for building the list, which includes cold outbound, event invite, webinar invite, partnership reach out, and advisor reach out (00:11:08).

Strategy for Fresh Versus Multiple Reachouts: Yogesh Jaiswal highlights that when handling cold outbound campaigns, practitioners must determine whether the target audience is being contacted for the first time or if multiple prior reachouts yielded no response. Yogesh Jaiswal explains that if multiple reachouts already occurred without response, a fresh build is unnecessary; instead, existing data stored in Google sheets should be retrieved, enriched, and validated for emails and LinkedIn rather than re-downloaded (00:13:16).

People-First Versus Company-First Search Criteria: Yogesh Jaiswal presents a real-world case study involving Castle, an artificial intelligence voice agent company selling to chief lending officers in the insurance industry, to teach the distinction between people-first searches (when job titles and cities are specified) and company-first searches (when specific companies or employee thresholds like 10,000 plus enterprises are mentioned) (00:14:44) (00:19:10). Medha Das and Khushboo suggest filtering by industry, banking and financial institutions, and enterprise company size during the discussion, while Sampath Hari GTM proposes factoring in location vicinity such as a 30 to 40 kilometer radius (00:17:41). Yogesh Jaiswal stresses that practitioners must correctly identify whether to use a people-first or company-first search to avoid expensive mistakes (00:22:25).

Refining Location and Seniority Filters for Chief Lending Officers: Yogesh Jaiswal demonstrates searching Prospio for chief lending officers in New York, finding only 77 results, which is deemed insufficient for an in-person event, leading to the decision to expand the search to the entire United States where 1,400 (or 1,363 suite-level) chief lending officers are found (00:23:37). Yogesh Jaiswal explains the importance of filtering out companies with 1 to 10 employees due to lack of budget, ultimately narrowing the United States list down to 1,286 chief lending officers across 1,146 unique companies (00:28:24). Khushboo inquires about department filters and seniority levels, prompting Yogesh Jaiswal to demonstrate searching for vice presidents of lending in New York, yielding 773 results and approximately 282 unique company-filtered profiles (00:31:13).

Handling Information Technology and Data Persona Requirements: Arti Fabiyani asks whether companies selling software must also reach out to information technology and finance teams, to which Yogesh Jaiswal clarifies that list building is a strategic part controlled by clients who provide exact requirements (00:34:45). Yogesh Jaiswal introduces another client, Daxter, an artificial intelligence native data operations platform targeting data leaders at director level and above in Germany, and discusses how to handle people-first searches with location parameters separated by person and company headquarters (00:35:55). Yogesh Jaiswal explains that for LinkedIn outreach, filters must be narrowed further by removing smaller company sizes (1 to 10 employees) and focusing on senior executive suites due to LinkedIn's monthly connection limits of 700 people per profile (00:38:48).

Data Hygiene and Column Structuring in Google Sheets: Yogesh Jaiswal shares a real-world example of a Phoenix dinner list, detailing how data clarity is maintained by separating city, state, and country columns and distinguishing between global data and total addressable market data processed via Claude (00:42:49). Yogesh Jaiswal outlines mandatory Google Sheet column structures for people-first lists, including first name, last name, full name, clean first name, job title, LinkedIn URL, cleaned company name, company domain, and separated location columns for city, state, and country. Yogesh Jaiswal emphasizes that clean first names and cleaned company names must be single words or appropriate placeholders for email campaigns to prevent awkward greetings like "Hi there" or overly long company names (00:46:14). Deepshikha and Yogesh Jaiswal discuss defining total addressable market and sorting data using Google Sheets text filtering (00:44:38) (00:50:48).

Mandatory Use of Sales Navigator for People-First Lists: Yogesh Jaiswal dictates that a Sales Navigator export is mandatory for any people-first list to ensure high data quality (00:52:11). Alok and Gagan Bhaisa note that Sales Navigator provides LinkedIn data and roughly 92 percent correct data regarding individual employment (00:53:43). Yogesh Jaiswal explains that tools like Apollo and Prospio take up to 30 days to process location updates, whereas individuals update their LinkedIn profiles immediately upon moving, making Sales Navigator essential for accurate location targeting in regions like the United States (00:55:03).

Addressing Base Location Discrepancies: Gagan Bhaisa raises a challenge regarding individuals who keep their company's base location on LinkedIn rather than their actual physical location, such as someone based in India listing their location as the United States (00:56:08) (00:58:41). Yogesh Jaiswal acknowledges this is a genuine problem, explaining that while junior roles frequently fake locations, senior personnel (C-suite, vice presidents, directors) rarely do so because they are not monitored in the same way. Yogesh Jaiswal notes mitigating strategies such as conducting outreach during United States night hours, blocking landing pages from opening in unauthorized countries, and recognizing that false locations affect only about 5 percent of profiles (00:57:10) (00:59:42).

Multi-Source Data Providers and Department Filter Tips: Yogesh Jaiswal states that GTM engineers should never rely on a single data source and must use three or more data providers, which explains why clients prefer hiring agencies that maintain 8 to 10 data tools over hiring individual engineers (01:01:06). Yogesh Jaiswal concludes by offering a quick tip on department filters in tools like Prospio, explaining that searching by specific departments like artificial intelligence combined with location parameters makes it easy to isolate targeted profiles such as chief roles in Bangalore (01:02:49).

Apollo Seniority Levels and Department Filtering: Yogesh Jaiswal demonstrated their approach to filtering and excluding specific departments and job titles within Apollo, noting that while standard decision-maker seniority follows a progression of director, head, vice president, and C-suite, Apollo's internal seniority listing counterintuitively places heads below directors (01:04:20).

Excluding Partner Seniorities in Prospecting: Medha Das raised their concern about why partner roles are excluded given their traditional decision-making authority, prompting Yogesh Jaiswal to explain in their response that partner listings often include channel partners or external partnerships—such as Mahima Aurora managing channel partners—rather than primary buyers, and advised reviewing or omitting them to protect data quality (01:05:34).

Data Export Sources and Pre-Clay Processing: Yogesh Jaiswal outlined their filtering parameters such as company locations, revenue, funding, and excluding nonprofit business models, instructing that data extracted from three separate sources—Apollo, Prospio, and Sales Navigator—must undergo their combined deduplication process in Claude before being transferred to Clay (01:09:33).

Platform Distinction Between Clay and Traditional Data Providers: Deepshikha asked their question regarding whether Clay provides more trusted data sources, leading Gagan Bhaisa and Yogesh Jaiswal to share their perspective that Clay functions strictly as an orchestration platform rather than a data platform, making established repositories like Apollo and Prospio irreplaceable due to decades of historical data collection (01:12:43).

Handling Scraped LinkedIn Profile Discrepancies: Yogesh Jaiswal explained their reasoning regarding Sales Navigator capturing contractors working for service providers like Infosys or TCS who incorrectly list end clients like Google on LinkedIn, whereas Apollo and Prospio filter out their invalid profiles, requiring a quality assurance check in Claude to flag mismatches between company names and work email domains (01:14:16).

Claude Prompt Parameters for Combining and Deduplicating: Yogesh Jaiswal detailed their Claude prompt mechanics for data consolidation, specifying that the system must retain the best available work email in a single column and enforce a strict deduplication sequence starting with LinkedIn URLs, followed by email IDs, and finally full names paired with company names (01:18:29).

TAMs and Outreach Tool Applications: Deepshikha shared their inquiry about Total Addressable Market metrics and outreach tools from a prior session, and Yogesh Jaiswal clarified in their response that Total Addressable Market parameters can only be accurately defined after launching market experiments, while adding that automation tools like Net 10 are reserved exclusively for enterprise clients with large budgets and technical teams (01:21:08).

List-Building Methodology and Regional Limitations of RB2B: Yogesh Jaiswal outlined their summary that list building requires determining the outreach channel, utilizing at least two data providers, and validating output counts with clients, while responding to Deepshikha by explaining that visitor tracking tool RB2B operates solely within the US market due to European regulatory compliance restrictions (01:23:20).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 15, 2026

### D11+D12: The data landscape + Apollo deep dive - Transcript

#### 00:04:51

Yogesh Jaiswal: Hey, good morning.

Neeraj Sujan: Warning.

Yogesh Jaiswal: uh n have you pasted the Apollo prosp

Neeraj Sujan: I'll do it. Yeah.

Yogesh Jaiswal: the the reason we are doing it because we need a real number.

Neeraj Sujan: Okay. Okay.

Yogesh Jaiswal: Um also one more reason that founders always ask for that those numbers like you know uh how big is the time so we'll do that okay no

Neeraj Sujan: Mhm.

Yogesh Jaiswal: problem uh let's move back here yeah hi Deepshikha ma how are you hi

Deepshikha: Hello.

Yogesh Jaiswal: hi okay okay so meanwhile everyone joins I just want to mention something like what we're going to discuss in the data layer and the several topics we're going to discuss is about data. Um, okay. One big reason like a founder needs us as a GTM engineer right now is because they want someone who not only deal with data but who also understand the numbers behind it. Uh that's why when I was giving you the task and I told that okay we need Apollo and Prospio screenshots. This was the reason because um founders today will directly ask you a question that um you know if I want if I want to sell my product in Australia how big is my market right so the responses that we give back to the pro to the client would be um according to Apollo these are the companies we can reach out according to Prospero these are the companies we can reach out and when we combine both

#### 00:07:20

Yogesh Jaiswal: information we can give a combined view about it. So whenever we are going to do anything related to GTM engineering, we have to present the data and uh mostly I mean have you used ClickUp earlier? Anyone of you? Yes.

Khushboo: No.

Yogesh Jaiswal: Okay, got it. Uh ClickUp would be Okay. So I'll show you what is ClickUp. Okay. ClickUp is a project management tool. Uh mostly in GTM engineering you would be working on ClickUp. Okay. So the I mean most like most of the people who um are doing GTM engineering are from other countries like India you know Europe other countries but the clientele is in US like the high paying clientele. So you would always get task in ClickUp. Okay. So let's go back. So let's think about the data layer right now that if you get a task, right? So how big is your tab, right? So this will get assigned to you on clickup. Okay? And let's say the assigne is needed.

#### 00:08:40

Yogesh Jaiswal: Okay? So the moment it get assigned, it also follows an SLA. Do you understand what is an SLA?

Neeraj Sujan: This service level agreement

Yogesh Jaiswal: Yes. Okay. Let's go back. Yeah. So the moment the task get assigned to you, you will also get an SLA. Typically data related task the SLA is one day same day. Yeah. Same day delivery. What most data task okay so let's say whenever you get a data related task assigned the delivery date would be same day. So in today interviews and let's say if you operate your own agency you reach out to a company they often ask that if I ask you to build a list how soon you can deliver and uh you need to be super clear that any complicated list build can take up to 3 to 6 hours. Some manual changes can take more to 2 3 hours. But a list build oftenly takes less than a day. Right? A small build can take uh less than like 2 hours.

#### 00:09:52

Yogesh Jaiswal: A complicated one can take 6 to 8 hours but the SLA for list building or data related task would be same day. Okay, got it. So yeah so now you have covered the tam sam part right now this is this part you have covered okay so let's remove this okay okay so yeah now every time when you get a campaign or any any kind of data build you need to also understand that what is the purpose of that uh you know set of people okay so this is a big mistake um mostly people make and that's why you also need a sales bit of sales knowledge in GTM engineering right so when I say I mean so let's say we get a requirement that we need to reach out to all of the product people right so we are we are going to sell our software and we have to reach out to all of the product people right so we need to be super clear that if we are going to reach out to the product people what what the how like okay you need to understand how the department looks like in a company how a product department looks like right.

#### 00:11:08

Yogesh Jaiswal: So how you know like you can just go ahead search here that how does the product man looks like G. Okay. Okay, you can see so at C level you have chief product officer, you have VP of product, right? You have director of product, you have group product managers, you have principal product managers, you have product leads, you have senior product managers, then you have day-to-day operations, product manager, associate product manager, right? So whenever we have any kind of data that we want to build, we need to have several questions in our mind. Okay. So let's say you get assigned a list building, right? So these are the questions you should always ask your client first. Okay. Build would be the part two before build. These would be the questions. Okay. The first Yeah. First question would be the reason why we are building the list. Okay. And you would get answers like old outbound, event invite, webinar invite, partnership reach out, advisor reach out.

#### 00:13:16

Yogesh Jaiswal: Okay, you need to also understand that okay when you get an answer that okay we are doing cold outburn right so you need to again ask a question that is this set of people you are reaching out is this the first time you're reaching out to them or the second time okay so fresh reach out or multiple reachouts happened earlier but no response. Okay. When multiple reachouts have happened earlier but no response, you don't need to get download again. Right? This is a very smart way to like do GTM engineering. So when they say okay we have already reached out to this set of people earlier we didn't got any response. you should just get the data from the earlier person or the data would be stored in a Google sheet. Okay, when that kind of data is there, you just need to enrich the emails, validate the emails and if it's LinkedIn, validating LinkedIn and you just need to reach out, right? So there is no fresh build required. Okay. Now when you are clear why you're building the list, second and the most critical part like this is where your decision making comes in. tools you are going to use.

#### 00:14:44

Yogesh Jaiswal: Okay. Now I want to give you a real case scenario. Okay. Insurance industry is a like very huge industry in US and most of the GTM engineering agencies these or clients you get are from insurance. Okay. There is a role called chief lending officer. Okay. So whenever you see AI tools where AI is in insurance, AI is in uh you know bookkeeping or I I think anything insurance related AI tool mostly you need to reach out to chief lending officers right and this is a very common term in insurance industry in US right. So now if I give you a let's say if we get a task right the task is find all the chief lending officers in New York that we can call or an inperson event. Okay. And most probably you would be getting these kind of tasks. I mean at a initial level like at least for next uh when you start your career like at least 3 to four months you would be getting all of these tasks right.

#### 00:16:05

Yogesh Jaiswal: So when you get the task find the chief lending officers in New York that we can call for an inerson event right and let's say the client is castle. Okay. So, I'll show you what Castle does. Castle. Yeah. Yeah. Okay. So, this is the company, right? They sell to banks and lenders and they sell to chief lending officer. Okay. Now, let's go back. So now I want to understand what approach you would follow then we can come up to approach that um what would be the kind of what what are the kind of approaches we are going to follow but just want to stop here and ask you if I ask you what's the approach you would follow or how would you like go about Okay, let's chief lending officer. Yeah, please please go ahead.

Khushboo: Who are the uh champion people in the insurance industry?

Yogesh Jaiswal: Sorry.

Khushboo: Who are the like the champion in the insurance industry?

Yogesh Jaiswal: Uh yeah, the question is good but can you understand like can you read what you have to build?

#### 00:17:41

Yogesh Jaiswal: Like if you understand the task Yeah. The task is you need to find all of the chief lending officers in New York that we can call for an inerson event and you even have the client. Okay, castle is basically AI Voice AI agents for insurance industry where you know you need to take a premium whatever you want you can automate that part okay with AI voice AI agent so I just want to understand what is your approach like how do you think to build the list what do we go in and search in Apollo or Prospio

Medha Das: Uh we can search by industry like we can

Gagan Bhaisa: I want you.

Medha Das: have banking and financial institutions maybe.

Yogesh Jaiswal: Okay, got it. What?

Khushboo: You can also have a filter like enterprise like like how big is the company like enterprise wise.

Yogesh Jaiswal: H

Sampath Hari GTM: So the location also we can put wherever the event is happening. So because like people don't like to travel so much probably we can say that in the vicinity of 30 to 40 km

#### 00:19:10

Yogesh Jaiswal: Okay, I'll just rephrase this. um the client tells that you need to find all of the chief lending officers in New York that they want to call for an inerson event. Okay. Now, we can also remove this inerson event to they want to book a meeting, right? Okay. And it can be also to call them for if they're interested to become advisers. Okay. So, let's let's not focus on this part. Let's focus on the two important parts. This is a job title. Okay. And this is a city. Got it? So we need to understand that the two information we have right now is job title and city. Right? Whenever we have job title information, let's say chief lending officer, chief execute, anything people. Okay? That is called a people first search. Okay? People first search means that you need to go on the tool and search the people first. Okay. Now, if you get a task like find the chief lending officers at,000 plus banks in New York.

#### 00:20:22

Yogesh Jaiswal: Now, this also contains a company information, right? This would be a company first search. Okay. So, are you clear with when to use people first search and when to use company first search?

Khushboo: Um so like when the client gives us that information can we ask them like for example if they just give chief lending officer but then can we ask them like uh should be fine for like 1,000 plus pence or no they Okay.

Yogesh Jaiswal: Yes. Yes. So if you see The first thing that you go and ask them is the reason why we are building the list.

Khushboo: But the number house and plus banks like will they give or or they can give a very big uh Peace.

Yogesh Jaiswal: Okay, one more thing we need to understand. Uh I mean you may find it weird but the founder of just building the product they don't have time to even figure out all of these things. So even though you say thousand plus employees banks, this would be your judgment more as a GTM engineer rather than their judgment.

#### 00:21:33

Yogesh Jaiswal: So okay, they don't have a sales or marketing team. And these are the companies who need GTM engineer right now. Okay, they don't have a sales team. They don't have a marketing team. They don't know sales. They don't know marketing. And they don't want to increase the headcount. Hiring a employee in US is very expensive. They don't want to hire two SDR, one BDR. It's not easy for them. they would just get one person from India or maybe in US. Okay. So this should be in your understanding but if they give you well and good okay but you need to always ask that why we are building the list. Okay. See typically this part will handle by the agency. Okay. You don't need to worry about it. If you work for an agency, they would handle the strategy part like with employee size, the reason why they are building the list. But you need to be also clear.

#### 00:22:25

Yogesh Jaiswal: Okay. So when I say find the CEO of all 10,000 plus AI companies in the world, what would you do? you would do a people search or a company first search for this file.

Deepshikha: company first.

Yogesh Jaiswal: Yes. Okay. Yes. So just please make this a note that never make a mistake here because um you are going to do a lot of work after that and any mistake would be expensive. So just understand if a company is mentioned company first if company is not mentioned like this people first. Okay. So let's remove this. Now I set to find chief lending officers in New York. Okay. So very easy. I go into Prospio. I search chief lending officer. Okay. You can see there is no employee mentioned right now. And I am not even asking the prospect or or sorry the client. Okay. I'll just go here. Click to location city New York. Okay.

#### 00:23:37

Yogesh Jaiswal: So for New York, New York, New York is the city. Okay. New York, US is the state. Okay. So state and country are like that in are like this in tools. Okay. If you see New York, United States, New York, these are states. Okay, new. This is state country. This is state city. Okay. So, let's pick up this. Okay. So, can you see how many chief lending officers I have in New York? Can you see this number? Okay. So, do you think that if I reach out to 77 people, I have enough people to come on a dinner?

Gagan Bhaisa: No.

Yogesh Jaiswal: Yes. So we don't have enough people that would come. Okay. So red flag. Okay. You cannot build this list. You need to now change the location. You need to now go at a state level. Okay. So let's do this.

#### 00:24:49

Yogesh Jaiswal: Okay. In New York itself you have uh state also you have only 77. Okay. So, I think we need to go entire US. Yeah. Yes.

Sampath Hari GTM: U so Yogesh can we also go second in charge after the chief learning officer like probably whoever is after chief learning officer

Yogesh Jaiswal: Uh you are right. But we need to also understand that I mean think like that from a very strategical point of view that whenever you get assigned a task from the

Sampath Hari GTM: Perfect.

Yogesh Jaiswal: client you need to be very clear that these guys are not even assigning just the way like okay let's assign something they think too much about it right so you cannot go back to them with a incomplete answer okay we have less chief lending officers now let's do something else right like that Because they are building the product for the chief lending officer. We need to be clear that they are only going to sell to chief lending officer. Right now I'm showing you how you will approach to this list.

#### 00:25:55

Yogesh Jaiswal: Right?

Sampath Hari GTM: Turn this.

Yogesh Jaiswal: How a good GTM engineer would approach to this list. Now in thei entire US I have seen that there are 1,400 chief lending officers. Right? And and by the way I have worked with uh Castle AI as a GTM engineer. So this is all real case studies I'm giving you. So when we go to Prospio yes okay so what I see is New York doesn't have a lot of chief lending officers but US have like 1400 officers right but again I need chief lending officer okay one more thing we need to understand whenever a job title contains okay I'll also clear out something whenever a list build contains seniority level okay Yeah. The seniority level is C level. Yeah. Can you do you understand this? Chief is a seniority C level. Are you clear?

Arti Fabiyani: Yeah.

Yogesh Jaiswal: Okay. So we need to be super clear that the chief lending officer is also containing chief which is a seniority level.

#### 00:27:07

Yogesh Jaiswal: Okay. So we cannot make a mistake there. Let's go to seniority and select chief. Okay. So can you see this? There are 139 in total but only se are 1365 63. Okay. So there was some false people that we don't need. Okay. We don't even need owner and founder also only seesuit. Okay. So there are 1363 chief lending officers. Right? Now you cannot again you can again cannot go back to the uh client tell okay we have 1363. Okay. You need to also do select per company. This means for from per company how many people we have. Okay. So let's do one. So we have 1 2 unique companies. Okay, if I select so okay you just to let you know select per company filter means if one company have one person how many unique companies are there so I said one so in this list only one one company would only have one person okay but again uh we have 120 1221 unique people okay now we do one more thing okay let's go to employee count Okay.

#### 00:28:24

Yogesh Jaiswal: See, I want to I want to show you something that do you think a company would sell to 1 to 10 employee companies? What do you think about it?

Sampath Hari GTM: No.

Khushboo: I mean they won't have budget for it.

Yogesh Jaiswal: Yes. Yes. But what what do you think about 11 to 20?

Keya Gupta: same thing. I mean, maybe more

Gagan Bhaisa: still can sell but pretty unmatured.

Yogesh Jaiswal: Yes. But can we do a red flag for 1 to 10? Like we don't need this.

Sampath Hari GTM: Yeah.

Yogesh Jaiswal: Can we remove this? Okay.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Let's pick up from 11. Okay. See if you see the number 74 is not a very big number. Okay. So I think that's a good idea. Okay. Now what do you think about this 10,000 plus enterprises? Would you include

Khushboo: They already might have the

Yogesh Jaiswal: H?

Khushboo: information.

Yogesh Jaiswal: Okay. Just just a heads up that we don't need to worry about anything above 100 or or all these things.

#### 00:29:40

Yogesh Jaiswal: Okay. It's fine. The main culprit is this 1 to 10. This like these guys would respond to you, talk to you, but they don't have money. Okay? So, let's not include the 1 to 10 mostly. Okay? Now we have 11146 uh unique companies And uh let's say if we remove the per company we have 1286. Okay. So I go to the task again and I say that 1286 in the entire US as New York only had 76 Yellow from 1146 unique companies 1 to 10 removed. Okay. So this should be your answer when you go to the client that you did a New York search. Okay. New York only had 760 chief lending officers. That's why this outreach cannot be done. Okay. So you need to call a different kind of seniority level to do a event in New York. Okay. But because they are doing something for chief lending officers, we have a chief lending officer number for them.

#### 00:31:13

Yogesh Jaiswal: Okay. So they have 1286 chief lending officers. It's there in the entire US and the companies are also unique 1146. So we can plan out a strategy for these guys. Okay. So this is how you should think for a you know in terms of list building. I mean you need to be super Yes. Yes.

Khushboo: Can you go back to uh Apollo?

Yogesh Jaiswal: Trust me. Okay. Okay. Yeah.

Khushboo: Um so when you like filtering out like uh Cuit no in the seniority so like other departments are zero is

Yogesh Jaiswal: Yes.

Khushboo: it because like there aren't those departments in the industry or like for example if someone says uh find out vice president but now there are like no vice president or very few even in like United States.

Yogesh Jaiswal: Mhm.

Khushboo: So like is it because VPs are not there in the in that industry particular industry?

Yogesh Jaiswal: Yes. Because our filter is also very strict like we are searching directly for chief lending officer. Okay.

#### 00:32:25

Yogesh Jaiswal: Now let's say let's say we understood that there are less chief lending officers in New York. then we need to do a debug here. Okay. So the department we are searching is lending. Let's search lending and let's again go back to New York. Okay. So you will get an answer easily. Yeah. See now you have more people. Okay. And now if you go to seniority level you may find other seniority as well. So, Can you see VP?

Khushboo: f*** this.

Yogesh Jaiswal: These are all my my ICPS by the way. Okay. I like when we sell castle, we even contact them. But we are we were doing this event for uh chief lending officer dinner event. But now we have an idea that there are more VPs in uh New York. So what would I do? I would just call the VPs

Khushboo: Okay.

Yogesh Jaiswal: I think I select let me select the city New York. Yes, I think it's the same.

#### 00:33:40

Yogesh Jaiswal: Yeah. So, you can see easily I have 773 vice president of lending. Okay. And by the way, this is just one step below chief lending officer. So now I have a clarity that okay, that doesn't work but this will work. Okay. Now again I would when I built this list I would have more exclusions. Okay I don't want APs. Okay. So typically in yeah so typically when you build a list of VPs you don't include AP. APS are assistant wife like this one. Okay. So when you clean this list this will come down to around 500 people. Okay. And then you can think from a per company point. Let's say from one company you need to only invite one person. So can you see now only 282 people.

Khushboo: Thank you.

Yogesh Jaiswal: So this is how you get more clarity about the data. Okay. Uh yeah let's go back here. Okay. Yes.

#### 00:34:45

Yogesh Jaiswal: So you understood people first list and company first list. Okay. You even understood how search works in Prospio. Okay. Now these are few things that you need to be careful about. Okay. First is playing around with filters. Okay. Now you might not get this kind of task that find all of the CTOs or CEOs, right? you might get that you you might get a task that um reach out to IT teams in Germany. So yes, Arti.

Arti Fabiyani: Uh so uh if a company is selling a software uh so they also have to reach out uh not only the niche uh domain but uh to the IT and finance team as well. Right?

Yogesh Jaiswal: Yes.

Arti Fabiyani: So we have to create a list for that particular domain as well.

Yogesh Jaiswal: No list build uh is a strategical part that is controlled by the client. They would give you what you need to build. You cannot say that I would build this. Okay.

#### 00:35:55

Arti Fabiyani: Okay.

Yogesh Jaiswal: Yeah. Now the second Important thing is playing around with filters. Okay. Now you get a task that reach out to. Okay. So I'll even show you the client. Okay. So yeah this is again a client and they sell to data teams. Okay. Now you know you might get a task because when you work in an agency you have tons of clients that you work. Okay. So you would get a task like reach out to all the data personas in Germany. Right now you get a client and you even So this is a people first list or a company first list according to you.

Sampath Hari GTM: People

Yogesh Jaiswal: Yes. Now you say Daxter personas, right? So yeah, this is what Daxter does. It's a AI native data operations platform, right? I just want to sum up for you so that it doesn't get complicated. Daxter sells to data teams. Okay, so Daxter personas are data leaders, director plus.

#### 00:37:21

Yogesh Jaiswal: Okay. So now we need to be super clear that whenever we get any kind of company and any kind of department as a uh requirement we need to build our own method of building the list. Okay. So data leaders right and Daxter. Okay. So let's go back to uh this again cross view. Okay. Let's select the location first. So okay very easy. Select the easy things first. What are the easy things you got? Germany and director plus. Okay, these are the easy things. So you again go here, you select location as Germany. Okay. And also the client location is also Germany. Okay. The company location I mean this is a uh do you understand what does this mean people and companies location? What like what's the separation difference?

Deepshikha: Yeah. So, where the person is located and where the company's headquarter is.

Yogesh Jaiswal: Yes. Yes. So this is where you need to always ask the client that when you say you're reaching out to Germany is the company should be also in Germany or companies can be anywhere.

#### 00:38:48

Yogesh Jaiswal: Okay. everything should be cleared right let's consider that the company should also be Germany and person should also be in Germany right now we said he said to reach out to the extra personas which are data leaders. Okay. So let's only search data. Seniority would be director plus. Okay. And whenever you have a seniority like director plus head plus never include partner. Okay. It's it's not right. Okay. So can you see I got four five 41 52 data personas. Head of data data data data. Right. I'll do one basic thing. I'll go go to employee headc count and I'll remove the 1 to 10. Okay. Yes, I have 4,000 30 contacts, right? Uh if this list build this list build was emails then I have right numbers. Okay, correct numbers. But if this list build was for LinkedIn outreach then I should narrow down more. Okay, because LinkedIn outreach only depends on the profile we connect.

#### 00:40:19

Yogesh Jaiswal: Okay, and we would be learning that. So let's go back to Prosper again. Okay, now if it's LinkedIn, then we need to narrow down more. Okay, how you will narrow down? Remove these companies. Start from thousand 100 plus. Okay. and also go to job title and remove the one which is causing you trouble. Okay. So let's say I remove director and head. So how many I have VPN suit only 366, right? So see again this is a very experimentation experimentational thing. You can do more variations but Yeah. Yeah. Khushboo

Khushboo: Why we remove the uh companies like 1 to 10 employees or like for LinkedIn?

Yogesh Jaiswal: see when we reach out to someone on LinkedIn there is a limit. Okay. We can only reach out to 700 people in a month. LinkedIn is a limited thing.

Khushboo: Okay.

Yogesh Jaiswal: Yeah. Yeah, when you reach out to 700 people in a month, there might be multiple campaigns, right?

#### 00:41:30

Yogesh Jaiswal: You and this is for per profile. Typically, when you work with a client, they have two profiles. Okay? So, when you do a LinkedIn outreach, it should only be done to the exact senior people, decision makers, because you don't want to waste your uh LinkedIn outreach on something, right? And emails, you know, it's unlimited. Emails can be unlimited, right? You can get so many domain, so many emails. So these numbers are totally fine. Okay. So what you do you just filter it more. Okay. Now I would before even I move to the next step I want to show you a real all of the real list build and what was the question that was asked what was the approach that has been followed and how that list build have done. Okay let me share my screen. Yes. Okay. Let's go to Yeah. Okay. A dinner list. You can see my screen, right?

Khushboo: Yes.

Deepshikha: Yeah.

Yogesh Jaiswal: Okay.

#### 00:42:49

Yogesh Jaiswal: Okay. Where was Yeah. Phoenix. Okay. Can you see this? What is this? All Phoenix. Okay. And you will you will also see that how I have presented the data. City, state and country separated. This is how data clarity is required when it comes to GTM engineering. you know even though Phoenix comes under Arizona but I have added a state column like you can see the kind of clarity I give to the client right and there are several uh nearby areas like Scottdale Glendale which are also a part of Phoenix but they are under Arizona okay so the client will not check out the cities okay the client will check out the state okay even if it's a bit wrong but the state is Arizona right now let's go back here and if you can see these are all the credit I mean this was credit officer servicing officers right can you see the numbers only 334 okay now this was a this was a company level s uh people first search right we have all of these people now what we do we have our own TAM also okay we we have set of companies that we want to reach out so when we only pick out pick up the companies that we want to reach out to that is within our tab we only have 114 people

#### 00:44:38

Deepshikha: Um, Yogesh I didn't get it. What do we mean by within time? This

Yogesh Jaiswal: okay I go to Prospio I get a requirement that reach out to build a list of all of the castle personas in Phoenix. Okay, for dinner. If you see the name of the list, castle Phoenix, in a list. Okay. Now, what I do, I go to Prospio, I type all of the personas, lending, lending, servicing. Okay. These are the personas of Carcel. And at a C- level, VP level, then I get all of these are all of the people that I got. This is everything. But my company is also surren total addressable market. Right? In this set of companies, I have removed and separated the companies which are within my total addressable market. So this is global data and this is within my data within my time. This is done by claude. Oh now do do you understand okay so can you see

Deepshikha: Yeah.

Yogesh Jaiswal: the see okay let's separate the time within time information but if you see as a client can you see the details I give maybe any good detail manager can give you give all of the people that are there in Phoenix and these are under a tab but I feel that if you get him complete details he can also leave this part okay leave the time Let's let's call most of these people for dinner, right?

#### 00:46:14

Yogesh Jaiswal: And also when you build a list, you need to be very clear of the columns you create. Okay, let me remove everything for you to get an idea. Okay, the first columns are always and we will do this before moving to clay by the way. Okay, you download data from Prospio. Then you come to Google sheet and then you will organize first name, last name, full name, clean first name. Okay, in US there is a big problem, right? I mean the clean first name means we use email as placeholders. Okay, I'll show you something. I first name. Okay, because we use it as placeholders, it should be high deep, right? It cannot be high. Okay, but in America if you see the names and I can even give you an example. Uh yeah, can you see this? How can I write high Hi? I mean it's not right. Correct. Okay. So we would do this high A too much.

#### 00:47:34

Yogesh Jaiswal: Okay. Or maybe if it's L, we can do L also. Okay. And you might have Okay, we don't have I think I've cleaned this list. Okay. You can even see this. height there cannot be height ty Right. Okay. So these are the clean names. Okay. Clean first name column is always the column which contains first name as single word. Okay. Single word. Okay. But with the first letter should be capital. First name then last name. Full name columns. Again full name columns are must because we would when we go to play uh full names are required to do the enrichment. Job title all the LinkedIn URL then clean company name. Okay. Cleaned company name should be only a company name which we can use as placeholders. Okay. So let's say I high company name. Okay. So I cannot write high stage bank of India mobile branch right this will not look good in the email then I write hi SPI okay so if you have these kind of uh words here you need to clean it okay and again I'll teach you how you can do this in plot but this should be SBI Okay.

#### 00:49:17

Yogesh Jaiswal: Okay. This is how you clean the company names. Okay. Then you have company domain in every people first. Again I'll keep as a note. Every people first list should have in the location should have city, state, country column separated. Okay. Uh this should be always mandatory for people first list. I mean when you do this for any company out there they would get amazed because this is like a very top-notch data hygiene. Okay. This should be separated. Okay. And this is the email part which we are going to learn later. Okay. So this was the Phoenix dinner list. But if I show you more list uh okay you can see this okay so these are chief operating officers of 10,000 plus companies okay US companies right so all of the chief operating officers okay and 1218 company 1218 people if I want to check unique companies I also have one idea I just go here and you can see I have 437 unique companies.

#### 00:50:48

Yogesh Jaiswal: Okay. Also one more thing I want to mention that uh before clay try to also become better in Google sheets. If I only want to find people who have operating officer in this list so that I remove the nonrelevant people. I just go here text contains operating. Okay. So now I have yeah I think I've already cleaned it but you might have people who are not having this word called operating. Okay. you need to remove it. Okay, got it. So, yeah, this was the data landscape list. Uh, yes. So, now have you got an idea that when it comes to a list build, how would you go about it? Right. So, uh, Maida, if I if I ask you to build a list from a client perspective, what are the steps you will follow? or anyone who would like to answer like Deep Shika or Gagan anything like now you have a requirement of building a list before even building the list what steps you will follow.

#### 00:52:11

Deepshikha: Uh first of all I'll uh get clear with that who am I building this list for and uh also

Yogesh Jaiswal: Mhm.

Deepshikha: checking where are my notes let me

Gagan Bhaisa: Yeah, before that I will check Y.

Yogesh Jaiswal: Yes.

Deepshikha: yeah and I would also check like let's say if it's an event or something uh inerson event or something I would get clarity on the data uh location wise uh where the company is located or the

Yogesh Jaiswal: Huh?

Deepshikha: people what all areas do we want to target so I would be like clear on the location as well

Yogesh Jaiswal: Okay. Cool.

Deepshikha: and also if uh this is a fresh reach out or we have already done it previously Then utilizing uh the list available.

Yogesh Jaiswal: Yes.

Deepshikha: Clean that up.

Yogesh Jaiswal: Yes.

Deepshikha: Yeah.

Yogesh Jaiswal: Also one more thing I want to mention that this is a note equal first list always contains a sales nav export. Okay. Sales nav export means when you create a people first list you need to always use sales navigator. This is mandatory if you want to have a good list.

#### 00:53:43

Yogesh Jaiswal: anything. Find people in New York, find people in Philadelphia, find people in Bangalore, find people any city, any country. Sales navigator is a must because can you can you tell me a reason why sales navigator is a must for people first test.

Alok: because it has LinkedIn data.

Yogesh Jaiswal: Yes, but uh that's like a very general answer. But apart from that like how Prospio and Apollo have like are not important but sales navigator is important for a people first list.

Gagan Bhaisa: because you get a I would say not 100% but at least 92% correct data and you could able to figure out like which company I mean individual

Yogesh Jaiswal: Okay.

Gagan Bhaisa: works for

Yogesh Jaiswal: Yes. Uh okay. I want to give you an example. Uh Gagan, tomorrow if you move to New York, what's the first thing you do?

Gagan Bhaisa: I would want my location to New York.

Yogesh Jaiswal: Where in LinkedIn? Right.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: And do you know from where Apollo and Crossview get the data?

Gagan Bhaisa: So I mean it's LinkedIn uh but again they scrap a lot of data

#### 00:55:03

Yogesh Jaiswal: Yes.

Gagan Bhaisa: uh

Yogesh Jaiswal: So you would change your location to New York when you move tomorrow instantly. Hardly it will take 5 minutes, right? But you know Apollo and Prosper will take 30 days for that information to process. So there is a huge gap here and many people who don't use a sales navigator um their list are never of good quality and they have always this problem that you know the client doesn't like the work or uh you know we doesn't like the work or something like that. So always sales navigator is a must for a people first list. Okay, that's why because any person in anywhere in the city they would update their LinkedIn first. Okay, and by the way in US there are a lot of movements occur people move from different cities to different cities. It's very common there even it's in India like people move from Hyderabad to Bangalore, Bangalore to Mumbai, Mumbai to Pune. So this should be a must that you know people first list should always contain sales target.

#### 00:56:08

Yogesh Jaiswal: right now a company.

Gagan Bhaisa: Uh yogis I have a question here.

Yogesh Jaiswal: Yep. Yes. Yes.

Gagan Bhaisa: Uh I have seen lot of people uh not putting their base location putting

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: the company base location. No company based location as their location. Let's say I'm still in India.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: I would put that as a US work for US and then my location is US. How do you fight on all those things?

Yogesh Jaiswal: Uh honestly like Like honestly this is a

Gagan Bhaisa: Yes.

Yogesh Jaiswal: problem uh and uh even I have indulged into this problem and we cannot do anything about it like this is what I believe because uh okay if you feel

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: okay there is a there is a way out let's say if I want to find all of the CEOs of YC companies Is this in US then I need to understand that CEOs would be everywhere in the world but they would mention the location is US right very easily now how many YC CEOs are there in in

#### 00:57:10

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: in US like let's say specific batch 800 900,000 CEOs so for these kind of list I would not have a problem but let's say now you say I have to find all of the product managers in US right Now I need to be very careful that I need to go here and also select the company location as US. This would eliminate the people who are not from uh US. Right? If the company is in US, the people is in US. More probabilities the people are in US. Right.

Gagan Bhaisa: But then other way you are losing some people who are not in US and be as a seesource.

Yogesh Jaiswal: Yes, that's right. Um I think the way out right now is to understand that any senior person would not fake their uh location right to in today's world. This is only happening with junior roles. So you know when we work in sales like when I remember when I was working in Freshworks we used to mention our LinkedIn location as New York or US or California but you were sitting in Bangalore right but if you see our managers like our managers or our VPs directors their location was always Bangalore okay so there are not a huge pro there is not a huge problem because seuit VP dire these guys will not fake the location sitting in India because they are not selling their

#### 00:58:41

Yogesh Jaiswal: monitoring. So the chances are low but again um I feel I'll get back to you with the right method because I have not done Yeah.

Gagan Bhaisa: No my question is not to get a right answer just to see how approach because uh yesterday I went back

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: to India I was in flight just we had a chat on this with a person and she says like the same problem with everywhere uh you see data sales navigator give you exact data but again there is a lot of problem where people suffers around the countries uh being in the different base location. So let's say taking an example of YC competitor okay there are I've seen a founder from uh I would say Europe uh making their location to India oh sorry making the location to US and then when you try to say that hey I mean we we are somewhere in

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: the s southern I mean uh central of Europe and then uh we we we will be not be able to make it to the event or so but we will happy to catch you up uh when we are in the city or in the states.

#### 00:59:42

Gagan Bhaisa: So yeah, I mean that's what but just to understand how you you just cut down that uh problem of

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: being approachable uh thought process.

Yogesh Jaiswal: No, I think uh that's a genuine problem even I have faced when we do outreach. Honestly, when we do LinkedIn when we do email outreach it's not a very big problem to detect but see

Gagan Bhaisa: Yeah. Yeah.

Yogesh Jaiswal: there there is a way out okay there are scrapers which which can verify if the profile is like in the right country or not but honestly uh like okay just understand if I change my location to US uh just I am the only person who understand that uh is it correct or not but okay there is one more thing when you do outreach to us you do in US times right you do in the night time okay so there are less chances of like uh Indians responding to it or other countries responding to it because they're not even in the same time zone lot of other things um you know there are other ways out that the landing page will not open in other countries so if there's a book of book to meeting uh landing page you can block the landing page to open from for other countries there are a lot of other ways out but uh right now that this is a problem but this is not a very big like only 5% of people would be these false people and uh you don't need to worry about

#### 01:01:06

Yogesh Jaiswal: it but again I feel that this should be worked out

Gagan Bhaisa: Mhm. Yeah. Got you.

Yogesh Jaiswal: okay cool so yes um yeah so now we are clear with sales navigator is a must um also this is a very common thing in GTM engineering but in GTM engineering you can never rely on one data source or let's say single data source. Okay, I can never I can never do this. You can never go to prosp and say okay this is what I got right. You should always use real or more. Okay. Now this will give you an understanding that and you might be shocked that it's very easy to understand why agencies are more rather than individual comp like rather companies hiring individually for a GTM engineer. Okay. So when I say that GTM engineer never relies on a single data source. We need three or more data sources. Okay. A company would not invest in three three data plans for a GTM engineer right that's why agencies are winning in the market right now okay if you work with an agency you might find agency have 8 to 10 data tools okay and you don't need to um you don't need to like uh when you work with a company company don't need to worry about okay I need to get this this tool that tool right so In GTM engineering always three or more data providers should be used.

#### 01:02:49

Yogesh Jaiswal: Okay. So everything is clear with this. Okay. Um any questions in all of the things we have discussed? Okay, got it. I just want to give you a basic lookout because again uh most of the things that we do in prospin Apollo you can control in Lord by a prompt. Okay, you would not even be coming here and like typing all of these things, right? So you have people filters. Okay, you have job title which is a simple job title. Okay, job title and you will find a thing called department. Right now this is again a mistake where um people make and I really wanted to give a very easy trick. You know if you want to find a very small department like let's say I want to find all of the AI related uh people in Bangalore. Okay, it's very easy. There is a department called artificial intelligence. Okay. I select the location as Bangalore. Okay. Now I only want to find chief people.

#### 01:04:20

Yogesh Jaiswal: Okay. or let's say even VPs. So can you see how easy it was? I just selected the department. I have not not selected any job title only the department and these are all of the AI people. Okay. AI AI AI AI. Okay. Now let's say I want to find product marketing. Okay. Product marketing. Let's remove engineering. Can you see? So easy. And if I have less people, I can even have a good view. Head, director. Okay. So also when you get a very specific kind of persona, you can even search here in the departments. Okay. But because if you search here, you need to add a lot of filters. You need to add product marketing, product marketing, lot of other things. Okay. So this is department. You have also exclude department. Okay. So let's say if you're finding product marketing, if you don't want advertising, you can just push exclude.

#### 01:05:34

Yogesh Jaiswal: Okay. And uh you have seniority levels. Okay. I just want to ask you a question that do you think do you think director should be above head or head should be below director like something where uh do you think director should be below VP and Then, Head should be below director because in Apollo it's not like that if you have Apollo and if you go into the seniority level you will find director here and head here. Okay. So just just want to let you know that head is a senior person senior seniority than director but in apollo head is below director okay so don't get confused in that the top decision maker seniority levels are always director head VP and seuit this would these will these will always be the decision makers very rare cases you have managers okay these are the seniority levels Yes. Yes. Ma

Medha Das: Uh there's just one quick question. Why why are we excluding partners?

Yogesh Jaiswal: like I just want to ask you what do you understand by a partner?

#### 01:06:57

Medha Das: I mean for me he said it's very different since I come from a big background that like uh partners are the people who are usually the decision makers for most of the projects because they are the one who actually bring in the projects and they sign contracts with the clients and they are the ultimate leaders who have a the

Yogesh Jaiswal: Mhm.

Medha Das: major say and then comes the director and then the senior managers and likewise So I'm little confused here like uh I'm confused with the hierarchy that uh you're following

Yogesh Jaiswal: Yes. Yes,

Medha Das: here.

Yogesh Jaiswal: these are very edge cases. Um, uh, honestly like if you see I'm searching all of the chief executive officers in Bangalore, I don't even have a partner here, right? Everyone is a seasuit. Okay, but in some other departments, let's say product is where I might have lot of partners. Okay, let's say suit. Okay, you see partner, right? So see a partner can also be a partner with other companies. These guys are also partner to other companies and this is not a good outreach.

#### 01:08:10

Yogesh Jaiswal: See now partner also contains partnerships. You have talent partner right? So this guy okay parak shival he's a talent partner right but I don't want to reach out to a partner right I want to reach out to a decision maker. These guys will buy my product. So again uh if you are really concerned then click on partner and check this list okay you will understand it better but I would say that you can avoid it and it's not a big headache I mean this can also ruin your sheet let's say you go to partner and uh what if you have a partner you can see the partner enablement right so do you understand product marketing by partner enablement.

Medha Das: All

Yogesh Jaiswal: That means this Mahima Aurora is responsible for channel partners and you are not going to sell to channel partners, right? You are going to sell to a decision maker.

Medha Das: right.

Yogesh Jaiswal: It it it majorly depends on the client you work with. Okay? If they have a lot of people coming in showing up in partner then you can download a list of partner create a Google sheet and share it to the client and you can just ask that okay do you think anyone and you know you have better ways to ask a question.

#### 01:09:33

Medha Das: Okay.

Yogesh Jaiswal: Do you think that from the partner uh seniority we can include more people and make our list better instead of asking should I include or not include.

Medha Das: Okay.

Yogesh Jaiswal: Okay, got it. Now this was seniority. Okay, now you have locations. Always company locations and uh city locations are separated. Now you have contact detail. Uh honestly this is we are going to do this in clay. So not to worry. Select people per company is selecting one company, one person per company, two person per company like that. Business model uh never include this nonprofit. Okay, we cannot sell to a nonprofit company very easily. Okay, then you have uh business models. Then you have again no need for this buying intents or funding. Okay, revenue funding you need to use. Okay, you have fundings. Then yeah, I think this is mostly like not needed. We can do it easily in uh claim. Okay. So yeah one more thing I want to mention that when you export the data from okay I said three data sources right so let's say export from Apollo crosspio and sales now okay you need to follow a process called combine and ded okay now can you explain me what does this name anyone.

#### 01:11:13

Yogesh Jaiswal: So I have three CSV files 1 2 3. So then I follow the first process in data building called combining and edoping.

Gagan Bhaisa: So it's basically merging and having a mean duplication. Uh one person doesn't relies on three of the seats.

Yogesh Jaiswal: Yes, also I am downloading data from three data sources because I want a clear picture. I don't want the rough number that 500 people, 600 people. I want the exact number. Okay, 800 people total then it's right. So combining and reduping is a process that we do to combine list combine data from all data sources and deliver a clean output. Okay, combining and deduping always happens in claude. Okay, this is just for your information that this process will always happen in claude. If you use GPD also in GPT if you use Grog Gemini anything never do this in clay. Uh we need to understand that when the data is clear before clay clay becomes very easy. You can even do this part in clay but clay will make this very complicated.

#### 01:12:43

Yogesh Jaiswal: Yes. Any questions?

Deepshikha: Yeah, uh clay also provide uh data, right? So are these more trusted sources? Uh and that is why we are not utilizing clay or what what is the reason

Yogesh Jaiswal: Yes. Uh okay. Clay provides data. But what is clay exactly? What is clay as a platform?

Deepshikha: enrichment platform.

Gagan Bhaisa: It's a data destination platform.

Yogesh Jaiswal: Yes. Clay is a orchestration platform, right? Clay is not a data platform.

Deepshikha: Yeah.

Yogesh Jaiswal: you know from how long Apollo exist how how long Apollo have how old the company is like Apollo like rough idea

Gagan Bhaisa: I mean beyond I started working is almost more than 10 years.

Yogesh Jaiswal: yes so see I mean you have a person here who's working from 10 years and he said that Apollo was there before he before he started his work so see data is

Deepshikha: Yeah.

Yogesh Jaiswal: just storage of information right uh storage of all of the information that we catch from outside right so no one can beat Apollo in the market because they have every like they are literally um gathering data from decades clay cannot just come in and say okay we do better data than Apollo right that's why now no one can beat Apollo today Apollo exist I can give you a guarantee that after 10 years also Apollo will exist Okay,

#### 01:14:16

Yogesh Jaiswal: Prospio again it's a very old company and they are doing amazing in data, right? So we need to understand that the clay people data is a scrape data. So if tomorrow Deepshika goes on LinkedIn and says I have joined you know this is a very um funny thing but there are companies where you work like you work with for Infosys but the client of Infosys is Google. So you go ahead on on LinkedIn and say okay I worked as a software engineer at Google right that is wrong information on LinkedIn where Dipshika tells that Dipshika works as a software engineer on LinkedIn but that's Deepshika works for Infosys and Infosys client is LinkedIn uh is uh Google right so Clay will give you that data. If you go in Clay and if you search Google software engineer India Clay will give you Dshika but Apollo prosp will not give you that. Okay, that's why we need to be super clear that Apollo and Prospe are the data validation provider also, right? And Gagan, I feel you might have a question that if still we do a sales nav export, if we still get the set of people which are uh irrelevant, we would have one more check called email ID check, right?

#### 01:15:41

Yogesh Jaiswal: So if Deepshika never worked in Google, she would never have a LinkedIn URL of Google and we can flag that person then and there itself.

Gagan Bhaisa: Uh, you guys, can you just go back to the last part you said for two? 2 seconds.

Yogesh Jaiswal: Okay, I said that Deepshika works for Infosys and the client of Infosys is Google,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: right?

Gagan Bhaisa: Okay.

Yogesh Jaiswal: And Deepshika is a senior software engineer in Bangalore. Now you are selling something to senior software engineers in Bangalore and Google is in your

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: TAM, right?

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: You go download data from Apollo, Prosp and Sales Navigator.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Now Polo and Prospec might not have DPSika because she's invalid right

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: they can detect it they do a data refreshing cleaning everything but sales navigator would have dipsshika because dipshika is working in infosys but she's showing on

Gagan Bhaisa: Yes.

Yogesh Jaiswal: uh LinkedIn that she works in Google now sales navigator might give you the data and that data might pop up in a your clean output list but when you further process the list for enrichment Deep Shika's email will come as a Infosys email.

#### 01:16:47

Gagan Bhaisa: Mhm. Yes.

Yogesh Jaiswal: You got it?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: And when it pops up as a Infosys email, we do a thing in GTM engineering called QA, right?

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: And in QA, we set up and we would learn everything. We have we have to set up a skill in claude. QA parameter tells that if the company name the company name and the email id of the person should be should be matched. So the company name is google.com and the person's email id is infosys.com right dipsadinfosys. So that would be flagged in the end that it's a false profile.

Gagan Bhaisa: got you.

Yogesh Jaiswal: Okay. So these are the steps and by the way in today's era these steps are mandatory because everyone is doing that. Most of the people you see online who works in Meta, Google from India, they're not working with them. They're working for Infosys TCS. But everyone is showing on uh LinkedIn that they work for these companies or maybe even Nvidia. This is a major problem for Qualcomm also I think 40 to 30 to 40% of Qualcomm staff in India is on uh this agent with contractors but all of the people on LinkedIn say that they work in Qualcomm right so we can flag that in the in clot itself okay now combining reduping happens in clot code it's a very simple prompt combine and redoup the list and keep all

#### 01:18:29

Yogesh Jaiswal: the keep the best available work image in one email column. Okay. uh do you understand why I gave this prompt this this prompt and we would do tomorrow and claude everything how we do combining and reduping but before that I want to ask do you know why I've given this prompt okay I've given this promp because Apollo also deliver personal emails if you download data from Apollo. You might see Apollo also have personal email column and work email column. Prosper will only give you work email but Apollo will also give you personal email. So if I'm reaching out to GAN, I cannot reach out to GAN@gmail.com. Right? It's it's not right to reach out someone on a personal email. So in all GTM engineering task, we need a work email. Okay? But Apollo might have a different work email. Pro might have a different work email. So we need we need one work email, right? So clude will automatically detect that keep the best available work email one email column and combine and duping parameters are also different.

#### 01:19:48

Yogesh Jaiswal: Okay. Did you start from LinkedIn URL then it moves to email id then it moves to full name plus company name. Okay. These are three parameters of du. If you have a list of um 10,000 people or 4,000 5,000 people, you need to ded from LinkedIn URL then email ID and then full name plus company name. That's why uh whoever told Clay also have a dedup thing. Clay can only ded from a LinkedIn URL point of view and email ID point of you cannot ded from a full name. Okay. Uh never did from full name alone. There can be James Bond like there can be people with same names in US it's very common and you might lose out the uh real ones. Okay. So tomorrow we are going to do a list build for the client company you have. We would go to the tools, download the data, reduce the data. create a clean list and that list will move to clay. Okay, got any questions?

#### 01:21:08

Yogesh Jaiswal: Anything? Yes.

Deepshikha: Yogesh I could not um join that Thursday class so I was going through the recording. So I do have question two questions from there. Shall I?

Yogesh Jaiswal: Yeah, please. No, no problem.

Deepshikha: Yeah. Yeah. So uh Thursday class was related to time sams.

Yogesh Jaiswal: Yes.

Deepshikha: So what I understood from s is that we can only like come to uh get that data only after we go live right once we do experimentation in the market.

Yogesh Jaiswal: Yes. That's why we cannot do a som filtration. Uh s are just parameters that you learn. Let you understand.

Deepshikha: Yeah.

Yogesh Jaiswal: Yes.

Deepshikha: Yeah. Okay. So, we start with TAM Sam and then only when we go live we do experiments and then we get to know and

Yogesh Jaiswal: Yes.

Deepshikha: then we Yeah.

Yogesh Jaiswal: Yes. Yes.

Deepshikha: And then you also mentioned like uh the outreach tools and uh we would be combining them. You mentioned hair reach trigg buffer. So I was wondering uh for the blue do we always end up using NA10 or is like to build pipeline?

#### 01:22:21

Yogesh Jaiswal: No. N.

Deepshikha: Is that how

Yogesh Jaiswal: Yeah. Net 10 would be a complete whole separate thing. Net 10 is only used for uh enterprises.

Deepshikha: Okay.

Yogesh Jaiswal: Yeah. See N is building and automation. Small companies already have technical people. They would just build themselves. They would not need a TTM user for that. Okay. N would be only required when you work with a good company where they have lot of money and a big team. They don't want to spend time on doing this small task. So they would get a consultant or a GTM engineer. Okay.

Deepshikha: Yeah. Okay.

Yogesh Jaiswal: All right. So uh perfect. Um I think this is it for data the data layer. Again if you see we don't need to go too much in sales. See I just want to sum up this. Um whenever you get a list build requirement just understand why we are building. Are we doing for email outreach, LinkedIn outreach?

#### 01:23:20

Yogesh Jaiswal: Why are we even building it? The reason you understand why we are building then follow the approach company first or people first. If it's people first, use sales navigator. If it's not people first, totally fine. Always use three data providers. If not three, at least two, not one. Okay? Then try to start building the list and give the clarity to the client. You might have Slack channels. go to the client and say that okay you said to do a build a list for New York New York only has 76 chief lending officers that's not right I want you to build a list for entire US okay so get back to to the client with clarity. Then the client will tell okay uh Dshika reach out to the 1286 CLOS's in entire US. Let's book a meeting with them. Okay. Then you download the data from Prospio Apollo and then you go here and you combine and redo it. Okay. You might get 1500 unique people.

#### 01:24:17

Yogesh Jaiswal: Okay. Tomorrow I'm going to show you how you can build a uh complete list like before moving to clay how you can build it. Okay, got it. Uh, yes.

Deepshikha: Yeah, Yogesh. One more question.

Yogesh Jaiswal: Yes.

Deepshikha: In one of the classes you mentioned about our B2B's uh limitation, I think related to US market. I could not understand that.

Yogesh Jaiswal: Yes.

Deepshikha: What does that mean?

Yogesh Jaiswal: Yes. RB2B. Okay. We are going to learn all of the tools uh in the coming uh days. But again, we we have started the discussion and that's totally fine. uh RB2B find personal person level visitors that is only allowed in US. So if you want to find any person visits your website that is only possible in US right now because in Europe there are compliances

Deepshikha: Okay.

Yogesh Jaiswal: okay so that's only possible in US okay and uh yeah we are going to also uh use RB2B and we are going to do everything in the coming days. So at this point I really want you to understand that GTM engineering is not complicated.

#### 01:25:31

Yogesh Jaiswal: Uh data build list building is also very easy. You just need to understand the reason why we are building the list. Many people I have I mean I have seen it live. They don't even ask the client why we are building the list. They would say they want to build this. they would just start building it and they would come back to them after a day that okay I've built this list and then it's completely wrong. So you can ask lot of questions before even building the list but you need to understand that the the list is the main foundation of everything that you do. Okay, got it. There are more ways to it. when you uh when you say that when the clients are we have already reached out then you need to get that data the data might be in a Google sheet the data might be in their CRM so you need to use cloud you need to use some APIs uh different ways but that is also we are going to cover in the future okay cool guys if you have any questions I would happy to answer in the WhatsApp group or you can give me a call after that I don't have any Okay, cool guys. I think this is it. Uh yeah, hope you have a nice day.

Medha Das: I'm

Yogesh Jaiswal: was if I rised in Yes.

Deepshikha: Thanks everyone. Bye-bye. Have a good day.

Sampath Hari GTM: Thank you. Bye.

Yogesh Jaiswal: Yes.

#### Transcription ended after 01:39:42

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.