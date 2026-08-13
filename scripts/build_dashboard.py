#!/usr/bin/env python3
"""Build the book-of-business dashboard from the CSVs in data/.

Usage:
    python3 scripts/build_dashboard.py            # writes dashboard.html
    python3 scripts/build_dashboard.py --out X    # writes somewhere else
    python3 scripts/build_dashboard.py --today D  # pretend it is date D (YYYY-MM-DD)

Standard library only, no install step. The CSVs are the source of truth, this
file only renders them.
"""

import argparse
import csv
import datetime as dt
import html
import pathlib
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

QP_PARTS = ("vmd", "value", "power", "plan")
STAGE_ORDER = ["discovery", "fac", "proposal", "commit", "closed-won", "closed-lost"]
OPEN_STAGES = {"discovery", "fac", "proposal", "commit"}


# ---------------------------------------------------------------- loading


def load(name):
    """Read data/<name>.csv into a list of dicts. Missing file is not an error."""
    path = DATA / f"{name}.csv"
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        rows = [
            {(k or "").strip(): (v or "").strip() for k, v in row.items()}
            for row in csv.DictReader(fh)
        ]
    return [r for r in rows if any(r.values())]


def parse_date(value):
    try:
        return dt.date.fromisoformat(value)
    except (ValueError, TypeError):
        return None


def is_example(row):
    return any(v.startswith("EX") and v[2:3] in {"-", "C", "Y"} for v in row.values())


# ---------------------------------------------------------------- rendering helpers


def e(text):
    return html.escape(str(text or ""))


def days_label(delta):
    if delta < 0:
        n = abs(delta)
        return f"{n}d overdue" if n != 1 else "1d overdue"
    if delta == 0:
        return "today"
    if delta == 1:
        return "tomorrow"
    return f"in {delta}d"


def urgency(delta):
    if delta < 0:
        return "critical"
    if delta == 0:
        return "warn"
    if delta <= 7:
        return "soon"
    return "later"


# ---------------------------------------------------------------- panels


def panel_followups(outreach, accounts, contacts, today):
    """Open touches with a follow-up date, soonest first. The decaying work."""
    rows = []
    for r in outreach:
        if r.get("status", "open").lower() != "open":
            continue
        due = parse_date(r.get("next_followup_date"))
        if not due:
            continue
        delta = (due - today).days
        acct = accounts.get(r.get("account_id"), {})
        cont = contacts.get(r.get("contact_id"), {})
        rows.append(
            {
                "due": due,
                "delta": delta,
                "urgency": urgency(delta),
                "account": acct.get("account_name", r.get("account_id", "")),
                "tier": acct.get("tier", ""),
                "contact": cont.get("name", ""),
                "title": cont.get("title", ""),
                "campaign": r.get("campaign_type", ""),
                "touch": r.get("touch_number", ""),
                "outcome": r.get("outcome", ""),
                "note": r.get("subject_or_note", ""),
            }
        )
    rows.sort(key=lambda x: x["due"])

    if not rows:
        return empty_panel(
            "Follow-ups",
            "No open follow-ups scheduled. Add rows to data/outreach.csv with a "
            "next_followup_date and status of open.",
        )

    counts = Counter(r["urgency"] for r in rows)
    chips = "".join(
        f'<span class="chip chip--{k}">{counts[k]} {lbl}</span>'
        for k, lbl in (
            ("critical", "overdue"),
            ("warn", "due today"),
            ("soon", "this week"),
            ("later", "later"),
        )
        if counts.get(k)
    )

    body = "".join(
        f"""
        <li class="due due--{r['urgency']}">
          <div class="due__when">
            <span class="due__date">{e(r['due'].isoformat())}</span>
            <span class="due__rel">{e(days_label(r['delta']))}</span>
          </div>
          <div class="due__who">
            <span class="due__account">{e(r['account'])}{tier_pill(r['tier'])}</span>
            <span class="due__contact">{e(r['contact'])}{' · ' + e(r['title']) if r['title'] else ''}</span>
          </div>
          <div class="due__what">
            <span class="due__note">{e(r['note'])}</span>
            <span class="due__meta">{e(r['campaign'])} · touch {e(r['touch'])} · {e(r['outcome'])}</span>
          </div>
        </li>"""
        for r in rows
    )

    return f"""
    <section class="panel panel--wide" id="followups">
      <header class="panel__head">
        <h2>Follow-ups</h2>
        <div class="chips">{chips}</div>
      </header>
      <ul class="due-list">{body}</ul>
    </section>"""


