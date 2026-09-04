import sys,csv,json,urllib.request,urllib.error,concurrent.futures
from pathlib import Path
p=Path(sys.argv[1]);phase=sys.argv[2];rows=list(csv.DictReader((p/'external-links.csv').open())); urls=sorted({r['destination_url'] for r in rows if r['destination_url'].startswith(('http:','https:'))})
def check(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'KujoReleaseAudit/1.0'}),timeout=15) as r:return u,dict(status=r.status,final_url=r.url,headers=dict(r.headers))
    except urllib.error.HTTPError as e:return u,dict(status=e.code,final_url=e.url)
    except Exception as e:return u,dict(status='',error=str(e),final_url=u)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: receipts=dict(pool.map(check,urls))
for r in rows:
    receipt=receipts.get(r['destination_url'],{});r['http_status']=receipt.get('status','');r['final_url']=receipt.get('final_url','');r['verification']='indeterminate access' if receipt.get('status') in ['',401,403,405,429] else 'public GET';r['phase']=phase
with (p/'external-links.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(p/'raw/live'/f'{phase}-external-probes.json').write_text(json.dumps(receipts,indent=2))
print(json.dumps({'destinations':len(urls),'unavailable':{u:r for u,r in receipts.items() if r['status'] in [404,410]}}))
