"""v2: closest-match additions per ad group, each checked against that ad group's landing page.

AD_GROUPS: ad group -> (campaign, landing page, what the page sells, status note)
ROWS: (keyword_de, english, match, ad_group, priority, closest_existing_keyword, page_proof, why)
  page_proof = the claim on the landing page that makes the keyword a fair promise.
"""

BE = "de.huel.com/products/huel-black-edition"
HS = "de.huel.com/products/hot-and-savoury-meal-packs"
CP = "de.huel.com/products/huel-complete-protein"
DG = "de.huel.com/products/huel-daily-greens"
BAR = "de.huel.com/products/huel-bar"
HOME = "de.huel.com (homepage)"

AD_GROUPS = {
    "Meal replacement": ("DE_SEARCH_GENERIC", BE, "Black Edition - powdered complete meal: 400 kcal, 40 g protein, 27 vitamins & minerals, vegan, no artificial sweeteners, 'high-protein breakfast or lunch', from ~€2.65 a meal", "existing"),
    "Weight Loss": ("DE_SEARCH_GENERIC", BE, "Black Edition (one ad uses Huel Lite RTD). Page FAQ: 'Can Huel Black Edition help with weight loss?'; 400 kcal meal, 40 g protein, up to 11 g fibre", "existing"),
    "Weight Gain": ("DE_SEARCH_GENERIC", BE, "Black Edition - 400 kcal / 40 g protein meal shake. NB: page has no weight-gain messaging; it is a meal, not a 1,000+ kcal gainer", "existing"),
    "Ready Meals": ("DE_SEARCH_GENERIC", HS, "Hot & Savoury - instant hot meals (pasta, curry, noodles), just add hot water, up to 25 g protein, vegan, some flavours gluten-free, ~€3.95 a meal", "existing"),
    "Outdoor Food": ("DE_SEARCH_GENERIC", HS, "Hot & Savoury - instant, add hot water, freeze-dried vegetables, vegan. NB: page never mentions outdoor/trekking", "existing"),
    "NEW: Competitors - Outdoor Food": ("DE_SEARCH_GENERIC", HS, "Hot & Savoury (as Outdoor Food)", "new"),
    "Competitors - Meal Replacement & Delivery": ("DE_SEARCH_GENERIC", HS, "Hot & Savoury - fits meal-kit / ready-meal brands (HelloFresh, Dinnerly, Prep My Meal, Löwenanteil, YouCook, Every Foods). Does NOT fit shake brands", "existing"),
    "NEW: Competitors - Meal Shakes": ("DE_SEARCH_GENERIC", BE, "Black Edition - the shake that yfood / Soylent / Jimmy Joy / Saturo buyers are comparing", "new"),
    "NEW: Competitors - Diet Shakes": ("DE_SEARCH_GENERIC", BE, "Black Edition (weight-loss FAQ) - or Huel Lite RTD if that page is live in DE", "new"),
    "Protein": ("DE_SEARCH_GENERIC", CP, "Complete Protein - plant protein powder, 20 g protein, complete amino acids, 27 vitamins & minerals, vegan, gluten-free, no soy, 'support training, recovery'. NB: page does NOT claim no-sweetener or sugar-free", "existing"),
    "Vegan": ("DE_SEARCH_GENERIC", CP, "Complete Protein (as above) - 100% vegan, plant-based, no soy", "existing"),
    "Greens": ("DE_SEARCH_GENERIC", DG, "Daily Greens - super-greens powder, 91 ingredients incl. organic greens, probiotics, adaptogens, vitamins & minerals, vegan, gluten-free, no artificial sweeteners", "existing"),
    "Competitors - Greens": ("DE_SEARCH_GENERIC", DG, "Daily Greens (as above) - positioned against AG1 on taste and price (from ~€1.50 a serving)", "existing"),
    "Bar": ("DE_SEARCH_GENERIC", BAR, "Complete Nutrition Bar - up to 14 g protein, 2 g sugar, vegan, 27 vitamins & minerals", "existing"),
    "Competitors - Protein": ("DE_SEARCH_GENERIC", CP, "Complete Protein", "existing"),
    "Products (Exact)": ("DE_SEARCH_BRAND", HOME, "All brand ads go to the homepage - no product pages", "existing"),
}

