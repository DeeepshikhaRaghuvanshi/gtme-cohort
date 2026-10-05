# D03+D04_ The seven-layer mental model + Stand up your workspace - 2026_09_08 08_57 IST - Notes by Gemini


## ✍️ Quick notes

### D03+D04: The seven-layer mental model + Stand up your workspace

Sep 8, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal ganesh.angal1995@gmail.com Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Framework introduction for go to market engineering via data pipelines and automation.

Data Sourcing Strategies

Modern GTM engineering requires utilizing at least 3 data providers rather than relying on a single source.

Apollo offers high data accuracy but lags during heavy filtering; Prospio is preferred for superior speed and filtration.

Visa and EVA Board are essential for exporting leads from Sales Navigator.

Enrichment and Waterfall Methodology

Waterfalls must start with lower-cost providers to minimize credit consumption across high-volume rows.

Google should be positioned low in domain-finding waterfalls as it acts as a search platform rather than a proprietary provider.

Clay serves as the primary hub for managing native integrations and centralizing waterfall logic.

Signals, Intents, and Orchestration

Signals represent global events, such as funding or hiring; Intents represent behavioral triggers, such as website visits.

RB2B is recommended for capturing website visitor data to build actionable automation.

n8n is the preferred platform for building seamless orchestration guardrails.

Execution Channels and Infrastructure

Email outreach success is derived from 80% infrastructure (SPF, DKIM, DMARC) and 20% copywriting.

Her Reach is currently the top-performing LinkedIn automation tool; Dripify is noted for a superior UI.

SmartLead is optimal for high-volume email outreach, whereas Email Bison targets response-focused strategies.

CRM and Agentic AI

Atio is recommended as a specialized CRM for GTM engineering workflows compared to Salesforce or HubSpot.

Master foundational skills like waterfalls before attempting to build expensive, complex agentic AI workflows.

DeepLine is being explored as a cost-effective, API-based alternative to Clay.

Portfolio Development and Environment

GTM engineering exercises focus on YC startups to demonstrate scalability and rapid growth capabilities.

Maintaining a separate browser workspace with a clean Gmail account is necessary to manage credentials and avoid access restrictions.

Next steps

[The group] Create Workspace: Set up a new Chrome workspace with a dedicated Gmail account to perform GTM engineering tasks.

[The group] Register Tools: Sign up for all data and GTM engineering platforms listed on WhatsApp.

[The group] Organize Bookmarks: Create a bookmarks bar in the new browser workspace for all required GTM engineering tools.

[The group] Select Portfolio Company: Choose a target entity from the YC startup directory for GTM engineering exercises.

[Yogesh Jaiswal] Share Resources: Send the list of tool websites and GTM agency pages to the WhatsApp group.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📝 Full notes

Sep 8, 2026

### D03+D04: The seven-layer mental model + Stand up your workspace

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal ganesh.angal1995@gmail.com Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D03+D04: The seven-layer mental model + Stand up your workspace

Meeting records Transcript Recording

#### Summary

Framework introduction for go to market engineering via data pipelines and automation.

GTM Engineering Overview
Introduction of framework layers to automate manual work and improve outreach efficiency.

Data and Waterfalls
Utilization of multiple data providers and stacked email finder tools for cost efficiency.

Automation and AI
Deployment of orchestration tools and infrastructure management alongside agentic artificial intelligence.

#### Next steps

[The group] Create Workspace: Set up a new Chrome workspace with a dedicated Gmail account to perform GTM engineering tasks.

[The group] Register Tools: Sign up for all data and GTM engineering platforms listed on WhatsApp.

[The group] Organize Bookmarks: Create a bookmarks bar in the new browser workspace for all required GTM engineering tools.

[The group] Select Portfolio Company: Choose a target entity from the YC startup directory for GTM engineering exercises.

[Yogesh Jaiswal] Share Resources: Send the list of tool websites and GTM agency pages to the WhatsApp group.

#### Details

GTM Engineering Overview: Yogesh Jaiswal introduced the framework for Go-to-Market (GTM) engineering, describing it as a series of connected layers including data and sourcing, enrichment, signals, orchestration, execution, CRM, and agentic AI (00:02:50). The primary goal of this engineering approach is to automate manual work, remove reliance on traditional sales roles, and improve outreach efficiency (00:21:57).

Data and Sourcing: Yogesh Jaiswal emphasized that the foundation of GTM engineering is accurate data, noting that successful agencies typically rely on at least three data providers rather than one (00:05:35). Apollo is highlighted for general data quality, while Prospio is favored for its speed during heavy filtration processes (00:06:51). For extracting leads from Sales Navigator, Yogesh Jaiswal recommended using tools such as Visa or Evaboot (00:09:48).

Data Enrichment Process: Yogesh Jaiswal explained that enrichment is essential for cleaning and validating data, often using the tool Clay. This process involves taking raw data downloads, such as lists from Apollo, and filling in missing parameters like LinkedIn URLs, email IDs, and professional details to ensure proper data hygiene before outreach (00:11:24).

Email and Domain Waterfalls: Yogesh Jaiswal and Gagan Bhaisa discussed the concept of "waterfalls," a method of stacking multiple email finder tools to maximize success rates (00:13:41). Yogesh Jaiswal advised prioritizing providers by cost to save credits, noting that efficient GTM engineers avoid starting with expensive tools when cheaper options are available (00:16:18). Rithika Murthy added that this approach involves stacking email finders based on credit usage to prioritize the most effective and cost-efficient tools (00:14:54).

