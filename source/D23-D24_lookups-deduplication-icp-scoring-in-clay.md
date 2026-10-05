# D23+D24_ Lookups & deduplication + ICP scoring in Clay - 2026_09_23 08_59 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D23+D24: Lookups & deduplication + ICP scoring in Clay

Sep 23, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Outbound messaging and data management strategies via Clay and Claude optimization.

Cold outbound messaging and regional strategy

Yogesh recommended keeping cold messages warm, straightforward, and focused on personal case studies.

European markets experience lower cold email volumes, resulting in higher prospect engagement rates.

Region-specific outreach utilizing local native languages significantly improves international campaign responses.

Clay lookup operations and blacklist management

Single and multiple record lookups prevent duplicate data enrichment across team workbooks.

Permanent blacklists exclude direct competitors and companies building identical products from outbound campaigns.

Exclusion lists temporarily restrict outreach to active clients and ongoing CRM deals.

Data deduplication workflows in Claude

Claude efficiently combines and deduplicates jumbled export files to reduce data processing costs.

Deduplication processes evaluate LinkedIn URLs, emails, and combined full names with company names.

Lead filtering and search optimization in Clay

Similar job title filters yield up to 60% greater lead coverage than rigid contains filters.

International searches require localized job titles and language filters to capture accurate prospect pools.

Lead profiles require minimum audience sizes of 100 followers and tenure thresholds of 6 to 12 months.

Sculptor operates as a dedicated AI agent within Clay to answer custom analytical queries.

Founder data validation scope

Sampath outlined the startup founder dataset containing names, company names, and email addresses.

Clay platform capabilities and live tables

Yogesh explained that Sculptor processes table queries to accurately retrieve missing data.

Yogesh introduced live tables operating via APIs in the background without opening Clay.

Portfolio content objectives

Yogesh established the goal to perfect the Clay table this week for an upcoming portfolio video.

Next steps

[Yogesh Jaiswal] Send messaging documents: Send the previously created messaging documents to Gagan for review.

[The group] Create delivery sheets: Develop a high-quality client delivery sheet for 50 companies using Clay. Perform signal processing, establish qualification parameters, identify individuals, and enrich the lead data.

[Gagan Bhaisa] Map Strategy: Align the strategy document with the 50 companies listed in the database.

[Gagan Bhaisa] Refine Clay Table: Verify that signals are accurate and included profiles contain valid LinkedIn email addresses.

[sampath vemulapati] Extract LinkedIn URLs: Execute a prompt to map full names, job titles, and company information to retrieve missing identifiers.

[sampath vemulapati] Enrich Profile Data: Run an enrichment process to confirm the current employment status of founders on the list.

[Gagan Bhaisa, sampath vemulapati] Finalize Project: Meet tomorrow to ship the sheet and complete last-minute adjustments.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 23, 2026

### D23+D24: Lookups & deduplication + ICP scoring in Clay

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D23+D24: Lookups & deduplication + ICP scoring in Clay

Meeting records Transcript Recording

#### Summary

Outbound messaging and data management strategies via Clay and Claude optimization.

Outbound Messaging Strategy
Target existing connections using straightforward messaging. Incorporate personal details.

Data Management in Clay
Utilize single-record and multiple-row lookups. Implement blacklists to exclude competitors.

Dataset Deduplication
Upload comma-separated value files into Claude to clean data. Refine tables and qualification parameters.

#### Next steps

[Yogesh Jaiswal] Send messaging documents: Send the previously created messaging documents to Gagan for review.

[The group] Create delivery sheets: Develop a high-quality client delivery sheet for 50 companies using Clay. Perform signal processing, establish qualification parameters, identify individuals, and enrich the lead data.

[Gagan Bhaisa] Map Strategy: Align the strategy document with the 50 companies listed in the database.

[Gagan Bhaisa] Refine Clay Table: Verify that signals are accurate and included profiles contain valid LinkedIn email addresses.

[sampath vemulapati] Extract LinkedIn URLs: Execute a prompt to map full names, job titles, and company information to retrieve missing identifiers.

[sampath vemulapati] Enrich Profile Data: Run an enrichment process to confirm the current employment status of founders on the list.

[Gagan Bhaisa, sampath vemulapati] Finalize Project: Meet tomorrow to ship the sheet and complete last-minute adjustments.

#### Details

Cold Outbound Messaging Strategy: Yogesh Jaiswal explained that cold outbound messaging must remain warm and straightforward, targeting existing LinkedIn connections, ex-colleagues, or website visitors (00:00:02). Yogesh Jaiswal noted that overly complex messages lead to low response rates, and advised incorporating case studies or personal details into communications (00:01:48). Additionally, Yogesh Jaiswal pointed out that targeting international markets like the Netherlands using local languages (such as Dutch) yields better engagement because prospects receive fewer cold messages (00:03:19). Gagan Bhaisa requested sample documentation, and Yogesh Jaiswal agreed to share messaging documents offline (00:01:48) (00:04:37).

Single-Record Lookups in Clay: Yogesh Jaiswal guided Gagan Bhaisa on using single-record lookups in Clay to streamline data management when multiple people work on the same company dataset (00:06:09). Gagan Bhaisa shared their screen to demonstrate running artificial intelligence enrichments for company headquarters on a new table and mapping those records back to the primary table using single-record lookups. Yogesh Jaiswal explained that this technique helps sales teams identify additional contacts within a company without needing to open HubSpot (00:08:01) (00:13:24).

Multiple-Record Lookups and Company Blacklists: Yogesh Jaiswal demonstrated multiple-row lookups in Clay to efficiently calculate the number of people associated with specific companies across large datasets without burning Claude credits (00:15:46). Yogesh Jaiswal introduced the concept of a "blacklist," explaining that companies must permanently exclude competitors (such as Razorpay and PhonePe) from outreach to avoid public relations issues on LinkedIn. Gagan Bhaisa and sampath vemulapati noted they were previously familiar with do-not-contact lists (00:18:48) (00:22:39).

Blacklists Versus Exclusion Lists: Yogesh Jaiswal clarified the operational differences between permanent blacklists and temporary exclusion lists, noting that exclusion lists contain current clients or active deals tracked in HubSpot (00:21:27). sampath vemulapati and Gagan Bhaisa discussed how reaching out to active clients or prospects with ongoing deals damages professional relationships (00:22:39). Yogesh Jaiswal emphasized that agencies frequently lose clients by mistakenly contacting blacklisted competitors (00:25:30).

