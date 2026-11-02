#!/usr/bin/env python3
"""Read-only, limited technical eligibility inspection for a PUBLIC URL.
Does not establish indexing or verified OAI bot reachability. Uses stdlib only.
"""
import argparse
import json
import re
import urllib.parse
import urllib.request
import urllib.robotparser
from html.parser import HTMLParser

class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=''; self.h1=[]; self.meta={}; self.links=[]; self.jsonld=0; self._title=False; self._h1=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); tag=tag.lower()
        if tag=='title': self._title=True
        if tag=='h1': self._h1=True; self.h1.append('')
        if tag=='meta':
            name=(a.get('name') or a.get('http-equiv') or a.get('property') or '').lower()
            if name: self.meta[name]=a.get('content','')
        if tag=='link': self.links.append(a)
        if tag=='script' and a.get('type','').lower()=='application/ld+json': self.jsonld+=1
    def handle_endtag(self,tag):
        if tag=='title': self._title=False
        if tag=='h1': self._h1=False
    def handle_data(self,text):
        if self._title: self.title+=text
        if self._h1 and self.h1: self.h1[-1]+=text

def fetch(url,limit=300000):
    req=urllib.request.Request(url,headers={'User-Agent':'AnswerDiscoveryGEO-Audit/1.0 (read-only public site inspection)'})
    with urllib.request.urlopen(req,timeout=10) as r:
        content=r.read(limit).decode('utf-8',errors='replace')
        return {'status':r.status,'final_url':r.geturl(),'headers':dict(r.headers),'body':content}

def inspect(url):
    parts=urllib.parse.urlsplit(url)
    if parts.scheme not in ('https','http') or not parts.hostname: raise ValueError('HTTP(S) public URL required')
    if parts.username or parts.password: raise ValueError('Credential-bearing URLs not supported')
    # Safety: no probing local, link-local, private IP literals.
    import ipaddress
    hostname=parts.hostname.lower()
    if hostname in ('localhost',) or hostname.endswith(('.local','.internal')): raise ValueError('Local destinations not allowed')
    try:
        ip=ipaddress.ip_address(hostname)
        if not ip.is_global: raise ValueError('Non-public IP not allowed')
    except ValueError as exc:
        if str(exc)=='Non-public IP not allowed': raise
    site=fetch(url); final=urllib.parse.urlsplit(site['final_url']); base=f'{final.scheme}://{final.netloc}'
    if site['final_url'].startswith(('http://127.','http://localhost','http://169.254.')): raise ValueError('Redirect to local target is not supported')
    p=Tags(); p.feed(site['body'])
    result={'requested_url':url,'resolved_url':site['final_url'],'http_status':site['status'],
            'content_type':site['headers'].get('Content-Type',''),
            'title':p.title.strip(), 'h1s':[x.strip() for x in p.h1[:5]],
            'meta_description':p.meta.get('description',''),
            'meta_robots':p.meta.get('robots',''),
            'x_robots_tag':site['headers'].get('X-Robots-Tag',''),
            'canonical':[urllib.parse.urljoin(base,x.get('href','')) for x in p.links if x.get('rel','').lower()=='canonical'],
            'jsonld_script_count':p.jsonld, 'robots_txt':None,'sitemap_xml':None,
            'warnings':[], 'notes':['Heuristic read-only check. Not proof of indexing, OAI-SearchBot origin access, or ChatGPT recommendation.']}
    if not p.title: result['warnings'].append('Missing HTML title in fetched document')
    if not p.h1: result['warnings'].append('No H1 found in fetched document')
    if 'noindex' in (result['meta_robots']+' '+result['x_robots_tag']).lower(): result['warnings'].append('Page includes noindex directive')
    try:
        robots=fetch(base+'/robots.txt',limit=100000)
        rp=urllib.robotparser.RobotFileParser(); rp.parse(robots['body'].splitlines())
        result['robots_txt']={'status':robots['status'],'searchbot_can_fetch_url_per_rules':rp.can_fetch('OAI-SearchBot',site['final_url']),
                              'sample_excerpt':robots['body'][:3000], 'note':'Uses simple robots parser; real crawlers may see WAF/edge differences.'}
        if not result['robots_txt']['searchbot_can_fetch_url_per_rules']: result['warnings'].append('Robots rules appear to disallow OAI-SearchBot on this URL')
    except Exception as e: result['warnings'].append('Could not inspect robots.txt: '+str(e)[:140])
    try:
        sitemap=fetch(base+'/sitemap.xml',limit=5000)
        result['sitemap_xml']={'status':sitemap['status'],'looks_like_sitemap':('<urlset' in sitemap['body'] or '<sitemapindex' in sitemap['body'])}
    except Exception as e: result['warnings'].append('Could not inspect default /sitemap.xml: '+str(e)[:120])
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('url'); ap.add_argument('--json'); a=ap.parse_args()
    try: out=inspect(a.url)
    except Exception as e: print('ERROR:',e); raise SystemExit(2)
    data=json.dumps(out,indent=2,ensure_ascii=False)
    if a.json:
        from pathlib import Path
        Path(a.json).write_text(data+'\n',encoding='utf-8')
        print('Saved heuristic audit to',a.json)
    else: print(data)
if __name__=='__main__':main()