def tier_pill(tier):
    if not tier:
        return ""
    return f'<span class="tier tier--{e(tier)}">T{e(tier)}</span>'


def panel_cycles(cycles, accounts, contacts, today):
    """Active opportunities with the QP bar. A hollow segment is a zero."""
    rows = [c for c in cycles if c.get("stage", "").lower() in OPEN_STAGES]
    if not rows:
        return empty_panel(
            "Active cycles",
            "No open cycles. Add rows to data/cycles.csv as discovery calls get booked.",
        )

    rows.sort(key=lambda c: STAGE_ORDER.index(c["stage"].lower()) if c.get("stage", "").lower() in STAGE_ORDER else 99)

    cards = []
    for c in rows:
        acct = accounts.get(c.get("account_id"), {})
        cont = contacts.get(c.get("contact_id"), {})

        segs, gaps = [], []
        for part in QP_PARTS:
            state = (c.get(part) or "no").lower()
            state = state if state in {"yes", "partial", "no"} else "no"
            if state != "yes":
                gaps.append(part.upper())
            segs.append(
                f'<span class="qp__seg qp__seg--{state}" title="{part.upper()}: {state}">'
                f'<span class="qp__label">{part.upper()}</span></span>'
            )
        qp_state = "blocked" if gaps else "built"

        nxt = parse_date(c.get("next_step_date"))
        if nxt:
            d = (nxt - today).days
            next_html = (
                f'<span class="cyc__next-date u-{urgency(d)}">{e(nxt.isoformat())}'
                f' <span class="cyc__rel">{e(days_label(d))}</span></span>'
            )
        else:
            next_html = '<span class="cyc__next-date u-critical">no date set</span>'

        verdict = (
            f'<p class="cyc__verdict cyc__verdict--blocked">QP blocked on '
            f'{e(", ".join(gaps))}. Multiplicative, so this is a zero, not a gap.</p>'
            if gaps
            else '<p class="cyc__verdict cyc__verdict--built">QP fully built. '
            "Proposal entry is open once OAT clears.</p>"
        )

        map_flag = (
            ""
            if (c.get("map_documented", "").lower() == "yes")
            else '<span class="flag">MAP not documented</span>'
        )

        aria = "QP components: " + ", ".join(
            f"{p.upper()} {c.get(p) or 'no'}" for p in QP_PARTS
        )

        cards.append(
            f"""
        <article class="cyc cyc--{qp_state}">
          <header class="cyc__head">
            <div>
              <h3>{e(acct.get('account_name', c.get('account_id', '')))}</h3>
              <p class="cyc__contact">{e(cont.get('name', ''))}{' · ' + e(cont.get('title', '')) if cont.get('title') else ''}</p>
            </div>
            <span class="stage stage--{e(c.get('stage', '').lower())}">{e(c.get('stage', ''))}</span>
          </header>
          <div class="qp" role="img" aria-label="{e(aria)}">{''.join(segs)}</div>
          {verdict}
          <dl class="cyc__meta">
            <div><dt>Next step</dt><dd>{e(c.get('next_step', 'not set'))}</dd></div>
            <div><dt>By</dt><dd>{next_html}</dd></div>
          </dl>
          {map_flag}
        </article>"""
        )

    return f"""
    <section class="panel panel--wide" id="cycles">
      <header class="panel__head">
        <h2>Active cycles</h2>
        <div class="chips"><span class="chip">{len(rows)} open</span></div>
      </header>
      <div class="cyc-grid">{''.join(cards)}</div>
    </section>"""


