# D27+D28_ Web scraping in Clay + The HTTP API column - 2026_09_28 08_56 IST - Notes by Gemini


✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D27+D28: Web scraping in Clay + The HTTP API column

Sep 28, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mahima jaiswal mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Data enrichment workflows and web scraping strategies via API integrations and tool optimizations

Clay execution logic and data filtering

Gagan migrated to a new table due to connection issues.

Table outputs must include outreach messaging rather than stopping at emails or URLs.

Yogesh flagged that at least 70% of companies must remain after running signals to avoid overly strict filtering.

Using Claude or GPT helps generate a Clay execution logic to separate strategy between Prospio and Clay.

Gagan configured his table with 47 qualified companies incorporating SOC2 compliance and platform security roles.

Automation and HTTP API architecture

Inbound leads are qualified by an AI agent using 11 Labs before routing to sales.

HTTP API serves enterprise-level data transfers, enrichments, and endpoint configurations.

Valid LinkedIn profiles require 100 or more connections.

Webhooks handle immediate data posts before executing HTTP API requests.

Error code 400 denotes request formatting issues, while 401 indicates authentication failures.

The upcoming curriculum integrates Slack, n8n, Clay, and HubSpot for automated workflows.

Web scraping and GTM tooling strategies

Web scraping extracts unique GTM data from Google Maps and public platforms not available in standard databases.

Apify supports scraping Google Maps and e-commerce sites, while ZenRows manages complex crawling tasks.

Yogesh shared a repository of over 400 tools spanning ABM, cold email, data scraping, and agent builders.

BuiltWith enrichments help identify tech stacks like Webflow across large company datasets.

External scrapers offer significantly lower operational costs compared to native platform credits.

Target audience and data enrichment

Gagan enriched lead data across regions including the UK and India using a free account.

Gagan prioritized leads focusing on platform security roles instead of platform building.

Gagan configured work email verification processes using the ZeroBounce platform.

Table structure optimization

Yogesh recommended reducing table columns to maintain scalability during growth.

Gagan cleaned up the table view by hiding unnecessary columns.

Company data mapping

Yogesh suggested integrating company parameters into the people table using lookup records.

Gagan configured single record lookups using the company name parameter in Clay.

Next steps

[Gagan Bhaisa] Send Table List: Provide the updated table list for review by the end of the class session.

[Yogesh Jaiswal] Send Tools Link: Share the URL for the tools repository in the group chat.

[The group] Research Tools: Experiment with tools from the provided list and maintain a document with one-line summaries for each tool.

[Yogesh Jaiswal] Plan Outreach: Draft an outreach strategy for potential clients seeking webflow services.

[sampath vemulapati] Pick Niche: Select a business niche such as search engine optimization and write a one-liner summary. Perform research to understand the core functions of the chosen niche.

[sampath vemulapati] Filter Companies: Gather a list of 50 companies matching established signals. Process the data through Clay while adjusting filtering parameters to ensure at least 70 percent of the companies remain.

[sampath vemulapati] Build Execution Logic: Paste the strategy document into Claude or GPT. Generate a Clay execution logic to define where the platform should be applied in the workflow.

[Gagan Bhaisa] Update Target Audience: Include platform security roles in the target outreach list. Expand the search criteria to ensure relevant professionals are included in the dataset.

[Gagan Bhaisa] Map Company Data: Perform a lookup record in Clay to associate company information with the people table. Configure the mapping using the company name parameter.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

📝 Full notes

Sep 28, 2026

### D27+D28: Web scraping in Clay + The HTTP API column

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mahima jaiswal mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D27+D28: Web scraping in Clay + The HTTP API column

Meeting records Transcript Recording

#### Summary

Data enrichment workflows and web scraping strategies via API integrations and tool optimizations

Clay Table And API Automation
Discussion covered data enrichment requirements and HTTP API fundamentals for enterprise sales workflows.

Web Scraping And Tool Mastery
Participants explored competitive intelligence gathering, specialized scraping tools, and database management strategies.

Lead List Optimization And Review
Review of lead lists resulted in streamlined spreadsheet columns and integrated company messaging lookups.

#### Next steps

[Gagan Bhaisa] Send Table List: Provide the updated table list for review by the end of the class session.

[Yogesh Jaiswal] Send Tools Link: Share the URL for the tools repository in the group chat.

[The group] Research Tools: Experiment with tools from the provided list and maintain a document with one-line summaries for each tool.

[Yogesh Jaiswal] Plan Outreach: Draft an outreach strategy for potential clients seeking webflow services.

[sampath vemulapati] Pick Niche: Select a business niche such as search engine optimization and write a one-liner summary. Perform research to understand the core functions of the chosen niche.

[sampath vemulapati] Filter Companies: Gather a list of 50 companies matching established signals. Process the data through Clay while adjusting filtering parameters to ensure at least 70 percent of the companies remain.

[sampath vemulapati] Build Execution Logic: Paste the strategy document into Claude or GPT. Generate a Clay execution logic to define where the platform should be applied in the workflow.

[Gagan Bhaisa] Update Target Audience: Include platform security roles in the target outreach list. Expand the search criteria to ensure relevant professionals are included in the dataset.

[Gagan Bhaisa] Map Company Data: Perform a lookup record in Clay to associate company information with the people table. Configure the mapping using the company name parameter.

#### Details

Clay Table Progress and Outbound Output Requirements: Gagan Bhaisa reported encountering connection issues with a previous table and stated they are moving to a new table, promising to share the list by the end of the class. Yogesh Jaiswal emphasized that tables are tools to execute strategy and must be kept clean, requiring minimal enrichments, clean names, and structured outputs designed for outbound messaging tools like HeyReach or Instantly rather than ending abruptly at emails or LinkedIn URLs (00:08:17).

Artificial Intelligence Agent Use Case for Website Visitors: Gagan Bhaisa described a straightforward inbound use case where website visitors who do not book a meeting are qualified via a calendar hook and an artificial intelligence agent built using ElevenLabs, which calls visitors to ask three specific questions before routing them to a human team member (00:10:30).

Hypertext Transfer Protocol Application Programming Interface Fundamentals in Enterprise Automations: Yogesh Jaiswal explained that Hypertext Transfer Protocol application programming interfaces are used for sending and receiving data at an enterprise level, noting that small companies typically build their own solutions while enterprises utilize platforms like n8n (00:11:29). Yogesh Jaiswal outlined the core components of application programming interfaces, including endpoints, methods (get, post, delete, put), headers, query parameters, JavaScript Object Notation formatting, and authentication, while distinguishing between test and production URLs (00:12:39).

Sales Automation Workflow Demonstration: Yogesh Jaiswal demonstrated a test Ideal Customer Profile check agent built on a Slack-to-n8n-to-Clay architecture, where pasting a LinkedIn URL triggers automated data enrichment and saves information directly to HubSpot, minimizing manual data entry for sales teams (00:13:45). Yogesh Jaiswal also outlined a complex event attendee outreach scenario where meeting attendees' LinkedIn URLs posted on WhatsApp flow through Slack, n8n, and Clay for instant enrichment and personalized outreach generation (00:17:21).

Application Programming Interface Error Code Troubleshooting: Yogesh Jaiswal detailed common Hypertext Transfer Protocol status error codes encountered during automation building, explaining that a 400 error indicates request formatting issues, 401 denotes unauthenticated requests requiring application programming interface key checks, 403 signifies permission and scope limitations, 404 means an endpoint does not exist, and 429 points to rate limits being exceeded due to excessive request frequency (00:21:58).

Workflow Integration and Web Scraping Introduction: Yogesh Jaiswal outlined the curriculum plan to connect Slack, n8n, Clay, and HubSpot, emphasizing practical workflow building over theoretical learning (00:23:07). Yogesh Jaiswal then introduced web scraping, prompting discussion on its application in Go-To-Market engineering. Sampath Vemulapati defined web scraping as an automated process to extract data from various websites using commands or chatbots (00:24:13) (00:26:25).

