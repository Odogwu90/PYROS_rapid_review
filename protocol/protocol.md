# Protocol: Do skilled professionals who migrate and restart their careers show more depressive symptoms than recent graduates who migrate before establishing a career? A rapid review.

| Field | Value |
|-------|-------|
| Version | 0.2 (approved 2026-09-12; decisions in section 15 adopted as proposed) |
| Date | 2026-09-12 |
| Reviewer / director | Dr. Okpara Onyedikachi Martins (MBBS; MSc Global Health, Bonn) |
| Support | Claude (Anthropic): drafting, screening assistance, extraction proposals, R code. All decisions by the reviewer. |
| Channel | PYROS (PyNexus research channel) |
| Registration | Not registered (rapid review). Protocol is published with the report. |

Items marked `DECISION` need the reviewer's choice before the step is run.
Items marked `TODO-VERIFY` need a confirmed source before they may be cited.

---

## 1. Background and rationale

Skilled migrants often cannot practise their original profession in the
destination country. Foreign qualifications may not be recognised, licensing
can take years, and many take jobs below their training level. This is
usually described as deskilling, overqualification, brain waste or
occupational downgrading. The rationale for this review is that a
professional who has already built a career, identity and income, and then
loses them on migration, may be at greater risk of depressive symptoms than
a recent graduate who migrates before those things exist and who may see
migration as the start of a career rather than an interruption.

The background section of the final report will need sourced statements on:
(a) the size of skilled migration flows, (b) rates of deskilling among
skilled migrants, (c) the general association between migration and
depressive symptoms, and (d) the role of occupational status in mental
health. Each is `TODO-VERIFY` until a confirmed source is in `search/`.

## 2. Review question

**Primary question.** Among adult international migrants with tertiary
qualifications, do those who migrated as established professionals and had
to restart their careers show higher levels of depressive symptoms than
those who migrated as recent graduates before establishing a career?

**Secondary questions.**

1. What is the prevalence, or mean scale score, of depressive symptoms in
   each migrant type?
2. Which explanatory factors do studies name for depressive symptoms in
   skilled migrants (for example credential non-recognition, loss of
   occupational status, income drop, discrimination, language, social
   support, length of stay)?
3. Which factors are linked to better outcomes, and what interventions or
   supports do studies report?

### 2.1 Framework (PECO)

| Element | Definition |
|---------|-----------|
| Population | Adults (18+) who migrated internationally and hold a tertiary (university or equivalent professional) qualification. |
| Exposure | Migrated as an **established professional**: had worked in their qualified field for a minimum period before migration (proposed: 2+ years; `DECISION`) and/or is described by the study as experiencing career restart, deskilling, credential non-recognition, re-licensing or occupational downgrading. |
| Comparator | Migrated as a **recent graduate**: completed the qualifying degree within a short period before migration (proposed: 2 years or less; `DECISION`) with no established career in the field; includes graduates who migrate to begin work or postgraduate training. |
| Outcome | Depressive symptoms measured by any validated self-report scale (for example PHQ-9, CES-D, HADS-D, BDI, K10 depressive items, DASS-21 depression subscale, GHQ depressive items, HSCL-25) reported as prevalence above a cut-off, mean score, or an effect estimate. Clinical diagnoses (interview or records) are also eligible and are reported separately as "depression". |
| Study designs | Quantitative observational studies (cross-sectional, cohort, case-control), intervention studies reporting depressive symptoms, and mixed-methods studies with a quantitative component. Qualitative studies are eligible **only** for secondary questions 2 and 3 (explanatory factors) and are tabulated separately. |

## 3. Hypothesis

**H1 (directional).** Established-professional migrants have higher
depressive-symptom scores or prevalence than recent-graduate migrants.

**H0.** No difference, or the reverse.

Under rule 4 the review reports all three possible findings for every
eligible comparison: supports H1, contradicts H1 (recent graduates worse),
or no difference. The synthesis tallies each direction.

## 4. Operational definitions

