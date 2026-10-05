# Clay Conditional Logic & _Only Run If_ — Basic to Advanced Guide


## Clay Conditional Logic & "Only Run If" — Basic to Advanced Guide

### 1. What Conditional Runs Are

In Clay, conditional runs let you tell any enrichment, action, or integration to fire only if a condition you define evaluates to true. Structurally it's a simple if/else:

if (condition is true) {

run the enrichment

} else {

skip it — no credits spent, no action taken

}

You'll find this control inside the Run Settings of almost any column or action, in a box usually labeled "Only run if."

This one feature is the backbone of almost every efficient Clay table. Without it, Clay is just an interface bolted onto a bunch of data providers — you pay for every provider on every row, whether you need it or not. With it, Clay becomes a decision engine: enrich selectively, route conditionally, and only spend credits where the data actually justifies it.

Why it matters (the credit-cost angle): If you have 1,000 leads and run 5 email-finding providers on all of them "just in case," you pay for up to 5,000 lookups — even when the first provider already found a good email. A conditional run says "only try Provider B if Provider A came back empty," which is exactly how waterfalls work under the hood. You've likely already used conditional logic without realizing it.

### 2. Where to Find It in the UI

Open any column (an enrichment, a Claygent prompt, an integration action, a "Write to Table," an "Add to Sequence," etc.).

Click into its Run Settings (usually a gear icon or a settings panel below the main column config).

Look for the "Only run if" field.

You have two ways to build the condition:

Manual formula — write the logic yourself using Clay's formula syntax.

"Use AI" — describe the condition in plain English and click Generate formula; Clay's AI Formula Generator writes the underlying formula for you and shows sample outputs on the right so you can sanity-check it before saving.

If you're on a newer version of the UI and can't immediately spot the option, it's typically nested one level deeper — inside the column's settings panel rather than on the main column toolbar. It hasn't been removed; Clay has just reorganized where run settings live from time to time.

### 3. The Basics: Building a Condition

#### 3.1 Referencing data

Use / inside the formula/condition box to pull in a column as a variable. In documentation and examples you'll often see this represented as {{column_name}}:

{{email}} is not empty

#### 3.2 Comparison operators

#### 3.3 Logical operators

Combine conditions for more nuance:

AND — every condition must be true {{company_size}} > 500 AND {{industry}} == "SaaS"

OR — at least one condition must be true {{title}} == "Founder" OR {{title}} == "CEO"

NOT — reverses a condition NOT {{status}} == "Closed"

#### 3.4 A first real example

You've enriched a person and want to send a personalized email — but only if a valid work email actually exists:

{{work_email}} is not empty

If true → the "Send Email" or "Upload to CRM" action fires. If false → Clay skips the row entirely, and you spend nothing on it.

### 4. Core Use Cases (Straight From Common Workflows)

### 5. Intermediate: Conditional Runs and Waterfalls

A waterfall — Clay's chained, ordered enrichment pattern — is really just a series of conditional runs stacked on top of each other:

Provider A (Findymail) → runs on every row

Provider B (Prospeo)   → "Only run if" {{email_from_A}} is empty

Provider C (broad DB)  → "Only run if" {{email_from_A}} is empty AND {{email_from_B}} is empty

Run Find my email - Validate email - Invalid Email - Again find email through Prospeo then again validate - Valid Email

Best practice: order your waterfall by cost and accuracy — put your most accurate/expensive providers first, and only fall back to broader, cheaper (or less accurate) databases if the good ones come up empty. This is the single highest-leverage use of conditional runs in most GTM stacks, because it directly controls spend at scale.

### 6. Intermediate: Conditional Claygent (AI Agent) Runs

Claygent (Clay's AI research agent) columns support the same "Only run if" logic, with two common patterns:

a) Gate on a prior AI classification. If you've already run a prompt that outputs "Yes"/"No" (e.g., "Is this person a founder, CXO, or in sales/marketing/growth?"), gate your next, more expensive Claygent call behind it:

{{qualification_column}} == "Yes"

This way you only spend deep-research credits on qualified rows.

b) Retry on error/failure state. If a Claygent column sometimes returns a red/error output, you can set a follow-up column (or a re-run) to fire only when the prior step failed:

{{prior_column_status}} == "error"

The AI Formula Generator can build this automatically — describe the scenario ("only run if the previous column's output is red/errored") and click Generate.

### 7. Advanced: Multi-Condition, Nested Logic

You can combine AND/OR/NOT to encode fairly sophisticated business rules directly into a single run condition. Example — "only trigger a deep AI research scrape if the company is currently hiring for engineering roles AND uses AWS; otherwise stop at basic enrichment":

{{hiring_engineering}} == "Yes" AND {{tech_stack}} == "AWS"

Layer in NOT and OR for edge cases:

({{title}} == "Founder" OR {{title}} == "CEO") AND NOT {{industry}} == "Nonprofit"

Notes on Clay's formula syntax (important at the advanced level):

Clay's formula language is a subset of JavaScript — it supports comparisons and conditional logic, but you generally can't define your own functions or variables the way you would in vanilla JS.

If you paste in a formula generated by ChatGPT or another LLM outside Clay, it may not run as-is if it uses unsupported JS features. Stick to Clay's AI Formula Generator, or keep hand-written formulas within its supported syntax.

### 8. Advanced Patterns & Cost-Optimization Playbook

Gate expensive steps behind cheap classifications. Run a cheap/free AI formula or simple field check first; only let the expensive Claygent/web-scrape/enrichment step fire if that first check passes.

Segment before you spend. Use conditional runs to separate "Tier 1" accounts (worth deep research) from "Tier 3" accounts (basic enrichment only) instead of running your most expensive workflow on every row.

Order waterfalls by cost + accuracy, not alphabetically or arbitrarily — accurate/expensive providers first, cheap/broad fallback providers last, each gated on the previous one returning empty.

Use "is empty" as your default waterfall gate. It's the simplest, most reliable way to avoid duplicate spend across chained providers.

Validate before you export. Gate CRM uploads, sequencer enrollments, and Slack/webhook notifications behind data-quality checks (valid email, non-empty phone, correct region) so downstream systems don't get junk rows.

Preview before you commit. Always check the sample outputs shown next to the formula generator before saving — conditions that look right in English can evaluate unexpectedly against real data (e.g., string vs. number comparisons, case sensitivity in ==).

### 9. Troubleshooting

### 10. Quick Reference Cheat Sheet

STRUCTURE

if (condition) { run } else { skip }

REFERENCE A COLUMN

{{column_name}}   (select via "/" in the UI)

COMPARISON OPERATORS

==   !=   >   <   >=   <=   is empty   is not empty

LOGICAL OPERATORS

AND   OR   NOT

COMMON PATTERNS

Waterfall fallback:     {{previous_result}} is empty

Quality gate for export: {{email}} is not empty

Score/segment gate:      {{lead_score}} > 80 AND {{industry}} == "SaaS"

Rep routing:             {{assigned_rep}} == "Kareem"

Retry on error:          {{status}} == "error"



### 11. Where This Fits in a Broader Clay Build

Conditional runs are the mechanism; waterfalls, round-robin routing, tiered enrichment, and sequencer filtering are all applications of it.

Pair conditional runs with AI formulas (Clay's credit-free, code-generating formula tool) for data shaping, and reserve conditional runs specifically for deciding whether an action/enrichment fires at all.

As your tables grow, conditional logic is what keeps a table's credit spend proportional to lead quality instead of list size — this is usually the single biggest lever for making a Clay build financially sustainable at scale.



| Operator | Meaning | Example |

|---|---|---|

| == | equals | {{industry}} == "SaaS" |

| != | not equal to | {{status}} != "Closed" |

| > / < | greater / less than | {{company_size}} > 500 |

| >= / <= | greater/less than or equal | {{lead_score}} >= 80 |

| is empty / is not empty | checks for blank output | {{work_email}} is empty |



| Use case | Condition example | What it does |

|---|---|---|

| Upload to CRM | {{email}} is not empty | Only pushes contacts with a valid email — keeps your CRM clean |

| Sequencer filtering | {{lead_score}} > 80 AND {{industry}} == "SaaS" | Only enrolls high-fit leads into outreach sequences |

| Write to Table | {{region}} == "North America" | Populates a column only for rows matching a target segment |

| Round-robin assignment | {{assigned_rep}} == "Kareem" | Runs a rep-specific action only for rows assigned to that rep |

| Waterfall email finding | {{work_email}} is empty | Only tries the next (often pricier) provider if the first came back blank |

| Claygent web research | {{prior_column}} == "red" (error state) | Only re-runs an AI agent if the previous step failed or errored |



| Problem | Likely cause / fix |

|---|---|

| Can't find "Only run if" in the UI | It's inside the column's Run Settings, one level deeper than the main column toolbar — look for a settings/gear icon on the column. |

| Generated formula doesn't match your intent | Rephrase your English description more precisely (mention exact column names/values), or hand-edit the generated formula in the code view. |

| Formula errors out on a JS snippet from outside Clay | Clay only supports a subset of JavaScript — no custom function/variable definitions. Rebuild it with the AI Formula Generator instead. |

| Condition seems to always evaluate false | Check for type mismatches (e.g., comparing a number field with a quoted string) and confirm you're referencing the right column via /. |

| Waterfall running every provider on every row | Confirm each downstream provider has its own "Only run if {{previous_output}} is empty" condition — without it, Clay runs steps unconditionally. |