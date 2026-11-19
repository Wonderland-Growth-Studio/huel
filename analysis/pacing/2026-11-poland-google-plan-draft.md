# Poland Google Ads: DRAFT for review (19 Nov 2026)

## Inputs

**Fospha (from the dashboard screenshots)**
- **Poland Nov MTD:** PM spend £31,595, 1,284 new customers. That's 89.8% of the new-customer target to date. Blended CPA is £24.61 against a £21.50 target (114.5%).

Fospha DDA+ by week (spend / new customers / CAC):

| Week | Google Shopping | Google Search generic | Meta |
|---|---|---|---|
| 19 Oct | £2,980 / 24 / £123 | £2,046 / 13 / £159 | £8,655 / 62 / £140 |
| 26 Oct | £2,747 / 24 / £113 | £2,442 / 13 / £191 | £7,780 / 48 / £162 |
| 2 Nov | £4,254 / 36 / £117 | £2,918 / 19 / £150 | £6,398 / 68 / £94 |
| 9 Nov | £3,630 / 32 / £113 | £1,904 / 14 / £139 | £5,883 / 65 / £91 |
| 16 Nov (2 days) | £994 / 6 / £181 | £608 / 4 / £160 | £1,756 / 17 / £104 |
| **4-week total** | **£14,605 / 123 / £119** | **£9,918 / 63 / £158** | **£30,471 / 260 / £117** |

- **Google Brand, 4 weeks:** £1,448 / 540 / £2.68.
- **Last 7 days:**
  - Brand: £308 / 101 / £3.04.
  - Non-brand: £4,921 / 31 / £157.
    - PL_SHOPPING_STN_GENERIC £3.19k / 19 / £171.
    - PL_SEARCH_GENERIC £1.73k / 13 / £136.
  - Meta: £4,888 / 50 / £98.

**Google Ads** (EUR; scratchpad `gads/pl/`, `gads/eu_daily.json`, `gads/brand_daily.json`)

**PL_SHOPPING_STN_GENERIC**
- Setup: tROAS 70%, budget €850, no target changes in the last 30 days.
- Budget-lost IS is 0% since September. Rank-lost IS is about 58–62%.
- Weekly platform CPA: €65, €80, €82, €85, €101, €86 (5 Oct–9 Nov). Realised ROAS 0.60–0.83, below the 70% target.
- 16–18 Nov: 2–2.6 conversions a day on €480–660 of spend, which looks like conversion lag. 5–6 Nov had a similar dip and recovered.
- Product level: no single SKU collapsed. The strawberry shake has 0 conversions in 3 weeks (€227), and Google is already cutting its spend.

**PL_SEARCH_GENERIC**
- Setup: Max Conversion Value. A Huel team member raised tROAS from 60% to 70% on 16 Nov. Budget €440, not binding. IS 17–20%, about 80% lost to rank.
- Keyword level, 19 Oct–18 Nov (complete data): about €11.8k spend, 104 conversions, CPA about €114.

| Ad group | Spend | Conversions | CPA | Notes |
|---|---:|---:|---:|---|
| Meal Replacements | ~€3.56k | 36.6 | €97 | |
| Outdoor | ~€2.03k | 22.1 | €92 | |
| Protein | ~€2.11k | 17.9 | €118 | |
| Vegan & Plant-Based | ~€3.43k | 24 | €143 | Biggest keyword "białko roślinne" BROAD, QS 1: €2,675 / 19 conversions (€141), 25% IS |
| Competitors | ~€684 | 3 | €228 | All QS 1. KFD alone €384 / 2 |

- "posiłek w proszku" BROAD: €348, 0 conversions.
- Search terms in Vegan & Plant-Based include generic protein queries ("bialko", "odżywki białkowe", "protein powder", "bez cukru"). Note: the search-term pull was capped at 5,000 rows.

**PL_SEARCH_BRAND**
- Setup: Target Impression Share, 75% anywhere on page, CPC cap €0.50, budget €46.
- Average CPC €0.10–0.12, CPA €1.1–1.8. Budget-lost IS is 0% since October. Rank-lost IS rose from 13–15% to 20–29% in November.
- "huel" exact: €188, 9,192 clicks, €0.02 CPC, 96% IS, 85% absolute-top.
- The rest of the spend goes on "huel" + modifier terms through broad, at €0.24–0.41 CPC. "huel opinie" alone was €150 for 20.8 conversions.

**Black Friday 2025:** neither PL brand nor PL Shopping showed a lift (brand conversions were flat at about 160–235 a week, with no budget loss).

## Draft recommendations

1. **Do now: pause the PL_SEARCH_GENERIC "Competitors" ad group.**
   - **Why:** CPA €228, 2× the campaign average, on about 6 CPAs of spend. Every keyword has QS 1.
2. **Do now: change "białko roślinne" from BROAD to PHRASE in Vegan & Plant-Based.**
   - **Why:** it's the biggest keyword, with QS 1 and CPA €141 (1.24× average) over about 23 CPAs of spend. Broad match pulls in generic protein queries that don't fit the ad group.
3. **Do now: pause "posiłek w proszku" BROAD.**
   - **Why:** €348 and 0 conversions. That's about 3 CPAs of spend; at the campaign conversion rate, zero conversions has about a 3–5% chance.
4. **Keep: PL Search generic tROAS at 70%** (Huel's change on 16 Nov).
   - **Why:** Search is Poland's worst Fospha line (£158 over 4 weeks), while Meta is now £91–98.
5. **No change: PL Shopping tROAS 70% and budget.**
   - **Why:** Fospha CAC has been steady at £113–123 for 4 weeks. The last-7-days £171 lines up with conversion lag (16–18 Nov, same pattern as 5–6 Nov). Shopping isn't the cheapest line in Poland (Meta is), so it shouldn't get more money either. Re-read on 23 Nov.
6. **No change: PL brand stays on Target Impression Share with the €0.50 cap.**
   - **Why:** it isn't conversion-based bidding, it's already cheap (€0.10 CPC, "huel" at €0.02), and nothing is lost to budget. There was no Black Friday lift in 2025.
7. **No Black Friday changes in Poland.**
   - **Why:** 2025 showed no Black Friday lift in brand or Shopping.
8. **For the Huel update:** Poland's best prospecting line right now is Meta (£91–98), not Google. If Poland wants volume, the money should go to Meta.
