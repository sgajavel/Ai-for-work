# Salesforce campaign event export, pulled 2026-08-13

Raw record of the event list Sairam pasted on 2026-08-13. Kept verbatim so the
playbook's event calendar has an auditable source and so the data survives if the
playbook gets rewritten.

**Coverage:** July 22, 2026 through September 21, 2026. Nothing beyond that date.
That ceiling is why the fall IGNITE wave (DC, Sacramento, Atlanta) is still
unverified.

**Handling:** contains internal campaign links and internal staff names. Internal
reference only, never prospect-facing. Intel firewall, CLAUDE.md Section 5.

**Read the name column correctly.** The people listed against each event are
**internal Info-Tech colleagues tagged as attending**. They are not the billed speaker
lineup and not a public agenda. Never repeat one of these names to a prospect as a
speaker, and do not treat them as contradicting the featured-speaker names in the
playbook, which come from the events page and are tracked separately.

---

## Upcoming as of 2026-08-13

| Date | Event | Type | Location | Venue | Info-Tech attendees (internal) |
|---|---|---|---|---|---|
| Aug 16-18 | CACP Conference | 3rd party (CACP) | Edmonton, AB | | Benjamin Selmani, Angela McDow, Cole Cioran |
| Aug 20 | Georgia Digital Government Summit | 3rd party (US Public Sector) | Atlanta, GA | | Isabelle Hertanto, Mike Daniels, Titus Moore, Lee Posey, Ryan Martin, Jordan Reed |
| Aug 25-27 | Tertiary ICT Conference | 3rd party (VUOW) | Wellington, NZ | | Ian Palmer |
| Sep 2 | Connecticut Digital Government Summit | 3rd party (GovTech) | Hartford, CT | Connecticut Convention Center | |
| Sep 9 | Digital Stratosphere 2026 | 3rd party (Third Stage Consulting) | Denver, CO | Le Méridien Denver Downtown | |
| Sep 9 | Mississippi Digital Government Summit | 3rd party (GovTech) | Flowood, MS | Sheraton Flowood The Refuge | |
| Sep 16 | CIO Roundtable Ottawa | Hosted, CIO Roundtable | Ottawa, ON | Lord Elgin Hotel | Cole Cioran |
| Sep 16-18 | Leadership Summit Ottawa | Summit | Ottawa, ON | | |
| Sep 17, 9AM-12PM | LEVEL-UP Austin, AI Workforce Development | Hosted, LEVEL-UP | Austin, TX | Hyatt Regency Austin | Jai Hebel |
| Sep 17, 2PM - Sep 18, 2:30PM | IGNITE Texas | Hosted, IGNITE | Austin, TX | Hyatt Regency Austin | Arushi Rawat |
| Sep 20-24 | 27th TribalNet Conference and Tradeshow | 3rd party (Tribal Net) | Texas | | |
| Sep 21, 3-6PM | LEVEL-UP Barcelona, AI Workforce Development | Hosted, LEVEL-UP | Barcelona, ES | Grand Hyatt Barcelona | Martin Bufi |
| Sep 21, 3-6PM | LEVEL-UP Barcelona, IT Leadership Development | Hosted, LEVEL-UP | Barcelona, ES | Grand Hyatt Barcelona | Amanda Mathieson |

## Passed

| Date | Event | Type | Location |
|---|---|---|---|
| Jul 22 | CIO Roundtable | Hosted | Washington, D.C. |
| Jul 22-24 | Leadership Summit Seattle | Summit | Seattle, WA |
| Aug 2-5 | TASSCC 2026 Annual Conference | 3rd party (TASSCC) | Grapevine, TX |
| Aug 12 | CIO Roundtable Nashville | Hosted | Nashville, TN |
| Aug 12-14 | Leadership Summit Nashville | Summit | Nashville, TN |

---

## What this export changed in the playbook

1. **IGNITE Austin confirmed**, September 17-18, Hyatt Regency Austin. Date and venue
   only. The export says nothing about the speaker lineup, so the playbook's featured
   name stands unchanged and still unverified.
2. **LEVEL-UP is active.** The playbook said the series had no scheduled dates. Wrong,
   there are three sessions.
3. **CIO Roundtable is active.** Ottawa, September 16. The playbook said nothing was
   upcoming.
4. **Leadership Summit series added.** It was not tracked in the playbook at all.
5. **No California event appears anywhere in the window.** Does not disprove IGNITE
   Sacramento in late October, since the window closes September 21, but it does mean
   nothing in California for at least the next five weeks.
6. **Co-location pattern.** LEVEL-UP runs alongside the bigger event (Austin the same
   morning as IGNITE, Barcelona the day before LIVE). CIO Roundtables attach to
   Leadership Summits at the same venue and date.

## Routing flags

Several of the third-party events sit in other reps' books:

- Georgia, Connecticut, and Mississippi Digital Government Summits → **SLED team**
- 27th TribalNet Conference → **Erin Font**, casinos and tribal enterprises
- Tertiary ICT Conference → education, and APAC

## Data quality notes in the source

Worth knowing the export is not clean, in case these fields get used elsewhere:

- Digital Stratosphere: end date 8/9 precedes start date 9/9, flagged "Error in
  calculation" in the source
- Leadership Summit Seattle: venue reads "The Joseph, a Luxury Collection Hotel,
  Nashville" while the city fields say Seattle, WA. Copy-paste error
- Nashville Leadership Summit appears twice, once with an end time before the start
- Connecticut summit city spelled "Hardfod"
- The event is titled "IGNITE Texas" while the city is Austin
