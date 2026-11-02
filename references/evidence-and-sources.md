# Evidence hierarchy, factual guidance and research sources
Updated 2026-11-02. Verify links, facts and policies during every later run.

## Source hierarchy
1. Official search-engine provider docs for crawler behavior and measurement semantics.
2. Verified first-party product/manual/price/legal docs for specific claims and current availability.
3. Authorized internal first-hand evidence (support, analytics, CRM, sales calls), anonymized with consent; never put personal info in a public article without authority.
4. Independent expert reports, domain publications, documented customer/user conversations, genuine competitor reviews (with dates and bias checks).
5. Academic studies, labeled with caveats about experiment settings.
6. Hypothesis templates, clearly not observed demand.

## Official primary references
- OpenAI crawlers: https://developers.openai.com/api/docs/bots — OAI-SearchBot is for ChatGPT Search; separate from GPTBot (model training) and ChatGPT-User (some user-triggered access). Allow published IP ranges through host/WAF if you want to be eligible. OpenAI notes robots.txt adjustment can take ~24 hours. Allowed is **not guaranteed** inclusion.
- OpenAI ChatGPT Search help: https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt — ChatGPT sometimes rewrites queries to send to third-party search providers, can use multiple targeted searches; rank is based on multiple factors and is not guaranteed.
- OpenAI partner/search announcement: https://openai.com/index/introducing-chatgpt-search/ — includes third-party search and partner content. Does not disclose a stable full list of search indexes used for every answer.
- Microsoft Bing AI Performance: https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c — shows supported Microsoft Copilot/Bing/selected partner AI citations and grouped grounding queries. **Not equivalent to ChatGPT visibility.** Citation counts ≠ clicks or rankings; reports are aggregated/sampled.
- Bing Topics Portfolio beta (Oct 2026): https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ — estimated topic opportunity based on sufficient site presence; not a complete query-volume source and not ChatGPT reporting.
- Google AI search optimization guidance: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — prioritize original useful content, technical SEO and known signals, not magic chunking/llms.txt tactics. Google documentation covers **Google**, not ChatGPT ranking.
- Google helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content — original, reliable, expert-led content for people.
- Google spam policies: https://developers.google.com/search/docs/essentials/spam-policies — avoid doorway pages, scaled low-value output and deceptive claims.
- Google Organization schema: https://developers.google.com/search/docs/appearance/structured-data/organization — truthful entity and publisher data, only if applicable.
- Google SoftwareApplication schema: https://developers.google.com/search/docs/appearance/structured-data/software-app — use for eligible software, after verifying accurate price/ratings etc.
- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx — SKILL.md with YAML frontmatter and references/scripts.

## Research literature (descriptive; not official ranking rules)
- Martinez (2026), critical GEO survey of 45 studies: https://arxiv.org/abs/2607.14035 — notes variable, multi-stage pipeline; limited reliable cross-platform causal evidence for durable organic gains.
- Chen & Koudas (2026): https://arxiv.org/abs/2610.15033 — large observational study of 158,099 answers and 468,037 citations; query-semantic alignment and retrieval choices important; avoid presenting findings as fixed weights or universal guarantees.
- Zhang et al. (2026): https://arxiv.org/abs/2604.25707 — distinguish citation selection and actual answer influence; platform differences.
- Aggarwal et al. foundational GEO work: https://arxiv.org/abs/2311.09735 — earlier experimental improvements conditional on setup, not evidence of guaranteed organic ChatGPT placement.

## Evidence records
Each nontrivial business claim must have `claim`, `proof_url_or_artifact`, `date_checked`, `verified_by`, `status`, and `caveats`. Each demand conclusion must have `question_verbatim`, `source_type`, `source_url_or_internal_ref`, `observed_date`, `frequency_basis`, `locale`, `confidence`.

## Explicit anti-overclaim rules
- Search snippets/PAA/Autocomplete are **cues**, not measured question frequency; do not equate visibility with demand volume.
- Never fabricate impression estimates, referral percentages or citation lift.
- A single ChatGPT response might be personalized; test independent sessions and paraphrases and record non-appearances.
- Structured data is useful for clarity/search eligibility; it is not a ChatGPT ranking lever with guaranteed impact.
- No claim that Bing AI Performance includes direct ChatGPT citations absent official proof.
- Do not collect private community content or scrape against site terms. Label external content as quoted/paraphrased and link its source.
