# D25+D26_ Ship_ an efficient scored pipeline + Claygent — AI research at scale - 2026_09_24 08_57 IST - Notes by Gemini


## ✍️ Quick notes

Please rate the new Quick notes tab by taking a short survey.

### D25+D26: Ship: an efficient scored pipeline + Claygent — AI research at scale

Sep 24, 2026

Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mahima jaiswal mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Signal strategy discussion and compliance testing with Lantern AI targeting setup

GTM signals and compliance qualification strategies

Qualification signals effectively filter target companies without requiring excessive data points.

Gagan utilized manual formulas to verify SOC2 compliance across 50 target companies.

Gagan flagged AI research agents as unreliable for accurate compliance validation.

Yogesh noted that funding history remains secondary for security and AI software companies.

Lantern AI product capabilities and target market definition

Lantern operates as an AI hiring manager that screens profiles and pressure tests roles.

Lantern targets high-growth companies maintaining dedicated recruitment teams and high-paying roles.

Yogesh estimated Lantern pricing at 10,000 dollars per year for enterprise clients.

Clay table building and qualification parameters

Neeraj filtered software development companies in Germany and the Netherlands using Clay.

Gagan added qualification parameters tracking job postings open for over 30 days.

Yogesh emphasized targeting roles where hire quality outweighs hiring speed.

Lantern company qualification criteria

Yogesh directed building a company qualification table for Lantern using website research.

Qualify companies with more than 10 active job postings indicating hiring focus.

Qualify companies with internal recruitment teams while excluding those using agencies.

Target markets in Germany, the Netherlands, or another selected territory.

Clay platform prompts and job posting enrichment

Gagan updated JSON schemas and prompts to output job titles, dates, and statuses.

Leveraged active job posting searches through LinkedIn scraping to gather recruitment data.

Next steps

[Gagan Bhaisa] Redo Clay Table: Reconstruct the Lantern AI prospect table by correctly applying qualification and disqualification logic. Ensure that the AI response parameters and JSON schema are preserved to avoid deleting output data.

[The group] Build Qualification Table: Define criteria to identify which businesses are eligible for the Lantern service. Research specific territories such as Germany or the Netherlands to gather insights.

[Yogesh Jaiswal] Develop Reference Example: Create a sample document over the weekend to demonstrate the ideal format for client identification. Share this resource to assist the team in mastering GTM engineering exercises.

Want to see more? View the full notes
Tip: You can always access your full notes from the left sidebar.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

## 📝 Full notes

Sep 24, 2026

### D25+D26: Ship: an efficient scored pipeline + Claygent — AI research at scale

Invited Rithika Murthy Alok artifabiyani5@gmail.com Gagan Bhaisa ddeepshikha.raghuvanshi@gmail.com Yogesh Jaiswal Shubham Gosavi heshitosh k hrishikeshpuri.hp@gmail.com jigisha2306bhatnagar@gmail.com khushboosells@gmail.com LIKKI GAYATRI REDDY medhadas06@gmail.com nrj127@gmail.com sampath vemulapati santoshsadhu18@gmail.com Sheikh Shaif shiiv.shanker@gmail.com sonirohitr@gmail.com sowmya.anand100@gmail.com suraj10bhandari07@gmail.com Vinothan A Yash Jain Keya Gupta mahima jaiswal mohammedshabaz7676@outlook.com sagarsuccena@outlook.com

Attachments D25+D26: Ship: an efficient scored pipeline + Claygent — AI research at scale

Meeting records Transcript Recording

#### Summary

Signal strategy discussion and compliance testing with Lantern AI targeting setup

Signal Strategy And Compliance
Evaluation of market size and qualification signals established target criteria. Compliance signal testing resolved contradictory results using manual formula filtering.

Clay Setup For Lantern
Participants configured Clay filters and prompts for Lantern AI targeting. Target company size and funding parameters were defined for international regions.

Workflow And Qualification
Recruitment team analysis and job posting duration metrics established qualification logic. Team members were assigned territorial qualification tables for outreach execution.

#### Decisions

Aligned

Company qualification criteria for job postings Companies with more than 10 job postings and an internal recruitment team should be qualified.

#### Next steps

[Gagan Bhaisa] Redo Clay Table: Reconstruct the Lantern AI prospect table by correctly applying qualification and disqualification logic. Ensure that the AI response parameters and JSON schema are preserved to avoid deleting output data.

[The group] Build Qualification Table: Define criteria to identify which businesses are eligible for the Lantern service. Research specific territories such as Germany or the Netherlands to gather insights.

[Yogesh Jaiswal] Develop Reference Example: Create a sample document over the weekend to demonstrate the ideal format for client identification. Share this resource to assist the team in mastering GTM engineering exercises.

#### Details

Signal Strategy in GTM Engineering: Gagan Bhaisa raised a problem regarding how to determine the minimum signal count to target when multiple signals fail for a company. Yogesh Jaiswal argued that companies must first evaluate their Total Addressable Market and market size, explaining that signals are unnecessary if market reach is small because signals disqualify companies. Yogesh Jaiswal noted observing companies succeed without signals while others spent $2,000 monthly on Clay with unsuccessful signals (00:02:22). Yogesh Jaiswal concluded that qualification signals alone are sufficient (00:04:10).

Compliance and Security Signal Testing Challenges: Gagan Bhaisa presented an analysis of artificial intelligence penetration testing and security companies testing compliance signals such as SOC 2, HIPAA, or ISO certification, identifying a problem with artificial intelligence data reliability producing contradictory results where text indicated compliance while compliance push flags marked false or medium (00:04:10). Gagan Bhaisa built a manual formula in the sheet resulting in 32 out of 50 companies marked as compliant, which Yogesh Jaiswal praised. Gagan Bhaisa and Yogesh Jaiswal agreed to filter out recent funding from 12 months prior and instead focus on leadership hires like CEOs, CTOs, VPs of engineering, and directors rather than general recent hires (00:06:29).

Hook Generation and Messaging via Market News: Yogesh Jaiswal stated that after qualifying companies, messaging should incorporate hooks based on market news, acquisitions like Fleet acquiring Pando, product expansions like Zoho expanding to Australia, or funding information (00:08:58). Gagan Bhaisa expressed skepticism about Claygent generating reliable data, preferring static data and stating Claygent provided inconsistent, fabricated data across accounts. Yogesh Jaiswal acknowledged that Claygent uses artificial intelligence and has inherent limitations (00:10:01).

Introduction of Lantern AI and Practical Table Exercise: Yogesh Jaiswal introduced a live practical exercise using Lantern AI, a company targeting the United States market, and asked participants to study its operations and build a single Clay table with Claygent elements (00:11:05). Deepshikha stated they were commuting and joined from a phone, prompting Yogesh Jaiswal to ask Neeraj Sujan to share their screen instead (00:12:20).

