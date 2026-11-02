---
name: answer-discovery-geo
description: Research question-led AEO/GEO opportunities for any software product, service, consultancy, or local business, prioritizing organic visibility in ChatGPT search. Mine verifiable customer questions, map intent to truthful capabilities, specify evidence-backed pages, audit crawler/index readiness, test unbranded ChatGPT recommendations, and report outcomes without inventing demand or promising placement. Use when asked about GEO, AEO, AI search citations, answer-engine visibility, solution-led discovery, SEO question research, or ChatGPT product recommendations.
license: MIT
compatibility: Requires a research-capable agent with web browsing for live discovery; Python 3.10+ for optional standard-library scripts. Does not require paid SEO tools or API keys. ChatGPT answer evaluation needs authorized access; do not bypass platform terms or rate limits.
---
# Answer Discovery GEO — reusable agent skill

## Mission
Make **a genuinely relevant offering findable, understandable, and citeable for unbranded problem-oriented questions** (e.g. "free tool to customize student grading" rather than "BrandName"). Prioritize **ChatGPT Search**, while keeping sound traditional SEO foundations. Operate on *any* product or service. Never assume that mentioning a brand in a model answer can be guaranteed or purchased through page editing.

## Activation and scope
When the user asks to improve AEO/GEO/answer-engine discovery, use this skill. Do not assume a particular company, site, niche, language, or country. Request an offering brief only when essential information is unavailable; otherwise make explicit provisional assumptions and work. Read `references/question-taxonomy.md`, `references/research-protocol.md`, `references/technical-playbook.md`, `references/chatgpt-evaluation.md`, and `references/evidence-and-sources.md` as appropriate.

Key distinction: **AEO** = content that directly answers a specific question accurately; **GEO** = discoverability, citation and accurate inclusion in generative answers. Both depend on genuine product fit, accessible evidence, and measurement; the labels are not separate official ranking systems.

## Inputs (obtain or infer transparently)
- OFFER: name, category, official URL, product/service, current availability, verified capabilities, exclusions, pricing and terms, evidence links.
- AUDIENCE: user role(s), industry, maturity, purchase authority, geography, language, pain points, existing tools.
- BOUNDARIES: who should *not* be targeted, prohibited claims, budget, legal/regulated constraints, approvals, tracked channels.
- OBJECTIVE: direct qualified recommendations, cited inclusion, branded disambiguation, or referral traffic. Default = **unbranded qualified recommendation in ChatGPT Search**.
- CONTEXT: time window, target country/language, sites in scope, access to Search Console/Bing/analytics/support logs, and ability to publish.

Template: `templates/offer-brief.json`. Never infer an undocumented capability as fact. Separate shipped, beta, planned, custom-build service, and unsupported features.

## Operating sequence — follow every time

### Phase 0 — Establish truth and guardrails
1. Build a **claim register** for each offering: claim, type (verified/pending/unsupported), proof URL or artifact, date checked, owner, restrictions. Unproved capabilities are never used as promises in drafts or target recommendation prompts.
2. Define success: *eligible*, *retrieved*, *cited*, *mentioned*, *recommended*, *accurately described*, and *qualified visit/lead* are **different metrics**.
3. Identify whether buyers need evidence of compliance, privacy, certifications, pricing, integrations or regional service availability.

### Phase 1 — Discover authentic questions, not just keywords
1. Mine evidence sources in this order when available: internal support/sales tickets, real search queries and referral data; public buyer Q&A/discussions and competitor reviews; search suggestions/related searches and industry forums; targeted web searches; then controlled **hypothesis generation**.
2. Use role + job-to-be-done + constraints + context + timing. Search for phrasing a real user would use: "how can I…", "free alternative to…", "what supports…", "which provider near…", "without…", "integrates with…", "how much…".
3. Log original wording, URL or data source, date, context, and independently observed frequency if available. Do **not** call generated templates "frequently asked", "high-volume" or "trending" without support.
4. Cluster by decision need (not shallow keyword similarity). Use the 18 intent families in `references/question-taxonomy.md`. For each cluster, retain buyer stage, role, geography/language, must-have feature, must-not-have constraints, and an evidence-backed intent label.
5. Construct a representative bank of 40–100 questions only if the offering has sufficient breadth; **quality > quantity**. Mark each as OBSERVED / INFERRED_FROM_SOURCE / HYPOTHESIS. One question can have multiple natural paraphrases.
6. For a fast initial seed only, run `python scripts/seed_questions.py templates/offer-brief.json --output question-seeds.csv`; these are hypotheses, never demand estimates.

