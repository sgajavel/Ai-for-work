# Building the territory report in Salesforce

The territory export was itself a Salesforce report, so its column headers are field
labels. That means the whole book can be pulled with one filter and no imported list.

**Verify the field labels in the report builder before relying on them.** They are
inferred from the export headers, which is usually right but not guaranteed.

---

## The one filter that matters

Every account in the book carries a **`Package Territories F27`** field. All 699 rows
contain the same substring:

```
SMB 35: California 4
```

So the entire filter is:

> **Package Territories F27** `contains` **SMB 35: California 4**

That is it. No account ID list, no name matching, no geography.

### Why `contains` and not `equals`

The field holds two different shapes. 680 accounts read:

```
IT Acquire | SMB 35: California 4 | Sairam Gajavelli | FY27
```

The 19 accounts held to February 1 read:

```
IT Acquire | SMB 35: California 4 | With <rep> (IT Acquire) until Feb 1, 2027 | Moves to Sairam Gajavelli (IT Acquire) | FY27
```

Filtering on `equals` returns 680 and silently drops the 19 holdovers, which are exactly
the accounts worth watching. `contains` catches both. It also survives a name spelling
change and does not care which rep is named in the holdover text.

---

## Report setup

**Report type:** Accounts. Add Contacts later as a separate report, since Accounts and
Contacts in one report type hides accounts that have no contacts, and most of the book
has none.

**Filters**

| # | Field | Operator | Value |
|---|---|---|---|
| 1 | Package Territories F27 | contains | `SMB 35: California 4` |
| 2 | Is Viable IT | equals | `Viable` |

Filter 2 matches the review guidance to work from the viable list. Remove it when you
need the full picture. Expect roughly 608 rows with it on, 699 with it off.

Set the scope selector to **All Accounts**, not My Accounts. Before August 24 these
records still belong to their current owners, so My Accounts returns almost nothing.

**Columns worth adding**

- Account Name, Account Group IT, ITRG Status
- Is Viable IT, Billing State/Province, Billing City, Billing Zip/Postal Code
- Account Owner, Package Territories F27
- Company LinkedIn URL
- Annual Revenue, Employees, Industry, NAICS

The last two groups are the point. **Billing City and Billing Zip were not in the export
and are the fastest route to the zip question.** Annual Revenue is what makes the
$50-500M band checkable, which is currently impossible from the export alone.

**Grouping:** group by Billing City to see the geographic shape of the territory, or by
ITRG Status to isolate the 38 winbacks.

---

## Saved variants worth having

| Report | Filters | Use |
|---|---|---|
| **My F27 book, viable** | contains `SMB 35: California 4` + Is Viable IT = Viable | The working list |
| **Feb 1 holdovers** | contains `SMB 35: California 4` + contains `until Feb 1, 2027` | The 19 accounts not yet workable, and the ones feedback was filed on |
| **Winbacks** | working list + ITRG Status = Winback | 30 viable winbacks, the only Tier 1 population with a reason to be called now |
| **Arriving Aug 24** | contains `SMB 35: California 4` + does not contain `until Feb 1` | What is live on day one |
| **Zip audit** | working list, grouped by Billing Zip/Postal Code | Answers the territory boundary question directly |

---

## After August 24

Once the book goes live, Account Owner becomes Sairam on the 680 that move, so a plain
**My Accounts** report covers most of it. Keep the `Package Territories F27` filter
anyway for two reasons: the 19 February holdovers will still sit with their current
owners and would drop out of a My Accounts view, and the territory field is the only
field that states which territory an account belongs to rather than who happens to own
it today.

Retire the holdover variant once every account has landed.

---

## What this does not solve

The report will show what Salesforce holds, which is not necessarily correct. Two things
to check on the first run:

- **The 37 duplicate records** are still separate account records until someone merges
  them, so the row count will overstate the number of real companies by that much. Detail
  in `territory/F27-Duplicate-Records-Sairam-Gajavelli.xlsx`.
- **Berje Inc** is a departure, so it will not appear under this filter at all. It carries
  a different territory value.
