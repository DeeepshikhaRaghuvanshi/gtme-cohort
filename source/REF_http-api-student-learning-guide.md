# http_api_student_learning_guide


Student Learning Guide: The HTTP API Column

Stable GTM · Work through this at your own pace

## What You'll Learn

By the end of this guide, you'll be able to:

Explain what the HTTP API column does and when to reach for it.

Tell the difference between HTTP API Enrichment and HTTP API as Source, and pick the right one.

Build a working HTTP API column two ways: with AI-assisted setup (Sculptor) and by hand.

Read and fix the most common errors on your own.

Complete a hands-on exercise using a real, free public API.

## Step 0: Learn the Vocabulary First

Don't skip this — every later section assumes you know these terms cold.

## Step 1: Understand What HTTP API Actually Does

Clay has native, pre-built integrations for a lot of tools — but not everything. HTTP API is how you connect Clay to any API that doesn't have a native integration, in either direction: pulling data in, or pushing data out.

Think of it like this: every other enrichment in Clay is a pre-built button. HTTP API is the wire you connect yourself.

## Step 2: Pick Your Mode

💡 If you're not sure which one you need, ask: "do I already have rows in a table?" If yes → Enrichment. If no → Source.

## Step 3: Before You Touch Clay

Open the API's documentation first. Search "{API name} API documentation" and keep that tab open. You need to find, before you start:

☐  The endpoint URL

☐  The method (GET, POST, PUT, or DELETE)

☐  Whether it needs authentication, and how (API key? bearer token?)

☐  What parameters or body fields it expects

## Step 4: Build Your First Column (Guided Walkthrough)

We'll use a free, no-auth-required weather API (Open-Meteo) so you can focus on the Clay mechanics without fighting an API key.

Try it with AI-assisted setup (Sculptor) first

In a Clay table, add a column with two fields: Latitude and Longitude (or use any two rows of coordinates you like).

Click Add enrichment → search for and select HTTP API. You'll land on the Generate tab.

Type this in plain English: "Find me the average temperature using Open-Meteo, using latitude and longitude."

Click Generate API connection and let Sculptor build the request for you.

Switch to the Configure tab and look at what it built — this is how you learn the mechanics, not just get an answer.

Click Test on one row. Check the result makes sense before running the whole table.

Now build the same thing manually

This is the part that actually teaches you the skill — rebuild the same column by hand, field by field:

Method: GET (you're retrieving data, not creating or changing anything).

Endpoint URL: the Open-Meteo forecast endpoint from their docs.

Query parameters: map latitude and longitude to your two columns.

Field path: find the exact dot-path to the temperature value in the response, so you return just that number instead of the whole payload.

Test on one row again and compare the result to what Sculptor gave you.

💡 If your manual version and Sculptor's version give the same answer, you've actually understood the config — not just copied it.

## Step 5: Know the JSON Body Rules Cold

This is where almost everyone makes their first mistake. Memorize these four rules before you try a POST or PUT request:

String values need quotes: "name": "Sam"

Numbers and booleans don't: "age": 30, "active": true

A dynamic column reference for a string needs quotes: "email": "/Email Column"

A dynamic column reference for a number doesn't: "count": /Score Column

WRONG:   {"name": /Name Column}
CORRECT: {"name": "/Name Column"}

WRONG:   {"name": "John" "age": 30}
CORRECT: {"name": "John", "age": 30}

## Step 6: Diagnose Errors Yourself

Before asking for help, check the error code against this table:

## Practice Exercise

Complete this on your own, without a walkthrough. Use the free REST Countries API (restcountries.com) — no authentication required.

☐  Create a new table with one column: Country Name (add 5 countries of your choice).

☐  Add an HTTP API enrichment that looks up each country and returns its capital city, population, and region.

☐  Configure it manually — no Sculptor this time.

☐  Use a field path to return only the three fields you need, not the entire response.

☐  Test on one row before running all five.

☐  Write one sentence: what would you change if this table had 10,000 rows instead of 5?

## Self-Check Quiz

Answer these in your own words before moving on. If you can't answer one confidently, go back to that section.

## You're Ready to Move On When...

☐  You can explain, without looking anything up, when to use Enrichment vs. Source.

☐  You've built at least one HTTP API column manually, not just with Sculptor.

☐  You can read a 400 or 401 error and know where to start fixing it.

☐  You've completed the practice exercise with the REST Countries API.

| Term | What it means |

|---|---|

| API | A defined way for two pieces of software to talk to each other — you send a request, it sends back data. |

| Endpoint | The specific URL you send your request to (e.g. https://api.example.com/customers). |

| Method | What kind of action you're doing: GET (read), POST (create), PUT (update), DELETE (remove). |

| Header | Extra info sent with your request — most often used to prove who you are (authentication). |

| Query parameter | Extra filters added to the end of a URL after a ?, like ?status=active. |

| JSON body | The structured data you send with a POST or PUT request, written in { "key": "value" } format. |

| Field path | A dot-path telling Clay exactly where in the response the value you want is located, e.g. data.user.email. |

| Authentication | Proving you're allowed to use the API — usually an API key or a bearer token in a header. |

| If you already have... | Use |

|---|---|

| A table of companies/people/records in Clay, and want to add API data to each row | HTTP API Enrichment |

| No table yet — you want to pull a fresh list from an API to create one | HTTP API as Source |

| Code | What it means | Where to look |

|---|---|---|

| 400 | Something's wrong with your request formatting | Your JSON body — check quotes and commas |

| 401 | You're not authenticated | Your API key or bearer token |

| 403 | You're authenticated but not allowed to do this | Your API key's permissions/scopes |

| 404 | The endpoint doesn't exist | Your endpoint URL — check for typos |

| 429 | You're sending requests too fast | Your rate limit settings |

| # | Question |

|---|---|

| 1 | What's the difference between HTTP API Enrichment and HTTP API as Source? |

| 2 | Why does a dynamic column reference for a string need quotes, but one for a number doesn't? |

| 3 | What does a 401 error tell you, and where would you go to fix it? |

| 4 | Why should you always test an HTTP API column on a single row before running it on the full table? |

| 5 | What's a field path, and why would you use one instead of returning the whole API response? |