Competitive Intelligence and Niche Web Scraping Applications: Gagan Bhaisa suggested using web scraping for gathering competitive intelligence by analyzing public financial reports of public companies, which Yogesh Jaiswal acknowledged as a deep insight approach (00:27:44). Yogesh Jaiswal explained Go-To-Market engineering use cases for scraping local businesses from Google Maps using tools like Apify when data is unavailable on Apollo or Clay, citing examples like targeting restaurants for Swiggy and Zomato or real estate brokers and lawyers (00:29:00). Yogesh Jaiswal also discussed website content crawling, such as tracking daily design additions for fashion brands, noting its legal gray areas and blocking mechanisms employed by European and American companies (00:29:59).

Specialized Scraping Tools and Cost Analysis: Yogesh Jaiswal highlighted local business review scraping on Google Maps, such as targeting popular salons for membership sales, as a high-value service that can command significant monthly retainers (00:32:02). Yogesh Jaiswal introduced ZenRows for handling complicated scraping tasks and deep company data extraction, noting that scraping tools are cost-effective compared to platform-native options (00:33:03). Yogesh Jaiswal compared Apify at nineteen dollars a month to Claygent at two hundred dollars for one thousand scrapings, explaining why companies choose separate specialized tools (00:40:50).

Lead Generation Tools Database and Tool Mastery Strategy: Addressing Sampath Vemulapati's request for a centralized tool reference sheet, Yogesh Jaiswal shared a directory containing over four hundred tools across categories like account-based marketing, agent builders, cold email sequencers, data scrapers, and customer support (00:43:46). Yogesh Jaiswal advised Sampath Vemulapati and Gagan Bhaisa to explore individual tools, create personal documentation with one-line summaries, and focus on one niche area at a time to master the market (00:44:48) (00:49:09).

Time Management Expectations for Go-To-Market Engineers: Yogesh Jaiswal stressed the importance of time management in Go-To-Market engineering, noting that building a clean Clay table should take only two to three hours to avoid excessive labor costs for employers, drawing on personal past experiences where simple tasks took multiple days (00:50:17).

Clay Table Signal Strictness and Qualification Strategy: Reviewing Sampath Vemulapati's Clay table, Yogesh Jaiswal observed that strict filtering reduced sixty companies down to six, advising that signal parameters should be loosened so that at least seventy percent of sourced companies pass qualification (00:52:28). Yogesh Jaiswal recommended performing company qualification prior to Clay in tools like Prospio to prevent double filtering, and suggested using Claude or GPT to generate a Clay execution logic document based on strategy (00:55:38). Yogesh Jaiswal announced that the team will move to email deliverability next while continuing to refine their basic outreach Clay tables (01:00:31).

Gagan Bhaisa's Completed Clay Table Review: Gagan Bhaisa presented their completed Clay table comprising forty-seven qualified companies complete with websites, LinkedIn profiles, domain sizes, industries, and estimated revenues. Gagan Bhaisa explained that they incorporated a signal checking for SOC2 compliance to qualify advanced target companies, and noted that they targeted specific roles such as vice presidents, directors, heads, and managers across security, DevOps, application security, and platform security to ensure an adequate audience size (01:02:52).

Lead List Building and Data Enrichment: Gagan Bhaisa discusses the creation and enrichment of a lead list targeting platform security professionals across the United States, United Kingdom, and India. Due to free account limitations, only 50 of 159 available profiles are displayed, with 109 locked behind an upgrade. Gagan Bhaisa details the data points collected, including full names, job titles, locations, and LinkedIn profiles, along with additional enrichment layers providing summaries and job counts. Gagan Bhaisa explains that these summaries help them filter out general platform builders and specifically target individuals focused on security, and they plan to verify work email addresses using ZeroBounce before reaching out to their 50 identified leads (01:05:35).

Feedback on Spreadsheet Column Structure: Following sampath vemulapati's departure for another meeting, Gagan Bhaisa asks Yogesh Jaiswal for feedback on their work (01:07:39). Yogesh Jaiswal notes that the build is much improved compared to previous attempts, but advises them to use fewer columns to prevent scaling difficulties. Accepting this feedback, Gagan Bhaisa hides several unnecessary columns, including the headline person column, resulting in a cleaner sheet that Yogesh Jaiswal agrees provides them with a solid foundation for crafting messaging (01:12:16).

Integrating Company Messaging via Lookups: Yogesh Jaiswal suggests adding company-level messaging to the people table using a lookup feature since individual summaries are not available for every profile. Gagan Bhaisa executes this recommendation by using single record lookups and mapping the data using the company name. Yogesh Jaiswal reviews the output and confirms that the combined information is sufficient for them to build effective messaging, before Gagan Bhaisa proposes stopping the recording to discuss off-topic matters (01:13:50).

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

📖 Transcript

Sep 28, 2026

### D27+D28: Web scraping in Clay + The HTTP API column - Transcript

#### 00:08:17

Gagan Bhaisa: Hey,

Yogesh Jaiswal: Good morning.

Gagan Bhaisa: good morning.

Yogesh Jaiswal: I think it's Monday.

Gagan Bhaisa: Yeah, sorry.

Yogesh Jaiswal: It's Monday. I think less people are joining.

Gagan Bhaisa: Yeah, I mean everybody was getting uh overcome with their weekends.

Yogesh Jaiswal: Yes. So,

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: have you built the table perfectly?

Gagan Bhaisa: I I did but I think there was some problem uh on my previous table.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: So I am just trying to move into a new table uh due to some connection.

Yogesh Jaiswal: Okay,

Gagan Bhaisa: So I think uh within maybe end of the not end of the day end of the class I'll I'll send you that list to see how that look like.

Yogesh Jaiswal: perfect. Perfect. So,

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: we just need to understand that uh the table is just the process to do the strategy.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: I mean uh and it needs to look perfect. So, we just need to take care of simple things. First of all,

Gagan Bhaisa: Mhm.

#### 00:09:17

Yogesh Jaiswal: enrichments only when needed.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Second data should be clear uh first name,

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: full name, clean names and uh also the output should be okay I'll tell

Gagan Bhaisa: Yes.

Yogesh Jaiswal: you the table output should be a message to the hey reach or instantly I mean if you're doing outbound so uh the table should not end at emails or LinkedIn URLs the

Gagan Bhaisa: Got it.

Yogesh Jaiswal: table should also build messaging and build uh further uh progress so clay's work should finished. I mean if you see a good table.

Gagan Bhaisa: God.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: M

Yogesh Jaiswal: Okay. So I'll just share my screen.

Gagan Bhaisa: yeah.

Yogesh Jaiswal: Um have you used anything earlier? Yeah.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Okay. Have you do you know how to connect an end to Slack?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Post and post and pre

Yogesh Jaiswal: Yes. Yes. Correct. Uh so have you connected an end to clay as well.

Gagan Bhaisa: uh not really I think I didn't find any use case uh to correct the case

#### 00:10:30

Yogesh Jaiswal: Okay, got it.

Gagan Bhaisa: but uh I I did connect it with other applications like uh your uh

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: inbound forms uh then basically 11 laps uh to

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: mostly so I mean our use case was pretty straightforward we want everyone uh like anybody who are coming to the website we want to make sure that we qualify them before routing to the sales.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: So and this happens to anyone who does not book a meeting. So we have a calendar in between and then calendar gives a hook say that who books a meeting who does not books a meeting and then somebody who not books a meeting our AI agent via 11 labs should goes back to the system uh call them ask them three pretty state question say

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: that hey this is what uh pixels do and we want some few details to basically route it to uh I mean some someone human and then they would reach back to you within no time. So yeah, that's what

Yogesh Jaiswal: Mhm.

#### 00:11:29

Yogesh Jaiswal: Got it. Uh yeah. Hi Sat good morning. Okay.

sampath vemulapati: Hi guys,

Yogesh Jaiswal: Hi.

sampath vemulapati: good morning.