Analysis of Lantern AI's Product and Value Proposition: Medha Das and Neeraj Sujan analyzed Lantern AI using its website and Y Combinator page, describing it as an artificial intelligence-first hiring manager and staffing platform that screens profiles, handles end-to-end hiring workflows, and acts as a reactive agent handling interview feedback without making final hiring decisions (00:13:39). Yogesh Jaiswal clarified that Lantern AI eliminates applicant tracking systems and focuses on high-growth, high-paying jobs rather than associate roles, targeting companies with strong artificial intelligence budgets and recruitment teams (00:17:10).

Setting Up Clay Filters for Lantern AI Target Companies: Neeraj Sujan created a new Clay workbook to find target companies in the technology sector including information technology services and software development in Germany and Netherlands to avoid United States competition (00:21:33). Regarding company size, Gagan Bhaisa suggested 11 to 50 employees, whereas Yogesh Jaiswal argued that companies of 11 to 50 employees would not purchase an expensive hiring tool because they hire very few people annually (00:24:19). Yogesh Jaiswal and Neeraj Sujan ultimately agreed to target company sizes of 51 to 200 and 200 to 500 (00:26:28).

Refining Clay Filters and Addressing Free Plan Limitations: Neeraj Sujan experienced issues with Clay's free plan filtering countries and company sizes, while Gagan Bhaisa stated the free plan worked for Gagan Bhaisa (00:27:17). Yogesh Jaiswal instructed Neeraj Sujan to add funding filters of 1 to 5 million and 5 to 10 million along with private company types, while removing annual revenue filters to prevent limiting results, and requested saving and running 10 rows (00:28:53).

Developing Job Posting Qualification Prompts in Clay: Neeraj Sujan addressed the problem of identifying active hiring pain points, proposing that companies with job postings active for 30 days or more indicate a struggle to find talent. Yogesh Jaiswal approved this parameter, and Yogesh Jaiswal instructed Gagan Bhaisa to write the Claygent prompt checking for domain-specific open job postings exceeding 30 days (00:32:39). Neeraj Sujan focused specifically on high-demand roles like forward-deployed engineers and artificial intelligence engineers where supply is low (00:33:45).

Evaluating HR Team Size and Recruitment Team Analysis: Neeraj Sujan suggested checking for leadership changes, but Yogesh Jaiswal noted tracking closed deals or C-level hires is difficult and instead requested checking the size of the company's recruitment team to identify lean teams needing assistance (00:36:47). Gagan Bhaisa executed a find contact action in Clay using job functions filtered for human resources and recruitment mapped to the company domain (00:37:46). Reviewing the output, Yogesh Jaiswal observed that companies like TL;DV lacked a recruitment team entirely, leading Yogesh Jaiswal to conclude that such companies would rely on agencies rather than purchasing Lantern AI (00:41:31). Neeraj Sujan asked if they could sell directly to staffing agencies, but Yogesh Jaiswal explained that companies partner with agencies rather than selling tools to them (00:43:20).

Implementing Qualify and Disqualify Logic Prompts: Yogesh Jaiswal instructed Gagan Bhaisa to write a qualification and disqualification prompt based on artificial intelligence responses, specifying that a company qualifies when job postings are open for over 30 days and there is one or more person in the human resources team, with all others disqualified (00:44:35). Gagan Bhaisa encountered errors resulting from deleted fields and missing JSON schema. Yogesh Jaiswal guided Gagan Bhaisa to select the OpenAI model via JSON schema generation from the prompt to restore proper fields (00:46:49). Yogesh Jaiswal confirmed the final logic that open roles over 30 days combined with a recruitment team constitutes qualification (00:52:09).

Refining Role-Based Qualification and Target Market Economics: Yogesh Jaiswal and Medha Das discussed whether Lantern AI should target all open roles or specific technical roles, with Medha Das noting that Lantern AI's actual clientele includes education, hospitality, legal services, real estate, and construction (00:52:09). Yogesh Jaiswal argued that roles like care manager or sales executive involve lower compensation and smaller human resources teams, making it unlikely for companies to spend approximately $10,000 annually on Lantern AI (00:54:42). Yogesh Jaiswal emphasized that Lantern AI focuses on hiring quality rather than speed and advised focusing on technical roles like quality assurance engineers, business intelligence development managers, and paid media account managers where job postings remain open despite having recruitment teams (00:56:16).

Lantern Company Qualification Table and Prompt Editing: Yogesh Jaiswal instructed Medha Das to build a proper qualification table for Lantern by researching the company and its website to determine which companies to qualify or disqualify based on what Lantern sells. Additionally, Yogesh Jaiswal directed Gagan Bhaisa to modify the first prompt by editing the JSON schema, generating from the prompt, saving, and running it again for 50 rows, noting that they could delete the first column.

Job Posting Data Extraction and Enrichment: Yogesh Jaiswal guided Gagan Bhaisa through the software interface to output job titles, posted dates, and open statuses, explaining that open posts older than 30 days are still useful for outreach. Gagan Bhaisa questioned whether active job postings should be filtered by department, to which Yogesh Jaiswal clarified they should not, and Yogesh instructed Gagan to add a job posting enrichment column using LinkedIn scraping and run a test of 10 rows.

Company Qualification Criteria and Territorial Targeting: Yogesh Jaiswal established the rule that companies with a job count of anything plus 10 should be qualified due to their hiring focus, provided they have an internal recruitment team rather than relying on external agencies. Yogesh Jaiswal tasked Medha Das, Neeraj Sujan, and Gagan to build this qualification table, suggesting they could use Claude for assistance and select territories such as Germany, the Netherlands, or a region of their choice.

Go-To-Market Engineering Workflow and Next Steps: Yogesh Jaiswal emphasized that the primary context of the meeting was to make fast decisions in Go-To-Market engineering by quickly understanding companies, building qualification tables, qualifying or disqualifying contacts, and extracting email addresses and URLs for outreach. Yogesh Jaiswal committed to building a sample table in Clay over the weekend to demonstrate the process to the team, and invited participants to post any questions in the group.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

## 📖 Transcript

Sep 24, 2026

### D25+D26: Ship: an efficient scored pipeline + Claygent — AI research at scale - Transcript

#### 00:02:22

Gagan Bhaisa: Hey, you guys.

Yogesh Jaiswal: Hey, good morning again.

Gagan Bhaisa: Hey. uh Yogesh I was trying to uh finish the yesterday assignment.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: So few things just like let's say if multiple uh signal doesn't works for a company I mean what is the minimum signal that we're going to target is it a three is it a five is it a oneh

Yogesh Jaiswal: See first of all I think we need to understand that our signals really required for that company. So we you need to check that how big is the TAM right

Gagan Bhaisa: Okay.

Yogesh Jaiswal: then how big is the market you are reaching out to okay if there are if there are not lot of companies like so many companies

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: then no need of signals because signal will disqualify a lot of companies right so

Gagan Bhaisa: Yes. Yes.

Yogesh Jaiswal: uh I want to give you a real market check that signals is good But we need to only set a boundary that this should be qualification signals.

Gagan Bhaisa: Yes.

