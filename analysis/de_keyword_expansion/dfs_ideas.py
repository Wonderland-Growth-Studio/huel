"""Pull Google Ads keyword ideas from DataforSEO for German (DE) seed themes.
Usage: python3 dfs_ideas.py OUT_DIR
Credentials: DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD env vars.
"""
import base64, json, os, sys, urllib.request

SEEDS = {
    "meal_replacement": ["trinkmahlzeit", "mahlzeitenersatz", "mahlzeitenersatz shake", "trinknahrung", "flüssignahrung",
                          "trinkmahlzeit pulver", "komplettnahrung", "vollwertige mahlzeit", "astronautennahrung",
                          "pulvernahrung", "trinkfrühstück", "frühstücksshake", "sattmacher shake", "trinkmahlzeit vegan",
                          "nährstoffshake", "mahlzeit zum trinken", "trinkmahlzeit test", "flüssige mahlzeit"],
    "ready_meals": ["fertiggerichte", "gesunde fertiggerichte", "protein fertiggerichte", "meal prep", "instant mahlzeit",
                    "schnelles mittagessen", "mittagessen büro", "gesunde instant nudeln", "high protein fertiggerichte",
                    "mikrowellengerichte", "vegane fertiggerichte", "fertiggerichte kalorienarm", "instant food",
                    "gesundes mittagessen", "fertiggerichte ohne kühlung", "becher gerichte"],
    "outdoor": ["outdoor nahrung", "trekking nahrung", "trekking essen", "gefriergetrocknete mahlzeiten", "camping essen",
                "expeditionsnahrung", "notfallnahrung", "krisenvorsorge lebensmittel", "survival nahrung",
                "bikepacking essen", "wandernahrung", "outdoor mahlzeiten", "notvorrat lebensmittel", "camping food",
                "langzeitnahrung", "tactical food"],
    "protein": ["proteinpulver", "eiweißpulver", "protein shake", "whey protein", "proteinpulver ohne süßungsmittel",
                "proteinpulver laktosefrei", "proteinpulver test", "clear whey", "proteinshake", "protein pulver",
                "proteinpulver ohne zucker", "proteinpulver kaufen", "proteinpulver frauen", "protein mahlzeit"],
    "vegan_protein": ["veganes proteinpulver", "vegan protein", "pflanzliches protein", "proteinpulver vegan",
                      "erbsenprotein", "bestes veganes proteinpulver", "vegan protein shake", "reisprotein",
                      "veganer proteinshake", "proteinpulver ohne milch"],
    "greens": ["daily greens", "greens pulver", "super greens", "grünes pulver", "superfood pulver", "ag1 alternative",
               "greens drink", "green powder", "vitamin pulver", "multivitamin pulver", "greens", "superfood drink",
               "gemüsepulver", "nährstoffpulver", "darmgesundheit pulver", "alles in einem pulver"],
    "weight_loss": ["abnehm shake", "diät shake", "eiweißshake abnehmen", "mahlzeitenersatz abnehmen", "shake zum abnehmen",
                    "trinkmahlzeit abnehmen", "proteinshake abnehmen", "kalorienarme mahlzeit", "sättigungs shake",
                    "abnehmen mit shakes", "low calorie shake", "diät drink", "kalorienarm essen", "gewichtsverlust shake"],
    "weight_gain": ["weight gainer", "zunehmen shake", "kalorienshake", "mass gainer", "hochkalorische trinknahrung",
                    "zunehmen", "schnell zunehmen", "masse shake", "gesund zunehmen", "hochkalorische nahrung",
                    "trinkmahlzeit zunehmen", "zunehmen untergewicht"],
    "competitors": ["prep my meal", "löwenanteil", "yfood", "jimmy joy", "saturo", "mana trinkmahlzeit", "ag1",
                    "every foods", "trek n eat", "adventure food", "this is food", "just food", "holi", "more nutrition",
                    "plenny shake", "feed trinkmahlzeit", "biogena one", "metaflow", "tellerglück", "onek"],
}

def call(endpoint, payload):
    auth = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
    req = urllib.request.Request(f"https://api.dataforseo.com/v3/{endpoint}", data=json.dumps(payload).encode(),
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for theme, seeds in SEEDS.items():
        res = call("keywords_data/google_ads/keywords_for_keywords/live",
                   [{"keywords": seeds[:20], "location_code": 2276, "language_code": "de",
                     "include_adult_keywords": False, "sort_by": "search_volume"}])
        t = res["tasks"][0]
        print(theme, t["status_code"], t["status_message"], t.get("cost"), t.get("result_count"))
        json.dump(t.get("result") or [], open(f"{out}/ideas_{theme}.json", "w"), ensure_ascii=False)
