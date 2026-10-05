# Cheat sheet: The HTTP API column

Condensed from the instructor's student learning guide.

## What it's for

Clay has native integrations for a lot of tools, but not everything. HTTP API connects Clay to any API without a native integration, either direction — pulling data in or pushing data out. Every other enrichment is a pre-built button; HTTP API is the wire you connect yourself.

## Step 1: pick the mode

- **HTTP API Enrichment** — you already have rows in a table and want to add API data to each one.
- **HTTP API as Source** — you have no table yet and want to pull a fresh list from an API to create one.

Quick test: "Do I already have rows in a table?" Yes → Enrichment. No → Source.

## Step 2: before touching Clay, read the API's docs

Search "{API name} API documentation" and find, before starting:
- The endpoint URL
- The method (GET, POST, PUT, or DELETE)
- Whether/how it authenticates (API key? bearer token?)
- What parameters or body fields it expects

## Step 3: build the column two ways

1. **AI-assisted (Sculptor):** add enrichment → HTTP API → Generate tab → describe the request in plain English → Generate → switch to Configure tab to see what it built → Test on one row.
2. **Manual rebuild (the part that actually teaches the skill):** set Method (GET to retrieve, POST to create, PUT to update, DELETE to remove), Endpoint URL, Query parameters mapped to your columns, and a Field path (dot-path to the exact value, e.g. `data.user.email`, instead of the whole payload). Test and compare to Sculptor's result — a match means you understood the config, not just copied it.

## JSON body rules (memorize before any POST/PUT)

- String values need quotes: `"name": "Sam"`
- Numbers and booleans don't: `"age": 30, "active": true`
- A dynamic column reference for a string still needs quotes: `"email": "/Email Column"`
- A dynamic column reference for a number doesn't: `"count": /Score Column`
- Commas between every key-value pair — `{"name": "John", "age": 30}`, not `{"name": "John" "age": 30}`

## Vocabulary (know cold)

API — two pieces of software talking: you send a request, it sends back data. Endpoint — the URL you send the request to. Method — GET (read), POST (create), PUT (update), DELETE (remove). Header — extra info, most often authentication. Query parameter — filters after a `?` in the URL, e.g. `?status=active`. JSON body — structured POST/PUT data, `{ "key": "value" }`. Field path — dot-path to where the value lives in the response. Authentication — an API key or bearer token in a header.

## Error codes — diagnose before asking for help

- 400 — request formatting is wrong — check your JSON body (quotes, commas)
- 401 — not authenticated — check your API key/bearer token
- 403 — authenticated but not allowed — check permissions/scopes
- 404 — endpoint doesn't exist — check the endpoint URL for typos
- 429 — sending requests too fast — check your rate limit settings

## Practice exercise (self-guided, no Sculptor)

Free, no-auth REST Countries API (restcountries.com): table with a Country Name column (5 countries), HTTP API enrichment returning capital, population, region, configured manually with a field path for just those three fields, tested on one row first, then one sentence on what you'd change at 10,000 rows.

## Applying this to the Saffron Clay table

- A new engineering-activity signal (GitHub public API for repo/commit activity, or a job-board API) would be an **HTTP API Enrichment**, not Source, since the 50 accounts already exist as rows.
- Read the target API's docs first, confirm auth (GitHub needs a token; some job-board APIs are no-auth), and note the exact field path so the column returns just that value.
- Build it manually, not just via Sculptor — rebuilding by hand confirms the config is understood, which matters for later debugging.
- Test on one account row before running across all 50 — the same "test small, then scale" rule taught for scraping.
- A 401/403 on GitHub or a job-board call means the API key/token or scope, not the field mapping — check credentials first.

## Credit-efficiency points

- Calls to free, no-auth public APIs cost no external fee — only Clay's own enrichment credit, generally cheaper than Claygent for the same row.
- Field path discipline (return only the exact value needed) keeps payloads small, which matters at scale.
- Test on a single row before running a full table to avoid burning credits on a misconfigured call.
- Prefer GET requests to free/public endpoints over paid tools where the same data is available for free — same "cheapest plausible tool" logic as the scraping ladder.