Yogesh Jaiswal: So you need to now think more because you know this only comes when you think strategically because I have I have seen companies doing amazing GTM engineering without any signals right.

#### 00:04:10

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Uh I have seen companies spending $2,000 in clay a month and they are not doing any anything good. I mean they are doing every kind of signal and nothing is working.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: So I think qualification signals are enough. If you qualify the company uh on any parameter those are enough.

Gagan Bhaisa: Yeah. So, I mean, okay, let me quick uh bring my screen here.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: What I'm trying to say? Uh, okay. Do you see my screen?

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Uh,

Yogesh Jaiswal: Yes.

Gagan Bhaisa: okay. share the one.

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: Okay. So since you know this company mostly sell to any tech companies in the industry mostly AI penetrating testing your security solution and everything. Okay.

Yogesh Jaiswal: H.

Gagan Bhaisa: So see let's say one of the strong signal I would say uh not a strong signal but compliance uh security uh it should be a SO2 or HIPPA or ISO certified. Okay.

Yogesh Jaiswal: Mhm.

#### 00:05:08

Gagan Bhaisa: any company should be this one so that this company can buy all this solution. Okay. So I basically use the AI to uh write me give me an evidence. Okay. So two things what I find uh it's kind of a BS to me. Why I'm saying BS to me is like let's say here is saying visit one SO2 compliance document and indicate it was last verified in 26 921 okay but when you and

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: it says has compliance push it say false okay which means that uh basically AI is kind of bluffing me around say that yes it's it's a compliance but we are also saying It's not a I mean high intent or something like they have never posted uh like that.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: So if you go to here uh this part huh restore a new dated stated that company certified with SO2 type two which is one of the I mean top SO2 certifications. Okay. But when you go here it says medium. Okay, it doesn't gives you I mean say that no this is not.

#### 00:06:29

Gagan Bhaisa: So what I have I have done manually say that so mentioned or not. try to pull all the evidence into one sheet and say that if any of this mentioned in the evidence or not.

Yogesh Jaiswal: Oh, you have the formula.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: That's nice.

Gagan Bhaisa: Yes. And it says yes out of 50 companies it's uh like almost 36 are it says we are compliance.

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: Uh yes it says out of 50 company 32 say we are compliant but if I go to on this part it says true false or

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: medium it's actually uh giving me a block answered it works or not

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: okay this is one challenge I found out second uh for this kind of company uh technically the funding would not

Yogesh Jaiswal: Yeah,

Gagan Bhaisa: allow Huh?

Yogesh Jaiswal: funding is not a big deal here.

Gagan Bhaisa: Funding would not allow. Uh also I see uh the recent hire would not be an uh uh I would say ideal but I would rather go find people who move to a leadership position for all this company to run the business.

#### 00:07:47

Gagan Bhaisa: So let's say any seesuit like these are mostly a software development company right?

Yogesh Jaiswal: Mhm.

Gagan Bhaisa: So they are building a product. Anyone who is in CEO like that can be a security officer, that can be a CTO, that can be a VP of engineering, that can be a director, that can be anyone who is in marketing. Okay, I think that would work because now since this company has evolved and they kind of move into a different space. So with this certification and then the CEO hire without any relevant department, I think that would work for me.

Yogesh Jaiswal: Got it. Yeah, I think the formula method was great which you have used. Uh the qualification works perfect but you can remove the recent funding. I think recent funding is

Gagan Bhaisa: No, I think this this doesn't work for me. I just trying to do a test uh early morning. It doesn't works for me.

Yogesh Jaiswal: the first test is good.

Gagan Bhaisa: So I mean uh any anything I mean they have been funding uh like they have taken funding but that's a pretty 12 months before uh I mean old which is on 24 25th 25th early so that's uh I mean data I'm

#### 00:08:58

Yogesh Jaiswal: Yes. Also few things about messaging see you do qualify the companies that's totally fine right you need to also understand when when we talk about messaging right so I'll show you something you know this company Pando got acquired like a month back by another company

Gagan Bhaisa: Mhm. Yeah.

Yogesh Jaiswal: called fleet xi fleet yeah so can you catch these kind of

Gagan Bhaisa: Yes. Yes.

Yogesh Jaiswal: news right so you know it's today we only run one prompt per company that um research about the company and catch one information that we can use as a hook in the messaging. These can be funding related information, any news in the market,

Gagan Bhaisa: Yes.

Yogesh Jaiswal: anything. So I think you can also run that parameter prompt that and you can also

Gagan Bhaisa: Yes.

Yogesh Jaiswal: explain to the founder that okay I don't want to miss any critical information. What if the company launched a new product and uh that's not related to hiring or funding, right?

Gagan Bhaisa: Yes.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Yeah. I mean mostly a product expansion or something like that.

#### 00:10:01

Yogesh Jaiswal: Yes. Maybe they are expanding to a new office like Zoho is expanding to Australia now.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Zoho.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: So we can only get this information in Claygentwhen we search for this information.

Gagan Bhaisa: uh but like I'm not sure about but clay agent seems to be BS to me. So I would rather prefer the static data. Uh so every time I run a clay agent I mean in fact not here I also build a clay agent inside my company's clay account.

Yogesh Jaiswal: Okay.

Gagan Bhaisa: Uh so every time it's give me a BS uh this form I mean data every time it's a different data so maybe I mean

Yogesh Jaiswal: Maybe I think uh uh

Gagan Bhaisa: it works in a different industry to industry uh but like for us is actually clear doesn't works

Yogesh Jaiswal: yes it's still an AI so I think we cannot do

Gagan Bhaisa: yeah yeah you know that's that's what I choose this part like uh

Yogesh Jaiswal: much. Yes.

Gagan Bhaisa: run everything say that give me the evidence and what are the parameter that this this actually takes true or compliance.

#### 00:11:05

Gagan Bhaisa: So then use a formula say that okay this is kind of compliance.

Yogesh Jaiswal: Got it. Perfect. So, um yeah, that's that's good. Uh so, hi hi Dika Na. How are you guys?

Neeraj Sujan: Hello. All good.

Yogesh Jaiswal: Yeah,

Gagan Bhaisa: Hey guys.

Yogesh Jaiswal: perfect. So, uh yes, so I have shared a company uh on WhatsApp. Okay. The company's name is Lantern AI, right? So, we just I mean we just want to do a simple exercise today that uh how well you have the knowledge in shipping a complete table and clay or building something. So uh I will share my screen and uh Yes. Yes. So this is the company and you need to do something creative with the company. They want to sell in the US, right? So you want to build a very simple this is you can consider it as a uh maybe uh practical something that we are going to do live. Okay. Anyone can share the screen and start building.

#### 00:12:20

Yogesh Jaiswal: Um yeah. So you need to study the company what they are doing. Right. So you can even open the website. Okay. Yeah, we need to open the website. Have a look into it. What they are doing, whom they are selling and just build a clay table for it, a single clay table. And there should be more of clay joints to make this table perfect, right? Okay. But I'll help you out. That's uh something I'll take care of. So anyone would like to share the screen and do that. I mean others can also do side by side like Deepshikha,Medha,Neerajanyone?

