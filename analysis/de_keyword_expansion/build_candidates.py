"""Merge DataforSEO ideas with account data and flag what is already covered.
Usage: python3 build_candidates.py DATA_DIR  -> writes DATA_DIR/candidates.json
"""
import json, re, statistics, sys, glob, os

D = sys.argv[1]

def norm(s):
    s = s.lower().replace("ß", "ss")
    s = re.sub(r"[^a-z0-9äöü ]", " ", s)
    return " ".join(s.split())

def toks(s):
    return norm(s).split()

# account keywords (any status) and active ones
kw = json.load(open(f"{D}/de_kw_all.json"))["result"]
existing_any, existing_active, neg_ag = {}, {}, {}
for r in kw:
    t = norm(r["ad_group_criterion.keyword.text"])
    if r["ad_group_criterion.negative"]:
        continue
    existing_any.setdefault(t, set()).add(f'{r["ad_group.name"]} ({r["ad_group.status"][:3]}/{r["ad_group_criterion.status"][:3]})')
    if r["ad_group.status"] == "ENABLED" and r["ad_group_criterion.status"] == "ENABLED" and r["campaign.name"] == "DE_SEARCH_GENERIC":
        existing_active.setdefault(t, set()).add(r["ad_group.name"])

# phrase negatives shared to DE_SEARCH_GENERIC (brand + agreement list)
BLOCK_PHRASES = ["huel", "my protein", "myprotein", "the protein works", "protein works", "proteinworks", "exante", "myvegan",
                 "my vegan", "hot and savoury", "almased", "barebells", "foodspring", "esn", "bulk"]

st = json.load(open(f"{D}/st_agg.json"))  # term -> [cost, clicks, conv, value, top_ag, status]
st_n = {}
for k, v in st.items():
    n = norm(k)
    a = st_n.setdefault(n, [0, 0, 0, 0, v[4]])
    for i in range(4):
        a[i] += v[i]

ideas = {}
for f in glob.glob(f"{D}/dfs/ideas_*.json"):
    theme = os.path.basename(f)[6:-5]
    for it in json.load(open(f)):
        k = norm(it["keyword"])
        ms = [m["search_volume"] or 0 for m in (it.get("monthly_searches") or [])][:12]
        med = statistics.median(ms) if ms else (it.get("search_volume") or 0)
        rec = ideas.get(k)
        if rec is None or (it.get("search_volume") or 0) > rec["sv"]:
            ideas[k] = {"kw": k, "theme": theme, "sv": it.get("search_volume") or 0, "sv_median": med,
                        "cpc": it.get("cpc"), "bid_low": it.get("low_top_of_page_bid"), "bid_high": it.get("high_top_of_page_bid"),
                        "comp": it.get("competition"), "monthly": ms}
        ideas[k].setdefault("themes", set()).add(theme)

out = []
for k, r in ideas.items():
    tt = toks(k)
    r["themes"] = sorted(r["themes"])
    r["active_in"] = sorted(existing_active.get(k, []))
    r["exists_any"] = sorted(existing_any.get(k, []))
    r["blocked"] = [b for b in BLOCK_PHRASES if re.search(rf"(^| ){re.escape(b)}( |$)", k)]
    s = st_n.get(k)
    r["st"] = s
    out.append(r)
json.dump(out, open(f"{D}/candidates.json", "w"), ensure_ascii=False)
print(len(out), "unique ideas")