Dataset Deduplication Using Claude: Yogesh Jaiswal instructed Gagan Bhaisa to export comma-separated value files from Clay and upload them into Claude to clean and deduplicate jumbled data from tools like Apollo and Prospio (00:25:30) (00:31:21). Yogesh Jaiswal provided a specific prompt logic using three parameters: LinkedIn Uniform Resource Locators as the primary filter, email addresses as the second, and a combination of full name and company name as the third (00:32:40). sampath vemulapati and Gagan Bhaisa acknowledged the data organization benefits, and Yogesh Jaiswal noted that leveraging Claude helps reduce reliance on expensive Clay features (00:31:21) (00:34:48).

Refining Clay Tables and Qualification Parameters: Yogesh Jaiswal advised participants to maintain clean and organized Clay tables for client deliveries, warning against overly strict qualification parameters that improperly disqualify up to 60 to 70 percent of leads (00:35:55). sampath vemulapati asked about lead dropouts encountered when downloading data from Prospio, and Yogesh Jaiswal recommended performing initial filtering directly inside Prospio rather than relying excessively on Clay (00:39:36). Furthermore, Yogesh Jaiswal demonstrated that using the "similar to" job title filter yields significantly broader results (such as 99 leads) compared to the rigid "contains" filter (00:38:14) (00:42:56).

Advanced Filtering by Language, Region, and Network Reach: Yogesh Jaiswal explained that when targeting international markets like Germany or Spain, Go-To-Market engineers must search using local language keywords (such as German or Spanish terms for founder) rather than English exclusively (00:46:01). Yogesh Jaiswal also highlighted Clay's language filter, demonstrating how to identify speakers of specific languages (like German or Telugu) to add personalized postscript notes in outreach messages (00:47:26). Additionally, Yogesh Jaiswal reviewed network metrics, instructing participants to set minimum audience sizes for LinkedIn connections and followers above 100 to filter out junk profiles (00:50:37).

Role Tenure Requirements and LinkedIn Uniform Resource Locator Enrichment: Yogesh Jaiswal and Gagan Bhaisa discussed filtering leads by the length of time spent in their current role, debating whether a 12-month or 6-month threshold is best to ensure prospects have purchasing authority (00:52:00) (00:54:31). sampath vemulapati asked how to find company details for contacts when email addresses are available but LinkedIn Uniform Resource Locators are missing (00:55:55). Yogesh Jaiswal explained that Clay requires LinkedIn Uniform Resource Locators for people-based enrichments, instructed sampath vemulapati to run a Clay prompt finding the Uniform Resource Locator using full name, job title, and company name, and briefly introduced "Sculptor" as Clay's built-in artificial intelligence agent for answering user queries (00:57:00).

Validating Startup Founders Data: sampath vemulapati explains that they have a list of startup founders and want to validate whether these individuals are still part of their respective companies. Gagan Bhaisa asks what data is available, and sampath vemulapati responds that they possess the founder name, company name, number of employees, and email identifiers (00:58:46). Yogesh Jaiswal notes that finding LinkedIn URLs will make the process work and explains that sculptor is necessary because it views the table before answering (01:00:31).

Clay Table Goals and Live Tables Overview: Yogesh Jaiswal sets a goal to make the Clay table look perfect by tomorrow or within the week so that they can create a long video portfolio for outreach. Yogesh Jaiswal introduces live tables, explaining that these operate in the background using application programming interfaces without requiring users to open Clay directly. Lastly, Yogesh Jaiswal arranges a connection for the following day to review the shipping of the table and make any last-minute modifications (01:00:31).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 23, 2026

### D23+D24: Lookups & deduplication + ICP scoring in Clay - Transcript

#### 00:00:02

Yogesh Jaiswal: Hey, good morning again.

Gagan Bhaisa: Hey, morning. Hey, I mean circling back to the yesterday what I asked uh about

Yogesh Jaiswal: Yes.

Gagan Bhaisa: the market message fit.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Okay. How does really works for you? I mean what sequence actually working for you when you try to reach out someone you whom you don't know and what is the multi channel that you are trying to reach out.

Yogesh Jaiswal: So for messaging we try to keep it very uh warm. I mean even though it's cold outbound but we keep it very warm right? uh let's say when we reach out we reach out to people who are in our LinkedIn connections or done some activity on LinkedIn or um

Gagan Bhaisa: Okay.

Yogesh Jaiswal: maybe ex-colagues ex company colleagues or maybe um

Gagan Bhaisa: Okay.

Yogesh Jaiswal: website visitors when we reach out completely cold that's when it's uh it's very different I mean we need to keep it messaging very straightforward like the reason we are reaching out to uh and

Gagan Bhaisa: Okay.

Yogesh Jaiswal: uh yeah the reason we are reaching out to and

#### 00:01:48

Gagan Bhaisa: Mhm. Got it.

Yogesh Jaiswal: what's the purpose we we cannot like confuse them with a long

Gagan Bhaisa: Got it. Mhm.

Yogesh Jaiswal: message that's the thing

Gagan Bhaisa: Got it. Do you have a sample? Can you just help me one? Any sample?

Yogesh Jaiswal: maybe I can send you some documents that I've created the messaging docs and

Gagan Bhaisa: Okay.

Yogesh Jaiswal: uh then you can have a look into Good. Honestly, I think we need to keep it very simple.

Gagan Bhaisa: Mhm. Yeah.

Yogesh Jaiswal: I think this this is what I feel the more I think if you keep the messaging complicated, no one will respond to it.

Gagan Bhaisa: Yes, that that's uh solid point.

Yogesh Jaiswal: And we need to also understand the infrastructure that u if you send on email email infrastructure if you send on LinkedIn which LinkedIn account you are using so everything plays a very important role

Gagan Bhaisa: Yes. Mhm.

Yogesh Jaiswal: things.

Gagan Bhaisa: Yeah, I think that that makes uh sense and also very helpful. Yesterday I was going through some document uh I mean we're trying to create some message for like our I mean a brand partnership client.

#### 00:03:19

Gagan Bhaisa: So yes.

Yogesh Jaiswal: Mhm. So I feel that try to implement more of these uh case studies that you have proof that you have see if tomorrow I get an email

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: uh let's say if I become a founder and 10 years down the line if someone sends me an email that um I still remember when you were teaching GTM engineering something like very personal so I would open and respond so it's all you need to like build an emotion into a message. I mean if uh I think someone should connect to it

