"""Build the v2 workbook: closest-match additions per ad group, checked against each landing page.

Usage: python3 build_xlsx_v2.py DATA_DIR OLD_WORKBOOK.xlsx OUT.xlsx
(OLD_WORKBOOK supplies the unchanged reference tabs: Already covered, Current DE keywords, Ad group benchmarks.)
"""
import json, re, sys
from collections import defaultdict
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
from recommendations_v2 import AD_GROUPS, ROWS, LP_FIXES, DROPPED  # noqa: E402
from recommendations import NEGATIVES  # noqa: E402

D, OLD, OUT = sys.argv[1:4]


def norm(s):
    s = s.lower().replace("ß", "ss")
    s = re.sub(r"[^a-z0-9äöü ]", " ", s)
    return " ".join(s.split())


vol = json.load(open(f"{D}/vol_v2.json"))
st = {}
for k, v in json.load(open(f"{D}/st_agg.json")).items():
    a = st.setdefault(norm(k), [0, 0, 0, 0])
    for i in range(4):
        a[i] += v[i]
agx = defaultdict(lambda: [0.0, 0.0])
for r in json.load(open(f"{D}/kw_perf.json"))["result"]:
    x = agx[r["ad_group.name"]]
    x[0] += int(r["metrics.cost_micros"]) / 1e6
    x[1] += float(r["metrics.conversions_value"])
AG_ROAS = {k: v[1] / v[0] for k, v in agx.items() if v[0]}


def results(k, ag):
    if AD_GROUPS[ag][0] == "DE_SEARCH_BRAND":
        return "Served via 'huel' broad today"
    s = st.get(norm(k))
    if not s or s[0] < 1:
        return "Not seen in account yet"
    n = round(s[2])
    conv = (f"{n} conversion" + ("s" if n != 1 else "")) if s[2] >= 1 else ("<1 conversion" if s[2] > 0 else "0 conversions")
    roas = f"ROAS {s[3] / s[0]:.1f}" if s[2] > 0 else "no return yet"
    return f"{conv} · {roas} · €{s[0]:,.0f}"


NAVY, NAVY_T = "1F3A5F", "DCE6F1"
HDR, HFONT = PatternFill("solid", fgColor=NAVY), Font(color="FFFFFF", bold=True)
THIN = Side(style="thin", color="D9D9D9")
P_FILL = {"P1": "D9EAD3", "P2": "FFF2CC", "P3": "F4CCCC"}
P_LABEL = {"P1": "1 - Add now", "P2": "2 - Add next", "P3": "3 - Test"}
wb = Workbook()


def table(ws, headers, rows, widths, start=1):
    ws.append(headers)
    for c in ws[ws.max_row]:
        c.fill, c.font = HDR, HFONT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for r in rows:
        ws.append(r)
        for c in ws[ws.max_row]:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=THIN)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(start + 1, 1)


def banner(ws, text, ncol, fill=NAVY_T, color=NAVY, size=12, italic=False, height=None, bold=True):
    ws.append([text])
    r = ws.max_row
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncol)
    c = ws.cell(r, 1)
    c.font = Font(bold=bold, size=size, color=color, italic=italic)
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    c.alignment = Alignment(wrap_text=True, vertical="center")
    if height:
        ws.row_dimensions[r].height = height


# ---------------- Keywords by ad group ----------------
wk = wb.active
wk.title = "Keywords by ad group"
NC = 7
heads = ["Priority", "German keyword", "English meaning", "Searches / month", "Closest existing keyword",
         "What on the landing page supports it", "Results so far (May-Nov)"]
widths = [13, 32, 32, 11, 24, 52, 30]
banner(wk, "Keywords to add - by ad group, checked against each landing page", NC, fill=None, size=15)
banner(wk, "Each keyword is the closest variant of a keyword the ad group already runs, and only uses words the landing page "
           "backs up. All Exact match unless marked (phrase). Searches = DataforSEO, Germany. Results = what that search already "
           "did in our account.", NC, fill=None, color="595959", size=10, italic=True, height=30, bold=False)
