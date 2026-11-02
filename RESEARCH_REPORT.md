# Research report: building ChatGPT-first AEO/GEO for any offering
**Research date:** 2026-11-02  
**Goal:** Unbranded problem → relevant solution recommendation; independent of any specific company or website.

## Executive conclusion
The highest-value reusable operation is **question-driven evidence mapping**: capture the questions real buyers ask, determine the true product/service fit, make a publicly accessible answer destination that resolves that exact need, and repeatedly check how ChatGPT Search answers the question. The workflow is an opportunity-development and measurement discipline, not a guarantee of organic placement.

## What is established vs not established
| Observation | Status | Consequence |
|---|---|---|
| ChatGPT can rewrite a user query into more targeted queries for third-party search providers | Documented by OpenAI | Optimize for the full **meaning** of buyer problems, not just exact phrasings |
| OAI-SearchBot is specifically for ChatGPT Search; GPTBot and ChatGPT-User have different roles | Documented by OpenAI | Check correct bot rules and edge security separately from training policies |
| Allowing OAI-SearchBot enables eligibility, not a ranking guarantee | Documented by OpenAI | Measure actual outcomes; don't sell bot permission as guaranteed placement |
| AI answers can vary due to retrieval, model and context | Supported by research review and practical test design | Use repeated, fresh, unbranded test runs |
| Question-semantic relevance is associated with citations; retrieval has a major role | Observational academic evidence (2026) | Favor original content that genuinely answers decision questions |
| Any particular schema/FAQ markup or llms.txt guarantees ChatGPT recommendation | **Not established** | Do not waste effort on "GEO hacks" as a substitute for useful evidence |
| Bing AI Performance reports citations from supported Microsoft/partner experiences | Documented by Bing | Useful diagnostic context; **do not label it ChatGPT citation data** |

## Primary recurring buyer question *families* (across industries)
The following families recur as **decision archetypes** for services and software, rather than as empirically ranked search queries. A particular category's actual incidence must be verified in that market.

1. **Solution existence:** “Is there a way/tool/provider to do X?”
2. **Best-fit recommendation:** “What should someone like me use for X?”
3. **Price/free:** “Can I do X for free/under budget Y? What's the catch?”
4. **Customization:** “Can I do X my way, with special rules?”
5. **Integration:** “Does it work with the tool/system I already use?”
6. **Replacement:** “What's an alternative to tool X without losing Y?”
7. **Comparison:** “X vs Y: which works for my constraint?”
8. **Location/service area:** “Who offers this in my city/country?”
9. **Role/industry:** “What's suitable for teachers/operations teams/clinics/etc.?”
10. **Security/privacy:** “Can it work without sharing sensitive data?”
11. **Reliability:** “Will it work offline/at my volume/on old equipment?”
12. **Setup:** “How hard is implementation, migration and onboarding?”
13. **ROI:** “What does it save compared with doing it manually?”
14. **Root cause:** “Why does X keep happening, and what fixes it?”
15. **Procurement:** “How do I evaluate vendors, SLAs and proposals?”
16. **Limitations:** “What doesn't this tool handle? What if something fails?”
17. **Contract/support:** “Who maintains it, handles bugs and owns the data?”
18. **Time-sensitive triggers:** “What can we deploy before deadline X?”

For a general reusable skill, these are more valuable than a static list of 200 generic keywords. Each individual offering has its own jobs-to-be-done, constraints, markets, terminology and user evidence.