Gagan Bhaisa: Got it.

Yogesh Jaiswal: and it's also becomes very easy when you work with international clients. So I'll tell you some of the European clients they don't have problem with messaging because no one is sending cold messages to their prospects.

Gagan Bhaisa: Mhm. Got you.

Yogesh Jaiswal: So if you are doing cold outbound in uh

Gagan Bhaisa: Uh.

Yogesh Jaiswal: Netherlands,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: so no one is doing that, right? No one is reaching out to people in Netherlands in Dutch language.

#### 00:04:37

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: So I think if you try to get more uh uh region wise like more

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: specific it it's it becomes easy.

Gagan Bhaisa: Yeah. Yeah. No, I think that that's what bringing. Okay. So, uh like the main point is how does the market fit actually uh works on? So, yeah.

Yogesh Jaiswal: Yep. Uh yes I think we can discuss this maybe we can discuss this on some documents and maybe this that will give you some idea.

Gagan Bhaisa: Yeah, sure. Sure. I mean, we we can take this offline.

Yogesh Jaiswal: Yep. Uh hi Sat how are you?

sampath vemulapati: Hi. Hi. How are you?

Yogesh Jaiswal: We are good. Uh, okay. Just one minute. I think I'll just check something. Okay, cool. Uh, yes. Uh Gagan, can you share your screen if possible like to play?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay. By the way, have you done lookups earlier?

#### 00:06:09

Gagan Bhaisa: I have uh not really in I mean okay let me show my screen. Yeah. So I think this is where I left.

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: Uh yeah.

Yogesh Jaiswal: Email. Okay. Uh I think we can do that. That's not a problem. Can you uh go to the first Can you go to the company table?

Gagan Bhaisa: Okay. Yeah.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: Just let me remove the filter here. The filter.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay. Now, this is a very interesting thing I'm going to show you which is called lookup. Okay. Now, the main purpose of lookup is see in GTM engineering many people will work on the same data. Okay. Like we all four can work on a one single company, right? And I want your data which you have and we all work on one claim. Okay. So um yeah, can you copy the companies? Yeah. No, no, the companies.

#### 00:08:01

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: Oh,

Yogesh Jaiswal: Just drag.

Gagan Bhaisa: you mean?

Yogesh Jaiswal: Yeah. Yeah. Yes. Yes. Copy this. No, no.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Only the companies. The company names. Yes. Drag it. Yeah. Copy 10. Yes. copy and paste it into a new workbook. No, no, here only add.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Go to add.

Gagan Bhaisa: Oh, you new sheep.

Yogesh Jaiswal: Yeah, blank sheet. Hm. Then um enrich domain. Yeah. Find the domain for them or or just very easy just run the enrichment. Uh yeah.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yeah. On this table and just run an enlistment at where their company headquarter is on the new table.

Gagan Bhaisa: Okay. Um

Yogesh Jaiswal: On the new table. Yes. Yeah. Run enrichment. You can run the AI enrichment. Yeah. Use AI. Yes. Yes. Now turn off auto run.

#### 00:10:41

Yogesh Jaiswal: No, it you cannot turn off now.

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: once it's finished.

Yogesh Jaiswal: Yes, you can turn off. Turn off.

Gagan Bhaisa: Yeah, I think this this needs to be finished then we don't know.

Yogesh Jaiswal: Yes. Yes. Yes.

Gagan Bhaisa: Bear with me. Just got some cold.

Yogesh Jaiswal: Oh, no problem.

Gagan Bhaisa: Yeah. Yeah. We got everything. We got city, we got region, we got country source URL,

Yogesh Jaiswal: Yes.

Gagan Bhaisa: we got Yeah. source name.

Yogesh Jaiswal: Yes. Now go to the first table which you have. Yes. Okay. Now add a column in the last. Yes. And add a column which is lookup single records. Yeah. Single row. Yes. Okay. Now select the table the new one which you have created. Yes. This was the new one.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: H. Now target column is company. Yeah.

#### 00:12:02

Yogesh Jaiswal: New column contains contains is slash. Click slash. Yeah. Select company name. Save and run 50 rows. Okay.

Gagan Bhaisa: got it.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: Oh,

Yogesh Jaiswal: Can you see now?

Gagan Bhaisa: I I I have run this one in uh Vas CRM. I got it now.

Yogesh Jaiswal: Yes. There is one more thing to it. Go to add column. Search. Look up object. No. No. No. Don't type search.

Gagan Bhaisa: Okay,

Yogesh Jaiswal: Yes. Look up object. This is very interesting. Yeah. Click the first one. Yes. Yes. Click it. Okay. This is very interesting. When you Right. So, HubSpot have four type of objects. Click on this. Yes. Yes.

Gagan Bhaisa: No, this will not show up until I add my account.

Yogesh Jaiswal: Oh, okay.

Gagan Bhaisa: Yeah. Yes.

Yogesh Jaiswal: So, maybe I can show you.

#### 00:13:24

Yogesh Jaiswal: Okay. No problem. Okay. So, it have four kind of objects. Um, companies, contacts, deals. Okay. Uh, and one more I don't recall it. But you can map the objects here and do a lookup. So, just imagine when you work as a GTM engineer and there's a sales guy, right? and sales guy said that the company I'm reaching out to uh there are only five people and they are not answering the call right so you can look up that company from clay itself and give him more people okay you can even help them out without even opening up spot

Gagan Bhaisa: Yes.

Yogesh Jaiswal: okay you can close this okay now click on the record found. Yes. Click on record. So, can you see these enrichments you ran on the other table?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: These are the same you ran on the other table. Now,

Gagan Bhaisa: Yes.

Yogesh Jaiswal: it came here. Okay, this is a very easy thing we have done right now where um we have just done lookup on a very one table and one parameter.

#### 00:14:41

Yogesh Jaiswal: Generally lookups are done on multiple parameters and I'll tell you why.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Move.

Yogesh Jaiswal: Now just imagine the custom table you have created is a blacklist. Okay. That means you cannot reach out to those companies. So what you do? You do a lookup and if you find that company you cannot reach out. Got it?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay. Also you can do a blacklist from HubSpot. So if a company have a deal Hubspot that is also a blacklist.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: So when you run Yes.

Gagan Bhaisa: We should call DNC do not contact list.

Yogesh Jaiswal: So uh you can even do that when you create a lookup you go to lookup object in HubSpot and you set up a parameter that if the company is present in HubSpot and if the deal is active then don't reach out. Okay these are two things. So um if you want to output can you you can output like try outputting use AI city.

