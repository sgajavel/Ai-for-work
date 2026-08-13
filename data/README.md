# Book of business data

Five CSVs. These are the **source of truth** for the tracker. Edit them directly, in
a text editor or a spreadsheet, then rebuild the dashboard:

```
python3 scripts/build_dashboard.py
```

Standard library only, no install step. Open `dashboard.html` in a browser.

> **EXAMPLE rows are in every file right now** so the dashboard renders before the
> territory list lands. Every one starts with `EXAMPLE` or an `EX-` id. Delete them
> all before working a real book. The dashboard shows a banner while any remain.

---

## accounts.csv — one row per account

| Column | Values | Notes |
|---|---|---|
| `account_id` | free | Your key. Anything stable |
| `account_name` | free | **Precise legal entity name.** Entity discipline |
| `tier` | `1` `2` `3` or blank | Blank means untiered, and the dashboard flags it |
| `tier_reason` | free | Required in practice. "T1" alone is useless a month later |
| `scope_status` | `in-book` / `routed-out` / `needs-ownership-check` | Set on every row |
| `routed_to` | free | Who owns it instead. Nick Pearson, Erin Font, Andrew Daigle, Partner Team, an LE vertical rep |
| `industry` | free | Drives the credit union, casino/tribal, SLED, and MSP exclusions |
| `revenue_musd` | number | Millions USD. **In-segment band is 50 to 500** |
| `parent_company` | free | Blank if standalone. The single most important scope field |
| `city`, `zip` | free | Zip decides the territory boundary. California is split five ways |
| `membership_status` | `none` / `live` / `lapsed-YYYY` | `live` removes the account from outreach entirely |
| `last_reviewed` | `YYYY-MM-DD` | |

## contacts.csv — one row per person

`contact_id`, `account_id`, `name`, `title`, `email`, `linkedin`, `persona_fit`
(`core-it` / `adjacent` / `mismatch`), `is_power` (`yes` / `no` / `unconfirmed`),
`notes`.

`is_power` defaults to `unconfirmed` and stays there until it has been explicitly
asked. Power is never assumed.

## outreach.csv — one row per touch

`touch_date`, `account_id`, `contact_id`, `channel`, `campaign_type`, `touch_number`,
`subject_or_note`, `outcome`, `next_followup_date`, `status`.

- `campaign_type`: `zero-cv`, `past-member`, `winback`, `event`, `hot-inbound`,
  `follow-up`, `reconnect`, `post-decline-reset`
- `outcome`: `sent`, `no-response`, `replied`, `meeting-booked`, `declined`, `bounced`
- `status`: `open` or `closed`

**This file is the follow-up engine.** A row with `status=open` and a
`next_followup_date` appears in the dashboard's follow-up panel, colour-coded by how
overdue it is. Close a row when the thread is genuinely done, not when you get bored
of it.

Playbook cadence: about a week for "in case it got buried," two-plus weeks before
"trouble reaching you." Tighten the CTA on the second touch.

## cycles.csv — one row per opportunity

`cycle_id`, `account_id`, `contact_id`, `stage`, `opened_date`, `vmd`, `value`,
`power`, `plan`, `next_step`, `next_step_date`, `map_documented`, `close_target`,
`notes`.

- `stage`: `discovery`, `fac`, `proposal`, `commit`, `closed-won`, `closed-lost`
- The four QP columns: `yes`, `partial`, or `no`

The QP columns drive the dashboard's QP bar. Since `QP = VMD x Value x Power x Plan`
is multiplicative, **any column that is not `yes` makes the whole cycle a zero**, and
the card renders as blocked. That is the intended reading, not a display quirk.

Do not mark `power` as `yes` off a soft participation probe. It is `yes` when you know
who signs, who controls budget, and who can veto.

## signals.csv — one row per signal event

`signal_date`, `account_id`, `signal_type`, `detail`, `source`, `actioned`.

`signal_type`: `inbound-pricing-wizard`, `inbound-demo`, `inbound-contact-form`,
`content-download`, `webinar`, `event-registration`, `leadership-change`, `funding`,
`acquisition`, `breach`, `membership-lapse`, `closed-lost-reopen`, `other`.

A signal is a re-tiering trigger. A Tier 3 that fills out a pricing wizard is Tier 1
that day. `actioned=no` keeps it visible on the dashboard until it has been worked.

---

## Handling

This data is non-public commercial information. It stays in the repo, behind the
intel firewall in CLAUDE.md Section 5. None of it goes in an email, and none of it
gets pasted into an external tool.
