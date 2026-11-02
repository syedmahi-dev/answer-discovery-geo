#!/usr/bin/env python3
"""Check GEO output file presence and machine-checkable evidence labels.
This complements, not replaces, human QA of claims and citations.
"""
import argparse,csv,sys
from pathlib import Path
REQUIRED=['01-offer-and-claims.csv','02-question-map.csv','03-opportunities.csv','04-page-briefs.md','05-technical-audit.md','06-chatgpt-evaluations.csv','07-action-plan.md','08-research-log.md']
LABELS={'OBSERVED','INFERRED_FROM_SOURCE','HYPOTHESIS'}
def validate(root):
    errors=[]; warnings=[]
    for n in REQUIRED:
        if not (root/n).exists(): errors.append('Missing '+n)
    p=root/'02-question-map.csv'
    if p.exists():
        with p.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
        if not rows: warnings.append('Question map has no rows')
        for i,row in enumerate(rows,2):
            label=row.get('origin_label','').upper().strip()
            if label not in LABELS: errors.append(f'Question row {i}: missing/invalid origin_label')
            if label=='OBSERVED' and not (row.get('source_url_or_ref') or '').strip(): errors.append(f'Question row {i}: observed but no source link/ref')
            if label=='HYPOTHESIS' and (row.get('frequency_value') or '').strip() not in ('','unknown','n/a','NA'): warnings.append(f'Question row {i}: hypothesis has frequency; investigate source')
    q=root/'06-chatgpt-evaluations.csv'
    if q.exists():
        with q.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
        for i,row in enumerate(rows,2):
            prompt=(row.get('unbranded_prompt') or '').strip()
            if not prompt: errors.append(f'Evaluation row {i}: missing prompt')
            if not (row.get('session_id') or '').strip(): errors.append(f'Evaluation row {i}: missing session ID')
            if not (row.get('date_utc') or '').strip(): errors.append(f'Evaluation row {i}: missing date')
    return errors,warnings

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('folder',type=Path);a=ap.parse_args()
    errors,warnings=validate(a.folder)
    for msg in errors:print('ERROR:',msg)
    for msg in warnings:print('WARN:',msg)
    print('Result:', 'FAIL' if errors else 'PASS',f'({len(errors)} errors, {len(warnings)} warnings)')
    sys.exit(1 if errors else 0)
if __name__=='__main__':main()
