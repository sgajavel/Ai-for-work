# ACD Command Center — Sairam Gajavelli, Info-Tech Research Group

**Owner:** Sairam Gajavelli, Associate Commercial Director (ACD)
**Territory:** California SMB (sub-$500M revenue accounts), zip-code defined
**Last updated:** 2026-08-13
**Status:** initial build. Territory list not yet loaded. Onboarding context loaded.

This file is the operating manual for this repo. It tells Claude who Sairam is, what
is in and out of his book, how the sales motion works, how accounts get tiered, and
where everything lives. When a rule changes, edit this file rather than carrying the
change in chat.

Deeper background lives in `reference/role-context.md` (the full onboarding
distillation) and `playbook/outreach-playbook.md` (all outreach drafting). This file
carries only what changes behavior day to day.

---

## 1. Role and scope

Sairam was promoted in **August 2026** from Enterprise AE to Associate Commercial
Director, moving into an SMB territory. This is a real change of motion, not a title
change: shorter call windows, higher volume, faster cycles, less room to build rapport
slowly. Onboarding is ongoing and intensive, run in parallel with a colleague, Jason.

He books and runs his own discovery calls. No BDR handoff, no director-led close on
standard outreach. On non-focused SMB accounts he owns Discover, Build, Present, and
Transition solo, with no Executive Counselor safety net, which means weak discovery
turns directly into a weak CKIP with nobody downstream to catch it.

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

**What he sells:** research and advisory memberships (Core Membership, tiered by seat
type: Counselor, Advisory, Team, Reference) plus attached services: diagnostics,
blueprints, workshops, price benchmarking, contract review, and counselor programs.
Buyers are CIOs, CTOs, CISOs, CDOs.

Note on geography: Sairam is based in Ontario, Canada and covers a California
territory remotely. Event geo-matching targets **California/West Coast** events for
prospects, never Ontario events. See Section 8.

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

This is the same discipline as the **entity precision** rule in Section 5. Getting
the legal entity right is what makes the ownership question answerable at all.

### Standing rule for Claude

When Sairam names or uploads an account, run the scope check first and say the
result in one line before doing anything else. If the account routes out, say so
and stop, do not draft outreach for it.

---

## 3. The sales motion

Full detail in `reference/role-context.md`. The parts that shape work in this repo:

### QP formula

```
QP = VMD x Value x Power x Plan
```

Vision Match Differentiated, times Value, times Power, times Plan. **Multiplicative.
A zero anywhere means no qualified prospect.** This is the spine everything hangs off.

**The value chain behind VMD:**

```
Corporate Objective -> Business Issue (Goal/Strategy) -> Key IT Initiative
  -> Problem -> Vision of Solution
```

### The 7 discovery questions

Each one maps to a slot in the chain above.

| # | Question | Captures |
|---|---|---|
| 1 | What projects are you working on? Rank them | Key IT Project |
| 2 | Why are you doing this project? | Business Goal |
| 3 | How do you envision solving this? | Vision of Solution |
| 4 | What is stopping you from getting this done? | Problem |
| 5 | What budget is tied to it? Projected ROI? | Value |
| 6 | When do you need it done by? | Plan |
| 7 | Who is working on this with you? | Power / Team |

Discovery's one job is establishing VMD, and it is not done until it is documented in
Salesforce. **Documentation is a stage gate, not admin.**

### One conversation, four artifacts

The five FAC discovery elements (Business Objective, Business Issues, Key IT
Initiatives, Problems, Vision of Solution) are the *same fields* as the QP formula,
the CKIP table columns, and the Salesforce notes headings. Capture them properly once
and everything downstream gets easier. This is why discovery notes need the prospect's
exact words captured live, not paraphrased afterward.

### How tiering connects to QP

Tier is a **pre-QP** judgment: how close is this account to a conversation where a QP
can be built. Reading the tiers against the formula:

- **Tier 1** has something live, so VMD is plausibly reachable on the first call
- **Tier 2** has a named contact, so **Power** has a candidate but is unconfirmed
- **Tier 3** has no named contact, so Power is a hard zero and no QP is possible yet

That is the real reason Tier 3 gets research before outreach, not outreach.

