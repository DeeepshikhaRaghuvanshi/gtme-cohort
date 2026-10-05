This week I built a full account-qualification pipeline in Clay, and the lesson I didn't expect was how much the cost depends on choices you make before anything runs.

The project: find the right companies and buyers for Saffron (YC S26), an AI-native technical interview platform. I started with 50 target companies and ended with 30 qualified accounts and 40 verified work emails for their engineering and talent leaders. Total cost: 118.6 Clay credits.

Four decisions kept it that low:

→ Cheapest model that can do the job. Clay pre-selected its most expensive research model (3 credits a row). The cheapest one (1 credit) answered my question just as well once I tightened the output format. When it returned messy answers, fixing the output fields worked; a pricier model wasn't needed.

→ Only run expensive columns where the answer can change the decision. My AI research ran on 16 of 50 companies, not all 50. It cost 19 credits instead of an estimated 150+.

→ Compare providers. The same "find people" step cost 0.1 per person on one provider and 1 to 3 on others. People search came to 9 credits.

→ Test on 10 rows first. Twice, the preview caught a bug before it cost anything: a true/false field stored as text, and a filter pointing at a column that didn't exist.

Also worth knowing: not every Clay enrichment charges per attempt. Some only charge when they find something.

#GTMEngineering #Clay #RevOps #Outbound