E, P = "Exact", "Phrase"
ROWS = [
    # ---------- Meal replacement -> Black Edition ----------
    ("mahlzeitenersatz shake", "meal replacement shake", E, "Meal replacement", "P1", "Mahlzeitenersatz", "'Is Huel Black Edition a meal replacement?' FAQ; shake format",
     "Closest variant of the AG's core keyword; 4 conversions at ROAS 2.4 already."),
    ("trinkmahlzeit pulver", "meal drink powder", E, "Meal replacement", "P1", "Trinkmahlzeit", "Powder you scoop and shake",
     "Powder-format buyers = exactly this product. 5.5 conversions."),
    ("protein trinkmahlzeit", "protein meal drink", E, "Meal replacement", "P1", "Trinkmahlzeit", "40 g protein per meal",
     "Black Edition's headline claim; ROAS 4.0 on small spend."),
    ("protein shake als mahlzeitenersatz", "protein shake as a meal replacement", E, "Meal replacement", "P1", "Mahlzeitenersatz", "Page headline: 'This is a meal. Not another protein shake.'",
     "The page is written for exactly this searcher."),
    ("proteinreiches frühstück", "high-protein breakfast", E, "Meal replacement", "P2", "frühstück", "Comparison table: 'High-protein breakfast or lunch'",
     "6.6k/month and literally the page's positioning. Exact only - much of the volume is recipe-seeking."),
    ("schnelles gesundes frühstück", "quick healthy breakfast", E, "Meal replacement", "P2", "Gesundes Frühstück", "'A complete meal in seconds'",
     "'Gesundes Frühstück' is one of the AG's better keywords (ROAS 1.27); the 'quick' version matches the page's speed claim."),
    ("trinkmahlzeit test", "meal drink test/review", E, "Meal replacement", "P2", "Trinkmahlzeit", "Taste guarantee; '4,000,000 satisfied customers'",
     "Comparison shoppers; 2.2 conversions already."),
    ("trinkmahlzeit testsieger", "best-rated meal drink", E, "Meal replacement", "P3", "Trinkmahlzeit", "As above", "Same comparison intent."),
    ("trinkmahlzeit günstig", "cheap meal drink", E, "Meal replacement", "P2", "Trinkmahlzeit", "'Save money - from €2.65 per meal'",
     "Price is a stated benefit; ROAS 8.3 on small spend."),
    ("gesunde trinkmahlzeit", "healthy meal drink", E, "Meal replacement", "P3", "Trinkmahlzeit", "27 vitamins & minerals, 'over 160 health benefits'", "Health framing the page leads with."),
    ("mahlzeitenersatz pulver", "meal replacement powder", E, "Meal replacement", "P3", "Mahlzeitenersatz", "Powder format", "Format-specific variant of the core keyword."),
    ("trinkmahlzeit ohne milch", "dairy-free meal drink", E, "Meal replacement", "P2", "Trinkmahlzeit", "100% vegan / plant-based",
     "Dairy-free is a real difference vs yfood and Saturo; 2 conversions."),
    ("gesundes frühstück für unterwegs", "healthy breakfast on the go", E, "Meal replacement", "P3", "Gesundes Frühstück", "'Scoop, shake, go'", "On-the-go breakfast = the use case on the page."),

    # ---------- Weight Loss -> Black Edition ----------
    ("abnehm protein shake", "weight-loss protein shake", E, "Weight Loss", "P1", "abnehm shake", "FAQ 'Can Huel Black Edition help with weight loss?'; 40 g protein",
     "Closest variant of the AG's best keyword (abnehm shake, ROAS 1.15)."),
    ("abnehm shake test", "weight-loss shake test", E, "Weight Loss", "P2", "abnehm shake", "Taste guarantee", "1.6k/month comparison searches."),
    ("abnehm shake testsieger", "best-rated weight-loss shake", E, "Weight Loss", "P3", "abnehm shake", "As above", "Same comparison intent."),
    ("abnehm shake vegan", "vegan weight-loss shake", E, "Weight Loss", "P2", "abnehm shake", "100% vegan", "Vegan is something most diet shakes (Almased, Layenberger) can't claim."),
    ("abnehm shake ohne süßungsmittel", "weight-loss shake without sweeteners", E, "Weight Loss", "P3", "abnehm shake", "'No artificial sweeteners'", "Small but a claim the page makes explicitly."),
    ("trinkmahlzeit zum abnehmen", "meal drink for weight loss", E, "Weight Loss", "P1", "diät shake", "400 kcal complete meal; weight-loss FAQ", "2 conversions at ROAS 1.5."),
    ("shake zum abnehmen", "shake for losing weight", E, "Weight Loss", "P2", "abnehm shake", "Weight-loss FAQ", "5.4k/month; we barely show on it today."),
    ("mahlzeitenersatz abnehmen", "meal replacement for weight loss", E, "Weight Loss", "P2", "diät shake", "Meal-replacement + weight-loss FAQ", "Both halves of the query are on the page."),
    ("sättigende shakes zum abnehmen", "filling shakes for weight loss", E, "Weight Loss", "P3", "diät shake", "Up to 11 g fibre, 40 g protein ('Properly filling')", "Satiety is the honest weight-loss angle."),

    # ---------- Weight Gain -> Black Edition ----------
    ("protein shake zum zunehmen", "protein shake for gaining weight", E, "Weight Gain", "P1", "zunehmen shake", "40 g protein, 400 kcal per serving",
     "Closest variant of the AG's main keyword. A protein-led shake is a fair promise; a 'gainer' isn't."),
    ("schnell zunehmen shake", "shake to gain weight fast", E, "Weight Gain", "P2", "zunehmen shake", "400 kcal per serving", "'schnell zunehmen' converted at ROAS 3.5."),
    ("veganer weight gainer", "vegan weight gainer", E, "Weight Gain", "P3", "weight gainer", "100% vegan", "Vegan gainers are rare; but the page is not a gainer - test only."),
    ("kalorien shake zum zunehmen", "calorie shake for gaining weight", E, "Weight Gain", "P3", "kalorienshake", "400 kcal per serving", "Closest variant of 'kalorienshake'."),

    # ---------- Ready Meals -> Hot & Savoury ----------
    ("gesunde fertiggerichte", "healthy ready meals", E, "Ready Meals", "P1", "fertiggerichte", "'100% nutritionally complete', 27 vitamins & minerals",
     "5.5 conversions at ROAS 1.8; only exists in a paused AG."),
    ("protein fertiggerichte", "protein ready meals", E, "Ready Meals", "P1", "fertiggerichte", "'Up to 25 g protein per meal'", "5.3 conversions at ROAS 2.2."),
    ("high protein fertiggerichte", "high-protein ready meals", E, "Ready Meals", "P2", "fertiggerichte", "'Up to 25 g protein per meal'", "1k/month; same claim."),
    ("fertiggerichte vegan", "vegan ready meals", E, "Ready Meals", "P1", "fertiggerichte", "100% vegan",
     "880/month. NB 'vegane fertiggerichte' sits in Meal replacement and lands on the shake page - this keeps vegan meals on the meals page."),
    ("glutenfreie fertiggerichte", "gluten-free ready meals", E, "Ready Meals", "P3", "fertiggerichte", "Some flavours marked gluten-free", "Only part of the range qualifies - test."),
    ("fertiggerichte bestellen", "order ready meals", E, "Ready Meals", "P2", "fertiggerichte", "Online subscription / box ordering", "2.4k/month order intent, buyable on the page."),
    ("gesunde fertiggerichte bestellen", "order healthy ready meals", E, "Ready Meals", "P3", "fertiggerichte", "As above", "Narrower, higher-intent version."),
    ("5 minuten terrine vegan", "vegan 5-minute cup meal", E, "Ready Meals", "P2", "fertiggerichte", "'Just add hot water', ready in minutes, vegan", "2 conversions at ROAS 4.6."),
    ("instant food", "instant food", E, "Ready Meals", "P2", "fertiggerichte", "'Hot & tasty instant meals'", "2 conversions at ROAS 6.4."),

    # ---------- Outdoor Food -> Hot & Savoury ----------
    ("gefriergetrocknetes essen", "freeze-dried food", E, "Outdoor Food", "P1", "gefriergetrocknete mahlzeiten", "'Vegetables are freeze-dried'; add hot water",
     "Closest variant of the AG's best keyword (ROAS 2.25)."),
    ("gefriergetrocknete gerichte", "freeze-dried dishes", E, "Outdoor Food", "P1", "gefriergetrocknete mahlzeiten", "As above", "ROAS 5.7 on small spend."),
    ("vegane trekkingnahrung", "vegan trekking food", P, "Outdoor Food", "P1", "trekking nahrung", "100% vegan; add hot water", "Converting; vegan is rare in freeze-dried outdoor food."),
    ("günstige outdoor nahrung", "cheap outdoor food", E, "Outdoor Food", "P3", "outdoor nahrung", "~€3.95 a meal (outdoor brands are €8-12)", "Closest variant DataforSEO finds; price is a real edge."),
    ("tactical food", "tactical food", E, "Outdoor Food", "P2", "outdoor nahrung", "Instant, shelf-stable meal", "4 conversions at ROAS 1.9."),
    ("trek n eat", "Trek'n Eat (brand)", E, "NEW: Competitors - Outdoor Food", "P1", "outdoor nahrung", "Same use: add hot water, cheaper, vegan", "12 conversions, but shown generic copy today."),
    ("adventure food", "Adventure Food (brand)", E, "NEW: Competitors - Outdoor Food", "P1", "outdoor nahrung", "As above", "7.5 conversions at ROAS 2.3."),

    # ---------- Competitors - Meal Replacement & Delivery -> Hot & Savoury (meal brands only) ----------
    ("prep my meal", "Prep My Meal (meal-prep delivery)", E, "Competitors - Meal Replacement & Delivery", "P1", "dinnerly", "Ready meals, no cooking, cheaper per meal",
     "45 conversions with no keyword (came via 'dinnerly')."),
    ("prep my meal alternative", "Prep My Meal alternative", E, "Competitors - Meal Replacement & Delivery", "P1", "dinnerly", "As above", "13 conversions at ROAS 1.2."),
    ("hello fresh alternative", "HelloFresh alternative", E, "Competitors - Meal Replacement & Delivery", "P1", "hello fresh", "'No cooking needed - just add hot water'",
     "Closest variant of 'hello fresh' (1.3k/month); the no-cooking message answers it directly."),
    ("löwenanteil alternative", "Löwenanteil alternative", E, "Competitors - Meal Replacement & Delivery", "P2", "löwenanteil", "Shelf-stable instant meals, vegan", "3 conversions at ROAS 2.0."),
    ("löwenanteil erfahrung", "Löwenanteil reviews", E, "Competitors - Meal Replacement & Delivery", "P3", "löwenanteil", "As above", "590/month research-stage searches."),
    ("youcook alternative", "YouCook alternative", E, "Competitors - Meal Replacement & Delivery", "P3", "youcook", "Healthier ready meal, 25 g protein", "Switching intent from a ready-meal brand."),
    ("every foods", "Every Foods (frozen meals)", E, "Competitors - Meal Replacement & Delivery", "P1", "dinnerly", "Ready meals, no freezer needed", "4 conversions at ROAS 2.1."),
    ("tellerglück", "Tellerglück (healthy ready meals)", E, "Competitors - Meal Replacement & Delivery", "P2", "dinnerly", "Healthy ready meals", "2.3 conversions at ROAS 1.9."),

    # ---------- NEW: Competitors - Meal Shakes -> Black Edition ----------
    ("yfood alternative", "yfood alternative", E, "NEW: Competitors - Meal Shakes", "P1", "yfood", "Powdered complete meal, cheaper per meal, vegan",
     "5 conversions; today it lands on the Hot & Savoury page."),
    ("yfood vegan", "yfood vegan", E, "NEW: Competitors - Meal Shakes", "P2", "yfood", "100% vegan (yfood is milk-based)", "720/month; a clear Huel advantage."),
    ("yfood pulver", "yfood powder", E, "NEW: Competitors - Meal Shakes", "P2", "yfood", "Powder format", "3.5 conversions at ROAS 1.7."),
    ("this is food", "This Is Food (yfood product)", E, "NEW: Competitors - Meal Shakes", "P1", "yfood", "Shake vs shake", "5 conversions at ROAS 2.1."),
    ("jimmy joy plenny shake", "Jimmy Joy Plenny Shake", E, "NEW: Competitors - Meal Shakes", "P1", "jimmy joy", "Shake vs shake", "4.6 conversions at ROAS 1.8."),
    ("metaflow alternative", "Metaflow alternative (diet shake)", E, "NEW: Competitors - Diet Shakes", "P2", "abnehm shake", "Weight-loss FAQ, 40 g protein", "2 conversions at ROAS 1.6."),
    ("sheko shake", "Sheko shake (diet shake)", E, "NEW: Competitors - Diet Shakes", "P2", "abnehm shake", "As above", "Early conversions; 22k/month."),

    # ---------- Protein -> Complete Protein ----------
    ("proteinshake", "protein shake", E, "Protein", "P1", "protein shake", "Protein powder you shake",
     "40k/month; currently served via 'proteinpulver' [E] with powder copy."),
    ("eiweißpulver zum muskelaufbau", "protein powder for muscle building", E, "Protein", "P1", "eiweißpulver", "'Support training, recovery'; complete amino acids",
     "720/month. Better home than 'muskelaufbau protein' in Weight Gain (ROAS 0.47 on the meal-shake page)."),
    ("protein shake zum muskelaufbau", "protein shake for muscle building", E, "Protein", "P2", "protein shake", "As above", "720/month."),
    ("pflanzliches proteinpulver", "plant protein powder", E, "Protein", "P1", "proteinpulver", "Plant-based protein, complete amino acid profile", "880/month."),
    ("veganes eiweißpulver", "vegan protein powder", E, "Protein", "P1", "eiweißpulver", "100% vegan", "1k/month; 'eiweißpulver' twin of a converting term."),
    ("proteinpulver laktosefrei", "lactose-free protein powder", E, "Protein", "P1", "proteinpulver", "100% vegan (so dairy-free)", "3 conversions at ROAS 3.6."),
    ("proteinpulver gesund", "healthy protein powder", E, "Protein", "P2", "proteinpulver", "FAQ 'Is Huel Complete Protein good for you?'; 27 vitamins & minerals", "1k/month."),
    ("proteinpulver test", "protein powder test", E, "Protein", "P2", "proteinpulver", "Taste guarantee", "9.9k/month comparison searches - watch CPA."),
    ("gutes proteinpulver", "good protein powder", E, "Protein", "P3", "proteinpulver", "As above", "1.3k/month."),

    # ---------- Vegan -> Complete Protein ----------
    ("veganes proteinpulver ohne soja", "soy-free vegan protein powder", E, "Vegan", "P1", "veganes proteinpulver", "'No soy' badge on the page", "390/month; most vegan proteins are soy-based - a real edge."),
    ("proteinpulver vegan", "vegan protein powder", E, "Vegan", "P2", "veganes proteinpulver", "100% vegan", "3 conversions; half its clicks go to the Protein AG today."),
    ("veganes proteinpulver test", "vegan protein powder test", E, "Vegan", "P2", "veganes proteinpulver", "Taste guarantee", "1.6k/month."),
    ("vegan protein shakes", "vegan protein shakes", E, "Vegan", "P2", "vegan protein", "Vegan protein powder for shakes", "720/month."),

    # ---------- Greens -> Daily Greens ----------
    ("super greens pulver", "super greens powder", E, "Greens", "P1", "super greens", "Page title: 'Supergreens powder'", "Closest variant of a live keyword; the page's own words."),
    ("grünes superfood pulver", "green superfood powder", E, "Greens", "P1", "grünes pulver", "'91 superfoods, greens and essential nutrients'", "390/month."),
    ("superfood greens pulver", "superfood greens powder", E, "Greens", "P2", "greens pulver", "As above", "480/month."),
    ("greens pulver test", "greens powder test", E, "Greens", "P2", "greens pulver", "'A greens powder that actually tastes good'", "Comparison searches; taste is the page's pitch."),
    ("multivitamin pulver", "multivitamin powder", E, "Greens", "P2", "multivitamin", "Vitamins & minerals in powder form", "Closer to the product than plain 'multivitamin' (which is mostly tablets)."),
    ("veganes multivitamin", "vegan multivitamin", E, "Greens", "P3", "multivitamin", "100% vegan", "170/month."),
    ("nahrungsergänzungsmittel vegan", "vegan supplements", E, "Greens", "P3", "nahrungsergänzungsmittel", "100% vegan", "320/month."),

    # ---------- Competitors - Greens -> Daily Greens ----------
    ("ag1 erfahrungen", "AG1 reviews", E, "Competitors - Greens", "P2", "ag1", "Taste + price vs AG1", "6.3 conversions; review-angle copy."),
    ("ag1 test", "AG1 test", E, "Competitors - Greens", "P2", "ag1", "As above", "1.6k/month."),
    ("ag1 inhaltsstoffe", "AG1 ingredients", E, "Competitors - Greens", "P2", "ag1", "'91 vitamins, minerals and superfoods' - an ingredient comparison", "ROAS 7.9 on small spend."),
    ("biogena one", "Biogena One (greens brand)", E, "Competitors - Greens", "P2", "ag1", "Greens + vitamins all-in-one", "2 conversions; currently on generic Greens copy."),

    # ---------- Bar -> Complete Nutrition Bar (test only) ----------
    ("veganer protein snack", "vegan protein snack", E, "Bar", "P3", "protein snack", "Vegan, up to 14 g protein", "Closest fit, but bar search terms have barely converted (Bar ROAS 0.67) - test only."),
    ("vegane schokoriegel", "vegan chocolate bars", E, "Bar", "P3", "schokoriegel", "Vegan; chocolate flavours; 2 g sugar", "590/month - same caveat."),

    # ---------- Brand -> needs product URLs ----------
    ("huel lite", "Huel Lite", E, "Products (Exact)", "P1", "huel (Huel Exact)", "Set final URL to the Huel Lite page", "45 conversions with no keyword; today lands on the homepage."),
    ("huel ready to drink", "Huel Ready-to-drink", E, "Products (Exact)", "P1", "huel (Huel Exact)", "Set final URL to the RTD page", "14.5 conversions via broad."),
    ("huel essential", "Huel Essential", E, "Products (Exact)", "P1", "huel (Huel Exact)", "Set final URL to the Essential page", "22 conversions via broad."),
    ("huel complete protein", "Huel Complete Protein", E, "Products (Exact)", "P2", "huel protein", "Final URL: " + CP, "10 conversions."),
    ("huel riegel", "Huel bars", E, "Products (Exact)", "P2", "huel (Huel Exact)", "Final URL: " + BAR, "13 conversions."),
    ("huel ramen", "Huel ramen", E, "Products (Exact)", "P2", "huel hot and savoury", "Final URL: " + HS, "14 conversions."),
]

