import hashlib,json,shutil,subprocess,sys
from pathlib import Path
repo=Path(sys.argv[1]).resolve();a=repo/'seo-audit/ability-release/2026-09-04'; raw=a/'raw';raw.mkdir(exist_ok=True)
for name in ['redirects.csv','crawler-access.csv']:
    if (a/name).exists(): shutil.copy2(a/name,a/('baseline-'+name))
dest=raw/'baseline-output';shutil.copytree(repo/'output',dest)
manifest={str(p.relative_to(dest)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.rglob('*')) if p.is_file()}
(raw/'baseline-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(raw/'baseline-source-commit.txt').write_text(subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True))
shutil.copy2(Path(__file__).with_name('live_crawl.py'),a/'live_crawl.py')
print(len(manifest),'baseline files sealed',repo)
