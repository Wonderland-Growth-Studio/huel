# Germany Google Ads: diagnosis and Black Friday plan (19 Nov 2026)

Sources:
- Fospha dashboard screenshots (spend and DDA+ new customers, in GBP).
- Google Ads account "Huel EU" (8046071519, in EUR), read through the API. Platform conversions count all purchases, not only new customers.
- Fospha GBP spend ≈ Google EUR spend × 0.87.

## 1. Why German non-brand spend halved from 9 Nov

Neither budgets nor manual changes caused it. Target ROAS bidding pulled back after the average order value (AOV) fell.

| DE Shopping generic (tROAS 108%) | Wk 26 Oct | Wk 2 Nov | Wk 9 Nov | 16 to 18 Nov |
|---|---:|---:|---:|---:|
| Spend per day | €834 | €922 | €542 | €411 |
| Platform CPA | €77.9 | €68.6 | €69.7 | lagging |
| Platform ROAS | 0.94 | 1.07 | 0.89 | 0.53 (lagging) |
| AOV (value ÷ conversions) | €73 | €73 | €62 | – |
| Average CPC | €1.4 to €1.5 | €1.6 | €1.1 to €1.3 | €1.0 to €1.1 |
| Impression share | 38% | 39% | 35% | ~33% |
| Impression share lost to budget | 0% | 0% | 0% | 0% |

- **Shopping cost per conversion stayed flat** (€69 to €70), but AOV fell about 15%. ROAS therefore dropped below the 108% target, and Smart Bidding cut bids: CPC went from €1.60 to €1.10 and impression share fell from 39% to 33%. Meanwhile Fospha DDA+ CAC on Shopping *improved* that week (£102 to £82). **The tROAS target is penalising lower basket values, not a worse cost per new customer.** Huel is judged on new customers and CAC, so the bidding target and the business KPI are pulling in different directions.
- **DE Search generic** (maximise conversion value, tROAS 100%):
  - Its impression share is under 10%. All of the lost share is from ad rank, none from budget.
  - Its budget was cut from €1,000 to €700 on 5 Nov by a Huel team member. It has spent €220 to €620 a day since, so the cut isn't what's limiting it.
- **1 to 4 Nov was a spike:** non-brand spent €2,200 to €2,800 a day at ROAS 0.35 to 0.87. That poor-ROAS stretch is probably what started the pullback.
- **No German campaign bid targets changed in the 30 days to 19 Nov.** There are also no Black Friday seasonality adjustments in the account, although the team used them in 2025.

## 2. A DDA+ CAC guardrail for Germany prospecting: £37 to ~£100 (not yet a measured number)

How the "£100" figure was calculated:
1. Blended PM CPA from 1 to 17 Nov: £72,739 ÷ 1,830 = £39.75. The target is £37.
2. DDA+ CAC from 19 Oct to 17 Nov: £125,568 ÷ 1,947 = £64.48. Split into brand (£6,959 ÷ 862) and prospecting, meaning non-brand plus Meta (£118,608 ÷ 1,086 = £109).
3. The ratio is 64.48 ÷ 39.75 = 1.62. In other words, each DDA+ new customer currently comes with about 0.62 unattributed new customers.
4. Assume that ratio stays fixed. The £37 target then becomes 37 × 1.62 ≈ £60 total DDA+ CAC.
5. Hold brand fixed and solve (6,959 + c × 1,086) ÷ 1,948 = 60. That gives c ≈ **£101**.

Weaknesses:
- **It's circular.** The result is just current prospecting CAC scaled by target ÷ actual (109 × 37 ÷ 39.75 ≈ £101). The earlier "cross-check" against the 7% overage wasn't independent, so it's withdrawn.
- **The two periods don't match.** Step 1 covers 1 to 17 Nov and step 2 covers four weeks. The spend totals also come from different tables.
- **It rests on one assumption: that unattributed new customers scale 1:1 with paid.** If they are instead a fixed organic baseline, a marginal paid new customer has to cost about £37 or less to avoid raising blended CPA. The truth sits between £37 and about £100, so **£100 is the generous end**.
- **It's an average, not a marginal threshold.** Budget decisions are made at the margin.

What still holds whatever the threshold turns out to be:
- The ranking: Shopping (£97) is cheaper than Meta (£109), which is cheaper than Search (£127).

How to replace this with a measured number:
- The Fospha **Halo** tab, if it measures how much paid media lifts organic and brand. That is the missing ratio.
- Alternatively, regress weekly total German new customers on weekly prospecting spend over 6 to 12 months.