Company Domain Waterfalls: Yogesh Jaiswal cautioned that creating a waterfall for finding company domains requires a specific hierarchy to avoid errors. They advised placing Google lower in the waterfall list, as it is a search platform rather than a data provider and can hallucinate or return advertisements instead of accurate website information (00:19:50).

Signals versus Intents: Shubham Gosavi and Yogesh Jaiswal differentiated between signals and intents. A signal is global information, such as a company hiring or raising funds, while an intent is a specific trigger based on an interaction, such as visiting a website or liking a LinkedIn post (00:21:57) (00:24:33). Yogesh Jaiswal mentioned tools like RB2B for website visitor tracking and Trigify for monitoring LinkedIn activity to craft timely, automated outreach messages (00:25:30).

Orchestration via N8N: Yogesh Jaiswal identified N8N as the primary tool for orchestration, which connects different systems to create seamless workflows (00:28:13). Unlike other methods, N8N allows users to build complex guardrails, such as conditional logic with true or false paths, making automation more efficient for clients (00:29:25).

LinkedIn Automation Tools: Yogesh Jaiswal reviewed various tools for LinkedIn automation, noting that Herreach currently performs best for agencies, while Dripify is recommended for users needing a better interface with fewer accounts (00:29:25). Lemlist is useful for combining email and LinkedIn campaigns, and Phantombuster was also noted as a popular option for LinkedIn tasks (00:31:10).

Email Outreach Tools: Yogesh Jaiswal categorized email tools based on scale and purpose (00:33:31). Instantly is suggested for smaller use cases with fewer emails, while Smartlead is preferred for extensive outreach requiring thousands of emails per month (00:32:17). For high-level, sophisticated outreach focusing on infrastructure and high response rates, Email Bison is recommended, although it is a paid-only tool costing approximately $600 (00:33:31).

Email Infrastructure Management: Gagan Bhaisa and Deepshikha asked for clarification on email infrastructure, which Yogesh Jaiswal described as representing 80% of the work in GTM engineering. This involves configuring technical compliances like SPF, DKIM, and DMARC when connecting email accounts from providers like GoDaddy, Google, or Microsoft to outreach tools (00:36:09). Proper infrastructure is critical to ensure emails reach the recipient's inbox rather than the spam folder (00:37:31).

CRM Integration and Data Hygiene: Yogesh Jaiswal discussed the role of CRMs like HubSpot, Salesforce, PipeDrive, and Atio in GTM engineering (00:37:31). Atio is described as well-suited for GTM engineering, while Salesforce may require specialized developers due to its complex SOQL language (00:39:57). Yogesh Jaiswal noted that Clay features native integrations with these CRMs, allowing GTM engineers to handle CRM-related tasks directly within the Clay platform (00:41:23).

Role of Agentic AI: Yogesh Jaiswal explained that agentic AI represents an advanced step in GTM engineering, currently used primarily by enterprise companies with significant budgets (00:42:34). These agents are distinct from simple automations because they can train themselves based on outcomes (00:44:01). GTM engineers are expected to build these agents for smaller companies that need to scale quickly (00:42:34).

Workspace Setup and Portfolio Building: To prepare for upcoming sessions, Yogesh Jaiswal instructed the team to create a new Chrome workspace and a dedicated Gmail ID. Participants must sign up for various tools discussed during the meeting to build muscle memory (00:45:51). Additionally, the team is tasked with selecting a company from the YC startup directory to use for their GTM engineering portfolio, which will include strategy documents and demonstration videos (00:49:25).

DeepLine as a Clay Alternative: Gagan Bhaisa and Yogesh Jaiswal discussed DeepLine, a tool that functions as an API to connect data providers (00:52:11) (00:56:07). Yogesh Jaiswal noted that while Clay is powerful, its cost can be prohibitive, whereas DeepLine offers a more cost-effective alternative for building waterfalls by connecting directly to Claude Code (00:54:40). The team plans to incorporate DeepLine practice into future sessions (00:52:11) (00:56:07).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 8, 2026

### D03+D04: The seven-layer mental model + Stand up your workspace - Transcript

#### 00:02:50

Deepshikha: Hello everyone. Good morning.

Rithika Murthy: Hey. Hi. Good morning.

Deepshikha: Uhoh.

Yogesh Jaiswal: It's Cool. Uh so meanwhile people are joining people who have joined I want to mention something that we are going to cover this. So um GTM engineering is divided into several parameters. we call it as a uh mental model but uh these are the areas we are going to go one by one. Uh these are also the layers. So every layer is connected to each other. The layer goes one by one. You we yeah we would start from data and sourcing enrichment signals orchestration execution CRM and agentic uh AI. We'll just wait for a couple of people more people to join. Anyone here used Apollo Prospio like AI? Have you used it? Ocean disco.

Alok: No.

Yogesh Jaiswal: Okay. Okay. So, we can start. I think this is good. We have enough people. Uh okay. So first is data and sourcing right.

#### 00:05:35

Yogesh Jaiswal: So GTM in GTM engineering a big big problem that we are aiming to solve is clarity of data. Any company out there selling into any market their main concern is are they reaching out to all of the people that are available uh or their ICPS or not. So before GTM engineering like if you talk a year back companies were only relying on one data provider. It was either Apollo or Zoom Info or Prospio or or maybe just one data provider. Today any GTM engineering agency or any GTM engineer would rely on at least three data providers. Okay, they would never rely on one data provider. They would always have at least three data providers. Now there is a small um there is a small catch here that sales navigator is also there but sales navigator is not a data provider right sales navigator is a okay it's it's basically an area or it's a platform where you can get all of the data you can filter it but sales navigator will not give you a possibility to just fetch that data easily okay so I'll start showing you everything here.

