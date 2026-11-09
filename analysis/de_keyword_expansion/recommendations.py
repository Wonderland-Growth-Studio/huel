"""Curated DE keyword expansion for Huel EU (8046071519).

Each row: (keyword_de, english, match_types, campaign, ad_group, priority, source, rationale)
  priority: P1 = add now, P2 = add next / monitor, P3 = test with a capped budget
  source:   HARVEST  = search term already converting in DE_SEARCH_GENERIC (May-Nov 2026) but not a keyword
            ADJACENT = DataforSEO keyword idea, related to a live ad group, not yet in the account
            CONTROL  = brand/product query already served via broad match; exact keyword gives ad/LP control
Search-term evidence and DataforSEO volume are joined in by build_xlsx.py; rationale here is the judgement.
"""

G = "DE_SEARCH_GENERIC"
B = "DE_SEARCH_BRAND"
E, P, EP = ["EXACT"], ["PHRASE"], ["EXACT", "PHRASE"]

ROWS = [
    # ---------------- Outdoor Food (best generic ROAS in DE: 1.15, QS 7-8) ----------------
    ("gefriergetrocknetes essen", "freeze-dried food", E, G, "Outdoor Food", "P1", "HARVEST",
     "2.5 conv. Sibling of 'gefriergetrocknete mahlzeiten' (best keyword in AG, ROAS 2.25)."),
    ("gefriergetrocknete gerichte", "freeze-dried dishes", E, G, "Outdoor Food", "P1", "HARVEST",
     "2 conv at ROAS 5.7. Same intent cluster as the AG's best keyword."),
    ("freeze dried meals", "freeze-dried meals", E, G, "Outdoor Food", "P2", "HARVEST",
     "2.3 conv, ROAS 3.76. English variant; low volume but clean intent."),
    ("dehydriertes essen", "dehydrated food", E, G, "Outdoor Food", "P2", "HARVEST",
     "2.4 conv, ROAS 2.78 on small spend."),
    ("tactical food", "tactical food", E, G, "Outdoor Food", "P2", "HARVEST",
     "4 conv, ROAS 1.87; 480/mo. Only reached via 'outdoor nahrung' [B] today - exact gives it its own keyword/QS. 'tactical foodpack' (brand) is in Ready Meals."),
    ("vegane trekkingnahrung", "vegan trekking food", P, G, "Outdoor Food", "P1", "HARVEST",
     "2 conv, ROAS 2.54. Huel is 100% vegan - a USP most freeze-dried competitors cannot claim. Phrase picks up 'vegane trekking nahrung kaufen' etc."),
    ("expeditionsnahrung", "expedition food", E, G, "Outdoor Food", "P3", "ADJACENT",
     "DataforSEO idea (60/mo, low competition). EUR 30 spent via broad so far, no conversion yet - same buyer as trekking food."),

    # ---------------- NEW ad group: Competitors - Outdoor Food ----------------
    ("trek n eat", "Trek'n Eat (outdoor-meal brand)", E, G, "NEW: Competitors - Outdoor Food", "P1", "HARVEST",
     "12.3 conv, ROAS 1.08 - 564 of 567 clicks came via 'outdoor nahrung' [B] with generic outdoor copy. Own it with comparison copy. Add as negative [E] to Outdoor Food after launch."),
    ("trek and eat", "Trek'n Eat (spelling variant)", E, G, "NEW: Competitors - Outdoor Food", "P2", "HARVEST",
     "Spelling variant of Trek'n Eat (210/mo): 1.2 conv, ROAS 0.76. 'track n eat' also converted (2 conv, ROAS 6.5)."),
    ("adventure food", "Adventure Food (outdoor-meal brand)", E, G, "NEW: Competitors - Outdoor Food", "P1", "HARVEST",
     "7.5 conv at ROAS 2.25 - best competitor term in DE. Currently served by Outdoor Food broad."),

    # ---------------- Competitors - Meal Replacement & Delivery ----------------
    ("prep my meal", "Prep My Meal (meal-prep delivery brand)", E, G, "Competitors - Meal Replacement & Delivery", "P1", "HARVEST",
     "Largest single converting term in DE generic: 45 conv / EUR 4.2k (ROAS 0.83) with no keyword - 4,632 of 4,747 clicks came via 'dinnerly' [B]. Exact gives bid control. Note: it is a negative in all other generic AGs (deliberate routing) - keep that."),
    ("prep my meal alternative", "Prep My Meal alternative", E, G, "Competitors - Meal Replacement & Delivery", "P1", "HARVEST",
     "12.7 conv at ROAS 1.15 - above account average. 'prepmymeal alternative' adds 8.4 conv (close variant)."),
    ("prep meal", "prep meal", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "6 conv, ROAS 1.77, served by Ready Meals today. Navigational to Prep My Meal - competitor copy fits."),
    ("jimmy joy plenny shake", "Jimmy Joy Plenny Shake (meal-shake product)", E, G, "Competitors - Meal Replacement & Delivery", "P1", "HARVEST",
     "4.6 conv, ROAS 1.78. Direct powder-meal substitute; brand 'jimmy joy' already live."),
    ("this is food", "This Is Food (yfood product line)", E, G, "Competitors - Meal Replacement & Delivery", "P1", "HARVEST",
     "5 conv, ROAS 2.07, 8.1k/mo. yfood's product name - same buyer as 'yfood' (live, 44 conv). Served today by 'Trinkmahlzeit' [B] in Meal replacement with generic copy."),
    ("yfood alternative", "yfood alternative", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "5 conv, ROAS 0.78. Already in this AG via 'yfood' [B] (73%) - exact separates switching intent from bare-brand traffic so it can carry its own bid. AG negative elsewhere (routing) - no conflict here."),
    ("yfood pulver", "yfood powder", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "3.5 conv, ROAS 1.72. Already in this AG via 'yfood' [B]; powder buyer = closest match to Huel Powder, worth its own keyword/copy."),
    ("löwenanteil alternative", "Löwenanteil alternative", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "3 conv, ROAS 2.01. Brand 'löwenanteil' live (45 conv)."),
    ("every foods", "Every Foods (frozen meal brand)", E, G, "Competitors - Meal Replacement & Delivery", "P1", "HARVEST",
     "4 conv, ROAS 2.12; 24.6k/mo. Exact only - bare 'every' query wasted EUR 183."),
    ("tellerglück", "Tellerglück (healthy ready-meal brand)", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "2.3 conv, ROAS 1.9-2.9; 3.6k/mo. Ready-meal competitor."),
    ("onek", "ONEK (weight-gain shake brand)", E, G, "Competitors - Meal Replacement & Delivery", "P2", "HARVEST",
     "3 conv, ROAS 4.75 (via Weight Gain AG). Competitor brand - keep out of generic ad groups. Use weight-gain angle in copy."),

    # ---------------- NEW ad group: Competitors - Diet Shakes ----------------
    ("metaflow alternative", "Metaflow alternative (diet-shake brand)", E, G, "NEW: Competitors - Diet Shakes", "P2", "HARVEST",
     "2 conv, ROAS 1.56. Metaflow is the biggest diet-shake brand in DE (very high brand volume). Lead with 'alternative' intent."),
    ("metaflow shake", "Metaflow shake", E, G, "NEW: Competitors - Diet Shakes", "P3", "ADJACENT",
     "22k/mo. Brand-product term - test on low cap; '-erfahrungen'/review variants are research traffic."),
    ("sheko shake", "Sheko shake (diet-shake brand)", E, G, "NEW: Competitors - Diet Shakes", "P2", "HARVEST",
     "Sheko terms: 1.6 conv, ROAS 1.72 on EUR 113. 22k/mo."),
    ("sheko alternative", "Sheko alternative", E, G, "NEW: Competitors - Diet Shakes", "P2", "HARVEST",
     "Converted (0.6) on EUR 14. Switching intent."),
    ("layenberger shake", "Layenberger shake (diet-shake brand)", E, G, "NEW: Competitors - Diet Shakes", "P3", "ADJACENT",
     "5.4k/mo, low CPC (~EUR 0.90). No account history yet."),

    # ---------------- Competitors - Greens ----------------
    ("ag1 erfahrungen", "AG1 reviews/experiences", E, G, "Competitors - Greens", "P2", "HARVEST",
     "6.3 conv, ROAS 0.98; 2.1k/mo. Already served in this AG via 'ag1' [B] - exact adds keyword-level bid/QS control and lets you write review-angle copy, not new volume."),
    ("ag1 kritik", "AG1 criticism", E, G, "Competitors - Greens", "P2", "HARVEST",
     "3 conv, ROAS 1.64; 880/mo. Already in this AG via 'ag1' [B] - add for control/copy (criticism angle), low incremental volume."),
    ("ag1 inhaltsstoffe", "AG1 ingredients", E, G, "Competitors - Greens", "P2", "HARVEST",
     "3 conv, ROAS 7.9 on EUR 28; 800/mo. Ingredient-comparison angle suits Daily Greens."),
    ("biogena one", "Biogena One (greens/multi-nutrient brand)", E, G, "Competitors - Greens", "P2", "HARVEST",
     "2 conv, ROAS 1.19; 5.4k/mo. Currently served by generic Greens AG - move to competitor copy."),

    # ---------------- Greens ----------------
    ("greens", "greens", E, G, "Greens", "P2", "HARVEST",
     "2 conv, ROAS 2.32; 18k/mo. Exact only - the bare term is too ambiguous for broad."),
    ("super greens pulver", "super greens powder", E, G, "Greens", "P2", "ADJACENT",
     "390/mo. Extends live 'super greens' and 'greens pulver'."),

    # ---------------- Meal replacement (largest generic AG: EUR 33k, ROAS 1.00) ----------------
    ("mahlzeitenersatz shake", "meal replacement shake", E, G, "Meal replacement", "P1", "HARVEST",
     "4 conv, ROAS 2.39; 720/mo. Today split between 'Mahlzeitenersatz' [E] (Meal replacement) and 'diät shake' [E] (Weight Loss). Own exact keeps it on meal-replacement copy."),
    ("trinkmahlzeit pulver", "meal drink powder", E, G, "Meal replacement", "P1", "HARVEST",
     "5.5 conv, ROAS 0.86; 390/mo. Powder-format intent = Huel Powder / Black Edition."),
    ("protein trinkmahlzeit", "protein meal drink", E, G, "Meal replacement", "P1", "HARVEST",
     "2.3 conv, ROAS 4.03. Black Edition angle (high protein)."),
    ("protein mahlzeit", "protein meal", E, G, "Meal replacement", "P2", "HARVEST",
     "3.4 conv, ROAS 1.83."),
    ("meal replacement shake", "meal replacement shake (English)", E, G, "Meal replacement", "P2", "HARVEST",
     "3 conv, ROAS 2.16."),
    ("trinkmahlzeit ohne milch", "meal drink without milk / dairy-free", E, G, "Meal replacement", "P2", "HARVEST",
     "2 conv, ROAS 2.74. Dairy-free is a Huel USP vs yfood/Saturo."),
    ("trinkmahlzeit günstig", "cheap meal drink", E, G, "Meal replacement", "P2", "HARVEST",
     "2 conv, ROAS 8.3. Huel Powder's cost-per-meal angle."),
    ("trinkmahlzeit test", "meal drink test/review", E, G, "Meal replacement", "P2", "HARVEST",
     "2.2 conv, ROAS 1.05; 480/mo. Half its clicks come via 'beste trinkmahlzeit' [E] (ROAS 0.30) - own keyword separates it. Use test/award copy."),
    ("frühstücksshake", "breakfast shake", E, G, "Meal replacement", "P3", "HARVEST",
     "390/mo. Mixed evidence: 'frühstück shake' 2 conv (ROAS 1.78) but 'frühstücksshake' itself EUR 72, 0 conv. Breakfast terms already live in this AG (Breakfast AG paused)."),
    ("proteinreiches frühstück", "high-protein breakfast", E, G, "Meal replacement", "P3", "HARVEST",
     "1.5 conv on EUR 55. 6.6k/mo but much of it is recipe intent - exact only, low cap, recipe negatives apply."),

    # ---------------- Ready Meals (Hot & Savoury / instant meals) ----------------
    ("gesunde fertiggerichte", "healthy ready meals", E, G, "Ready Meals", "P1", "HARVEST",
     "5.5 conv, ROAS 1.80; 2.9k/mo. Exists only in paused 'Ready Meals OLD'."),
    ("protein fertiggerichte", "protein ready meals", E, G, "Ready Meals", "P1", "HARVEST",
     "5.3 conv, ROAS 2.21."),
    ("gesunde 5 minuten terrine", "healthy 5-minute cup meal", P, G, "Ready Meals", "P2", "HARVEST",
     "'5 minuten terrine' cluster: 7.9 conv, ROAS 1.15. The healthy/vegan modifiers convert; the bare Knorr term doesn't - so phrase on the modified version only."),
    ("5 minuten terrine vegan", "vegan 5-minute cup meal", E, G, "Ready Meals", "P2", "HARVEST",
     "2 conv, ROAS 4.58 ('vegane 5 minuten terrine' +1 conv)."),
    ("instant food", "instant food", E, G, "Ready Meals", "P2", "HARVEST",
     "2 conv, ROAS 6.35."),
    ("gesunde instant gerichte", "healthy instant meals", E, G, "Ready Meals", "P3", "HARVEST",
     "0.5 conv on EUR 46; direct description of Hot & Savoury."),
    ("fertiggerichte ohne kühlung", "ready meals without refrigeration / shelf-stable", E, G, "Ready Meals", "P3", "ADJACENT",
     "Shelf-stable is a Hot & Savoury advantage over Prep My Meal/Every Foods."),
    ("high protein fertiggerichte", "high-protein ready meals", E, G, "Ready Meals", "P3", "HARVEST",
     "2 conv but ROAS 0.69 - add exact to set its own bid rather than let broad overpay."),

    # ---------------- Protein ----------------
    ("proteinshake", "protein shake (compound)", E, G, "Protein", "P1", "HARVEST",
     "6.5 conv, ROAS 1.08; 40k/mo head term. Today it is served as a close variant of 'proteinpulver' [E] (112 of ~150 clicks), i.e. with protein-powder ad copy. Own exact = shake-specific copy and its own QS."),
    ("proteinpulver laktosefrei", "lactose-free protein powder", E, G, "Protein", "P1", "HARVEST",
     "3 conv, ROAS 3.58. Huel Complete Protein is plant-based so lactose-free by default."),
    ("laktosefreies proteinpulver", "lactose-free protein powder", E, G, "Protein", "P2", "ADJACENT",
     "1k/mo. Word-order sibling of the converting term above; EUR 57 via broad, no conversion yet - watch."),
    ("proteinpulver ohne süßungsmittel", "protein powder without sweeteners", E, G, "Protein", "P2", "HARVEST",
     "4 conv, ROAS 0.87; 3.2k/mo. Only in a paused AG today."),
    ("proteinpulver ohne zucker", "sugar-free protein powder", E, G, "Protein", "P2", "HARVEST",
     "2 conv, ROAS 1.11. Only in a paused AG today."),
    ("gesundes proteinpulver", "healthy protein powder", E, G, "Protein", "P2", "ADJACENT",
     "940/mo; seen in search terms. Matches Huel's 'complete nutrition' positioning."),
    ("bestes proteinpulver", "best protein powder", E, G, "Protein", "P3", "ADJACENT",
     "3.2k/mo. Comparison traffic - CPC ~EUR 1.80. Watch ROAS; 'beste trinkmahlzeit' [E] ran at 0.30."),

    # ---------------- Vegan ----------------
    ("proteinpulver vegan", "vegan protein powder", E, G, "Vegan", "P2", "HARVEST",
     "3 conv, ROAS 1.13; 3.2k/mo. Half its clicks go to the Protein AG via 'proteinpulver' [B] - exact pins it to Vegan copy."),
    ("erbsenprotein", "pea protein", E, G, "Vegan", "P3", "ADJACENT",
     "3.6k/mo. Huel Complete Protein's main protein source - ingredient-led searchers."),

    # ---------------- Weight Gain ----------------
    ("trinkmahlzeit zum zunehmen", "meal drink for gaining weight", E, G, "Weight Gain", "P1", "HARVEST",
     "3 conv, ROAS 1.72."),
    ("schnell zunehmen", "gain weight fast", E, G, "Weight Gain", "P2", "HARVEST",
     "3 conv, ROAS 3.50; 940/mo. Only in a paused AG; reached today via 'weight gainer' [B]."),
    ("hochkalorische nahrung", "high-calorie food", E, G, "Weight Gain", "P2", "HARVEST",
     "2.4 conv, ROAS 1.28; 2.9k/mo. Reached via 'kalorienshake' [B] today. Sits next to medical nutrition (Fresubin) - pair with the negatives on the Negatives tab."),
    ("veganer weight gainer", "vegan weight gainer", E, G, "Weight Gain", "P2", "HARVEST",
     "'vegan weight gainer' 1 conv on EUR 56; 'weight gainer vegan' EUR 67, 0 conv. Vegan gainers are scarce - Huel fit, but unproven."),
    ("getränk zum zunehmen", "drink for gaining weight", E, G, "Weight Gain", "P3", "ADJACENT",
     "210/mo; 'drink zum zunehmen' also appears in search terms."),

    # ---------------- Weight Loss ----------------
    ("shake zum abnehmen", "shake for losing weight", E, G, "Weight Loss", "P2", "ADJACENT",
     "5.4k/mo but only ~10 clicks in 6 months (close variant of 'diät shake' [E]) - we are barely showing. Exists only in paused AGs. CPC ~EUR 5.60, no conversion yet - add with its own keyword, monitor CPA."),
    ("trinkmahlzeit zum abnehmen", "meal drink for weight loss", E, G, "Weight Loss", "P1", "HARVEST",
     "2 conv, ROAS 1.46; 480/mo."),
    ("mahlzeitenersatz abnehmen", "meal replacement weight loss", E, G, "Weight Loss", "P2", "ADJACENT",
     "190/mo, CPC ~EUR 3.50. Exact match to Huel Lite / Powder WL positioning."),
    ("sättigende shakes zum abnehmen", "filling shakes for weight loss", E, G, "Weight Loss", "P3", "HARVEST",
     "600/mo; converted on EUR 10. Satiety (protein + fibre) is Huel's WL message."),
    ("veganer shake zum abnehmen", "vegan weight-loss shake", E, G, "Weight Loss", "P2", "ADJACENT",
     "170/mo. Vegan USP."),
    ("bester abnehmshake", "best weight-loss shake", E, G, "Weight Loss", "P3", "ADJACENT",
     "3.6k/mo, CPC ~EUR 4.40 - expensive comparison term. Test with a cap."),

    # ---------------- DE_SEARCH_BRAND > Products (Exact) : control, not incremental volume ----------------
    ("huel lite", "Huel Lite (product)", E, B, "Products (Exact)", "P1", "CONTROL",
     "707 clicks, 44.7 conv via 'huel' broad. Product-specific copy + LP should lift CVR."),
    ("huel ready to drink", "Huel Ready-to-drink (product)", E, B, "Products (Exact)", "P1", "CONTROL",
     "14.5 conv via broad. Send to the RTD page."),
    ("huel essential", "Huel Essential (product)", E, B, "Products (Exact)", "P1", "CONTROL",
     "22 conv via broad."),
    ("huel complete protein", "Huel Complete Protein (product)", E, B, "Products (Exact)", "P2", "CONTROL",
     "10 conv across exact/broad hits. 'huel protein' [E] is live but this is a different query."),
    ("huel pulver", "Huel powder", E, B, "Products (Exact)", "P2", "CONTROL",
     "24 conv across AGs. Route to Powder PDP."),
    ("huel riegel", "Huel bars", E, B, "Products (Exact)", "P2", "CONTROL",
     "13 conv via broad. Route to bars PDP."),
    ("huel ramen", "Huel ramen (Hot & Savoury flavour)", E, B, "Products (Exact)", "P2", "CONTROL",
     "13.9 conv via broad. Hot & Savoury / Instant Meals PDP."),
    ("huel probierpaket", "Huel sample/starter pack", E, B, "Products (Exact)", "P2", "CONTROL",
     "17.5 conv via broad ('starter kit' +6.6). Send to bundle/starter page."),
]

