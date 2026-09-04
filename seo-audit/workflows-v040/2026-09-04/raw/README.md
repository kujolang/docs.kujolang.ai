# Raw evidence

`baseline-output/` is the immutable deployed `gh-pages` artifact at the commit
recorded in `deployment-commit.txt`. It is excluded from Git because it
duplicates generated site output. `baseline-output-sha256.txt` fingerprints
every file. The tracked Lens reports, screenshots, and production diagnostics
preserve the bounded browser and edge evidence used by this audit.

The verified after build is the source commit recorded in `after-commit.txt`
and deployed `gh-pages` commit recorded in `after-deployment-commit.txt`.
`after-output-sha256.txt` fingerprints the clean local build that matched the
deployed output.
