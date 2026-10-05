# D13+D14_ LinkedIn Sales Navigator + Data quality fundamentals - 2026_09_16 08_56 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D13+D14: LinkedIn Sales Navigator + Data quality fundamentals

Sep 16, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

The session defined modern Go-To-Market engineering roles while detailing advanced data acquisition, quality verification, and strategic targeting methods.

GTM Engineering Role and Scope

GTM engineering involves full-cycle management, covering strategy, problem-solving, and consistent outcome delivery.

The role extends beyond list building to include multi-channel outreach such as LinkedIn and events.

Engineers must think beyond pre-built AI agents to explore broader product features and messaging.

Future expectations involve single experts managing entire sales and marketing functions independently.

Sales Navigator Usage and Limitations

Sales Navigator identifies niche domains like .uk or .fitness effectively.

The platform lacks an API, requiring manual data handling and no automated connectors.

Mass exports are restricted; significant data extraction requires expensive third-party tools.

LinkedIn Sales Navigator data requires a mandatory cleaning step before use due to inconsistent quality.

Data Fetching and Deduping Methodology

Blitz API and FullEnrich allow direct data fetching without relying on intermediary platform exports.

Use Claude to run deduping logic based on LinkedIn URLs, emails, and name-company combinations.

Organizing data into separate Company and People tabs in Claude ensures clean, structured output.

Storing processed data in Supabase facilitates reuse and prevents redundant enrichment processes.

Data Quality and Email Verification

Data quality relies on verifiable LinkedIn URLs and precise email delivery parameters.

Avoid sending emails to Mcast domains, as these cybersecurity gateways block external spam.

Differentiate between valid, catch-all, and valid-catch-all email types to ensure high deliverability.

Utilize multiple verification tools like Enrichly, BounceBan, and Million Verifier for data integrity.

Expect only 60% of exported data to remain usable after filtering invalid and Mcast records.

ICP Identification and Strategic Planning

Identify ICPs by analyzing current sales channels and customer behaviors on company websites.

Segment target audiences by size, distinguishing between small hosts and large enterprise clients.

Prioritize paid ads for low-ACV segments and targeted outbound for enterprise-level property managers.

Validate the buying committee before selecting outreach channels or participating in specific events.

Next steps

[Yogesh Jaiswal] Send Video Walkthrough: Distribute the 1-hour Sales Navigator walkthrough video to the attendees.

[The group] Generate Target List: Curate a list of 50 potential client accounts for the previously selected company. Include the company name, website domain, and LinkedIn URL for each entry.

[Yogesh Jaiswal] Send Documents: Provide documentation regarding catch all and valid catch all concepts to assist with project understanding.

[sampath vemulapati] Prepare List: Assemble the data list required for upcoming operations.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 16, 2026

### D13+D14: LinkedIn Sales Navigator + Data quality fundamentals

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D13+D14: LinkedIn Sales Navigator + Data quality fundamentals

Meeting records Transcript Recording

#### Summary

The session defined modern Go-To-Market engineering roles while detailing advanced data acquisition, quality verification, and strategic targeting methods.

Defining Go-To-Market Engineering
Modern Go-To-Market engineering encompasses comprehensive strategy and technical execution, moving beyond basic lead generation to manage sales functions independently. Professionals in this role act as technical experts.

Advanced Data Processing Strategies
Combining diverse datasets requires rigorous deduplication hierarchies centered on unique identifiers like LinkedIn URLs. Utilizing Application Programming Interface providers enables more efficient data fetching than manual exports.

Outreach Quality and Deliverability
Maintaining outreach efficiency requires strict Mail Exchange domain filtering and multi-tool email verification to bypass cybersecurity blocks. Centralized storage for cleaned records effectively prevents repeated infrastructure costs.

#### Next steps

[Yogesh Jaiswal] Send Video Walkthrough: Distribute the 1-hour Sales Navigator walkthrough video to the attendees.

[The group] Generate Target List: Curate a list of 50 potential client accounts for the previously selected company. Include the company name, website domain, and LinkedIn URL for each entry.

[Yogesh Jaiswal] Send Documents: Provide documentation regarding catch all and valid catch all concepts to assist with project understanding.

[sampath vemulapati] Prepare List: Assemble the data list required for upcoming operations.

#### Details

Role and Scope of a Go-To-Market Engineer: Yogesh Jaiswal explained that as companies increasingly recognize the value of Go-To-Market (GTM) engineers, the role extends far beyond basic list building and encompasses comprehensive strategy and execution (00:04:06). Yogesh Jaiswal stated that GTM engineers handle everything from identifying problems and managing campaigns to exploring alternative growth channels like Google paid ads, product revamps, and competitive analysis when standard outbound approaches fail (00:05:00). sampath vemulapati noted that while learning 90% of these business concepts was new, the fundamental objective remains sales (00:04:06). Yogesh Jaiswal ultimately projected that in two to three years, GTM engineers will operate as technical experts capable of independently managing functions traditionally handled by separate sales and marketing teams (00:06:07).

Application to AI Agent Companies: sampath vemulapati inquired whether working with a company like Goji Berry, which is an AI agent for sales and lead capture, would present difficulties. Yogesh Jaiswal clarified that Goji Berry provides a pre-built AI agent rather than GTM engineering itself, emphasizing that GTM engineers must think beyond a single product and analyze competitor features and messaging if initial strategies fail (00:07:03).

Sales Navigator Capabilities and Limitations: Yogesh Jaiswal demonstrated LinkedIn Sales Navigator, noting its structural similarities to tools like Apollo and Prospio while highlighting key operational constraints (00:08:24). Yogesh Jaiswal explained that Sales Navigator does not support mass exports beyond 1,000 to 2,000 leads without expensive third-party tools, lacks direct API integrations requiring manual data handling, and provides lower data quality that necessitates pre-cleaning. However, Yogesh Jaiswal noted that Sales Navigator is exceptionally effective at detecting non-.com domains (such as .uk or fitness domains) for company searches (00:09:34).

