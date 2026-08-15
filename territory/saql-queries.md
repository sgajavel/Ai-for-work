# CRM Analytics SAQL queries, F27 territory

Dataset: `F27_Territories_v2`.

The base query is transcribed from a screenshot of Analytics Studio, so if a field name
errors on paste, check it against the dataset's field list rather than assuming the
query is wrong.

---

## 1. Base query, arrivals

This is the original, reformatted onto separate lines so the projection is editable.
Behaviour is identical.

```sql
q = load "F27_Territories_v2";
q = filter q by 'Scenario' == "Arrivals";
q = filter q by 'F27_Proposed_Terr.ID18' is not null;
q = filter q by 'Rep_Name' == "Sairam Gajavelli";
q = foreach q generate
      q.'F27_Proposed_Terr.ID18' as 'F27_Proposed_Terr.ID18',
      q.'Name' as 'Name',
      q.'Account_Group_IT__c' as 'Account_Group_IT__c',
      q.'Account_Status_IT_Picklist__c' as 'Account_Status_IT_Picklist__c',
      q.'Company_LinkedIn_URL__c' as 'Company_LinkedIn_URL__c',
      q.'BillingCountry' as 'BillingCountry',
      q.'BillingState' as 'BillingState',
      q.'Is_Viable_IT__c' as 'Is_Viable_IT__c',
      q.'F27_Proposed_Terr.Current_User.Name' as 'F27_Proposed_Terr.Current_User.Name',
      q.'F27_Proposed_Terr.Proposed_IT_Terr_Own.Name' as 'F27_Proposed_Terr.Proposed_IT_Terr_Own.Name',
      q.'F27_Proposed_Terr.Open_Opportunities_Proposal' as 'F27_Proposed_Terr.Open_Opportunities_Proposal',
      q.'F27_Proposed_Terr.Moving_Time_Frame' as 'F27_Proposed_Terr.Moving_Time_Frame',
      q.'F27_Proposed_Terr.Package_Territories_F27' as 'F27_Proposed_Terr.Package_Territories_F27',
      q.'User.Name' as 'User.Name';
q = limit q 25000;
```

Returns 699 rows.

---

## 2. Discover what values `Scenario` accepts

Worth running once. Dana's guide talks about Retained, Departures and Arrivals, so the
departures view is probably the same dataset with a different scenario value rather than
a separate report.

```sql
q = load "F27_Territories_v2";
q = filter q by 'Rep_Name' == "Sairam Gajavelli";
q = group q by 'Scenario';
q = foreach q generate q.'Scenario' as 'Scenario', count(q) as 'count';
```

---

## 3. Departures

Same as the base query with the scenario swapped. **The exact spelling is unconfirmed**,
so run query 2 first and use whatever it returns.

```sql
q = load "F27_Territories_v2";
q = filter q by 'Scenario' == "Departures";
q = filter q by 'Rep_Name' == "Sairam Gajavelli";
q = foreach q generate
      q.'F27_Proposed_Terr.ID18' as 'ID18',
      q.'Name' as 'Name',
      q.'Is_Viable_IT__c' as 'Is_Viable_IT__c',
      q.'Account_Status_IT_Picklist__c' as 'ITRG_Status',
      q.'F27_Proposed_Terr.Current_User.Name' as 'Current_Owner',
      q.'F27_Proposed_Terr.Proposed_IT_Terr_Own.Name' as 'Future_Owner',
      q.'F27_Proposed_Terr.Moving_Time_Frame' as 'Moving_Time_Frame',
      q.'F27_Proposed_Terr.Package_Territories_F27' as 'Package_Territories_F27';
q = limit q 25000;
```

This is where **Berje Inc** (`001f300001v97U9AAI`) lives, and it is the query that shows
who it is moving to, which is the blank on the feedback form row.

---

## 4. Viable only

Add one line to any query above. Confirm the picklist spelling first, it may be `Viable`
or `Yes`.

```sql
q = filter q by 'Is_Viable_IT__c' == "Viable";
```

Returns 608 on the arrivals set.

---

## 5. The February 1 holdovers

```sql
q = load "F27_Territories_v2";
q = filter q by 'Scenario' == "Arrivals";
q = filter q by 'Rep_Name' == "Sairam Gajavelli";
q = filter q by 'F27_Proposed_Terr.Moving_Time_Frame' == "Feb 1, 2027";
q = foreach q generate
      q.'Name' as 'Name',
      q.'Is_Viable_IT__c' as 'Is_Viable_IT__c',
      q.'Account_Status_IT_Picklist__c' as 'ITRG_Status',
      q.'F27_Proposed_Terr.Current_User.Name' as 'Held_By',
      q.'F27_Proposed_Terr.Open_Opportunities_Proposal' as 'Open_Opps_Proposal_Plus';
q = limit q 100;
```

Returns 19 rows. These are the accounts the feedback rows were filed against.

---

## 6. Field discovery

Drop the `foreach` and the results panel shows every column the dataset carries. Use this
before assuming a field is absent.

```sql
q = load "F27_Territories_v2";
q = filter q by 'Rep_Name' == "Sairam Gajavelli";
q = limit q 10;
```

---

## What this dataset cannot do

It carries exactly one opportunity field,
`F27_Proposed_Terr.Open_Opportunities_Proposal`, which counts **open** opportunities at
Proposal stage or beyond and reads `0` on all 699 rows. There is no stage, no close date
and no opportunity name.

So closed-lost, closed-won, and anything sitting at Discovery or Qualification are all
invisible here regardless of how the filter is written. Those need a standard Salesforce
report against the Opportunity object, covered in `territory/salesforce-report-setup.md`.