#### 00:06:51

Yogesh Jaiswal: Okay. Starting from Apollo. So we have Apollo which is the most like the oldest platform in terms of data and uh Apollo is also I mean so if if you are using a data provider and you don't want to like um you you don't want to settle down for the less Apollo is the is the top one right now. I mean it would have every kind of data. Um the quality is also very good. Now you have Prospio. Prospio is where you you know this is for modern companies where you have a lot of filteration, lot of uh when you do a lot of filtering. Okay. The reason Apollo and Prospio are different is um okay Apollo is good in terms of data quality and in terms of the data accuracy but when you do a lot of filtrations in Apollo and we would be doing that live in in in reality but when you do a lot of filtration in Apollo like selecting the company filter selecting the uh funding filter Apollo lags a bit uh a bit right So, Prospio is a modern CRM that doesn't lag.

#### 00:08:05

Yogesh Jaiswal: Okay, it works perfectly when it comes to doing filtration and it's also very fast. So, if you wanted to go download the data from Apollo, it you might put in 10 minutes to download the data. Everything it's like so u everything takes time. Prosped yesterday. uh AI is again it takes time to download the data uh but filteration is much better than prospio and uh also the data accuracy is not very good uh just want to mention that there are several industries where a is uh is really bad when it comes to insurance industry when it comes to uh automotive industry I is also good For modern data like technical data or people or more of a core technical data or um you know selling to modern companies. uh this is where a is having a leverage right now again moving back to we have ocean for the uh for the lookalike companies then we have disco for the disco like for the yeah disco for the local companies right now this is the data okay now data and sourcing is just a okay data sourcing is just it I mean it looks easy to you that it's it's a very easy thing to just go out and grab data and you know export it.

#### 00:09:48

Yogesh Jaiswal: I just want I just want to mention that nine out of 10 people make a mistake here. if they start executing GTM engineering the foundation is data everything revolves around the data that you fetch and if in this part if you are wrong then uh the whole thing that you do is like doesn't make any sense so that's why um whenever you get a GTM engineering problem data and sourcing should be checked everywhere I mean in every tool that you have rather than just jumping in one tool okay also to mention one thing that sales navigator is only possible by yeah okay sales navigator is only possible by visa this is a tool which is used to export sales navigator leads and uh so you open sales navigator and you have to have visa to download data from sales navigator so sales navigator will not have uh uh you know just give you data like that right so you need visa for that okay visa Again uh one of the tool there are more tools out there but um sales navigator export is only possible by visa but you can have more tool more tools sales yes so you can see yes you have eva boat also this is again very popular but exa is uh sorry visa is uh the most popular one but even this one evabol is also very popular so two tools.

#### 00:11:24

Yogesh Jaiswal: If you ask me to export data from sales navigator, the two top tools are Visa and EVA board. Okay, we would be uh again going up into that. But now enrichment, this part is the reason where uh clay came in. So before GTM engineering, this part was handled by a team of revops engineers, sales engineers, uh data engineers. Now only one person can even handle entire enrichment. Enrichment means when you download data from Apollo. Okay, let's say you download a data of 100 people from Apollo. You might have 70 emails, you might have uh improper information that is not even validated and you might miss out a lot of things. Now you okay if I give you an option to download a list of all the CTO's based out of uh Germany. So you might download a set of people from Apollo which is can which can be 100 people. You might download more people from Prospio which can be again 150 people. So you need a place where you can gather all of the data that you are bring exporting and to clean it.

#### 00:12:37

Yogesh Jaiswal: Enrichment is where you get get all the data. Okay. I can even show you how it looks like. Okay. So yes. Okay. This is just a sample sheet. So this is what enrichment looks like. Okay. I have a LinkedIn URL but then I enrich person. Now I enrich the person. I get full name, job title, LinkedIn connection, follower, headline, company parameters, company name, company domain, person location and other things, right? Yes. So enrichment is where you need clay to fill out all of the missing data. Now from an email point of view, so okay, from an outreach point of view, you need two things. LinkedIn URL and L email id. So these are the top parameters to do the enrichment. Then you also verify the email. Okay. Then there is text stack. There is lot of lot of enrichment. It's possible uh when it comes to enriching the data. Right.

#### 00:13:41

Yogesh Jaiswal: Now you have uh waterfall. I just want to ask does anyone are you guys clear with what is waterfall or you want me to explain? Anyone know what is waterfall here? Yes. Yes. Uh yes, Gagan. So uh uh can we can we directly talk about an email waterfall? Now I need to find email id. How would a waterfall looks like? Gagan and then Rithika can go ahead.

Gagan Bhaisa: Yeah. So what I do, my approach is basically I connected different systems. Uh so when I say uh let's say prospinder uh can be another tools like visa uh and

Yogesh Jaiswal: What the

Gagan Bhaisa: then basically layer them. So what I trying to say let's say if one falls the second would take second false the third would take third if third would fall then it automatically goes to fallbackation when it

Yogesh Jaiswal: heat?

Gagan Bhaisa: goes uh try to find on web scrapers. So yes,

Yogesh Jaiswal: Yes.

Gagan Bhaisa: I think this is what I understood.

#### 00:14:54