# Existing keywords whose landing page doesn't fit (data May-Nov)
LP_FIXES = [
    ("proteinriegel", "Meal replacement", "Black Edition shake page", "€936 · 2 conversions · ROAS 0.24", "Pause (bar terms don't convert in Search) - or move to Bar."),
    ("muskelaufbau protein", "Weight Gain", "Black Edition meal page", "€1,347 · 9 conversions · ROAS 0.47", "Move to Protein (Complete Protein page talks training and recovery)."),
    ("gesunde schokolade", "Meal replacement", "Black Edition shake page", "€5 · 0 conversions", "Pause - nothing on the page about chocolate."),
    ("yfood, soylent, mana, saturo, jimmy joy, shape republic, vly food", "Competitors - Meal Replacement & Delivery", "Hot & Savoury meals page",
     "yfood €5.8k ROAS 0.87 · soylent €5.0k ROAS 1.18 · jimmy joy €536 ROAS 0.98", "Shake buyers land on hot meals. Move to new 'Competitors - Meal Shakes' with the Black Edition page; run it as an experiment as soylent already performs OK."),
    ("seitenbacher", "Competitors - Meal Replacement & Delivery", "Hot & Savoury meals page", "€0", "Muesli brand - no fit with any Huel page. Remove."),
    ("vegane fertiggerichte, fertiggerichte", "Meal replacement", "Black Edition shake page", "€1,094 ROAS 1.15 · €541 ROAS 1.31",
     "Ready-meal searches on the shake page - they perform fine, so don't move blindly: test 'fertiggerichte vegan' in Ready Meals first and compare."),
    ("all keywords in Products (Exact)", "DE_SEARCH_BRAND", "Homepage", "huel black edition, daily greens, protein, hot and savoury",
     "Add keyword-level final URLs to each product page."),
]

