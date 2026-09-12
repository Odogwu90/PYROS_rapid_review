# Do skilled professionals who migrate and restart their careers show more depressive symptoms than recent graduates who migrate before establishing a career? A rapid review.

A rapid literature review produced for **PYROS** (PyNexus research channel).

**Director and reviewer:** Dr. Okpara Onyedikachi Martins (MBBS, Nigeria; MSc Global Health, University of Bonn).
**Analytic and drafting support:** Claude (Anthropic), working under the rules in `CLAUDE.md`. All study selection, data verification and conclusions are made by Dr. Okpara.

## Status

| Step | Description | Status |
|------|-------------|--------|
| 1 | Protocol | Draft written, awaiting review |
| 2 | Project scaffold (folders, git, log templates) | Done |
| 3 | Search strings per database | Not started |
| 4 | Screening | Not started |
| 5 | Data extraction | Not started |
| 6 | Analysis in R | Not started |
| 7 | Report | Not started |
| 8 | Solutions list | Not started |
| 9 | Video script | Not started |

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

## Outputs

1. A research report with tables and figures, published on PYROS with its
   data (CSV) and R code.
2. A plain-language video for a global audience.