Yogesh Jaiswal: Yes. Yes. This is correct. We need to add one security layer also that I'm going to show you um how to safely use waterfall to make sure that we don't consume a lot of credits but this is good. Yeah. Yes.

Rithika Murthy: Uh yeah, I think Gagan pretty much covered it, but to sum it up, essentially you stack up a couple of email finders and um based on the credits that they use, you um you know prioritize it and um it goes through each tool and tries to find the right email. If one of it fails, it goes the next one. And uh that's how wonderful enrichment works.

Yogesh Jaiswal: Yes, that's right. Uh that's completely right. In GTM engineering, uh we just want to be careful. Okay. Because okay, every tool is unique. Every tool consumes different kind of credits. Their plans are different. Okay. So one thing I want to mention that uh waterfall is for when we talk about waterfall as GTM engineers we would refer to two things either a waterfall in clay or either a waterfall in clay uh clot code right generally it would be in clay only because uh clay have native integration with these providers.

#### 00:16:18

Yogesh Jaiswal: So there are so many providers and we cannot purchase everything right. So this is a problem where we only need we can only solve with clay because clay have every tool native integration. Right? Now if I ask you to run a waterfall like this right and if I show this waterfall a question is do you think this waterfall looks perfect to you? Do you think this is perfect or uh what can I do to make this perfect? this waterfall.

Gagan Bhaisa: So technically what you can do uh so let's say you want to find on specific

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: industry and you know where you can find the data you can basically shuffle them up down to make sure like let's say hunter gives you a correct data 90% then you goes to below data proc then you go to visa then you go to ICPS so yeah that's how you can manage those

Yogesh Jaiswal: Yes. But from a money point of view, from a financial point of view, uh because Prospio is expensive, find my email is also expensive.

#### 00:17:29

Yogesh Jaiswal: So, okay, I'll I'll show you. Uh many people what they do is they run waterfall. Uh I mean, Gagan as you know technicalities of these things, but there are people who just run waterfall like this.

Gagan Bhaisa: Yeah. Yeah.

Yogesh Jaiswal: They would they would go here.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: They would do this and run it. Right?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Now you need to understand that if you go into waterfall you have this which consumes six credit. Right? And by the way this is expensive everywhere. Smarty. Okay. So waterfall there is A um okay there is a way to create any waterfall right you need to push in you need to start from the providers which charge you low okay so you can see 0.5 credits right then one credit then one credit okay then one credit then two credit 6 credit okay this is the first step to understand waterfall properly that whenever there is a waterfall you need to only Start with you need to start with the providers which are charging you less.

#### 00:18:36

Yogesh Jaiswal: Okay. Now what if ICPS give me the email and uh I I only consume uh 0.5 credits. But if this was the waterfall okay it will start from Visa. makes no sense for me like I'm getting the same email which I'm getting u and now I have consume two credits and the problem with GTM engineering is it's not one row you have thousands of rows to work on uh so let's say if I want to find email of thousand uh leads visa consumes 2,000 credits and ICPS consumes 500 credits 1,500 credits I could have saved if I my waterfall was correct Okay. So, this is a parameter that we need to make sure it's correct. Uh, we have more waterfalls I want to show you. And, uh, for now I'm sticking to clay, but we would have more um, uh, we would have more waterfall uh, discussions in plot code as well. So, let's say I talk about waterfall. Okay. You have a yes, you have a Facebook waterfall, you have a CRM waterfall.

#### 00:19:50

Yogesh Jaiswal: Okay. One more waterfall we do use is finding a company domain. Okay. Yeah. This waterfall is um I mean again people make a lot of mistake here. So when we find okay email finding waterfall is finding an email right there is a company domain waterfall because in GTM engineering you will you come across lot of parameters where you don't have a company domain right now. This waterfall looks easy like you can just put Google up uh snow view. You can put this up and like this right. But there is a problem here that when you do a waterfall of company domain with Google uh and finding a company domain, Google will just search and give you the first uh the first website. Right? It's advisable that in this waterfall of company domain, Google should be here rather than at the top because Google is not a provider, right? It's a search platform. So if someone is doing a paid marketing and if their brands comes up uh Google can Google can hallucinate there.

#### 00:21:02

Yogesh Jaiswal: Okay. So, this is how and this is a company domain waterfall. Okay. I would show you more things. Okay. You have a mobile phone waterfall. This is very popular if you sell to India. Okay. This is by the way really big also. You can see you have so many providers. Okay. This is also used when you work with American companies and when they um when they do events and stuff. Um yeah. So you need to find emails but you need to find or you need to find phone numbers but you need to only find numbers of very like few people. Okay. So you can see that phone number you have lot of options. Okay. Yeah. You have again a Latin America uh mobile phone waterfall. Okay. For now we are just sticking to clay but we have we can build our own waterfall also uh in N10 or cloud code. Okay.

#### 00:21:57

Yogesh Jaiswal: So this is waterfall. Let's go back. Now you have signals and intents um as the next step. So can you do you uh like are you trying to understand? We get the data, we enrich the data and then we make the data like we just optimize the data to make sure we get more responses. Okay. So does anyone here would like to speak on what's the difference between a signal and an intent? Like what do you understand?

Shubham Gosavi: See signal is basically let's say if they are hiring then that could be a signal for us and intent is something if they went on our website and was exploring something then that could be identified as the intent that means that they are looking for inside.

Yogesh Jaiswal: Yes, correct. Um, okay. This is one parameter. A second parameter for Okay, this is one example. A important reason why we talk more about signal and intent is in GTM engineering because GTM engineering is also to um it's also happening to remove sales people product like remove sales people and uh automate the manual work.