Yogesh Jaiswal: Hi. So uh again just to make it very easy I mean as you have not connected an attend to Clay um everything is very easy. I mean it's it's really very easy and uh the main goal I'm trying to uh the main thing I'm trying to explain you is on a broader term that HTTP API is only used when it comes through sending or receiving the data right and uh when we going to build automations on nin okay now uh on a real understanding what I have learned and what I've seen is companies who are enterprises are more keen to use nit small companies would not use it because uh see small companies already have technical people they themselves build they don't like to like get a new person to build something okay so What I want to mention is um everything we are going to do on HTTP API is going to be on a um enterprise levels.

#### 00:12:39

Yogesh Jaiswal: So enterprise facing problems, enterprise facing deal enrichments, contact enrichments, building functions. Okay. Um yeah. So just to let you know HTTP API is just a method of uh sending and receiving data. Okay. API is nothing but how two pieces talk to each other. Endpoint is where you uh send your request to. Method is if you read the data, get post the data, create uh again very easy. When we're going to do live in narrator, it's going to be really easy. Okay. Header, it's just the header that uh your information uh query parameter that if it's an active uh filter or a not active filter. um a little thing that we need to learn JSON how JSON works. Okay. So it's very easy I mean whatever output or input which is happening needs to be output on JSON. Okay. Now field path is where the path is if you want to post to clay or post to a Google sheet anywhere. Okay.

#### 00:13:45

Yogesh Jaiswal: Then you have authentication. Um whenever we going to use N10 we are going to do everything in test URL. So do you know what is text and production URL?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Okay.

sampath vemulapati: I am not aware actually.

Yogesh Jaiswal: Uh yeah yeah yeah. So uh sut test and production URL is very easy. Okay. And in N10 we are going to build an automation right. The automation can be that I'll give you an example that I have built. So let's say if a company have 100 people in their sales team. Okay. Now every saleserson is a nontechnical person and is just sitting and dialing people. Right now the company wants anyone then say that the saleserson dials that the person needs to be checked validated and the information should be saved in HubSpot. Okay. So we are going to build an automation where the person will post a LinkedIn URL on Slack. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: after that uh or maybe I can even show you uh IC.

#### 00:15:06

Yogesh Jaiswal: Okay, let me show you this. Can you see the screen?

sampath vemulapati: Yeah, I can see.

Yogesh Jaiswal: Okay, ju just imagine that this is a agent that so this is what we going to build ICP check and we we can build anything, right? This is just a test thing. So what I'm going to do is I'm going to paste a LinkedIn URL. Okay? And I'm a sales guy.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So when I post a LinkedIn URL, it should work good. When I know not post a LinkedIn URL, it should give me a text. Please add a LinkedIn URL to use the ICP agent. Okay. I paste the LinkedIn URL. Now, can you see that now this in I get this information by

sampath vemulapati: Yeah.

Yogesh Jaiswal: claim. Okay. So the back end of all of these things is clay. Okay,

sampath vemulapati: Got it.

Yogesh Jaiswal: we go down. Uh the next step I built was enrichment. Okay,

#### 00:16:08

sampath vemulapati: Yeah,

Yogesh Jaiswal: so see I run the uh um LinkedIn URL and it gives me all of the information. So this information will also save in HubSpot, right?

sampath vemulapati: forgot.

Yogesh Jaiswal: So saleserson should not is not spending a lot of time on this. He just faced okay I am a saleserson Sampathis the um head of CSR at

Gagan Bhaisa: Thank you.

Yogesh Jaiswal: uh my cities right I want to sell you something okay now I will just copy your LinkedIn URL paste it in slack everything will be automated your information will be automated everything will be get saved in HubSpot now if I want to do enrichment right I can even do an enrichment right so enrichment means I will get your see I'll show Yes. Yes. Okay. Enrichment I think I have not built. So enrichment will further give you email which is valid or invalid. Uh LinkedIn URL which is valid or invalid. But we can easily check LinkedIn URL which is valid and invalid. Connections are more than the LinkedIn URLs are valid.

#### 00:17:21

Yogesh Jaiswal: If it's 100 or less then it's invalid.

sampath vemulapati: Oh,

Yogesh Jaiswal: Okay. So let's uh yes let's now think beyond a task beyond learning. Now we need to understand what all things you can automate in a company right and when

sampath vemulapati: sure.

Yogesh Jaiswal: you sit down and think about this there are endless possibilities right maybe in your company um someone is going to an event right in that event the person is going to meet a lot of attendees right let's say some in your company 10 people are going into an event okay those 10 people are going to meet at least 100 people each.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Right? Now you want to do outbound over them, right? So you know that it's going to be really difficult because um when it when the outbound happens everything needs to be perfect.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So what if we create an agent where the event attendee let's say Gagan is also working in Satwa and Gagan attends the event right so Gagan is just

sampath vemulapati: Heat.

Yogesh Jaiswal: going to let's say Gagan is talking to Nilles and Nilish is some CEO of a company and Gagan and Nish met now Gagan wants to do outreach right so what Gagan will do

#### 00:18:36

sampath vemulapati: Yeah,

Yogesh Jaiswal: Gagan will copy the LinkedIn URL and Gagan will paste it in WhatsApp Right now everything everything will start automating in WhatsApp.

sampath vemulapati: good.

Yogesh Jaiswal: WhatsApp it will go to Slack it will you will create a channel event attendees from Slack it will go to N it will go to clay everything will be enriched will get an information that the URL of Nash is right. Okay, the information will then move to clay. Everything will move to her in instantly and Gagan will get a successful message, right? And the sequence can be that hi nilles, we met in this event. Uh nice talking to you.

sampath vemulapati: Oh

Yogesh Jaiswal: Okay, so can you imagine the scope of an automations

sampath vemulapati: yeah. Yeah, actually

Yogesh Jaiswal: and by the way it's very uh costfriendly. You're not going to spend a lot of money on this.

sampath vemulapati: makes sense. Makes sense because we were also facing a similar issue.

Yogesh Jaiswal: This

sampath vemulapati: Yogesh.So I mean in my current uh consultancy contract they wanted to reach out to multiple people and uh you know the data that we were getting was not so valid.

#### 00:19:48

sampath vemulapati: So like I'm trying to build a validation protocol first and then say that like you know these people have to be reached out automatically. So I I was just thinking then then I think editin will work really well for

Yogesh Jaiswal: heat.

sampath vemulapati: them.

Yogesh Jaiswal: Yes. See, uh, one thing I've understood is an anyone can learn an by the way, right?

sampath vemulapati: Right.

Yogesh Jaiswal: The only problem is,

sampath vemulapati: Right.

Yogesh Jaiswal: um, people cannot like hardly people use an efficiently. Okay? Because either they burn a lot of credits, they build unc uh, they build uncomplicated automations which is not needed. Okay? So we need to also understand that how we are using an attit right then this is the next phase we are going to go after okay uh yes now let's go back to HTTP API okay so HTTP API would be the main method to use any okay because the data flow will happen to an HTTP API okay uh there is one more way of data flow which is called web hook okay in clay right so web hook means when we going to build a live table.

#### 00:20:58

Yogesh Jaiswal: Everything will happen through a web hook. Okay, I'll tell you what is a web hook. What does a web hook means?

sampath vemulapati: Yeah.

Yogesh Jaiswal: Uh let's say if you paste an information anywhere, right? And that information needs to be worked on immediately. Okay, that's a web hook. So every time you post, there will be a hook to pass on that uh process. Okay. Then when the information gets processed then you use HTTP API. Okay. And you use the method post. Post means it's very easy. Post mean post the data. Get means get the data. Okay. Delete and put the same. Okay. So uh it's going to be very easy. You're going to get get from webbook and post it from a HTTP API. Okay. Now uh you know how a chatbot works right? Um right.

Gagan Bhaisa: Open

Yogesh Jaiswal: So everything that we see around uh on the internet related to SAS companies

#### 00:21:58

Gagan Bhaisa: two.

