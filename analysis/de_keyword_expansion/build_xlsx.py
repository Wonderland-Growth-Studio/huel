"""Build the DE keyword-expansion workbook.

Usage: python3 build_xlsx.py DATA_DIR OUT.xlsx
DATA_DIR holds the raw exports (de_kw_all.json, kw_perf.json, st_agg.json, shared_negs.json,
candidates.json) and dfs/ (DataforSEO responses). Missing DataforSEO volumes are fetched live.
"""
import base64, json, os, re, statistics, sys, urllib.request
from collections import defaultdict
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommendations import ROWS, NEGATIVES, EXCLUDED, COVERED  # noqa: E402
from readable_why import WHY  # noqa: E402

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
ws.title = "Full data (analyst)"
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

# --- Readable add list, grouped by ad group ---
missing = [r[0] for r in ROWS if r[0] not in WHY]
assert not missing, f"no plain-English why for {missing}"
THIN = Side(style="thin", color="D9D9D9")
P_LABEL = {"P1": "1 - Add now", "P2": "2 - Add next", "P3": "3 - Test"}


def results(k):
    s_ = st.get(norm(k))
    if not s_ or s_[0] < 1:
        return "Not searched yet - new reach"
    n = round(s_[2])
    conv = (f"{n} conversion" + ("s" if n != 1 else "")) if s_[2] >= 1 else ("<1 conversion" if s_[2] > 0 else "0 conversions")
    roas = f"ROAS {s_[3] / s_[0]:.1f}" if s_[2] > 0 else "no return yet"
    return f"{conv} · {roas} · €{s_[0]:,.0f} spent"


def brand_results(why_full):
    m = re.search(r"([\d.]+) conv", why_full)
    return f"{float(m.group(1)):.0f} conversions via the 'huel' keyword" if m else "Served via 'huel' keyword"


_agx = defaultdict(lambda: [0.0, 0.0])
for _r in json.load(open(f"{D}/kw_perf.json"))["result"]:
    _x = _agx[(_r["campaign.name"], _r["ad_group.name"])]
    _x[0] += int(_r["metrics.cost_micros"]) / 1e6
    _x[1] += float(_r["metrics.conversions_value"])
AG_ROAS = {k: v[1] / v[0] for k, v in _agx.items() if v[0]}
ORDER, groups = [], defaultdict(list)
for kw, en, mts, camp, ag, prio, src, why in ROWS:
    if (camp, ag) not in groups:
        ORDER.append((camp, ag))
    groups[(camp, ag)].append((prio, kw, en, mts, src, why))

wr = wb.create_sheet("Keywords to add", 0)
wr.sheet_properties.tabColor = "1F3A5F"
heads = ["Priority", "German keyword", "English meaning", "Match type", "Searches / month", "Results so far (May-Nov)", "Why add it"]
widths = [14, 32, 36, 15, 12, 32, 78]
wr.append(["Keywords to add - Huel EU, German Search"])
wr["A1"].font = Font(bold=True, size=14, color="1F3A5F")
wr.append(["Grouped by where each keyword goes. Priority 1 = add now, 2 = add next and watch for 2-3 weeks, 3 = test on a small budget. "
           "'Searches / month' = DataforSEO, Germany, 12-month median. 'Results so far' = what that exact search already did in our account."])
wr.merge_cells("A2:G2")
wr["A2"].alignment = Alignment(wrap_text=True, vertical="top")
wr["A2"].font = Font(italic=True, color="595959")
wr.row_dimensions[2].height = 32
wr.append([])
wr.append(heads)
for c in wr[4]:
    c.fill, c.font = HDR, HFONT
    c.alignment = Alignment(wrap_text=True, vertical="center")
for i, w in enumerate(widths, 1):
    wr.column_dimensions[get_column_letter(i)].width = w
wr.freeze_panes = "A5"