#### 00:23:21

Yogesh Jaiswal: So see in GTM the two top channels are emails and LinkedIn right and uh emails and LinkedIn works the best when you you show something relevant you make a humanistic email okay signals and intents are um just to make sure that even though your channel that you're using is least responsive because if I do a phone call it's more responsive but when I do a email or LinkedIn It's not that kind of not that responsive as compared to my top channel. Signals and intent will make sure that the channel is performing good. Okay. So signals signals would be global signal. Signals are always global. Okay. So, any company raising funds, any company, okay, let's say if you're selling a CRM, you saw a company raise funds, uh the company is also hiring for salespeople or marketing people and uh they also hired a new chief sales officer and uh so that can be a signal for you. Okay, signals means you can catch signal anywhere. Okay, I mean without going deep diving into the company, right?

#### 00:24:33

Yogesh Jaiswal: Intent is a trigger in easy words. Okay. Now if Shubam I want to sell you something and I saw your company have raised $1 million. Okay. Now I got that signal and I given I have given a LinkedIn DM to you. Hi uh Shubham. I saw that your company raised $1 million. I want to congratulate you. Right. Uh and then after uh after talking to you, after connecting to you, I then post something on LinkedIn that I just connected with this. I connected with Shubham. We exchanged a conversation and the company has raised $1 million and I'm I genuinely you are doing a great job. Not like that, but I app let's say I appreciate your company in a LinkedIn post and you like my post. Okay. The moment you like my post, that is a intent for me. Okay. Or a trigger for me. Okay. And uh let's say someone from your team visits my website.

#### 00:25:30

Yogesh Jaiswal: Okay. And they are visiting my landing page again and again. Okay. So that those are intent and intent is where we convert it into a trigger. Okay. I want to show you something. Yes. Okay. Uh right now the top intent we prefer is uh website visitor uh analysis and uh this is where we I mean this is where we generally focus on uh getting a okay let I'll login in later but yes okay so uh yes anyone visits your website is the top intent right now that we can capture and build an automation around in GTM engineering okay Uh RB2B is again leading it because RB2B captures the website visitor and you can build an automation around it. Yes. Uh yeah. Also there is one more thing. Yeah. There is one more thing called trigify. Yeah. Yes. So triggery is also uh a tool that can use to catch triggers and signals and uh this this is very LinkedIn heavy signals.

#### 00:26:47

Yogesh Jaiswal: Okay. So if let's say Gagan posts something about uh AI in his company and how they're adopting AI and uh I want to automate my outreach to Gagan so I can craft a message. depending on Gagun's activity on LinkedIn and the message and my connection request would be hi Gagan I saw your recent post regarding this and you're pretty active talking uh about the AI topic right and uh then you can craft something so trigify is again a top uh choice when it comes to LinkedIn signals and triggers Okay. Yes. Uh any questions between signals and triggers or intents? Okay. Uh just to mention trigger is the next step of intent. So intent is an activity that we use to trigger something. Okay. If I visit an I if I visit a cyber security event in Europe, okay, and uh I am a chief technical officer at a company in Bangalore, there is a reason I visiting that event in Europe, right? Because I'm concerned about my security. Okay.

#### 00:28:13

Yogesh Jaiswal: If after that a cyber security company contacts me and say that hi Yogesh, I saw you visited the event. um just want to check are you also looking out for cyber security services or what was the reason you visiting there as a tech chief technical officer. So intent is closely related to a trigger. Okay. Signal is just information that you keep to uh uh you keep to build a knowledge base. Okay. Now orchestration right? uh mostly I would also want to give you a heads up that this part is enough for you to do outbound. Okay, you just need to add another layer here of execution. Orchestration is where you talk about doing things in a more seamless and a more um how do I say in a in a seamless and a more efficient way. Okay. Again, NAN is the top. Yeah, N is the top match when it comes to doing um orchestration. Okay. Uh guess it's still still opening. Okay.

#### 00:29:25

Yogesh Jaiswal: Yeah. So, Nitan is where orchestration becomes really easy. Okay. So, you can see that uh we are trying to build something here. And uh okay why Niten is different from claude code or claude or doing orchestration? Um okay you can build a skill or you can build something around cloud code but when you build something in n and make.com again n is better than make. So, this runs into a specific uh guard rails that you build around. Okay, you can see the guardrail here is true false. Okay, uh goes to play or goes to slack, right? So um just want to mention that orchestration is only NAN and NAN is a very by the way this automation I have built for a cyber security company based in Europe and uh you can see it's very small but but it was only possible uh through Natan right because it it's much better to build it okay so we we would again we would be learning everything uh about an as well okay so orchestration ution is n yeah now execution right uh yeah let's go here okay execution again has several parameters the top performing parameter is LinkedIn okay and uh for LinkedIn we have her okay her is uh yeah her is performing the best right now because it's automating LinkedIn and u LinkedIn automation is like working the best.

#### 00:31:10

Yogesh Jaiswal: I think it will keep on working the best. Okay. So, you connect your LinkedIn account like that and you build a campaign and uh yeah, you you just go ahead and start reaching out. Okay. Okay. My subscription. Okay. Yeah. So, we would again talk more about her reach. We you all will practice. Okay. Then you have a tool called Ripify. Okay. So see her reach is for a agency point of view right when you have more LinkedIn accounts when you have less or like one LinkedIn account to automate and you need more a better UI dripify is uh working the best. Okay. Dripify is the same thing automating LinkedIn. Okay. Now you have uh Lemlist. Okay. Now LM list is also used for automating LinkedIn but uh yeah but right now uh LM list also do emails. So LM list is a mix of emails plus LinkedIn. Okay, I can even show you.