# Negatives to add alongside the expansion (keyword, english, level, where, why)
NEGATIVES = [
    ("fresubin", "Fresubin (medical nutrition brand)", "PHRASE", "DE_SEARCH_GENERIC (campaign)",
     "Protect new 'hochkalorische nahrung' / existing 'trinknahrung' from medical-nutrition traffic (49.5k/mo brand)."),
    ("fortimel", "Fortimel (medical nutrition brand)", "PHRASE", "DE_SEARCH_GENERIC (campaign)", "Same as above."),
    ("apotheke", "pharmacy", "PHRASE", "DE_SEARCH_GENERIC (campaign)", "Pharmacy-sourced medical drinks; not Huel."),
    ("senioren", "seniors", "PHRASE", "Weight Gain + Meal replacement", "Senior/clinical malnutrition intent (astronautennahrung für senioren, etc.)."),
    ("sondennahrung", "tube feeding", "PHRASE", "DE_SEARCH_GENERIC (campaign)", "Clinical intent."),
    ("rezept", "recipe", "PHRASE", "Ready Meals + Outdoor Food", "Recipe intent dominates 'fertiggerichte'/'camping essen' idea lists."),
    ("rezepte", "recipes", "PHRASE", "Ready Meals + Outdoor Food", "As above."),
    ("campingplatz", "campsite", "PHRASE", "Outdoor Food", "'camping essen' broad drifts to campsite restaurants (Knaus Campingpark etc.)."),
    ("knorr", "Knorr", "PHRASE", "Ready Meals", "Keep the bare Knorr '5 Minuten Terrine' brand searches out when adding the modified terrine terms."),
    ("trek n eat", "Trek'n Eat", "EXACT", "Outdoor Food", "Route to new Competitors - Outdoor Food AG."),
    ("adventure food", "Adventure Food", "EXACT", "Outdoor Food", "Route to new Competitors - Outdoor Food AG."),
    ("onek", "ONEK", "PHRASE", "Weight Gain", "Route to Competitors - Meal Replacement & Delivery."),
    ("biogena", "Biogena", "PHRASE", "Greens", "Route to Competitors - Greens."),
    ("prep meal", "prep meal", "EXACT", "Ready Meals", "Route to Competitors - Meal Replacement & Delivery."),
    ("metaflow", "Metaflow", "PHRASE", "Weight Loss", "Route to new Competitors - Diet Shakes AG."),
    ("sheko", "Sheko", "PHRASE", "Weight Loss", "Route to new Competitors - Diet Shakes AG."),
    ("more nutrition", "More Nutrition (brand)", "PHRASE", "DE_SEARCH_GENERIC (campaign)",
     "EUR 591 for 2 conv (ROAS 0.25) - huge brand volume, wrong buyer."),
]