#### 00:15:46

Yogesh Jaiswal: No no click on record found. Yeah record. Yeah. Try output use AI city. Yes. So once you click now this data was in the other table, right? It came here. Okay. Now this is one method, right? Now go to the

Gagan Bhaisa: Uh, sorry.

Yogesh Jaiswal: go to the custom table again. Yes. Now auto run is off right. Now click on add. Add 10 column rows. No no the rows.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yeah. Click on this. Okay. Copy po. Yes. And paste pandos from 11 to 20. Only po. I don't think this will okay. Work. Okay. Yeah. Go to the main table again. Yes. Now run a lookup called lookup multiple rows. Yes. Now select the same thing. Yes. So this will give you numbers.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Okay.

#### 00:17:37

Yogesh Jaiswal: So this is used. So can you see on Pando it give us 11 records. Okay. So this is also used to the calculation. Um that means we have a people list of 10,000 people right and we have a company list of thousand companies. Now if I give you a task that please check how many people we have in those companies. If you go into claude, you may burn credits, right? So the best way out is to do a formula. So look up multiple records is the way to um do that on a formula basis. So it went to the your sheet and checked there are 11 pandos. Okay. So look up single record is done. Look up multiple record is done. Okay. uh others did you understood sat nir did you understood how it worked?

sampath vemulapati: Yes. Yes. English.

Yogesh Jaiswal: Okay. If I ask you why do you feel we should use both of the things like what do you think even Dagen you can answer it like what do you think the purpose of lookup single and lookup multiple

#### 00:18:48

Gagan Bhaisa: Okay. So single is basically look. So both solve one purpose is basically to make sure you don't have a duplicate and

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: if you have a duplicate you're going to not enrich repeated time not look on the same record multiple times.

Yogesh Jaiswal: Okay. Uh sample

sampath vemulapati: Yeah, I also had a similar uh opinion about it. Yogish, maybe to uh you know cut through the duplicates.

Yogesh Jaiswal: Yes. Do you know this thing called blacklist?

sampath vemulapati: No, I'm not aware.

Yogesh Jaiswal: Okay. See, a company now I give you a good example, right? A company will never reach out to um competition. Okay. So if Razer pay if Razer pay is doing an outreach Razer Pay will never reach out to Phone Pay because it can create some comedy on LinkedIn right that my competitor reached out to me. Okay.

Gagan Bhaisa: Mhm.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So there is a thing called blacklist where you can never reach out to those companies. I mean there is no uh chance to reach out that I mean as if Swiggy cannot reach out to Zomato uh phone pay to cash free or razor pay again in CRM Zoho to hub Hubspot and all.

#### 00:20:13

Yogesh Jaiswal: So every company have a blacklist right and that blacklist might contains hundreds of companies 100 200 companies right now these companies can be competition or these companies can be doing the same thing which we are doing maybe they are building the same thing

sampath vemulapati: Yeah.

Yogesh Jaiswal: okay so we need to be super clear that every time when we complete the table that we built we need to run lookup single and uh Gagan can you go to lookup single and filter it. So I'll show you something. Filter. Yeah.

sampath vemulapati: Heat.

Yogesh Jaiswal: Filter to has no results. Yes. So now you have filtered it.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: That means you have removed the companies which were found. Okay,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: this also helps in removing the blacklist. Just imagine if those 10 companies were from your blacklist list. Okay, so it becomes very easy for you to filter it. I mean you know we were talking about exclusion list, right? Yeah.

sampath vemulapati: Yeah, you in the initial classes also you mentioned about this this blacklisting because it can also be their existing customers.

#### 00:21:27

sampath vemulapati: So the blacklist is something like a uh accumulation of all of these lists or is it like completely like only competitors exclusivity? Uh is is it something like that?

Yogesh Jaiswal: Uh see there are two things okay blacklist and exclusion list okay now I'll give you the differentiation of both of the things blacklist remains permanent

sampath vemulapati: Oh,

Yogesh Jaiswal: so blacklist are companies which are competition competition companies or companies who are going to build in the same way. Okay. U let's say Phone Pay and Razer Pay are always competition, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: They they would never reach out to enter each other. So these are your blacklist. So for Razer Pay every in India are blacklist for outreach. Okay. Now this is blacklist. Now there is a thing called exclusion list. Okay, exclusion list means if Razer Pay have reached out to Snitch,

sampath vemulapati: Heat.

Yogesh Jaiswal: okay, and Snitch responded that I want to buy your plan and later snitch is not buying it, right? But there is a deal ongoing in HubSpot.

#### 00:22:39

sampath vemulapati: Yeah.

Yogesh Jaiswal: So we we cannot reach out to him again that oh hi we we do this with because we already talk to Razer Pay like from two to snitch from two years now. So we do a lookup HubSpot and then we will create an exclusion list. So exclusion list contains current clients and current deals that they are going

sampath vemulapati: Got it.

Yogesh Jaiswal: on.

sampath vemulapati: Understood. Yeah.

Yogesh Jaiswal: See just just imagine if you are uh if sat you are already selling to uh a company right you're already talking to them you are the founder you have created the company and uh out of nowhere after one year suddenly you send one more message that hi uh I do this I do that and you even spoke to the founder properly so that doesn't gives a good

sampath vemulapati: Yeah.

Yogesh Jaiswal: look Okay.

Gagan Bhaisa: I I think we we all were I think neither would agree we we are really wor with do not contactless DNC. I mean blacklist is something new for us but we've been using do not contact list which is comp I mean combination of competitor your uh like somebody who build on the same space or you don't want to reach out to them or like anything listed non-reion yeah uh uh n uh what do you

#### 00:24:04

Neeraj Sujan: Sorry. Can you repeat?

Gagan Bhaisa: I mean as Yogesh was kind of explaining about blacklist I think we were well was about do not contact list like DMC list

Neeraj Sujan: Yeah. Yeah. I'm not sure about this.

Gagan Bhaisa: okay but I think I have gone through the same Okay. Uh never heard about blacklist as a term but always use DNC do not contact list which is combination of companies which are competitor building same space or you don't want to reach out to them. So yeah XY Z.

Yogesh Jaiswal: Yes. See also blacklist remains permanent. I mean you cannot um you cannot reach out to blacklist at all like exclusion list is fine.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: I mean you reach out to a person which you know and uh that's fine like you see I mean if I if I uh create a tool like clay right and if I start selling it to people whom I already know uh and again with a cold message that will not give a good look right I mean you already know these guys so exclusion is fine but who who is working in clay that uh I am doing this I won't do that so we need to be very clear that uh blacklist should never be reached out.