## Discovery method that can identify **actual** recurring questions
1. **First-party voice of customer:** collect privacy-safe support/CRM/customer-call questions; preserve exact phrasing and count distinct independent occurrences over a defined period.
2. **First-party search behavior:** group Search Console/Bing queries and site-search terms by decision need. Interpret impressions correctly: an impression is not a unique person or ChatGPT query.
3. **Third-party public discussions:** inspect authentic buyer requests in forums, Reddit, industry associations, public support communities and review sites. Identify source bias and date. Do not claim a synthetic prompt is a quotation.
4. **Question-form search:** use `"[problem]" "recommend"`, `"[problem]" "free"`, `site:reddit.com "[problem]"`, `"[tool] alternative"`, `"[industry] [problem]"`, and compare SERP answer destinations.
5. **Source-grounded paraphrase expansion:** once an actual question is found, create a few realistic constraints/locale variants. Label these **INFERRED** or **HYPOTHESIS**, never observed.
6. **Prioritize honestly:** require verified fit and proof before planning a destination; avoid encouraging recommendation for a customer who is not served by the product.

## Content architecture that emerges
An offering should have a minimal, credible set of canonical pages for distinct decision needs: the category overview; buyer-specific use cases; high-value jobs/outcomes; genuine capability docs and limitations; current pricing; integrations; practical how-to; case studies with proof; methodology; migration; procurement criteria; comparison when factually supportable; and helpful FAQ sections. Not every offering needs every page. Don't generate dozens of near-identical URLs from paraphrases.

## What to measure specifically in ChatGPT
Report at least three separate rates with explicit denominators: **qualified recommendation**, **citation**, and **accuracy**. Add mention and referral conversions as separate diagnostics. Every observation must log exact unbranded prompt, search enabled/on/off/unknown, locale, model/interface when visible, fresh conversation, date, direct cited URLs, full answer excerpt and competing suggestions. Run multiple paraphrases on multiple independent runs and compare after significant changes. Note that the consumer ChatGPT product, OpenAI API web search, Bing AI Performance and Perplexity are not interchangeable measurement surfaces.

## Suggested first cycle
- Day/phase A: truth register + 30–50 seed questions (all candidate), then evidence discovery.
- Phase B: identify 5–12 highest-fit, evidence-backed clusters and test a baseline in ChatGPT Search.
- Phase C: publish or improve 5–12 substantial, accurate answer destinations after review.
- Phase D: monitor indexing, real crawler errors, unbiased answer outcomes and referral quality; rerun identical prompt cohort at a consistent cadence.

These are a **workflow order** only, not promised delivery times or expected ranking improvements.

## Practical evidence cautions
- The research does **not** establish stable universal ChatGPT ranking factors, even if industry blogs claim so.
- A 2026 survey specifically cautions that experimental improvements on already-retrieved pages do not prove durable organic discovery improvements.
- Bing's Topics Portfolio beta (Oct. 13, 2026) can reveal *its own* thematic opportunity queries when enough data exist; that is useful but does not reveal exact ChatGPT user prompts.
- Google explicitly recommends good foundational SEO and unique useful content over supposed AEO/GEO markup tricks for **Google** search; applying these principles to ChatGPT is a rational cross-platform practice, not a claim that their ranking systems are identical.

## Primary sources
1. OpenAI search crawler documentation: https://developers.openai.com/api/docs/bots
2. ChatGPT search mechanics and sourcing: https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt
3. ChatGPT Search providers and publishers: https://openai.com/index/introducing-chatgpt-search/
4. Bing AI Performance (scope and caveats): https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
5. Bing Topics Portfolio beta (Oct. 2026): https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/
6. Google guidance on AI SEO/GEO myths: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
7. Google helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
8. Google spam policies: https://developers.google.com/search/docs/essentials/spam-policies
9. Martinez 2026, critical survey: https://arxiv.org/abs/2607.14035
10. Chen & Koudas 2026, retrieval/citation observational study: https://arxiv.org/abs/2610.15033
11. Zhang et al. 2026, citation vs absorption: https://arxiv.org/abs/2604.25707

## How to execute this research next time
Read `SKILL.md` and run mode `DISCOVER`, `PLAN`, `IMPLEMENT`, `EVALUATE` or `FULL` with an offering brief. The workflow produces the claim register, evidence-backed question clusters, a prioritized plan, page briefs, technical checks, reproducible ChatGPT testing and a dated research log.