#### 00:32:17

Yogesh Jaiswal: So yeah, you can see it's an email campaign but yeah if I create a campaign you can see that yeah if I create something yeah you can see that I can even add LinkedIn here you can see here visit profile visit and invitation okay now these are for LinkedIn okay we have one more thing called phantom Um okay there is one more thing called phantom buster. This is also for LinkedIn. Okay. Uh LinkedIn automation and we would be learning everything. Okay. Yeah. Now this is for LinkedIn. Now you have emails. Okay. you when you work with one single company where uh yeah when you work with one single company and you don't have a lot of stuff to do like you just have several emails that you want to use it uh instantly is the best okay I can even show you yeah so you can see that uh this is a real client and uh you just have one client which is hyper analyst and you are building something for them.

#### 00:33:31

Yogesh Jaiswal: Okay, you have same campaigns, inboxes, but again we would be going deep diving into it but right now I just want to give you a basic overview. Yes. So this is uh for small use case. Okay. Instantly then you have smart lead. Smart lead is uh for okay just understand smart lead is for extensive email outreach. Okay. when you send uh thousands of emails in a month or maybe a lack of email in a month, smart lead comes in. Okay, smart lead is also um better at doing things when it comes to email check, email validate, email enrich, lot of other things. Okay, now after smart lead, we have a tool which is if you want to like if you want to be the top 1% which is email bison. Uh many people don't know about this and by the way this is this is a bit difficult to use as well but this is like okay this is for a very extensive email outreach and uh this is highly focused on a response right because in instantane smart lead your goal is to do an outreach and okay uh responses can come or cannot come bison is it's more focused on infrastructure and outreach and eventually reading it uh eventually having good responses.

#### 00:35:02

Yogesh Jaiswal: So, email bison is where um you need to have you you need to like check it check this again. This is uh email bison is very uh like it's impossible to use uh on a free trial because it only operates on a paid version and it's $600. But if you get a chance to work in an agency and if you use email bison you'll understand that this is like the next level of email outreach. Okay the it have a parameter. So send outlook from outlook google from Google and a lot of other things. So yes email bison is there and uh yeah we go back. Okay so execution is done. Now CRM and reporting. Okay. Uh I don't want to complicate CRM here but just want to mention that. Okay. I want to show you something. Yeah. Yeah. Okay.

Gagan Bhaisa: Uh hey guess I think we spoke about uh email infrastructure. are the email delivery is also a part of this uh curriculum activities.

#### 00:36:09

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yes. So, uh right now people who are good in email infrastructure are winning as compared to people who are good in writing emails. So now the demand is for people who can have who can build or manage a good infrastructure. So when we as GTME work with client generally client have 50 emails minimum. So infrastructure is a huge uh parameter like 80% is infrastructure uh 20% is just the copy. Yeah. Okay. uh giving you an example of because see I I I can even show you. Yes. Yes.

Deepshikha: Yeah, Yogesh, can you expand more on the infrastructure part? I didn't actually get it.

Yogesh Jaiswal: Okay. Okay. Infrastructure means um when we set and we would we would have like whole week talking about email infrastructure. So uh we would cover that. Okay. When we purchase a email, it p we purchase it from uh GoDaddy or Google or Microsoft. Okay. Then we connect these emails to the tool which is instantly smart lead email bison.

#### 00:37:31

Yogesh Jaiswal: Then we also have because it's a global channel. Okay. So we need to set up certain uh compliances um or maybe parameters you can say which are SPF, DKIM, DMARK um and then we build the infrastructure so that when Yogesh sends an email to Deepshikha, Deepshikha gets it and opens it. That's the infrastructure. If infrastructure is wrong that Yogesh will keep on sending the email and it will not uh come into your inbox. It will go into your spam. Okay. uh infrastructure is using email at its full potential as a channel. Okay. Yes. Now when we talk about CRM uh just want to mention that you have HubSpot, you have Salesforce, you have uh you have Pipe Drive, you have atio. Okay. Yeah. I would show you at first. Okay. Yeah. Uh yeah. When you talk about GTM engineering, ATIO comes into the play where this is way better than HubSpot and Salesforce only for GTM engineering, right? This is a core GTM engineering based CRM.

#### 00:38:41

Yogesh Jaiswal: Okay. But if you want to know more about Okay. Yeah. Yes. So if you want to know more about what we do and CRM like HubSpot and Salesforce as DTM engineers. So you can open this agency page. I'll sh send it to you. It's revenue hoop. They do only CRM, GTM engineering. Okay. So you can see here right. So the problem statement is um you pick up a company and uh you clean everything and you make sure CRM looks good. And if you are working on ground, you know that any CRM of any company is not super clean and super uh it's always messy. Okay. Uh yeah. So I also want to show you something that uh this agency this this is again based out of US. Um yeah they're doing an amazing work and if you want to understand how what is the role of CRM in GTM engineering. So CRM enrichment prioritization. Okay. You have a lot other things as well.

#### 00:39:57