API-Driven Data Sources: Yogesh Jaiswal introduced API-as-a-data providers like Blitz API and Full Enrich, which allow GTM engineers to fetch data directly via prompts rather than downloading information from tools like Apollo (00:11:22). Yogesh Jaiswal demonstrated running a prompt in Claude to find the top 10 Chief Technology Officers of Y Combinator 26 AI-native companies in the United States using Blitz API and Full Enrich to compare data quality (00:12:42).

Data Combination and Deduplication Logic: Yogesh Jaiswal reviewed the combination and deduplication methodology using Claude to merge CSV files from different providers like Apollo, Prospio, Blitz API, and Full Enrich into a master sheet (00:14:03). Yogesh Jaiswal detailed the specific deduplication hierarchy created in Claude: first deduplicating by LinkedIn URL, second by email address, and third by a combined parameter of full name and company name to account for common names (00:15:12). Yogesh Jaiswal explained that Claude outputs the processed data into two clean, separate tabs—a company tab and a people tab—which simplifies subsequent enrichment in Clay compared to performing the operations directly within Clay (00:17:07).

Guest Ideal Customer Profile Exercise: Yogesh Jaiswal led an exercise analyzing the website for a company named Guest to determine its Ideal Customer Profile (ICPs). Through contributions from sampath vemulapati, Gagan Bhaisa, and Neeraj Sujan, the team identified that the platform functions as an AI-powered vacation rental property management software serving vacation rental hosts and property management companies (00:19:38). Yogesh Jaiswal detailed that the platform targets small hosts (having one to three listings) via paid marketing and ads due to low pricing ($9 per seat), while targeting property management companies (having four to 200+ listings) via outbound sales (00:21:41).

Simulated GTM Strategy Discussion for Guest: Neeraj Sujan and Gagan Bhaisa engaged in a roleplay exercise proposing first-week actions for a GTM engineer joining Guest as a startup (00:24:09) (00:27:50). Yogesh Jaiswal outlined the current sales process as relying primarily on small real estate and property management events and booths in the United States where the $9 software is sold on the spot (00:25:28). Gagan Bhaisa proposed identifying the buying committee, evaluating event return on investment, and focusing on organic growth channels like SEO and Instagram outreach for small hosts while segmenting property managers for B2B outreach (00:27:50). Yogesh Jaiswal critiqued that the team initially omitted questions regarding product features, competition, and global market positioning, while noting that Guest employs approximately 819 people, predominantly in customer success and support rather than large sales teams (00:31:40).

Data Quality Parameters in GTM Engineering: Yogesh Jaiswal and Neeraj Sujan discussed data quality fundamentals, identifying verified email addresses and LinkedIn profile URLs as critical parameters to prevent wasting expensive data and infrastructure resources (00:34:05). Yogesh Jaiswal noted that LinkedIn Sales Navigator data requires a one-step cleaning process in Clay to verify real profiles through followers and connections, whereas Apollo and Prospio data can be used immediately (00:36:36). Yogesh Jaiswal emphasized that due to invalid emails, missing information, and cybersecurity blocks, GTM engineers typically expect only 60% of an exported dataset to be usable for outreach (00:47:16).