wk.append([])
wk.append(heads)
for c in wk[wk.max_row]:
    c.fill, c.font = HDR, HFONT
    c.alignment = Alignment(wrap_text=True, vertical="center")
for i, w in enumerate(widths, 1):
    wk.column_dimensions[get_column_letter(i)].width = w
wk.freeze_panes = "A5"

groups, order = defaultdict(list), []
for row in ROWS:
    if row[3] not in groups:
        order.append(row[3])
    groups[row[3]].append(row)
for ag in order:
    camp, lp, page, status = AD_GROUPS[ag]
    name = ag.replace("NEW: ", "")
    roas = AG_ROAS.get(ag)
    tag = "NEW ad group - create it" if status == "new" else (f"ROAS {roas:.2f} May-Nov" if roas else "existing")
    wk.append([])
    banner(wk, f"{name}   ·   {tag}   ·   {len(groups[ag])} keyword{'s' if len(groups[ag]) > 1 else ''}", NC,
           fill="FCE4D6" if status == "new" else NAVY_T, color="7F3F00" if status == "new" else NAVY, height=20)
    banner(wk, f"Landing page: {lp}  -  {page}", NC, fill="F2F2F2", color="404040", size=9, italic=True, bold=False, height=28)
    for kw, en, mt, _, prio, closest, proof, why in sorted(groups[ag], key=lambda x: (x[4], -vol.get(norm(x[0]), 0))):
        label = kw + ("  (phrase)" if mt == "Phrase" else "")
        wk.append([P_LABEL[prio], label, en, vol.get(norm(kw)) or None, closest, proof, results(kw, ag)])
        r = wk.max_row
        for c in wk[r]:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=THIN)
        wk.cell(r, 1).fill = PatternFill("solid", fgColor=P_FILL[prio])
        wk.cell(r, 1).font = Font(bold=True)
        wk.cell(r, 2).font = Font(bold=True)
        wk.cell(r, 4).number_format = "#,##0"
        wk.cell(r, 4).alignment = Alignment(horizontal="center", vertical="top")
        wk.cell(r, 5).font = Font(color="595959")

# ---------------- Landing-page fixes ----------------
wf = wb.create_sheet("Landing-page fixes")
banner(wf, "Existing keywords that land on the wrong page", 5, fill=None, size=14)
banner(wf, "Found while checking each ad group's landing page. Results are May-Nov 2026.", 5, fill=None, color="595959",
       size=10, italic=True, bold=False)
wf.append([])
table(wf, ["Keyword(s)", "Ad group", "Lands on", "Results so far", "What to do"], [list(x) for x in LP_FIXES],
      [34, 28, 24, 34, 70], start=4)

# ---------------- Dropped after LP check ----------------
wd = wb.create_sheet("Dropped after page check")
banner(wd, "Removed from the earlier list because the landing page doesn't back them up", 3, fill=None, size=14)
wd.append([])
table(wd, ["Keyword(s)", "English meaning", "Why dropped"], [list(x) for x in DROPPED], [44, 34, 80], start=3)

# ---------------- Negatives ----------------
keep_ags = set(AD_GROUPS)
neg_rows = [[n[0], n[1], n[2].title(), n[3], n[4]] for n in NEGATIVES if n[0] not in ("onek", "prep meal")]
neg_rows += [["yfood", "yfood (brand)", "Phrase", "Competitors - Meal Replacement & Delivery",
              "Route yfood searches to the new Competitors - Meal Shakes ad group (Black Edition page)."],
             ["jimmy joy", "Jimmy Joy (brand)", "Phrase", "Competitors - Meal Replacement & Delivery", "As above."],
             ["soylent", "Soylent (brand)", "Phrase", "Competitors - Meal Replacement & Delivery", "As above (once moved)."]]
wn = wb.create_sheet("Negatives to add")
table(wn, ["Negative keyword (German)", "English meaning", "Match type", "Add it to", "Why"], neg_rows, [24, 28, 11, 34, 80])

