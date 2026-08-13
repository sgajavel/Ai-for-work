# F27 proposed book, analysis

**Source:** `F27_Proposed_North_America_Territories_Internal_Version_1.csv`, 699 rows
**Analysed:** 2026-08-13
**Feedback cut-off:** 2026-08-19. Target to director 2026-08-14.

Every row in the file is proposed to Sairam Gajavelli. This is the whole book, not an
extract.

---

## 1. What the book actually is

| Cut | Count |
|---|---|
| Rows in the file | 699 |
| Distinct account groups | 590 |
| Viable | 608 |
| Non-Viable | 84 |
| Viability blank in SFDC | 7 |
| California billing | 647 |
| Everything else | 52 |
| Prospect | 661 |
| **Winback (lapsed member)** | **38** |

**The working number is not 699.** After retiring duplicate records and setting aside
what routes out, the tracker resolves to **566 in-book accounts**, 68 needing an
ownership decision, 37 duplicate records, 25 non-viable, 3 routing out.

**This is a Northern California / Bay Area book.** The account names carry it clearly:
Port of San Francisco, SF SPCA, SFMOMA, KQED, Exploratorium, Golden Gate National Parks
Conservancy, Alameda Alliance for Health, Contra Costa Water District, North East
Medical Services, San Francisco AIDS Foundation, Chinese Hospital. California 4 of 5 is
the Bay Area. That is the first useful thing the file tells us, because the zip list is
still undefined.

Composition skews technology and SaaS heavily, with a real second cluster of Bay Area
nonprofits, healthcare, construction, and professional services.

---

## 2. Timing, tested against the F27 holdover rules

| Moving Time Frame | Count |
|---|---|
| August 24, 2026 | 680 |
| **Feb 1, 2027** | **19** |

### Open Opportunities Proposal+ is zero on all 699 rows

Not "mostly zero." Zero on every row. Two things follow:

1. **No holdover exposure on the Oct 1 rule.** That rule holds an account with its
   current owner only where the opp is at Proposal or beyond with CPQ sent and contact
   in the previous 60 days. Nothing in this book qualifies, so nothing is being held
   from Sairam under it and nothing of his is at risk under it. The open item in
   CLAUDE.md Section 14 can close.
2. **Nothing arrives warm.** There is no inherited pipeline at Proposal. The book is
   566 accounts and no live late-stage opportunity. That is what the fast start plan
   has to be built against.

### The 19 held to Feb 1, 2027

These are not held under the Proposal+ rule, since they have no Proposal+ opps. They
are held under the **FAC-in-the-last-24-months** rule: a rep keeps an account they have
a recent FAC on, and the opp has to reach QO by January or the account moves.

| Account | Held by | Status |
|---|---|---|
| Federal Home Loan Bank of San Francisco | Steve Platt | Prospect |
| Samba TV, Inc. | Josh Scott | **Winback** |
| On Lok, Inc. | Kevin Gharibizadeh | **Winback** |
| Irhythm Technologies, Inc. | Cameron McLean | Prospect |
| Human Interest Inc. | Shubhangi Mallik | Prospect |
| Glooko, Inc. | Lucas Duncan | Prospect |
| Backblaze, Inc. | Andrew Bell | Prospect |
| Yubico Inc. | Skeni Patel | Prospect |
| Vir Biotechnology, Inc. | Eric Witmer | Prospect |
| Burning Man Project | Andrew Bell | Prospect |
| Black Rock City LLC | Andrew Bell | Prospect |
| Exar Corporation | Kevin Gharibizadeh | Prospect |
| Maxlinear | Kevin Gharibizadeh | Prospect |
| Mode | Akshat Singh | Prospect |
| Enable | Abhishek Narayan | Prospect |
| Enable Benefits | Abhishek Narayan | Prospect |
| Jews for Jesus | Christopher Prassinos | Prospect |
| VODACOM GROUP LTD | Andrew Daigle | Prospect |
| KnowledgeStorm | Abhishek Narayan | **Winback** |

Andrew Bell holds three (Burning Man Project, Black Rock City LLC, Backblaze), and
Burning Man Project and Black Rock City LLC are the same organisation. Kevin
Gharibizadeh holds three, two of which (Exar, Maxlinear) are the same buying group.

### The date conflict is now material

