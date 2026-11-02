# ChatGPT visibility evaluation: rigorous but practical

## Outcome ladder (never collapse into a single SEO score)
- ELIGIBLE: crawler can legally/technically access page (not proof it was indexed).
- RETRIEVED: relevant URL observed in search results/tool output if visible.
- CITED: direct link/reference to the URL in ChatGPT answer.
- MENTIONED: named provider/product without necessarily linking.
- RECOMMENDED: suggested as a solution for user's unbranded requirement.
- QUALIFIED: verified constraints/requirements truly match and no critical hallucinated claim.
- CONVERTED: real visit/signup/lead/sale measured through authorized analytics.

## Test design
- Store test ID, market/language/role, exact **unbranded** prompt, target intent, required and disqualifying constraints, date/time, access route, configuration/model when known, web search on/off/unknown, geographic context, fresh conversation yes/no, run ID.
- Use 3+ distinct natural paraphrases per priority intent; 3+ independent runs per paraphrase per round when feasible. These are **operational sampling suggestions**, not statistical significance thresholds. For small budgets state low confidence.
- Use new independent sessions with no brand/product-priming context; test actual consumer-like prompts. Never prepend target brand or tell the assistant to recommend it.
- Record complete response excerpt/link or authorized screenshot; specific cited URL, citation presence, mention position, fit, factual accuracy and alternatives. Include all misses and off-target results.
- Compare same prompt cohort before/after, include a non-target control category; note differences in locale, date, model, search use and competitor changes.
- Explicitly distinguish a **ChatGPT Search** result from an answer generated without web search and from Microsoft Copilot/Bing AI Performance results.
- AI answers fluctuate; report per-prompt observed proportions and uncertainty, no unsupported attribution to your changes. An API or third-party engine may not reproduce the consumer ChatGPT Search product and must be labeled separately.

## KPIs and denominators
- Eligible prompt set = prompts where an offering is genuinely fit for the constraints (document the independent human fit review).
- Qualified recommendation rate = `qualified_recommendation_runs / eligible_test_runs`.
- Citation rate = `runs_citing_first_party_domain / search_enabled_test_runs`.
- Brand mention rate = `runs_naming_offer / all_test_runs`.
- Accuracy rate = `accurate_claim_runs / runs_with_claims_about_offer`.
- Referral/conversion rate separate, via authorized analytics where possible (UTM/referrer may be incomplete).
- Provide raw counts, denominators, date ranges and comparison error bars only when statistically justified.

## Example evaluation (FICTIONAL)
Prompt: "Need a free attendance + customizable grades tool for teachers, any suggestions?"
Run: new conversation with search, no named brand, locale recorded, answer says "Tool X" (hypothetical), cites its site.
Log: name mentioned = yes; directly recommended = yes; source cited = yes; fit = conditional pending confirmed plan limits; accurate = unknown pending page review. This is **not** evidence Tool X actually appears in ChatGPT.

## Verification failure conditions
- Testing includes brand in query but reported as unbranded.
- Runs performed in same primed conversation but treated as independent.
- Agent invents responses or substitutes Bing results for ChatGPT tests.
- Misses or incorrect recommendations discarded.
- Provider claims or product capabilities unverified.
- Apparent rate changes from tiny non-comparable samples claimed as causal proof.
