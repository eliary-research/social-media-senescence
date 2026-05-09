# Social Media Senescence — Working Paper

> Kim, C. (2026). *Social Media Senescence: Why Platforms Age and What Comes After*. Working paper, Eliary Inc.

**Status:** Draft v0.1 (~5,600 words, 8 sections). Cleanup in progress, target arXiv `cs.SI` submission by 2026-05-12.
**Target venue:** ICWSM 2027 (full paper, January 2027 submission).
**Author:** Chanmin Kim (Eliary Inc.).
**License:** Paper + data — CC BY 4.0. Code — MIT.

---

## Abstract

Social media platforms follow a remarkably consistent lifecycle: explosive growth, maturation, and eventual decline. We term this pattern *social media senescence* and argue it is not incidental but structurally inevitable in advertising-funded platforms optimizing for engagement. Drawing on 56 quarters of Meta financial disclosures (2012–2025), 36 quarters of Snap Inc. data, Pew Research Center surveys tracking generational adoption across six platforms (2012–2025), and lifecycle records of 15 question-based social platforms, we formalize a senescence model identifying three causal mechanisms: (1) the *advertising ratchet*; (2) *generational displacement*; and (3) *content inflation*. We further introduce a platform taxonomy based on content production models — Push (user-initiated) versus Pull (externally prompted) — crossed with interaction accumulation structure. Question-based platforms exhibit the fastest senescence (median active lifespan: 2–4 years) due to one-shot interaction structures. We conclude by proposing structural design principles — pull-driven content with accumulation, weighted relationship edges, and planned ecosystem succession — that may delay senescence onset.

**Keywords:** social media, platform lifecycle, senescence, network effects, enshittification, question platforms, generational displacement.

## Why this paper

The standard accounts of platform decline — algorithmic mismanagement, competitive displacement, generational fashion — describe correlates rather than mechanisms. This paper proposes a structural model: senescence is the predictable consequence of advertising-funded engagement optimization, not a sequence of bad management decisions. The model is testable, the data is public, and the implications are actionable for platform designers.

## Companion papers

- **EN6 (Signal Inflation Hypothesis)** — micro-level mechanism explaining how the like button passes through inflation → toxicity → deprecation. EN1 macro / EN6 micro form a complementary pair.
- **EN4 (Political Economy of Platform Competition)** — structural-realism analysis of why platforms converge on the same advertising-driven design even when alternatives are available.
- **CC6 (The Single-Creator Trap)** — prospective case study of cold-start dynamics on a single platform; EN1 micro-evidence for the senescence model at the moment of birth.
- **EN5 (Signal Cost of Connection)** — preregistered field experiment testing whether human-only signals produce different relationship outcomes than AI-mixed signals.

## Repository contents

```
EN1/
├── README.md             ← this file
├── CITATION.cff          ← citation metadata
├── LICENSE               ← MIT (code, prose)
├── LICENSE-DATA          ← CC BY 4.0 (data/ directory)
├── outline.md            ← framework + hypothesis structure
├── draft.md              ← v0.1, ~5,600 words, 8 sections
├── references.md         ← 30+ entries, bibliography in progress
├── citation_audit.md     ← inline citation cross-check (in progress)
├── data/
│   ├── meta_quarterly_sources.md         ← 56 quarters Meta SEC filings
│   ├── snap_quarterly_sources.md         ← 36 quarters Snap SEC filings
│   ├── engagement_rate_decline.md        ← Rival IQ / Socialinsider sources
│   ├── att_impact_research.md            ← Apple ATT natural experiment
│   └── dead_internet_authenticity_research.md
└── figures/
    ├── senescence_curves.pdf             ← 4-stage lifecycle illustration
    ├── generational_shift.pdf            ← cohort displacement (Pew data)
    ├── question_platform_lifecycle.pdf   ← 15-platform median lifespan
    └── snap_recovery.pdf                 ← Snapchat 2018 redesign case
```

## Key empirical claims

- Meta organic reach declined from approximately 16% (2012) to under 1.5% (2023) — verified against Edgerank Checker, Social@Ogilvy, and Locowise sources.
- Question platform median active lifespan: 2–4 years across 15 surveyed platforms (Formspring, Ask.fm, Sarahah, tbh, Gas, NGL, Yik Yak, etc.) — roughly one-fifth the lifespan of content-based platforms.
- Generational displacement: Pew Research data shows youth (13–17) abandonment of Facebook beginning ~2017, paralleled by parental adoption beginning 2014.
- Snapchat's 2018 redesign crisis (DAU 191M → 186M) and subsequent recovery support the claim that signal cost is a determinant of platform resilience.

## Roadmap to arXiv submission

| Date | Action |
|---|---|
| 2026-05-03 | WIP repo public — draft v0.1 + outline + references + 4 figures |
| 2026-05-08 → 5/12 | Tier A cleanup — section §6 empirical analysis code execution, references.md → BibTeX inline, CSV ↔ body number verification, arXiv typeset |
| Post-endorsement | Submission to arXiv `cs.SI` (primary), `econ.GN` and `physics.soc-ph` cross-list. Endorser: Prof. Jong Hee Park (SNU PSIR; MCMCpack co-developer; APSA Best Methodology 2010, Best Software 2013). |
| 2026-10 (target) | Full paper submission to ICWSM 2027 |

## Positionality

The first author operates Eliary Inc., parent of Currot — a social platform that implements several of the structural alternatives discussed in §6. All quantitative data in this analysis is drawn from public sources (SEC filings, Pew Research, published industry benchmarks). The theoretical framework predates the platform's operational evolution; the SSRN/arXiv timestamp of this manuscript serves as a public freeze-point for the framework prior to subsequent operational outcomes. A companion preregistered field experiment (EN5; OSF DOI forthcoming) further constrains the dual-role concern by locking analytic specifications in advance.

## Citing this work

```bibtex
@misc{kim2026senescence,
  author       = {Kim, Chanmin},
  title        = {Social Media Senescence: Why Platforms Age and What Comes After},
  year         = {2026},
  howpublished = {Working paper, Eliary Inc.},
  note         = {arXiv submission in preparation},
  url          = {https://github.com/eliary-research/social-media-senescence}
}
```

A `CITATION.cff` file is provided for automated citation parsers.

## Contact

Chanmin Kim — chanmin@eliary.com