Email Verification and Deliverability Classification: Yogesh Jaiswal explained email verification mechanics utilizing tools such as Enrichly, Bounce Ban, and Million Verifier to categorize emails and maintain low bounce rates (00:38:43) (00:42:51). Yogesh Jaiswal distinguished between "catch-all" emails (where an inactive employee's email still receives mail but gets no response) and "valid catch-all" emails (where an email structure redirects to an active ID), advising that valid catch-alls are safe for outreach while standard catch-alls should be avoided (00:40:26). Yogesh Jaiswal outlined a multi-tool verification workflow in Clay combining Enrichly, Bounce Ban, and Million Verifier parameters to determine whether to execute outreach (00:43:54).

MX Domain Filtering and Cybersecurity Blocks: Yogesh Jaiswal explained that MX domain information reveals a company's email workspace (such as Google or Outlook) and identifies cybersecurity security gateways like Mimecast, which block and prevent spam emails from landing (00:45:38). Yogesh Jaiswal instructed that outreach emails must never be sent to domains protected by Mimecast or similar mail spam protection services because delivery will fail, and recommended aligning outbound sender accounts with 80% Google and 20% Outlook ratios based on target MX domains (00:47:16).

Centralized Data Storage in Supabase: Yogesh Jaiswal explained that GTM engineering agencies store all cleaned and enriched data records in Supabase to enable continuous reuse across campaigns. Yogesh Jaiswal noted that storing data in Supabase prevents the repeated costs and time of re-enriching thousands of records each month, allowing GTM engineers to query historical data using APIs connected to Claude (00:48:58).

Account-Level Export Assignment: Yogesh Jaiswal assigned an exercise for participants to create a target account list of 50 companies using platforms like Apollo or Prospio based on the specific company they selected (such as Goji Berry) (00:51:54). Yogesh Jaiswal instructed participants to filter for the right company profile, export batches of 25 accounts to compile company names, domains, and LinkedIn URLs into a Google Sheet, and prepare the data for upcoming workflow exercises in Clay (00:53:10).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 16, 2026

### D13+D14: LinkedIn Sales Navigator + Data quality fundamentals - Transcript

#### 00:04:06

Yogesh Jaiswal: Hey, good morning Sit.

sampath vemulapati: Good morning. How are you?

Yogesh Jaiswal: I'm good. How are you?

sampath vemulapati: Good. Good.

Yogesh Jaiswal: How's it going with everything uh with what we are learning?

sampath vemulapati: Yeah, I'm being able to apply uh most of the learnings but uh you know since I'm pretty new to this entire uh business,

Yogesh Jaiswal: Yes. Yes.

sampath vemulapati: I'm still you know learning like a lot of thing is like almost 90% of the things uh that are taught are new to me.

Yogesh Jaiswal: Yes.

sampath vemulapati: So still trying to get my head through that. But yeah,

Yogesh Jaiswal: Yeah.

sampath vemulapati: I mean uh it's pretty simple as in when I'm understanding at the end of the day we here to sell and

Yogesh Jaiswal: Yes. Yeah.

sampath vemulapati: then um I also have a couple of doubts like um good time to take but like you

Yogesh Jaiswal: Yes.

sampath vemulapati: want Yeah. So uh I mean where does the job of GTM engineer ends? Because like you know what I understand is like we do the list building.

#### 00:05:00

sampath vemulapati: We do uh we do specific list and then our job ends at sending the list or we also reach out to the people in multiple ways or doing some mail blast or something or what like where do you think the role ends typically?

Yogesh Jaiswal: See the first of all the role doesn't end because I mean if you see mature companies who are hiring GTM engineer right now when they understand the value of GTM engineer and this is typically happening with US companies. So they would want you to do everything.

sampath vemulapati: got it.

Yogesh Jaiswal: You would be doing everything.

sampath vemulapati: H.

Yogesh Jaiswal: You would be uh managing it. You would be understanding strategically. Wherever you feel that there is a problem, you are going to solve it. And you are going to sit on the team and give give the results and you have to keep giving the results.

sampath vemulapati: Okay.

Yogesh Jaiswal: See if email doesn't work, LinkedIn will work. LinkedIn doesn't work, events will work. You know, there are so many things right now.

#### 00:06:07

Yogesh Jaiswal: Google ads, right? If you're thinking that is outbound every time going to work. No, outbound never works sometimes.

sampath vemulapati: Correct. Of course,

Yogesh Jaiswal: What if what if Yeah.

sampath vemulapati: like cold emailing barely works.

Yogesh Jaiswal: What if nothing works? What you you should do? You cannot say that okay, I am a GTM engineer and I'm not responsible. You might have to go Google paid ads. You might also have to deal with a product revamp. You might also have to check competition how they are growing, why you are not growing. So this there is there are endless I mean if you ask me 2 three years down the line just consider yourself as an expert who have technical knowledge where a company can utilize only you and they don't need a sales and marketing team. That's where we are going to head towards.

sampath vemulapati: Got it. I I mean uh the reason why I was also asking this question is um I have chosen this company called uh Goji Berry.

#### 00:07:03

Yogesh Jaiswal: What's the video?

sampath vemulapati: So and it it exactly does the same. I mean doing what it does to them won't be difficult or because like it's kind of like uh you know it converts the buyers or uh you know it it basically captures the signals that do matter for the businesses. So it it's more of like a GTM uh in in itself. So like do you think like will it be difficult uh for me to do this

Yogesh Jaiswal: See first of all uh your company is an EI agent which is doing sales. Okay.

sampath vemulapati: correct?

Yogesh Jaiswal: or uh again GTM engineering is not what goji where is doing it is an AI agent which is getting the leads okay so you can consider that this is something which is pre-built and can be used immediately but this this is just one format so we need to be super clear that what if this doesn't work I mean if this doesn't work then what's next so you can also be a think beyond what goji berry is doing and understand that if this doesn't work what are the next steps so don't think about if you are a GTM engineer you're just going to scale goji berry right you might also see the product and if you might also see the features which others have and you might create messaging around

#### 00:08:24

sampath vemulapati: Yeah,

Yogesh Jaiswal: it so you need to think beyond only doing outbound

sampath vemulapati: I got Got it.

Yogesh Jaiswal: yes okay uh I had sales navigator last time in my uh earlier class. Just a second. Yes. But this time I have I don't have a subscription but I can show you very easily. Uh okay. Sales n have anyone here have used sales navigator by the way? No one. Okay.

sampath vemulapati: I have used earlier but like that was for a nonprofit purpose so doesn't matter.

Yogesh Jaiswal: Oh yes. Yes.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So it's the same like uh Apollo. Okay. Few things I just want to mention. It's it's very same like Apollo or Prospio. Okay. If you can see you have information, company, past company, current company. I have also created a separate video. I'll send it to you after the class. So that is an entire sales navigator walkthrough of 1 hour. We just want to mention here that few things which are not possible in sales navigator.

#### 00:09:34

Yogesh Jaiswal: Okay. Ma mass export is not possible in sales navigator. So let's say if you see this 15,000 results here. Uh I cannot export this easily. You need tools which are expensive. So mass export is not easy. Uh you can export up to like 1,000 2,000 leads uh easily but beyond that it's very difficult. Second thing um uploading companies and then searching people around it is uh easy but it's not very easy as compared to Apollo and Pluspio. Okay. Now one thing I want to mention um which is very very important for everyone here. Do you know this companies called which have a URL like net app.uk UK dotfitness uh you know this company called bold.fit fit. So you know these domains right which are not.com but still the companies are very famous these kind of domains when you have a list of companies like this always use sales navigator because sales navigator can detect it very easily okay and uh rest I would send you the video after this class you can go through it but it's definitely it's the most easiest thing to use but um yeah but also So you need to understand where you need to use people first search would be obvious you need to use it but apart from that there is not a big use of sales navigator in uh GTM engineering it's always going to be Apollo prospin also there is no API to connect sales navigator by the way uh there is no API so everything needs to be going here

#### 00:11:22

Yogesh Jaiswal: and doing it manually okay so this is it uh yeah not rocket science that's why I'm not giving you much information you can just open a sales navigator dashboard whenever you're using hardly take 10 minutes for you to understand but just the good steps I've given you okay now I want to show you something few things anyone heard of this this thing blitz API like have you heard this online or on LinkedIn Okay. Yes.

Gagan Bhaisa: Yeah. No, I heard about this and we use it at eternity.

Yogesh Jaiswal: Okay. Perfect. So, uh guys, this is uh API as a data, right? So, you know that data fetching is really difficult. You go into tools, you put uh information, then you download the data, then you run it. Uh this is an API directly can connect this API and the data is there for ready to use. Okay. Uh so this is a leading one called blitz API. Okay. There is one more thing called and we would be using this.

#### 00:12:42

Yogesh Jaiswal: There's one more thing called full enrich. Okay. So this is also very popular amongst uh using API as a data provider. Okay. So okay let me show you how it can be done. Uh you get some idea. Okay. I'll show you how this works. Just a second. Okay. Can you see my screen? Uh, can you see my screen?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. Okay. Sorry. Perfect. So, can you see that um I was doing a data comparison. So, I was running everything from cloud code. That means I'm not going to Apollo to find uh or cross or sales navigator. So I said find top 10 CTOs of YC26 AI native companies in the US using blitz API and full enrich. So I was creating two list to check the quality of which is delivering the best. Okay. So yeah after giving the API can you see this? I got the list.

#### 00:14:03

Yogesh Jaiswal: Okay. So I've just written a prompt and I got the people that I want. Okay, perfect. So this is just the API. You can just type. Okay, I need the CT of Google like that. Okay, of all Fortune 500 companies. Okay, so it's going to be like that. Okay. No, no need to go to Apollo and do that. Okay. This is typically when YC startups where experimentation is going on. Okay. Um yes. Now I also want to mention that yesterday we discussed combine and ddup, right? So this is the combine and dup methodology. Okay. So uh combining and reduping means I had two files here like one and two two CSV files. files. Now you can consider this is from Apollo, this is from Prospio. Right? Now this is from Blitz API. This is a full enrich. Okay. When we combine and did you it creates a master sheet.

#### 00:15:12

Yogesh Jaiswal: Okay. And then yeah or maybe I can show you how Okay. So this is basically a skill that we create in claude and uh it's going to be doing combining reduping in certain parameters. parameters would be checking both of the files. Then it would be uh yes uh then it would be doing the video from emails then LinkedIn URLs then full name and uh company name combination. I'll just show you how that skill works. Okay. Uh yes. Uh you can see this right? You can read this. So this is the duping logic we have created. First the dup from LinkedIn URL. Okay. Second it moves to email address. Then third it moves to a combination of full name and company name. Okay. So there cannot be okay there can be one sad working at satwa but there cannot be two of find but there can be two sat easily in India right or there can be two gagan easily so we cannot do a full name full names are pretty common but we need to do a full name plus company name due okay and also when we create.

#### 00:17:07

Yogesh Jaiswal: Okay. The reason we use claude is it outputs in a good format. Okay. So the output is in two separate tabs. First is company tab. So company name, company domain, company Indian URL, company employee count. Then you have people tab. First name, last name, full name, job title, seniority, LinkedIn, city, state, country. Can you see city, state, country, company name, company domain, company LinkedIn URL and email id. Okay. So the whole purpose of doing it in claw is it's very neat and clean here. You don't you if you do this in clay it might take 1 hour for you to do this. So that's why it's very easy to do in plot. Okay. We would be learning that but just wanted to show you. Uh okay let's go back. Yes. Okay. By the way, after dedoping it, uh, it. The sheet will look like this. Uh I'll show you a sample sheet. Okay.

#### 00:18:13

Yogesh Jaiswal: This is the sheet and it will look like this. Okay. So I have created this list from uh Apollo, Prospio, Sales Navigator and then video and combined in clot and then enriched in clay. Okay. So can you see the organization company is separated. Okay. This is company tab and company have domain and company name website employee count. Okay. Everything. And then I have a people tab. Okay. So it was very easy. I have moved this data from uh Google sheet to clay. These part I enched these three parts. So clay becomes very easy for me if I do this neat and clean. Okay. Yes. Any questions in this? Any questions in combining andoping logic? No. Okay. Uh okay. I had an exercise for you. I mean I just want to understand if we are on the same page. So can you see my screen? Yes.

#### 00:19:38

Yogesh Jaiswal: Can you see this company? Uh can you can you see this company? Uh my screen gets

Neeraj Sujan: Yes.

Yogesh Jaiswal: okay. Uh a very small exercise that can you go through this and if I ask you whom they are going to sell, can you come up with that? I'll just paste this into the chat. It's in the chat. I just want to check that if you are able to find the uh ICP for this or not. We just need to understand whom we are going to sell. Uh so for everyone this uh the link is in the uh meeting window uh meeting chat. You just need to go to the website and just let me know what is the ICP right ICP for this company.

Gagan Bhaisa: uh small house owner, uh rental uh taker,

Yogesh Jaiswal: Uh, you said what? Small.

Gagan Bhaisa: I say small house owner

Yogesh Jaiswal: Sorry. Uh, no.

sampath vemulapati: This is for Airbnb. Sorry, this is for the vacation rental owners or host who who has multiple listings.

#### 00:21:41

sampath vemulapati: Uh and

Yogesh Jaiswal: So you check yeah check these options these ones you will understand what what is the ICP this

Gagan Bhaisa: Yeah. So,

Neeraj Sujan: Yeah.

Gagan Bhaisa: it's providing full ERP for all solutions. Uh I mean kind of a ERP, not a full ERP, kind of ERP for someone who owns a lot of rental apartments,

Yogesh Jaiswal: Yes.

Gagan Bhaisa: uh who owns lot of uh basically house listing like Airbnbs.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: So whom do they sell to? Like if you go into Apollo, what will you search? Like whom are they going to sell? What kind of companies? Like can we if we go specific on the uh type,

Gagan Bhaisa: Cool.

Yogesh Jaiswal: what companies we are going to sell? And it's um it's already there. Then if you just scroll the website and understand. Okay, no worries. Uh can you see this this prop

Neeraj Sujan: Yes.

Yogesh Jaiswal: property management companies these are ICP okay and this tool is a uh property management software PMS even though they have mentioned that uh it's an AI powered vacation rental platform but it's a property management software if you see this your first property management software okay and they sell to small host which are having one to three listing then four to 200 listing they're enterprise but these would all property management companies and for small host I don't think we need outbound because if you see the pricing it's only $9 per seat.

#### 00:24:09

Yogesh Jaiswal: So for this part we are going to do paid uh marketing or ads this part because reaching out to one person is like not a good idea. So for these two parts you would be doing outbound. Okay. So my question is uh till now whatever we have learned if you are going to work on this company as a GTM engineer what questions you are going to ask me if I am the founder of guest like any five questions you would like to ask me and this is your first week so imagine I am a founder who have made guest I have all of the people who are coming to me which are uh small host I don't have any property man managers or enterprise clients and uh I need a GTM engineer that can help me out. So how would you position it yourself and how what questions you will ask me? Um what outputs can I expect from you?

sampath vemulapati: probably I may start with um what are the channels that you're getting maximum reservations from and is there any problem in

#### 00:25:28

Yogesh Jaiswal: So for the channels I am getting all of the deals closed on events. Uh I organize small events in US. Uh I call property managers and they buy my software. That's the only channel I have right now.

sampath vemulapati: Amen.

Neeraj Sujan: Like the very first question I will ask what is your current uh sales process? How does it look like before I dive deeper?

Yogesh Jaiswal: So uh yes so nish the current sale process is very easy. I do small events I have small communities in US. Uh in those events I call property managers and uh when they like my platform they purchase it then and there. Uh but I have not explored anything beyond that.

Neeraj Sujan: And how do you call the property managers to these events? Where do you find them?

Yogesh Jaiswal: These are property real estate events. So they always come there and I have my own booth over there and they come to my booth and we sell it because it's $9. It's very easy to sell on the spot.

#### 00:26:40

Yogesh Jaiswal: If you see

Neeraj Sujan: So once they come to these events, do you follow up with them? Do you take the contacts? What is the next steps after the event gets over?

Yogesh Jaiswal: Yeah, I do talk to them, but I don't have a lot of People. to deal with. I just have few people who come to the event. I talk to them and that's how it's going. I was planning to have salespeople because right now my huge focus is to uh get property management companies but uh yeah I thought to like check if a GTM engineer can help me out.

Neeraj Sujan: Okay. And do you deal with commercial properties or residential properties?

Yogesh Jaiswal: I deal with all kind of properties. Any person who is listing properties, I can deal uh I can sell it to them as per the listing. I can also connect their current properties which are on Airbnb to my platform.

Neeraj Sujan: Okay.

Yogesh Jaiswal: Yes. And we are not competing with anything. We we are building one single so we are competing with point solutions.

#### 00:27:50

Yogesh Jaiswal: We are building one single platform which does uh event sorry guest reservations operations and payments everything would be under one platform. So we don't compete with anything out there but we want to scale it from here now. So I just want to understand if you come to work with me as a GTM engineer what you're going to do in the first week.

Gagan Bhaisa: Uh yog is to understand the buying committee who are actually a buyer of the solutions.

Yogesh Jaiswal: Yes. Yes. That's right. Because I have not sorted out whom I can like my correct set of people who are going to buy. But apart from that for the whole one week, what can we do more? Uh that's that first plan.

Gagan Bhaisa: Okay. So first thing uh understanding the buying committee.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Second thing uh what channels or what are the specific uh revenue that you are getting from as you mentioned events right so what kind of events uh when I say figure out different kinds of events uh we want to participate with a lesser cost and see what the ROI is basically coming out that's the plan third

#### 00:29:09

Yogesh Jaiswal: Yes. Mhm.

Gagan Bhaisa: thing is most uh since this is a rental side of thing which is a D2 B2C maybe a B2C B2B I mean I'm not categorizing this as a B2B but more as a B2C business customer so I

Yogesh Jaiswal: Yes.

Gagan Bhaisa: would uh put my money on organic growth uh like mostly SEO kind of thing have a beautiful

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: Instagram outreach where most of the people spend their time have a like and then goes on like Facebook and other things. So and then try to I mean these are the planning phase I would do for one week by I mean kind of sitting with you and then more plans on B2B side uh like as you said property management companies to understand who are actually buyers uh because what I understood as a person property manager are technically someone who manage the property but who don't have a dedicated uh authority to take a decision on this so I want to make sure that I talk to the property manager hex or so on who takes a decision to procure this

#### 00:30:29

Yogesh Jaiswal: Yes. Uh also just want to understand are you going to do emails or LinkedIn outreach or not?

Gagan Bhaisa: I I would not do ladian and outreach.

Yogesh Jaiswal: No LinkedIn.

Gagan Bhaisa: There is a there is a reason why I say no.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Uh maybe you have a different opinion.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: uh because since uh I categorize this B2C company, B2C company would hardly see any people in uh mostly I would say LinkedIn or email it's always a word and mouth solution uh you show commercials uh you show like your organic growth as I said uh because people really attract on all this uh thing rather than emails one.

Yogesh Jaiswal: Got it. Yeah. Just to mention, we are also selling to property management companies. So, uh these are B2B.

Gagan Bhaisa: Yes. On on those case. Yes. Yeah. When we categorize basically who are our basically tire one uh buyer, tire two buyer, tire three buyer based on like the segment that we are setting and then we can start out like

#### 00:31:40

Yogesh Jaiswal: Got it. Yeah, this is cool. Okay. Uh, okay. I think this is good. Uh, one few things I just want to mention that um try to talk more about the business that are you coming up with new product features? What is your competition? Uh, how are you even positioning in US or like global market? because we miss this questions. Uh if you don't even know which market they are targeting, uh then it becomes really difficult. Um yeah, but I think this is good. But uh just to mention this company is again a very big company and if you see here, you can take out some time and also check it. So they have around five yes around 819 people working with them. So you can after this call you can check out that where they have most of the people. Okay I like in GTM or you can see here right there are most of the people in customer success and support. So sales is again their uh you can you can sum up here right you you are right that they're mostly sales are getting from SEO and paid ads because they have few sales people here like 90 uh if you see big companies they have top would be the

#### 00:33:00

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: salespeople right so definitely they are having lot of growth from paid marketing so yes you were right and they have more in support okay yeah this is

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: good

Gagan Bhaisa: No also that customer success and support is also a part of sales where people uh like small bookings like let's say someone calls you for credit card you fill up a form like they work like that also.

Yogesh Jaiswal: Okay. Okay. Got it.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Super. So yeah, I mean easily we can sum up but we can the goal to show you this was just to let you know that uh these kind of companies will start looking out for GTM engineers now right uh where they don't want to train people again and again in sales and marketing. They want one person. They would arrange a team, train that person, and that person would be single-handedly doing everything. Outreach, events, planning, everything. Okay. Uh this is good. Okay. I want to talk about data quality fundamentals now.

#### 00:34:05

Yogesh Jaiswal: Okay. Uh before talking about data quality, I just want to ask you uh what do you understand by data quality in only in GTM engineering? So only the Apollo prosp all of the data. So if you can mention what do you understand by data quality and then maybe we can uh dig more deep into it. So if I say data quality what do you understand by data quality and why it's so important.

Neeraj Sujan: So first is the data points uh they are verifiable. So it's multiple uh like the emails are verified, the LinkedIn profiles are verified or if one platform does not uh give us an email or we we need to we need to check from multiple platforms if the email matches and only then we are certain that this is uh a good quality.

Yogesh Jaiswal: Yes. Like apart from email, do you think there are more parameters to data quality?

Gagan Bhaisa: Yes, there are.

Yogesh Jaiswal: Uh what it is

Gagan Bhaisa: Yeah, I would approach like this the data quality. How can this data be reusable uh for different way of uh leveraging to get connected with the person?

#### 00:35:33

Gagan Bhaisa: That can be email, that can be any intent, that can be any uh pointer that I got, that can be any signals. How can this be useful for every time that I talk to the person?

Yogesh Jaiswal: Mhm. Yes. Uh but if you see in a broader term right now at this point people are not concerned about the messaging what they write in the message right it's it's very easy anyone can even a six uh sixth class student can write a email and that could be good. Right now we need to understand that if the data quality is not good there is no point of doing infrastructure sequencing messaging campaigns anything and also we need to again understand that data is expensive. So if you are a GTM engineer and if you're not good with data um then you're going to spend a lot of money of the client right. uh for an example that whenever you download a data it contains emails. Okay. So data quality would be in parameters. The parameter would be LinkedIn URL and emails.

#### 00:36:36

Yogesh Jaiswal: Okay. Also just want to give you an information when you use sales navigator and you export you will not get LinkedIn profile URL. Okay. You need to again enrich it in clay and we would learn that but just want to mention it here. So when we talk about data quality, if you're a sales navigator, you need to again fetch the LinkedIn URL from a uh clay. Okay. Also, LinkedIn sales navigator data quality is worst. Okay, that means that if you're trying to search something, it will give you everything, but the quality would not be. So, LinkedIn sales navigator data requires a one-step cleaning before using it. A polar prosecutor you can use it immediately. Okay. Now data quality have two parameters. First is LinkedIn URL. Second is email. Okay. Uh how would you define if the LinkedIn URL is right or not? Okay. Very easy. If that LinkedIn profile is a real person, uh if it's a real profile, they have followers, connections, then it's a real uh good data, right?

#### 00:37:43

Yogesh Jaiswal: But when you open the LinkedIn URL, it's not right. Then it's actually a bad data. I mean makes no sense. What will you do with that? If you're reaching out to LinkedIn, the LinkedIn URL is not good. Then the data quality is like bad. Okay. So first thing is LinkedIn URL and the method is going into C. We would be doing that but going into clay checking their followers and connections and then uh understanding it that if it needs correction or not. Okay. Second is emails. right now. Uh see emails are very different when it comes to data quality because you need to understand even if you send an email and they don't respond future they can respond right so you don't have a problem. See emails are not very expensive. The tool cost is 7,000 rupees a month right you can send one lakh emails in a month with that tool. Okay. and uh you can work on 5,000 uh contacts like very easily.

#### 00:38:43

Yogesh Jaiswal: So for a company a cost like 15,000 rupees is nothing. Okay. So they but they want that when they send an email the email should get go to them. Okay. So uh before we even send an email, they want every email to be delivered. Okay, bounce rate should not be high. Okay, uh that's why we do email verification. Okay, so I'll show you something. Uh enrichly. Yes. Okay. There is a tool called enrichly and we would be using this a lot. um enrichly validates the email if it's verified or not. Okay. So, can you see this? This is how it verifies verified. Okay. But yes, so can you see email verified deliverable catch all safe and verified. Okay. There are multiple parameters to how we verify an email. Do you understand what is catch all or have you heard of this term uh before no okay I'll show you something so that you get an idea um yes okay if you go into this is a real sheet If you go into this email, we have emails.

#### 00:40:26

Yogesh Jaiswal: Okay. And this is done by Enrichly. So for every email, we have an understanding that if it's a catch all email, valid email. Okay. There is one more thing called valid catch all. Okay. Okay. First of all, valid email is a valid email. Okay. If you send email to this, they would see and they would it would deliver. Okay. Okay, it would not bounce. Now a catch all valid there are two things. Okay, I'll write it here. Catch all and a valid catch all. Okay. So when you send emails even you can send it to a valid catch all. Catch all means this is catching the emails. Okay. And it's delivering right? Catch all catch all you should not send. Okay. It means this person is catching the emails but it's not going anywhere. It's only catching. Right. I'll give you an example.

#### 00:41:39

Yogesh Jaiswal: If Nirj Sujan works in Razer Pay and he left right now when you send email to him it will again land. Right? But he will not respond because now it's not working. But his email id is active. Okay? These kind of email ids are catch all. Right? Now if Neeraj Sujan works in Razerpay with the email id ners.sujenraerpay.com for some reason the email id has changed now to n.sraerpay.com. Okay that means when I send email to nujen.com it's going to deliver and it's going to redirect to your new ID. Okay, these kind of emails are valid catchall. That means totally fine if you want to send emails to valid catch all but don't send to catch all. Okay. Yes. There are several more parameters. Let's go back here. Okay. Now you get three kind of information for the email. If it's valid, invalid email, uh catch all email and valid catch all email. Now you have another parameter which is deliverable and undeliverable.

#### 00:42:51

Yogesh Jaiswal: Okay. This parameter is different. And this is different. Okay. Now I'll show you one more tool so you get an idea. Okay. So this is a tool called bounce and it will just going to give you two information deliverable or not deliverable. Okay. It's not going to give you information like catch all or valid catch all. It is just going to give you that if you can deliver email to this or not deliver email. Okay. Can you see this more deliverable or undeliverable people? Okay. So, uh we in GTM engineering we use at least two or three verification tools. Okay. We don't rely on one. So, bounce band will give us the information that if it's delivered or not delivered before even we send. Okay. So, can you see this? This is what I was talking about. Not all catch alls are risky. Okay. So even though in enrichly it is catch all but bounce band can say that it's a deliverable email.

#### 00:43:54

Yogesh Jaiswal: Okay that's why we need need to use two. Okay there's one more thing called million verifier. Okay and I know you might have heard of zero bounce also but it's expensive that's why we don't use it. So million verifier also verifies it. Okay. the these three things do the same thing. Uh enrichly, bounce by a million verifier. Okay. So can you see verify new emails, block emails and clean the old emails. Okay. Now in GTM engineering, we are going to build a formula where the email get verified by all these three parameters and we get a single output outreach or not outreach. Okay. This is what we're going to do in clay. Right. Uh any questions in email verification? Okay. Uh I just want to understand what you understand by this column. So Whenever we use a email verification service, we also get a column called MX domain. What do you understand by this? When you see this Okay.

#### 00:45:38

Yogesh Jaiswal: Uh yeah. So yeah, I'll tell you what it is. No worries. See, MX domain is the DNS information which gives you uh which gives you an information that what workspace they are using. So air is using google.com right ashray at bluefog is using outlook.com okay again outlook google mail Google these are Google right now when you do email outreach you might also see a thing called mcast okay you cannot send emails to a company which is using Mcast by the way. Okay, this is a cyber security company. So if you see go here, if you just filter Mcast, yes, we cannot send emails to them. They will not land even though if it's valid, these guys will not receive the email. Mycast will have a security parameter. Okay. So there are cyber security companies like Mcast where they prevent any spam emails or anything, right? And this is very popular in Europe. So if you can see, can you see this? Email collaboration and thread protection.

#### 00:47:16

Yogesh Jaiswal: Okay. Okay. Let's go back. So whenever you do email outreach it's very easy for MX domain you need to do Google and Google email and you would send emails from a Gmail account to these guys and most of the people will use Gmail okay so this is would be this through this is should be through Gmail and if you see outlook this should be through an outlook account that's why when you do email outreach you purchase 80% account from Google 20% from outlook Good. Any questions? So if I remove Google and outlook right now what we should do with this right very easy don't send emails to these people you have my car PP hosted your emails will not land here can you see this mailspamproction.com Okay, these are the services companies are using and mcast is again the leader of it. But um if you send an email to these guys, your all of the emails that you send is waste and can you see how many are these? Okay. So whenever we talk about data quality understand that if you export a list of thousand records you can only work on 600. 100 will go that we don't have an email.

#### 00:48:58

Yogesh Jaiswal: 100 will go invalid email. 100 will go uh of mcast and all of these things and another 100 will go because of uh maybe improper information. Name is different, company name is different, right? So we whenever we do email outreach, we don't work on 100% data, right? We only work on the 80% data. Okay? uh sorry 60% because rest data would be going into waste. Okay. Also to mention the reason we keep data clean is there is a thing called super. Okay. Have you heard of this thing called superbase? Okay.

Neeraj Sujan: Yes.

Yogesh Jaiswal: Uh okay.

Neeraj Sujan: Yes.

Yogesh Jaiswal: Uh good. So uh when it comes to GTM engineering we store all of the data in superbase right uh if you work in an agency everything that they do would be stored in a superbase okay uh and uh this is just to reuse data again and again so today if I export thousand records and if I monthly if every day I'm exporting thousand records in a month I have um 30,000 records right now I don't want to again enrich 30,000 records again next month if I keep using this.

#### 00:50:26

Yogesh Jaiswal: So I store everything in superbase and then I would have an API of superbase connected to claude. I'll just type a prompt and get it back. Okay. Or if I want to push to her or something. Okay. So yes, got it. So if I ask you a question why we don't send emails to Mcast what how would you Is it?

Neeraj Sujan: Hey, Perfect.

Yogesh Jaiswal: Uh if I ask you this question that uh why do we don't send emails to Mcast like how would you go about it?

Neeraj Sujan: Oh, not sure.

Yogesh Jaiswal: Okay. Mmcast a security gateway uh which company uses and this is cyber security company. So they block all of the emails uh spam emails right. So we are actually spamming them when we reach out to them, right? So that's why we don't reach out.

Neeraj Sujan: Okay. Little bit.

Yogesh Jaiswal: Yes. Uh okay. Now you need to do something, right? Um you need to create a list of Yeah, I'll just share my screen again because we would be pushing this data to clay now.

#### 00:51:54

Yogesh Jaiswal: Uh yes, I'll show you. So you need to create a list of 50 accounts. Okay. Only accounts, companies, right? Where it is? Yeah. Okay. So just to mention that you might have several doubts. It it's going to be cleared in clay because clay have everything uh happening like you can visually see data quality, you can visually see wrong personas and everything. Okay. So you need to create a list of 50 accounts right from the company you have selected. So you you have Apollo which have 75 credits for free. Prospio gives you 100 credits for free. Uh even AIR gives you uh some credits for free. So you just need to go to Apollo, Prosperior, AI or any other tool and just get top 50 accounts that you are going to uh send uh sell from your company. Okay, which you have selected and that data will be moved to clay and we would perform everything in clay. Okay. So, just be very clear that these should be top 50 companies that you can sell into and we just want few information.

#### 00:53:10

Yogesh Jaiswal: Company name, company uh LinkedIn URL, company domain. That's it. I mean, if you get more information that's totally fine. Okay. Is it is it clear?

Neeraj Sujan: Yes. Yes.

Yogesh Jaiswal: Okay. Good.

Rithika Murthy: So this is a company level search right not uh person

Yogesh Jaiswal: Yes. Yes. Yes. If you see account target list, it's not people account list.

Rithika Murthy: Okay.

Yogesh Jaiswal: Okay. We would search people and play itself.

Rithika Murthy: Okay.

Yogesh Jaiswal: Yeah. So the goal is to understand and just don't consider this is a very easy task. The task is you need to find top 50 companies or accounts that you can sell. Okay. if you are working in that company as a GTM engineer right so every there should be a meaning behind those 50 companies you're selecting okay and just create a list of company name company domain and company LinkedIn URL very easy uh or maybe I'll show you okay yes go to companies here Okay, just select a company like I'll select.

#### 00:54:34

Yogesh Jaiswal: Okay, just select companies like this and export it. Okay, and you have 100 credits in crosspio. So it's very easy to export. Okay, so try to export two exports of 50/50 20 or 25 that would be 50. Okay. uh you can even export more that's not a problem but you should filter here according to the right companies that you can sell it to okay and also uh tomorrow we are going to log into clay so clay would give you all of the clarity I mean I understand at this point every information is more theoretical uh that's why we are you know like we might go hay wire sometimes but in clay it becomes neat and clean. Okay, cool. Uh any questions? Anything with what we discussed?

sampath vemulapati: Uh you wish one last doubt like can you repeat the export once again because I am actually

Yogesh Jaiswal: Yeah.

sampath vemulapati: not done.

Yogesh Jaiswal: Uh so you need to export a list of 50 accounts. Okay. 50 accounts which are 50 companies.

#### 00:55:57

Yogesh Jaiswal: Now this is for the company you have selected. So if you have selected Goji AI, if you are selling Goji AI, what are the top 50 companies you can sell to in the market?

sampath vemulapati: Got

Yogesh Jaiswal: It can be any company, right?

sampath vemulapati: it.

Yogesh Jaiswal: So you have to filter those companies here.

sampath vemulapati: Got it.

Yogesh Jaiswal: Okay?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Employee count let's say 20 under 50 whatever it is. And just go here and select 25. Okay. And you can export. Click here and it will get exported. Okay.

sampath vemulapati: Understood. Yeah.

Yogesh Jaiswal: Then go to next page and then export again.

sampath vemulapati: Okay.

Yogesh Jaiswal: So you have you have two sheets.

sampath vemulapati: Sure.

Yogesh Jaiswal: Just go into Google sheet and create one sheet. Okay. Export like this. Okay.

sampath vemulapati: This is something we could do from Prospio and uh any other platform as well. Apollo also,

Yogesh Jaiswal: Yeah.

sampath vemulapati: right?

Yogesh Jaiswal: Anything. Uh, by the way, when you need to download uh accounts or companies,

#### 00:56:54

sampath vemulapati: Got

Yogesh Jaiswal: you can use any platform. It's not a big deal like every platform have a good company data.

sampath vemulapati: it.

Yogesh Jaiswal: Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: But yeah, it's it's totally free. You can just log in through your Gmail account and you can do it.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay. But still if you have any trouble just let me know.

sampath vemulapati: Sure.

Yogesh Jaiswal: Okay. Uh also are we completely clear with data quality? Uh we clear with catch all valid catch all everything. Okay, no worries. I'll send you some documents of catch all valid catch all and all of these things. You will get more understanding about what I'm talking about. Okay, and how everything works. So cool. I think just get that list ready and uh let's perform real things. Um and let's keep this going. Okay, cool guys. Uh this is it for today. Uh let's connect tomorrow.

Neeraj Sujan: Thank you.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Thank you.

Shubham Gosavi: Thanks.

#### Transcription ended after 01:10:10

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.