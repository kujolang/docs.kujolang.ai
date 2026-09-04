"""Report assembler for the verified Ability release audit, not a general verdict engine."""
import csv,json,sys,shutil,hashlib,subprocess
from pathlib import Path
from datetime import date,timedelta
repo=Path(sys.argv[1]).resolve();a=repo/'seo-audit/ability-release/2026-09-04';web=(repo/'build.kujo').is_file();origin='https://kujolang.ai' if web else 'https://docs.kujolang.ai';phase=sys.argv[2]
def rows(name):return list(csv.DictReader((a/name).open()))
def write(name,data,fields=None):
 if not data and not fields:return
 with (a/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(data[0]),extrasaction='ignore');w.writeheader();w.writerows(data)
# Enrich the generated inventory with independently preserved live receipts.
pages=rows(phase+'.csv');live=json.loads((a/'raw/live'/f'{phase}-full-crawl.json').read_text())['pages']
for r in pages:
 r['production_status']=live.get(r['url'],{}).get('status','NOT AVAILABLE — DATA ACCESS REQUIRED')
 if not web:
  rel=r['url'].removeprefix(origin).strip('/');source=repo/'content'/(rel+'.md')
  if source.is_file():r['source_file']=str(source.relative_to(repo))
write(phase+'.csv',pages);summary=json.loads((a/(phase+'-summary.json')).read_text());summary['production_200_pages']=sum(str(r['production_status'])=='200' for r in pages);(a/(phase+'-summary.json')).write_text(json.dumps(summary,indent=2)+'\n')
external=json.loads((a/'raw/live'/f'{phase}-external-probes.json').read_text())
e=rows('external-links.csv')
for r in e:
 x=external.get(r['destination_url'],{});r['http_status']=x.get('status','');r['final_url']=x.get('final_url','');r['verification']='indeterminate access' if x.get('status') in ['',401,403,405,429] else 'public GET'
write('external-links.csv',e)
write('broken-links.csv',[r for r in e if str(r['http_status']) in ['404','410']],list(e[0]))
if phase=='baseline':
 for f in ['metadata-audit','content-audit','internal-links','external-links','broken-links','image-audit','schema-audit','indexability','crawlability']:
  shutil.copy2(a/(f+'.csv'),a/('baseline-'+f+'.csv'))
 print(json.dumps(summary));sys.exit()
assert summary['production_200_pages']==summary['canonical_pages'], 'Production inventory is incomplete'
for metric_name in ['missing_titles','duplicate_titles','missing_descriptions','duplicate_descriptions','h1_issues','missing_canonicals','canonical_mismatches','broken_internal_links','orphan_pages','missing_alt','missing_dimensions','schema_parse_errors']:
 assert summary[metric_name]==0, (metric_name,summary[metric_name])
assert not any(x.get('status') in [404,410] for x in external.values()), 'Confirmed external failures remain'
write('site-inventory.csv',pages)
idx=rows('indexability.csv')
for r in idx:
 r['production_status']=live.get(r['url'],{}).get('status','NOT AVAILABLE — DATA ACCESS REQUIRED')
write('indexability.csv',idx)
content=rows('content-audit.csv')
for r in content:
 r['citation_worthiness']='Editorial hypothesis; citation outcomes require platform evidence'
 r['purpose']='Explain '+r.get('topic_entity','this Kujo topic')+' and its documented boundaries'
 r['action']='Review actual user queries and citation evidence before broader editorial changes'
 if r['url'].endswith('/ability/'):
  r['original_evidence']='Tagged Ability release, executable fixtures, compatibility and runtime guides'
  r['gap']='Release coverage resolved; live citation performance unmeasured'