def panel_book(accounts_list):
    """Book composition: tier split and scope split."""
    in_book = [a for a in accounts_list if a.get("scope_status") == "in-book"]
    tiers = Counter(a.get("tier") or "untiered" for a in in_book)
    scope = Counter(a.get("scope_status") or "unset" for a in accounts_list)

    tier_defs = {
        "1": "Warm and active. Meet first.",
        "2": "Qualified with a hook. Attack list.",
        "3": "Cold whitespace. Build before you touch.",
        "untiered": "Not yet tiered.",
    }
    total = max(len(in_book), 1)
    bars = "".join(
        f"""
        <li class="bar">
          <div class="bar__top">
            <span class="bar__name">{'Tier ' + e(k) if k != 'untiered' else 'Untiered'}</span>
            <span class="bar__val">{tiers.get(k, 0)}</span>
          </div>
          <div class="bar__track"><span class="bar__fill bar__fill--t{e(k)}" style="width:{tiers.get(k, 0) / total * 100:.1f}%"></span></div>
          <p class="bar__note">{e(tier_defs[k])}</p>
        </li>"""
        for k in ("1", "2", "3", "untiered")
        if tiers.get(k)
    ) or '<li class="bar"><p class="bar__note">No in-book accounts loaded yet.</p></li>'

    routed = "".join(
        f'<li><span>{e(k)}</span><span class="mono">{v}</span></li>'
        for k, v in sorted(scope.items())
        if k != "in-book"
    ) or '<li><span>nothing routed out</span><span class="mono">0</span></li>'

    return f"""
    <section class="panel" id="book">
      <header class="panel__head"><h2>Book composition</h2>
        <div class="chips"><span class="chip">{len(in_book)} in book</span></div>
      </header>
      <ul class="bars">{bars}</ul>
      <h3 class="sub">Outside the book</h3>
      <ul class="kv">{routed}</ul>
    </section>"""


def panel_signals(signals, accounts, today):
    rows = sorted(
        (r for r in signals if parse_date(r.get("signal_date"))),
        key=lambda r: parse_date(r["signal_date"]),
        reverse=True,
    )[:12]
    if not rows:
        return empty_panel("Signals", "No signals logged. Add rows to data/signals.csv.")

    items = "".join(
        f"""
        <li class="sig{'' if r.get('actioned','').lower() == 'yes' else ' sig--open'}">
          <span class="sig__date mono">{e(r['signal_date'])}</span>
          <span class="sig__body">
            <span class="sig__type">{e(r.get('signal_type', ''))}</span>
            <span class="sig__acct">{e(accounts.get(r.get('account_id'), {}).get('account_name', r.get('account_id', '')))}</span>
            <span class="sig__detail">{e(r.get('detail', ''))}</span>
          </span>
          <span class="sig__flag">{'' if r.get('actioned','').lower() == 'yes' else 'unactioned'}</span>
        </li>"""
        for r in rows
    )
    unactioned = sum(1 for r in rows if r.get("actioned", "").lower() != "yes")
    chip = f'<span class="chip chip--warn">{unactioned} unactioned</span>' if unactioned else ""
    return f"""
    <section class="panel" id="signals">
      <header class="panel__head"><h2>Signals</h2><div class="chips">{chip}</div></header>
      <ul class="sig-list">{items}</ul>
    </section>"""