| Term | Definition used in this review |
|------|--------------------------------|
| International migrant | Person living in a country other than their country of birth or citizenship, regardless of legal status, for any reason including work, study, family or asylum. |
| Skilled / professional migrant | Migrant holding a tertiary qualification or a regulated professional licence (for example medicine, nursing, engineering, law, teaching, accounting, IT). |
| Established professional | Skilled migrant with 2+ years of post-qualification work in the field before migration (`DECISION` on threshold). Where a study does not report years of experience, "established" is inferred if the study describes participants as practising professionals before migration (for example "internationally educated nurses who worked as nurses in their home country"). Inference is recorded in `notes`. |
| Recent graduate | Skilled migrant who migrated within 2 years of completing the qualifying degree (`DECISION` on threshold) and had not established a career in the field. Includes migrants who completed the degree in the origin country and migrated for a first job or postgraduate training. `DECISION`: whether migrants who completed the degree **in the destination country** (former international students) count as recent-graduate migrants. Proposed: include, flagged in `notes` as "destination-educated". |
| Career restart | Any of: retraining, re-licensing, credential assessment, working outside the field, working below qualification level, prolonged unemployment attributable to non-recognition. |
| Depressive symptoms | Score on a validated depressive-symptom scale. "Depression" is used only where a study reports a clinical diagnosis. |
| Migrant type (extraction code) | `professional`, `recent_graduate`, or `mixed` (sample contains both and does not separate them). |

## 5. Eligibility criteria

### 5.1 Inclusion

1. Adults aged 18 or over.
2. International migrants (see definition) with tertiary qualifications, or
   a study in which such migrants are a reported subgroup.
3. Reports depressive symptoms with a validated scale, or clinical
   depression diagnoses, for at least one of the two migrant types, or
   compares them.
4. Quantitative or mixed-methods design (any); qualitative for secondary
   questions only.
5. Any destination and origin country.
6. Published 2000-01-01 to search date (`DECISION`; rationale: recent
   licensing and migration regimes).
7. Peer-reviewed articles, theses, and grey literature (reports from
   international agencies, professional bodies, government).
8. Language: English; plus any other language the reviewer can read
   (`DECISION`: list languages).

### 5.2 Exclusion

1. Internal (within-country) migrants only.
2. Second-generation migrants (born in the destination country) only.
3. Current international students who have not yet graduated, unless
   reported as a comparison group alongside graduates or professionals.
4. Samples defined solely by forced migration (refugees, asylum seekers)
   **without** any measure of prior professional status (`DECISION`;
   proposed rationale: distinct exposure profile. Skilled refugees whose
   pre-migration profession is reported remain eligible).
5. No validated depressive-symptom measure (for example single unvalidated
   item, general "stress" only).
6. Reviews, editorials, commentaries, protocols (reference lists are
   screened for eligible primary studies).
7. Conference abstracts without retrievable data.
8. Studies of return migrants only.

## 6. Information sources

| Source | Type | Who runs it | Export format into `search/` |
|--------|------|-------------|-----------------------------|
| PubMed | Database | Reviewer | .csv or .nbib, plus a text file of the query and result count |
| PsycINFO (via Ovid or EBSCO, `DECISION`) | Database | Reviewer | .ris or .csv |
| Google Scholar | Database | Reviewer | First 200 results per string, exported via Publish or Perish or copied to .csv (`DECISION`) |
| Grey literature | WHO, IOM, OECD, ILO, national health-workforce bodies, ProQuest Dissertations, medRxiv, PsyArXiv, SSRN | Reviewer, guided by Claude's search terms | .csv list with URL and access date |
| Citation chasing | Reference lists and forward citations of every included study | Reviewer with Claude's help on reference lists in PDFs | Appended to `screening_log.csv` with `source = citation` |

Every search is logged in `search/search_log.csv` (date, database,
string, filters, number of results, export filename). Claude creates this
file in step 3.

## 7. Search strategy (draft; finalised in step 3)

Three concepts joined by AND: (A) migrant, (B) skilled / professional /
graduate / deskilling, (C) depressive symptoms.

### 7.1 PubMed (draft)

```
(("Emigrants and Immigrants"[Mesh] OR "Transients and Migrants"[Mesh]
  OR migrant*[tiab] OR immigrant*[tiab] OR emigrant*[tiab]
  OR "foreign-born"[tiab] OR "foreign born"[tiab] OR expatriate*[tiab]
  OR "internationally educated"[tiab] OR "international medical graduate*"[tiab]
  OR "overseas-trained"[tiab] OR "overseas trained"[tiab])
AND
 (skilled[tiab] OR "highly skilled"[tiab] OR professional*[tiab]
  OR physician*[tiab] OR doctor*[tiab] OR nurse*[tiab] OR engineer*[tiab]
  OR "recent graduate*"[tiab] OR "new graduate*"[tiab] OR graduate*[tiab]
  OR deskill*[tiab] OR "de-skill*"[tiab] OR overqualif*[tiab]
  OR "over-qualif*"[tiab] OR "occupational downgrad*"[tiab]
  OR credential*[tiab] OR "brain waste"[tiab] OR underemploy*[tiab]
  OR "career"[tiab] OR licens*[tiab] OR "qualification recognition"[tiab])
AND
 ("Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depress*[tiab]
  OR "PHQ-9"[tiab] OR "PHQ9"[tiab] OR "CES-D"[tiab] OR "HADS"[tiab]
  OR "Beck Depression"[tiab] OR "psychological distress"[tiab]
  OR "mental health"[tiab]))
Filters: Humans; 2000/01/01 to present.
```