Yogesh Jaiswal: Yeah. Okay. Yes. Yeah. Yes. So, I'll send it to you across but uh mostly CRM if if you are a GTM engineer and if you have a CRM uh that needs to be super clear and that needs to say everything that you do in GTM engineering. Okay. Yes. Let's go back. Okay. CRM and reporting. Okay. Yeah. You can see here, right? Data hygiene, attribution, HubSpot, Salesforce. Again, um I would not uh urge you to try Salesforce in GTM engineering because Salesforce is you need people who understand Salesforce like Salesforce developers, Salesforce architects. So when it comes to GTM engineering and if a client is using HubSpot then you can't control everything. If they don't if they are not even using a CRM then you can get atio or even you can just have Google sheets doing everything. But if the client is using Salesforce u which is very common in European companies because Europe is very compliant about data and they want on-prem CRM.

#### 00:41:23

Yogesh Jaiswal: So uh Salesforce is where it gets difficult and yeah if I want to show you something here that clay do have native integrations with you can see right HubSpot. Okay you even have with Salesforce. Okay, Salesforce the problem is Salesforce have their own language which is S OQL. Okay, so you need an understanding about it. Okay. Now you even have atio and uh at is also connected in clay. So I think everything is connected into clay. You don't need need to worry about it. Okay. And you even have pipe drive. Okay. Yeah. So pipe drive is also there. So any CRM related work you can do inside clay itself and we would be doing that. Okay. But um if you ask me the first step is to do everything in clay then into claude and others. Okay. So that's why we would only be focused on clay for now. Yes. Then you have agentic. Yeah.

#### 00:42:34

Yogesh Jaiswal: Then you have agentic uh AI and agents. uh I would also suggest that try to uh go here when you are perfect in every place because when you don't even understand how clay works when you don't even understand how a waterfall works and there are thousands of these topics that you need to understand how it works and once you understand everything then the right way is to go towards AI and agents but I also want to show you something that what kind of agents we are talking about. So okay so yes this is the leading company who does that. The problem is building an agent is expensive and uh right now only good like enterprise companies who have a lot of money are using uh AI agents for GTM engineering but there are also small companies who wants to spend less and then GTM engineers like you will come into the picture and build that agent. Okay. So yes this is just a sample uh company or not a sample company this is an example. Okay. So they build a agents GTM agents for uh the top 2000 uh companies global 2000 companies and uh service now uh other companies are using them.

#### 00:44:01

Yogesh Jaiswal: Okay. So if I show you the kind of agents they build okay yeah you can see okay sales intelligence agentic workflows account intelligence. So they are these are not automations these are agentic automations. So if something happens in the agent in the automation they it will also train it okay rather than niten or claw claude skills where they are just a they just a skill right that doesn't train itself themselves. So yes yeah so and they also have per account agent. So when you're reaching out and doing ABM on a per account basis, they also have uh an AI agent. So you can see where the world is heading towards. Um okay. Yes. Uh any questions in this whole thing? Do you understand? understood or uh do you need more details? Any questions? Any doubts? Anyone? Okay, got it. So as a next step um because we have talked about so many tools uh as a next step you need to have you need to understand that yeah sorry yeah you need to understand that when you don't even open these tools you cannot learn these tools and uh every tool we talked about is they have a free trial and they have a uh and they have a free sign up for 15 days or 20 days.

#### 00:45:51

Yogesh Jaiswal: Okay. Um I would show you something email. Yeah, I will send you a Yeah, I'll send you a website where you can get free company emails to sign up these tools because from your personal Gmail ID if you sign up uh you cannot access it. So I would send you a website where you can go ahead and use a sample uh business email uh test email. Okay, I'll give you that. So now as a next step uh okay I can even show you what I'm trying to say. Okay, can you see my screen now? Uh yeah if we leave this can you see instantly clay claude hair reach miro rb2 but can you see this blitz API spot

Deepshikha: Yep.

Yogesh Jaiswal: buffer github google analytics deepline slack loom niten. Okay. So, you need to create a separate workspace like this. Okay. So, you just need to go here uh on uh Chrome and you need to create a new workspace. Okay. You need to create a basically a new uh Gmail ID to perform GTM engineering.

#### 00:47:10

Yogesh Jaiswal: Okay. So, this is going to be a next step for you. And uh I'm going to post some tools on WhatsApp. You need to just sign up for th those tools. Okay. The first tools would be Apollo, Prospio, uh EI and all of the data tools. Okay. So GTM engineers who are proficient in most of the tools can easily enter the market or can easily be valued in the market because every day there are new set of tools coming right and uh you cannot you cannot go back and learn that tool and again because GTM engineering is also more of a non-technical a field for non- tech people. So uh tools would be your uh armor right? Um, so you need to create a new workspace in uh in Chrome and um create a new Gmail ID and I would be posting all of the tools which you need to sign up. You need to sign up and you need to create a yeah and you need to create a bookmark like this.

#### 00:48:18

Yogesh Jaiswal: Okay. Like this hair reach clay claude. Okay. Like that instantly. So you will start from the data tools here. Then again the other tools. Cool. Um yes. Okay. Uh can can it be done by today like everyone before we meet tomorrow? Is it possible? Okay, got it. So yes, this is it for today. Uh I again just want to let you know that we would be going slow in the beginning because uh we don't want to like jump into a topic where we are we don't have clarity about uh but the moment we move to clay which is going to be super soon it becomes more uh more of everyday putting 2 hours kind of activity. We would be going slow because we want to build that slow pace to build a good muscle memory. Okay. Uh also one more thing I just want to give a heads up here itself that we would be doing this entire GTM engineering around the company.

#### 00:49:25