def panel_attention(accounts_list, cycles, outreach, today):
    """Things that are wrong right now, stated plainly."""
    issues = []

    needs_check = [a for a in accounts_list if a.get("scope_status") == "needs-ownership-check"]
    if needs_check:
        issues.append(
            (
                "critical",
                f"{len(needs_check)} account{'s' if len(needs_check) != 1 else ''} awaiting an ownership call",
                "Run the buying-group test before any work goes into them. "
                + ", ".join(a["account_name"] for a in needs_check[:3]),
            )
        )

    live = [a for a in accounts_list if a.get("membership_status", "").lower() == "live"]
    if live:
        issues.append(
            (
                "critical",
                f"{len(live)} account{'s' if len(live) != 1 else ''} carrying a live membership",
                "Membership guardrail: these come out of outreach entirely. Reclassify and hand off.",
            )
        )

    blocked = []
    for c in cycles:
        if c.get("stage", "").lower() not in OPEN_STAGES:
            continue
        if any((c.get(p) or "no").lower() != "yes" for p in QP_PARTS):
            blocked.append(c)
    power_blank = [c for c in blocked if (c.get("power") or "no").lower() != "yes"]
    if power_blank:
        issues.append(
            (
                "warn",
                f"Power unconfirmed on {len(power_blank)} of {len(blocked) or 1} open cycle"
                f"{'s' if len(power_blank) != 1 else ''}",
                "The habitual blank. Question bank is in reference/deal-stages.md.",
            )
        )

    no_date = [
        c
        for c in cycles
        if c.get("stage", "").lower() in OPEN_STAGES and not parse_date(c.get("next_step_date"))
    ]
    if no_date:
        issues.append(
            (
                "warn",
                f"{len(no_date)} open cycle{'s' if len(no_date) != 1 else ''} with no dated next step",
                "Every next step lands on a specific day. 'The week after' does not count as a close.",
            )
        )

    overdue = [
        r
        for r in outreach
        if r.get("status", "open").lower() == "open"
        and parse_date(r.get("next_followup_date"))
        and (parse_date(r["next_followup_date"]) - today).days < 0
    ]
    if overdue:
        issues.append(
            (
                "critical",
                f"{len(overdue)} follow-up{'s' if len(overdue) != 1 else ''} past due",
                "Listed in the follow-ups panel.",
            )
        )

    untiered = [
        a for a in accounts_list if a.get("scope_status") == "in-book" and not a.get("tier")
    ]
    if untiered:
        issues.append(
            (
                "soon",
                f"{len(untiered)} in-book account{'s' if len(untiered) != 1 else ''} untiered",
                "Tier with a written reason, not just a number.",
            )
        )

    if not issues:
        return """
    <section class="panel panel--wide panel--clear" id="attention">
      <header class="panel__head"><h2>Needs attention</h2></header>
      <p class="clear-note">Nothing flagged. No overdue follow-ups, no undated next steps,
      no unresolved ownership checks.</p>
    </section>"""

    items = "".join(
        f"""
        <li class="att att--{lvl}">
          <span class="att__title">{e(title)}</span>
          <span class="att__body">{e(body)}</span>
        </li>"""
        for lvl, title, body in issues
    )
    return f"""
    <section class="panel panel--wide" id="attention">
      <header class="panel__head"><h2>Needs attention</h2>
        <div class="chips"><span class="chip chip--critical">{len(issues)} flagged</span></div>
      </header>
      <ul class="att-list">{items}</ul>
    </section>"""


def empty_panel(title, note):
    return f"""
    <section class="panel">
      <header class="panel__head"><h2>{e(title)}</h2></header>
      <p class="empty">{e(note)}</p>
    </section>"""


# ---------------------------------------------------------------- page


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --ground:#FFFFFF; --surface:#F4F6F7; --surface-2:#EAEEF0; --line:#D8DFE3;
  --ink:#10171C; --ink-2:#3A4A55; --muted:#5C6B75;
  --accent:#0F6E7B; --accent-soft:#E3F0F1;
  --critical:#A8324A; --critical-soft:#F7E7EB;
  --warn:#9A6414; --warn-soft:#FAF0DF;
  --ok:#2F6B4F; --ok-soft:#E5F1EA;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  --r:3px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0E1418; --surface:#161E24; --surface-2:#1E282F; --line:#2C3941;
    --ink:#E8EEF1; --ink-2:#AFC0CA; --muted:#8399A6;
    --accent:#4FB3BF; --accent-soft:#123034;
    --critical:#E8879C; --critical-soft:#331A21;
    --warn:#D9A758; --warn-soft:#33270F;
    --ok:#7FC3A1; --ok-soft:#162C22;
  }
}
:root[data-theme="dark"]{
  --ground:#0E1418; --surface:#161E24; --surface-2:#1E282F; --line:#2C3941;
  --ink:#E8EEF1; --ink-2:#AFC0CA; --muted:#8399A6;
  --accent:#4FB3BF; --accent-soft:#123034;
  --critical:#E8879C; --critical-soft:#331A21;
  --warn:#D9A758; --warn-soft:#33270F;
  --ok:#7FC3A1; --ok-soft:#162C22;
}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}
.mono,.due__date,.bar__val,.sig__date,.cyc__next-date{font-family:var(--mono);
  font-variant-numeric:tabular-nums}
.wrap{max-width:1180px;margin:0 auto;padding:32px 24px 72px;
  display:flex;flex-direction:column;gap:24px}

/* masthead */
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;
  gap:16px;padding-bottom:20px;border-bottom:2px solid var(--ink)}
.mast h1{margin:0;font-size:26px;font-weight:640;letter-spacing:-.02em;text-wrap:balance}
.mast__sub{margin:6px 0 0;color:var(--muted);font-size:13.5px;max-width:62ch}
.mast__meta{text-align:right;font-family:var(--mono);font-size:12px;color:var(--muted);
  display:flex;flex-direction:column;gap:3px}