#### 00:25:30

Yogesh Jaiswal: I you you will be shocked that many people lose their clients because they reach out to blacklist many agencies. Okay, cool. So are we clear with lookups? Okay.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay. Now,

Neeraj Sujan: Yes.

Yogesh Jaiswal: uh yes. Now let's talk about dduplication. So anyone of you have clawed right now?

Gagan Bhaisa: You mean a paid version or a free version?

sampath vemulapati: I have

Yogesh Jaiswal: Yes. Any any version would not a problem. Fade free anything was fine. Okay. Now uh yeah go to go to toolmo. Uh Gagango to the toolmo. Yes. Now go to clay.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yeah. Yeah. Now download the Yeah. Clear filters. Yes. Okay. Now download this sheet in CSV tools. Export. Download CSV. Okay. Now download the people sheet also. Hm. Download SCSV. Yes. Now go to claude.

#### 00:27:13

Yogesh Jaiswal: Yes. Now upload these two sheets. Okay. Now, I'm going to give you a prompt, right? Just a second. And uh you need to use that prompt. Okay. It's there in my cloud code. So, I'll just check it. Yes. Combining. Yeah. What's here? Okay. Okay. Where? Okay. Should I give in the WhatsApp group or should I Okay. I just can.

Gagan Bhaisa: Messenger.

Yogesh Jaiswal: Yeah. Meeting. Yes. Yes. Yes. No problem. in the meeting window. H can you clear it like properly? Start from red logic. Yes. Okay. Now just prompt it combine and redoup this file in this exact method. Combine and ddup. Dup actually means like combining files. Yeah, combine and red in this method. Uh yes. Meanwhile you implement can you can you check what is happening?

#### 00:29:11

Yogesh Jaiswal: Uh can you read the prompt and see what is there exactly?

Gagan Bhaisa: Okay, normal matches. Okay. Basically looking into both the sheet. Oh, sure.

Yogesh Jaiswal: Yes. Okay. Now run it.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: I think you stopped sharing

Gagan Bhaisa: No, no. I mean some something kind of interrupted. You see now you see now the

Yogesh Jaiswal: it.

Gagan Bhaisa: screen.

Yogesh Jaiswal: No, no.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Yes. Enter. Yeah. So now claude code is very easy right you are doing everything in cloud in claw code cloud code will access your file folders. So the the feature remains the same the logic. So we are actually combining these two files and dduping it. So the main purpose of this method is whatever kind of information we have when the output comes the output should be clear into our terms right. So right now you have given a jumble data. Okay. Yeah.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Now go to people.

#### 00:31:21

Yogesh Jaiswal: Yes. One more prompt that fill seniority as per the uh job title but that's fine. Go to the right. No in the in the sheet.

Gagan Bhaisa: Yeah, I think it's ending.

Yogesh Jaiswal: Okay. Perfect. Yes. So did you understand the logic of it?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Yes. Uh other sat n do you understood this logic?

sampath vemulapati: Uh no YogeshI could not understand this.

Yogesh Jaiswal: Okay, I'm pasting the prompt in the WhatsApp group also. So this is a method that we use to use jumble data. See you use Apollo, you use Prospio, you use various data tools. Now you use clay, everything that you do is ruining the data quality, right? Because you cannot keep a quality check. So you run a skill called combine and redo which will combine all the files you have and create one single file which can be used to have a look. Okay. And it's also organized. So we use a logic to create that.

#### 00:32:40

Yogesh Jaiswal: Okay.

sampath vemulapati: You mean more of like a data organizing uh kind of thing, right?

Yogesh Jaiswal: Yes. Yes.

sampath vemulapati: Got it.

Yogesh Jaiswal: data organizing and data.

sampath vemulapati: Yeah.

Yogesh Jaiswal: You know what is the meaning of DDUP?

sampath vemulapati: No, no.

Yogesh Jaiswal: Okay. If there are four sat in my file right then I would by mistake reach out to four one people four times one person four times.

sampath vemulapati: Correct. Yeah. Yeah.

Yogesh Jaiswal: So dduping means I would remove the duplicates. Okay.

sampath vemulapati: Right.

Yogesh Jaiswal: Now GTM engineering I cannot remove sad because there can be many sut right.

Gagan Bhaisa: What's that?

sampath vemulapati: Correct.

Yogesh Jaiswal: So the logic I do is first I'll deduke with your LinkedIn URL. Two sampl right. It will it will be no no they will always have different same LinkedIn URL if

sampath vemulapati: Yeah.

Yogesh Jaiswal: it's different then mean these are two different people okay then the second parameter I will use is email so two samp will always have the same email right if

#### 00:33:44

Gagan Bhaisa: Let's

Yogesh Jaiswal: it's if they are same but if they are not same they would have different email now the third logic is a mix of full name plus company name so sat vulapati plus uh let's pick up any company uh razor pay so

Gagan Bhaisa: see.

sampath vemulapati: Yeah,

Yogesh Jaiswal: in razer pay there cannot be two sample right so I will use a combination so

sampath vemulapati: correct.

Yogesh Jaiswal: I use three parameters LinkedIn URL first parameter second emails and third full name plus company name now many people uh can you go to clay if

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: possible yeah so just go to full name yeah full name Yes,

Gagan Bhaisa: perfect.

Yogesh Jaiswal: try dooping it. So in clay also you have an option to doop right but this is a wrong method.

sampath vemulapati: Right. Yeah.

Yogesh Jaiswal: This is the wrong method because there can be five abishek aid in in in the world I mean in in US and because in American names it's very

sampath vemulapati: Yeah.

Yogesh Jaiswal: easy see you can see one Alex is here only so Alex John

#### 00:34:48

sampath vemulapati: Yeah.

Yogesh Jaiswal: Johnson James everyone have so similar names that uh if you try to do a full name did you then you actually remove so many

sampath vemulapati: Got it. Yeah.

Yogesh Jaiswal: So basically we do this in cloud and honestly don't worry about why we are using claude. See claude is a very easy to use tool.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: I mean uh if when we see dependency of claude from a business

Gagan Bhaisa: East.

Yogesh Jaiswal: point of view it's good because claude is $20 per month right clay is $120

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: $190 per month. So if some part of clay can be done in clawed it's actually a benefit.