Deepshikha: Um, Yogesh, I think I've missed out on your question. I'm a little loud. So, would you mind repeating yourself?

Yogesh Jaiswal: Yeah. Can you share your screen to play and uh practice?

Deepshikha: Yeah.

Yogesh Jaiswal: Yeah,

Deepshikha: Actually,

Yogesh Jaiswal: we are.

Deepshikha: yeah. The thing is I'm commuting. I have joined from phone.

Yogesh Jaiswal: Oh, okay.

#### 00:13:39

Yogesh Jaiswal: Okay. No,

Deepshikha: Oh,

Yogesh Jaiswal: that's that's fine.

Deepshikha: yeah.

Yogesh Jaiswal: That's fine. Yeah. N you are there on your on your Yeah.

Neeraj Sujan: Yes.

Yogesh Jaiswal: Can you share your screen to

Neeraj Sujan: Uh, just a second. I need to

Yogesh Jaiswal: Yeah. I think most of the times Gagan was sharing so I thought let's pick a new person.

Neeraj Sujan: do I need a paid plan of play.

Yogesh Jaiswal: No, no, no.

Neeraj Sujan: Just give me 2 minutes.

Yogesh Jaiswal: Yeah, sure. Sure. Yeah. Yeah. But meanwhile, Gagan, when you have a look into this company, MedhaGagan,what do you think what they do?

Medha Das: So basically, Yogesh from what I understood is uh instead of I mean it first of all the company helps into hiring. I mean mean there are no hiring uh resources and instead of a like a person screening the profile uh we are using AI to do the initial

Yogesh Jaiswal: Mhm.

Medha Das: screening I mean that's what I'm I mean just going through the website of IC combinator so

#### 00:15:34

Yogesh Jaiswal: Mhm.

Medha Das: they uh I mean they use AI to screen profiles against various criter areas and also help in running like the end to end hiring like from scoring to I mean having I mean assessing the profile

Yogesh Jaiswal: Yep, that's correct.

Medha Das: having the communication and then ultimately like maybe offering the

Yogesh Jaiswal: Yep.

Medha Das: role

Yogesh Jaiswal: Yep. Uh uh N can you open the link which I shared on the meeting window the YC link like you can share and open the link.

Neeraj Sujan: Can you see it?

Yogesh Jaiswal: Yes. Yes. So now the question is what do you understand by what they do? I mean can you you can check the uh 5C page even the website.

Neeraj Sujan: Turn your taste into higher lantern lawn. What exceptional looks like? Yeah, I think it's a it's like a staffing agency that helps uh find the talent talent. Yeah, it's it helps other companies find the right talent without wasting a lot of time

Yogesh Jaiswal: Okay.

Neeraj Sujan: uh and gets them to an interview.

#### 00:17:10

Neeraj Sujan: So, it's like a staffing agency, modern AI first staffing agency. I think it's the same one that I sent you somewhat similar. Do you remember I had sent you one Dutch company Talentex

Yogesh Jaiswal: Yes. Yes. Yes. Yes. Yes.

Neeraj Sujan: uh and they are helping find the right candidates based on the requirements that the companies would be sending them what they are looking for. uh they match that with all the profiles and find find these people. Am I right or

Yogesh Jaiswal: Yeah. Yes. But it's if you go to the website, it says that it's a AI hiring manager. If you go at the top and if you see Yeah. Go up a bit up. Yeah.

Neeraj Sujan: Amen.

Yogesh Jaiswal: Can you see AI AI hiring manager? Yes. So, can you also open FAQ page? I'll it will just clear. Yeah. Yes.

Neeraj Sujan: which trade-offs matter and what candidates need to prove. It also pressure tests the role against the talent market and shows where standard openings your hiring goes to the people the market can actually offer attentions.

#### 00:18:38

Neeraj Sujan: Okay. Yeah. So I I guess it also helps in uh changing the job description or a bit based on based on the signals they are getting from the market.

Yogesh Jaiswal: Yes.

Neeraj Sujan: uh they also help in uh so it's a it's a reactive reactive agent

Yogesh Jaiswal: Mhm.

Neeraj Sujan: I guess hold back of a millia when the proof is weak and false positive without missing less less obvious person when counter evidence and unknown visible it can hold back a familiar looking profile when the proof is weak Yeah. So, yeah, it's it's doing a lot of checks uh and scoring. I I guess this is a scoring logic.

Yogesh Jaiswal: Yes.

Neeraj Sujan: And if it Yeah.

Yogesh Jaiswal: For the do you need an ATS?

Neeraj Sujan: No. S.

Yogesh Jaiswal: No.

Neeraj Sujan: No. Yeah. Talent.

Yogesh Jaiswal: So it's eliminating eliminating the ATS part also. I mean the tool part also.

Neeraj Sujan: Yes.

Yogesh Jaiswal: Okay. Are they also doing sourcing? Can you check sourcing the candidates? Oh no.

#### 00:20:10

Neeraj Sujan: No, they don't know.

Yogesh Jaiswal: Okay. Okay. Got it.

Neeraj Sujan: So what source the talent they just what is the end deliverable?

Yogesh Jaiswal: The deliverable is the right talent if you see.

Neeraj Sujan: So they do source right.

Yogesh Jaiswal: Okay. Can you go down? Can you go down? Yeah. I can just stay stick. Yes. So I think it's also a note taker because it stays in all the calls. Interview feedback change approval recorded session.

Neeraj Sujan: Mhm.

Yogesh Jaiswal: it never make the final hiring decision. Okay, let's just understand that companies who have good AI budgets

Neeraj Sujan: Mhm.

Yogesh Jaiswal: goods and who have a good recruitment team would buy lantern, right? Or do you want to add more things to it

Neeraj Sujan: Uh I guess it can also uh help start

Yogesh Jaiswal: or raise funds? Yeah,

Neeraj Sujan: help.

Yogesh Jaiswal: companies would raise funds, they would also more people

Neeraj Sujan: Yeah. even if they don't have a big HR team and can help uh for early stage startup to find the talent,

#### 00:21:33

Yogesh Jaiswal: Yes, also we need to be clear that these are for high growth jobs, high paying jobs, right? No one will use that to hire a an associate level person. These are like jobs where companies pay a lot and they don't want a bad talent, right?

Neeraj Sujan: right?

Yogesh Jaiswal: Okay. So now you need to make a clay table out of it, right? So the goal is to find few companies in US that we can sell to for lantern.

Neeraj Sujan: Mhm.

Yogesh Jaiswal: So can you go to clay? Yes. Uh uh new table. Yeah. New workbook. Yeah. Yes. File table. Okay, let's find companies first. I think that's a good idea. Yes. No, just click on the search filters and you will get the filter option up. Yeah. Up up up. No, no, this this search filters below criteria. Yeah. Yeah. So let's uh let's find the industry fit for this.

#### 00:22:52

Yogesh Jaiswal: So which industry do you think is going to be the top-notch fit for this?

