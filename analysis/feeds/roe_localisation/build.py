# -*- coding: utf-8 -*-
"""Build localised Rest-of-Europe Merchant Center feeds from the English source.

Only title, description, product_highlights and product_detail are localised.
Every other column (ids, GTINs, google_product_category, product_type,
custom_label_0-3, shipping, prices, links, images) is copied verbatim.

Usage:  python3 -I build.py   (run from this directory)
Writes: ROE_feed_localised.xlsx, csv/feed_<lang>.csv, qa_report.txt
"""
import csv, json, os, re, sys, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_data import LANGS, LANG_META, FLAV, TITLE, DESC, EXTRA, HL, PD, FLAV_HL, UP_TO

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.reader(open(os.path.join(HERE, "source_roe_feed_en.csv"), encoding="utf-8")))
HEAD, DATA = rows[0], rows[1:]
COL = {h.strip(): i for i, h in reversed(list(enumerate(HEAD)))}  # first occurrence
I_ID, I_TITLE, I_DESC = COL["id"], COL["title"], COL["description"]
I_HL, I_PD, I_L1 = COL["product_highlights"], COL["product_detail"], COL["custom_label_1"]

def family(pid):
    for pre, fam in [("BLKS16", "BE_BOX"), ("BLK-", "BE_POW"), ("CNB15", "BAR_BOX"), ("CNB-", "BAR"),
                     ("GRE-", "GREENS"), ("PGF-", "GF_POW"), ("POW-", "POW"), ("PTN-", "PROT"),
                     ("RTB-", "BE_RTD"), ("RTD-", "RTD"), ("SAVS14", "SAV_BOX"), ("SAVS7", "SAV"),
                     ("ESS-", "ESS"), ("RAL6", "RAL"), ("RAB6", "RAB")]:
        if pid.startswith(pre):
            return fam
    raise ValueError(pid)

# custom_label_1 -> flavour key, where the label differs from the copy key
FLAV_FIX = {"Dark Chocolate & Raspberry": "Dark Chocolate & Raspberry", "Chick'n Mushroom": "Chick'n & Mushroom Pasta",
            "Hoisin Duck Noodles": "Hoisin 'Duck' Noodles", "Classic Chicken": "Classic 'Chicken'",
            "Asian-style Beef": "Asian-Style 'Beef'", "Pasta & Grains Selection Box": "Pasta & Grains",
            "Noodles Selection Box": "Noodles"}

def flavour_key(row, fam):
    lab = row[I_L1].strip()
    if row[I_ID] == "PTN-BAN-20-EDP":
        return "Banana Milkshake"
    return FLAV_FIX.get(lab, lab)

def protein(row, fam):
    pid = row[I_ID]
    if fam == "BAR":
        m = re.search(r"provides (\d+)g of protein", row[I_DESC]); return m.group(1)
    if fam == "SAV":
        m = re.search(r"Protein:(\d+)g", row[I_PD]); return m.group(1)
    if fam in ("RAL",): return "25"
    if fam in ("RAB",): return "40"
    return ""

def has_flavour_hl(row):
    return "flavour with natural flavouring" in row[I_HL] or re.search(r'"\w[^"]* flavour"', row[I_HL])

def fmt_hl(items):
    return ", ".join('"%s"' % i.replace('"', '""') for i in items)

def product_detail(lang, row, fam, p):
    src = row[I_PD]
    if fam in ("RAL", "RAB"):
        kcal = re.search(r"Calories:(\d+)", src).group(1)
        fib = "6" if fam == "RAL" else UP_TO[lang] + " 6"
        return PD[lang]["_ramen"].format(p=p, kcal=kcal, fib=fib)
    if fam == "GREENS":
        return PD[lang]["_greens"]
    m = re.search(r"Protein:(\d+)g", src)
    return PD[lang]["_simple"].format(p=m.group(1))

def tidy(s):
    s = re.sub(r"\s+", " ", s).strip()
    return s.replace(" .", ".")