The file says **Feb 1, 2027**. The deck body says Feb 1, 2027. The FAQ says **Jan 1,
2027**. Nineteen accounts and five months of prospecting time turn on which governs.
This was an academic open item before the list landed. It is now a concrete question
worth asking before Aug 19.

---

## 3. Duplicate records to merge

**24 clusters, 37 redundant records.** Detected on normalised legal name and on shared
LinkedIn company URL within the same account group. Shared LinkedIn URL is the strong
signal, since it means SFDC is pointing two records at one company page.

The recommended survivor is the Viable + California record in each cluster.

| Keep | Merge in | Records |
|---|---|---|
| AppDirect | AppDirecte Canada Inc, Microcorp LLC, Enterprise Jbilling Ltd | 4 |
| North American Title | + Company of Colorado, + Company Inc., + Company | 4 |
| Doma Holdings, Inc. | Doma, Doma, Doma Title Insurance Inc. | 4 |
| XYZ | xyz, XYZ, xyz | 4 |
| Achievers LLC | Achievers Llc, Achievers, Achievers Solutions Inc. | 4 |
| Wiser Solutions, Inc. | Wiser Solutions Inc. (dup), Wiser Inc | 3 |
| Kabam, Inc. | Kabam Games Inc, Kabam | 3 |
| Wag! Group Co. | Wag Labs Inc., Wag's | 3 |
| Affinity | Affinity (BC, different LinkedIn) | 2 |
| Securonix | Securonix (TX) | 2 |
| Jerry | Jerry (blank viability) | 2 |
| SRS Acquiom | SRS Acquiom Inc. (CO) | 2 |
| Vir Biotechnology, Inc. | Vir Biotechnology, Inc. (CO) | 2 |
| Go1 USA LLC | Go1 (MI) | 2 |
| Workstream | Workstream Inc. (OH) | 2 |
| Advantest Test Solutions | Advantest America R&D Center Inc | 2 |
| Proofpoint | Proofpoint, Inc. | 2 |
| California Casualty | California Casualty Management Company | 2 |
| Vodacom | VODACOM GROUP LTD | 2 |
| Enable | Enable (blank viability) | 2 |
| Eaze, Inc. | Eaze (blank viability) | 2 |
| North East Medical Services | North East Medical Services (2nd LinkedIn) | 2 |
| Mozilla Foundation | Mozilla Corporation | 2 |
| Juniper Square | Juniper Square Inc. (TX) | 2 |

**Two to verify rather than merge blind:**

- **Mozilla Foundation / Mozilla Corporation.** Genuinely two legal entities, the
  nonprofit parent and its taxable subsidiary. They share a LinkedIn page, which is why
  they clustered. Same decision unit in practice, but confirm before merging.
- **Doma / North American Title.** Both sit in the Title Resources Group account group,
  which holds 8 records in total. Title Resources Group acquired Doma's title business,
  so these are two dupe clusters inside one real buying group. Worth handling as one
  consolidation rather than two.

**Burning Man Project and Black Rock City LLC** are the same organisation but sit in
different account groups, so they did not cluster automatically. Both are held to Feb 1
by Andrew Bell. Flag as a merge.

---

## 4. Non-viable accounts

84 marked Non-Viable, plus 7 with the field blank.

**No account group is entirely non-viable.** Every single Non-Viable row has at least
one Viable sibling in its own account group. That means Non-Viable in this file is
almost never "this company is dead." It is "this record is redundant, or it is a
subsidiary shell of a company we already have."

Of the 84, **37 are duplicate records** handled in Section 3. The remaining **25 flagged
non-viable in the tracker** are genuine subsidiary or acquired-entity records inside a
group whose primary account is live: Traceable by Harness, Split, Qwiet, Armory,
Thycotic, Fastpath, AdColony, Fyber, Mobile Posse, Observeit, Socialware, and similar.

**Practical read: do not work them as accounts, but do not discard them either.** They
are acquisition history, and the acquired brand is often where a named IT contact still
sits. They belong in account mapping, not in the outreach list.

### The 7 blanks

Jerry, Go1, XYZ, Proofpoint, SF Chinese Hospital, Enable, Eaze. Six resolve through
duplicate merging. **SF Chinese Hospital is the one that does not** and needs the
viability field set. It is a real San Francisco hospital and a plausible in-book
account, so leaving it blank risks it being silently skipped.

---

## 5. Scope problems worth submitting as feedback

Only objective, material issues are eligible. These qualify.

### Routes out, unambiguous (3)

