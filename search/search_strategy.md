# Search strategy (step 3) — final strings to run

Date prepared: 2026-09-12. Protocol v0.2, section 7.
Run each search, then fill one row per search in `search_log.csv` and save
the export into this folder with the filename given in the log.

Three concepts, joined with AND:

| Concept | Idea |
|---------|------|
| A | International migrant |
| B | Skilled / professional / recent graduate / career restart (deskilling, credential recognition, overqualification) |
| C | Depressive symptoms |

Concept B is the widest. It includes profession names (nurse, physician,
engineer) because many relevant studies describe "internationally educated
nurses" or "international medical graduates" without ever using the word
"skilled".

Terms marked `CHECK` are ones I cannot verify from here (MeSH headings and
thesaurus descriptors). PubMed shows how it interpreted every term in the
**Search details** box on the results page; if a heading is not recognised
it will appear there as a plain-text search instead, which is harmless but
should be noted in the log.

---

## 1. PubMed

Interface: https://pubmed.ncbi.nlm.nih.gov/advanced/

### 1.1 How to run

1. Open Advanced search. Paste **each numbered line below** into the query
   box one at a time and click **Add to history**. This gives you a count
   per concept, which goes in the log.
2. In the History table, combine with the line numbers PubMed assigns:
   `#1 AND #2 AND #3` and add to history again.
3. On the final result page apply filters: **Humans** and
   **Publication date: Custom range 2000/01/01 to 2026/09/30**. Note the
   count after filters.
4. Export: **Save → Selection: All results → Format: CSV** →
   `pubmed_2026-09-12.csv`. Also **Send to → Citation manager** →
   `pubmed_2026-09-12.nbib` (the .nbib file keeps abstracts, the CSV does
   not; I need the .nbib for screening).
5. Copy the text in **Search details** into `pubmed_2026-09-12_details.txt`.

### 1.2 Lines

**Line 1 — migrant (concept A)**

```
"Emigrants and Immigrants"[Mesh] OR "Transients and Migrants"[Mesh] OR "Emigration and Immigration"[Mesh] OR "Foreign Medical Graduates"[Mesh] OR "Foreign Professional Personnel"[Mesh] OR migrant[tiab] OR migrants[tiab] OR immigrant[tiab] OR immigrants[tiab] OR emigrant[tiab] OR emigrants[tiab] OR "foreign-born"[tiab] OR "foreign born"[tiab] OR expatriate[tiab] OR expatriates[tiab] OR "internationally educated"[tiab] OR "internationally trained"[tiab] OR "international medical graduate"[tiab] OR "international medical graduates"[tiab] OR "overseas-trained"[tiab] OR "overseas trained"[tiab] OR "overseas qualified"[tiab] OR "foreign-trained"[tiab] OR "foreign trained"[tiab] OR "newcomer"[tiab] OR "newcomers"[tiab]
```

`CHECK` MeSH: "Foreign Medical Graduates" and "Foreign Professional
Personnel" — confirm in Search details that they mapped as headings.

**Line 2 — skilled / professional / graduate / career restart (concept B)**

```
skilled[tiab] OR "highly skilled"[tiab] OR "highly-skilled"[tiab] OR "high-skilled"[tiab] OR professional[tiab] OR professionals[tiab] OR physician[tiab] OR physicians[tiab] OR doctor[tiab] OR doctors[tiab] OR nurse[tiab] OR nurses[tiab] OR engineer[tiab] OR engineers[tiab] OR pharmacist[tiab] OR pharmacists[tiab] OR dentist[tiab] OR dentists[tiab] OR teacher[tiab] OR teachers[tiab] OR academic[tiab] OR academics[tiab] OR scientist[tiab] OR scientists[tiab] OR "recent graduate"[tiab] OR "recent graduates"[tiab] OR "new graduate"[tiab] OR "new graduates"[tiab] OR "early career"[tiab] OR "early-career"[tiab] OR "university graduate"[tiab] OR "university graduates"[tiab] OR "college graduate"[tiab] OR "college graduates"[tiab] OR deskilling[tiab] OR deskilled[tiab] OR "de-skilling"[tiab] OR "de-skilled"[tiab] OR overqualified[tiab] OR overqualification[tiab] OR "over-qualified"[tiab] OR "over-qualification"[tiab] OR "over-education"[tiab] OR overeducation[tiab] OR overeducated[tiab] OR "occupational downgrading"[tiab] OR "occupational mobility"[tiab] OR "downward mobility"[tiab] OR "status loss"[tiab] OR credential[tiab] OR credentials[tiab] OR credentialing[tiab] OR "brain waste"[tiab] OR underemployed[tiab] OR underemployment[tiab] OR "under-employed"[tiab] OR "under-employment"[tiab] OR licensure[tiab] OR licensing[tiab] OR relicensing[tiab] OR "re-licensing"[tiab] OR "qualification recognition"[tiab] OR "recognition of qualifications"[tiab] OR "foreign qualifications"[tiab] OR "career transition"[tiab] OR "career change"[tiab] OR "professional identity"[tiab] OR "tertiary educated"[tiab] OR "university educated"[tiab] OR "highly educated"[tiab]
```