How Germany's channels compare with that par:

| Channel | 4-week DDA+ CAC | Last 7 days | Against the ~£100 par |
|---|---:|---:|---|
| Google Shopping generic | £97 | £90 to £96 | At or under par |
| Google Search generic | £127 | £115 | Over par |
| Meta (75% of spend) | £109 | £119 | Over par, and getting worse |

- **Google Shopping is the most efficient prospecting channel in Germany** and has headroom to scale.
- Weekly spend against CAC (£10.7k at £117, £5.6k at £91) puts the par point at about **£7.4k a week of non-brand spend, roughly €1,200 a day**. The current run rate is about €850 a day.

This is a working number: the assumption that organic customers scale with paid is the weak link. Use it as a guardrail and replace it once Fospha or an incrementality test gives a measured halo.

## 3. Brand: judge on coverage, not DDA+ CAC

`DE_SEARCH_BRAND` (€140 a day, maximise conversions):
- It loses 4 to 18% impression share to budget and about 10% to rank.
- Last year in Germany, brand conversions rose from about 30 to 60 a day to 70 to 94 a day on 26 to 30 Nov.
- **The monthly cap effect is small.** Spend is projected to overshoot the €4,256 limit by about €160, which means a throttle of roughly €13 a day on the last two days. A rise in Black Friday searches would matter more than the cap.
- **Its £8 DDA+ CAC is the wrong lens.** Most people searching "Huel" would convert through the organic listing anyway.
- **What brand should be optimised for:** keeping competitors and resellers from capturing brand searchers, at the lowest CPC, and showing the Black Friday offer in the ad.
- **Lost impression share only costs anything if someone else shows when our ad doesn't.** Auction insights aren't available through this API connection, so check them in the Google Ads interface.

## 4. Recommended Google changes for Germany (19 Nov to 1 Dec)

| # | Campaign | Change | Why |
|---|---|---|---|
| 1 | DE_SEARCH_BRAND | **Conditional.** Raise the budget for 26 Nov to 1 Dec only if auction insights show competitors on brand terms, or if Germany has a Black Friday offer to show | Brand isn't a lever for new customers. The extra spend only pays off if someone else would otherwise take the click |
| 2 | DE_SHOPPING_STANDARD_GENERIC | tROAS 108% to **95%** | Its cost per conversion is at par, so this undoes the pullback the AOV dip caused. Aim for €650 to €750 a day |
| 3 | DE_SEARCH_GENERIC | **Hold** at tROAS 100% and leave the budget at €700 | DDA+ CAC is £127 over 4 weeks. It was worst (£141 to £156) when spend was higher. The budget isn't limiting spend, and in 2025 its conversion rate didn't rise on Black Friday. Put any extra money into Shopping, and work on search-term efficiency |
| 4 | Guardrail | Weekly German Shopping DDA+ CAC ≤ **£100** in Fospha | If it goes above that for a full week, roll back step 2 |
| 5 | Black Friday seasonality adjustment | Only if Germany runs a Black Friday offer | In 2025, German non-brand conversion rate barely rose on Black Friday; brand did. Don't add an adjustment to generic campaigns without an offer |

**Expected effect:**
- Shopping goes from about €430 to about €700 a day: roughly +£2.8k over the 12 days left.
- At a marginal DDA+ CAC of £110 to £150, that's about **+20 to 25 DDA+ new customers**.
- Germany is about 252 new customers behind target, so **Google is a small part of the answer. The gap is a Meta question.**

## 5. Other European markets: what the platform shows (needs Fospha channel views to confirm)

| Market | What the platform shows (12 to 18 Nov) |
|---|---|
| Sweden | **SE Shopping loses 23% impression share to budget** (€300 a day), and its tROAS was *raised* from 80% to 90% on 16 Nov. SE brand loses 14% to budget. Non-brand CPA is rising every week (€70 to €116). Fits Sweden's 131% CPA |
| Poland | PL Search tROAS raised from 60% to 70% on 16 Nov. Non-brand CPA jumped in the week of 16 Nov (€215, ROAS 0.24), probably partly conversion lag. PL brand is at its budget |
| Rest of Europe | ROE Search generic spends above its budget (€1,063 a day against €920, cut on 16 Nov) and loses 9% to budget. Its tCPA was cut from €120 to €100 on 30 Oct. ROE brand loses 6% to budget. Non-brand CPA rose to €130 to €150 in November |
| Italy | IT Search generic was paused on 3 Nov |