out, issues = {}, []
for lang in LANGS:
    o = []
    for row in DATA:
        r = list(row)
        pid, fam = row[I_ID], family(row[I_ID])
        fk = flavour_key(row, fam)
        f = "" if fam in ("BE_BOX", "BAR_BOX") else FLAV[lang][fk]
        p = protein(row, fam)
        x = EXTRA[lang].get(pid, "")
        r[I_TITLE] = tidy(TITLE[lang][fam].format(f=f, p=p))
        r[I_DESC] = tidy(DESC[lang][fam].format(f=f, p=p, x=x))
        hl_fam = fam if fam in HL[lang] else {"BAR_BOX": "BAR", "SAV_BOX": "SAV"}.get(fam, fam)
        hp = (UP_TO[lang] + " 25") if fam == "SAV_BOX" else (p or "25")
        hl = [h.format(f=f, p=hp) for h in HL[lang][hl_fam]]
        if fam == "SAV_BOX": hl[0] = hl[0][0].upper() + hl[0][1:]
        if has_flavour_hl(row) and fam not in ("BE_BOX", "BAR_BOX", "SAV_BOX"):
            hl.append(FLAV_HL[lang].format(f=f))
        r[I_HL] = fmt_hl(hl)
        r[I_PD] = product_detail(lang, row, fam, p)
        # QA
        if len(r[I_TITLE]) > 150: issues.append(f"{lang} {pid} title {len(r[I_TITLE])} chars")
        if len(r[I_DESC]) > 5000: issues.append(f"{lang} {pid} description too long")
        if "{" in r[I_TITLE] + r[I_DESC] + r[I_HL] + r[I_PD]: issues.append(f"{lang} {pid} unfilled placeholder")
        if any(len(h) > 150 for h in hl): issues.append(f"{lang} {pid} highlight >150")
        if fam in ("BAR", "RAL", "RAB") and not x: issues.append(f"{lang} {pid} missing flavour sentence")
        o.append(r)
    out[lang] = o

# ------------------------------------------------------------- outputs
# custom_label_4 = feed content language (ISO 639-1), inserted after custom_label_3,
# so Google Ads can segment/report by feed language (segments.product_custom_attribute4).
I_L4 = COL["custom_label_3"] + 1
HEAD_OUT = HEAD[:I_L4] + ["custom_label_4"] + HEAD[I_L4:]
def with_lang(data, code):
    return [r[:I_L4] + [code] + r[I_L4:] for r in data]
def shifted(i):
    return i + 1 if i >= I_L4 else i

os.makedirs(os.path.join(HERE, "csv"), exist_ok=True)
for lang, o in list(out.items()) + [("en", DATA)]:
    with open(os.path.join(HERE, "csv", f"feed_{lang}.csv"), "w", encoding="utf-8", newline="") as fh:
        csv.writer(fh).writerows([HEAD_OUT] + with_lang(o, lang))

# search-term validation layer
def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).replace("-", " ")

# Raw Google Ads search_term_view export (not committed); set SEARCH_TERMS_JSON to its path.
TERMS = json.load(open(os.environ.get("SEARCH_TERMS_JSON", os.path.join(HERE, "search_terms_raw.json"))))["result"]
agg = collections.defaultdict(lambda: [0, 0, 0.0, set()])
for t in TERMS:
    a = agg[t["search_term_view.search_term"]]
    a[0] += int(t["metrics.impressions"]); a[1] += int(t["metrics.clicks"])
    a[2] += float(t["metrics.conversions"]); a[3].add("Shopping" if "SHOPPING" in t["campaign.name"] else "Search")

