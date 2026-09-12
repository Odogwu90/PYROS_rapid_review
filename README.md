# Do skilled professionals who migrate and restart their careers show more depressive symptoms than recent graduates who migrate before establishing a career? A rapid review.

A rapid literature review produced for **PYROS** (PyNexus research channel).

**Director and reviewer:** Dr. Okpara Onyedikachi Martins (MBBS, Nigeria; MSc Global Health, University of Bonn).
**Analytic and drafting support:** Claude (Anthropic), working under the rules in `CLAUDE.md`. All study selection, data verification and conclusions are made by Dr. Okpara.

## Status

| Step | Description | Status |
|------|-------------|--------|
| 1 | Protocol | v0.2 approved 2026-09-12 |
| 2 | Project scaffold (folders, git, log templates) | Done |
| 3 | Search strings per database | Done (search/search_strategy.md); searches to be run by reviewer |
| 4 | Screening | PubMed: 215 screened, 15 to full text, 7 included, 8 excluded (S090 not retrievable); decisions approved by reviewer 2026-09-12. Reviewer decision: no further databases |
| 5 | Data extraction | Done for 7 studies (8 rows) plus quality.csv; verified by reviewer 2026-09-12 |
| 6 | Analysis in R | Done (analysis/run_analysis.R; outputs regenerated from extraction.csv); approved 2026-09-12 |
| 7 | Report | Version 1.0 (outputs/report.md); single database |
| 8 | Solutions list | Version 1.0 (outputs/solutions.md); lived-experience text drafted for reviewer amendment |
| 9 | Video script | Version 1.0 (video/script.md, 12 min, narrator over graphics); Scene 9 drafted for reviewer amendment |

## Repository layout

```
protocol/    protocol.md
search/      exported database records and search log
screening/   screening_log.csv
extraction/  extraction.csv (+ local, git-ignored PDFs)
analysis/    RStudio project, run_analysis.R
outputs/     tables/, figures/, report.md
video/       script.md
```

## Reproducing the analysis

Once step 6 is complete: open `analysis/` as an RStudio project and run
`run_analysis.R`. Every table and figure is regenerated from
`extraction/extraction.csv`.

## Audience

The report is for the global health community; the video is for a general worldwide audience across PYROS social media channels. Plain language, no jargon, no statistics on screen.

## Outputs

1. A research report with tables and figures, published on PYROS with its
   data (CSV) and R code.
2. A plain-language video for a global audience.