for camp, ag in ORDER:
    items = sorted(groups[(camp, ag)], key=lambda x: (x[0], -(int(dfs(x[1]).get("sv_median") or 0))))
    is_new = ag.startswith("NEW:")
    name = ag.replace("NEW: ", "")
    if is_new:
        note = "NEW ad group - create it"
    else:
        b = AG_ROAS.get((camp, ag))
        note = f"existing ad group · ROAS {b:.2f} May-Nov" if b else "existing ad group"
    wr.append([])
    wr.append([f"{name}   ({camp})   -   {note}   -   {len(items)} keyword{'s' if len(items) > 1 else ''}"])
    r = wr.max_row
    wr.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    cell = wr.cell(r, 1)
    cell.font = Font(bold=True, size=12, color="1F3A5F" if not is_new else "7F3F00")
    cell.fill = PatternFill("solid", fgColor="DCE6F1" if not is_new else "FCE4D6")
    wr.row_dimensions[r].height = 20
    for prio, kw, en, mts, src, why in items:
        vol = int(dfs(kw).get("sv_median") or 0) or None
        res = brand_results(why) if src == "CONTROL" else results(kw)
        wr.append([P_LABEL[prio], kw, en, " + ".join(m.title() for m in mts), vol, res, WHY[kw]])
        rr = wr.max_row
        for c in wr[rr]:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=THIN)
        wr.cell(rr, 1).fill = PatternFill("solid", fgColor=P_FILL[prio])
        wr.cell(rr, 1).font = Font(bold=True)
        wr.cell(rr, 2).font = Font(bold=True)
        wr.cell(rr, 5).number_format = "#,##0"
        wr.cell(rr, 5).alignment = Alignment(horizontal="center", vertical="top")
wr.page_setup.orientation = "landscape"
wr.page_setup.fitToWidth = 1
wr.page_setup.fitToHeight = 0
wr.sheet_properties.pageSetUpPr.fitToPage = True

# --- Editor upload ---
ws2 = wb.create_sheet("Google Ads Editor upload")
sheet(ws2, ["Campaign", "Ad group", "Keyword", "Criterion Type"], upload, [22, 40, 34, 14])

# --- Negatives ---
ws3 = wb.create_sheet("Negatives to add")
sheet(ws3, ["Negative keyword (German)", "English meaning", "Match type", "Add it to", "Why"],
      [[n[0], n[1], n[2].title(), n[3], n[4]] for n in NEGATIVES], [24, 30, 11, 30, 80])

# --- Already covered ---
cov = []
for k, en in COVERED.items():
    s_ = st.get(norm(k))
    t = trig.get(norm(k), {})
    top = max(t.items(), key=lambda x: x[1])[0] if t else None
    caught = f'"{top[1]}" ({top[2].lower()}) in {top[0]}' if top else ""
    cov.append([k, en, results(k), caught])
wsc = wb.create_sheet("Already covered - no add")
sheet(wsc, ["Search term (German)", "English meaning", "Results so far (May-Nov)", "Already caught by existing keyword"],
      cov, [30, 30, 32, 60])

# --- Excluded ---
ws4 = wb.create_sheet("Considered - not recommended")
sheet(ws4, ["Keyword / cluster (German)", "English meaning", "Searches / month", "Why not"],
      [list(x) for x in EXCLUDED], [38, 36, 14, 90])

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
ws0 = wb.create_sheet("Summary", 0)
ws0.sheet_properties.tabColor = "1F3A5F"
ws0.sheet_view.showGridLines = False
for col, w in zip("ABCDEFG", [4, 44, 30, 10, 10, 10, 12]):
    ws0.column_dimensions[col].width = w
SEC = Font(bold=True, size=12, color="1F3A5F")


def line(text, font=None, indent=True, height=None):
    ws0.append(["", text] if indent else [text])
    r = ws0.max_row
    c = ws0.cell(r, 2 if indent else 1)
    ws0.merge_cells(start_row=r, start_column=2 if indent else 1, end_row=r, end_column=7)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if font:
        c.font = font
    if height:
        ws0.row_dimensions[r].height = height


line("Huel EU - German Search keyword expansion", Font(bold=True, size=16, color="1F3A5F"), indent=False, height=24)
line("Prepared 9 Nov 2026 · account data 1 May - 8 Nov 2026 · search volumes from DataforSEO (Germany, German)",
     Font(italic=True, color="595959"), indent=False)
ws0.append([])
line("In one sentence", SEC, indent=False)
line(f"Add {n_kw} keywords ({by_p['P1']} now, {by_p['P2']} next, {by_p['P3']} as tests) to the German Search campaigns, "
     f"create 2 new competitor ad groups, and add {len(NEGATIVES)} negatives. Most of these searches already convert in the account "
     f"but are caught by the wrong keyword and shown the wrong ad; the rest are new, closely related searches.", height=48)
