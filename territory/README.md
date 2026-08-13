# Territory

**Status as of 2026-08-13:** territory list not yet received. This directory is the
landing zone for it.

## What lives here

- `zip-codes.md` — the assigned California zip codes that define the boundary
- `territory-list.xlsx` / `.csv` — the raw list as delivered, unmodified
- `territory-scoped.md` — the post-scope-check working list (in-book vs routed out)

Keep the raw delivered file untouched. All filtering and tiering happens in derived
files so the original stays auditable.

## Fields worth having

If the list is thin, these are the fields that make the scope check and tiering pass
possible. Anything missing has to be researched per account, which is slow, so it is
worth asking for them up front.

**For the scope check (Section 2 of CLAUDE.md):**

- Account name
- Billing/HQ city, state, zip
- Annual revenue
- Parent company / ultimate parent (the single most important field, since the
  conglomerate test depends on it)
- Industry / SIC / NAICS (drives the credit union, casino/tribal, and SLED exclusions)

**For tiering (Section 3 of CLAUDE.md):**

- Membership status and any lapse date
- Open or historical opportunities
- Last activity date and last meeting date
- Prior rep or owner
- Named contacts with titles
- Marketing engagement signals (downloads, webinars, events, pricing wizard)

## Ingestion steps once the list arrives

1. Drop the raw file in this directory unmodified.
2. Run the scope check across every row. Bucket into: **in-book**,
   **routed-out** (with the receiving rep named), and **needs-ownership-check**.
3. Produce `territory-scoped.md` with those three buckets and the count in each.
4. Tier the in-book accounts into T1/T2/T3 with a one-line reason each.
5. Write the assigned zip codes into `zip-codes.md` so the boundary is explicit and
   future accounts can be checked against it without re-reading the sheet.

`.xlsb` files: read with `pyxlsb`, or convert via LibreOffice headless to `.xlsx`
and use `openpyxl`. Per the playbook, Section 15.
