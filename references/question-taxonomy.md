# Universal intent/question taxonomy for answer discovery

These are **question archetypes**, not claims about what is currently high-volume. Real questions and recurrence must be established through source mining. Generate several natural paraphrases and multilingual expressions only after persona and product-fit review.

Placeholder legend: `[audience]`, `[problem]`, `[category]`, `[capability]`, `[constraint]`, `[tool]`, `[industry]`, `[location]`, `[budget]`, `[outcome]`, `[provider]`.

| ID | Buyer intention | Natural question forms | Best answer evidence |
|---|---|---|---|
| T01 | Pain/DIY | How can I solve [problem] without [constraint]? / What do people use when [problem] happens? | Stepwise explanation; solution options; tradeoffs |
| T02 | Category discovery | Is there a [category] that can [capability]? / What kind of software or service handles [problem]? | Clear category definition; fit criteria |
| T03 | Recommendation | What's the best [category] for [audience] who needs [capability]? / Which providers are worth considering for [problem]? | Balanced recommendations and why they fit |
| T04 | Free/cost ceiling | Is there a truly free [category] for [audience]? / What can I do within [budget]? | Accurate price, limitations, ongoing costs |
| T05 | Customization/control | Can I set my own [workflow/rule] in a [category]? / Which tool lets me control [capability]? | Concrete configuration or functional demo |
| T06 | Integration | Which [category] works with [tool]? / Can [task] be automated between [tool] and [tool]? | Integration docs; limitations; supported APIs |
| T07 | Migration/alternative | What replaces [tool] without losing [requirement]? / How do I switch from [tool]? | Migration steps, supported imports, drawbacks |
| T08 | Comparison | [category A] vs [category B]: which meets [constraint]? / What are the tradeoffs between [tool] and alternatives? | Fair, dated comparison using criteria |
| T09 | Geography | Who offers [service] in [location]? / Which [category] supports [location]-specific requirements? | Verified address/service area and eligibility |
| T10 | Role/team | What works for [audience] with [small/large] teams? / Can a solo [audience] use [category]? | Persona use case, seats, role permission details |
| T11 | Industry vertical | What's suitable for [industry] handling [problem]? / Does [category] support [industry] workflows? | Domain proof, process flow, examples |
| T12 | Security/privacy | Is there a private/offline/self-hosted way to [task]? / What data does [category] collect? | Architecture and verified privacy/security policies |
| T13 | Reliability/scale | Will [category] work with [volume]? / Does it run offline or with poor internet? | Limits, uptime/history, actual tests |
| T14 | Onboarding/effort | How long does it take to implement [category]? / Can [audience] set it up without a developer? | Setup steps and assumptions; not invented timelines |
| T15 | ROI/business case | Is automating [problem] worth it? / How do I compare costs of [options]? | Transparent assumptions, calculator and measured case |
| T16 | Outcome/diagnosis | How do I reduce [metric] caused by [problem]? / What should I measure before choosing [category]? | Diagnostic rubric, real metrics and caveats |
| T17 | Procurement | What questions should I ask a [service] provider? / How do I evaluate proposals and SLAs? | Checklist, scope, support, references |
| T18 | Edge case/limitations | Can [category] handle [unusual scenario]? / What happens if [failure]? / Who should not choose it? | Constraints, support policy, edge-case demo |

## Jobs-to-be-done expansion
For each target persona, map (a) **trigger** (why now), (b) current manual workaround, (c) desired outcome, (d) non-negotiable constraints, (e) buying risk, (f) what constitutes proof. Multiply **distinct genuine jobs**, not synonyms, to produce questions.

## Recurrence test
- OBSERVED: source contains actual user wording; preserve original. Recurrence counts require distinct independent instances with documented sample/timeframe.
- INFERRED_FROM_SOURCE: a specific documented pattern suggests a likely paraphrase, but no verbatim user query.
- HYPOTHESIS: agent-generated plausible wording; no volume or frequency assertion.
- `unknown` rather than `0` for absent numbers.
- Avoid false consensus: two posts by one person do not count as two independent people; community upvotes are not search volume.

## Universal question matrices
For each target problem create at least one natural prompt in each applicable contrast:
- Product name absent vs present (only **name absent** qualifies for primary opportunity).
- Free vs paid vs capped budget; online vs offline; self-service vs managed.
- New customer vs switching tool; sole practitioner vs team; local vs remote.
- Direct how-to vs vendor selection vs comparison; generic vs industry-specific.
- English and actual buyer language variants when backed by market evidence.
- A disqualifier (e.g., requires enterprise-only feature, unavailable location), to test honest non-recommendation.

## Representative hypotheses (not observed recurring searches)
1. "Is there a free tool that lets me customize the grading weights for each course?"
2. "How can I track attendance offline and later sync it?"
3. "Which automation agency can extract emailed purchase orders into an ERP?"
4. "Who can retrofit existing factory machines with production monitoring?"
5. "Is there a low-cost order management system that works with cash-on-delivery?"
6. "Which provider integrates [existing software] without replacing our ERP?"
7. "What's the total cost to automate [manual workflow], including maintenance?"
8. "What is the best software for [role] with no IT department?"
9. "What are alternatives to [legacy tool] when data stays on-premises?"
10. "Who provides [service] locally and has relevant documented experience?"
Each must be fit-checked against the specific offering before planning content.