# ---------------- Editor upload ----------------
FINAL = {"Products (Exact)": {"huel complete protein": AD_GROUPS["Protein"][1], "huel riegel": AD_GROUPS["Bar"][1],
                              "huel ramen": AD_GROUPS["Ready Meals"][1]}}
up = []
for kw, en, mt, ag, prio, *_ in ROWS:
    camp, lp, _, status = AD_GROUPS[ag]
    url = FINAL.get(ag, {}).get(kw, "")
    if ag == "Products (Exact)" and not url:
        url = "<set to product page>"
    elif status == "new":
        url = "https://" + lp
    up.append([camp, ag.replace("NEW: ", ""), kw, mt, P_LABEL[prio], ("https://" + url) if url.startswith("de.") else url])
we = wb.create_sheet("Google Ads Editor upload")
table(we, ["Campaign", "Ad group", "Keyword", "Criterion Type", "Priority", "Final URL (only where it must differ)"], up,
      [22, 40, 34, 12, 13, 58])

# ---------------- Full data ----------------
full = []
for kw, en, mt, ag, prio, closest, proof, why in ROWS:
    s = st.get(norm(kw))
    full.append([prio, AD_GROUPS[ag][0], ag, AD_GROUPS[ag][1], kw, en, mt, vol.get(norm(kw)), closest, proof,
                 round(s[0], 2) if s else None, round(s[2], 1) if s else None,
                 round(s[3] / s[0], 2) if s and s[0] else None, why])
wfull = wb.create_sheet("Full data (analyst)")
table(wfull, ["Priority", "Campaign", "Ad group", "Landing page", "Keyword", "English", "Match", "Searches / mo",
              "Closest existing keyword", "Landing-page support", "Search-term cost (EUR)", "Conv.", "ROAS", "Why"],
      full, [8, 20, 30, 40, 30, 28, 8, 10, 22, 44, 10, 8, 8, 60])
wfull.auto_filter.ref = wfull.dimensions

# ---------------- Reference tabs copied from v1 ----------------
old = load_workbook(OLD)
for name in ["Already covered - no add", "Considered - not recommended", "Current DE keywords", "Ad group benchmarks"]:
    src, dst = old[name], wb.create_sheet(name)
    for row in src.iter_rows(values_only=True):
        dst.append(list(row))
    for col, dim in src.column_dimensions.items():
        dst.column_dimensions[col].width = dim.width
    for c in dst[1]:
        c.fill, c.font = HDR, HFONT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for row in dst.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    dst.freeze_panes = "A2"

# ---------------- Summary ----------------
ws = wb.create_sheet("Summary", 0)
ws.sheet_view.showGridLines = False
for col, w in zip("ABCDEFGH", [3, 40, 44, 10, 10, 8, 8, 8]):
    ws.column_dimensions[col].width = w
SEC = Font(bold=True, size=12, color=NAVY)


def line(text, font=None, indent=True, height=None):
    ws.append(["", text] if indent else [text])
    r = ws.max_row
    ws.merge_cells(start_row=r, start_column=2 if indent else 1, end_row=r, end_column=8)
    c = ws.cell(r, 2 if indent else 1)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if font:
        c.font = font
    if height:
        ws.row_dimensions[r].height = height


by_p = defaultdict(int)
for r in ROWS:
    by_p[r[4]] += 1
line("Huel EU - German Search: keyword additions per ad group", Font(bold=True, size=16, color=NAVY), indent=False, height=24)
line("v2 · 9 Nov 2026 · closest matches to existing keywords, each checked against the ad group's landing page",
     Font(italic=True, color="595959"), indent=False)
ws.append([])
line("In one sentence", SEC, indent=False)
line(f"{len(ROWS)} keywords ({by_p['P1']} now, {by_p['P2']} next, {by_p['P3']} tests). Every one is a near variant of a keyword "
     "the ad group already runs, and only promises what its landing page says. The page check also turned up "
     f"{len(LP_FIXES)} fixes to existing keywords, the biggest being shake competitors (yfood, Soylent) landing on the hot-meals page.",
     height=48)