| Account | Should go to | Why |
|---|---|---|
| **Contra Costa Water District** | Andrew Daigle, SLED | California special district, local government |
| **Alameda County Water District** | Andrew Daigle, SLED | California special district, local government |
| **Port of San Francisco** | Andrew Daigle, SLED | Account group is "City and County of San Francisco, CA" |

Port of San Francisco is the cleanest single submission in the file. The account group
field names the city and county as the parent, so the classification is wrong on the
record's own data.

### Outside the territory entirely (4 viable)

| Account | Billing | Note |
|---|---|---|
| **Vodacom** | Gauteng, South Africa | Account group is Vodafone Group Plc. Enterprise telecom |
| **Implats** | Gauteng, South Africa | Impala Platinum Holdings. Enterprise mining |
| **Alef Education** | Abu Dhabi, UAE | Not North America |
| Go1 | Michigan | Australian company, resolves via merge to Go1 USA LLC (CA) |

Three viable accounts on two other continents in a California SMB book is a data issue,
not a judgement call.

### Likely enterprise buying groups (needs-ownership-check)

**98 viable accounts sit under a parent entity with a different name.** Most are fine,
a startup with a distant investor or a small acquisition. But per the F27 buying-group
test, an SMB-sized account inside a larger enterprise buying group stays with the LE
territory that owns that group, and these parents are large enough that the test should
be run before any outreach:

Nokia, Mitsubishi Electric, Mitsubishi HC Capital, Autodesk, CoStar Group, Corteva
Agriscience, KRAFTON, Netmarble, Informa PLC, Vodafone Group, Fortune Brands
Innovations, Embracer Group, Shueisha, Wesco International, Brookfield Properties,
Stillfront, Next 15 Group, Kahoot!, Nash Squared, RateGain, Bending Spoons, Coretronic,
Posiflex, UOL, Enero Group, Flos B&B Italia, Stingray Group, The Linux Foundation,
Cobham Satcom, Allspring Global Investments, Archdiocese of San Francisco, BETA Risk
Management Authority.

The affected accounts are marked `needs-ownership-check` in `data/accounts.csv` with the
parent named in `routed_to`. Use the `account-mapping` skill on these before working
them. The decisive question is shared IT leadership, not the existence of a parent.

Two worth calling out:

- **BETA Healthcare Group** under BETA Risk Management Authority. A JPA is a public
  entity, so this may be SLED rather than a buying-group question.
- **Catholic Charities SF** under Archdiocese of San Francisco. Whether the Archdiocese
  runs one IT decision unit across its agencies decides this one.

---

## 6. The gap this file does not close

**There is no revenue column.** The F27 SMB definition is $50-500M, and nothing in this
export lets that be tested. Account size misclassification is one of the five
feedback-eligible categories, and it cannot be checked against the only data available.

Two consequences:

1. Any submission about size has to be built account by account from outside sources.
   That is not realistic across 566 accounts before Aug 19.
2. There is no way to know how many of these fall under the $50M floor, which is also
   the segment where F27 does not say who owns them.

Worth asking for a revenue field on the territory dashboard rather than trying to
reconstruct it.

Also absent: **no contact data.** No named IT leaders, no titles. Under the tiering
framework, Power is a hard zero without a named contact, so nothing in this file can be
Tier 2 yet. The 38 winbacks are the only accounts with a real reason to be Tier 1 today.

---

## 7. Recommended feedback submission, by Aug 19

In priority order, all objective and all supported by the file's own data:

1. **Port of San Francisco** to SLED. Account group names City and County of San
   Francisco.
2. **Contra Costa Water District** and **Alameda County Water District** to SLED.
   California special districts.
3. **Vodacom, Implats, Alef Education** out of the book. South Africa and UAE, and
   Vodacom sits under Vodafone Group Plc.
4. **37 duplicate records** for merge, listed in Section 3. SFDC data issue.
5. **SF Chinese Hospital** viability field is blank.
6. **Burning Man Project / Black Rock City LLC** are one organisation across two
   account groups.
7. **Ask, do not submit:** which date governs the 19 holdovers, Feb 1 or Jan 1.
8. **Ask, do not submit:** can the territory dashboard expose annual revenue, since the
   $50-500M band cannot be verified without it.

Items 1 through 6 are data corrections with evidence in the export. Items 7 and 8 are
questions for the director, not feedback submissions.
