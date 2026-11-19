# UK Google Ads plan (19 Nov 2026)

Account: Huel UK (3455924316). Reviewed with an Opus reviewer working from the same data.

**Context**
- **UK Nov MTD:** new customers at 88% of target, CPA £37.34 against a £33 target (113%).
- **Fospha DDA+ 4-week CAC:** Shopping £165, Search £175, Meta £161, Demand Gen £1,110.
- **Demand Gen's budget is protected.**

## Actions
1. **Demand Gen TEST (prospecting): switch to new customers only.**
   - **Why:** the budget is fixed, so make it buy the KPI. Right now no customer-acquisition goal is set, so it bids on every purchase.
   - **Check first:** the new-customer share of its conversions (it needs about 200 or more a month to keep learning), and that the customer list is fresh.
   - **Fallback:** if the setting isn't offered, exclude past purchasers (the Customer Match list plus 540-day site purchasers).
2. **Demand Gen: remove the "Parents" and "Female Focused" ad groups.** They spent £194 for 0 conversions. This is housekeeping.
3. **Get the Fospha Demand Gen numbers by month for Aug–Nov.**
   - **Why:** the 5 Oct split into TEST plus retargeting coincides with platform ROAS falling from about 1.9 to about 0.6 at a similar spend, and with eligible UK brand-search demand falling about 28%.
   - **Decision rule:** if Aug–Sep delivered clearly more DDA+ new customers, restore the pre-split setup.
4. **Set up a Conversion Lift study on Demand Gen.** Use a user-level holdout, measure new-customer purchases, and add a Search Lift on "huel". Run it for 3–4 weeks. It doesn't cut spend, so it fits the protected budget.
5. **Ask Huel and Fospha to report Demand Gen separately from Google non-brand.**
   - **Why:** with Demand Gen included, non-brand CAC reads £215. Without it, Shopping plus Search is £170.
6. **UK_SEARCH_WEIGHT_LOSS: raise tROAS from 75% back to 82%.**
   - **Why:** since the 22 Oct loosening, spend is up 26%, and the extra conversions cost about £135 each on the platform, or roughly £300 per Fospha new customer.
7. **UK_SHOPPING_STANDARD_BRAND: add negatives now for non-brand terms** ("freeze dried meals", "foods to stockpile", "morrisons", and similar). Then run a 2-week test of +20% max CPC on brand terms only.
   - **Why:** non-brand terms take about 24% of visible spend at an £83 CPA, against £6 for "huel" terms. The campaign loses 41% of IS to rank.

## Not doing
- **No pause or cut to Demand Gen,** because its budget is protected.
- **No extra spend into generic Shopping or Search.** Both are past their efficient spend: Shopping got 157 new customers at £21.4k a week but only 141 at £28.3k.
- **Huel's recent tightening stays:** Shopping core at 85%, Search Generic at 110%, Meal Replacement at 80%, and the budget cuts. The budget cuts don't limit spend anyway (0% budget-lost).
- **No new-customer bidding on Shopping core yet.** Test it later, paired with a higher tROAS so spend stays flat.
- **No action on 16–18 Nov.** UK saw only a mild dip (conversion rate 2.35% → 2.04%), not the collapse seen in DE and PL.
- **Brand-demand drop (−28% since 5 Oct):** flag it as unexplained, not as something Google can't fix.

---

## Search & Shopping, revised (19 Nov)

**Rule (from the user):** pause something only when Smart Bidding will move that spend to more efficient parts of the account. In practice that means the campaign is budget-capped, or the item takes spend away from another campaign. In uncapped tROAS campaigns, leave weak items to Smart Bidding.

**Budget status, 5–18 Nov:**
- Capped: WEIGHT_LOSS (£1,343/day vs £1,300 budget) and GENERIC (£436 vs £400).
- Uncapped: COMPETITORS (£98 vs £200) and SHOPPING_GENERIC_CORE (£3,171 vs £4,700).

New-customer CAC below = spend ÷ "New Customer Purchase", 20 Sep–18 Nov.

**Actions**
1. **WEIGHT_LOSS (capped): pause "Medical/trending".**
   - £3.06k for 10.95 new customers, about £280 each. The rest of the campaign runs at £106–152 (Shakes & MR £106, Diet Plans £123, Fasting £141, Core £152).
   - Because the campaign is capped, the freed spend moves to those ad groups.
   - Keep Fasting: it has the highest new-customer share in the campaign.
2. **WEIGHT_LOSS: raise tROAS from 75% to 82%,** after action 1. Since the 22 Oct loosening, the extra conversions have cost about £135 each on the platform.
3. **GENERIC (capped): pause "Stockpiling".**
   - £3.71k for 24.3 new customers, about £153 each. The freed spend goes to Convenient Meals (£130) and Weight Gain (£50).
4. **SHOPPING_STANDARD_BRAND: add non-brand terms as negatives** ("freeze dried meals", "foods to stockpile", "morrisons", and similar). Then run a +20% max CPC test on brand terms only.
   - This counts as a valid exclusion: the campaign is on Manual CPC, so Smart Bidding doesn't price these terms. It also wins generic queries that Shopping core should serve on tROAS.

**Withdrawn, because Smart Bidding prices these in uncapped campaigns**
- Pausing Competitors ad groups (Greens & Wellness, Meal Replacement, Sports Nutrition).
- Shopping core product exclusions.
- Informational and GLP-1 negatives.
