# ACD Command Center — Sairam Gajavelli, Info-Tech Research Group

**Owner:** Sairam Gajavelli, Associate Commercial Director (ACD)
**Territory:** California SMB (sub-$500M revenue accounts), zip-code defined
**Last updated:** 2026-08-13
**Status:** initial build. Territory list not yet loaded. Meeting content not yet loaded.

This file is the operating manual for this repo. It tells Claude who Sairam is, what
is in and out of his book, how accounts get tiered, and where everything lives.
When a rule changes, edit this file rather than carrying the change in chat.

---

## 1. Role and scope

Sairam is an ACD covering **small and mid-market accounts in California**. He books
and runs his own discovery calls. There is no BDR handoff and no director-led close
on standard outreach.

**In scope:**

- Accounts whose registered/primary location falls in one of his assigned California
  zip codes
- Annual revenue **under $500 million**
- Standalone entities, meaning the sub-$500M revenue is the whole company, not a
  division of something larger

**Out of scope (see Section 2 for routing):**

- Any account under $500M that is a subsidiary, division, or business unit of a
  larger conglomerate
- Small credit unions
- Small casinos and tribal enterprises
- State, local, and education (SLED)

Note on geography: Sairam is based in Ontario, Canada and covers a California
territory remotely. Event geo-matching should target **California/West Coast**
events for prospects, not Ontario events. See Section 6.

---

## 2. Coverage exclusions and rep routing

**Test every account against this before doing any work on it.** Time spent on an
account that belongs to another rep is time lost, and double-touching an account
another rep owns is a real problem, not a cosmetic one.

| Account type | Owner | Notes |
|---|---|---|
| Sub-$500M but part of a larger conglomerate | Large enterprise rep | The parent relationship, not the sub's revenue, decides ownership |
| Small credit unions | Nick P | Full name to be confirmed |
| Small casinos and tribal enterprises | Erin Font | Full name to be confirmed |
| State, local, education | SLED team | Named contact to be confirmed |

### The conglomerate test

An account passes into Sairam's book only if it is standalone. Before tiering or
prospecting, check for:

- A parent company, holding company, or PE/VC sponsor with operating control
- "A [X] company" or "part of the [X] family" language on the site or LinkedIn
- Shared IT leadership with a parent (a CIO whose title spans multiple entities)
- A LinkedIn company page that redirects or ladders up to a larger parent

If any of these hit, flag it as **enterprise-owned** and route out. When it is
genuinely ambiguous (minority investor, loose franchise relationship, recently
divested), flag it as **needs-ownership-check** rather than guessing. Do not
silently drop it and do not silently keep it.

### Standing rule for Claude

When Sairam names or uploads an account, run the scope check first and say the
result in one line before doing anything else. If the account routes out, say so
and stop, do not draft outreach for it.

---

## 3. Tiering framework (DRAFT v0, pending Sairam's confirmation)

Sairam tiers his territory by **warm active cycles** first, then by fit and
reachability. The point of tiering is to answer three questions: who do we need to
meet with, who can we attack now, and who sits on the back burner.

These definitions are a starting proposal. Sairam should confirm or rewrite them
once the territory list lands, and this section gets updated to match.

### Tier 1 — Warm and active. Meet first.

Something is already live or recently live on the account.

- Open or recently closed-lost opportunity
- Lapsed membership (winback candidate)
- A meeting held in roughly the last 12 months, by anyone
- Live inbound signal (pricing wizard, demo request, contact form)
- Named contact who was a member at a prior employer
- Heavy recent research/resource engagement footprint

**Action:** direct meeting push. Highest personalization. First on the calendar.

### Tier 2 — Qualified with a hook. Attack list.

No active cycle, but the account is a real fit and there is a named contact plus
something to open on.

- Right size, right industry, IT leadership identified
- Some engagement footprint (webinar attendance, downloads, LinkedIn follow, event
  registration)
- Or a clean industry-timing hook even with a thin footprint

**Action:** sequenced outreach per the playbook. Volume lives here.

### Tier 3 — Cold whitespace. Build before you touch.

In territory and in scope, but not yet workable.

- No named IT contact, or only a stale/vague one
- No engagement footprint at all
- Fit is plausible but unconfirmed

