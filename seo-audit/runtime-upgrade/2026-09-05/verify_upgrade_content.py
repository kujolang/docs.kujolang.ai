from pathlib import Path
from bs4 import BeautifulSoup
import json,sys
root=Path(sys.argv[1]); kind=sys.argv[2]
if kind=='docs':
 page=root/'upgrade/index.html'; s=BeautifulSoup(page.read_text(),'html.parser'); body=s.select_one('.docs-body').get_text(' ',strip=True)
 for term in ['v1.2.3','unreleased','--check','--json','--allow-downgrade','not proof of ownership','manual recovery','standalone Kujo executable','no failure JSON']:
  assert term in body,term
 assert s.find('link',rel='canonical')['href']=='https://docs.kujolang.ai/upgrade/'
 assert len(s.find_all('h1'))==1
 for route in ['install','reference','start-here','release-boundaries','tools/kujo']:
  h=BeautifulSoup((root/route/'index.html').read_text(),'html.parser')
  assert h.select_one('.docs-body a[href="/upgrade/"]'),route
 assert 'https://docs.kujolang.ai/upgrade/' in (root/'sitemap.xml').read_text()
 assert '/upgrade/' in (root/'assets/js/docs-search-index.json').read_text()
 assert '/upgrade/' in (root/'llms.txt').read_text()
else:
 for path in ['index.html','ecosystem/kujo/index.html']:
  s=BeautifulSoup((root/path).read_text(),'html.parser')
  assert s.select_one('footer a[href="https://docs.kujolang.ai/upgrade/"]')
  dialog=s.select_one('[data-quick-install-modal]')
  assert 'unreleased' in dialog.get_text() and 'v1.2.3' in dialog.get_text()
 s=BeautifulSoup((root/'ecosystem/kujo/index.html').read_text(),'html.parser')
 for term in ['--check --json','manual recovery','package manager']:
  assert term in s.get_text(' ',strip=True),term
for p in root.rglob('*.html'):
 s=BeautifulSoup(p.read_text(),'html.parser')
 for script in s.select('script[type="application/ld+json"]'): json.loads(script.string or script.get_text())
print(kind+': upgrade content, availability, discovery links, and JSON-LD passed')
