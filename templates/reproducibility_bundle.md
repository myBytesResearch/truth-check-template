# Reproducibility Bundle Checklist (Step 4)

Use this checklist for every publication that contains numerical claims.
Tick each box; if a box cannot be ticked, document the reason in the
article's Limitations section.

## Code

- [ ] All scripts/notebooks producing claims are in version control.
- [ ] Random seed is fixed and documented.
- [ ] `requirements.txt` (or `pyproject.toml`) pins library versions
      to a known-good state.
- [ ] Notebook runs end-to-end in a fresh environment.

## Data

- [ ] Data source is named explicitly (URL or DOI).
- [ ] Date of data pull is recorded.
- [ ] If data is proprietary: an anonymised demo dataset is included
      that runs the same pipeline.
- [ ] Data licence is checked and stated.

## Metadata

- [ ] `CITATION.cff` present and up-to-date.
- [ ] `LICENSE` file present (code + content licences clear).
- [ ] `README.md` explains the reproduction steps in ≤ 6 commands.

## CI

- [ ] A CI workflow runs the key notebook on every push and fails on
      regression in the headline number(s).

## Independent Review

- [ ] A reviewer not involved in the original draft has reproduced the
      headline number from scratch.
- [ ] Reviewer is named in the article footer.