**Line 3 — depressive symptoms (concept C)**

```
"Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depression[tiab] OR depressive[tiab] OR depressed[tiab] OR "PHQ-9"[tiab] OR "PHQ9"[tiab] OR "Patient Health Questionnaire"[tiab] OR "CES-D"[tiab] OR "CESD"[tiab] OR "Center for Epidemiologic Studies Depression"[tiab] OR "HADS"[tiab] OR "Hospital Anxiety and Depression"[tiab] OR "Beck Depression"[tiab] OR "BDI"[tiab] OR "DASS"[tiab] OR "DASS-21"[tiab] OR "K10"[tiab] OR "K6"[tiab] OR "Kessler"[tiab] OR "GHQ"[tiab] OR "General Health Questionnaire"[tiab] OR "HSCL"[tiab] OR "Hopkins Symptom Checklist"[tiab] OR "psychological distress"[tiab] OR "mental distress"[tiab] OR "common mental disorder"[tiab] OR "common mental disorders"[tiab]
```

**Line 4 — combine**

```
#1 AND #2 AND #3
```

then filters Humans; 2000/01/01–2026/09/30.

### 1.3 If line 4 is too large

If line 4 exceeds roughly 3,000 records after filters, a rapid review
cannot screen it. Run this narrower **line 5** instead and log both counts:

```
#1 AND #3 AND (skilled[tiab] OR "highly skilled"[tiab] OR "internationally educated"[tiab] OR "international medical graduate"[tiab] OR "international medical graduates"[tiab] OR deskilling[tiab] OR deskilled[tiab] OR overqualified[tiab] OR overqualification[tiab] OR overeducation[tiab] OR "occupational downgrading"[tiab] OR "downward mobility"[tiab] OR credential[tiab] OR credentials[tiab] OR "brain waste"[tiab] OR underemployed[tiab] OR underemployment[tiab] OR licensure[tiab] OR "qualification recognition"[tiab] OR "recent graduate"[tiab] OR "recent graduates"[tiab] OR "new graduate"[tiab] OR "new graduates"[tiab] OR "early career"[tiab] OR "professional identity"[tiab])
```

Decision on which set to screen is yours; record it in the log `notes`.

---

## 2. PsycINFO

Protocol section 15 left the interface open (Ovid or EBSCO). Both versions
are given. Use whichever your Bonn library login provides and log which.

### 2.1 Ovid syntax

Enter each line in **Advanced Search → Multi-Field** or, simpler, switch to
the **command line** box (Advanced → "Search Fields" is not needed; paste
the whole line). `.ti,ab.` searches title and abstract; `/` marks a
thesaurus subject heading; `exp` explodes it to narrower terms; `adj3`
means within three words.

```
1  exp Immigration/ OR exp Human Migration/ OR (migrant* OR immigrant* OR emigrant* OR foreign-born OR "foreign born" OR expatriate* OR "internationally educated" OR "internationally trained" OR "international medical graduate*" OR "overseas trained" OR "overseas qualified" OR "foreign trained" OR newcomer*).ti,ab.
2  exp Occupational Status/ OR exp Underemployment/ OR exp Professional Personnel/ OR (skilled OR "highly skilled" OR professional* OR physician* OR doctor* OR nurse* OR engineer* OR pharmacist* OR dentist* OR teacher* OR academic* OR scientist* OR "recent graduate*" OR "new graduate*" OR "early career" OR "university graduate*" OR "college graduate*" OR deskill* OR "de-skill*" OR overqualif* OR "over-qualif*" OR overeducat* OR "over-educat*" OR "occupational downgrad*" OR "downward mobility" OR "status loss" OR credential* OR "brain waste" OR underemploy* OR "under-employ*" OR licens* OR relicens* OR "qualification recognition" OR "recognition of qualifications" OR "foreign qualifications" OR "career transition" OR "career change" OR "professional identity" OR "highly educated" OR "tertiary educated").ti,ab.
3  exp Major Depression/ OR exp "Depression (Emotion)"/ OR (depress* OR PHQ-9 OR PHQ9 OR "Patient Health Questionnaire" OR CES-D OR CESD OR "Center for Epidemiologic Studies Depression" OR HADS OR "Hospital Anxiety and Depression" OR "Beck Depression" OR BDI OR DASS OR DASS-21 OR K10 OR K6 OR Kessler OR GHQ OR "General Health Questionnaire" OR HSCL OR "Hopkins Symptom Checklist" OR "psychological distress" OR "mental distress" OR "common mental disorder*").ti,ab.
4  1 AND 2 AND 3
5  limit 4 to (yr="2000 - 2026" and "adulthood <18+ years>")
```

