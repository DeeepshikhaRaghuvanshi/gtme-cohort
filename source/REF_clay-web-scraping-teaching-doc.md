# clay_web_scraping_teaching_doc


Teaching Web Scraping in Clay: Basics to Advanced

Stable GTM · Instructor Reference Doc

Clay adds and reprices scraping integrations often. Spot-check tool names, actor pricing, and Zenrows/Apify costs inside Clay right before class — the framework below is stable, the exact numbers may drift.

## 1. What Web Scraping Is

Every web scrape follows the same four-step loop, no matter which tool runs it: request the page, parse its HTML, extract the target values, and structure them into rows. The hard part is almost never the request — it's the extract step, because a page's layout doesn't tell a scraper which tag holds the price and which holds a footer link. Traditional scrapers rely on exact selectors and break when a page changes; AI-based scraping reads the page for meaning instead, which is more resilient but more expensive.

In Clay's own framework of find, enrich, transform, and export, web scraping sits inside find and enrich. It's a way to pull in a list of things (find) or to fill in a missing fact about something you already have (enrich) — not a category on its own.

## 2. The Strategic Question First: Should You Even Scrape?

Before opening any scraping tool, teach students to ask two questions:

Is this data more easily available through an existing Clay data provider or waterfall?

Which source is actually the most reliable for this specific data point?

Example: for headcount at an established SaaS company, a standard enrichment or headcount waterfall is usually reliable — scraping would be redundant. But for an SMB segment like dentist offices or law firms, data providers often have thin or inaccurate coverage, and scraping the business's own website becomes the more reliable source. Scraping is a tool for gaps, not a default habit.

## 3. Legal & Ethical Basics

Set this expectation early, before any hands-on scraping:

Always check a site's terms of service and robots.txt before scraping it, and treat anything gated or containing personal data as higher-risk regardless of which tool makes it technically possible.

## 4. The Clay Scraping Toolkit — Basic to Advanced

This is the core mental model to teach: a ladder of five tools, roughly ordered from cheapest/simplest to most powerful/expensive. Recommend students always try the cheapest tool that could plausibly work before reaching for the next one up.

## 5. Basics: Your First Scrape

Option A — Clay Native Scraper (static pages)

Add a scraping enrichment to your table and point it at a URL column.

Choose what to extract: emails, phone numbers, links, or full page body text.

Run it on a few rows and confirm the output before scaling.

Option B — Clay Chrome Extension (a visible list or table on a page)

Install the Clay Chrome extension and open the page containing the list you want.

Click the Clay icon — the extension auto-detects repeating list/table patterns on the page.

If auto-detect doesn't match what you want, create a custom recipe: click two items in the list to define the pattern, then select the specific attributes to pull (name, title, location, etc).

Save the recipe and send the scraped rows straight into a new Clay table.

## 6. Intermediate: Choosing the Right Tool for the Job

Walk students through this decision order — it mirrors how Clay's own team recommends approaching a new scraping task:

Is the data already sitting in a visible list or table on a page you're browsing? → Chrome Extension.

Is it a static, simple page like a company homepage, and you need a defined field (emails, phones, links, body text)? → Native Scraper.

Is the content unstructured, or does the answer require reading and interpreting the page rather than pulling one exact field? → Claygent.

Does the exact platform you need (LinkedIn, Reddit, job boards, real estate listings) already have a maintained scraper in Apify's marketplace? → Apify Actor.

Is the site actively blocking you — CAPTCHAs, human-verification walls, heavy JavaScript rendering? → Zenrows.

## 7. Advanced: Combining Tools in One Workflow

Real workflows rarely use just one scraping tool. A common advanced pattern: use the Chrome Extension to pull an initial list from a directory or conference page, use the Native Scraper to grab each company's homepage body text, run Claygent over that text to extract qualitative signals (mission, ICP, positioning), and fall back to Zenrows only for the specific detail pages that are protected (e.g. a Crunchbase funding page). Each tool does the part it's actually good at instead of forcing one tool to do everything.

Teach students to treat Zenrows and Apify as the escalation path, not the starting point: reach for Zenrows when the Native Scraper or Chrome Extension gets blocked, and reach for Apify when the target platform already has a purpose-built actor that would take far longer to replicate by hand.

## 8. Advanced: What's Happening Under the Hood

Pagination: many scrapes need to walk through multiple pages of results — advanced tools like Zenrows and Apify actors handle this automatically, but students should know it's happening so they can debug incomplete results.

Proxy rotation: sites block IP addresses that send too many automated requests in a short window; premium proxies cycle through different IPs so the scrape can keep running after one address gets blocked.

JavaScript rendering: some pages only load their real content after JavaScript runs in a browser — a plain HTTP request won't see it, which is exactly the gap Zenrows' JS rendering option closes.

Auto-parse / structuring: raw scraped HTML still needs to be turned into clean columns — this is where Clay's column extraction tools and formula/AI columns take over after the raw scrape lands.

## 9. Cost & Scaling Considerations

Native Scraper and Chrome Extension are the cheapest options — default to these whenever the page allows it.

Claygent costs AI credits per row scraped, scaling with how much reasoning the page requires.

Apify actors often carry their own subscription or per-use fee on top of Clay (e.g. a niche actor might run a monthly fee after a short free trial) — check the actor's pricing before scaling to a full list.

Zenrows is comparatively low-cost per request and can also be run through a personal Zenrows account if a team wants to manage billing directly.

Universal rule regardless of tool: test on a handful of rows first, confirm the output is clean, then scale to the full table.

## 10. Quick Reference for Students

Static page, exact field needed → Native Scraper.

Visible list/table on a page → Chrome Extension.

Unstructured content, needs interpretation → Claygent.

Known platform with a marketplace actor → Apify.

Site is blocking you → Zenrows.

Always ask first: is scraping even the right call, or does Clay already have a more reliable source for this data?

| Situation | General risk level |

|---|---|

| Public data, no login required | Lower risk — broadly permitted in the US, but still depends on jurisdiction, the site's own terms, and the type of data. |

| Data behind a login or paywall | Higher risk — accessing gated content raises legal exposure regardless of the tool used. |

| Personal data covered by GDPR/CCPA | Higher risk — regulated regardless of whether the source page itself is public. |

| Tool | Tier | Best for | Watch out for |

|---|---|---|---|

| Clay Native Scraper | Basic — default | Static pages (company homepages), built-in extraction of emails, phone numbers, links, and raw body text. | Struggles with JS-heavy or protected pages — it's the cheap, simple option, not the powerful one. |

| Clay Chrome Extension | Basic | Turning a visible list or table on a page (directories, case study pages, attendee lists) into a Clay table via auto-detect or a custom recipe. | Best for structured, tabular-looking data — messier layouts need a hand-built recipe. |

| Claygent | Intermediate | Unstructured or semantic content: reasoning over a page's meaning rather than its exact HTML tags, so it survives page redesigns better than fixed selectors. | Costs AI credits per row and is slower than a direct scrape — don't use it where a native scraper would do. |

| Apify Actors | Advanced | Platforms with a pre-built scraper already in Apify's marketplace: social platforms, job boards, real estate sites, niche directories. | Many actors carry their own subscription or per-use fee on top of Clay; quality depends on the actor's maintainer. |

| Zenrows | Advanced | Sites with real anti-bot protection — JS rendering, premium proxies, CAPTCHA/human-verification walls (e.g. Crunchbase-style pages). | Overkill for simple static pages; reach for it only after the Native Scraper or Chrome Extension has failed. |