ws.append([])
line("Ad group → landing page → keywords", SEC, indent=False)
ws.append(["", "Ad group", "Landing page", "Add now", "Next", "Test", "Total", ""])
for c in ws[ws.max_row][1:7]:
    c.fill, c.font = HDR, HFONT
for ag in order:
    cnt = defaultdict(int)
    for r in groups[ag]:
        cnt[r[4]] += 1
    ws.append(["", ag.replace("NEW: ", "") + ("  (new)" if ag.startswith("NEW:") else ""), AD_GROUPS[ag][1].replace("de.huel.com/products/", "/"),
               cnt["P1"] or "", cnt["P2"] or "", cnt["P3"] or "", len(groups[ag])])
    for c in ws[ws.max_row][1:7]:
        c.border = Border(bottom=THIN)
    for col in (4, 5, 6, 7):
        ws.cell(ws.max_row, col).alignment = Alignment(horizontal="center")
ws.append(["", "Total", "", by_p["P1"], by_p["P2"], by_p["P3"], len(ROWS)])
for c in ws[ws.max_row][1:7]:
    c.font = Font(bold=True)
for col in (4, 5, 6, 7):
    ws.cell(ws.max_row, col).alignment = Alignment(horizontal="center")
ws.append([])
line("What the landing-page check found", SEC, indent=False)
for t in [
    "1.  Shake competitors land on hot meals. yfood, Soylent, Mana, Saturo and Jimmy Joy sit in 'Competitors - Meal Replacement & "
    "Delivery', whose ads go to the Hot & Savoury page. Proposed: a new 'Competitors - Meal Shakes' ad group on the Black Edition page "
    "(run as an experiment - Soylent already returns 1.18).",
    "2.  'muskelaufbau protein' (Weight Gain) lands on the Black Edition meal page: €1,347 at ROAS 0.47. Muscle-building terms belong on "
    "Complete Protein, whose page talks about training and recovery.",
    "3.  'proteinriegel' in Meal replacement lands on the shake page: €936 at ROAS 0.24. Pause it.",
    "4.  Weight Gain's page (Black Edition) never mentions gaining weight, so only protein-shake variants are proposed there, not 'gainer' terms.",
    "5.  Outdoor Food converts well (ROAS 1.15) even though the Hot & Savoury page never mentions outdoor use - an outdoor section "
    "on that page is the obvious next lift.",
    "6.  All brand ads go to the homepage, including product keywords like 'huel black edition'. Add product final URLs.",
    "7.  Three earlier suggestions failed the check: the Complete Protein page doesn't claim 'no sweeteners', 'sugar-free' or pea protein.",
]:
    line(t, height=44 if len(t) > 160 else 30)
ws.append([])
line("Tabs", SEC, indent=False)
for t in ["Keywords by ad group - the list, grouped under each ad group with its landing page",
          "Landing-page fixes - existing keywords on the wrong page",
          "Dropped after page check - earlier suggestions removed and why",
          "Negatives to add · Google Ads Editor upload (with final URLs where needed)",
          "Full data, Already covered, Not recommended, Current DE keywords, Ad group benchmarks - reference"]:
    line("•  " + t)

order_tabs = ["Summary", "Keywords by ad group", "Landing-page fixes", "Dropped after page check", "Negatives to add",
              "Google Ads Editor upload", "Full data (analyst)", "Already covered - no add", "Considered - not recommended",
              "Current DE keywords", "Ad group benchmarks"]
wb._sheets = [wb[n] for n in order_tabs]
for n in order_tabs[:4]:
    wb[n].sheet_properties.tabColor = NAVY
for n in order_tabs[5:]:
    wb[n].sheet_properties.tabColor = "BFBFBF"
for n in order_tabs[:5]:
    w = wb[n]
    w.page_setup.orientation = "landscape"
    w.page_setup.fitToWidth, w.page_setup.fitToHeight = 1, 0
    w.sheet_properties.pageSetUpPr.fitToPage = True
wb.active = 0
wb.save(OUT)
print("saved", OUT, len(ROWS), "keywords")