# Converting terms already reached through a close variant of an EXACT keyword in the right ad group: no add needed
COVERED = {'trekking essen': 'trekking food / trekking eating', 'trekking food': 'trekking food', 'camping food': 'camping food', 'camping essen': 'camping food', 'camping mahlzeit': 'camping meal', 'outdoor essen': 'outdoor food', 'wandernahrung': 'hiking food', 'flüssige mahlzeit': 'liquid meal', 'flüssigmahlzeit': 'liquid meal (compound)', 'mass gainer': 'mass gainer', 'shakes zum zunehmen': 'shakes for gaining weight', 'zunehm shake': 'weight-gain shake', 'protein shake zum abnehmen': 'protein shake for weight loss', 'alternative zu ag1': 'alternative to AG1', 'ag1 ersatz': 'AG1 replacement', 'bestes veganes proteinpulver': 'best vegan protein powder', 'veganer proteinshake': 'vegan protein shake', 'green powder': 'green powder'}

# Considered and rejected - so the next person doesn't re-test them blindly
EXCLUDED = [
    ("astronautennahrung", "astronaut food (colloquial: medical high-calorie drinks)", "8.1k/mo",
     "Search terms: EUR 114 for 0.9 conv (ROAS 0.49). Searchers want Fresubin-style clinical drinks for seniors."),
    ("hochkalorische trinknahrung", "high-calorie drink nutrition", "4.4k/mo",
     "EUR 228 for 1.2 conv. Medical intent; the broader 'hochkalorische nahrung' converts better and is recommended instead."),
    ("fresubin / fortimel / trinknahrung apotheke", "medical nutrition brands", "50k+/mo",
     "Clinical products; added as negatives instead."),
    ("whey protein / whey isolat / clear whey", "whey protein", "55k/mo",
     "Every Huel protein product is plant-based. Whey terms converted a little (ROAS 1.5 on EUR 365) but product mismatch means poor LTV/returns risk. Revisit only with a 'whey alternative' angle."),
    ("proteinriegel / protein snack / gesunde snacks", "protein bar / snacks", "high",
     "Bar search terms: EUR 460 for 1 conv. Bar AG ROAS 0.67. Do not expand bars in Search."),
    ("more nutrition", "More Nutrition (brand)", "900k/mo",
     "EUR 591, 2 conv (ROAS 0.25). Added as a negative."),
    ("formula diät", "formula diet", "1.3k/mo",
     "Already an exact negative in Weight Loss (likely claims/medical reasons). Left alone."),
    ("almased / barebells / foodspring / esn / myprotein / protein works / myvegan / exante", "competitor brands", "-",
     "Excluded by the account's negatives / 'Agreement with Brands' list. Not recommended."),
    ("notfallnahrung / notvorrat / langzeitnahrung", "emergency food / long-life food", "~1.5k/mo",
     "Huel's ~12-month shelf life doesn't compete with 10-25-year emergency food; 'notfallnahrung' EUR 8, 0 conv."),
    ("schnelles mittagessen / mittagessen rezepte / kalorienarm X", "quick lunch / recipes / low-calorie X", "very high",
     "Recipe/informational intent; no conversions in search terms."),
    ("kollagen / gerstengras / maca / spirulina pulver", "collagen / barley grass / maca / spirulina powder", "high",
     "Single-ingredient supplements, not a greens-blend buyer. No account conversions."),
    ("zunehmen / gesund zunehmen", "gain weight / gain weight healthily", "2.9k / 1.3k",
     "Informational head terms ('zunehmen' EUR 86, 1 conv). Use the shake/drink-modified terms instead."),
    ("travellunch", "Travellunch (outdoor-meal brand)", "1k/mo",
     "Looks like a natural competitor add, but it already matched via broad: EUR 318 for 0.3 conv (ROAS 0.04). Consider a negative in Outdoor Food."),
    ("plenny shake", "Plenny Shake (Jimmy Joy product, without brand)", "390/mo",
     "EUR 157 for 0.4 conv (ROAS 0.13) without the brand; the branded 'jimmy joy plenny shake' converts and is recommended instead."),
    ("fertiggerichte lidl / aldi / rewe / frosta", "supermarket ready-meal brands", "high",
     "Retailer-navigational; buyer wants a supermarket product."),
]