### Phase 2 — Investigate current answers and competitors
For **each priority cluster**, run fresh, unbranded searches: how-to, request-for-recommendation, comparison, local, constraint-driven, and substitution variants. Record exact queries and URLs consulted. Inspect the pages ChatGPT/search results actually surface (not merely Google's top 10). Note *which facts* led to recommendations, why candidates fit, their shortcomings, and whether sources are first-party or independent. Do not falsely imply any ranking/citation outcome from a standalone website search.

### Phase 3 — Fit/priority scoring
For each question score 0–5 with written reasons:
- **F**: genuine feature/service fit; **I**: commercial/user intent; **E**: strength of claim evidence; **G**: uncovered answer gap; **D**: observed demand signal (unknown = null, not zero); **R**: effort/competitive difficulty (higher is harder).
- Gate: exclude if `F<3`, `E<3`, or materially misaligned. Never sell planned features as live.
- Rank *eligible* items by `(3F + 2I + 2E + 2G - R)`, then use observed demand **as a qualitative tie-breaker** only when real data exist. Avoid implying score is a search engine formula.
- Choose 5–12 strong clusters for a first publishing wave, not hundreds of thin articles.

### Phase 4 — Design the best answer destination
For each chosen cluster choose a page **type**, one canonical destination, and an evidence plan. Examples: feature/use-case page, step-by-step solution guide, genuine comparison, pricing/free plan eligibility, integrations/how-to, industry process, geographic services, calculator, documentation, video transcript, case study, FAQ within a substantive page. Required page ingredients:
- A human-readable title/H1 matching the problem, a direct factual answer early, constraints and eligibility, verifiable demonstration, pricing/conditions when relevant, evidence and recent accuracy review, logical internal links, next-step CTA.
- Specific answers to who it suits / doesn't suit, what it does / doesn't do, installation/integration/setup, tradeoffs and credible alternatives.
- Unique evidence: workflows, screenshots, data, reproducible demo, real case studies/benchmarks with methodology, manuals, approved testimonials. Never invent reviews, client names, certifications, savings percentages, or comparisons.
- Avoid mechanical page proliferation, keyword swapping, fake Q&A, link schemes, fabricated authors or testimonials, invisible prompt instructions, manipulative schema, copied competitor wording.
Use `templates/page-brief.md` and `references/content-patterns.md`.

### Phase 5 — Technical eligibility
Inspect (do not blindly overwrite) robots.txt, `OAI-SearchBot` access and CDN/WAF/IP restrictions; public rendering including without JS; HTTP 200/canonical/noindex/sitemap/internal links; mobile usability; redirects and access gates; metadata; optionally relevant, truthful structured data. `ChatGPT-User` and `GPTBot` are **not** substitutes for `OAI-SearchBot`. Never claim allowing crawler guarantees inclusion. Review `references/technical-playbook.md`. Run the **read-only** `scripts/site_readiness.py <url>` where network access is authorized; its findings are heuristic, **not** proof of real crawler access or indexing.

### Phase 6 — Publish with review gates
Create a staged implementation plan or code changes only with permission and repository access. Require claim-owner review, accessibility/technical checks, factual consistency across pages/schema/metadata, editorial review, and regression tests. Keep an immutable evidence log and diff. Never auto-publish speculative facts. Make proposed code changes rather than fabricating deploy success.

### Phase 7 — ChatGPT Search recommendation evaluation
Before/after measurement **must** distinguish ChatGPT with web search from model-only answering. Use **fresh independent conversations**, no brand priming, neutral customer phrasing, realistic location/language/device constraints, and competitors allowed. For each target cluster, test multiple paraphrases in repeated sessions/dates; log search activation, mention, recommendation qualification, citation URL, factual accuracy, answer excerpt, competitor set, and disclosed limitations. Record all misses. A single response is anecdotal, not proof of ranking. Human-review every extracted result. Follow `references/chatgpt-evaluation.md` and log in `templates/evaluation-results.csv`.

### Phase 8 — Report, improve, rerun
Return: (1) claim register; (2) **evidence-labeled** question map; (3) prioritized topic/opportunity matrix; (4) 5–12 page briefs; (5) technical readiness and required changes; (6) ChatGPT evaluation baseline; (7) implementation tickets and owner; (8) dated source/research log; (9) monitoring plan. Indicate explicitly what was **not** verified. Do not confuse Bing AI Performance/Copilot citations with ChatGPT citations. Update periodically after meaningful publication changes and monitor actual referral conversions separately.

## Acceptance gates
- All promised capabilities and price/free claims backed by dated proof.
- At least one **unbranded, problem-oriented** question for each target cluster; no brand leakage in baseline testing.
- Questions labelled OBSERVED / INFERRED_FROM_SOURCE / HYPOTHESIS with supporting source data or unknown status.
- Search terms and consulted URLs logged. Measured volumes only with provenance; absent metrics = `unknown`.
- No duplicate thin content; one useful destination per intent cluster.
- OpenAI crawler/robots/WAF checks distinguished from indexing and actual recommendation.
- ChatGPT tests: transparent sample sizes, test dates, exact prompts, independent runs, citations vs mentions, and misses.
- No fake authority, reviews, testimonials, awards, comparative measurements, or schema declarations.
- Output is reproducible from saved inputs and source links.

## Modes
- **DISCOVER**: research question demand and cluster; produce bank, evidence and opportunities only.
- **PLAN**: produce prioritized page briefs, technical tasks and measurement plan.
- **IMPLEMENT**: implement approved page/schema/technical changes with tests.
- **EVALUATE**: run/baseline unbranded ChatGPT visibility tests and write a defensible report.
- **FULL**: run phases 0–8 with evidence gates. If no website/analytics access, mark later stages planned/not tested instead of faking results.

## Embedded workflow invocation
"Use the `answer-discovery-geo` skill in DISCOVER/PLAN/FULL/EVALUATE mode for [offer]. Target [audience] in [geography/language]. Focus on *unbranded* problems and user questions. Treat assumptions as hypotheses and cite every demand/claim finding. Produce the skill's output artifacts."

## Source-of-truth and further reading
See `references/evidence-and-sources.md` for OpenAI crawler/search guidance, Microsoft Bing measurement scope, Google quality and structured-data guidance, and published GEO research. Check source publication dates again each run; these systems change.
