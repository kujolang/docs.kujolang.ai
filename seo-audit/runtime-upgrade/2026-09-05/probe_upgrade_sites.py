from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
import json,hashlib,ssl,sys
from bs4 import BeautifulSoup
phase=sys.argv[1]
root=Path('/Users/robertdevore/2026/Kujolang/kujo-repos')
for repo,host,routes in [('docs.kujolang.ai','docs.kujolang.ai',['/','/upgrade/','/install/','/reference/','/start-here/','/release-boundaries/','/tools/kujo/','/robots.txt','/sitemap.xml','/llms.txt','/assets/js/docs-search-index.json','/upgrade-audit-missing-20260905/']),('kujolang.ai-work','kujolang.ai',['/','/ecosystem/kujo/','/robots.txt','/sitemap.xml','/upgrade-audit-missing-20260905/'])]:
 a=root/repo/'seo-audit/runtime-upgrade/2026-09-05'; raw=a/'raw'/phase; raw.mkdir(parents=True,exist_ok=True)
 requests=[('https://'+host+p,'Mozilla/5.0',p) for p in routes]+[('http://'+host+'/','Mozilla/5.0','http-home')]+[('https://'+host+('/upgrade/' if host.startswith('docs.') else '/ecosystem/kujo/'),ua,'crawler-'+ua) for ua in ['Googlebot','OAI-SearchBot','ChatGPT-User','GPTBot']]
 def fetch(item):
  url,ua,label=item
  try:
   try: response=urlopen(Request(url,headers={'User-Agent':ua}),timeout=30)
   except HTTPError as e: response=e
   body=response.read(); final=response.url; status=response.code; headers=dict(response.headers)
   filename=label.strip('/').replace('/','_') or 'home'; (raw/(filename+'.body')).write_bytes(body)
   soup=BeautifulSoup(body,'html.parser') if 'text/html' in headers.get('Content-Type','') else None
   canonical=soup.find('link',rel='canonical') if soup else None
   meta=soup.find('meta',attrs={'name':'description'}) if soup else None
   row=dict(url=url,user_agent=ua,status=status,final_url=final,headers=headers,sha256=hashlib.sha256(body).hexdigest(),bytes=len(body),title=soup.title.get_text() if soup and soup.title else None,description=meta.get('content') if meta else None,canonical=canonical.get('href') if canonical else None,h1_count=len(soup.find_all('h1')) if soup else None,upgrade_mentioned=b'kujo upgrade' in body or b'/upgrade/' in body)
   return row
  except Exception as e: return dict(url=url,user_agent=ua,error=str(e))
 with ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(fetch,requests))
 (a/(phase+'-live-probes.json')).write_text(json.dumps(rows,indent=2)+'\n')
 print(repo,[(r['url'],r.get('status',r.get('error'))) for r in rows])
