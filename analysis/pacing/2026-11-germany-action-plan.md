# Germany Google Ads action plan, v3 FINAL (19 Nov 2026)

How this was made:
- I pulled the data and drafted each recommendation. An Opus reviewer worked independently from the same data, then challenged each step.
- Everything below rests on actual account history: 58 weeks of campaign data, product weeks, change history and the Fospha dashboard. No Google simulator figures.
- Account: Huel EU (8046071519), EUR. Fospha figures are in GBP.

---

## 1. DE_SHOPPING_STANDARD_GENERIC: lower tROAS from 108% to 95% today

**Why**
- **What happened, week of 2 Nov → week of 9 Nov:**
  - Conversion value per click fell 35%. Conversion rate went from 2.25% to 1.71%, and AOV from €73 to €62.
  - So ROAS fell from 1.07 to 0.89, under the 108% target.
  - Google cut CPC 23%. Spend fell 41% and conversions fell 42%.
- **The customers didn't get worse.** CPA held at €69–70, below the 58-week median of €72.5.
- **AOV is at a 13-month low:** €62 against a median of €71. Fospha confirms the volume loss: Shopping new customers fell from 55 to 40 a week while CAC improved from £102 to £82.
- **A 12% target cut offsets most of the AOV fall.** That loosens the bid limit Google has been running into.

**What to expect**
- **A modest lift, not a return to €900 a day.** The account's only real tROAS test was ROE Shopping, 108% → 102% on 30 Oct. Measured against DE as a control, it produced no measurable increase in relative spend.
- **The conversion-rate drop won't be fixed by this.** It needs separate investigation (see actions).

**Keep all products**
- Spicy Chick'n noodles' week of 9 Nov (€89 CPA) sits within its 10-week range of €40–89. It hasn't collapsed.

**Actions**
- [ ] tROAS 108% → 95%. Leave the budget (€1,225) as it is; it isn't limiting spend.
- [ ] Merchant Center: check stock, price and disapprovals on Daily Greens (`gre-ori-20r-edp`). It got 0 conversions on 89 clicks; at its usual 5.3% conversion rate, that has about a 1% chance.
- [ ] Look into the conversion-rate drop: landing pages, prices and stock for the top 4 SKUs around 8–10 Nov.

**Guardrail.** Read only data at least 3 days old, starting with the week of 23 Nov. Revert to 108% if any of these happens:
- 2 consecutive weeks with CPA above €80.
- 1 week with CPA above €90. That happened in only 3 of 58 weeks.
- Fospha Shopping CAC above £105. At about £5k a week of spend, that caps the marginal cost at about £210.

**No Black Friday tROAS cut.** DE Shopping AOV in Black Friday week 2025 was €69.5, the same as the weeks around it. Revisit only if Huel runs a deeper discount this year.

---

## 2. DE_SEARCH_GENERIC: hold (tROAS 100%, €700). No negatives.

**Why**
- **Shopping is the better home for any extra money.** Search costs £128 per Fospha new customer against £97 for Shopping (4-week averages). If Huel wants the Shopping increase to be CAC-neutral, trim Search first.
- **The competitor structure works.** The prepmymeal leak into Ready Meals cost €668 for 1.3 conversions. It stopped on 11 Nov, when 19 exact-match ad-group negatives went in. A phrase-match "prepmymeal" negative is now also present.
- **Every remaining stray term has spent under 1.5 CPAs.** That's not enough data to act on.

**Actions**
- [ ] None now.
- [ ] Monthly: scan the non-competitor ad groups for competitor names and add phrase-match negatives.

---

## 3. DE_SEARCH_BRAND: keep Maximise Conversions

Budget: **€175 now, €200 for 24 Nov–1 Dec, back to €140 on 2 Dec.**

**Why**
- **Budget has been the limit for 13 months.** Lost impression share from budget has been 5–17% every week.
- **Extra brand budget buys the cheapest conversions in the account.**
  - 13–14 Nov (€99 a day) against 6–7 Nov (€146): spend −32%, clicks −2%, conversions −18%.
  - That puts the marginal CPA at about €6, against about €70 for Shopping.
  - Even if most brand conversions would happen organically anyway, that's still the cheapest line.
- **Black Friday 2025:** conversions were +55% at €131 a day, and lost impression share from budget hit 17%. Covering that needs +25–40% budget, which is €175–200.
- **Why not more than €200:** extra brand spend mostly buys pricier clicks. 15 Nov: €188 bought 53 conversions at €0.43 CPC. 16 Nov: €145 bought 61.
- **Why not Target Impression Share:** the budget is what limits the campaign, not the bid strategy.

**Actions**
- [ ] Today: budget €175.
- [ ] Schedule €200 for 24 Nov–1 Dec, then €140 from 2 Dec. Total extra cost is about €650.
- [ ] Find out what capped spend at exactly €99 on 13–14 Nov. Change history shows no budget change.

---

## Changed after the debate

| Topic | Before | After | What decided it |
|---|---|---|---|
| Shopping target | 95% → 100% (v2) | **95%** | 100% doesn't offset the 15% AOV fall. The reviewer agreed |
| Shopping expected outcome | Back to €670–920 a day | **Modest lift** | The ROE 108→102 test showed no measurable spend lift |
| Shopping guardrails | €80 CPA / £115 Fospha | **2 weeks > €80 or 1 week > €90; Fospha ≤ £105** | €80 is breached in 11 of 58 normal weeks. £115 allowed about £445 at the margin |
| Product exclusions | Exclude 2 SKUs (v2) | **None** | Spicy Chick'n noodles is within its 10-week range |
| Black Friday tROAS cut | Planned (v2) | **None** | 2025 Black Friday AOV was normal |
| Search justification | £231 marginal | **£128 vs £97 averages** | The marginal fit has R² 0.55; the averages are solid |
| Brand Black Friday budget | €250–280 | **€200** | The real marginal CPA is €6.2, not €2.6. Extra budget buys pricier clicks |

## Open decision for Huel
Volume or CAC for the rest of November? Germany is 252 new customers behind target, and CPA is 107% of target. Each recommendation above improves one and costs some of the other. The brand change is the exception: it's cheap enough to improve both.