# LP check removed these from the v1 list
DROPPED = [
    ("proteinpulver ohne süßungsmittel", "protein powder without sweeteners", "Complete Protein page claims no artificial flavours/colours, but NOT no sweeteners."),
    ("proteinpulver ohne zucker", "sugar-free protein powder", "Page says 'low in sugar', not sugar-free."),
    ("erbsenprotein", "pea protein", "Page doesn't name pea as the protein source."),
    ("onek", "ONEK (weight-gain brand)", "Black Edition page has no weight-gain message - a gainer brand would land on the wrong promise."),
    ("hochkalorische nahrung", "high-calorie food", "Medical/clinical intent; a 400 kcal meal page doesn't answer it."),
    ("gesunde 5 minuten terrine / gesunde instant gerichte / fertiggerichte ohne kühlung", "cup meals / shelf-stable meals", "Covered by the higher-volume H&S terms above; low volume."),
    ("bester abnehmshake / veganer shake zum abnehmen / layenberger shake / metaflow shake / sheko alternative", "various WL comparison terms", "Kept the strongest WL variants only; these are thin or expensive."),
    ("protein für muskelaufbau / wieviel protein pro tag", "protein for muscle building", "Mostly informational ('how much protein') - the page sells a product, not advice."),
    ("low carb frühstück / frühstück vegan / low carb diät", "low-carb / vegan breakfast", "6-10k/month but dominated by recipes and café searches."),
    ("whey / clear whey / isolat", "whey protein", "Every Huel protein is plant-based."),
]