---

## 4. Call structures

**30-minute discovery** (six steps): Build Rapport, Confirm Agenda, R&A Experience
check, Show Management & Governance Framework, Showcase Blueprint, Ask for More Time.
This is an *earn the second meeting* call, not full discovery.

**60-minute FAC** (eight steps): adds Establish Credibility (story slot) and a full
discovery block covering the five elements **before** showcasing any capability, then
a Recap/MAP close with calendarized next steps.

**Mutual Action Plan:** every opportunity gets one, no size or stage threshold. Two
required halves, a recap of the discussion and next steps on a reverse timeline. The
Actions and Next Steps table has three columns, Action Item / Owner / Date, and every
line is dated and owned. Reserve the last 10 minutes of any call for it. Same-day
follow-up is the standard.

---

## 5. Standing sales rules

These apply on every call and in every written output.

- **Intel firewall.** Internal account knowledge never surfaces on a call or in an
  email. Use peer framing ("I've worked with companies like yours"), never internal
  CRM detail. Everything in `territory/` and `accounts/` is behind this firewall.
- **Entity discipline.** Always the precise legal entity name. See the entity gotchas
  in playbook Section 13 (CSC Global, Harvard, TPG).
- **Power is the habitual blank.** It must be explicitly asked, never assumed. Flag it
  unfilled until confirmed. "Anyone else you'd bring in?" is a soft participation
  probe, not the Power question. The real ask is who signs off and who else has to
  agree.
- **No screen share by default.** Exceptions: Building Alignment live co-creation, and
  the FAC website walkthrough.
- **Roleplay and simulation content is never citable as real account intel.**
- **Never fabricate policy or numbers under pressure.** If it is unclear what is
  sendable or available, say so and confirm after. This applies to Claude too: do not
  invent an Info-Tech policy, price, entitlement, or event.
- **No em dashes.** Sairam's personal writing rule, everywhere, not just email.

### Stalls versus objections

Different handling, and the distinction gets missed.

- An **objection** gets answered.
- A **stall** ("send me something first," "maybe later") gets the **Deferral Ladder**:
  shrink the ask, then a cancelable placeholder, then a renewal-date hook.

Every response to a stall must land on a specific day and time. "The week after" does
not count as a close.

---

## 6. Coaching focus

Three development areas from Jillian Reed. All coaching maps back to these, so drafts
and prep should support them rather than work around them.

1. **Push deeper after paraphrasing a pain.** A paraphrase and a nod is not enough.
   Ask one consequence question before moving on. "What happens if this doesn't get
   solved?"
2. **Earn the close before booking.** Never move to calendar logistics before an
   explicit value or interest confirmation. "Was this useful, worth another
   conversation?" comes before offering times.
3. **Build a tactical SMB fast start plan.** Concrete actions, channels, numbers,
   cadences. Not a strategic overview.

**Number 3 is blocked on the territory list**, which is also the top open item in
Section 11. When the list lands, the fast start plan is the first deliverable, ahead
of any outreach drafting.

### Known failure patterns

- **Over-scripting.** Answers the question prepared for instead of the one asked. Fix:
  one beat of direct answer first, then decide whether a prepared line fits.
- **Fake double-downs.** "Based on what you said about X" only counts if the
  explanation genuinely responds to their words. Test: if the line could have been
  said before they spoke, it is a repeat, not a double-down.
- **Case study pronunciation.** Gimeno (Autoneum), Husco, Amkor, Ampath.

---

## 7. People

| Person | Role | When they matter |
|---|---|---|
| Jillian Reed | Hiring manager, primary coach | Source of the three development areas |
| Alexandra Keech | Onboarding lead | Process and policy questions |
| Dana | VP of Business Development | Pending conversation |
| Mel Kellman | Acquire director | |
| Kennedy Confurius | Competitive intelligence | Escalation contact on Gartner deals |
| Linda Lepore | Runs win rooms | Competitive deals |
| Craig Broussard | Senior Executive Counsellor | Warm-referral source, CC convention in playbook Section 14 |
| Tom Zehren | CEO | Executive escalation only, rare |
| Brad Sprecher | CRO | Executive peer-to-peer only, rare |

