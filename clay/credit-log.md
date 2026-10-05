# Clay credit log: Saffron build

Fill in one row per run. The numbers feed the LinkedIn post, so record them honestly, including failed runs (Clay charges per attempt, not per success).

Starting balance: ____ data credits / ____ actions (📸 date/time: ____)

| # | Column / step | Model or provider | Rows run | Data credits used | Actions used | Rows with a good result | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Enrich Company | | 10 | | | | |
| 2 | Enrich Company | | 40 | | | | |
| 3 | SWE Openings (job postings) | | 10 | | | | |
| 4 | SWE Openings fallback (Use AI) | Helium | | | | | only rows where count was empty |
| 5 | Has TA Team (Find Contacts) | | 10 | | | | |
| 6 | New Eng/Talent Leader | | 10 | | | | |
| 7 | AI Coding Tools | **Helium** | 10 | | | | first sweep |
| 8 | AI Coding Tools | **Neon** | (failed rows only) | | | | escalation |
| 9 | Work Email waterfall | cheapest-first | 10 | | | | |
| 10 | Verify (Enrichly) | | | | | | only if email not empty |
| 11 | Personalization line | Helium | | | | | only if Sendable = Yes |

Ending balance: ____ data credits / ____ actions

## Numbers for the post
- Total credits for 50 accounts → ____ qualified accounts → ____ sendable contacts
- Rows that were **skipped** by "only run if" gates (credits not spent): ____
- Helium vs Neon on the same 10 rows: ____ vs ____ credits; accuracy ____/10 vs ____/10
- Estimated cost if every AI column had run on Neon/Argon for all 50 rows, with no gates: ____
