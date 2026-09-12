# PYROS rapid review: depressive symptoms in skilled-professional vs recent-graduate migrants

Rapid literature review for PYROS (PyNexus research channel).
Director: Dr. Okpara Onyedikachi Martins (MBBS; MSc Global Health, Bonn).
Claude builds, drafts and codes. Dr. Okpara decides, verifies and approves.

## Non-negotiable rules

1. **No unverified sources.** No citation, study, statistic or quotation enters
   any file unless the source PDF or exported record exists in `search/` or
   `extraction/` and Dr. Okpara has confirmed it. Never invent, guess or
   "recall" references. If unsure a study exists, say so and leave a
   placeholder marked `TODO-VERIFY`.
2. **Terminology.** Use "depressive symptoms" (scale scores), not
   "depression", unless a study reports clinical diagnoses.
3. **Traceability.** Every number in a table or graph must trace to a row in
   `extraction/extraction.csv` with a `study_id`.
4. **Both directions.** Report evidence for and against the hypothesis. Do not
   shape the analysis toward the hypothesis.
5. **No database access.** Claude cannot access PubMed, PsycINFO or paywalled
   papers. Claude gives exact search strings; Dr. Okpara runs them and exports
   results and PDFs into the folders.
6. **Recommendations.** The report may only recommend what the included
   studies support. Lived-experience advice is added by Dr. Okpara and
   labelled as such.
7. **Ask first.** Ask before deleting or overwriting anything Dr. Okpara
   wrote. Stop at the end of each step and wait for approval. Do not skip
   ahead of approved steps.

## Folder structure

- `protocol/`   protocol.md (review question, criteria, search, analysis plan)
- `search/`     exported database records (.ris/.csv/.txt) and search logs
- `screening/`  screening_log.csv (one row per record, every decision logged)
- `extraction/` extraction.csv (one row per study x migrant group) and PDFs
- `analysis/`   RStudio project; run_analysis.R rebuilds every table/figure
- `outputs/`    tables/, figures/, report.md
- `video/`      script.md for the plain-language video

## Planned steps (each ends with approval)

1. Protocol draft.  2. Scaffold (folders, git, CSVs).  3. Search strings.
4. Screening.  5. Extraction.  6. R analysis.  7. Report.
8. Solutions list.  9. Video script.

## Conventions

- R: tidyverse style, native pipe `|>`, ggplot2, gt or flextable. Explain
  code line by line; Dr. Okpara is learning R.
- CSVs are the single source of truth. Never hand-edit numbers into outputs.
- `study_id` format: `S001`, `S002`, ... assigned at screening and reused
  everywhere.
- PDFs are kept locally in `extraction/pdf/` but are git-ignored (copyright).
  Exported bibliographic records are tracked.
- Dates in files are absolute (YYYY-MM-DD).
