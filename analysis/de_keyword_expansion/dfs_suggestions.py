"""For every live DE generic keyword, pull DataforSEO Labs keyword_suggestions (searches that contain the keyword).
Usage: python3 dfs_suggestions.py DATA_DIR   -> DATA_DIR/dfs/suggestions.json  {seed: [items]}
"""
import base64, json, os, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

D = sys.argv[1]
kw = json.load(open(f"{D}/de_kw_all.json"))["result"]
seeds = {}
for r in kw:
    if (r["campaign.name"] == "DE_SEARCH_GENERIC" and not r["ad_group_criterion.negative"]
            and r["ad_group.status"] == "ENABLED" and r["ad_group_criterion.status"] == "ENABLED"):
        seeds.setdefault(r["ad_group_criterion.keyword.text"].lower(), r["ad_group.name"])
auth = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()


def get(seed):
    body = [{"keyword": seed, "location_code": 2276, "language_code": "de", "limit": 150,
             "include_seed_keyword": False, "order_by": ["keyword_info.search_volume,desc"]}]
    req = urllib.request.Request("https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    t = json.load(urllib.request.urlopen(req, timeout=180))["tasks"][0]
    items = ((t.get("result") or [{}])[0] or {}).get("items") or []
    out = [{"kw": i["keyword"], "sv": (i.get("keyword_info") or {}).get("search_volume"),
            "cpc": (i.get("keyword_info") or {}).get("cpc"),
            "intent": ((i.get("search_intent_info") or {}).get("main_intent"))} for i in items]
    return seed, t["status_code"], t.get("cost") or 0, out


res, cost = {}, 0
with ThreadPoolExecutor(8) as ex:
    for seed, code, c, out in ex.map(get, sorted(seeds)):
        res[seed] = {"ad_group": seeds[seed], "items": out}
        cost += c
        if code != 20000:
            print("ERR", seed, code)
json.dump(res, open(f"{D}/dfs/suggestions.json", "w"), ensure_ascii=False)
print(len(seeds), "seeds | items", sum(len(v["items"]) for v in res.values()), "| cost $", round(cost, 3))
