# Raw evidence

`baseline-output/` is the immutable local multi-section baseline and is ignored to avoid duplicating generated site artifacts in Git. Its per-file SHA-256 manifest and source commit are tracked beside this file. `baseline-output-incomplete/` preserves the excluded stale local artifact for this working copy only. Live HTTP and Lighthouse receipts remain tracked and normalized into the parent datasets.
