# Cheat sheet: Web scraping in Clay

Condensed from the instructor's teaching doc. Clay reprices/renames scraping integrations often — treat tool names as stable, exact prices as approximate.

## The mental model

Every scrape is the same four-step loop: request the page → parse HTML → extract target values → structure into rows. Extraction is the hard part, since a page's layout doesn't label which tag holds the price vs. a footer link. Fixed-selector scrapers break on redesigns; Claygent reads for meaning instead, so it's more resilient but costlier. In Clay's find/enrich/transform/export framework, scraping sits inside find (new list) and enrich (fill a missing fact) — not its own category.

## Ask first: should you even scrape?

Is this data more easily available through an existing Clay provider or waterfall? Which source is actually most reliable for this data point? Example: headcount at an established SaaS company — use a standard waterfall, scraping is redundant. Headcount for a dentist office or law firm — provider coverage is thin, so scraping the business's own site is more reliable. Scraping fills gaps; it isn't a default habit.

## Legal/ethical basics

Check a site's terms of service and robots.txt before scraping. Treat anything gated (login/paywall) or containing personal data as higher risk regardless of what's technically possible.

## The five-tool ladder (cheapest/simplest → most powerful/expensive)

1. **Clay Native Scraper** — static pages (company homepage). Pick what to extract: emails, phones, links, or full body text. Test on a few rows before scaling.
2. **Clay Chrome Extension** — for a visible list/table already on a page. Install it, open the page, click the icon to auto-detect the repeating pattern, or build a custom recipe (click two example items, pick attributes), then send rows straight into a Clay table.
3. **Claygent** — for unstructured content that needs interpretation, not one exact field. Survives redesigns better since it reads meaning, but costs AI credits per row and is slower.
4. **Apify Actors** — when the target platform (LinkedIn, Reddit, job boards, real estate listings) already has a maintained scraper in Apify's marketplace. Often carries its own subscription/fee on top of Clay.
5. **Zenrows** — for sites actively fighting you: CAPTCHAs, human-verification walls, heavy JS rendering. Comparatively low-cost per request; can run through a personal Zenrows account for direct billing.

Decision order: visible list/table on a page → Chrome Extension. Static page, exact field → Native Scraper. Unstructured, needs interpretation → Claygent. Known platform with a marketplace actor → Apify. Site is blocking you → Zenrows. Reach for Zenrows/Apify only after the cheaper tools fail or don't apply — treat them as an escalation path, not a starting point.

## Combining tools (realistic workflow)

Chrome Extension pulls an initial list from a directory/conference page → Native Scraper grabs each company's homepage body text → Claygent reads that text for qualitative signals (mission, ICP, positioning) → Zenrows only for the specific protected detail pages (e.g. a Crunchbase funding page). Each tool does the part it's actually good at.

## Under the hood (for debugging, not building)

Pagination — advanced tools walk multi-page results automatically. Proxy rotation — premium proxies cycle IPs after one gets blocked. JavaScript rendering — Zenrows' JS option catches content that only loads after JS runs. Auto-parse/structuring — raw HTML still needs Clay's column extraction/formula/AI columns to become clean data.

## Applying this to the Saffron Clay table

- The Accounts table's Claygent-on-Helium step (AI-coding-tool detection) is tier 3 on the ladder — keep it only where source text is genuinely unstructured; drop to Native Scraper first for defined fields like a careers-page list.
- Before any new scrape, apply "should you even scrape?": does the People table's 11-provider waterfall already cover it? Scrape only genuine gaps like careers-page tool mentions.
- A JS-heavy or blocking target site is a Zenrows case, not a reason to lean harder on Claygent.
- BuiltWith-style tech-stack detection is a cheaper complementary signal alongside Claygent for the AI-tool column.

## Credit-efficiency points

- Native Scraper and Chrome Extension are the cheapest options — default to these whenever the page structure allows it.
- Claygent costs AI credits per row, scaling with how much reasoning the page needs — reserve it for genuinely unstructured content, not fields a Native Scraper could pull directly.
- Apify actors often carry their own subscription/per-use fee on top of Clay — check actor pricing before scaling from a test batch to a full list.
- Zenrows is comparatively low-cost per request; a personal Zenrows account lets a team manage billing directly instead of through Clay credits.
- Universal rule: test on a handful of rows first, confirm clean output, then scale to the full table — never run a new scrape configuration across a full table on the first pass.