write('content-audit.csv',content)
keys=['canonical_pages','indexable_pages','production_200_pages','sitemap_urls','missing_titles','duplicate_titles','missing_descriptions','duplicate_descriptions','h1_issues','missing_canonicals','canonical_mismatches','broken_internal_links','orphan_pages','pages_deeper_than_three_clicks','missing_alt','missing_dimensions','schema_parse_errors','schema_coverage_pages']
before=json.loads((a/'baseline-summary.json').read_text());table='| Metric | Before | After |\n| --- | ---: | ---: |\n'+''.join(f'| {k} | {before.get(k)} | {summary.get(k)} |\n' for k in keys)
oldext=json.loads((a/'raw/live/baseline-external-probes.json').read_text());badbefore=sum(r.get('status') in [404,410] for r in oldext.values());badafter=sum(r.get('status') in [404,410] for r in external.values());table+=f'| Unique public external 404/410 destinations | {badbefore} | {badafter} |\n| P0 root causes | 0 | 0 |\n| P1 content coverage root causes | 1 | 0 |\n'
(a/'before-after.md').write_text('# Before and after\n\n2026-09-04. Immediate technical evidence only.\n\n'+table+'\n'+('Canonical route count is unchanged.' if web else 'One new canonical route, /tools/ability/, is intentional.')+' Internal scores were not computed: no platform visibility or field performance data supports a complete readiness score.\n')
issues=[]
def issue(id,cat,sev,urls,count,evidence,action,status):issues.append(dict(id=id,phase='after',category=cat,severity=sev,affected_urls=urls,affected_count=count,evidence=evidence,expected_benefit='Accurate discovery and user expectations',confidence='High',difficulty='Low',recommended_action=action,owner='repository maintainers',status=status))
issue('ABILITY-CONTENT','content','P1',origin+('/ecosystem/ability/' if web else '/tools/ability/'),1,'baseline content and release v1.1.0','Publish factual Ability coverage and link installation guidance','resolved')
issue('PRIVATE-SOURCE','external links','P2',origin,4 if web else 2,'baseline-external-links.csv; authenticated GitHub API confirms private repository visibility','Remove public links to private repositories; state source access','resolved')
write('issues.csv',issues)
# Topic map is a review aid, not measured keywords.
write('keyword-map.csv',[dict(phase='after',url=r['url'],primary_topic=r['title'],primary_entity=r['h1'],search_intent='developer task / reference' if not web else 'product discovery / learning',primary_query_theme=r['h1'],secondary_queries='',related_entities='Kujo',relevant_questions='What does this tool do and what are its limits?',competing_internal_url='',content_gap='Ability release coverage addressed; broader intent hypotheses require query data',recommended_action='Measure actual queries; preserve source-backed boundaries') for r in pages])
missing='NOT AVAILABLE — DATA ACCESS REQUIRED'
write('search-rankings.csv',[dict(query=q,search_engine='controlled Google/Bing rank tracking',date='2026-09-04',country=missing,device=missing,page_found=missing,observed_position_or_range=missing,competing_results=missing,rich_features=missing,ai_result_presence=missing,evidence='Public web search returned no reliable Kujo Ability rank observation',limitations='Not evidence of absence from an index') for q in ['Kujo Ability','portable operation contracts','Kujo Ability TypeScript Python SDK']])
write('ai-search-benchmark.csv',[dict(question=q,platform=missing,date='2026-09-04',domain_appeared=missing,domain_cited=missing,cited_url=missing,citation_context=missing,citation_order=missing,competing_domains=missing,accurate_representation=missing,content_gap='Compare factual preview/runtime boundaries',evidence=missing,limitations='Planned controlled benchmark; not an observed answer') for q in ['What is Kujo Ability?','How do I validate an Ability definition?','Can the Ability fixture server run production operations?','How do Ability SDK digests differ from runtime receipts?','How are signed Ability packs verified?']])
performance=[]
for f in sorted((a/'raw').glob('*lighthouse.json')):
 d=json.loads(f.read_text());au=d['audits'];metric=lambda k:au.get(k,{}).get('numericValue','');net=au.get('network-requests',{}).get('details',{}).get('items',[]);weight=lambda kind:sum(x.get('resourceSize',0) for x in net if x.get('resourceType')==kind)
 performance.append(dict(phase=f.name.split('-')[0],url=d.get('finalDisplayedUrl',d.get('requestedUrl')),template='ecosystem detail' if web else 'docs',run_date=d['fetchTime'],environment='Lighthouse default simulated mobile; headless Chrome; local Mac',lighthouse_version=d['lighthouseVersion'],html_bytes=weight('Document'),css_bytes=weight('Stylesheet'),js_bytes=weight('Script'),image_bytes=weight('Image'),font_bytes=weight('Font'),requests=len(net),lcp_ms=metric('largest-contentful-paint'),inp_ms=missing,cls=metric('cumulative-layout-shift'),ttfb_ms=metric('server-response-time'),source=str(f.relative_to(a)),notes='Resource bytes are decoded Lighthouse network sizes. Localhost new-guide smoke is not comparable to live runs. One live run per phase; no field outcome claim'))