Neeraj Sujan: Oh, okay. Wait.

Yogesh Jaiswal: Yes. Technology. Yeah. IT information technology and services. H

Neeraj Sujan: Okay. No.

Yogesh Jaiswal: technology. You have more technology if you go down. Yeah. Yes. Last two. Okay. Confirm. Yes. Yes. Software. Can you see software development industry?

Neeraj Sujan: Did you select or no?

Yogesh Jaiswal: Yeah. Yeah.

Neeraj Sujan: Good.

Yogesh Jaiswal: It's selected. It's in the left if you see. Yeah. Search software development. Oh, yes. biggest. Okay, thanks. You confirm. Yeah, now country is Yeah, let's go to country. Let's select a narrower country. I think US is going to be a big uh market. So, no, no, let's select a different country where um because you know there's a lot of competition in US.

#### 00:24:19

Yogesh Jaiswal: So, what if we try for a new comp country? Yes. Yeah, you can select Germany. Not a problem. Okay. Netherlands. Okay. Latin America. Yes, we can even do that. Yeah. No, not a problem. I think Germany is uh is fine. Perfect.

Neeraj Sujan: Mhm.

Yogesh Jaiswal: Uh company size. Yes. Yeah. Gagan, you can even mute. Not a problem. Um unmute. Sorry. Not a problem. Uh yeah.

Gagan Bhaisa: No, that that's okay.

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: I'm just trying to help like what I thought.

Yogesh Jaiswal: Yeah. So, what do you think a good in uh size is for lantern?

Gagan Bhaisa: I mean, anyone who has 15 to 200.

Neeraj Sujan: 5100.

Gagan Bhaisa: Yeah,

Yogesh Jaiswal: Yes,

Gagan Bhaisa: 15 to 200 and 100 to 50.

Yogesh Jaiswal: that's why 11 to

Gagan Bhaisa: Uh, sorry, 11 to 15 because nowadays people are running in a lean team

Yogesh Jaiswal: 50

#### 00:25:15

Gagan Bhaisa: and they want someone right fit. uh why 11 to 15 is basically let's say somebody wants a founding uh AI engineer or forward deployed engineer or uh I mean on a software development industry they're always this kind like they always give it to this company uh like AI hire software companies they they handle the all the GCC and the recruitment part of the

Yogesh Jaiswal: But I would yeah I would say that these people don't pay I think definitely lantern would be expensive and uh they would initially hire people by themsel only. I think I mean I don't know but this I have a strong feeling that an 11 to 50 employee

Gagan Bhaisa: Uh-huh.

Yogesh Jaiswal: company would not even buy a hiring tool because they would only hire two three people right in a year or four five people

Gagan Bhaisa: Yeah. So that's became more so I mean what I have into industry and saw it two things one they run hackathon and second they gives this kind of company to hire them uh to like hire all this specialist people what we call I mean if you can go to lantern do we have a pricing page that's clear

#### 00:26:28

Yogesh Jaiswal: No,

Gagan Bhaisa: like

Yogesh Jaiswal: I don't think they would say show the pricing right now.

Gagan Bhaisa: Okay.

Yogesh Jaiswal: Yeah. Yeah. No, companies won't show the pricing these days. Okay.

Gagan Bhaisa: Uhhuh.

Yogesh Jaiswal: I think let's let's do 200.

Gagan Bhaisa: I mean, let's take it. I mean, I would say 100 to

Yogesh Jaiswal: Yeah. 52. Uh yes. Can you go to uh the Clay?Uh,

Neeraj Sujan: Yeah, that's

Yogesh Jaiswal: yes. Uh, can you se go to the size? Okay. Very easy. Close this f. Close this. Uh filter. Yeah. Go to the left. Yeah. The size, right? Company size. No, no, no. Down. Down. Click on the company size. Yes. Yes. Just click on this. 51 to 200. No. No. 51 to 200. Yes. Yes. Add it here. Make it uh 200 to 500 also.

#### 00:27:17

Yogesh Jaiswal: I think this is also a good set of companies. Yes. Uh yeah, I think we are good now. industries, their country, their uh

Neeraj Sujan: No, there are no results. Maybe I add more countries.

Yogesh Jaiswal: yes, go to the country like how it's possible. Can you add United States? I think there is a problem with Clay.Yeah. Remove United States. Yeah. It's just not showing you. Yes. Click on continue. Yeah. Okay. I think Clay's free plan is now not working for uh companies filter. Company filters. That's why. H. Okay. Let's uh You have a paid

Neeraj Sujan: Let's I'm taking one minute

Yogesh Jaiswal: plan?

Neeraj Sujan: out.

Yogesh Jaiswal: Yes.

Gagan Bhaisa: Hey, it's it's actually working the free plans.

Yogesh Jaiswal: Working.

Gagan Bhaisa: Yeah, I can able to search the companies.

Yogesh Jaiswal: Yeah. So, I think it's fine. It's fine. Let's Can you share your screen?

#### 00:28:53

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: No problem. No problem. Yeah. I think clay is acting weird these days. So the free free plan of clay. Okay. Okay. Okay. It's working for you, right? So can you add the same filters, Gagen? Yes. So industries were software development. Yes. Yes. Uh, Germany and Netherlands. Okay, just a second. Uh, I think we can add more filters to it. So, can you check can you add a funding filter? I think we should reach out to funded companies, right? Um, funding raised maybe 1 to 5 million, 5 to 10 million. Yes, I think these are good ones. Yeah. Okay. Just a second. Uh, company types. Yeah, I think it's fine. Private company is fine. No, no. I think it will narrow down the result. Can you Yeah, remove this. Like we we'll still get less companies because we are on a free plan.

#### 00:30:41

Yogesh Jaiswal: Yeah. So, can you go up a bit? I think we should also add annual revenue. Yeah. 500,000 to 1 million. Yes. Oh, you can remove annual revenue also. No, no, you can remove it because we cannot judge a company by uh revenue, right? I think it's limiting the companies. Yeah, I think this is enough. Uh yeah, you can click on continue. I think this is enough. No. Yeah. Remove this. Yeah. Yeah. It will this will not get removed. You can save and run 10 rows. H perfect. Yes. Yeah. So you can first remove this uh delete this enriched company, right? Yeah, you can delete these columns. We don't need them. Uh yes. So now can you start running some uh qualification parameters on this with Claygentlike what comes into your mind n anything that comes into your mind?

Neeraj Sujan: So uh one is we can look for job postings right

#### 00:32:39

Yogesh Jaiswal: Yes.

Neeraj Sujan: if their company is already if the job posting has been active for last let's say 30 days or 90 days that mean that means they have not been able to find talent

Yogesh Jaiswal: Yes, that's correct. If the job postings are active for more than like do you think 30 days is a good number or like we keep to 10 days or 15 days. What do you think? Even more than 10 days is not a good number, right?

Neeraj Sujan: I think we can I I think the pain would be that more there would be more pain if uh job posting has been idle for 30 days and that means Yeah.