.mast__meta b{color:var(--ink);font-weight:600;font-size:14px}

/* counters */
.counts{display:grid;grid-template-columns:repeat(auto-fit,minmax(132px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.count{background:var(--surface);padding:14px 16px;display:flex;flex-direction:column;gap:3px}
.count__n{font-family:var(--mono);font-variant-numeric:tabular-nums;font-size:26px;
  font-weight:600;line-height:1;letter-spacing:-.03em}
.count__l{font-size:10.5px;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);font-weight:600}
.count--accent .count__n{color:var(--accent)}
.count--critical .count__n{color:var(--critical)}
.count--warn .count__n{color:var(--warn)}

/* panels */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:24px}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  padding:18px 20px 20px;display:flex;flex-direction:column;gap:14px;min-width:0}
.panel--wide{grid-column:1/-1}
.panel__head{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.panel__head h2{margin:0;font-size:12px;text-transform:uppercase;letter-spacing:.11em;
  font-weight:680;color:var(--ink-2)}
.sub{margin:6px 0 0;font-size:10.5px;text-transform:uppercase;letter-spacing:.1em;
  color:var(--muted);font-weight:650}
.empty,.clear-note{margin:0;color:var(--muted);font-size:13.5px;max-width:62ch}
.panel--clear{border-left:3px solid var(--ok)}

.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip{font-family:var(--mono);font-size:11px;padding:2.5px 8px;border-radius:999px;
  background:var(--surface-2);color:var(--ink-2);white-space:nowrap}
.chip--critical{background:var(--critical-soft);color:var(--critical);font-weight:600}
.chip--warn{background:var(--warn-soft);color:var(--warn);font-weight:600}
.chip--soon{background:var(--accent-soft);color:var(--accent);font-weight:600}

/* follow-ups */
.due-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.due{background:var(--surface);display:grid;
  grid-template-columns:minmax(120px,132px) minmax(180px,1.1fr) minmax(200px,1.5fr);
  gap:14px;padding:11px 14px 11px 15px;border-left:3px solid transparent;align-items:start}
.due--critical{border-left-color:var(--critical);background:var(--critical-soft)}
.due--warn{border-left-color:var(--warn);background:var(--warn-soft)}
.due--soon{border-left-color:var(--accent)}
.due--later{border-left-color:var(--line)}
.due__when,.due__who,.due__what{display:flex;flex-direction:column;gap:2px;min-width:0}
.due__date{font-size:13px;font-weight:600}
.due__rel{font-size:11px;color:var(--muted);font-family:var(--mono)}
.due--critical .due__rel{color:var(--critical);font-weight:600}
.due--warn .due__rel{color:var(--warn);font-weight:600}
.due__account{font-weight:600;font-size:13.5px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.due__contact,.due__meta{font-size:12px;color:var(--muted)}
.due__note{font-size:13px;color:var(--ink-2)}
.due__meta{font-family:var(--mono);font-size:11px}

.tier{font-family:var(--mono);font-size:10px;font-weight:700;padding:1px 5px;border-radius:2px;
  background:var(--surface-2);color:var(--ink-2)}
.tier--1{background:var(--critical-soft);color:var(--critical)}
.tier--2{background:var(--accent-soft);color:var(--accent)}
.tier--3{background:var(--surface-2);color:var(--muted)}

/* cycles */
.cyc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.cyc{background:var(--ground);border:1px solid var(--line);border-radius:var(--r);
  padding:14px 15px;display:flex;flex-direction:column;gap:11px;min-width:0}
.cyc--blocked{border-left:3px solid var(--critical)}
.cyc--built{border-left:3px solid var(--ok)}
.cyc__head{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}
.cyc__head h3{margin:0;font-size:14.5px;font-weight:640;letter-spacing:-.01em}
.cyc__contact{margin:2px 0 0;font-size:12px;color:var(--muted)}
.stage{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.06em;
  padding:2.5px 7px;border-radius:2px;background:var(--surface-2);color:var(--ink-2);
  white-space:nowrap;font-weight:650}
.stage--proposal,.stage--commit{background:var(--accent-soft);color:var(--accent)}

.qp{display:grid;grid-template-columns:repeat(4,1fr);gap:3px}
.qp__seg{height:26px;border-radius:2px;display:flex;align-items:center;justify-content:center;
  border:1px solid var(--line)}
.qp__label{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.05em}
.qp__seg--yes{background:var(--ok);border-color:var(--ok)}
.qp__seg--yes .qp__label{color:var(--ground)}
.qp__seg--partial{background:var(--warn-soft);border-color:var(--warn)}
.qp__seg--partial .qp__label{color:var(--warn)}
.qp__seg--no{background:transparent;border-style:dashed;border-color:var(--critical)}
.qp__seg--no .qp__label{color:var(--critical)}

.cyc__verdict{margin:0;font-size:12px;line-height:1.45}
.cyc__verdict--blocked{color:var(--critical);font-weight:550}
.cyc__verdict--built{color:var(--ok);font-weight:550}
.cyc__meta{margin:0;display:flex;flex-direction:column;gap:6px;
  border-top:1px solid var(--line);padding-top:10px}
.cyc__meta div{display:flex;gap:10px;justify-content:space-between;align-items:baseline}
.cyc__meta dt{font-size:10.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);
  font-weight:650;flex-shrink:0}
.cyc__meta dd{margin:0;font-size:12.5px;text-align:right;color:var(--ink-2)}
.cyc__next-date{font-size:12px}
.cyc__rel{color:var(--muted);font-size:11px}
.u-critical{color:var(--critical);font-weight:600}
.u-warn{color:var(--warn);font-weight:600}
.flag{align-self:flex-start;font-family:var(--mono);font-size:10.5px;padding:2px 7px;
  border-radius:2px;background:var(--warn-soft);color:var(--warn);font-weight:600}

/* bars */
.bars{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:13px}
.bar__top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px}
.bar__name{font-size:13px;font-weight:600}
.bar__val{font-size:14px;font-weight:650}
.bar__track{height:7px;background:var(--surface-2);border-radius:999px;overflow:hidden}
.bar__fill{display:block;height:100%;border-radius:999px;background:var(--accent)}
.bar__fill--t1{background:var(--critical)}
.bar__fill--t2{background:var(--accent)}
.bar__fill--t3{background:var(--muted)}
.bar__note{margin:5px 0 0;font-size:11.5px;color:var(--muted)}
.kv{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:5px}
.kv li{display:flex;justify-content:space-between;gap:12px;font-size:12.5px;
  padding-bottom:5px;border-bottom:1px solid var(--line);color:var(--ink-2)}