write('performance.csv',performance)
(a/'changes.md').write_text('# Changes\n\n'+('Ability product copy now covers SDK previews, offline trust, and fixture tooling without release numbers. A docs link replaces the version-specific install section. Four product pages no longer link to private repositories. Leash and Ward use a private-source template without public clone instructions.' if web else 'Added the Ability installation and reference guide with digest compatibility, SDK preview and fixture boundaries. Linked it from Primitives, Agents SDK, and MCP. Source and Cinch now state that their repositories are private.')+'\n\nSource edits and generated routes are verified through repository contracts and full crawls.\n')
(a/'unresolved.md').write_text('# Unresolved measurements\n\n'+missing+' — Search Console, Bing Webmaster Tools, analytics, full request logs, field CWV, backlinks, controlled rank and AI citation benchmarks. Public GETs blocked by third-party access controls remain indeterminate; see external-links.csv. No remaining confirmed repository-safe P0/P1 defect is established by these checks.\n')
(a/'recommendations.md').write_text('# Measurement plan\n\nRepeat the same route inventory, redirects, crawler profiles, external checks, and mobile lab conditions on '+', '.join(str(date(2026,9,4)+timedelta(days=d)) for d in [7,28,60,90])+'.\n\nWith authorized property data, compare indexing and chosen canonicals; query/page clicks, impressions, CTR and position; Bing citations and cited URLs; AI referrals; field LCP/INP/CLS; and edge 404/5xx URLs. Run the saved AI questions on named platforms and record exact answers, citations, locale, date, and competing domains. Compare competitor intent satisfaction and source evidence only when real results are available. Do not infer improvement from this technical audit. No scheduled automation or submission was created.\n')
(a/'methodology.md').write_text('# Methodology\n\n2026-09-04. Scope: both full canonical inventories, with release editorial review focused on Ability and source-access corrections. Audience: developers evaluating and adopting Kujo. Primary conversions: docs, reviewed source, and installation. English canonical HTTPS origins.\n\nSource → Kujo SSG static output → GitHub Pages → public domain/edge. Docs publishes gh-pages; the product site main branch triggers its pinned Pages workflow. DNS/WAF policy was unchanged. Docs builds through scripts/build_site.py with sibling SSG; the product uses its vendored build.kujo plus npm run images:responsive. Local builds used the checksum-verified Kujo v1.2.3 macOS x64 archive ca53715bb65f69386c5ab3c9fe5624c4c7409e33d0734e29afa918aef76f0bbe. Runtime overrides were local, not committed absolute dependencies.\n\nBaseline output was preserved from the already verified, immutable GitHub deployment before editing. The product artifact comes from successful workflow 33922119926 at cd00a3a; later source differences are audit records only. Docs uses gh-pages f856e51, qualified by the prior same-day audit at source 8fddff9; current source differs only in audit records and gitignore. Redundant local baseline builds were stopped under heavy machine load. raw/baseline-manifest.json seals every generated file. Source commit, live HTML bodies, HTTP headers, and lab JSON are preserved separately. Baseline CSVs are immutable. Run the preserved crawl scripts with --repo, --output, --origin, --audit-dir and --phase; live_crawl.py accepts origin, audit path and phase. Reuse identical inventories, then explain the new docs route.\n\nTechnical crawl covers titles/descriptions, H1/heading structure, canonical/robots/sitemap consistency, graph depth/orphans, media existence/alt/dimensions, schema parsing, external HTTP destinations, and all static HTML. Content and query maps are source-based intent review aids, not measured queries or automatic quality verdicts. No rankings, citations, authorship, expertise, field CWV, or rich-result eligibility was fabricated. The Cloudflare /cdn-cgi/l/email-protection helper discovered on the public edge is infrastructure, not a sitemap/canonical content page.\n\nBaseline and after Lighthouse use the same existing representative route; the new Ability docs route is separately checked by crawl and visual review. Training policy, DNS, analytics and search submissions are outside the implemented changes. Scores omitted rather than presented as platform measurements.\n')
(a/'executive-summary.md').write_text('# Ability release audit\n\n**PASS WITH RECOMMENDATIONS** — 2026-09-04.\n\n'+str(summary['canonical_pages'])+' canonical pages audited, '+str(summary['production_200_pages'])+' serving HTTP 200 after deployment. '+('Four product content pages and the private-source template changed.' if web else 'Six docs content pages were added or updated.')+' One content-coverage root cause (P1) was resolved; P0 remained zero. Private-source links were corrected from verified access evidence.\n\n'+table+'\nInternal SEO/AI scores: not computed. Lab evidence: performance.csv and raw Lighthouse JSON. Search visibility and AI citation outcomes: NOT AVAILABLE — DATA ACCESS REQUIRED. No outcome improvement claimed.\n\nSee issues.csv, changes.md, methodology.md, data-availability.md, and recommendations.md for reproducible evidence and 7/28/60/90-day measurements.\n')
print(json.dumps(summary))