### Competitive: Gartner

Gartner is the #1 competitor, Forrester rising. Their weakness is complex, siloed,
seat-based licensing that confuses their own clients. GTP (Gartner for Technical
Professionals) is the emerging threat, cheap per-seat with narrow research scope, so
RFP comparisons against Info-Tech's full-access seats are apples to oranges.

Talk track is curiosity first. Never lead with a pitch, never trash Gartner. The
killer question: **"Walk me through the last project Gartner supported and the
outcome."** It usually exposes that the client did the work themselves. Log competitor
mentions in Salesforce at opportunity and account level to trigger competitive
support.

---

## 8. Tiering framework (DRAFT v0, pending Sairam's confirmation)

Sairam tiers his territory by **warm active cycles** first, then by fit and
reachability. The point is to answer three questions: who do we need to meet with, who
can we attack now, and who sits on the back burner.

These definitions are a starting proposal. Sairam confirms or rewrites once the
territory list lands. Working detail in `accounts/tiering-framework.md`.

### Tier 1 — Warm and active. Meet first.

Something is already live or recently live on the account.

- Open or recently closed-lost opportunity
- Lapsed membership (winback candidate)
- A meeting held in roughly the last 12 months, by anyone
- Live inbound signal (pricing wizard, demo request, contact form)
- Named contact who was a member at a prior employer
- Heavy recent research or resource engagement footprint

**Action:** direct meeting push. Highest personalization. First on the calendar.

### Tier 2 — Qualified with a hook. Attack list.

No active cycle, but a real fit with a named contact and something to open on.

- Right size, right industry, IT leadership identified
- Some engagement footprint, or a clean industry-timing hook

**Action:** sequenced outreach per the playbook. Volume lives here.

### Tier 3 — Cold whitespace. Build before you touch.

In territory and in scope, but not yet workable. No named IT contact, no footprint,
fit plausible but unconfirmed.

**Action:** contact discovery and account mapping before outreach. Use the
`account-mapping` skill. Promote to Tier 2 once a named contact and a hook exist.

### Tier assignment rules

- Tier is a property of the **account**, not the contact
- Any live membership on the account removes it from outreach entirely, per the
  playbook guardrail
- Re-tier on new signal. A Tier 3 that fills out a pricing wizard is Tier 1 that day
- Record the reason, not just the number. "T1: lapsed 2024, prior contact still in
  seat" is useful. "T1" alone is not

---

## 9. Skills built for this role

Six skills exist for this workflow. Reach for them rather than improvising.

| Skill | Use when |
|---|---|
| `account-mapping` | Corporate structure, buying centres, org charts, whitespace. **Also the tool for the conglomerate test** |
| `discovery-call-prep` | Prepping a booked call. Also Phase 2, filling the QP form from call notes |
| `discovery-story` | Scripting a customer story, rapport or in-discovery variant |
| `ckip-builder` | CKIP prep before discovery, or building the needs slide after |
| `discovery-deck-builder` | Assembling the discovery deck. Explicit request only |
| `sales-gap-analysis` | Post-call debrief, Salesforce notes, MAP, gap analysis |
| `chat-handoff` | Long session, accumulated drafts, context getting heavy |

Verified customer story library: Brett Wilson (Australian Red Cross), Jose Gimeno
(Autoneum), Seneca Gaming, CrossCountry Mortgage, Husco, Amkor, Leonardo DRS, NASA,
New-Indy Containerboard, Ampath Laboratories. Full 46-entry catalog is in Drive.

---

## 10. Standing behaviors for Claude

### On every account or prospect Sairam brings

1. **Scope check first** (Section 2). One line. In-book, routes out, or needs
   ownership check.
2. **Membership check.** Live membership on the contact or account means stop and
   reclassify.
3. **Tier it** if not already tiered, with a one-line reason.
4. Then do the actual work he asked for.

### On drafting outreach

Follow `playbook/outreach-playbook.md` exactly. The two rules broken most often:

- **No em dashes anywhere.** Commas or periods.
- **Sign off "Talk soon," blank line, "Sairam."** Never "Sai."