Yogesh Jaiswal: or any companies everything the back end is mainly a uh n and claw or an AI tool. Okay. So uh you just need to understand how HTTP API works and scraping works. Okay. Uh yeah. So this is how an htt JSON body looks like. Okay, you need to learn how to use JSON and it's very easy. Okay, you just need to understand the commas, okay, the slashes, when to use, when not to use. Okay, and it's also very easy when you run something and you get an error. This is the easiest thing to diagnose. 400 something with your formatting request. check your body and you will get this in clay. 401 not authenticated not authenticated your API keys uh needs

Gagan Bhaisa: Yes.

Yogesh Jaiswal: to be checked. 403 um you're authenticated but not allowed. You need to go to permissions and scopes. Okay. 404 endpoint doesn't exist. You need to check your endpoint. Okay.

#### 00:23:07

Yogesh Jaiswal: 4 to9 you're sending requests too far too fast. You need to change your rate limit. Okay. So, uh we can I think the most easiest way to learn all of these things is connecting it to Slack. Okay. So, what we are going to do is the plan is um we are going to connect Slack to NAN. Okay. Uh and then you will connect N to clay, right? And we are going to build a simple workflow around everything because uh it's it's easy to learn things when you do practically rather than uh learning it theoretically. Okay. So uh whatever information you have built in the play table

Gagan Bhaisa: It's

Yogesh Jaiswal: right as a next step we are also going to add hubspot. not layer to it. Okay, we are going to push data to HubSpot as well. Okay.

Gagan Bhaisa: Thank you.

Yogesh Jaiswal: Uh after pushing data to HubSpot, we are also going to build an edit and automation around it. Right. But that would be a separate table.

#### 00:24:13

Yogesh Jaiswal: Okay. The table would be mostly an enterprise company having a sales team and doing an ICP check, right? But we can think more uh we we can think beyond uh all of these things also like we can build a u website visitor agent uh automation we can build a lead enrichment automation right so whatever you feel like okay cool so uh yeah not going deep

Gagan Bhaisa: Oops.

Yogesh Jaiswal: diving into the technicalities okay uh it's it's very easy when you use it rather than when you uh practice That's it. Okay. Now there is one more thing called uh web scraping. Okay. Uh do you understand by what this web scraping means? Like if I ask you.

Gagan Bhaisa: Uh you guys before we dive into this web scrapingpart uh can we go a little one

Yogesh Jaiswal: Yes.

Gagan Bhaisa: step before and then uh I just wanted to understand the whole picture behind the slack to N8 connect and then N8 connect and then whatever the result is coming and then

Yogesh Jaiswal: Yes.

#### 00:25:26

Gagan Bhaisa: come back to Slack. Do you have that background architect with you as of now available?

Yogesh Jaiswal: Yes. So the plan is the HTTP API column we we are just learning clay but uh right now and we are talking about from a clay perspective. Okay. what I have said nit slack everything we are going to build that in the later topics so we have

Gagan Bhaisa: Okay.

Yogesh Jaiswal: it uh in the curriculum yeah the problem is I'm not

Gagan Bhaisa: Mhm. No, I mean, so like you said, right? Uh you're going to put some input. Okay. I mean, I got you. I mean, I'm just going ahead. So, maybe some is here.

Yogesh Jaiswal: yeah yeah no that's fine it's like I'm uh we are

Gagan Bhaisa: So,

Yogesh Jaiswal: learning how an engine works and we we might not build our engine now but we are just learning it

Gagan Bhaisa: yeah. Yeah. Okay.

Yogesh Jaiswal: so the thing is um I'm going to help you build a automation but I'm going to build unique automations for you so that you can try on different aspects.

#### 00:26:25

Yogesh Jaiswal: So HTTP API is generally for enter automations. So right now we are not focused on because our focus is to build a good clean clay

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: table but uh once the clay table is ready we are the next step we are going to build an edit in automotion.

Gagan Bhaisa: Got it.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Happy.

Yogesh Jaiswal: Yes. Uh yeah. Uh do you what do you understand by web scraping if I ask you?

sampath vemulapati: Uh so it's basically I mean to my limited understanding it's basically scraping the data from the different websites through an automatic process like for example uh what I've built on my clay uh on my cloud is uh I've built a skill to my cloud saying that I'll give you a command and then you have to basically scrape multiple websites and it happens through probably like a chatbot or a multiple option so it retrieves the information uh and can be scraped to the you know whatever use that is Yes.

Yogesh Jaiswal: Uh okay. Uh but do you understand the reason why we are talking about web scraping from a GTM engineering point of view like because everything is available on Apollo or L or Clay but why we talk about scraping

#### 00:27:44

sampath vemulapati: Yeah.

Yogesh Jaiswal: here.

sampath vemulapati: So I I think whatever I've understood is uh probably for the funding news or hiring news or any other uh I mean let's say any other litigations or maybe mergers or acquisitions. So for such things or maybe we may use uh the websites and other uh news platforms uh to make the lead more enriched.

Yogesh Jaiswal: Mhm.

sampath vemulapati: I I I feel so

Yogesh Jaiswal: Yes. Um I think we need to also divide this conversation into if you're trying to scrape something and if you have a tool let's say somebody told about funding right you know currency base is already there. So you don't need to use general scraping right directly you can use crunch base okay

Gagan Bhaisa: Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: uh it's very easy to understand the scope of scraping where we are just going to scrape things where tool is not working okay very easy very easy uh

sampath vemulapati: Yeah.

Yogesh Jaiswal: let's say you want yeah mhm

Gagan Bhaisa: you guys I would put like this. Okay. So I mean from my point of view let's say I want to read a financial plan I mean uh financial report for this company which is a public company.

#### 00:29:00

Gagan Bhaisa: I want to reach out to them.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: I could get lot of data from the financial data with web web scraping which is actually not

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: available in any of the data. I mean it's public but it take a lot of time to basically scrap it.

Yogesh Jaiswal: Mhm. Yes. Yes. I think uh that is correct. You're talking about from a deep insight level which is also correct.

Gagan Bhaisa: Yes. Maybe you can say competitive intelligence.

Yogesh Jaiswal: The Yes. Yes. I think uh that is good. But when we talk about GTM engineering uh right now there are a lot of clients who sell to small businesses. Okay.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: I'll give you a very good example. You know Zomato and Swiggy right? uh they sell to restaurants, hotels, small joints. You cannot find them on Apollo. Okay? You can easily find them on Google maps. Okay? So there is a tool called API.

#### 00:29:59

Yogesh Jaiswal: Okay, it can scrape Google maps maps perfectly. Okay, the data is freely available. Now definitely if there is a GTM engineer in blink in sorry in uh Swiggy and Zumato he would be building an automation of anything new uploaded on Google maps get the they'll get the information they will contact right

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: so uh there are very small like see real estate companies right now just imagine I want to sell something to real estate brokers right a software or maybe a a software for lawyers. So how would I do that? I I the data is not available on clay, right? So or Apollo. So we use API, right? API is just a I'll show you and I'll also show you a good reason. Okay. Yeah. Can you see Google map scraper, Instagram scraper, e-commerce scraper, uh website content crawler. Uh you know what is content crawling?

sampath vemulapati: No, I'm not aware.

Yogesh Jaiswal: Okay, very easy. You uh not only check the website but you also crawl everything in the website.

#### 00:31:12

Yogesh Jaiswal: Let's say I crawl snitch how many designs they add new every day and I sell that information to Myntra very easy and by the way this is a new industry which is emerging. You crawl website and sell data and by the way this is illegal but if you do it even if you do it it's it's a good money companies are doing it.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Okay. So um yeah this is called scrolling. Okay.

sampath vemulapati: So this you said this is illegal or legal.

Yogesh Jaiswal: Yeah it's not legal like you cannot crawl someone's data right it's an illegal but when you do on a

Gagan Bhaisa: Security.

sampath vemulapati: Okay. Okay. Yeah.

Yogesh Jaiswal: small use case then it's fine but you're sitting and crawling everything around the world. Uh that's a problem. And by the way there are European companies and American companies you cannot crawl. They block you.

