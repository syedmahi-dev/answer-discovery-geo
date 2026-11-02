# Actual question discovery and competitor investigation

## 1. Research inputs by evidence strength
**Direct voice-of-customer:** consented anonymized support tickets, sales chats, FAQ requests, demo notes, product search logs, in-app failed searches, survey responses, returned quotes, post-demo objections.
**Behavioral data:** Search Console verified queries, Bing Webmaster Tools organic queries, GA4 landing/referrals, real site search queries, optional research tools with date and market. Do not present click/impression data as direct ChatGPT prompts.
**Public buyer voice:** Reddit discussions, Stack Overflow/Stack Exchange (when applicable), industry forums, public review platforms (G2/Capterra/Trustpilot etc.), help communities, YouTube comment themes, public procurement RFPs, community Q&As. Follow terms of access, do not scrape private data, identify astroturfing and commercial bias.
**Search signals:** targeted Bing/Google searches, autocomplete, People Also Ask, related searches, query-focused SERPs, competitors' FAQ docs/support; these indicate relevance/existence, not necessarily measured frequency.
**Synthesis:** AI-generated paraphrases are allowed **only as hypotheses**.

## 2. Search strings to execute and log
Substitute `[pain]`, `[persona]`, `[tool]`, `[industry]`, `[region]`:
- `"[pain]" "looking for" software` / `"[pain]" "any recommendations"`
- `site:reddit.com "[pain]" "free"` / `site:reddit.com "[tool] alternative"`
- `"[industry]" "how do you" "[problem]"`
- `"[category]" "custom" "[requirement]"`
- `"[service]" "quote" "[region]"`
- `"[tool]" "doesn't support" "[capability]"`
- `"[category]" "privacy" "self hosted"`
- `"[category]" "which is better" "[constraint]"`
- `"[service]" "RFP" "requirements"`
Log exact query, time/date, search provider/tool, results examined, evidence quality, bias/limitations. If browsing isn't possible, declare all question candidates hypotheses and do not pretend an external study was done.

## 3. Question record and clustering
Fields: id, actual_or_candidate_question, demand_label, original_source, date_observed, language, location, persona, trigger, task/problem, constraints, category, intent_family, search_stage, feature_fit, proof_pointer, frequency_value, frequency_unit, frequency_source, competitor_facts, suggested_destination, confidence, next_action.

Merge *semantically equivalent* questions; preserve natural wording variants as children. Split when constraints materially change choice, e.g., free for 1 user vs unlimited seats, offline vs cloud, local law applicability.

## 4. Competitor research fairness
For each cluster find: incumbent baseline; 3–6 plausible alternatives; actual pricing (date and plan); real fit/disqualifiers; genuine support docs and outside reviews; no invented winner. Acknowledge where another vendor is better. Do not publish pseudo-independent rankings disguised as impartial reviews. Supplier authored comparisons should transparently identify the author.

## 5. Demand scoring
If source measures actual occurrences, attach time range, sampling frame, population and count. Forum mentions ≠ search volume. Search Console impressions ≠ unique customers. If no reliable count, describe signals as qualitative with confidence and omit faux numerical demand scores.

## 6. Research stop conditions
- No verified offering proof? Stop publishing claims; ask for product verification.
- No observed questions? Deliver transparent hypothesis bank with a discovery/measurement plan, not an invented frequency report.
- Unclear legal applicability? Do not claim compliance or a service area.
- No live Search access? Make a baseline plan instead of fabricating visibility tests.

## 7. Research log
For each URL record claim/question supported, observed date, date the page was published when available, retrieved wording excerpt (brief and within copyright limits), strength, conflict, and follow-up. Templates in `templates/`.