`CHECK` thesaurus headings: Immigration, Human Migration, Occupational
Status, Underemployment, Professional Personnel, Major Depression,
Depression (Emotion). Type each into **Search Tools → Map Term** first; if
a heading does not exist, delete that `exp .../` fragment and note it in
the log. The free-text part of each line stands on its own.

Export: select all → **Export → Format: RIS** (with abstracts) →
`psycinfo_2026-09-12.ris`. Also save the search history as a text file
(`psycinfo_2026-09-12_history.txt`).

### 2.2 EBSCOhost syntax

Advanced Search, one line per search box or paste into one box. `TI` =
title, `AB` = abstract, `DE` = exact subject heading, `*` truncates,
`N3` = within three words.

```
S1  DE "Immigration" OR DE "Human Migration" OR TI (migrant* OR immigrant* OR emigrant* OR "foreign-born" OR "foreign born" OR expatriate* OR "internationally educated" OR "internationally trained" OR "international medical graduate*" OR "overseas trained" OR "overseas qualified" OR "foreign trained" OR newcomer*) OR AB (migrant* OR immigrant* OR emigrant* OR "foreign-born" OR "foreign born" OR expatriate* OR "internationally educated" OR "internationally trained" OR "international medical graduate*" OR "overseas trained" OR "overseas qualified" OR "foreign trained" OR newcomer*)
S2  DE "Occupational Status" OR DE "Underemployment" OR DE "Professional Personnel" OR TI (skilled OR "highly skilled" OR professional* OR physician* OR doctor* OR nurse* OR engineer* OR pharmacist* OR dentist* OR teacher* OR academic* OR scientist* OR "recent graduate*" OR "new graduate*" OR "early career" OR "university graduate*" OR "college graduate*" OR deskill* OR "de-skill*" OR overqualif* OR "over-qualif*" OR overeducat* OR "occupational downgrad*" OR "downward mobility" OR "status loss" OR credential* OR "brain waste" OR underemploy* OR "under-employ*" OR licens* OR relicens* OR "qualification recognition" OR "recognition of qualifications" OR "foreign qualifications" OR "career transition" OR "career change" OR "professional identity" OR "highly educated" OR "tertiary educated") OR AB (skilled OR "highly skilled" OR professional* OR physician* OR doctor* OR nurse* OR engineer* OR pharmacist* OR dentist* OR teacher* OR academic* OR scientist* OR "recent graduate*" OR "new graduate*" OR "early career" OR "university graduate*" OR "college graduate*" OR deskill* OR "de-skill*" OR overqualif* OR "over-qualif*" OR overeducat* OR "occupational downgrad*" OR "downward mobility" OR "status loss" OR credential* OR "brain waste" OR underemploy* OR "under-employ*" OR licens* OR relicens* OR "qualification recognition" OR "recognition of qualifications" OR "foreign qualifications" OR "career transition" OR "career change" OR "professional identity" OR "highly educated" OR "tertiary educated")
S3  DE "Major Depression" OR DE "Depression (Emotion)" OR TI (depress* OR "PHQ-9" OR PHQ9 OR "Patient Health Questionnaire" OR "CES-D" OR CESD OR HADS OR "Hospital Anxiety and Depression" OR "Beck Depression" OR BDI OR DASS OR K10 OR K6 OR Kessler OR GHQ OR "General Health Questionnaire" OR HSCL OR "Hopkins Symptom Checklist" OR "psychological distress" OR "mental distress" OR "common mental disorder*") OR AB (depress* OR "PHQ-9" OR PHQ9 OR "Patient Health Questionnaire" OR "CES-D" OR CESD OR HADS OR "Hospital Anxiety and Depression" OR "Beck Depression" OR BDI OR DASS OR K10 OR K6 OR Kessler OR GHQ OR "General Health Questionnaire" OR HSCL OR "Hopkins Symptom Checklist" OR "psychological distress" OR "mental distress" OR "common mental disorder*")
S4  S1 AND S2 AND S3
Limiters: Published Date 20000101–20260930; Age Group: Adulthood (18 yrs & older)
```

