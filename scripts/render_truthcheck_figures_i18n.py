"""Localized (EN/PL) renders of the three truth-check plots for article X2-01.

DE originals are produced by X2-01_render_plots.py. This script reuses the same
executive_plots rendering engine but passes localized labels, and writes
``<name>.en.png`` / ``<name>.pl.png`` into the canonical workspace figures dir.

PL labels are a first draft and must be reviewed by Mariusz (native register).
Defendability numbers are unchanged; only labels are translated.

Output:
    ~/myBytes-workplace/articles/truth-check-protocol/figures/plot{1,2,3}_*.<loc>.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "common"))

from executive_plots import (  # noqa: E402
    FunnelStep,
    TierRow,
    executive_claim_heatmap,
    executive_tier_pyramid,
    executive_truth_funnel,
    set_source_prefix,
)

OUT_DIR = Path(__file__).resolve().parents[1] / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Localized label sets. "en" is final; "pl" is a draft for Mariusz review.
# ---------------------------------------------------------------------------
LOCALES: dict[str, dict] = {
    "en": {
        "source_prefix": "Source: ",
        "funnel_steps": [
            ("1 · Claim Extraction", 1.00),
            ("2 · Classification", 0.92),
            ("3 · Anchor Mapping", 0.74),
            ("4 · Reproducibility", 0.58),
            ("5 · Steel-Man", 0.42),
            ("6 · Limitations", 0.28),
            ("7 · Independent Review", 0.18),
        ],
        "funnel_title": "Seven filters between an AI claim and its publication",
        "funnel_caption": "Most claims do not survive the process. That is exactly why it is here.",
        "funnel_source": "myBytes Research, schema adapted from Gelman & Loken 2014",
        "funnel_annotation": (
            "95% of GenAI pilots without P&L impact (MIT NANDA 2025)  ·  "
            "30% abandoned after PoC (Gartner 2024)"
        ),
        "tiers": [
            ("Tier 1", "peer-reviewed scientific literature",
             "JoF, Econometrica, Nature, Science, RSE"),
            ("Tier 2", "institutional, authoritative",
             "IMF, FAO, ICCO, USDA, EU Commission, ESA, MIT NANDA, Gartner"),
            ("Tier 3", "industry-respected, never on its own",
             "Mintec, Reuters, FT, Bloomberg, Risk.net"),
            ("Tier 4", "own research with full reproducibility",
             "public repo · fixed seed · documented data version"),
        ],
        "tier_title": "Which source suffices for which claim. A hierarchy",
        "tier_caption": ("Tier 3 never suffices on its own. Tier 4 suffices only with "
                         "public code, seed and data version."),
        "tier_source": "myBytes Research, based on ASA Statement 2016 and Ioannidis 2005",
        "heatmap_title": "How this article was checked against its own claims",
        "heatmap_caption": "The protocol is applied, not asserted.",
        "heatmap_source": "myBytes Research, own application of the truth-check protocol",
        "columns": ["Anchor Tier", "Repro Bundle", "Steel-Man", "Limitations", "Reviewer"],
        "claims": [
            "95% of GenAI pilots without P&L impact",
            "30% of GenAI projects abandoned after PoC",
            "Replication crisis as common root cause",
            "SHAP not interpretable as causal",
            "Model Confidence Set handles the multiple-comparison problem",
            "Tier 3 does not suffice for T1/T3/T6/T7",
            "Seven steps scale with the level of commitment",
            "Independent review catches blind spots",
            "Slowing down is intentional",
        ],
    },
    "pl": {
        "source_prefix": "Źródło: ",
        "funnel_steps": [
            ("1 · Ekstrakcja twierdzeń", 1.00),
            ("2 · Klasyfikacja", 0.92),
            ("3 · Mapowanie źródeł", 0.74),
            ("4 · Odtwarzalność", 0.58),
            ("5 · Steel-Man", 0.42),
            ("6 · Ograniczenia", 0.28),
            ("7 · Niezależny przegląd", 0.18),
        ],
        "funnel_title": "Siedem filtrów między twierdzeniem AI a jego publikacją",
        "funnel_caption": ("Większość twierdzeń nie przetrwa tego procesu. "
                           "Właśnie dlatego on istnieje."),
        "funnel_source": "myBytes Research, schemat na podstawie Gelman & Loken 2014",
        "funnel_annotation": (
            "95% pilotaży GenAI bez wpływu na wynik finansowy (MIT NANDA 2025)  ·  "
            "30% porzuconych po PoC (Gartner 2024)"
        ),
        "tiers": [
            ("Poziom 1", "recenzowana literatura naukowa",
             "JoF, Econometrica, Nature, Science, RSE"),
            ("Poziom 2", "instytucjonalne, autorytatywne",
             "IMF, FAO, ICCO, USDA, Komisja Europejska, ESA, MIT NANDA, Gartner"),
            ("Poziom 3", "uznane w branży, nigdy samodzielnie",
             "Mintec, Reuters, FT, Bloomberg, Risk.net"),
            ("Poziom 4", "własne badania z pełną odtwarzalnością",
             "publiczne repozytorium · stałe ziarno · udokumentowana wersja danych"),
        ],
        "tier_title": "Które źródło wystarcza dla którego twierdzenia. Hierarchia",
        "tier_caption": ("Poziom 3 nigdy nie wystarcza samodzielnie. Poziom 4 wystarcza tylko z "
                         "publicznym kodem, ziarnem i wersją danych."),
        "tier_source": "myBytes Research, na podstawie ASA Statement 2016 i Ioannidis 2005",
        "heatmap_title": "Jak ten artykuł sprawdzono względem jego własnych twierdzeń",
        "heatmap_caption": "Protokół jest stosowany, nie deklarowany.",
        "heatmap_source": "myBytes Research, własne zastosowanie protokołu truth-check",
        "columns": ["Anchor Tier", "Repro Bundle", "Steel-Man", "Limitations", "Reviewer"],
        "claims": [
            "95% pilotaży GenAI bez wpływu na wynik finansowy",
            "30% projektów GenAI porzuconych po PoC",
            "Kryzys replikacji jako wspólna przyczyna",
            "SHAP nie jest interpretowalny przyczynowo",
            "Model Confidence Set rozwiązuje problem wielokrotnych porównań",
            "Poziom 3 nie wystarcza dla T1/T3/T6/T7",
            "Siedem kroków skaluje się ze stopniem zobowiązania",
            "Niezależny przegląd wychwytuje martwe punkty",
            "Spowolnienie jest zamierzone",
        ],
    },
}

# claim status matrix (encoding 2=pass, 1=partial, 0=fail, nan=n/a) — language-invariant
CLAIM_MATRIX = [
    (2, np.nan, 2, 2, 1),
    (2, np.nan, 2, 2, 1),
    (2, np.nan, 1, 2, 1),
    (2, np.nan, 1, 2, 1),
    (2, np.nan, 1, 1, 1),
    (1, np.nan, 2, 2, 1),
    (1, np.nan, 2, 2, 1),
    (1, np.nan, 1, 2, 1),
    (1, np.nan, 2, 1, 1),
]


def render_locale(loc: str, L: dict) -> None:
    set_source_prefix(L["source_prefix"])

    # Plot 1 — funnel
    fig1, _ = executive_truth_funnel(
        [FunnelStep(label, pct) for label, pct in L["funnel_steps"]],
        title=L["funnel_title"],
        caption=L["funnel_caption"],
        source=L["funnel_source"],
        header_annotation=L["funnel_annotation"],
    )
    fig1.savefig(OUT_DIR / f"plot1_funnel.{loc}.png", dpi=160, bbox_inches="tight")

    # Plot 2 — tier pyramid
    fig2, _ = executive_tier_pyramid(
        [TierRow(t, d, e) for t, d, e in L["tiers"]],
        title=L["tier_title"],
        caption=L["tier_caption"],
        source=L["tier_source"],
    )
    fig2.savefig(OUT_DIR / f"plot2_pyramid.{loc}.png", dpi=160, bbox_inches="tight")

    # Plot 3 — claim heatmap
    matrix = pd.DataFrame(CLAIM_MATRIX, columns=L["columns"], index=range(1, len(CLAIM_MATRIX) + 1))
    fig3, _ = executive_claim_heatmap(
        matrix,
        claim_texts=L["claims"],
        title=L["heatmap_title"],
        caption=L["heatmap_caption"],
        source=L["heatmap_source"],
    )
    fig3.savefig(OUT_DIR / f"plot3_claim_heatmap.{loc}.png", dpi=160, bbox_inches="tight")


if __name__ == "__main__":
    for loc, L in LOCALES.items():
        render_locale(loc, L)
    set_source_prefix("Quelle: ")  # reset module default for other importers
    print(f"Rendered EN/PL truth-check plots to {OUT_DIR}")
    for p in sorted(OUT_DIR.glob("*.??.png")):
        print(f"  {p.name} ({p.stat().st_size / 1024:.1f} KB)")