sampath vemulapati: Right. Right.

Yogesh Jaiswal: Uh they're very smart but in India it's fine. Okay, you know what's a blue Google map scraper,

#### 00:32:02

sampath vemulapati: Yeah.

Yogesh Jaiswal: right? See, you can now also include reviews. See, uh some what if there is a salon and you know Tonyian guy, right, in Bangalore, they are doing a good revenue.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: What if you can build an automation for them that anyone who posts a positive review, you sell them a a membership, right? And they have lots of stores around India, every day hundreds of people are posting good reviews, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: that automation you can build. Okay. Uh and by the way you can easily charge and maintain these kind of work at lakh two lakh rupees and monthly retainer would be 70 80,000 rupees a month. So you can now understand where GTM engineering is going. It's not sticking to traditional outbound.

sampath vemulapati: Wait.

Yogesh Jaiswal: Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: And now we are talking about Tonian guy.

sampath vemulapati: Yeah.

Yogesh Jaiswal: What if you work for a big uh um uh beauty chain? in in New York they would not think about $1,000 $2,000 right they would think about $10,000

#### 00:33:03

sampath vemulapati: Yeah.

Yogesh Jaiswal: $20,000 of uh money so we need to now think about better ways to

sampath vemulapati: Yeah.

Yogesh Jaiswal: position oursel also in the market okay so all of this information we will get from API and by the way it's very uh reasonable you don't need to worry about the charges you can see $19 only okay there's one more thing and which Dan mentioned Okay. Uh which is lenros, right? Uh see this is for complicated data, right?

sampath vemulapati: Okay.

Yogesh Jaiswal: You you know you have seen captur website.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: Yeah. So anything which is complicated not easily scraped you use zenros. Okay. And if you see um if I need to deep dive into a company and get more information about the same company then I would not use API. I mean API will not be perform perfectly. I would use Zenros.

sampath vemulapati: Yeah,

Yogesh Jaiswal: Zenro will go inside the uh company go more inside more pages and scrape data. Right?

sampath vemulapati: got it.

#### 00:34:11

Yogesh Jaiswal: Uh can you see if you try to understand what Zenro is doing? It's trying to do more complicated scraping.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay, whenever you have a complicated scraping task and again uh these scraping tools are not expensive. Okay, you can see $16 a month, right? Uh not like clay where unlike clay where it's $190, okay? Uh you might see everything more technical but again we can use the same in clay, right? So it becomes non-technical for us. Uh we not going to code or anything but yeah can you see live web access pricing changes okay watching the market filling you know consultancy companies right EY and all what they do they do these things EI deoid

sampath vemulapati: Yeah. A lot of market intelligence cash,

Yogesh Jaiswal: okay yes yes so they are technically ally building an automation, maintaining it and selling the data, right?

sampath vemulapati: right?

Yogesh Jaiswal: Um industry signals. Okay. Okay. And everything is connected. You can see. So you can see clay is already there.

#### 00:35:32

Yogesh Jaiswal: Okay. Uh we try to do everything in clay unless we have clay. But you can even do in flot, right? And in plot code also it's very easy. Okay. Yes. So, are we clear with the difference between API and Zenros?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: You guys out out of the topic, I mean this is a different question.

Yogesh Jaiswal: Mhm. Yeah. Yeah. Please, please.

Gagan Bhaisa: Do you have any reference or you know any uh tool which gives us a uh data on someone who is looking to build a web flow uh I mean implement web flow in their website like CMS webflow maintenance web flow uh website building any specific tool who gives us the data or where I can go and find uh like communities uh say that they are actually looking for a web site building services.

Yogesh Jaiswal: Okay. So, are you providing services or are you a tool?

Gagan Bhaisa: No, we are providing services. It's it's one of my I mean I mean brand partner we working

#### 00:36:42

Yogesh Jaiswal: Yeah. Yeah. Yeah. I it's it's very uh so okay you are providing website building

Gagan Bhaisa: with.

Yogesh Jaiswal: services and you want to okay got it u I would say this would

Gagan Bhaisa: Yeah. I I mean yeah it's not just like website building it's a advanced

Yogesh Jaiswal: be yes I would say this would be

Gagan Bhaisa: version of website building with a web flow implementation.

Yogesh Jaiswal: gohead I would say this would be less possible through because see I mean either you scrape every website and check if they're using web flow or not. I think the better way is to just do organic marketing. I mean, why don't you just start doing some paid marketing? You can easily get good.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: I have a friend who does that who does that. He just do paid up marketing and get a lot of leads. I think uh sometimes you can you cannot find data of all of these activities because you cannot track it. We don't know what website where it build like before we check it on

#### 00:37:40

Gagan Bhaisa: That

Yogesh Jaiswal: built with or something. So that would be something like paid marketing would work I would say. I mean rather than either sorry

Gagan Bhaisa: What is the top? No, no, you're saying something. I interrupted unnecessarily.

Yogesh Jaiswal: uh or either the best way is why don't you pick a segment and run a builtwith enrichment on let's say 10,000 websites. Okay. And you do everything in cloud. So you don't need to use clay also. And you just check if they're using web flow or not.

Gagan Bhaisa: Okay. Uh yeah, just an extension to this one. what would be the top signal? I would not say top signal, top notified version that would be more useful for me. So let's say somebody is looking for a website maintainance, somebody is a lean team, somebody has been in this industry but the website is not updated since industry is moving to AI native. What is the four point possibility? I would not get a signal.

#### 00:38:49

Gagan Bhaisa: possibility of talking.

Yogesh Jaiswal: Um, I think Here we cannot even understand the signals unless we talk to them because

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: mainly you are trying to reach out to small companies right so I would say the better approach of this would be pick up a subcategory let's say you select salos in US right now there can

Gagan Bhaisa: That's it.

Yogesh Jaiswal: be 10,000 salos in US right you get the data through API move into cloud run a builtwith on everything right when you run a built with you will understand if the website is in god ID it's in API oh sorry it's it's in web flow if it's in

Gagan Bhaisa: What happened?

Yogesh Jaiswal: WordPress and then you build a messing around it. If it's in web flow, you offer web flow maintenance. If they need website redesigning, that's why this market is huge. I mean, you just need to reach out and talk to them rather than thinking more because the ticket size is also small, right? They would pay $500, $600.

Gagan Bhaisa: No. Uh I mean tickets are pretty huge.

#### 00:39:50

Gagan Bhaisa: We I mean the branch charge like almost 15 to 20.

Yogesh Jaiswal: Oh, so I think we need to plan an outreach for them.

Gagan Bhaisa: Uh

Yogesh Jaiswal: Uh where we can just go to cloud and understand what we need to build. But yeah, I think the best way is to use built with and scrape.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: The more data you see, the more data you'll understand and that's the better way to learn because uh

Gagan Bhaisa: Got it.

Yogesh Jaiswal: yeah. Uh I hope that clears but yeah,

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: I think uh yes.

Gagan Bhaisa: I mean that makes Thank you.

Yogesh Jaiswal: Yes, works. So, uh yeah, even we have options of scraping in clay. You know, we do it in clay, right? Uh with a native scraper, but it's very it's a very static information, right? Homepage, web pages, uh email, phone numbers, link. There is a clay native scraper. Okay. There is a clay chrome extension. We don't use it generally. I mean, it's not very popular.

#### 00:40:50

Yogesh Jaiswal: But yes, there is clayent, right? I would say Clayent also does a good job, right? Uh the only reason Clayent is not good because it's expensive. I mean uh we use neon let's say which is two credits, right? Uh for,000 uh scraping, right? So that would cost us $200.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Okay, AP5 would cost us $19. So, can you see the difference? I mean, this is the reason we companies would purchase separate tools, right? Um, and by the way, API would also Yeah, API would also give us credits. So,

Gagan Bhaisa: Don't hold up.

Yogesh Jaiswal: Okay. We'll check this later. But yes, API would be a lot less. Okay. So, uh very easy when the the scraping task is only limited to 10, 15, 20 companies. We don't try to use API or Zenros. You can even use Clayent. Okay. Uh I feel there's a native API and Zenro integration in Clay as well. I need to still check because I have not used it.

