## HUEL - REST OF EUROPE PRODUCT FEED, LOCALISED (DE / FR / NL / IT / ES / PT / EL)
Source: "NEW ROE product feed" (68 rows). One tab per language. Each tab is the source feed copied exactly: same columns, same order, same values. Only these 4 columns change (orange headers): title, description, product_highlights, product_detail.
One column is ADDED to every tab, including EN (green header): custom_label_4, placed right after custom_label_3. It holds the feed language code: en, de, fr, nl, it, es, pt, el.

## LANGUAGE → COUNTRY (from the ROE_SHOPPING_STN_GENERIC targeting in Google Ads)
DE  → Austria, Switzerland
FR  → France, Belgium (Wallonia/Brussels), Switzerland (Romandy)
NL  → Netherlands, Belgium (Flanders)
IT  → Italy, Switzerland (Ticino)
ES  → Spain
PT  → Portugal
EL  → Greece
EN (source, unchanged) → Ireland, plus English-language searchers in every country
Not built: DA and FI. Denmark and Finland are targeted only by ROE_SEARCH_GENERIC, not by Shopping. Add them if Shopping expands there.

## HOW THE COPY WAS WRITTEN (commercial, not literal)
Title formula: [the local generic query people type] + Huel + range + flavour + key proof point (protein / kcal) + pack size. The first ~70 characters (what shows in the SERP) always hold the local category keyword plus the flavour. All titles are under 150 characters (Google limit 150).
Lead keywords per language (taken from ROE search terms where volume exists): DE Mahlzeitenersatz / Trinkmahlzeit / Proteinpulver / Proteinriegel / Fertiggericht · FR substitut de repas / repas à boire / barres protéinées / plat préparé · NL maaltijdshake / maaltijdvervanger / drinkmaaltijd / eiwitpoeder / eiwitrepen · IT pasto sostitutivo / barrette proteiche / proteine in polvere / piatto pronto proteico · ES batido sustitutivo de comida / proteína vegana / barritas de proteína / comida preparada · PT substituto de refeição · EL υποκατάστατο γεύματος.
Descriptions keep every fact in the English source (protein grams, fibre, 26 vitamins & minerals, pack sizes, kcal) and add no new claims. The source health claims (ramen: muscle, energy, immune, skin/hair/nails) use the wording of the authorised EU claims register (Reg. 432/2012) in each language.
Deliberately NOT added: weight-loss wording ("abnehmen", "adelgazar", "minceur" and similar). It shows up in search terms, but weight-control claims on meal replacements are tightly regulated in the EU (Reg. 1924/2006, Reg. 2016/1813), and Google's health policies apply too. "Low calorie" / "kalorienarm" was also avoided: Lite Ramen is about 350 kcal/100 g, so it does not qualify for that claim. "Under 230 kcal" is used instead.
Brand "Huel" was added to every title. The source titles don't include it, and Google's title best practice puts brand in the title.

## GOOGLE SPEC VALIDATION - WHAT DOES / DOESN'T NEED TRANSLATING
title, description → TRANSLATED. These are shown to shoppers and must be in the feed's content language.
product_highlight → TRANSLATED. Shown to shoppers. Google: "Describe only the product itself... Don't provide your business's history or policies"; foreign-language words are not allowed. The source contains "Free mainland UK delivery over £45" on the 7 ramen rows. That is a shipping/policy claim, and it is wrong for EU customers, so it was removed from every translation. Empty "" items in the source were also removed (minimum 2, recommended 4-6 per product).
product_detail → TRANSLATED. Shown to shoppers as structured spec rows. section_name, attribute_name and attribute_value were all localised.
google_product_category (5702) → KEEP. A numeric ID is language-neutral. Google: "If the taxonomy... isn't available in your language, use the English values or numeric ID."
product_type → KEEP IN ENGLISH. Your own internal taxonomy, used for bidding and reporting. It is not shown to shoppers. Keeping it identical keeps reporting comparable across languages.
custom_label_0-3 → KEEP IN ENGLISH (critical). The ROE Shopping campaigns subdivide product groups on custom_label_0. Translating it would drop every product into "Everything else".
custom_label_4 → NEW: feed language (en/de/fr/nl/it/es/pt/el). For reporting in Google Ads, segment by "Custom label 4" in the Products / Product groups report (API: segments.product_custom_attribute4). Because Belgium and Switzerland run 2-3 languages, this is the only way to split performance by language there. Not used in any product group today, so bidding is unaffected. If you later want separate bids per language, subdivide product groups on it. Values are lowercase because Google Ads lowercases custom labels anyway.
Merchant Center: custom_label_4 must be in all 8 data sources, including the English one. Otherwise the EN products show up as "(not set)" in reports.
shipping_label, shipping, free_shipping_threshold, price, availability, condition, brand, gtin, mpn, ids, links, images → KEEP.