### 7.2 PsycINFO (draft, free-text form)

Controlled-vocabulary terms (thesaurus descriptors for immigration,
occupational status and depression) are `TODO-VERIFY` against the live
thesaurus in the interface the reviewer uses.

```
(migrant* OR immigrant* OR emigrant* OR "foreign-born" OR expatriate*
 OR "internationally educated" OR "overseas trained")
AND
(skilled OR professional* OR physician* OR nurse* OR engineer* OR graduate*
 OR deskill* OR overqualif* OR "occupational downgrad*" OR credential*
 OR "brain waste" OR underemploy* OR career OR licens*)
AND
(depress* OR "depressive symptoms" OR PHQ-9 OR CES-D OR HADS
 OR "psychological distress")
Limits: adulthood (18+); 2000 to present.
```

### 7.3 Google Scholar (draft; run each separately, first 200 results)

```
"skilled migrants" depressive symptoms deskilling
"internationally educated nurses" depression
"international medical graduates" depressive symptoms
"recent graduates" migration depressive symptoms
overqualification immigrants depression
```

### 7.4 Grey literature terms

`skilled migrant mental health report`, `deskilling immigrants wellbeing`,
`brain waste health workers survey`, combined with site restrictions for
who.int, iom.int, oecd.org, ilo.org.

## 8. Study selection (screening)

1. Records are exported into `search/`; Claude deduplicates them (exact and
   fuzzy title match) and assigns `study_id` (S001, S002, ...).
2. **Stage 1, title and abstract.** Claude proposes include / exclude /
   unsure with a one-line reason against section 5. The reviewer makes
   every final decision. Unsure goes to stage 2.
3. **Stage 2, full text.** The reviewer supplies the PDF into
   `extraction/pdf/`. Claude proposes a decision with the criterion number
   that applies. The reviewer decides.
4. Every decision is logged in `screening/screening_log.csv`:

| Column | Values |
|--------|--------|
| study_id | S### |
| title | as exported |
| year | YYYY |
| source | pubmed / psycinfo / scholar / grey / citation |
| stage | title_abstract / full_text |
| decision | include / exclude / unsure |
| exclusion_reason | criterion number from section 5.2 plus short text, blank if included |

5. Counts at each stage are reported in a PRISMA-style flow diagram.
6. Single-reviewer screening with AI assistance is a stated limitation
   (section 12).

## 9. Data extraction

One row per study **per migrant group** for which an estimate is reported,
so a study that reports both groups contributes two rows sharing a
`study_id`; a study reporting only a mixed sample contributes one row with
`migrant_type = mixed`. Claude proposes each row from the PDF; the reviewer
verifies every value against the PDF page before the row is accepted (rules
1 and 3). Unverifiable values stay blank, never guessed.

| Column | Definition |
|--------|-----------|
| study_id | S### from the screening log |
| authors | First author surname et al. |
| year | Publication year |
| country | Destination country (origin countries in `notes`) |
| design | cross_sectional / cohort / case_control / intervention / mixed_methods / qualitative |
| sample_size | n analysed for this row's group |
| migrant_type | professional / recent_graduate / mixed |
| measure | Scale name and cut-off, e.g. `PHQ-9 >=10` |
| prevalence | Percent above cut-off, as reported |
| mean_score | Mean (SD in `notes`) |
| effect_estimate | OR / RR / mean difference / beta for professional vs recent graduate (or vs reference stated in `notes`), with type in `notes` |
| ci_low, ci_high | 95% CI bounds |
| factors_named | Semicolon-separated list from a controlled list (section 9.1) |
| notes | Everything else: page numbers, adjustment set, inferred classification, direction of effect |

### 9.1 Controlled factor list (extended as studies are read; additions logged)

credential_non_recognition; occupational_downgrading; unemployment;
income_loss; loss_of_status_identity; discrimination; language_barrier;
social_isolation; family_separation; social_support (protective);
length_of_stay; legal_status_insecurity; workplace_stress; age_at_migration;
prior_mental_health; sense_of_coherence_or_resilience (protective);
recognition_or_bridging_programme (protective); mentoring (protective); intention_to_return (added 2026-09-12 from S058, approved).