#### 00:42:25

Yogesh Jaiswal: uh if there's a native integration then you can even use API and zenros inside clay with clay credits okay uh or else I think mostly most of the times when you're going to use zenros and ampify you might come along a company where they having their own account okay again choosing the right tool to understand for complicated strapping we are going to use API and generos for smaller ones you can use

Gagan Bhaisa: Okay.

Yogesh Jaiswal: cleent okay uh Um this is more of I think scraping would be more of to do with small and medium uh company selling to small and medium businesses. Okay. So let's be focused over there that the task would be more of positioning to the small companies to selling to small companies and mid companies or small businesses. complicated scraping would be deep diving into the company, right? But that can be done with Legit. Okay,

Gagan Bhaisa: Is that

Yogesh Jaiswal: cool. Uh any questions in scraping?

Gagan Bhaisa: okay?

sampath vemulapati: Uh Yogesh my question is not directly regarding the scraping but also I remember you sharing one sheet with all the tools uh it has a phase wise approach as well like for example uh initially we were for for the lead generation you had a bunch of tools so do

#### 00:43:46

Yogesh Jaiswal: honestly.

sampath vemulapati: you have any singular sheet where we can just refer to all the tools in one sheet

Yogesh Jaiswal: Uh, I'll show you something. Okay.

sampath vemulapati: because I tried building my own sheet while I'm attending the classes but you know it somehow got missed and then a lot of these uh tools got missed.

Gagan Bhaisa: We have

Yogesh Jaiswal: Yes. So, uh see uh there are more than 400 tools right now and uh I really want

sampath vemulapati: Yeah.

Yogesh Jaiswal: you to understand that the person who knows every tool or just get a basic idea about it will win the market. Okay? Because you don't know what the company's using right now. Okay? So try to go through this website. I like I will sell that share the exact link to it. So you will see there are a lot of tools okay uh try to just open and understand what it does and definitely this would take you a lot of time right so can you see for ABM you have

Gagan Bhaisa: f***.

#### 00:44:48

Gagan Bhaisa: Excuse me.

Yogesh Jaiswal: play common room cmai warmly wombora right so I my goal is

sampath vemulapati: Yeah.

Yogesh Jaiswal: not you to Click. not let you focus on a single tool because tomorrow if an interview someone ask you what is bomba and you are like I I don't know what is this so this should not be the thing because we are now

sampath vemulapati: H.

Yogesh Jaiswal: learning it in depth okay so try to go I'll send this uh here this link into the group uh okay

sampath vemulapati: Sure.

Yogesh Jaiswal: so try to create your own document where if you have experimented with this tool if you have used it maybe a single liner of what you understand. Okay. So you have agent builders,

sampath vemulapati: Yeah.

Yogesh Jaiswal: okay?

Gagan Bhaisa: Holy

Yogesh Jaiswal: You have app builders, right? And then you have uh frameworks, you have note takers.

Gagan Bhaisa: ghost.

Yogesh Jaiswal: Now we need to also understand that Gong is the leader but still there are a lot of companies. Okay. Then you have AI role play.

#### 00:45:54

Yogesh Jaiswal: Okay. Then you have sales prospecting. Okay, you have AI, SDR, coding agents, you have content designing, cold email. Can you see for cold email how many uh tools are there?

sampath vemulapati: Yeah, there are a lot here. Yeah,

Yogesh Jaiswal: So I think why don't we just open everything and understand what it does? Okay, because see outreach is a CRM by the way. Outreach.io is a CRM but it's shown here in cold email sequencer.

sampath vemulapati: got it.

Yogesh Jaiswal: It's it's also cold emailing but also a CRM. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Then you have uh here which is called call dialer.

Gagan Bhaisa: What? Happy.

sampath vemulapati: Okay.

Yogesh Jaiswal: You have content ideation, content management, copyrightiting, customer support. Can you see for data scraping? How many there?

sampath vemulapati: Yeah.

Yogesh Jaiswal: How many are there?

sampath vemulapati: Okay.

Yogesh Jaiswal: Server is for Google scraping.

sampath vemulapati: Okay.

Yogesh Jaiswal: Google search script. Yes. And then you have data orchestration. You have data infrastructure.

#### 00:47:02

Yogesh Jaiswal: Okay. Email finder deployment.

Gagan Bhaisa: You're welcome.

Yogesh Jaiswal: See look like disco like and portion. So this market is not crowded.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: You have marketing automation multi.

sampath vemulapati: Does it also list our web scraping for now?

Gagan Bhaisa: That is a pleasure.

Yogesh Jaiswal: Sorry.

sampath vemulapati: Web scraping. Does it does it include any tools here?

Yogesh Jaiswal: Yeah. Yeah. Can you see here?

sampath vemulapati: data

Yogesh Jaiswal: Uh yeah. Here. Data scraping.

sampath vemulapati: Okay. Okay.

Yogesh Jaiswal: API ser phantom booster rapid API easy scraper and rows octopars. But I think um the more you understand what every tool does, if you if you can create a sheet and if you have your own oneliner,

sampath vemulapati: Yeah.

Yogesh Jaiswal: I you can easily win the market because no one is spending time on this,

sampath vemulapati: Yeah.

Yogesh Jaiswal: Right? People are trying to do the work of bon through zenros. Okay? There is a reason why this tool exist.

#### 00:48:07

sampath vemulapati: Yeah.

Yogesh Jaiswal: I mean uh the more you understand that the tool this is called a tool works properly I think you can easily win the market. You have project management. I think there are there are a lot of tools here and you should check out I this is what I do every day.

sampath vemulapati: Yeah. Great.

Yogesh Jaiswal: I mean um so I've shared this link to

sampath vemulapati: Sure.

Yogesh Jaiswal: you just try to pick one area don't pick everything at once pick let's

sampath vemulapati: Right.

Yogesh Jaiswal: say let's say you pick specialized database okay do you know what is store

sampath vemulapati: Yeah.

Yogesh Jaiswal: leads the store leads provide e-commerce

sampath vemulapati: Uh no.

Yogesh Jaiswal: data yeah so how do I know it because

sampath vemulapati: Okay. Okay.

Yogesh Jaiswal: I've used it right so that would be My advice is see now you have this influencer website. I don't know what is this. So it gives you influencer data.

sampath vemulapati: influences data. Yeah.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Now now people are sitting find finding this data in Apollo and clay.

#### 00:49:09

sampath vemulapati: Yeah.

Yogesh Jaiswal: What if you use this tool and these tools will not be expensive. Okay.

sampath vemulapati: Sure.

Yogesh Jaiswal: This is expensive but uh generally tools start from $19 $20.

sampath vemulapati: $19 like typically how the cloud is.

Yogesh Jaiswal: Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Yeah. Okay. So, let's go back. Yeah. So, pick pick a niche. Uh let's say you pick SEO and just go open understand what it does and write your oneliner.

sampath vemulapati: All right.

Yogesh Jaiswal: Okay. And I think that's the best way you can master everything. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Cool. Um let's go back to scraping. Okay. Yeah. So, one thing I want to mention here is um we are going to do this in Slack and Nit and uh web scraping HTTP API and everything. Okay. And I think you have already used Clayent. Clayent is doing the scraping part only. Okay. Now the one thing I want to and I that's the reason I kept very theoretical today.

#### 00:50:17

Yogesh Jaiswal: One thing I want to mention is a good clay table should only take you to only takes two to three hours to build. Right? Uh this is where many people are not going really good like doing really good in GTM engineering because they're taking a lot of time. Okay. I want you to be learn how to be conservative of time. Right? So if I ask you select a company and build uh a clay table around it, it's very easy. Select a company, build the document that might take 2 hours. Then you might go to clay and you just build a company table, run signals what which you have. Then move to a people table and run enrichments and validate the emails. Okay, we need to be understand that if you're not conservative in UTM engineering, someone is going to spend $23,000 a month on you. Okay, and if you are taking more than what is required, then definitely it's going to be a problem like you might not work with them for a long time and I have even faced this when I was new in the market.

