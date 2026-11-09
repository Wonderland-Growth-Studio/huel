"""Build the DE keyword-expansion workbook.

Usage: python3 build_xlsx.py DATA_DIR OUT.xlsx
DATA_DIR holds the raw exports (de_kw_all.json, kw_perf.json, st_agg.json, shared_negs.json,
candidates.json) and dfs/ (DataforSEO responses). Missing DataforSEO volumes are fetched live.
"""
import base64, json, os, re, statistics, sys, urllib.request
from collections import defaultdict
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommendations import ROWS, NEGATIVES, EXCLUDED, COVERED  # noqa: E402

D, OUT = sys.argv[1], sys.argv[2]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def norm(s):
    s = s.lower().replace("ß", "ss")
    s = re.sub(r"[^a-z0-9äöü ]", " ", s)
    return " ".join(s.split())


def blocks(query, neg, mt):
    q, n = norm(query).split(), norm(neg).split()
    if not n:
        return False
    if mt == "EXACT":
        return q == n
    if mt == "PHRASE":
        return any(q[i:i + len(n)] == n for i in range(len(q) - len(n) + 1))
    return set(n) <= set(q)


# ---------- account data ----------
kw_all = json.load(open(f"{D}/de_kw_all.json"))["result"]
ag_negs = defaultdict(list)
active = defaultdict(set)  # norm kw -> {(campaign, ag, match)}
for r in kw_all:
    key = (r["campaign.name"], r["ad_group.name"])
    if r["ad_group_criterion.negative"]:
        ag_negs[key].append((r["ad_group_criterion.keyword.text"], r["ad_group_criterion.keyword.match_type"]))
    elif r["ad_group.status"] == "ENABLED" and r["ad_group_criterion.status"] == "ENABLED":
        active[norm(r["ad_group_criterion.keyword.text"])].add((r["campaign.name"], r["ad_group.name"], r["ad_group_criterion.keyword.match_type"]))

shared = json.load(open(f"{D}/shared_negs.json"))  # campaign -> [(text, match, list)]
st = {}
for k, v in json.load(open(f"{D}/st_agg.json")).items():  # sum spelling variants that normalise to one key (ß/ss etc.)
    a = st.setdefault(norm(k), [0, 0, 0, 0, v[4]])
    for i in range(4):
        a[i] += v[i]
cands = {r["kw"]: r for r in json.load(open(f"{D}/candidates.json"))}

# which keyword actually triggered each search term (search term x keyword segment export)
trig = defaultdict(lambda: defaultdict(int))
for r in json.load(open(f"{D}/st_kw.json"))["result"]:
    trig[norm(r["search_term_view.search_term"])][(r["ad_group.name"], r["segments.keyword.info.text"],
                                                   r["segments.keyword.info.match_type"].title())] += int(r["metrics.clicks"])


def matched_by(k):
    t = trig.get(norm(k))
    if not t:
        return "Not seen in DE search terms May-Nov (new reach)"
    tot = sum(t.values())
    top = sorted(t.items(), key=lambda x: -x[1])[:2]
    return "; ".join(f'{a} > "{kw}" [{mt}] {c / tot:.0%}' for (a, kw, mt), c in top)

# ---------- DataforSEO volumes ----------
vol_cache = f"{D}/dfs/search_volume_extra.json"
if os.path.exists(vol_cache):
    extra = json.load(open(vol_cache))