sampath vemulapati: Makes sense. Yeah. Yeah.

Yogesh Jaiswal: Okay. Uh now this is clear. Yes. So yeah at this point I feel that can we organize the sheets properly because uh I think u gagan when you see the client work you have done there is uh lot of jumbled things you have done right.

#### 00:35:55

Yogesh Jaiswal: So at this point, my only advice would Can you make a good like not now but can you

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: all make a good client delivery sheet starting from claim? So you have 50 companies right? Can you run good signals that you already have and then you create good qualification parameter? Then you find people then you create enrich those people and then you move to then we can move to the messaging part or the more uh critical parts but that is going to be your important task for everyone. I mean your clay table should look neat and clean at this point.

Gagan Bhaisa: Okay,

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: cool.

Yogesh Jaiswal: So I mean if you can spend some time into create creating this properly as

Gagan Bhaisa: Oops.

Yogesh Jaiswal: in realistically when we use clay right so we cannot show this to the client or the agency or the company you work with. So from the qualification parameter if you can qualify it because I'll give you a realistic view right if you work with 100 companies at least 60 to 70 should be qualified.

#### 00:37:08

Yogesh Jaiswal: I mean if you work with 100 companies and if your signals are making qualification less than 20 only 20 30 companies are qualifying then you are literally ruining the data because what if you can qualify more companies and because of strict qualification you're not qualifying more.

Gagan Bhaisa: Look.

Yogesh Jaiswal: Okay. So we need to be super clear should not be vague. It should it should not disqualify companies on very simple things. Okay. Now when we search people um Yeah. Can you can you go to add? Yeah. Can you go to this uh Okay. Go up. No, no, no. Go up. Yeah. Click on this three. Three. No. No. No. Yeah. Click on edit source. Yes. Yes. Click on edit inputs. Okay. Can you see job title?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay. Keep job title always similar to if you open this it will also see contains.

Gagan Bhaisa: That's it.

#### 00:38:14

Yogesh Jaiswal: Yeah. Click on this. Yeah. So contains will not give you more data. Okay. Similar similar to will give you more data. Right. So type sales anything marketing sales. Yes. Yeah. You can remove the exclude part.

Gagan Bhaisa: Yeah. Yes.

Yogesh Jaiswal: Yeah. Remove this thing. Yes. Now wait. See similar to gives you 61 result. Okay. Down. If you see down in the left corner, yeah, 61. Now if you go to similar to and change it to contains wait there is something wrong here then.

Gagan Bhaisa: I think we should remove this one. Your function.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Yeah. And like 50 166.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: And then go to similar. It's going to show us. Okay. I think pretty similar.

Yogesh Jaiswal: No, no, the problem is clay works on when you find the people. So it's not gives you the correct numbers.

#### 00:39:36

Gagan Bhaisa: Huh.

Yogesh Jaiswal: Uh yeah,

Gagan Bhaisa: Huh.

Yogesh Jaiswal: because it the final result they give in the loading part. Okay.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Yes.

sampath vemulapati: Uh also Yogesh like well we were doing yesterday u because I saw a

Gagan Bhaisa: All

sampath vemulapati: similar issue when I downloaded the data from prospio uh it

Gagan Bhaisa: right.

sampath vemulapati: it had the best results like it had more results of course like only downloaded 50 but when I tried qualifying in them in clay then it it is a little different. So there's a lot of dropout of the leads due to the qualification parameters.

Gagan Bhaisa: All right.

sampath vemulapati: uh but I put similar filters in prospia while downloading so there is a difference in the data like it's it's it's general or like like did I do anything wrong while downloading the data from prosper Amen.

Yogesh Jaiswal: No definitely if you are removing then there is something wrong honestly because most of the GTM engineers out there are not able to do this perfectly.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: So one advice is when you go to the strategy document and if you feel that some

#### 00:40:44

Gagan Bhaisa: s***.

Yogesh Jaiswal: qualification can be done in prosper I mean what if your qualification parameter was

sampath vemulapati: Yeah.

Yogesh Jaiswal: that the company's funded you can already see in prosper that the company can filter

sampath vemulapati: M yeah but that's a paid option as well.

Yogesh Jaiswal: uh it's funded or not right so why you I mean see that's a paid option

sampath vemulapati: Yeah yeah yeah yeah

Yogesh Jaiswal: but when you work on ground you would have a paid cross view so if you can filter those things in the

sampath vemulapati: correct

Yogesh Jaiswal: f first search itself there's no need to re-qualify in clay see nowadays clays use should be

sampath vemulapati: understood. Yeah.

Yogesh Jaiswal: minimal I mean we should use less clay features as possible because everything outside clay is growing prospio have lot of features um nowadays even MX domain you try to output right Google Microsoft certain email

sampath vemulapati: Mhm.

Yogesh Jaiswal: tools have those those feature also they would validate the email also they would find MX domains also. So we need to be clear that we use clay where other tools cannot perform especially for data no one uses clay.

#### 00:41:51

sampath vemulapati: learn.

Yogesh Jaiswal: I mean the way we are finding people in clay, no one uses. people always use a polar crossp because the data quality is uh it's a scrap data they

sampath vemulapati: Yeah.

Yogesh Jaiswal: have scrap data uh I can even give you okay not here but someday I'll show you on clay that um there are so many CEOs of Microsoft if you search uh on clay right there are so many

sampath vemulapati: Yeah.

Yogesh Jaiswal: Indian CEOs uh sitting in they just mentioned on LinkedIn that they are CEO at

sampath vemulapati: Mhm.

Yogesh Jaiswal: Microsoft oft and you will show it here. So we need to be clear that clay's data is not generally used for outreach.

sampath vemulapati: You got it. Yeah. Yeah.

Yogesh Jaiswal: Cool. So yes, always use similar to, right? See,

Gagan Bhaisa: s***.

Yogesh Jaiswal: similar to means um when you use Yeah. Can you remove marketing again if possible? I think that's why it's not working. Yes. So now it gives you 99.

Gagan Bhaisa: Okay.

#### 00:42:56

Yogesh Jaiswal: And now click contains. I think now the problem is with your companies. Um, select marketing and remove sales. Yes. So it gives you 68. Now click on similar to H. I think the problem is with we are because we are not searching when we continue it then clay search again.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: It's a free version that's why it's not showing but you will be amazed that the numbers are 60% higher.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: So if if you search leads with contains and if you get 200 leads with similar you can get 600 leads like you can get twice as more leads as compared to contains filter. Okay so I'll maybe I'll uh show you someday like how it works. Okay. So um now we are clear with the duping combining part. We are clear with the lookup part. Okay. Uh are you also clear with the scoring we did yesterday? Lead scoring. We did a account scoring yesterday,

