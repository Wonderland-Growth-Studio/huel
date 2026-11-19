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

## 2. The right DDA+ CAC for Germany: about £100 for prospecting

- **The data:** Germany's blended PM CPA target is £37 and current blended CPA is £39.75 (107% of target). Over the last 4 weeks, total DDA+ CAC was £64.5, with brand at £8 and prospecting (non-brand plus Meta) at £109.
- **The assumption:** organic and unattributed new customers move in proportion to paid DDA+ new customers. At present Fospha counts about 1.9 total new customers for every DDA+ new customer.
- **The result:** the £37 blended target is equivalent to roughly **£60 total DDA+ CAC**. With brand held where it is, that means **about £100 average DDA+ CAC for prospecting**.
- **Cross-check:** current prospecting is £109 against a par of £101, so 8% over. That matches the 7% blended overage, so the par holds together.

How Germany's channels compare with that par:

| Channel | 4-week DDA+ CAC | Last 7 days | Against the ~£100 par |
|---|---:|---:|---|
| Google Shopping generic | £97 | £90 to £96 | At or under par |
| Google Search generic | £127 | £115 | Over par |
| Meta (75% of spend) | £109 | £119 | Over par, and getting worse |

- **Google Shopping is the most efficient prospecting channel in Germany** and has headroom to scale.
- Weekly spend against CAC (£10.7k at £117, £5.6k at £91) puts the par point at about **£7.4k a week of non-brand spend, roughly €1,200 a day**. The current run rate is about €850 a day.

This is a working number: the assumption that organic customers scale with paid is the weak link. Use it as a guardrail and replace it once Fospha or an incrementality test gives a measured halo.

## 3. Brand: budget-limited, and will hit its monthly cap over Black Friday weekend

`DE_SEARCH_BRAND` (€140 a day, maximise conversions):
- It loses 4 to 18% impression share to budget most days.
- Its monthly limit (€4,256) will be reached around **29 Nov**, the Saturday after Black Friday. From then Google throttles it.
- Last year in Germany, brand conversions rose from about 30 to 60 a day to **70 to 94 a day on 26 to 30 Nov**, while spend stayed flat.
- Brand is the cheapest source of new customers (DDA+ £8 to £10). However, a lot of brand demand would convert organically anyway, so treat this as protecting Black Friday demand rather than finding new customers.

## 4. Recommended Google changes for Germany (19 Nov to 1 Dec)

| # | Campaign | Change | Why |
|---|---|---|---|
| 1 | DE_SEARCH_BRAND | Budget €140 to **€250** until 2 Dec | Removes the budget limit and the monthly cap over Black Friday weekend. Costs about +€1k to €1.3k |
| 2 | DE_SHOPPING_STANDARD_GENERIC | tROAS 108% to **95%** | Its cost per conversion is at par, so this undoes the pullback the AOV dip caused. Aim for €650 to €750 a day |
| 3 | DE_SEARCH_GENERIC | tROAS 100% to **90%**, budget back to **€1,000** | A smaller loosening, because Search is over par. The budget won't limit spend, but restoring it keeps room for Black Friday (new limit ≈ €23k, about €1,000 a day of headroom) |
| 4 | Guardrail | Weekly German non-brand DDA+ CAC ≤ **£105** in Fospha | If it goes above that for a full week, roll back steps 2 and 3 |
| 5 | Black Friday seasonality adjustment | Only if Germany runs a Black Friday offer | In 2025, German non-brand conversion rate barely rose on Black Friday; brand did. Don't add an adjustment to generic campaigns without an offer |

**Expected effect:**
- Non-brand goes from about €850 to about €1,200 a day: roughly +£3.6k over the 12 days left.
- At a marginal DDA+ CAC of £130 to £170, that's about **+20 to 30 DDA+ new customers, or about +40 to 55 blended**.
- Germany is about 252 new customers behind target, so **Google can close roughly a fifth of the gap. The rest depends on Meta**, which is the bigger and less efficient channel.

## 5. Other European markets: what the platform shows (needs Fospha channel views to confirm)

| Market | What the platform shows (12 to 18 Nov) |
|---|---|
| Sweden | **SE Shopping loses 23% impression share to budget** (€300 a day), and its tROAS was *raised* from 80% to 90% on 16 Nov. SE brand loses 14% to budget. Non-brand CPA is rising every week (€70 to €116). Fits Sweden's 131% CPA |
| Poland | PL Search tROAS raised from 60% to 70% on 16 Nov. Non-brand CPA jumped in the week of 16 Nov (€215, ROAS 0.24), probably partly conversion lag. PL brand is at its budget |
| Rest of Europe | ROE Search generic spends above its budget (€1,063 a day against €920, cut on 16 Nov) and loses 9% to budget. Its tCPA was cut from €120 to €100 on 30 Oct. ROE brand loses 6% to budget. Non-brand CPA rose to €130 to €150 in November |
| Italy | IT Search generic was paused on 3 Nov |
