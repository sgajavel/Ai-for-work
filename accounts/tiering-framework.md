# Tiering Framework — working detail

**Status:** DRAFT v0, 2026-08-13. Written before the territory list landed. Sairam
confirms or rewrites once he sees the real data.

The summary lives in `CLAUDE.md` Section 3. This file holds the working detail: the
signal definitions, the promotion rules, and the record format.

---

## The question tiering answers

Not "how good is this account" in the abstract. Three operational questions:

1. **Who do we need to meet with?** Warm and active. Tier 1.
2. **Who can I attack now?** Fit, named contact, a hook to open on. Tier 2.
3. **Who needs work before they are workable?** Whitespace. Tier 3.

An account that cannot be actioned this quarter is not Tier 1 no matter how large or
attractive it is. Tier is about **cycle temperature and readiness**, not account size.

---

## Signal definitions

### Warm-active signals (any one puts the account in Tier 1)

| Signal | Notes |
|---|---|
| Open opportunity | Any stage |
| Closed-lost in the last ~12 months | The reason for the loss becomes the reopen hook |
| Lapsed membership | Winback bucket in the playbook. Note the lapse year |
| Meeting held in the last ~12 months | By anyone, not just Sairam |
| Live inbound | Pricing wizard, demo request, contact form. Same-day follow-up |
| Contact was a member at a prior employer | Past-member bucket in the playbook |
| Heavy engagement footprint | 10+ related resources in tight succession signals a program being built, not browsing |

### Tier 2 qualifiers (fit plus a hook, no active cycle)

- Named IT leader identified and currently in seat
- Plus at least one of: engagement footprint, a clean industry-timing hook, a shared
  LinkedIn connection, a relevant event in geo, a public trigger event (funding,
  acquisition, new CIO, breach, compliance deadline)

An account with a named contact but genuinely nothing to open on is still Tier 2, it
just sits at the bottom of it. Sequence it on role-based relevance per the playbook's
Zero CV default.

### Tier 3 markers

- No named IT contact, or the one on file is stale or holds a vague title
- Zero engagement footprint
- Fit plausible but unconfirmed

Tier 3 is a **research queue**, not a discard pile. The work is contact discovery and
account mapping, not outreach.

---

## Disqualifiers (not a tier, removed from the book)

These come out of the tiering pass entirely, with the reason recorded:

- **Live membership** on the account or contact. Playbook guardrail, Section 1.
  Reclassify and hand off, never cold-pitch a current member
- **Out of scope** per CLAUDE.md Section 2: conglomerate-owned, credit union, casino
  or tribal, SLED
- **Out of territory** by zip
- **Over $500M** revenue

Keep these in a rejected list with the reason. A conglomerate that divests, or a
membership that lapses, comes back into the book later, and the reason field is what
makes that catchable.

---

## Promotion and re-tiering

Tier is not static. Re-tier on new signal, same day where possible.

- T3 → T2 when a named contact and a hook both exist
- T2 → T1 on any warm-active signal, most commonly an inbound or a meeting booked
- T1 → T2 when the cycle goes quiet for a quarter with no reply
- Any tier → disqualified on membership, ownership change, or revenue correction

---

## Record format

One line per account in the working list, expanded to a file in `accounts/` once real
work starts on it.

```
| Account | Tier | Reason | Named contact | Next action | Last touch |
```

The **reason** field is the one that has to be filled properly. "T1" alone is not
usable a month later. "T1: membership lapsed 2024, CIO Jane Doe still in seat" is.

## Suggested cadence

- Full re-tier when the territory list refreshes
- Weekly pass over T1 for anything that went quiet
- Rolling T3 research to keep T2 stocked

Cadence is a proposal, not a rule. Sairam sets it.
