# The Seven Steps - in Detail

This document is the protocol as referenced by the companion article.
It is intentionally short. The discipline of the protocol comes from
*applying* it, not from reading about it.

## Step 1 · Claim Extraction

Break the text into **atomar claims** - single, falsifiable sentences.
"Our model beats the baseline" is not atomar; it conflates *which*
model, *which* baseline, *which* metric.

**Output:** `claim_map.csv` with one row per claim.

## Step 2 · Claim Classification

Each atomar claim is one of seven types:

| Type | Description |
|---|---|
| T1 Stylized Fact | Distributional or descriptive claim about data. |
| T2 Methods | Comparative claim about model/method performance. |
| T3 Causal-Economic | Claim about a causal or leading mechanism. |
| T4 Forecast-Performance | Quantified out-of-sample claim (AUC, MAE, lead time). |
| T5 Regulatory-Legal | Claim about regulation, deadlines, definitions. |
| T6 Remote Sensing | Claim about what a sensor measures or predicts. |
| T7 Market Mechanism | Claim about market dynamics or driver attribution. |

**Why this matters:** A T3 claim cannot be backed by a T1-style anchor
alone, and vice versa.

## Step 3 · Anchor Mapping

For every claim, at least one external anchor from Tier 1 or Tier 2.

| Tier | Source class | Stand-alone valid for |
|---|---|---|
| **T1** | peer-reviewed scientific literature | any claim type |
| **T2** | institutional / authoritative | any claim type |
| **T3** | industry-respected | T2/T4 only, never alone for T1/T3/T6/T7 |
| **T4** | own research with full reproducibility | not alone for T7 |

**Output:** `anchor_mapping.csv` with one row per claim, anchor source,
tier, URL/DOI.

## Step 4 · Reproducibility Bundle

See `templates/reproducibility_bundle.md` for the checklist. Headline
numbers must be reproducible by an external reviewer from a fresh
environment in ≤ 6 commands.

## Step 5 · Steel-Man Counter-Argument

The strongest opposing view, rendered fairly, addressed in-text - not
in a footnote. If you cannot articulate the steel-man, you do not yet
understand the claim well enough to publish it.

## Step 6 · Limitations Section

Dedicated end-of-article section. Three to five limitations that a
knowledgeable reader would actively check.

## Step 7 · Independent Review

A reviewer not involved in drafting checks steps 1-6 and signs off in
the article's footer. The reviewer is named.

## Skin in the game

The protocol scales with the *publication commitment level*:

| Publication type | Required steps |
|---|---|
| Internal discussion paper | none |
| LinkedIn hypothesis post | 1, 2, 6 |
| Medium article / TDS | all 7 |
| SSRN working paper | all 7, plus DOI + versioning |
| Submitted peer-reviewed paper | all 7, formal pre-registration |