Yogesh Jaiswal: Okay. Okay. 30 days or more.

Neeraj Sujan: because then uh they are struggling to find people and then it's easy to pitch them.

Yogesh Jaiswal: Yes. Yes. That's a that's a good qualification.

Neeraj Sujan: But if

Yogesh Jaiswal: Yes. Uh, Gan, can you write the prompt that if they're in the company, if their job postings are still open for more than 30 days?

#### 00:33:45

Yogesh Jaiswal: Yeah. Always uh refer to domain. Yeah, domain. Yes, domain. And see if they are open for more than 30 days. Yes. Yeah. Neither does anything else come to your mind after this. Okay. This is a good this is a good parameter. But can we think about more parameters? Let's say the job posting is open. But do you think we should also check how big is their HR team, recruitment team? Um or they are also hiring for any HR related people something like that.

Neeraj Sujan: Uh, so did we put a filter for the type of jobs.

Yogesh Jaiswal: Yes. Yes. Yes.

Neeraj Sujan: Uh so I would uh the current market is hiring these forward deployed engineers, AI engineers. So I would maybe I I will uh f put my uh focus on those roles where demand is high and uh supply is less. So,

Yogesh Jaiswal: Yes.

Neeraj Sujan: uh,

Yogesh Jaiswal: Yeah.

Neeraj Sujan: can't think of So

#### 00:35:08

Yogesh Jaiswal: You can you can run it. It's fine. Yeah. Generate. I think the next thing we need to check if they are hiring for any uh HR related roles because uh yes uh then you can select helium helium helium helium and

Neeraj Sujan: heat.

Yogesh Jaiswal: Yes.

Neeraj Sujan: But I don't think if if it's a 51 to 200 sized company they I mean uh why do we

Yogesh Jaiswal: H.

Neeraj Sujan: need to check if they are hiring HR? They are already posting jobs. So uh

Yogesh Jaiswal: Uh, Gan, can you go to the edit? I think you have deleted the prompt. Yes. Go to edit. Yeah. Go down. You have done something wrong in this. Yes. Click on save 10 rows. Yeah. Okay. Okay. Okay. Meanwhile, can you also add another prompt? Um yesi. So what can we check more here? I think open positions we would get from the client itself

#### 00:36:47

Neeraj Sujan: If there is a change in leadership that means uh

Yogesh Jaiswal: HR. So HR leadership or any leadership.

Neeraj Sujan: the no if there is if there is if they have hired a very vice president of product or something that means they would they would be having plans to hire more people or if the company closed some big deals.

Yogesh Jaiswal: Yeah, we cannot get a track of the deals that they have closed. First of all, uh we can even not use this information that any big uh sea level they have joined or got.

Neeraj Sujan: We can we can we can at least we can find it through news. At least some some of these big companies some consulting companies do publish publish this news

Yogesh Jaiswal: Yes.

Neeraj Sujan: and based on that we

Yogesh Jaiswal: Do you Yeah. Do you feel that we should check how big is their recruitment team? Do you think we should do that?

Neeraj Sujan: Yes. Yeah. Yeah. Because if it's a lean team, that means they would need help.

#### 00:37:46

Yogesh Jaiswal: Yes. So, uh, Gad, can you run an in, uh, find contact at a company column? Yeah. Find contact at a company because we need to see how big is the recruitment team, right? Find. Yeah. Yes. Okay. Uh, no, no, no, no. Don't do job. Go to Okay. No, no, no. Don't do this. Go to job functions. Yes. Now here select human resources and recruitment. Yes. Yes. Okay. Uh select the identifier. Wait, wait, no, no, no, no. That's wrong. That's Go to identifier. Select identifier. Sub top top. No, no, no. Yes. Select domain.

Gagan Bhaisa: this one. Right.

Yogesh Jaiswal: Yes. Select. No. No. Don't do this. This is wrong. Don't uh do slash and Yeah, it's already there. Company domain. Yes. Company domain.

#### 00:38:57

Yogesh Jaiswal: Yes. Now, select column. Uh, Uh yes, company domain. Domain. Yes. Yeah. Now do the job function. Yes. HR, right? Um okay. We need to see every how big is the HR team, right? Okay. So continue to add fields. Yeah, you can continue it. Yes. Yeah. Just wait. People count. Yes, you can run it and okay, we even got some output here and which is good. Now we can even understand how big is their HR team. Okay, perfect. So yes uh okay can you run all Gaganfor job posting and all for find contacts? All the rows remaining rows. Yes. And all for find contacts. Yes. Yes. Okay. Also click on the uh Yeah. Click on this job job posting. Yeah. Go to job posting. Yeah. Click on the output.

#### 00:40:19

Yogesh Jaiswal: Oh, no. Output. Output. H. It will give you more output. Uh, okay. You okay, you got one response itself. Okay, that's fine. You can close it, I think. Yeah. So, yes. Can you see the output? Job title sales executed still open. Yeah. anything the the other column. No, the error column.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: Yes. So, can you see this role is open for more than 30 days? 3 months. Okay. Yeah, you can close this.

Gagan Bhaisa: Uh but Yogesh uh what happened nowadays people are actually not updating on website.

Yogesh Jaiswal: Yes. Yes.

Gagan Bhaisa: Will that be feasible to look into website?

Yogesh Jaiswal: I think that's fine. I think we cannot do anything about it. Like they keep the role open maybe to just attract good candidates.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: I mean some companies just keep on hiring like they never stop hiring.

Gagan Bhaisa: Yes.

#### 00:41:31

Yogesh Jaiswal: So cool. I think we have done good two qualifications. Uh the open roles and how big is their recruitment team? Right. Uh can you check the recruitment team go down? Yes. Okay. I think we have good numbers, right? Many companies don't have a big recruitment team. Okay. Many companies don't even have a Can you check the 15th row TLDV? Yeah, they don't even have a recruitment team. See? And I think TLDV is a famous note taker, right? I have used it. Yes.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Cool. So okay we have run these two

Gagan Bhaisa: Hey.

Yogesh Jaiswal: but one more problem is if they don't have a recruitment team uh we cannot sell lantern to them who will use lantern then right if you go to the lantern's website and if you see uh companies who have a recruitment team uses lantern

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Typically who have a recruitment team who will use lantern right people who companies who don't have a recruitment team why will they use a tool they would rely on an agency See?

#### 00:43:20

Neeraj Sujan: So, can't we sell in directly to the staffing agencies to scale their operations?

Yogesh Jaiswal: Yeah, that's a good idea. They would just partner with them, right? They would not sell. Typically, companies don't sell to agencies. They partner with them because agencies will not use for themselves,

Neeraj Sujan: Okay.

Yogesh Jaiswal: right? They will use for other clients on their behalf. That's a separate thing. I mean that's called alliances and partnerships. Yes. Uh can you go to Yeah. Clear table. Yes. So yeah. Um yes. Now we can run another prompt because uh yeah. Yeah. Because we don't didn't got the perfect output on the first prompt. Yeah. So we can run a qualify disqualify prompt. Right. Now they generate a prompt that as per the information from use AI response information from use AI response the top. Yes. And find contacts at a company. Yeah. Select the whole thing.

