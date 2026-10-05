# Before today's class: what you missed on 28 Sep

## Things to know

1. HTTP API column: Clay's general connector to any external API without a native integration. Core vocabulary: endpoint, method (GET/POST/PUT/DELETE), headers, query parameters, JSON body, field path, authentication, test vs. production URL. Error codes: 400 bad request formatting, 401 not authenticated, 403 not permitted, 404 endpoint doesn't exist, 429 rate limited.
2. Web scraping ladder: cheapest to most expensive: Native Scraper, Chrome Extension, Claygent, Apify, Zenrows. Always try the cheapest tool that could work first. Claygent is expensive at scale (~$200/1,000 rows) vs. Apify (~$19/month) — use Claygent only when a page needs interpretation, not plain field extraction.
3. Clay table hygiene: a table must end in outreach-ready messaging, not just an email or LinkedIn URL. Use fewer columns, not one per detail. A clean table should take 2-3 hours to build, not days.
4. Signal filtering rule: at least 70% of sourced companies should survive qualification. One classmate dropped from 60 to 6 companies — a sign of too-strict signals or double-filtering across two tools.
5. Live table review: a classmate's 47-company table (SOC2-compliance signal, security/DevOps roles) got feedback to hide unused columns and add a People-table lookup (mapped on Company Name) pulling in company-level messaging — a reusable pattern.

## Homework given (check if it applies to you)

- Everyone: work through the shared 400+ tool directory, keep a one-line summary per tool tried.
- Two classmates: rebuild company lists to keep ≥70% after filtering, and generate a "Clay execution logic" doc via Claude/GPT.
- One classmate: expand target roles to "platform security" and build the company-to-people lookup.
- Nothing assigned to you specifically since you weren't there — ask Yogesh if the tool-directory task applies to you too.

## Questions worth asking Yogesh

1. HTTP API column for a free signal (GitHub or job-board data) — Enrichment or Source, given my table already has 50 rows?
2. Should I shift some Claygent-on-Helium AI-tool detection to a cheaper Native Scraper pass, given the cost gap raised in class?
3. Does my Outreach Eligibility formula pass the 70%-survival rule?