ws0.append([])
line("Where the keywords go", SEC, indent=False)
ws0.append(["", "Ad group", "Campaign", "Add now", "Add next", "Test", "Total"])
hr = ws0.max_row
for c in ws0[hr][1:]:
    c.fill, c.font = HDR, HFONT
for camp, ag in ORDER:
    cnt = defaultdict(int)
    for it in groups[(camp, ag)]:
        cnt[it[0]] += 1
    ws0.append(["", ag.replace("NEW: ", "") + ("  (new)" if ag.startswith("NEW:") else ""), camp,
                cnt["P1"] or "", cnt["P2"] or "", cnt["P3"] or "", sum(cnt.values())])
    for c in ws0[ws0.max_row][1:]:
        c.border = Border(bottom=THIN)
    for col in (4, 5, 6, 7):
        ws0.cell(ws0.max_row, col).alignment = Alignment(horizontal="center")
ws0.append(["", "Total", "", by_p["P1"], by_p["P2"], by_p["P3"], n_kw])
for c in ws0[ws0.max_row][1:]:
    c.font = Font(bold=True)
    if c.column > 3:
        c.alignment = Alignment(horizontal="center")
ws0.append([])
line("Biggest opportunities", SEC, indent=False)
for t in [
    "1.  Competitor searches already converting but shown generic ads - Prep My Meal (45 conversions, no keyword of its own), "
    "This Is Food, Every Foods, Jimmy Joy, Trek'n Eat, Adventure Food. Give them their own keywords and comparison ads.",
    "2.  Outdoor is the best-returning theme in Germany (ROAS 1.15). Freeze-dried, vegan-trekking and tactical-food searches "
    "only reach us through one broad keyword today.",
    "3.  'proteinshake' (40k searches/month) is being shown protein-powder ads. Give it its own keyword and shake copy.",
    "4.  Several converting searches only exist in paused 'Old' ad groups (e.g. 'schnell zunehmen', 'gesunde fertiggerichte').",
    "5.  Brand: 'huel lite' drove 45 conversions with no product keyword or product landing page.",
]:
    line(t, height=32)
ws0.append([])
line("How the list was built", SEC, indent=False)
line(f"Benchmark: German generic search returned ROAS {g_val / g_cost:.2f} (CPA €{g_cost / g_conv:,.0f}) over May-Nov, so every "
     "keyword is judged against roughly 1.0, not against brand. Sources: every keyword, negative and search term in the German "
     "campaigns, plus ~21k DataforSEO keyword ideas. Each keyword was checked against existing keywords and all negatives "
     "(no conflicts). Searches that an existing exact keyword already catches are listed separately and not added.", height=62)
ws0.append([])
line("Worth a look (outside this request)", SEC, indent=False)
for t in [
    "Possible brand-agreement issue: 'proteinworks' (one word) is live in Competitors - Protein and spent €358. "
    "The agreement list only blocks 'protein works' as two words.",
    "Competitors - Protein returns ROAS 0.45 - no expansion recommended there.",
    "Austria and Switzerland: the rest-of-Europe generic campaign doesn't target the German language, so German-speaking "
    "searchers there are largely missed.",
]:
    line("•  " + t, height=32)
ws0.append([])
line("Tabs in this file", SEC, indent=False)
for t in [
    "Keywords to add - the list, grouped by ad group, with English meaning and a one-line reason",
    "Negatives to add - keeps the new keywords clean and routes competitor searches to the right ad group",
    "Already covered / Not recommended - converting or tempting searches we deliberately did not add, and why",
    "Google Ads Editor upload - ready to paste",
    "Full data, Current DE keywords, Ad group benchmarks - the underlying numbers",
]:
    line("•  " + t)

order = ["Summary", "Keywords to add", "Negatives to add", "Already covered - no add", "Considered - not recommended",
         "Google Ads Editor upload", "Full data (analyst)", "Current DE keywords", "Ad group benchmarks"]
wb._sheets = [wb[n] for n in order]
for n in order[5:]:
    wb[n].sheet_properties.tabColor = "BFBFBF"
wb.active = 0
wb.save(OUT)
print("saved", OUT, "| rows", len(rows), "| conflicts", conflicts)