#### 00:44:35

Yogesh Jaiswal: Yes. You need to qualify and disqualify a company. need to qualify and disqualify a company. Yes. Qualify when? No. No. No. No.

Gagan Bhaisa: Oh, f*** sake.

Yogesh Jaiswal: No, that's fine. It will still open. Yeah. Go to generate. Yes. Uh yeah. uh qualify when the job posting is more than 30 days and there is one or more person in the HR team. HR team resources team. Yeah. Output or also write uh after full stop write else disqualify. Else disqualify. Yes. Yeah. Now go down say output put qualify. Disqualify. Yes. Disqualify. Open ro. And from how many days it's open and yeah from how many days it is open. And in one line, how does their recruitment team looks like from the job uh from the find from the people looks like in one line?

Gagan Bhaisa: from the people.

Yogesh Jaiswal: Uh in one line.

#### 00:46:49

Gagan Bhaisa: Sorry. Uh Mah

Yogesh Jaiswal: In one in one line. Yeah. Change the recruitment to human resources. Yeah, because we have written human resources up, right? Yeah, you can generate it. H yes these kind of things are also very easy on ground because primary you can use GPT for this GPT AI and it's not going to cost you anything. Yeah. Can you select uh model? Just sele Okay. Don't close the model uh because it closes the prompt also. Yeah, always select. Yeah, that's fine. Go down. Uh, yeah, go to JSON schema. Yes, generate from prompt because we don't even have an output. That's why the first uh AI enrichment was wrong. Yeah. Go down, save and run. Yeah. In the first column, Gagan,the first job posting, you have removed the output column. Yeah. Yeah. No, no, no, no, not a problem. Yeah. Go to the edit.

#### 00:48:23

Yogesh Jaiswal: Get it. Select OpenAI model. Go down. Select Open AI 55. GPT5. Go up.

Gagan Bhaisa: Minnie.

Yogesh Jaiswal: GPT5. Yeah. Mini. Yeah, you can run it. Yeah. See, I'll show you the fun mistake you did. Go to job posting. Yeah. Go to the job edit. Yes. Go down. Yes. You know what you did? You deleted the field. We even deleted the JSON schema. Right. You should never do. Yeah. If you create generate from prompt, uh then you will get right field. That's why you got all the information. See this is what wait this is how you should get the information. Job posting, posting, sourcing, type. But you deleted the fields, right? So the output got deleted. So next time don't do anything without like uh I mean checking it because if you delete the information then the output is wrong.

#### 00:49:41

Yogesh Jaiswal: But that's not a problem. I mean next time you can check. Yeah, you you got the qualification uh yeah don't save. Yeah. Click on response. Yes. Uh let's go to qualifier. Yeah. Yes, this one. Okay. Uh okay. Go to reasoning. Yeah, you can output reasoning, open ro, HR team summary, all you can output everything, open ro. No, no, not this open role. The top one and HR team summary. Okay. See, there are open roles. For some reason, it's disqualifying because of the information, but that's totally fine. You can delete the first output column. Use AI response to this one. Yeah. Yes. Okay. So, uh we just need to do the re like you need to redo the table because I think the qualification and disqualification is wrong. Uh because of the first output table, it got everything into one row. That's why it's not working.

#### 00:52:09

Yogesh Jaiswal: Yeah, this one. So, you need to re not not now, you can do it later. Not a problem. But you understood what you need to do, right? The output was wrong.

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Okay, cool. Uh the qualification should be any company who is the when the there are open roles uh for more than 30 days and there is a recruitment team then it should qualify. So it has disqualified some companies that's fine. Yeah no not a problem. Cool. Um go to the start again like go to the end. Yes. So human okay we have open roles mostly every company have open roles right. So do you think that we should sell lantern to companies who are only having tech related roles or do you think lantern is good for every role?

Gagan Bhaisa: No, it's good for everyone because they are recruitment solution, right?

Yogesh Jaiswal: Yes. But do you think for a role like care manager people will buy lantern?

Gagan Bhaisa: Sorry, what do you say?

#### 00:53:13

Yogesh Jaiswal: Yeah.

Gagan Bhaisa: What am I repeating?

Yogesh Jaiswal: A role like care manager. See the seventh row. Eighth row. Yeah. Yeah. No. See the Yeah. Eighth. Eight. Yeah. Do you think someone would buy a tool for hiring a person like care manager?

Gagan Bhaisa: I mean, not really.

Yogesh Jaiswal: Open it. Can you open it? Yes. Okay. Yeah. So, I think we need to eliminate this company. Yes. Yeah. Go go go to the uh Yes. Yes. Met.

Medha Das: Uh, you Just one quick question. So I mean if you see the client I mean you mentioned like uh why would a company use Landon to hire the care manager but if you see

Yogesh Jaiswal: Yes.

Medha Das: Lantern's like current cliental base it's mostly like education sector hospitality I mean I was just checking the clientele base and it's mostly like uh higher education legal services hospitality real estate construction I mean those are the additional sectors that they serve to uh on top of like uh tech I mean technology and software and services.

#### 00:54:42

Medha Das: So I mean I'm a little confused right

Yogesh Jaiswal: See I mean you are right you you're thinking in the right direction but do just want to ask you do you know how much a company would pay to a care manager like uh let's keep it the example as India Uh it would be 30,000 rupees a month, right? Care manager. And can you go Gan?

Medha Das: Okay.

Yogesh Jaiswal: Can you go to the uh uh again the qualification disqualification uh one? Yes. Uh yeah. Can you see the other one? Sales executive. Right. Now can you open this? Yeah. Sales exe. Yes. Sales executive would be around in India 4 to 5 LPA. Right. Now if you see the amount they're paying to these people right uh generally they don't use a tool here see there is a need but not now there can be a future need but if you see role like a quality assurance engineer business intelligence development manager paid media account manager um that's where we can even have a hope of selling but see I don't say you are wrong I we can even we don't know if the care manager company would buy uh lantern and uh we we don't know that but I think we need to understand that now we are working on 50 companies right we don't work on 50 companies on ground we work on thousands of companies so we don't have capacity to reach out

#### 00:56:16

Yogesh Jaiswal: everyone that's the problem we were solving

Medha Das: right? Also, is it because like uh I mean for the companies who would uh like opt for lantern like I mean I'm just thinking out loud like or

Yogesh Jaiswal: Sorry.

Medha Das: maybe the companies who do wellness hiding they would need lantern more than the companies who are doing like I mean for few profile a few designations or roles Please.

Yogesh Jaiswal: Yes, you are right. See, for any company when the quality of the hire is more important, right? If you see the lantern, it's all about quality of hire. It's never about speed, okay? It's about quality. If you see the website everything that's what I was trying to say when when I shared the website that companies where the quality of hire is more important rather than speed and who which kind of company focus on quality companies like service now Salesforce Microsoft Google companies like juice vantu extra marks or whatever they don't consider quality right am I right or wrong I mean they don't care about the quality So see we don't know how education sector works in the other