## 10. Quality appraisal

Rapid-review level appraisal only: for each quantitative study the reviewer
records, in `extraction/quality.csv` (created in step 5), yes / no /
unclear for: (1) sampling method described and representative of the
target group, (2) validated depressive-symptom measure, (3) migrant type
defined clearly enough to classify, (4) response rate reported and 50% or
higher, (5) adjustment for at least age, sex and length of stay in any
comparative estimate. A formal appraisal tool is not applied; if one is
named in the report it is `TODO-VERIFY`.

## 11. Synthesis and analysis plan

All analysis is in R (`analysis/run_analysis.R`, tidyverse, ggplot2, gt or
flextable) and reads only `extraction/extraction.csv` and
`extraction/quality.csv`. Narrative synthesis; **no meta-analysis unless**
3 or more studies report the same comparison with the same outcome type,
in which case a random-effects model may be added after reviewer approval
(`DECISION` at step 6).

| Output | Content | Source columns |
|--------|---------|----------------|
| Table 1 | Study characteristics: id, authors, year, country, design, n, migrant type, measure, quality flags | all except results |
| Table 2 | Findings by migrant type: prevalence, mean score, effect estimate and CI, direction relative to H1 | prevalence, mean_score, effect_estimate, ci_low, ci_high |
| Figure 1 | Prevalence of depressive symptoms by migrant type; one point per study row, grouped by scale and cut-off; scales are not merged | prevalence, migrant_type, measure |
| Figure 2 | Forest-style plot of effect estimates with 95% CI (professional vs recent graduate, or vs stated reference) with a null line; no pooled diamond unless meta-analysis approved | effect_estimate, ci_low, ci_high |
| Figure 3 | Frequency of explanatory factors named across studies, split by whether the study found them risk-increasing or protective | factors_named |
| Direction tally | Count of comparative studies: supports H1 / contradicts H1 / no difference | notes (direction) |

Handling heterogeneity of scales: prevalence is reported only within the
scale and cut-off used; where a study uses a non-standard cut-off it is
plotted with a distinct shape and noted. Mean scores are never compared
across different scales.

## 12. Limitations of a rapid review (to be stated in the report)

- Single reviewer for screening and extraction, with AI assistance rather
  than a second human reviewer; risk of selection and extraction error.
- Limited databases (PubMed, PsycINFO, Google Scholar) and limited
  languages; risk of missing studies, especially from non-English regions.
- No contact with study authors for missing data.
- "Established professional" and "recent graduate" are rarely reported as
  study groups; classification will often be inferred from sample
  descriptions and is recorded as such.
- Brief quality appraisal rather than a full risk-of-bias tool.
- Heterogeneous scales and cut-offs prevent pooling; findings are
  descriptive.
- Rapid timeline; no protocol registration.

## 13. Roles and safeguards

| Task | Reviewer (Dr. Okpara) | Claude |
|------|-----------------------|--------|
| Protocol | Decides, approves | Drafts |
| Searches | Runs, exports | Writes strings, logs |
| Screening | Final decision on every record | Proposes decision and reason |
| Extraction | Verifies every value against the PDF | Proposes rows |
| Analysis | Approves code and outputs | Writes and explains R code |
| Report | Approves; adds lived-experience content, labelled | Drafts from CSVs only |
| Video | Approves, presents | Drafts script |

## 14. Outputs and dissemination

1. Research report (`outputs/report.md`) with Tables 1-2, Figures 1-3,
   PRISMA-style flow, reference list limited to verified sources, plus
   `extraction.csv`, `screening_log.csv` and `run_analysis.R`, published
   on PYROS.
2. Plain-language video script (`video/script.md`), 8-12 minutes.

## 15. Decisions requested from the reviewer before step 3

**Status 2026-09-12:** protocol v0.1 approved by the reviewer ("go ahead")
with no changes requested. The proposed values below are therefore adopted
as the working defaults. Any later change is logged here with its date.

1. Years-of-experience threshold for "established professional" (proposed 2+).
2. Time-since-graduation threshold for "recent graduate" (proposed 2 or less).
3. Whether destination-educated graduates (former international students) count as recent-graduate migrants (proposed: yes, flagged).
4. Whether to exclude forced-migrant-only samples without prior-profession data (proposed: yes).
5. Publication date range (proposed 2000 to present).
6. Languages beyond English.
7. Which PsycINFO interface (Ovid or EBSCO) and whether Google Scholar exports go through Publish or Perish.
8. Whether a random-effects pooled estimate is permitted if 3 or more comparable studies exist.