# (term as searched, language, concept matched in titles, decision)
LOCAL = [
 ("substitut de repas", "fr", "substitut de repas", "used"), ("substitut de repas protéiné", "fr", "substitut de repas proteine", "used"),
 ("substitut repas", "fr", "substitut de repas", "used"), ("repas protéiné", "fr", "proteine", "used (BE powder lead)"),
 ("repas a boire", "fr", "repas a boire", "used"), ("boisson repas", "fr", "repas a boire", "covered by 'repas à boire'"),
 ("repas liquide", "fr", "repas a boire", "covered by 'repas à boire'"), ("repas en poudre", "fr", "repas complet en poudre", "used"),
 ("boisson protéinée", "fr", "proteine", "partial - used 'protéiné' modifier"), ("barre protéinée", "fr", "barres proteinees", "used"),
 ("nouilles protéinées", "fr", "nouilles", "used (ramen titles)"), ("proteine sans gluten", "fr", "sans gluten", "used (GF powder)"),
 ("plat proteine", "fr", "plat prepare riche en proteines", "used"),
 ("maaltijdshake", "nl", "maaltijdshake", "used"), ("maaltijd shake", "nl", "maaltijdshake", "used"),
 ("maaltijdshakes", "nl", "maaltijdshake", "used"), ("maaltijdvervangers", "nl", "maaltijdvervanger", "used"),
 ("maaltijd vervangers", "nl", "maaltijdvervanger", "used"), ("drinkmaaltijd", "nl", "drinkmaaltijd", "used"),
 ("ontbijtshake", "nl", "ontbijt", "not used in title - in description ('ontbijt')"),
 ("eiwitpoeder", "nl", "eiwitpoeder", "used"), ("vegan eiwitpoeder", "nl", "vegan eiwitpoeder", "used"),
 ("proteine poeder", "nl", "eiwitpoeder", "covered by 'eiwitpoeder'"), ("kant en klare maaltijden", "nl", "kant en klaar", "used"),
 ("batidos sustitutivos", "es", "batido sustitutivo", "used"), ("batidos sustitutivos de comida para adelgazar", "es", "batido sustitutivo de comida", "used - 'adelgazar' deliberately NOT added (EU claims)"),
 ("proteina vegana", "es", "proteina vegana", "used"), ("proteina vegetal", "es", "proteina", "covered by 'proteína vegana'"),
 ("proteina sin gluten", "es", "sin gluten", "used (GF powder)"), ("proteina en polvo", "es", "proteina vegana en polvo", "used"),
 ("comida preparada", "es", "comida preparada", "used"),
 ("pasto sostitutivo", "it", "pasto sostitutivo", "used"), ("pasti sostitutivi", "it", "pasto sostitutivo", "used (singular)"),
 ("pasti pronti proteici", "it", "piatto pronto proteico", "used"), ("pasti pronti", "it", "piatto pronto", "used"),
 ("piatti pronti proteici", "it", "piatto pronto proteico", "used"), ("barrette proteiche", "it", "barrette proteiche", "used"),
 ("proteine in polvere", "it", "proteine vegane in polvere", "used"), ("proteine in polvere senza glutine", "it", "senza glutine", "partial"),
 ("substituto de refeição", "pt", "substituto de refeicao", "used"),
 ("trinkmahlzeit", "de", "trinkmahlzeit", "used"), ("proteinpulver", "de", "proteinpulver", "used"),
 ("veganes proteinpulver", "de", "veganes proteinpulver", "used"), ("protein pulver", "de", "proteinpulver", "covered"),
 ("fertiggerichte", "de", "fertiggericht", "used"),
]
EN_SEEN = ["meal replacement shakes", "meal replacement", "protein powder", "vegan protein powder", "protein shake",
           "protein bars", "high protein meals", "meal replacement powder", "gluten free protein powder", "ready meals"]

def in_titles(lang, concept):
    c = norm(concept)
    return sum(1 for r in out[lang] if c in norm(r[I_TITLE]))

val_rows = []
for term, lang, concept, decision in LOCAL:
    a = agg.get(term, [0, 0, 0.0, set()])
    val_rows.append([term, LANG_META[lang][0], a[1], round(a[2], 1), "/".join(sorted(a[3])), concept,
                     in_titles(lang, concept), decision])

# ------------------------------------------------------------- workbook
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
wb = Workbook()
ws = wb.active; ws.title = "READ ME"
bold = Font(bold=True)
hdr_fill = PatternFill("solid", fgColor="111111"); hdr_font = Font(bold=True, color="FFFFFF")
loc_fill = PatternFill("solid", fgColor="FFF2CC")

notes = open(os.path.join(HERE, "README_sheet.txt"), encoding="utf-8").read().splitlines()
for line in notes:
    ws.append([line])
    if line.isupper() or line.startswith("##"):
        ws.cell(ws.max_row, 1).font = bold
ws.column_dimensions["A"].width = 160
for c in ws["A"]: c.alignment = Alignment(wrap_text=True, vertical="top")