.kv li:last-child{border-bottom:0}

/* signals */
.sig-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.sig{display:grid;grid-template-columns:78px 1fr auto;gap:10px;align-items:start;
  padding-left:9px;border-left:2px solid var(--line);font-size:12.5px}
.sig--open{border-left-color:var(--warn)}
.sig__date{font-size:11px;color:var(--muted)}
.sig__body{display:flex;flex-direction:column;gap:1px;min-width:0}
.sig__type{font-family:var(--mono);font-size:10.5px;text-transform:uppercase;
  letter-spacing:.05em;color:var(--accent);font-weight:650}
.sig__acct{font-weight:600;font-size:12.5px}
.sig__detail{color:var(--muted);font-size:12px}
.sig__flag{font-family:var(--mono);font-size:10px;color:var(--warn);font-weight:650;
  text-transform:uppercase;letter-spacing:.05em}

/* attention */
.att-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.att{background:var(--surface);padding:11px 14px;border-left:3px solid var(--line);
  display:flex;flex-direction:column;gap:2px}
.att--critical{border-left-color:var(--critical)}
.att--warn{border-left-color:var(--warn)}
.att--soon{border-left-color:var(--accent)}
.att__title{font-weight:640;font-size:13.5px}
.att--critical .att__title{color:var(--critical)}
.att--warn .att__title{color:var(--warn)}
.att__body{font-size:12.5px;color:var(--muted)}

/* notices + footer */
.notice{border:1px dashed var(--warn);background:var(--warn-soft);color:var(--warn);
  border-radius:var(--r);padding:11px 14px;font-size:12.5px;font-weight:550}
.foot{border-top:1px solid var(--line);padding-top:16px;font-size:11.5px;color:var(--muted);
  display:flex;flex-wrap:wrap;gap:8px 22px}