Yogesh Jaiswal: Okay. So yes, you just need to go to this uh yeah, you just need to go to YC startup directory and yeah from the batch. Yeah, you can see fall 26 and summer 26. Okay, you can even select all of the 26 batches. You need to select one company from here because these are the ideal companies to do GTM engineering for. Okay. So you would be doing an entire GTM engineering for this company. Okay, that's our goal to achieve like because you all don't have a portfolio right now. Um and we would be building a portfolio. Uh also the portfolio includes your loom videos, your loom videos using clay, using strategy document, using uh using tools and everything. Okay. So I would be pasting this list and you can select it. Um also I am very open if you want to select a very difficult company. Okay. like uh like this company you can see voice first hardware interface for human agent interaction AI claims investigator for insurance.

#### 00:50:48

Yogesh Jaiswal: Okay. So just want also want to want you to uh give this information that today GTM engineering is only for very hardcore AI native companies. A company like Zoho will not be focused on GTM engineering right now. Okay, they would focused on automations but not GTM engineering. So um any company new in the market wants to scale quickly is ideal company for GTM engineering. Okay. And YC is they pay like uh 4 cr rupees and these companies only have two three people. So at this point these companies would not hire a lot of salespeople. they would only get people who are can control everything right now. Okay. So do select the company, keep it ready and we can uh go ahead with that tomorrow. Okay. Yes. Uh any questions anyone? Okay. Yes. I also meanwhile we close this. I also want to show you something. Uh yeah. Okay. There is this new tool.

#### 00:52:11

Yogesh Jaiswal: Uh I mean even though Oh, sorry. I would sh Yeah. There is this new thing called deep line which is eliminating clay. And by the way in the previous batch we have done everything without clay. Um today if you have clawed code with you um try using deepline um and I can give you an access as well. I have a yeah I have a free access uh for deepline um the founder gave us. So try using deepline um or understand these tool because these kind of tools take time to learn. Okay. So you have integrations here. So the more you learn about GTM engineering, the more it becomes easy for you to understand. So you can see that for emails, right? Uh the waterfall in email. Okay. Uh the waterfall in clay and can you see the waterfall in deep line? You have so many providers. Okay. So yeah, always try to be a person who is ready to explore a new tool um or something new.

#### 00:53:25

Yogesh Jaiswal: There's one more thing called blitz scale something. Yeah. Yeah. I'll let you know that that's a clay alternative. So yes, always be ready to explore a new tool. Okay. So I I think this is good. Uh if you don't have any questions we can wrap this up and tomorrow we can be ready with the workspace. Uh I would be posting a lot of tools that you need to sign up and create a bookmark of and that's it. We don't need to do anything more. Cool. Any questions? Anything?

Deepshikha: Um Yogesh you mentioned some uh company's website uh I don't know for explanation

Yogesh Jaiswal: of agents.

Deepshikha: no uh it it mentioned sp a r a I don't know what was it about it was to learn uh which you mentioned that you would be sharing in the WhatsApp group as well so I couldn't like understand

Yogesh Jaiswal: Okay. Okay. I'll share all of the websites. I would be sharing uh after this call I would be sharing all of these websites which I opened and uh you can

#### 00:54:40

Deepshikha: I know.

Yogesh Jaiswal: go uh check this out because uh okay one more problem is GTM

Deepshikha: Yep.

Yogesh Jaiswal: engineering is highly popular right now in US and Europe. In Indian companies, it's very like Indian companies are not preferring it because they don't they don't like spending thousand $2,000 on a person. So these agencies are working with American clients or European clients. Okay. So you can check these websites and understand the services they provide because that is the real GTM engineering which is happening. Okay. I would definitely share that. Okay. So just keep the workspace ready and um you might put in like you need to put in one more hour later today and we can go towards it. Okay.

Gagan Bhaisa: uh Yogesh just wanted to uh talk on this. You spoke about deep line. Okay.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: How does deepline is basically differentiate from uh I mean you writing and pushing I mean see code into GitHub

Yogesh Jaiswal: Uh okay, just want to mention that today whatever we are doing in clay uh is expensive because clay's plan starts from $190.

#### 00:56:07

Yogesh Jaiswal: That is approximately uh a monthly 22 200 rupees $200 spend uh which is 19,000 a month spend on getting 2,000 credits right uh deepline is just eliminating that part by connecting the providers. So okay is having partnership with providers and clay provide those tools in clay credits. Deepline is also doing the same thing but because deep line is an API which can connect to plot code. Deepline is slightly cheaper than clay because clay have a front end clay have a UI uh and they charge you more because they want to run that interface. Deepline is just an API that you connect to cloud code and we would definitely be doing using deepline and doing everything uh on on that. So uh it it's it's something we would be practicing. ing in you would have better clarity.

Gagan Bhaisa: Got you.

Yogesh Jaiswal: Yeah, got it. So, uh please get this workspace ready um and let's connect uh once you're ready with it. Okay. Yeah. Any anything if you have and you can just post in the WhatsApp group and we can uh connect it. Okay. So, I'm posting you tools. Uh just keep it ready and Yes. Yeah, I hope you u had you were clear with everything we discussed, but uh if you have any doubts, you can give me a call or like text. That's not a problem. Okay, cool guys. Uh have a nice day.

Deepshikha: Thanks everyone.

Shubham Gosavi: Yes, sir.

Yogesh Jaiswal: Thanks.

Deepshikha: Bye-bye.

Yogesh Jaiswal: Yeah.

#### Transcription ended after 00:58:27

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.