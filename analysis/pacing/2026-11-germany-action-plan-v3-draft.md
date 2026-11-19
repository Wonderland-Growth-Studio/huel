# Germany Google Ads, v3 DRAFT: each recommendation tied to real account data

Data used (no Google simulator):
- Weekly campaign history, 6 Oct 2025 to 18 Nov 2026: scratchpad `gads/weekly_long.json`.
- Daily data, Oct to Nov: `gads/eu_daily.json`.
- Product weekly history for 4 SKUs, Jul to Nov.
- Search terms by ad group: `gads/st_ag.json`.
- Change history.
- Fospha weekly Shopping and Search figures from the dashboard: Shopping (£4,099 spend, 41 new customers), (£5,077, 50), (£5,610, 55), (£3,298, 40). Search (£3,895, 37), (£4,593, 29), (£5,074, 36), (£2,335, 22).

## R1. Shopping generic: lower tROAS from 108% to 95%. Keep all products.

**Inputs**
- **AOV hit a 13-month low.** It was €62.1 in the week of 9 Nov. Across 58 weeks the minimum is €61.8 and the median €71.1.
- **CPA did not move.** It was €69.7 that week, below the 58-week median of €72.5.
- **tROAS turns AOV into a CPA ceiling.** The implied ceiling is AOV ÷ tROAS: €73/1.08 = €68 in October, €62/1.08 = €57 now. Google is willing to pay 16% less per conversion, though no target changed and nothing about the customers changed.
- **Spend tracked that ceiling.** €834–922 a day in the weeks of 26 Oct and 2 Nov, then €542.
- **95% restores the ceiling** to €62/0.95 ≈ €65. That's still below October's €68.
- **The product mix supports a lower target.** The 16-pack trial pack ramped from €38 to €254 a day (12 Oct to 2 Nov) with an AOV of €61–72. It is the acquisition product, and a high tROAS penalises it.

**Expected outcome**, read from real weeks at that operating point:
- Spend €670–920 a day, platform CPA €69–78.
- Fospha 50–55 Shopping new customers a week at £100–102 (weeks of 26 Oct and 2 Nov), against 40 at £82 now.
- That is about +10–15 Fospha new customers a week, at a marginal cost of about £148 (4-week fit).

**Why it's worth it**
- Shopping is the cheapest prospecting line in Germany at the margin. Fospha marginal cost is £148 for Shopping against £231 for Search. Platform elasticity is 0.97 for Shopping against 0.75 for Search.
- Germany is 6% under its planned spend, so the budget exists.

**Why not 100%** (stress-test v2): 100% only gets the ceiling to €62, still below the level that produced the October volume.

**Keep products**
- **Spicy Chick'n noodles:** weekly CPA €40–89 over the last 10 weeks, and the week of 9 Nov was €89, at the top of its range. v1 compared it against its best fortnight. It is not a collapse.
- **Daily Greens:** 0 conversions on €234 over 2 weeks, when it normally converts 3–7 a week. That is anomalous, but Google has already cut it to about €10 a day. Check Merchant Center only.

**Guardrail**
- Platform 7-day CPA, on data at least 3 days old, ≤ €80. That's the upper quartile of 58 weeks.
- Weekly Fospha Shopping CAC ≤ £115. The highest observed at full spend is £102.

**No Black Friday tROAS cut**, unless Huel confirms a deeper discount this year: DE Shopping AOV in Black Friday week 2025 was €69.5, the same as the weeks around it.

## R2. Search generic: hold, and add no negatives

**Inputs**
- Search is the worst marginal line in German Google. Fospha marginal cost is about £231 against an average of £128. Platform elasticity is 0.75 (marginal CPA €99 against an average of €74).
- **The competitor structure works.** The leak into Ready Meals was €668 for 1.3 conversions. It stopped on 11 Nov when 19 exact-match negatives went in. A phrase-match "prepmymeal" negative is also present now.
- Every remaining stray term has spent under 1.5 CPAs. That's too little evidence to act on.

**Action**
- No bid or budget change.
- Run a monthly scan of the non-competitor ad groups for competitor names.
- If Huel wants CAC-neutral volume, fund the Shopping increase by trimming Search first, since Search is the worst marginal line.

## R3. Brand search: keep Maximise Conversions. Budget €175 now, €250 for 24 Nov–1 Dec, back to €140 on 2 Dec

**Inputs**
- **The budget has been the limit for 13 months.** Budget-lost impression share was 5–17% every week.
- **Conversions follow spend.** Elasticity over 41 weeks is 0.79, so the marginal platform CPA is €2.6.
- **January 2026 tested it.** Spend went up to €224–307 a day and conversions scaled with it (to 812 a week at €2.6).
- **13–14 Nov tested it the other way.** Spend dropped to €99 (−33%) and conversions fell 38%.
- **Black Friday week 2025:** conversions were +55% (512 against about 330) and budget-lost impression share hit 17%. Demand outran the budget.

**Why it's worth it, even if brand is mostly not incremental**
- At €2.6 a conversion, even 10% incrementality means €26 per incremental conversion. That's cheaper than any other line.
- The total extra cost is about €0.9k.

**Why not Target Impression Share**
- The budget is what limits the campaign, not the bid strategy.
- Target Impression Share would raise CPCs.

**Check**
- What capped spend at exactly €99 on 13–14 Nov? It wasn't a budget change.
