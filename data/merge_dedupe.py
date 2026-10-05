"""Merge company exports from several providers (Apollo, Prospeo, Sales Nav, Clay...)
into one deduped account list with only: Company Name, Domain, Company LinkedIn URL.

Usage:
    python3 data/merge_dedupe.py data/raw/*.csv --limit 50 --out data/saffron_50_accounts.csv

Each input CSV may use its own column names; common variants are auto-detected.
Rows are deduped on the cleaned root domain. Rows from earlier files win, but blank
fields are filled from later duplicates. A per-row 'sources' column is written to a
separate audit file so you can see which providers found each company.
"""
import argparse
import csv
import re
import sys
from collections import OrderedDict
from pathlib import Path

NAME_COLS = ["company name", "company", "organization name", "account name", "name", "company_name"]
DOMAIN_COLS = ["domain", "company domain", "website", "company website", "website url", "company_domain", "url"]
COUNTRY_COLS = ["country", "company country", "hq country"]
US_NAMES = {"united states", "us", "usa", "united states of america"}
LINKEDIN_COLS = ["company linkedin url", "linkedin url", "company linkedin", "linkedin", "company_linkedin_url",
                 "linkedin company url", "company linkedin page"]

# Disqualifier keywords from the strategy doc (staffing/outsourcing sell engineers rather than hire them).
DISQUALIFY = re.compile(r"\b(staffing|outsourc|recruit(ing|ment) agency|consultancy|body ?shop)\b", re.I)


def pick(row, candidates):
    lowered = {k.strip().lower(): v for k, v in row.items() if k}
    for c in candidates:
        if lowered.get(c):
            return lowered[c].strip()
    return ""


def clean_domain(raw):
    d = raw.strip().lower()
    d = re.sub(r"^[a-z]+://", "", d)
    d = d.split("/")[0].split("?")[0].split("#")[0]
    d = re.sub(r"^www\d*\.", "", d)
    return d.strip(".")


def clean_linkedin(raw):
    u = raw.strip()
    if not u:
        return ""
    m = re.search(r"linkedin\.com/(company|school|showcase)/([^/?#]+)", u, re.I)
    return f"https://www.linkedin.com/company/{m.group(2).lower()}" if m else u


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--out", default="data/saffron_50_accounts.csv")
    ap.add_argument("--exclude", default="data/exclude.csv",
                    help="CSV with domain,reason: competitors, partners and manual disqualifications")
    args = ap.parse_args()

    excluded = {}
    if Path(args.exclude).exists():
        with open(args.exclude, newline="") as f:
            excluded = {clean_domain(r["domain"]): r["reason"] for r in csv.DictReader(f)}

    accounts = OrderedDict()
    stats = {"rows": 0, "no_domain": 0, "disqualified": 0, "excluded": 0, "non_us": 0, "dupes": 0}
    for path in args.inputs:
        src = Path(path).stem
        with open(path, newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                stats["rows"] += 1
                name = pick(row, NAME_COLS)
                domain = clean_domain(pick(row, DOMAIN_COLS))
                li = clean_linkedin(pick(row, LINKEDIN_COLS))
                if not domain:
                    stats["no_domain"] += 1
                    continue
                country = pick(row, COUNTRY_COLS).lower()
                if country and country not in US_NAMES:
                    stats["non_us"] += 1
                    continue
                if domain in excluded:
                    stats["excluded"] += 1
                    continue
                if DISQUALIFY.search(" ".join(str(v) for v in row.values() if v)):
                    stats["disqualified"] += 1
                    continue
                if domain in accounts:
                    stats["dupes"] += 1
                    a = accounts[domain]
                    a["Company Name"] = a["Company Name"] or name
                    a["Company LinkedIn URL"] = a["Company LinkedIn URL"] or li
                    a["sources"].add(src)
                else:
                    accounts[domain] = {"Company Name": name, "Domain": domain,
                                        "Company LinkedIn URL": li, "sources": {src}}

    # Prefer companies found by more providers (higher confidence), then original order.
    ranked = sorted(accounts.values(), key=lambda a: -len(a["sources"]))
    final = ranked[: args.limit]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Company Name", "Domain", "Company LinkedIn URL"])
        w.writeheader()
        for a in final:
            w.writerow({k: a[k] for k in w.fieldnames})
    with open(out.with_name(out.stem + "_audit.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Company Name", "Domain", "Company LinkedIn URL", "found_in", "n_sources"])
        for a in ranked:
            w.writerow([a["Company Name"], a["Domain"], a["Company LinkedIn URL"],
                        ";".join(sorted(a["sources"])), len(a["sources"])])

    missing_li = sum(1 for a in final if not a["Company LinkedIn URL"])
    print(f"input rows {stats['rows']} | unique domains {len(accounts)} | dupes merged {stats['dupes']} | "
          f"no domain {stats['no_domain']} | keyword-disqualified {stats['disqualified']} | excluded list {stats['excluded']} | non-US HQ {stats['non_us']}")
    print(f"wrote {len(final)} accounts -> {out}  (missing LinkedIn URL: {missing_li})")
    if len(final) < args.limit:
        print(f"WARNING: only {len(final)} accounts, short of {args.limit}", file=sys.stderr)


if __name__ == "__main__":
    main()