**Action:** contact discovery and account mapping before outreach. Use the
`account-mapping` skill. Promote to Tier 2 once a named contact and a hook exist.

### Tier assignment rules

- Tier is a property of the **account**, not the contact
- Any live membership on the account removes it from outreach entirely, per the
  membership guardrail in the playbook (Section 1 of the playbook)
- Re-tier on new signal. A Tier 3 that fills out a pricing wizard is Tier 1 that day
- Record the reason for the tier, not just the number. "T1: lapsed 2024, prior
  contact still in seat" is useful; "T1" alone is not

---

## 4. Repo map

```
CLAUDE.md                       This file. Operating manual and standing rules.
playbook/
  outreach-playbook.md          Single source of truth for all outreach drafting.
                                Voice, subject lines, structure, campaign types,
                                event calendar, pre-send checklist.
territory/                      Territory list, zip codes, coverage boundaries.
  README.md                     Ingestion spec and current status.
accounts/                       Tiered account working files and account maps.
  tiering-framework.md          Working detail behind Section 3.
meetings/                       Notes and content from internal meetings, training,
                                enablement, and kickoffs.
bdr-claude-pitch-deck/          Unrelated prior project (internal Claude pitch deck).
                                Not part of ACD workflow. Leave alone unless asked.
```

---

## 5. Standing behaviors for Claude

### On every account or prospect Sairam brings

1. **Scope check first** (Section 2). One line. In-book, routes out, or needs
   ownership check.
2. **Membership check.** Live membership on the contact or account means stop and
   reclassify, per the playbook guardrail.
3. **Tier it** if it is not already tiered, with a one-line reason.
4. Then do the actual work he asked for.

### On drafting outreach

Follow `playbook/outreach-playbook.md` exactly. It governs voice, banned phrases,
subject line format, email structure, campaign types, and the pre-send note. Two
rules from it that get broken most often:

- **No em dashes anywhere.** Commas or periods.
- **Sign off "Talk soon," blank line, "Sairam."** Never "Sai."

Go straight to the draft. No preamble, no explanation of how the campaign type was
classified.

### On event mentions

The playbook's event calendar (playbook Section 11) is **stale as of 2026-08-13** and
was already flagged overdue on 2026-07-21. Several listed sessions have passed. Do
not reference an event from that table without refreshing from
https://www.infotech.com/events first, then updating the playbook file.

For this California territory, the near-term in-person anchor is **IGNITE Sacramento,
October 27-28, 2026** for Northern California prospects. Southern California has no
matched in-person event in the current calendar, so use an industry-matched virtual
session or skip the event mention. Never invent a geo-match.

### On uncertainty

Ask rather than guess on: account ownership, revenue thresholds, parent structure,
membership status, and contact identity. Guess freely on nothing that reaches a
prospect.

---

## 6. Open items

Tracked so nothing gets lost between sessions. Update as these close.

- [ ] **Territory list.** Not yet received. Once it lands, load into `territory/`,
      run the scope check across it, and produce the initial tiering pass.
- [ ] **Zip code list.** The actual assigned zip codes are not yet defined here.
- [ ] **Meeting content.** Sairam has meetings from 2026-08-13 to share. Lands in
      `meetings/`.
- [ ] **Confirm tiering definitions.** Section 3 is a draft proposal.
- [ ] **Full names for routing reps.** "Nick P" and "Erin Font" as given. SLED team
      contact unnamed.
- [ ] **Refresh the event calendar** in the playbook. Overdue since 2026-06-22.
- [ ] **Reconcile playbook to California.** The playbook's geo-matching table and
      large-account coordination list were written for a national/mixed book. Both
      need a California SMB pass once the territory is known.

---

## 7. Conventions

- Dates in `YYYY-MM-DD`.
- Account files named by company, lowercase, hyphenated: `accounts/acme-widgets.md`.
- Anything that could reach a prospect gets checked against the playbook's banned
  list before it is handed over.
- Salesforce IDs, internal notes, and rep names stay out of prospect-facing text.
- Territory and account data may contain non-public commercial information. It stays
  in this repo and does not get pasted into external tools.
