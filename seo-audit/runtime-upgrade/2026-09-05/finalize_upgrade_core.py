from pathlib import Path
import importlib.util,shutil,subprocess
spec=importlib.util.spec_from_file_location('builder','scripts/build_site.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
out=b.ROOT/'output'; core=b.ROOT/'.output-upgrade-core'
assert (core/'upgrade/index.html').is_file()
for p in core.rglob('*.html'):
 rel=p.relative_to(core)
 if rel.parts[0] in ['blog','updates','feed']:continue
 (out/rel).parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,out/rel)
b.merge_webmcp_indexes(out,[core/'.well-known/kujo-site-index.json'])
subprocess.run(['python3',str(b.SSG_ROOT/'scripts/docs_search_index.py'),'--content',str(b.ROOT/'content'),'--output',str(b.ROOT/'assets/js/docs-search-index.json'),'--site-url','https://docs.kujolang.ai'],check=True)
shutil.copy2(b.ROOT/'assets/js/docs-search-index.json',out/'assets/js/docs-search-index.json')
b.finalize_html(out);b.write_aux(out,'https://docs.kujolang.ai')
print('Core pages rebuilt; merged catalog, search and site auxiliaries refreshed.')