Go straight to the draft. No preamble, no explanation of how the campaign type was
classified.

### On event mentions

The playbook's event calendar (Section 11) was partially refreshed 2026-08-13 from a
Salesforce campaign export. **It is confirmed only through September 21, 2026.**
Everything after that date, including IGNITE Sacramento, is unverified.

**As of today there is no confirmed California event and no live virtual fallback, so
skip the event mention on California outreach.** Never invent a geo-match. Every row
in the calendar carries a verification mark, check it before using the row.

**Names on an SFDC campaign record are internal colleagues tagged as attending, not
the speaker lineup.** Never repeat one to a prospect as a speaker, that is a
fabricated claim about the agenda. They are also internal, so they stay behind the
intel firewall. Speaker names come from the events page only.

### On uncertainty

Ask rather than guess on: account ownership, revenue thresholds, parent structure,
membership status, contact identity, Info-Tech pricing, entitlements, and policy.
Guess freely on nothing that reaches a prospect.

---

## 11. Repo map

```
CLAUDE.md                       This file. Operating manual and standing rules.
reference/
  role-context.md               Full onboarding distillation. Sales framework,
                                training takeaways, coaching feedback, product lines.
playbook/
  outreach-playbook.md          Single source of truth for outreach drafting.
                                Voice, subject lines, structure, campaign types,
                                event calendar, pre-send checklist.
territory/                      Territory list, zip codes, coverage boundaries.
  README.md                     Ingestion spec and current status.
accounts/                       Tiered account working files and account maps.
  tiering-framework.md          Working detail behind Section 8.
meetings/                       Notes from internal meetings, training, enablement.
bdr-claude-pitch-deck/          Unrelated prior project. Leave alone unless asked.
```

---

## 12. Open items

Merged from this repo and from the onboarding notes. Update as these close.

**Blocking:**

- [ ] **Territory list.** Not yet received. Once it lands: load into `territory/`, run
      the scope check across it, produce the initial tiering pass, then build the
      tactical SMB fast start plan (Jillian development area 3).
- [ ] **Zip code list.** Assigned zip codes not yet defined.
- [ ] **SMB activity benchmarks.** Needed for the fast start plan. Unknown.

**Events:**

- [ ] **Confirm IGNITE Sacramento Oct 27-28, 2026.** The only California in-person
      anchor and currently unverified. Needs an SFDC export reaching into November, or
      the events page.
- [ ] **Confirm the rest of the fall IGNITE wave.** DC Oct 1-2, Atlanta Nov 2-3.
- [ ] **No virtual fallback exists.** Every Industry Roundtable and webinar has passed
      and the IT Playbooks Summit is undated. Nothing to offer a no-geo-match prospect.

**Sales enablement:**

- [ ] **What is sendable to a prospect pre-meeting?** Sample report, one-pager? Flagged
      after a pitchmonster where policy may have been fabricated under pressure.
- [ ] **Which customer stories are cleared for verbal use** versus quote-only.
- [ ] **Updated FY26 member value stat sheet**, whether one exists.
- [ ] **CKIP Lesson 6 and FAC Module Lesson 4** not yet captured.

**Admin:**

- [ ] **Meeting content** from 2026-08-13. Lands in `meetings/`.
- [ ] **Confirm tiering definitions.** Section 8 is a draft proposal.
- [ ] **Full names for routing reps.** "Nick P" and "Erin Font" as given. SLED contact
      unnamed.
- [ ] **Date of the Dana conversation.**
- [ ] **Reconcile playbook to California.** The large-account coordination list in
      playbook Section 9 was written for a national enterprise book and is mostly
      irrelevant to a California SMB territory. Needs a rewrite once the list is known.

---

## 13. Conventions

- Dates in `YYYY-MM-DD`.
- Account files named by company, lowercase, hyphenated: `accounts/acme-widgets.md`.
- Anything that could reach a prospect gets checked against the playbook's banned list
  before it is handed over.
- Salesforce IDs, campaign links, internal notes, and rep names stay out of
  prospect-facing text. Intel firewall, Section 5.
- Territory and account data may contain non-public commercial information. It stays
  in this repo and does not get pasted into external tools.