else:
    auth = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
    raw_need = sorted({r[0] for r in ROWS if norm(r[0]) not in cands} | {"travellunch"})
    req = urllib.request.Request("https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
                                 data=json.dumps([{"keywords": raw_need, "location_code": 2276, "language_code": "de"}]).encode(),
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    res = json.load(urllib.request.urlopen(req, timeout=180))
    extra = res["tasks"][0].get("result") or []
    json.dump(extra, open(vol_cache, "w"), ensure_ascii=False)
    print("search_volume cost", res["tasks"][0].get("cost"))
for it in extra:
    k = norm(it["keyword"])
    ms_raw = it.get("monthly_searches") or []
    ms = [m["search_volume"] or 0 for m in ms_raw][:12]
    cands.setdefault(k, {"kw": k, "sv": it.get("search_volume") or 0,
                         "sv_median": statistics.median(ms) if ms else (it.get("search_volume") or 0),
                         "cpc": it.get("cpc"), "bid_low": it.get("low_top_of_page_bid"),
                         "bid_high": it.get("high_top_of_page_bid"), "comp": it.get("competition"), "monthly": ms,
                         "monthly_raw": ms_raw})


def dfs(k):
    return cands.get(norm(k), {})


def peak(k):
    """Peak calendar month from the DataforSEO monthly series (most recent first)."""
    c = dfs(k)
    ms = c.get("monthly") or []
    if not ms or max(ms) == 0:
        return ""
    # DataforSEO series is newest first; index 0 = Sep 2026 (latest complete month at pull time)
    idx = ms.index(max(ms))
    return MONTHS[(8 - idx) % 12]


# ---------- workbook ----------
wb = Workbook()
HDR = PatternFill("solid", fgColor="1F3A5F")
HFONT = Font(color="FFFFFF", bold=True)
P_FILL = {"P1": "D9EAD3", "P2": "FFF2CC", "P3": "F4CCCC"}


def sheet(ws, headers, rows, widths):
    ws.append(headers)
    for c in ws[1]:
        c.fill, c.font = HDR, HFONT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for r in rows:
        ws.append(r)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions


# --- Keywords to add ---
ws = wb.active
ws.title = "Keywords to add"
rows, upload, conflicts = [], [], []
seen = set()
for kw, en, mts, camp, ag, prio, src, why in ROWS:
    n = norm(kw)
    assert (n, ag) not in seen, f"duplicate {kw} {ag}"
    seen.add((n, ag))
    c, s = dfs(kw), st.get(n)
    # is it already live somewhere (exact text)?
    live = sorted(f"{a} [{m[0]}]" for (cp, a, m) in active.get(n, set()) if cp == camp)
    # negative conflicts in the target ad group / campaign
    hits = []
    for t, m in ag_negs.get((camp, ag), []):
        if blocks(kw, t, m):
            hits.append(f'AG negative "{t}" [{m}]')
    for t, m, lst in shared.get(camp, []):
        if blocks(kw, t, m):
            hits.append(f'Shared list "{lst}": "{t}" [{m}]')
    conflict = "; ".join(hits) if hits else "None"
    if hits:
        conflicts.append((kw, ag, conflict))
    roas = round(s[3] / s[0], 2) if s and s[0] else None
    for mt in mts:
        rows.append([prio, camp, ag, "New ad group" if ag.startswith("NEW:") else "Existing (enabled)", kw, en, mt.title(),
                     src, int(c.get("sv_median") or 0) if c else None, c.get("sv") if c else None, peak(kw) if c else "",
                     c.get("cpc"), c.get("bid_low"), c.get("bid_high"), c.get("comp"),
                     round(s[0], 2) if s else None, s[1] if s else None, round(s[2], 1) if s else None,
                     roas, matched_by(kw) if src != "CONTROL" else "DE_SEARCH_BRAND via 'huel' broad/exact - figures in rationale", "; ".join(live) or "No", conflict, why])
        upload.append([camp, ag.replace("NEW: ", ""), kw, mt.title()])
sheet(ws, ["Priority", "Campaign", "Ad group", "Ad group status", "Keyword (DE)", "English translation", "Match type",
           "Source", "DFS volume / mo (12-mo median)", "DFS volume / mo (avg)", "Peak month", "DFS CPC (EUR)",
           "Top-of-page bid low (EUR)", "Top-of-page bid high (EUR)", "Competition",
           "Acct search-term cost May-Nov (EUR) - DE_SEARCH_GENERIC", "Acct clicks", "Acct conversions", "Acct ROAS", "Triggered today by (ad group > keyword, share of clicks)",
           "Already a keyword in target campaign?", "Negative-keyword conflict", "Rationale"],
      rows, [8, 20, 30, 16, 30, 30, 9, 10, 12, 11, 8, 9, 9, 9, 10, 12, 9, 10, 8, 44, 16, 22, 70])
for row in ws.iter_rows(min_row=2):
    row[0].fill = PatternFill("solid", fgColor=P_FILL[row[0].value])

# --- Editor upload ---
ws2 = wb.create_sheet("Google Ads Editor upload")
sheet(ws2, ["Campaign", "Ad group", "Keyword", "Criterion Type"], upload, [22, 40, 34, 14])

# --- Negatives ---
ws3 = wb.create_sheet("Negatives to add")
sheet(ws3, ["Negative keyword (DE)", "English translation", "Match type", "Apply to", "Why"],
      [list(n) for n in NEGATIVES], [24, 32, 10, 30, 80])

# --- Already covered ---
cov = []
for k, en in COVERED.items():
    s_ = st.get(norm(k))
    cov.append([k, en, int(dfs(k).get("sv_median") or 0) or None, round(s_[0], 2) if s_ else None,
                round(s_[2], 1) if s_ else None, round(s_[3] / s_[0], 2) if s_ and s_[0] else None, matched_by(k)])
wsc = wb.create_sheet("Already covered - no add")
sheet(wsc, ["Search term (DE)", "English translation", "DFS volume / mo (median)", "Cost May-Nov (EUR)", "Conv.", "ROAS",
            "Already triggered by (ad group > keyword, share of clicks)"], cov, [32, 30, 12, 12, 8, 8, 80])

# --- Excluded ---
ws4 = wb.create_sheet("Considered - not recommended")
sheet(ws4, ["Keyword / cluster (DE)", "English translation", "DFS volume / mo", "Why not"],
      [list(x) for x in EXCLUDED], [40, 40, 14, 90])

# --- Current keywords baseline ---
perf = json.load(open(f"{D}/kw_perf.json"))["result"]
agg = defaultdict(lambda: [0, 0, 0, 0, 0, None])
for r in perf:
    k = (r["campaign.name"], r["ad_group.name"], r["ad_group_criterion.keyword.text"].lower(), r["ad_group_criterion.keyword.match_type"])
    a = agg[k]
    a[0] += int(r["metrics.cost_micros"]) / 1e6
    a[1] += int(r["metrics.clicks"])
    a[2] += int(r["metrics.impressions"])
    a[3] += float(r["metrics.conversions"])
    a[4] += float(r["metrics.conversions_value"])
    a[5] = r.get("ad_group_criterion.quality_info.quality_score") or a[5]
base = []
for r in kw_all:
    if r["ad_group_criterion.negative"] or r["ad_group.status"] != "ENABLED" or r["ad_group_criterion.status"] != "ENABLED":
        continue
    k = (r["campaign.name"], r["ad_group.name"], r["ad_group_criterion.keyword.text"].lower(), r["ad_group_criterion.keyword.match_type"])
    a = agg.get(k, [0, 0, 0, 0, 0, None])
    base.append([k[0], k[1], r["ad_group_criterion.keyword.text"], k[3].title(), a[5], round(a[0], 2), a[1], a[2],
                 round(a[3], 1), round(a[4], 2), round(a[4] / a[0], 2) if a[0] else None,
                 round(a[0] / a[3], 2) if a[3] else None])
base.sort(key=lambda x: (x[0], x[1], -x[5]))
ws5 = wb.create_sheet("Current DE keywords")
sheet(ws5, ["Campaign", "Ad group", "Keyword", "Match type", "Quality Score", "Cost May-Nov (EUR)", "Clicks", "Impr.",
            "Conv.", "Conv. value (EUR)", "ROAS", "CPA (EUR)"], base, [20, 40, 34, 10, 8, 12, 9, 10, 9, 12, 8, 9])

# --- Ad group benchmarks ---
agb = defaultdict(lambda: [0, 0, 0, 0])
for k, a in agg.items():
    x = agb[(k[0], k[1])]
    x[0] += a[0]; x[1] += a[1]; x[2] += a[3]; x[3] += a[4]
live_ags = {(r["campaign.name"], r["ad_group.name"]) for r in kw_all if r["ad_group.status"] == "ENABLED"}
bench = [[c, a, "Enabled" if (c, a) in live_ags else "Paused", round(x[0], 2), x[1], round(x[2], 1), round(x[3], 2),
          round(x[3] / x[0], 2) if x[0] else None, round(x[0] / x[2], 2) if x[2] else None]
         for (c, a), x in sorted(agb.items(), key=lambda t: -t[1][0])]
ws6 = wb.create_sheet("Ad group benchmarks")
sheet(ws6, ["Campaign", "Ad group", "Status", "Cost May-Nov (EUR)", "Clicks", "Conv.", "Conv. value (EUR)", "ROAS", "CPA (EUR)"],
      bench, [20, 42, 10, 14, 10, 10, 14, 8, 10])

# --- Summary (first tab) ---
n_kw = len({(norm(r[0]), r[4]) for r in ROWS})
by_p = defaultdict(int)
for r in ROWS:
    by_p[r[5]] += 1
gen = [b for b in bench if b[0] == "DE_SEARCH_GENERIC"]
g_cost, g_val, g_conv = sum(b[3] for b in gen), sum(b[6] for b in gen), sum(b[5] for b in gen)
summary = [
    ["Huel EU (8046071519) - German Search keyword expansion", ""],
    ["Prepared", "2026-11-09. Account data: Google Ads API (Wonderland MCC), 1 May - 8 Nov 2026. Volumes: DataforSEO Google Ads data, Germany / German."],
    ["Scope", "DE_SEARCH_GENERIC (12 enabled ad groups, ~200 live keywords) and DE_SEARCH_BRAND (3 enabled ad groups). Targeting: Germany, German language. Shopping/PMax not in scope."],
    ["Benchmark", f"DE generic search May-Nov: EUR {g_cost:,.0f} spend, {g_conv:,.0f} conv, ROAS {g_val / g_cost:.2f}, CPA EUR {g_cost / g_conv:,.0f}. Outdoor Food (1.15), Competitors - Greens (1.05) and Meal replacement (1.00) lead; Competitors - Protein (0.45) and Bar (0.67) trail. Recommendations are judged against this ~1.0 ROAS bar, not against brand."],
    ["Method", "1) Pulled every keyword, negative and shared negative list on the DE campaigns. 2) Pulled 6 months of search terms (1,651 unique terms with 5+ clicks). 3) Ran DataforSEO keyword ideas for 9 seed themes that mirror the live ad groups (~21k ideas). 4) Kept only terms that either already convert in the account (HARVEST) or are close relatives of a live ad group's intent and Huel's products (ADJACENT). 5) Checked each against existing keywords and every negative that would block it."],
    ["What you get", f"{n_kw} keywords ({by_p['P1']} P1 / {by_p['P2']} P2 / {by_p['P3']} P3), 2 new ad groups (Competitors - Outdoor Food, Competitors - Diet Shakes), {len(NEGATIVES)} negatives that protect/route the new terms, {len(COVERED)} converting terms that need no keyword because an existing exact keyword already catches them, and {len(EXCLUDED)} clusters that look attractive in DataforSEO but should not be added."],
    ["Priorities", "P1 = add now (converting or direct sibling of a converting term). P2 = add next and watch for 2-3 weeks. P3 = test on a capped budget."],
    ["Match types", "Mostly Exact. The campaign already runs broad on every head term under Max Conversion Value, so a new keyword only earns its place if it (a) brings in a query we don't reach today (ADJACENT), or (b) moves a converting query off the wrong keyword/ad copy (e.g. 'prep my meal': 4,632 of 4,747 clicks via 'dinnerly' [B]; 'trek n eat': 564 of 567 via 'outdoor nahrung' [B]; 'proteinshake' via 'proteinpulver' [E]). Each harvested term was checked against the keyword that actually triggered it; terms already caught by an exact close variant in the right ad group are on the 'Already covered' tab, not in the add list. Phrase only where the modifier set is large (vegan trekking, healthy 5-minute terrine)."],
    ["Biggest wins", "1) Competitor routing: Prep My Meal (+alternative), This Is Food, Every Foods, Jimmy Joy Plenny Shake, Trek'n Eat and Adventure Food already convert (ROAS 1.1-2.3 on most) but are served by generic broad keywords with generic copy; two new competitor ad groups (Outdoor, Diet Shakes). 2) Outdoor: freeze-dried / vegan-trekking / tactical terms reached only via 'outdoor nahrung' broad - best-ROAS theme in DE. 3) Distinct high-volume terms served with the wrong copy ('proteinshake' 40k/mo via 'proteinpulver' [E]). 4) Converting terms that only exist in paused 'Old' ad groups (schnell zunehmen, proteinpulver ohne süßungsmittel/zucker, gesunde fertiggerichte). 5) Brand product exacts (Huel Lite: 45 conv with no keyword)."],
    ["Flag - brand agreement", "Competitors - Protein has 'proteinworks' [Broad] + [Exact] enabled (EUR 358 spend May-Nov). The 'Agreement with Brands Exclusion List' blocks 'protein works' / 'the protein works' as phrase, but the one-word spelling 'proteinworks' is not blocked. Check the agreement and pause these keywords / add 'proteinworks' to the list. 'myprotein' keywords are live too but are blocked by the list (no spend)."],
    ["Flag - Competitors - Protein", "ROAS 0.45 May-Nov ('esn' paused after EUR 3.4k at 0.37). No expansion recommended here."],
    ["Flag - AT/CH (out of scope)", "ROE_SEARCH_GENERIC targets Austria and Switzerland with English/French/Spanish/Dutch language settings only - German is not selected. German-speaking AT/CH searchers are only reached when Google infers another language. Worth a separate look (DE keyword set applied to AT/CH)."],
    ["Caveats", "DataforSEO volumes are Google Ads planner ranges and some ideas share a grouped volume (e.g. 'abnehmshakes' and 'zunehmshakes' both show 11k). Use the 12-month median column; 'camping food' etc. are very seasonal. Account ROAS on small search terms (<EUR 100) is directional only. Output is .xlsx (modern Excel); legacy .xls cannot hold this formatting."],
    ["Tabs", "Keywords to add | Google Ads Editor upload | Negatives to add | Already covered - no add | Considered - not recommended | Current DE keywords | Ad group benchmarks"],
]
if conflicts:
    summary.insert(6, ["Negative conflicts", "; ".join(f"{k} -> {a}: {c}" for k, a, c in conflicts)])
else:
    summary.insert(6, ["Negative conflicts", "None. Every recommended keyword was checked against its target ad group's negatives and the shared lists on its campaign."])
ws0 = wb.create_sheet("Summary", 0)
for r in summary:
    ws0.append(r)
ws0.column_dimensions["A"].width = 26
ws0.column_dimensions["B"].width = 150
ws0["A1"].font = Font(bold=True, size=14)
for row in ws0.iter_rows(min_row=2):
    row[0].font = Font(bold=True)
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")

wb.save(OUT)
print("saved", OUT, "| rows", len(rows), "| conflicts", conflicts)