Neeraj Sujan: Yes.

Yogesh Jaiswal: right?

#### 00:44:28

Yogesh Jaiswal: Are we clear?

Neeraj Sujan: Yes. Yes.

Yogesh Jaiswal: Okay. Yes. No. Perfect. See, at this point, we are making sure we learn all the features rather than making our clear tables look perfect. Uh that's the goal because you need if we understand the nitty-gritty of it like we

Gagan Bhaisa: I'll be

Yogesh Jaiswal: know that job title should be similar too to get better data right or uh can you can you do a Google search GaganI think you might understand Just type

Gagan Bhaisa: All

Yogesh Jaiswal: that does similar to gives you better results that than contains filter in clay people search contains filter in clay people search.

Gagan Bhaisa: right.

Yogesh Jaiswal: No clay people search. Yeah. Okay. You can get a better idea now. Right. So contains is a rigid filter. If it contains then only it will give.

Gagan Bhaisa: Okay. I think it gives a maximum coverage when you use a similar tool.

Yogesh Jaiswal: Yes. So we want to be very clear that because one mistake we would have less people right.

#### 00:46:01

Yogesh Jaiswal: So this is a very big mistake people make nowadays they use uh contents and that goes wrong. Okay one more thing when you work with European companies, Chinese companies, Korean companies you need to be clear that you cannot use English keywords. Okay. So can you go and search on Google founder? Yeah. Yeah. Founder in German.

Gagan Bhaisa: ordering. in Germany.

Yogesh Jaiswal: Yeah. No. No. Only German. Enter. Enter. Yes. So what? You can see the name, right? I don't know what it is. But when you search on a tool founder and if the clients are in Germany you cannot use founder you will use founder but you will use this also this term.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Okay same for every territory change from Germany to uh Spanish. Yes. Enter. So can you see now see because English is our prime language but if you see other countries they would also u go on LinkedIn and they would not use ling English as the language.

#### 00:47:26

Yogesh Jaiswal: There can be many founders you can find on uh data tools if you use these terms. Okay. Now there is one more interesting thing and this is very new in clay. Go to clay. Yeah. Now clear filters. Okay. Yeah. Go to go to a new table. Go to new people search. H yeah fine people. Yes. Okay. Now wait wait wait wait. There is a thing called language filter in play also. Go to language. Yes. You can filter. Okay. Type German. Enter. You know you can filter out people who you speak German all over the world. Okay. Now there are different things to it. You can even select Hindi. Okay. Let's let's go very narrow, right? Uh let's select Telu. T E L U G. Yeah. Yes. No. T E L U G. Yes.

#### 00:48:45

Yogesh Jaiswal: Okay. Now, this is a very unique thing. Can you see these people some or the other way for their names or for their content they post clay detected that these people speak Telu. Okay. Now we can go even more narrow. Which is the language which is very uh less spoken. I know couple of them. Um can you select Odia? Maybe you will find more less people. Yeah. Can you see? Okay. And you know there is there is a reason we use this. Okay. I'll give you an example now. Gage lives in US now and created a company right you don't know anyone. Okay. A GTM engineer will use your language to who are founders. Okay. And then the messaging would be same but at the last of the messaging there would be a PS that wonderful that um you are also from Odia background something like that right to build a connection so people would reply more okay so that's why uh language also plays a very important role there are multiple languages in the world like Bostonian uh Lebanese is where you may find niche people also uh you know if you clear this out and write Jewish yes JJ W I SH yes

#### 00:50:37

Yogesh Jaiswal: so you may you may find these uh Jewish I I don't know why it's not working here but I'll show you in my uh clay or something. So this this is a very important thing when we use founders detail on LinkedIn.

Gagan Bhaisa: Got it.

Yogesh Jaiswal: Yes. So we know the language filter. Uh also go to network and reach. Okay. Do you know what is the minimum? What is this estimated audience size? This is LinkedIn followers.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes. So if you select uh 100 these people should have less than 100 LinkedIn followers. Okay. Go to professional bio. So all yeah audience size is connections. Network size is followers. Okay. Uh bio you already know right? Name keywords and everything. Go to experience. Now this is very unique right? So Gagan now you are the CEO at Lina AI but you just joined one month back. I cannot sell you something right now because you just joined one month back right.

#### 00:52:00

Yogesh Jaiswal: So in months in the current role change it to 12. Yeah minimum 12. So this means people are there in the company from at least 12 months. Okay. Number of experience you don't need like people can work in multiple companies and it doesn't matter right but when you create an outbound list make sure the experience should be less than 12 months or more than 12 months because people generally cannot purchase they don't have even have a right to purchase right I mean they just joined the company why would they come in and say okay we need to purchase a tool of 1 cr rupees or 10 lakh rupees and uh network and reach should always be 100 uh when you do LinkedIn outbound the network should be always more than 100 connections or followers less than 100 are junk profiles.

Gagan Bhaisa: Got you.

Yogesh Jaiswal: Okay. You can even can you open this Narendra Modi profile row 13? Yeah. Yes. Open the LinkedIn URL. Yeah. Just click on this. It will open.

#### 00:53:16

Yogesh Jaiswal: Oh, this is a real profile. Got it. Most of the times you may find viewer profiles, the people who are not the real people. Okay,

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: perfect. So, uh the next task is to map the strategy document and make the

Gagan Bhaisa: cool.

Yogesh Jaiswal: clay table look perfect. Okay, you know everything now, right? You know, uh literally everything to create the perfect clay table. Okay. So, make that late table look perfect and tomorrow we are going to ship it. Ship it means we are going to make make it ready to use. Okay. So you uh write uh signal should be correct. Signal should not remove so many companies. People should have valid LinkedIn email ids, right? So that that's going to be your task for today to complete it. Like we need to make the clay table look perfect for the 50 companies we got it into clay, right?

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yeah. Any questions?

#### 00:54:31

Yogesh Jaiswal: Good. Uh, one advice, um, clay only comes, clay only becomes easy when you keep on using it. Uh, so just keep using clay. I think if you put in a week to use clay every day, it becomes very easy to use. That's that's my advice. I mean it's a very easy tool but when you use it again and again it becomes easier. Okay.

