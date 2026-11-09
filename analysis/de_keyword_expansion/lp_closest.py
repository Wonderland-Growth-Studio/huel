"""Closest-match keyword candidates per ad group, gated by what each landing page supports.

A candidate qualifies when it = an existing live keyword in the ad group + extra words, and EVERY extra word is
either a neutral commercial modifier or an attribute the ad group's landing page actually claims.
Usage: python3 lp_closest.py DATA_DIR  -> DATA_DIR/lp_candidates.json
"""
import json, re, sys
from collections import defaultdict

D = sys.argv[1]


def norm(s):
    s = s.lower().replace("ß", "ss")
    s = re.sub(r"[^a-z0-9äöü ]", " ", s)
    return " ".join(s.split())


def stem(w):
    for suf in ("innen", "en", "er", "es", "e", "n", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def sig(k):
    return " ".join(sorted(stem(w) for w in k.split()))


# Landing pages (from the enabled ads; no keyword-level URL overrides exist)
LP = {
    "Meal replacement": "black", "Weight Loss": "black", "Weight Gain": "black",
    "Ready Meals": "hs", "Outdoor Food": "hs", "Competitors - Meal Replacement & Delivery": "hs",
    "Protein": "protein", "Vegan": "protein", "Competitors - Protein": "protein",
    "Greens": "greens", "Competitors - Greens": "greens", "Bar": "bar",
}
LP_URL = {"black": "de.huel.com/products/huel-black-edition", "hs": "de.huel.com/products/hot-and-savoury-meal-packs",
          "protein": "de.huel.com/products/huel-complete-protein", "greens": "de.huel.com/products/huel-daily-greens",
          "bar": "de.huel.com/products/huel-bar"}

NEUTRAL = set("""beste bester bestes besten gute guter gutes gut test testsieger vergleich günstig günstige günstiger günstiges
preiswert online bestellen shop top für zum zur mit ohne und als bei im in de deutschland gesund gesunde gesunder gesundes
gesunden frauen frau männer mann sport alternative alternativen erfahrungen erfahrung bewertung""".split())

# Attributes each page claims (read from the page): words allowed beyond the seed keyword
SUPPORTED = {
    "black": set("""vegan vegane veganer veganes pflanzlich pflanzliche pflanzlicher pflanzliches protein proteinreich
        proteinreiche proteinreicher proteinreiches eiweiss eiweissreich high shake shakes pulver drink trinken
        mahlzeit mahlzeiten trinkmahlzeit komplett vollwertig vollwertige nährstoffe vitamine ballaststoffe sättigend
        sättigende satt schnell schnelle schnelles büro arbeit frühstück mittagessen unterwegs laktosefrei milch
        süssungsmittel süssstoff kalorien low carb kohlenhydratarm ersatz""".split()),
    "hs": set("""vegan vegane veganer veganes pflanzlich protein proteinreich proteinreiche high instant schnell
        schnelle schnelles warm warme heiss heisse mittagessen büro arbeit unterwegs trekking camping outdoor wandern
        reise reisen gefriergetrocknet gefriergetrocknete gefriergetrocknetes glutenfrei glutenfreie haltbar
        lange kühlung pasta nudeln curry essen gericht gerichte mahlzeit mahlzeiten fertiggericht fertiggerichte
        nahrung""".split()),
    "protein": set("""vegan vegane veganer veganes pflanzlich pflanzliche pflanzliches protein proteine pulver shake shakes
        glutenfrei glutenfreies soja sojafrei laktosefrei laktosefreies milch vitamine aminosäuren muskelaufbau
        training workout sport vanille schoko schokolade erdbeer""".split()),
    "greens": set("""vegan vegane veganes pulver drink greens super grünes grüne superfood probiotika adaptogene
        vitamine mineralstoffe nährstoffe glutenfrei süssungsmittel immunsystem energie verdauung darm täglich""".split()),
    "bar": set("""vegan vegane veganer veganes protein proteinriegel riegel snack snacks wenig zucker zuckerarm
        süssungsmittel ballaststoffe vitamine unterwegs""".split()),
}
# Goal words allowed only where the ad group is about that goal
GOAL = {"Weight Loss": {"abnehmen", "diät", "kalorienarm", "kalorienarme", "gewichtsverlust", "abnehm"},
        "Weight Gain": {"zunehmen", "zunehm", "kalorienreich", "masse", "muskelaufbau", "gewichtszunahme", "kalorien"},
        "Outdoor Food": {"trekking", "camping", "outdoor", "wandern", "expedition"}}
# Words that contradict a page outright
CONTRA = {
    "protein": {"whey", "isolat", "clear", "casein", "kollagen", "süssungsmittel", "zucker", "zuckerfrei"},  # page claims neither no-sweetener nor sugar-free
    "black": {"whey", "riegel", "rezept", "rezepte", "glutenfrei"},
    "hs": {"shake", "shakes", "pulver", "drink", "kochbox", "lieferung", "liefern", "rezept", "rezepte", "tiefkühl"},
    "greens": {"bio", "kapseln", "tabletten"},
    "bar": {"ohne"},  # 2g sugar: no 'ohne zucker' claims
}

kw = json.load(open(f"{D}/de_kw_all.json"))["result"]
existing, ex_sig, ag_kws, agneg = set(), set(), defaultdict(set), defaultdict(list)
for r in kw:
    t = norm(r["ad_group_criterion.keyword.text"])
    if r["ad_group_criterion.negative"]:
        agneg[r["ad_group.name"]].append((r["ad_group_criterion.keyword.text"], r["ad_group_criterion.keyword.match_type"]))
    elif r["ad_group.status"] == "ENABLED" and r["ad_group_criterion.status"] == "ENABLED":
        existing.add(t)
        ex_sig.add(sig(t))
        ag_kws[r["ad_group.name"]].add(t)
shared = json.load(open(f"{D}/shared_negs.json"))["DE_SEARCH_GENERIC"]


def blocks(q, n, mt):
    q, n = norm(q).split(), norm(n).split()
    if not n:
        return False
    if mt == "EXACT":
        return q == n
    if mt == "PHRASE":
        return any(q[i:i + len(n)] == n for i in range(len(q) - len(n) + 1))
    return set(n) <= set(q)


sug = json.load(open(f"{D}/dfs/suggestions.json"))
out = defaultdict(dict)
for seed, v in sug.items():
    ag = v["ad_group"]
    lp = LP[ag]
    s_toks = norm(seed).split()
    allowed = NEUTRAL | SUPPORTED[lp] | GOAL.get(ag, set())
    for it in v["items"]:
        k = norm(it["kw"])
        if not it["sv"] or it["sv"] < 30 or k in existing or sig(k) in ex_sig:
            continue
        toks = k.split()
        extra = list(toks)
        for w in s_toks:  # remove seed words once
            if w in extra:
                extra.remove(w)
        if not extra or len(extra) > 3:
            continue
        if any(w in CONTRA[lp] for w in toks):
            continue
        if not all(w in allowed for w in extra):
            continue
        if any(blocks(k, t, m) for t, m in agneg[ag]) or any(blocks(k, t, m) for t, m, _ in shared):
            continue
        s = sig(k)
        cur = out[ag].get(s)
        if cur is None or it["sv"] > cur["sv"]:
            out[ag][s] = {"kw": k, "seed": seed, "extra": extra, "sv": it["sv"], "cpc": it["cpc"], "intent": it["intent"],
                          "lp": LP_URL[lp]}
res = {ag: sorted(d.values(), key=lambda x: -x["sv"]) for ag, d in out.items()}
json.dump(res, open(f"{D}/lp_candidates.json", "w"), ensure_ascii=False, indent=0)
for ag, rows in res.items():
    print(f"===== {ag} -> {rows[0]['lp'] if rows else ''} ({len(rows)})")
    print("; ".join(f"{r['kw']}|{r['sv']}|+{' '.join(r['extra'])}" for r in rows[:60]))