def feed_sheet(name, data, code):
    s = wb.create_sheet(name)
    s.append(HEAD_OUT)
    for r in with_lang(data, code): s.append(r)
    for j, h in enumerate(HEAD_OUT, 1):
        cell = s.cell(1, j); cell.fill, cell.font = hdr_fill, hdr_font
        s.column_dimensions[get_column_letter(j)].width = 14
    s.cell(1, I_L4 + 1).fill = PatternFill("solid", fgColor="38761D")
    for idx, w in [(shifted(I_TITLE), 60), (shifted(I_DESC), 80), (shifted(I_HL), 50), (shifted(I_PD), 40)]:
        s.column_dimensions[get_column_letter(idx + 1)].width = w
        if name != "EN (source)":
            s.cell(1, idx + 1).fill = PatternFill("solid", fgColor="B45F06")
    s.freeze_panes = "B2"

feed_sheet("EN (source)", DATA, "en")
for lang in LANGS:
    en, native, countries = LANG_META[lang]
    feed_sheet(f"{lang.upper()} - {'+'.join(countries)}", out[lang], lang)

v = wb.create_sheet("Search term check")
v.append(["Search term (ROE, last 90 days)", "Language", "Clicks", "Conv.", "Campaigns", "Concept checked in titles", "# titles containing it", "Decision"])
for r in val_rows: v.append(r)
v.append([]); v.append(["English-language terms (IE + English searchers elsewhere) - served by the EN source feed, unchanged"]); v.cell(v.max_row, 1).font = bold
for t in EN_SEEN:
    a = agg.get(t, [0, 0, 0.0, set()]); v.append([t, "English", a[1], round(a[2], 1), "/".join(sorted(a[3])), "", "", "EN feed (unchanged)"])
for j in range(1, 9):
    v.cell(1, j).fill, v.cell(1, j).font = hdr_fill, hdr_font
for col, w in zip("ABCDEFGH", [44, 12, 8, 8, 16, 34, 12, 60]): v.column_dimensions[col].width = w

# side-by-side review tab
rv = wb.create_sheet("Title review")
rv.append(["id", "EN (source)"] + [f"{l.upper()}" for l in LANGS])
for i, row in enumerate(DATA):
    rv.append([row[I_ID], row[I_TITLE].strip()] + [out[l][i][I_TITLE] for l in LANGS])
for j in range(1, 10):
    rv.cell(1, j).fill, rv.cell(1, j).font = hdr_fill, hdr_font
    rv.column_dimensions[get_column_letter(j)].width = 18 if j == 1 else 55
for r in rv.iter_rows(min_row=2):
    for c in r: c.alignment = Alignment(wrap_text=True, vertical="top")
rv.freeze_panes = "C2"

wb.save(os.path.join(HERE, "ROE_feed_localised.xlsx"))

# client-facing copy: feed tabs only (no READ ME / search-term / review tabs)
for name in ["READ ME", "Search term check", "Title review"]:
    del wb[name]
wb["EN (source)"].title = "EN - IE"
wb.active = 0
wb.save(os.path.join(HERE, "ROE_feed_localised_client.xlsx"))

# QA report
with open(os.path.join(HERE, "qa_report.txt"), "w", encoding="utf-8") as fh:
    fh.write(f"rows per language: {len(DATA)}; languages: {', '.join(LANGS)}\n")
    for lang in LANGS:
        tl = [len(r[I_TITLE]) for r in out[lang]]
        fh.write(f"{lang}: title len min {min(tl)} max {max(tl)} avg {sum(tl)//len(tl)}; "
                 f"desc max {max(len(r[I_DESC]) for r in out[lang])}\n")
    # verify untouched columns
    for lang in LANGS:
        for a, b in zip(DATA, out[lang]):
            for j in range(len(HEAD)):
                if j not in (I_TITLE, I_DESC, I_HL, I_PD) and a[j] != b[j]:
                    issues.append(f"{lang} {a[I_ID]} column {HEAD[j]} changed!")
    fh.write("issues:\n" + ("\n".join(issues) if issues else "none") + "\n")
print(open(os.path.join(HERE, "qa_report.txt"), encoding="utf-8").read())