#### 00:51:25

Yogesh Jaiswal: um like one and a half year back I was doing a task which is which can be done in 2 hours in 2 3 days okay so what I want to mention is let's also be conservative on time if we start building something and this is where engineers are doing an amazing job I mean you give this task to a person who is a engineer right who is solving problems every day he have an ETA to do a task Right? So let's also think more here from an engineering perspective that when we have to do something we need to find a way how to do it. Okay. So u try to spend some time in understanding how everything works how nit works and we are going to build a real automation around it. Okay. Uh yes. So, uh, Sar, have you built the clay table?

sampath vemulapati: Yeah, I have the trade table available but with those few leads only, not the entire 50 ones.

Yogesh Jaiswal: Yeah. If you also find like can you show if possible?

#### 00:52:28

sampath vemulapati: Yeah. Yeah, I'll just do that.

Yogesh Jaiswal: Yes. Yeah. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So, company name

sampath vemulapati: website and company employees.

Yogesh Jaiswal: Okay. Oh, you were doing the signals thing. Okay, got it.

sampath vemulapati: Yeah.

Yogesh Jaiswal: I think this this was just a practice. You need to rebuild this from a 50 company point of view. Um, oh,

sampath vemulapati: Yeah.

Yogesh Jaiswal: these are 50 companies, right? Then it got less to six.

sampath vemulapati: It got Yeah. Yeah. for all the signals and everything.

Yogesh Jaiswal: Uh-huh.

sampath vemulapati: Uh I scraped the data again from Raspio but it showed similar results actually. So from Drospio I uh why is it not showing up? Got logged out. again it's it's showing almost these number of companies as per my ICP

Yogesh Jaiswal: H so we need to understand that before we even jump to do anything in GTM engineering we need to understand if a company is doing very easy work like what goji bear is doing right the TAM should be huge okay your TAM should easily be 10,000 companies right in US uh and when you filter it out I mean so out of 60 only six are filled in That's a wrong math.

#### 00:54:35

Yogesh Jaiswal: Uh so try to think about this uh that when you run

sampath vemulapati: Good day.

Yogesh Jaiswal: signals at least 70% of companies should stay because already you're using prosperio right.

sampath vemulapati: Right. Right.

Yogesh Jaiswal: I mean you're already filtering the good companies.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So let's also think more and by the way filter company first and then people. Okay.

sampath vemulapati: Yeah.

Yogesh Jaiswal: Don't Yeah.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So I think you need to spend some time today and just need to think about it that if I have to filter out enrich companies in uh clay where at least

sampath vemulapati: Yeah.

Yogesh Jaiswal: 70% of companies should remain then you need to loosen down the signals.

sampath vemulapati: Okay.

Yogesh Jaiswal: Okay the signals should be loosened down because your signals are strict and this is called signaling uh methodologies. If you are having strict signals right then it's a problem.

sampath vemulapati: Yeah.

Yogesh Jaiswal: If you have loose signals like um any outreach tool they're using, I think you can easily get up to 70% companies. See at least 60% companies are good.

#### 00:55:38

sampath vemulapati: Right.

Yogesh Jaiswal: But if you are going down to less than 50% then you are doing something wrong.

sampath vemulapati: Yeah. Right. Right. So I'll I'll again get a secuded list of about like again 50 companies which are uh falling under my signals and then I'll again run it through uh clay then

Yogesh Jaiswal: Yeah. Also check if you're if it's really required to do signal uh uh qualification in play. If crossway is doing it then totally fine not a problem.

sampath vemulapati: yeah prospect I'm not doing it manually. Yeah.

Yogesh Jaiswal: Yes. No, I said like uh the qualification which we do and the signals that we run in uh the sorry the qualification parameter that we run in if it's doing in if it's happening in prospio then you don't need to do it in clay for example.

sampath vemulapati: Right. Huh.

Yogesh Jaiswal: Really?

sampath vemulapati: This is what uh is happening. So for example, I have um I think downloaded about uh 50. I I can also share my raw sheet.

#### 00:56:39

Yogesh Jaiswal: Mhm.

sampath vemulapati: Um so And just just give Yeah. So this is how my raw sheet looks like.

Yogesh Jaiswal: Okay.

sampath vemulapati: Let me name.

Yogesh Jaiswal: So these are the right companies you should reach out to.

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: Okay.

sampath vemulapati: So this is from Yeah.

Yogesh Jaiswal: then you don't need to uh then I think we are doing again filtering in play and that is the reason we are going into less numbers

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: so you need to think again rethink this I mean uh you need to use claude or GPT I think Lord is a good tool to use so try to rethink the strategy document again and now separate the strategy document and what needs to be done in procure what needs to be done in play.

sampath vemulapati: I'm destroy. Yeah.

Yogesh Jaiswal: Yes,

sampath vemulapati: Yeah. Yeah.

Yogesh Jaiswal: we are when we go unprepared to play, play is the worst place to be in because uh it gives you like you you don't know what to uh cook and you enter a kitchen with 10,000 ingredients.

#### 00:58:08

sampath vemulapati: Yeah.

Yogesh Jaiswal: I mean definitely you would spend like at least two three days understanding what I need to cook, what type of dishes.

sampath vemulapati: Right.

Yogesh Jaiswal: So let's we go prepared in clay and um the thing is called a clay execution logic.

sampath vemulapati: Right.

Yogesh Jaiswal: So when you go to claude or GPT um try to paste your strategy and say that build a clay execution logic also.

sampath vemulapati: Okay.

Yogesh Jaiswal: So it will give you where to use clay where not to use clay.

sampath vemulapati: Understood. Understood.

Yogesh Jaiswal: Yeah, because I think the company sourcing you're using clay and for uh qualification also you're doing in pro and also you're doing in uh this yeah so I think two parameters are

sampath vemulapati: Clear. Yeah. I mean it's become double qualification. So maybe Yeah.

Yogesh Jaiswal: yeah maybe not needed like uh qualification that we are doing

sampath vemulapati: Yeah.

Yogesh Jaiswal: Okay.

sampath vemulapati: But one thing I was also understanding Yogeshis when we apply the same filters like the same way in clay versus um even in prospio but like the lead count should not be less right like it should be as it is whatever prosp has qualified clay should also qualify the same what I'm not being able to understand is like why there is a

#### 00:59:24

Yogesh Jaiswal: Thank you.

sampath vemulapati: difference between the numbers uh maybe clay's data is more updated treated than cross pure. It can also be one of the cases that

Yogesh Jaiswal: Definitely the data of clay would be better because clay is using advanced tools. Right now if you do a funding filter in procio if you again do it in crunchbase definitely crunch base will deliver better result.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So you need to understand that does the company require strict filtering or not. Okay, just imagine um uh a store like Zara, right?

sampath vemulapati: Yeah.

Yogesh Jaiswal: I I'll give you a very good example. Uh Zara doesn't care about who enters the store, right? He knows that someone will enter and the type of customers will enter and buy it. So,

sampath vemulapati: Yeah.

Yogesh Jaiswal: they are still open to everyone. So, for the for the same reason, companies are also open to outreach anyone. Not a problem. I mean,

sampath vemulapati: All right.

Yogesh Jaiswal: you're not wasting your time, right? You can still reach out to companies where you have a slight possibility to sell and you can sell it.

#### 01:00:31

sampath vemulapati: Yeah.

Yogesh Jaiswal: That's why

sampath vemulapati: And I was also hoping to download more data so that like whatever data can go away at least I'll stay back with 30 40 at least of the companies is what I'm just hoping instead of downloading 50 and then like I downloaded only 50 uh leads from Prospio. So which in turn became very thin. I'm just hoping to download more data and then let it go whatever is not being qualified as per the signals.

Yogesh Jaiswal: Yes, perfect.

sampath vemulapati: Yeah.