Same `CHECK` on the `DE` headings (use the **Thesaurus** link at the top).
Export: **Share → Export results → RIS** → `psycinfo_2026-09-12.ris`.

---

## 3. Google Scholar

Scholar has no export and no field tags, so it is used as a supplementary
source. Run each string below **separately**, sorted by relevance, with
**custom range 2000–2026**, and record the first **200 results** per
string (protocol section 6).

Two ways to capture results:

- **Publish or Perish** (free desktop tool by Harzing; Google Scholar
  source; max results 200 per query; **Save results as CSV**). Filename:
  `scholar_Q1_2026-09-12.csv`, `scholar_Q2_...` and so on.
- Or the **Zotero** browser connector, saving each page of results into a
  collection named `scholar_Qn`, then export the collection as RIS.

Strings:

```
Q1  "skilled migrants" OR "skilled immigrants" "depressive symptoms" deskilling OR overqualification OR underemployment
Q2  "internationally educated nurses" depression OR "depressive symptoms" OR "psychological distress"
Q3  "international medical graduates" depression OR "depressive symptoms" OR "psychological distress"
Q4  immigrants "credential recognition" OR "foreign credentials" OR "qualification recognition" depression OR "mental health"
Q5  "recent graduates" OR "new graduates" migration OR migrants OR immigrants "depressive symptoms"
Q6  immigrants overqualification OR overeducation OR "downward mobility" depression OR "depressive symptoms"
Q7  "brain waste" immigrants "mental health" OR depression
Q8  expatriates OR "self-initiated expatriates" "early career" "depressive symptoms" OR "psychological distress"
```

Scholar counts are approximate and change daily; log the number shown on
the first page and the number actually saved.

---

## 4. Grey literature

Record each source searched in the log even when it returns nothing.
Save any candidate document's citation (title, organisation, year, URL,
access date) in `grey_2026-09-12.csv` with these columns:
`title,organisation,year,url,access_date,search_string,notes`.
PDFs go into `../extraction/pdf/` (they are git-ignored).

| Source | How | Strings |
|--------|-----|---------|
| WHO (who.int, incl. IRIS repository iris.who.int) | Site search and IRIS search | `migrant health workers mental health`; `international migration health personnel wellbeing` |
| IOM (iom.int, publications.iom.int) | Publications search | `skilled migration mental health`; `migrant mental health deskilling` |
| OECD (oecd.org, oecd-ilibrary.org) | iLibrary search | `overqualification immigrants`; `migrant skills mismatch well-being` |
| ILO (ilo.org) | Site search | `skilled migrant workers mental health`; `brain waste` |
| ProQuest Dissertations & Theses (via Bonn library) | Advanced search, abstract field | `(immigrant* OR migrant*) AND (skilled OR professional* OR credential* OR deskill*) AND (depress* OR "psychological distress")` |
| medRxiv / PsyArXiv / SSRN | Site search | `skilled migrants depressive symptoms`; `immigrant overqualification depression` |
| Google (plain) | 8 site-restricted searches, first 5 pages each | `site:who.int skilled migrant mental health`; `site:iom.int skilled migration depression`; `site:oecd.org overqualification immigrants mental health`; `site:ilo.org migrant professionals mental health` |
| Professional-body reports | Google | `internationally educated nurses survey mental health report`; `international medical graduates wellbeing survey report` |

---

## 5. Citation chasing (after full-text screening)

For every study marked `include` at stage 2:

1. I read the PDF reference list and list candidate titles for you.
2. You run a **"Cited by"** search in Google Scholar for each included
   study and save the first 100 results (`citedby_S###_2026-xx-xx.csv`).
3. New records enter `screening_log.csv` with `source = citation`.

---

## 6. What to send back

Put these in `search/` and I will deduplicate and assign study IDs:

- `pubmed_2026-09-12.nbib`, `pubmed_2026-09-12.csv`, `pubmed_2026-09-12_details.txt`
- `psycinfo_2026-09-12.ris`, `psycinfo_2026-09-12_history.txt`
- `scholar_Q1..Q8_2026-09-12.csv` (or RIS)
- `grey_2026-09-12.csv`
- `search_log.csv` with one row per search run

Change the date in filenames to the day you actually run the searches and
use the same date in the log.