## HOW TO SET IT UP IN MERCHANT CENTER (account 5348230986, feed label ROE_FEED)
1. Create one data source per language. Use the same feed label (ROE_FEED) so the existing ROE Shopping campaigns pick them up, set the content language to DE/FR/NL/IT/ES/PT/EL, and target the countries above. Belgium and Switzerland get 2-3 data sources each. That is supported: Google serves the version that matches the user's language.
2. Keep the English source data source live with all countries. It serves IE and English-language searchers. Shopping matches today are mostly English queries ("yfood", "protein powder", "meal replacement shakes") because the feed is English. The local-language feeds add coverage on local queries; they don't replace the English matches.
3. LANDING PAGE LANGUAGE: Google expects the landing page in the same language as the feed. Every link points to eu.huel.com (one row uses /de-at/). If eu.huel.com has locale paths (e.g. /fr-fr/, /nl-nl/), swap the link column per tab before upload. I could not verify this from here, so please confirm.
4. Switzerland: prices are in EUR. Confirm Merchant Center currency conversion is on for CH, or add CHF prices.

## DATA ISSUES FOUND IN THE SOURCE FEED (copied as-is; fix in the source before or after upload)
1. DUPLICATE ID: row 9 (Black Edition Unflavoured & Unsweetened) uses id BLK-CC-11-EDP and GTIN 5060495115325, the same as row 2 (Coffee Caramel). Merchant Center keeps only one of the two. The Unflavoured BE needs its own id and GTIN.
2. Row 10 (BLK-MAT-11-EDP, Matcha Latte): the English title says "Unflavoured & Unsweetened". The localised titles use Matcha Latte. Its link points to /de-at/ unlike every other row.
3. DUPLICATE GTIN: RTB-VAN-10-DE and RTB-COF-10-DE (Vanilla and Iced Latte RTD) both use 5060925294590.
4. Broken links: PGF-VA-30-EDP and RAB6-ABF-10 use "/1/ot=onetime" (should be "/1?ot=onetime"). PGF-CH-30-EDP has a trailing ". " after the URL. GRE-WAT-20R-EDP-EDP is missing "/1?ot=onetime".
5. Custom label mismatch (performance risk): ROE_SHOPPING_STN_GENERIC splits on custom_label_0 values 'be powder', 'bars', 'rtd', 'protein', 'gluten-free powder', 'hot savoury', 'instant noodle pot'. This feed uses 'Black Edition Powder', 'Protein Bars', 'Ready to drink', 'Complete Protein', 'Gluten Free Powder', 'H&S Meal Packs', 'Lite Ramen', 'Black Edition Ramen'. Only some values match (black edition powder, black edition rtd, complete protein, daily greens, essentials, gluten free powder, h&s meal packs, powder, protein bars, ready to drink). Lite Ramen and Black Edition Ramen match no group in either campaign. Align the labels or the product groups.
6. Inconsistent facts in the English source, kept as given: bars say 14g protein in product_detail but 15g in some descriptions. Classic RTD highlight says 20g protein, the description says "up to 22g" (translations follow the description). Madras description calls it "Spicy Indian Curry" and Mexican Chilli is spelled "Chili". BE powder titles say 1.5kg but unit pricing is 1530g (translations use 1,53 kg). Essentials title says 2.3kg but unit pricing is 2250g (translations use 2,25 kg).
7. Ramen rows (RAL6/RAB6) have no unit_pricing values. Bars Selection Box (15 bars) has unit_pricing_measure 660g, the same as the 12-bar packs.
8. Malformed highlight quoting: PGF-SC, POW-SC, PTN-SCA (missing opening quote) and ESS-CHO/VAN (missing comma). Fixed in the translations.
9. Some ids are double-suffixed (…-EDP-EDP), and RTB ids end in -DE. Harmless, but worth tidying with the id fixes.

## TABS
READ ME · EN (source) · one feed tab per language · Search term check (local search terms vs. titles) · Title review (EN vs. all languages side by side)
Copy should get a native-speaker spot check before going live, especially EL and PT, and brand/legal review of the claims wording.