Gagan Bhaisa: Uh you guess one question from my side. uh when you said this one right 12 months role uh what I have seen is this is more used when uh there is a difference in buying committee let's say CMO director of marketing or anyone who director wants to come in and then there is a no process and nothing and they they want to make sure everything looks good and clean and uh runs smoothly rather than uh I mean blocking or uh failing every time. Uh it can be also six month in current role also that works. What do you say?

Yogesh Jaiswal: I mean um yeah I mean it totally depends on the company what they want you to do but uh yeah I think 6 months is also fine that's not a problem yeah it it

#### 00:55:55

Gagan Bhaisa: Okay. Mhm.

Yogesh Jaiswal: totally depends on your strategy and execution uh that's why in GTM engineering we

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: also need sales knowledge so because you know sales and marketing you come to this conclusion usion someone who don't know they would just use 12 or 11. Okay. So um yeah I mean you are right that we can even go 6 months that's not a problem.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Yes s

Gagan Bhaisa: All right.

sampath vemulapati: uh yog also like apart from this I actually have a list and I just have one doubt that like what if I want to like I do have their email ids I don't have their LinkedIn uh ids actually the urls so what if I want to run a list where uh I want to know where exactly this person is currently working or uh like can I get to know h how do I do

Yogesh Jaiswal: Yes. Anything in clear related to people, you need a LinkedIn URL.

sampath vemulapati: Right.

Yogesh Jaiswal: So you need to first find the LinkedIn URL And finding the LinkedIn URL is very easy.

#### 00:57:00

Yogesh Jaiswal: Run a clay prompt. Find the LinkedIn URL of the person map,

sampath vemulapati: Great.

Yogesh Jaiswal: full name, job title and company name. You will get all the LinkedIn URLs. And then you enrich person.

sampath vemulapati: Got it. So,

Yogesh Jaiswal: Mhm.

sampath vemulapati: first I do LinkedIn uh um enrichment.

Yogesh Jaiswal: Find URL. Find URL.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yes.

sampath vemulapati: Yeah. Find enrich person.

Yogesh Jaiswal: And then run enrich person also.

sampath vemulapati: Right. Yeah. And then in yeah in in that I'll get to know uh where exactly

Yogesh Jaiswal: Yeah, sorry.

sampath vemulapati: this maybe like the list I have I do have their email ids but u can I get to know where exactly this person is currently working

Yogesh Jaiswal: Yes, you can you can get everything also. Do you know what is sculptor?

sampath vemulapati: Awesome.

Yogesh Jaiswal: Okay, Gagan, do you know what is sculptor?

Gagan Bhaisa: Yeah, I know.

Yogesh Jaiswal: Can you open sculptor if possible? Just close this. Close the fine people.

#### 00:57:58

Yogesh Jaiswal: It will Okay. Okay.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Can you close the fine people? It will not work properly. Yes. Yeah. Go to any sheet list building. Yeah. Oh, no. Go to Yeah. Yeah. The already existing one,

Gagan Bhaisa: Okay.

Yogesh Jaiswal: not the Yes.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes.

sampath vemulapati: Good boy.

Yogesh Jaiswal: Go to Yeah. Now, uh Sut, this is a thing called sculptor. Kagan, can you click on this? Okay. Make it to analyze. Don't build. Keep it to analyze. Yeah. Go down. There is a thing called build and analyze. Right. Click to an Yes. Don't click on build. It will start building it for you. So,

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: uh sat you can have any query here and it will answer. This is clay specific AI agent.

sampath vemulapati: Okay. Okay.

Yogesh Jaiswal: You can ask any question.

#### 00:58:46

Yogesh Jaiswal: You can even does my clay table looks perfect.

Gagan Bhaisa: Hello.

Yogesh Jaiswal: It will check the table also.

sampath vemulapati: Got it.

Yogesh Jaiswal: Can you write a prompt?

Gagan Bhaisa: Okay. Uh let me know how mess Yeah. 12.

sampath vemulapati: This is great.

Gagan Bhaisa: I'm missing the value of a state region per hour 20.

sampath vemulapati: I think this makes a lot of sense. Uh, in general, like I I can just simply paste the list here and then probably I can ask

Gagan Bhaisa: Uh sut can you just repeat the question that you asked?

sampath vemulapati: uh yeah so I'm thinking that uh I have a list uh of few bunch of founders startup founders and I want to check if they

Gagan Bhaisa: Okay.

sampath vemulapati: still uh are part of the same company or not uh and uh yeah that's that's what I just wanted to validate the

Gagan Bhaisa: Okay. And what data you have?

sampath vemulapati: like startup founders this uh list.

Gagan Bhaisa: No, no, no. I mean uh in terms of data, what what data you have?

#### 01:00:31

Gagan Bhaisa: You have a founder name and

sampath vemulapati: Yeah. Founder name, uh company name, number of employees it holds,

Gagan Bhaisa: Okay.

sampath vemulapati: uh their um this thing as well, their email ids as well.

Gagan Bhaisa: Okay, got it.

sampath vemulapati: I think I think it should like I can just upload the CSV in this and then I think it should do. Yeah.

Yogesh Jaiswal: Yes, find LinkedIn URL and it will work.

sampath vemulapati: Yeah,

Yogesh Jaiswal: You can go sculptor and sculptor will give you the same thing.

sampath vemulapati: you perfect. Perfect. Yeah, that's

Yogesh Jaiswal: So sculptor is necessary because see if you ask a question from your table, I have not seen your table, right? So sculptor first see your table then answer it.

sampath vemulapati: got

Yogesh Jaiswal: Perfect. Cool. So try making your clear table looks look perfect by maybe tomorrow or maybe this week. The goal can be to make sure the table looks perfect because we going to create a long video around it, right? We need a portfolio to reach out. Yes. So that's going to be the goal and yeah I think we have covered few important topics but we are going to cover some advanced topics now. I'll also show you how to create live tables. So live tables means you don't need to even open clay. Clay will work on the background. You will use clay's API to use clay. Right? So this is it for today. Uh and let's connect tomorrow on uh shipping this table and put doing last minute changes and yes any questions you can text me not a problem.

sampath vemulapati: Thank you.

Yogesh Jaiswal: Yeah guys have a nice day.

Gagan Bhaisa: Thank you.

sampath vemulapati: Nice day. Bye.

Yogesh Jaiswal: Okay.

sampath vemulapati: Thank you.

#### Transcription ended after 01:02:19

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.