#### 00:57:28

Medha Das: Yeah.

Yogesh Jaiswal: countries but in India at least if we see the Indian market um customer support customer success no one seek quality there they just want people to get the work done cheap people right uh so let's let's think more about creating this clay table that um if you want to sell this to a territory I mean Germany and Netherlands would you like are you even going into the right direction which is you are uh absolutely right that uh we can even sell to the companies hiring for a care manager but I really feel that this will just waste your time because I know that if a company is not even paying that kind of amount and lantern would be I I can give you a rough estimate lantern would be $10,000 a year almost US dollars so companies would not spend $10,000 at least on hiring a care manager and they even if you see the care man care manager they have two people HR team right realistically if you understand they would only hire the care manager and if you see the senior account manager also they have a two people HR team what they are going to do every day they are going to hire people right and humans are better than AI you know that So we can reach out to these other ones the manager paid media they have a five people HR team still the job posting is open for 30 days right that's where there is a problem

#### 00:59:09

Gagan Bhaisa: Come on.

Medha Das: Oh, thank you.

Yogesh Jaiswal: but I mean I don't say whatever I'm saying is correct whatever you are saying is correct I think there is a u space to think about this table. Cool. I think that's a good exercise. Um, so what my advice is, can you pick up lantern and build a proper qualification table for it where you qualify and disqualify companies uh as per what Lantern would sell to and also go to the website properly. I think there's a lot to research about the company also.

Medha Das: I'll show you.

Yogesh Jaiswal: Okay. Um, Yes. Yeah. Gagan.Um, yeah. I think Gagan,you need to change the first prompt. Uh, yeah. Yes. Edit JSON schema and generate from prompt. Yes. Save and run all again. 50 rows. 50 rows. Yeah. Not a problem. Not a problem. You can delete the first column. Use response. Yeah.

#### 01:01:04

Yogesh Jaiswal: Yeah. This one.

Gagan Bhaisa: Stop.

Yogesh Jaiswal: Yes, you can delete. No, no problem. Delete it. Yes. Now, click on response. Yeah. Click on that one. Res. Yes. Now output uh job

Gagan Bhaisa: Okay.

Yogesh Jaiswal: title and posted date. Yes, I output this posted date. Uh-huh. And I also output open for 30 days.

Gagan Bhaisa: No, I think we are looking for to give us a result looking at the company which posted 30 days before,

Yogesh Jaiswal: Yeah,

Gagan Bhaisa: right?

Yogesh Jaiswal: that's fine. We can still get use this information, right? I mean, and also output the last one. Yes, we will still get this. Not a problem.

Gagan Bhaisa: That's

Yogesh Jaiswal: So my thought is even if they have not posted less than 30 more than 30 days it's open we can still use it right we can still reach out to a company not a problem.

Gagan Bhaisa: good.

Yogesh Jaiswal: If you see the five regional managers, this is a very good company to reach out to.

#### 01:02:40

Yogesh Jaiswal: Intersect 14. Yes, this one. And see the HR team is only three people. Huh? Yes, this is good. Now I think some information is not working. We need to redo the prompt or something. Not a problem. But uh yeah we got the information. Okay cool. So uh I think can you check Gagen there is also a uh enrichment for job posting. If you go to the right add yeah add column search job posting. No only job posting. Job posting. Yes. Okay. Yeah. Can you see find active job postings? Yes. Can you click on this? Okay. We can even use this domain and uh Okay, you have everything. See has recruiter. Yeah. So, I think this is going to work for us.

Gagan Bhaisa: Want me to run?

Yogesh Jaiswal: Yeah, you can do a test run, I think. Let's No, no, no. It will not run.

#### 01:05:06

Yogesh Jaiswal: You have not tabbed anything.

Gagan Bhaisa: No. So basically we are looking for someone who is hiring right find active job posting. So active job posting can be anything. It's not related to any department or something right or we are looking for some department.

Yogesh Jaiswal: No, no, no. Go down.

Gagan Bhaisa: Uh maximum job posted 30 days plus.

Yogesh Jaiswal: Uh yeah, I think you can even leave it. I think it will give you all the information. Yeah.

Gagan Bhaisa: Mhm.

Yogesh Jaiswal: Yeah, you can run it. Run it. Sorry. Run it. Run it. Yeah. Yes. Let's run 10. Wow. So, this was helpful than the clay agent. Oh, wow. Okay. Yes. Can you click on the first one? Okay. This this is working for us. I think this uses LinkedIn scraping that's why it's giving better data.

Gagan Bhaisa: Turn.

Yogesh Jaiswal: Okay. You can also output the this one hashtag.

#### 01:06:13

Yogesh Jaiswal: What? 2414. This is wrong. No, that that's fine. That's fine. Not a problem. Okay. I think we can use anything plus 10. So you can create a formula right not now but later you can create a formula. Anything plus 10 job count is a qualified company for you because uh they have a lot of focus on hiring good people now. Cool. Okay. So I'll tell you what you need to build. Uh find active job posting uh for everyone ma and nage and everyone find active job posting. uh anything more than 10 should be qualified right and then the recruitment team if recruitment team then you should qualify the company if they don't have a recruitment team don't qualify they are using agency so no need to qualify there okay uh try to try to build this table I think whatever we have discussed is

Neeraj Sujan: Okay.

Yogesh Jaiswal: just our thoughts maybe you can use claude and get a better way of building it the Only thing we need to build is um how many companies we can sell in Germany and Netherlands or you can even select a territory of your choice.

#### 01:07:32

Gagan Bhaisa: Yeah.

Yogesh Jaiswal: Not a problem. Uh but you need to keep a build a company qualification list. The qualified companies by Lantern can sell to and also go through Lantern properly. So in real life when you are a GTM engineer you are going to do this exercise a lot. every time you will get a new company and you need to research and you need to do what they are doing understand so that's going to be a usual thing for you uh in GTM engineering okay try to build this table I'm going to build this also for you over the weekend maybe and I'll also show you how it's done uh cool cool guys any questions

Neeraj Sujan: No, no.

Yogesh Jaiswal: Yeah.

Neeraj Sujan: forward.

Yogesh Jaiswal: Yeah. The main context here is to do fast decisions in GTM engineering. So you get a company, everything should be quick. Now understand the company, build a qualification company table, get people qualify, disqualify uh and get email ids, lending URLs and reach out. Every company is only focused here at this at this part. Okay, cool guys. I think this is it.

Neeraj Sujan: Okay.

Yogesh Jaiswal: Um try building this uh building this and uh you can even post in the group if you have any questions. I will also build this side by side for you so that I can show you how it's perfectly built. Okay, I'll build in my clay and show you. Okay, cool guys. Have a nice day.

Neeraj Sujan: Okay, thank

Yogesh Jaiswal: Yeah. Yeah.

Medha Das: Action one.

#### Transcription ended after 01:09:16

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.