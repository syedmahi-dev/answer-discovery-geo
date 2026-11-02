# Answer Discovery GEO — reusable skill (v1.0, 2026-11-02)

An open-format Agent Skill for **unbranded problem-to-solution discovery**: research real customer questions, determine whether an offering truly fits, create evidence-led answer destinations, audit search eligibility, and evaluate unbiased ChatGPT Search citation/recommendation outcomes.

## What you receive
- `SKILL.md` — primary skill, works with agents implementing the [Agent Skills spec](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx).
- `references/` — question taxonomy, source mining, technical playbook, answer content, ChatGPT test protocol, sources.
- `templates/` — input brief, research log, claim register, question map, test sheet, page brief.
- `scripts/seed_questions.py` — *hypothesis* question generation from an offer brief (not keyword volume).
- `scripts/site_readiness.py` — safe read-only URL/robots/HTML eligibility *heuristic*.
- `scripts/validate_deliverables.py` — output quality gates.
- `examples/` — a fictional example, labeled as sample data.

## Installation (choose the directory your harness recognizes)
Unzip and copy the **folder** `answer-discovery-geo` into your agent skill directory. Common possibilities (verify with your tool's current docs):
- Claude Code: `~/.claude/skills/answer-discovery-geo/` or `.claude/skills/answer-discovery-geo/` in repo.
- Codex: `${CODEX_HOME:-$HOME/.codex}/skills/answer-discovery-geo/` (global) or `.agents/skills/answer-discovery-geo/` (repo-local).
- Other Agent Skills-compatible tools: their documented skills directory.

The official **Agent Skills specification** defines the `SKILL.md` format but does **not** guarantee that every vendor uses the same install path.

## Use it
Tell your agent:

> Use `answer-discovery-geo` in FULL mode. Our offering is [describe capabilities and proof]. Audience: [role/location/language]. Find evidence-backed unbranded questions and current alternatives; score honest fit; plan minimal useful pages, audit OpenAI SearchBot access, and establish a ChatGPT Search baseline. Don't assume invented question templates have search volume and do not assert live recommendations unless tested.

Or run focused modes: `DISCOVER`, `PLAN`, `IMPLEMENT`, `EVALUATE`.

## Local helper commands
```bash
python scripts/seed_questions.py examples/fictional-offer.json --output /tmp/question-seeds.csv
python scripts/site_readiness.py https://example.org --json /tmp/eligibility.json
python scripts/validate_deliverables.py /path/to/project-geo-output
python -m unittest discover -s tests -v
```

Scripts use Python standard library. Live website analysis and ChatGPT search require appropriate network/tools access; scripts cannot measure or manipulate ChatGPT ranking. Website checks must not be treated as proof of indexing or visibility.

## Deliverable structure per research run
```text
geo-project/
  01-offer-and-claims.csv
  02-question-map.csv
  03-opportunities.csv
  04-page-briefs.md
  05-technical-audit.md
  06-chatgpt-evaluations.csv
  07-action-plan.md
  08-research-log.md
```

### Important limits
- There is no publicly documented formula that ensures a ChatGPT recommendation.
- Bing's AI Performance is **not** a direct ChatGPT dashboard.
- An agent-generated question bank is a **hypothesis set**, not verified recurring user questions or search-volume data.
- `llms.txt` is not required for Google Search visibility; don't prioritize it over crawlable and helpful pages.
- Focus on accurate, differentiating evidence and buyer utility rather than synthetic mention farms or mass programmatic landing pages.
