# ChatGPT Search eligibility & technical content playbook

## Key crawler facts (OpenAI primary documentation)
- `OAI-SearchBot`: ChatGPT search crawling; allow through robots.txt and relevant WAF/bot controls and published IP ranges if desired. Searchbot access makes you **eligible**, not included. Check https://developers.openai.com/api/docs/bots and https://openai.com/searchbot.json.
- `GPTBot`: separate foundation-model training crawler. You may disallow it while allowing search. Do not conflate model training with real-time ChatGPT Search.
- `ChatGPT-User`: user-requested fetches, not a substitute for automated Searchbot access; not used to determine search inclusion.
- CDN, firewall, authentication and JS rendering can matter. A `robots.txt` `Allow` directive alone does not prove actual crawler access or indexing.

## Review checklist
1. Resolve scheme, redirects, final URL, host, certificate, and HTTP 200 public content.
2. Request `/robots.txt` on each relevant host and check for `OAI-SearchBot` and `*` rules and relevant disallows; record CDN/network uncertainty. Example only (do not overwrite existing controls):

```text
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

3. Inspect `meta robots` and `X-Robots-Tag` for `noindex`/`nosnippet` and accidental disallow. Validate canonical, hreflang (if truly localized), sitemap and internal links.
4. Read **HTML before JS execution** for answer-bearing information: title, H1, actual useful page copy, pricing and supported features. Rendering should not depend solely on browser JS or gated dashboard. Check mobile/accessibility with appropriate authorized tools.
5. Audit Cloudflare or other WAF challenge behavior for real verified crawler agents. IP rules should use up-to-date official lists; never unconditionally trust forged user-agent strings.
6. Verify structured data corresponds exactly to public visible content; `Organization`, `Service`, `SoftwareApplication`, `FAQPage` only as legitimately relevant. Do not fabricate ratings, offers or price. Google FAQ rich results were removed in 2026; FAQ content is for readers, not a promised Google rich-result hack.
7. Ensure consistent name/publisher/category and accurate price/version/capabilities across homepage, docs, directories, profiles, screenshots, changelog, schema and third-party sources.
8. Monitor logs for crawler user agents, origin errors and cache challenges; filter with actual IP verification. Do not infer crawling from a spoofable user-agent alone.
9. Publish in a coherent hierarchy and submit XML sitemaps to search webmaster tools as appropriate; record date, error codes and status. IndexNow may be useful for participating engines; not an OpenAI submission shortcut.

## What not to prioritize
- `llms.txt` is not documented as necessary for ChatGPT Search placement; Google explicitly states it does not use llms.txt for Google Search. Optional only for an explicitly supported workflow.
- No mass-production of geo-keyword doorway pages, hidden AI prompt injections, fake Q&A, schema manipulation, fabricated review widgets, irrelevant pages.
- Rankings are probabilistic, not controlled by a bot directive, FAQ markup or generic "AI-friendly" formatting trick.

## Read-only helper script
`python scripts/site_readiness.py https://example.org --json readiness.json`
Checks simple HTTP HTML, title, description, H1, canonical, robots and sitemap clues. It is not a web crawler, cannot see internal analytics, nor verify WAF behavior for OpenAI's real IPs. Network requests require authorized environment access.
