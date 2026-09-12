# search/

- `search_strategy.md` : final strings and export instructions per database (step 3).
- `search_log.csv`     : one row per search run. Columns: date (YYYY-MM-DD), database (pubmed / psycinfo / scholar / grey / citation), interface (e.g. pubmed.gov, ovid, ebsco, publish_or_perish, iris), string_id (Line 4, Line 5, S4, Q1..Q8, or source name for grey), filters (as applied), n_results (count after filters), export_file (filename saved here), notes (e.g. headings that did not map, decisions).
- Exported records (.nbib, .ris, .csv) and search-details text files are saved here and tracked in git.
- PDFs never go here; they go to `../extraction/pdf/` (git-ignored).