.foot code{font-family:var(--mono);font-size:11px;background:var(--surface-2);
  padding:1px 5px;border-radius:2px;color:var(--ink-2)}
@media (max-width:760px){
  .due{grid-template-columns:1fr;gap:5px}
  .mast__meta{text-align:left}
  .sig{grid-template-columns:70px 1fr}
  .sig__flag{grid-column:2}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def build(today):
    accounts_list = load("accounts")
    contacts_list = load("contacts")
    outreach = load("outreach")
    cycles = load("cycles")
    signals = load("signals")

    accounts = {a["account_id"]: a for a in accounts_list if a.get("account_id")}
    contacts = {c["contact_id"]: c for c in contacts_list if c.get("contact_id")}

    in_book = [a for a in accounts_list if a.get("scope_status") == "in-book"]
    open_cycles = [c for c in cycles if c.get("stage", "").lower() in OPEN_STAGES]
    open_touches = [r for r in outreach if r.get("status", "open").lower() == "open"]
    overdue = sum(
        1
        for r in open_touches
        if parse_date(r.get("next_followup_date"))
        and (parse_date(r["next_followup_date"]) - today).days < 0
    )
    due_week = sum(
        1
        for r in open_touches
        if parse_date(r.get("next_followup_date"))
        and 0 <= (parse_date(r["next_followup_date"]) - today).days <= 7
    )
    qp_built = sum(
        1 for c in open_cycles if all((c.get(p) or "no").lower() == "yes" for p in QP_PARTS)
    )

    counts = [
        ("in book", len(in_book), ""),
        ("tier 1", sum(1 for a in in_book if a.get("tier") == "1"), "accent"),
        ("open cycles", len(open_cycles), ""),
        ("QP built", qp_built, "accent" if qp_built else ""),
        ("overdue", overdue, "critical" if overdue else ""),
        ("due in 7d", due_week, "warn" if due_week else ""),
    ]
    counts_html = "".join(
        f'<div class="count{" count--" + cls if cls else ""}">'
        f'<span class="count__n">{n}</span><span class="count__l">{e(label)}</span></div>'
        for label, n, cls in counts
    )

    n_examples = sum(
        1 for a in accounts_list if a.get("account_name", "").startswith("EXAMPLE")
    )
    notice = (
        f'<p class="notice">{n_examples} EXAMPLE rows are still in the CSVs. '
        f"They exist so this page renders before the territory list lands. "
        f"Delete them from every file in <code>data/</code> before working a real book.</p>"
        if n_examples
        else ""
    )

    return f"""<title>Territory Board</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class="wrap">
  <header class="mast">
    <div>
      <h1>Territory Board</h1>
      <p class="mast__sub">California 4 of 5 &middot; SMB, $50-500M, own decision unit.
      Follow-ups, active cycles, and account signals, read straight from the CSVs in
      <code>data/</code>.</p>
    </div>
    <div class="mast__meta">
      <b>{today.strftime('%d %b %Y')}</b>
      <span>{len(accounts_list)} accounts &middot; {len(contacts_list)} contacts</span>
      <span>{len(outreach)} touches logged</span>
    </div>
  </header>

  {notice}

  <div class="counts">{counts_html}</div>

  {panel_attention(accounts_list, cycles, outreach, today)}
  {panel_followups(outreach, accounts, contacts, today)}
  {panel_cycles(cycles, accounts, contacts, today)}

  <div class="grid">
    {panel_book(accounts_list)}
    {panel_signals(signals, accounts, today)}
  </div>

  <footer class="foot">
    <span>Source of truth: <code>data/*.csv</code></span>
    <span>Rebuild: <code>python3 scripts/build_dashboard.py</code></span>
    <span>Internal only. Intel firewall, CLAUDE.md Section 5.</span>
  </footer>
</div>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dashboard.html"))
    ap.add_argument("--today", default=None, help="override today, YYYY-MM-DD")
    args = ap.parse_args()

    today = parse_date(args.today) if args.today else dt.date.today()
    if today is None:
        sys.exit(f"bad --today value: {args.today}")

    out = pathlib.Path(args.out)
    out.write_text(build(today), encoding="utf-8")
    print(f"wrote {out} for {today.isoformat()}")


if __name__ == "__main__":
    main()
