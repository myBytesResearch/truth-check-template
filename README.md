# truth-check-template

Companion repository to the article
**"Ein Truth-Check-Protokoll für AI-Forschungs-Output - wie wir bei
myBytes nichts veröffentlichen, das wir nicht verteidigen können"**
([mybytes.com/research/truth-check-protokoll](https://mybytes.com/research/truth-check-protokoll)).

This repository contains the templates and a reproducible demo notebook
that anyone can use to apply the seven-step truth-check protocol to
their own AI/ML research output, vendor evaluations, or PoC reviews.

## What you get

- `templates/claim_map.csv` - empty template for **Step 1 + 2**:
  atomar claims of an article or pitch, each typed (T1-T7).
- `templates/anchor_mapping.csv` - empty template for **Step 3**: per
  claim, the external evidence anchor with tier classification.
- `templates/reproducibility_bundle.md` - checklist for **Step 4**.
- `notebooks/truth_check_demo.ipynb` - reproduces Plot 3 of the
  companion article from the example claim-map.
- `docs/protocol.md` - the seven steps in detail, as authored.

## The seven steps in one line each

1. **Claim Extraction** - break the text into atomar claims.
2. **Claim Classification** - type each claim (T1 Stylized Fact, T2
   Methods, T3 Causal, T4 Forecast, T5 Regulatory, T6 Remote Sensing,
   T7 Market Mechanism).
3. **Anchor Mapping** - for every claim, at least one Tier-1 or Tier-2
   source. Tier-3 never stands alone.
4. **Reproducibility Bundle** - code, seed, data version, CITATION.cff.
5. **Steel-Man Counter-Argument** - the strongest opposing view,
   addressed in-text.
6. **Limitations** - where would this claim be false?
7. **Independent Review** - second reviewer signs off against 1-6.

## Quick start

```bash
git clone https://github.com/myBytesResearch/truth-check-template.git
cd truth-check-template
python -m pip install -r requirements.txt
jupyter notebook notebooks/truth_check_demo.ipynb
```

## Adapt for your own publication

1. Fork this repo.
2. Copy `templates/claim_map.csv` and `templates/anchor_mapping.csv`
   into your article's working directory.
3. Fill them out as you write. The discipline of doing it inline
   prevents the most common Truth-Check violations.
4. Use the `notebooks/truth_check_demo.ipynb` as a starting point for
   your own claim-map visualisation.

## Tier hierarchy at a glance

| Tier | Definition | Examples |
|---|---|---|
| **T1** | peer-reviewed scientific literature | *Nature*, *Science*, *Econometrica*, *Journal of Finance*, *Remote Sensing of Environment*, SSRN/arXiv with caveat |
| **T2** | institutional, authoritative | IMF, World Bank, FAO, ICCO, USDA, EU Commission, ESA, NASA, MIT NANDA, Gartner Research |
| **T3** | industry-respected (never stands alone) | Mintec, S&P Global Commodity Insights, Argus, Reuters, FT, Bloomberg, Risk.net |
| **T4** | own research with full reproducibility | public repo, fixed seed, dated data version, license-compliant |

## Licence

- **Content** (Markdown, documentation, templates): CC BY 4.0
- **Code** (Python, notebooks): MIT

Both licences explicitly permit forking, adaptation and commercial use.
Attribution to myBytes GmbH appreciated, not required.

## Citation

See `CITATION.cff` for machine-readable metadata. To cite in text:

> Winger, G. & Pianowski, M. (2026). The myBytes Truth-Check Protocol
> for AI Research Output. myBytes GmbH. https://mybytes.com/research/truth-check-protokoll

## Issues, PRs, criticism

Please open issues or PRs. The protocol is explicitly open for
critique - we want it to be stronger after release than before.