Yogesh Jaiswal: I think let's close this clay loop tomorrow because we are going to uh move

sampath vemulapati: Yeah.

Yogesh Jaiswal: to email deliverability. So the plan is we are going to do every automation related thing at the end because I think you cannot build an automation when you don't understand how everything works.

sampath vemulapati: Yeah.

Yogesh Jaiswal: So now we'll move to email deliverability right and there are a lot of things to learn but side by side we we are going to keep building a clay table perfect okay uh unless we have a good clay table of uh an outreach that's a very basic step we cannot move to the new tables okay and it's fine to take time no need to rush I mean that's totally

#### 01:01:42

sampath vemulapati: Yeah.

Yogesh Jaiswal: fine cool uh

sampath vemulapati: Sure. Thanks. Thank you.

Yogesh Jaiswal: any yes So uh in the previous back also people are still connected to me and they're still progressing in where they have missed. So that's totally fine. I think what I'm trying to show here is a strategical thinking that we need to build as a GTM engineer because a good GTM engineer will never left things uh perfect right it it will always be perfect in in uh in what a GTM engineer does in in place. So uh imperfect sorry now will make sure it's perfect. So um when you have a task in play that needs to be completed so that needs to be completed and be perfect. Okay cool.

sampath vemulapati: trouble.

Yogesh Jaiswal: I think uh any questions gag anything?

Gagan Bhaisa: Uh, no, I'm good. Uh, would you mind taking my this table?

Yogesh Jaiswal: Yeah please please.

Gagan Bhaisa: I think I completed.

Yogesh Jaiswal: I thought you have not built it. Yes.

Gagan Bhaisa: Just give me a sec.

#### 01:02:52

Gagan Bhaisa: Let me Uh yes, I'm just trying to move this part of the profite. So, okay, I mean, let me go back to the company. This is what the company looks like.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: I have like 50 odd company. I mean 47 or something. You have 47 odd company and they have a website,

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: they have LinkedIn, I have enriched data, they have a domain, they have a size, they have industry, they have an Android revenue. Uh one of the compliance that works pretty well for me. Uh I mean a signal just to make sure they are qualified or not. And then what I saw is basically to make sure they are SO2 compliant. Okay.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: What is this? SO2 compliance is mostly anyone who is compliance with VAT uh other tool SOC uh maybe governments and compliance part. So if you look into anything they have a this is a I mean advanced version of qualifying and companies uh okay and they say they are actually SOC2 compliance with this industry.

#### 01:04:18

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Thank you.

Gagan Bhaisa: But there are other uh compliance which we can basically target. I have not added it. When you see no public evidence found, right? So this is actually a qualified company but with this

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: SOC2 compliance is not qualified. Okay. But it's actually it's actually a qualified company for my target audience and but I would be building another one to make sure they are qualified. But as of now 47 companies are actually qualified. And then when I go to my people section I have uh targeted uh yeah uh VP director head manager. Why? Because this kind of role technically uh there is not broader I mean not bigger uh audience like human resource or member of technical staff. These are more specific related uh I mean roles and responsibilities which maybe in a company there are hardly two or three guys who handles. So I had to forcefully take a managers to make sure I broader my audience part and then move to people who looks for technology security, DevOps, engineering, appsac application security, platform security.

#### 01:05:35

Gagan Bhaisa: Uh see

Yogesh Jaiswal: Okay.

Gagan Bhaisa: I'll just add it later on.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: uh platform security.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: Uh, I think I just uh app security. with E. Yeah. So, yeah. And then I wanted people from uh states, United Kingdom, India. And like if I go back to the same sheet, I got almost uh like 50 is showing uh since this is a free account 109 I mean 159 is not available it's asking you to upgrade but this is what the data looks like I have a city I have enriched everything like full name last name first name last name full name job title country city state country LinkedIn profile and then try to add another layer of enrich people which gives me what the collection looks like what the looks like,

Yogesh Jaiswal: Okay. Okay.

Gagan Bhaisa: what the summary looks like, what is the job count. Uh so I mean I don't know where this comes from. uh but yeah so this is all about uh this summary gives me a more valid point why I should reach out to them because these people are based on summary these are more qualified people to me because in this uh I mean 2026 what is happening somebody who has a different summary but a different title let's say platform engineering so platform engineer ing can be two thing one can we move into

#### 01:07:39

Gagan Bhaisa: a platform security also can we move into a somebody who builds a platform so I don't want to reach out to anybody who want to build a go for a build a platform I want somebody who are more into

Yogesh Jaiswal: I'm

Gagan Bhaisa: security part so this makes me more important and then like try to add my work email uh let me do a configuration But I can use a zero bounce. And then now looking for all 50 guys.

Yogesh Jaiswal: Yeah, I think this looks good. Um,

Gagan Bhaisa: Yeah. And then I going to go and add a value name value.

sampath vemulapati: Uh, Yog and Gag, I just have to drop off to another meeting.

Yogesh Jaiswal: Yeah, sure. Sure.

Gagan Bhaisa: Hey,

Yogesh Jaiswal: That's fine.

sampath vemulapati: Thanks. Thanks so much.

Yogesh Jaiswal: Welcome.

sampath vemulapati: Bye.

Gagan Bhaisa: man.

Yogesh Jaiswal: Have a nice day.

Gagan Bhaisa: Yeah. This is

Yogesh Jaiswal: Yes.

Gagan Bhaisa: uh uh any constructive feedback on here. What did I I mean what wrong I did.

#### 01:12:16

Yogesh Jaiswal: I think from the past time you have built this looks much perfect. Um one thing if you want to make it better is if you use less columns uh like for every small detail you have a new

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: column.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: The problem is when you scale it becomes uh difficult.

Gagan Bhaisa: Yes. Yeah.

Yogesh Jaiswal: So the only for feedback is if you can do everything in less columns

Gagan Bhaisa: Mhm. Got it.

Yogesh Jaiswal: rest everything looks good.

Gagan Bhaisa: Got it. So, I think we don't need this one. We don't need this one. We don't need this one. Hide it. What's this headline person? Yeah. I mean, now it's pretty clean.

Yogesh Jaiswal: Yes, it looks better now. I think this is good what you have built.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Um, yeah, I think this is what I was talking about to have a good play table. Yeah, I think we can easily build a messaging now and we have all the information to build a good messaging.

#### 01:13:50

Yogesh Jaiswal: So yes, I think this is good. Good progress.

Gagan Bhaisa: Garbage.

Yogesh Jaiswal: Uh from the company table,

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: can you get some kind of company messaging to the people table using lookup?

Gagan Bhaisa: I can do that.

Yogesh Jaiswal: Yeah. So because see when we build the messaging we are going to use the people column, right?

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: A people table and there is no information because the summary is also not there for everyone. So we can use the headline to build messaging. Uh but also if we can use a company parameter. So yes.

Gagan Bhaisa: Look up record

Yogesh Jaiswal: Yeah. Look up single records. Yes.

Gagan Bhaisa: custom or Clay.

Yogesh Jaiswal: No, no, not evidence summary. Uh you should map it with company name.

Gagan Bhaisa: Oh. Uhhuh.

Yogesh Jaiswal: Yeah, company name contains company name here. Yeah, company name. Yeah, just output the S. Yeah. Cool. Cool. That's That's right. Perfect. Yeah, I think this is good. Mhm. Good. Good. Good. Yeah, this is all what we needed. Cool.

Gagan Bhaisa: Got you.

Yogesh Jaiswal: I think this is enough to build a good message.

Gagan Bhaisa: Mhm. Yeah. Uh yeah. Cool. Then hey, also one thing uh I mean now we are uh I mean this is off the topic.

Yogesh Jaiswal: Mhm. Sure.

Gagan Bhaisa: I mean we we can stop the recording and then talk after

Yogesh Jaiswal: Sure. Okay. Okay. Sure. I'll just Yeah.

Gagan Bhaisa: the

Yogesh Jaiswal: Yeah. Just a second. Uh

#### Transcription ended after 01:16:12

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.