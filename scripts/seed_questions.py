#!/usr/bin/env python3
"""Seed plausible unbranded buyer questions for research, never measured demand.
Usage: python scripts/seed_questions.py brief.json --output seeds.csv
Only capabilities_verified are used. Planned capabilities are excluded.
"""
import argparse
import csv
import json
import re
from pathlib import Path

TEMPLATES = [
    ('T01', 'How can {audience} solve {problem}?'),
    ('T01', 'What is a practical way to fix {problem} {constraint}?'),
    ('T02', 'Is there a {category} that helps with {job}?'),
    ('T02', 'What type of solution is suitable for {problem}?'),
    ('T03', 'Which {category} providers are worth comparing for {job}?'),
    ('T03', 'Can anyone recommend a {category} for {audience}?'),
    ('T04', 'What does a {category} typically cost for {audience}?'),
    ('T04', 'Are there free or low-cost approaches to {job}?'),
    ('T05', 'How can I customize the workflow for {job}?'),
    ('T05', 'Which tools give {audience} control over {capability}?'),
    ('T06', 'Can {tool} be integrated into a workflow for {job}?'),
    ('T06', 'How do I connect {tool} without replacing the current system?'),
    ('T07', 'What alternative workflow solves {problem} with minimal migration?'),
    ('T07', 'How would I migrate from a manual process for {job}?'),
    ('T08', 'Is it better to build or buy a solution for {job}?'),
    ('T08', 'What are the tradeoffs between doing {job} manually and automating it?'),
    ('T09', 'Which providers in {region} can help with {job}?'),
    ('T09', 'Can I get a {category} service in {region}?'),
    ('T10', 'What is a suitable {category} for {audience}?'),
    ('T10', 'Can a small team handle {job} without a full IT department?'),
    ('T11', 'How do companies handle {problem} in practice?'),
    ('T11', 'What does a successful implementation for {job} look like?'),
    ('T12', 'How can I manage data privacy while solving {problem}?'),
    ('T12', 'Can I solve {problem} without uploading sensitive data?'),
    ('T13', 'What are reliability limits of solutions for {job}?'),
    ('T13', 'What happens when a system for {job} goes offline?'),
    ('T14', 'How do I start implementing a solution for {job}?'),
    ('T14', 'What should I prepare before hiring someone for {job}?'),
    ('T15', 'Is automation worth the cost for {problem}?'),
    ('T15', 'How do I estimate the ROI of improving {job}?'),
    ('T16', 'What metrics tell me whether I have solved {problem}?'),
    ('T16', 'How do I diagnose the root cause of {problem}?'),
    ('T17', 'What questions should I ask a {category} provider?'),
    ('T17', 'How should I compare quotes for {job}?'),
    ('T18', 'What limitations should I watch for when solving {problem}?'),
    ('T18', 'Who should avoid buying a {category} for {job}?'),
]

def first(items, fallback):
    return next((str(x).strip() for x in items if str(x).strip()), fallback)


def generate(brief):
    """Return a deduplicated, labeled candidate list with intentionally no frequency claim."""
    audience=brief.get('audience') or ['a small team']
    jobs=brief.get('jobs_to_be_done') or ['their workflow']
    problems=brief.get('problems') or jobs
    capabilities=brief.get('capabilities_verified') or ['the stated requirement']
    constraints=brief.get('constraints') or ['with minimal overhead']
    regions=brief.get('geographies') or ['my region']
    tools=brief.get('existing_tools') or ['an existing system']
    category=brief.get('category') or 'service or software'
    fmt = {'audience':first(audience,'a small team'), 'job': first(jobs,'a manual workflow'),
           'problem':first(problems,'manual work'), 'constraint':first(constraints,'without high cost'),
           'capability':first(capabilities,'the required workflow'), 'tool': first(tools,'my current system'),
           'region': first(regions,'my region'), 'category':category}
    expanded=[]
    # Alternate across at most three jobs and problems; avoid combinatorial doorway content.
    pairs=max(1,min(3,max(len(jobs),len(problems))))
    for i in range(pairs):
        f=dict(fmt); f['job']=str(jobs[i % len(jobs)]); f['problem']=str(problems[i % len(problems)])
        if capabilities: f['capability']=str(capabilities[i % len(capabilities)])
        if constraints: f['constraint']=str(constraints[i % len(constraints)])
        if audience: f['audience']=str(audience[i % len(audience)])
        for family,template in TEMPLATES:
            q=re.sub(r'\s+',' ',template.format(**f)).strip()
            expanded.append((family,q))
    seen=set(); result=[]
    for family,q in expanded:
        key=q.lower()
        if key in seen: continue
        seen.add(key)
        result.append({'id':f'Q{len(result)+1:03}', 'intent_family':family,
                       'question':q,'origin_label':'HYPOTHESIS',
                       'source_url':'','observed_frequency':'unknown',
                       'verified_offer_fit':'NOT_REVIEWED'})
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('brief',type=Path)
    ap.add_argument('--output',type=Path,default=Path('question-seeds.csv'))
    a=ap.parse_args()
    data=json.loads(a.brief.read_text(encoding='utf-8'))
    out=generate(data)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f'Wrote {len(out)} HYPOTHESIS candidate questions to {a.output}; NO frequency/volume measured.')

if __name__=='__main__': main()
