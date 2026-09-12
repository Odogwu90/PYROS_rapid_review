"""Parse a PubMed MEDLINE-format export (Save -> Format: PubMed) into a CSV.

Usage:  python screening/parse_pubmed.py search/pubmed_2026-09-12.txt search/records_pubmed.csv

Each record starts with a 'PMID- ' line. Tags are 4 characters, then '- ',
then the value; continuation lines start with six spaces.
"""
import csv, sys, re

def parse(path):
    recs, cur, tag = [], None, None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            if re.match(r"^[A-Z]{1,4}\s*- ", line):
                tag, val = line[:4].strip(), line[6:]
                if tag == "PMID":
                    cur = {}
                    recs.append(cur)
                cur.setdefault(tag, []).append(val)
            elif line.startswith("      ") and cur is not None and tag:
                cur[tag][-1] += " " + line.strip()
    return recs

def year(rec):
    m = re.match(r"(\d{4})", rec.get("DP", [""])[0])
    return m.group(1) if m else ""

def main(src, dst):
    recs = parse(src)
    with open(dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["pmid", "title", "year", "journal", "pub_types", "language", "abstract"])
        for r in recs:
            w.writerow([
                r["PMID"][0],
                " ".join(r.get("TI", [""])),
                year(r),
                r.get("TA", [""])[0],
                "; ".join(r.get("PT", [])),
                r.get("LA", [""])[0],
                " ".join(r.get("AB", [""])),
            ])
    print(f"{len(recs)} records -> {dst}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
