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

## 3. DE_SEARCH_BRAND: switch to Manual CPC today (enhanced CPC off)

Budget becomes a ceiling: **€180 now, €250 for 24 Nov–1 Dec, €180 from 2 Dec.**

**Why**
- **Under Max Conversions, extra brand spend buys nothing.**
  - Daily regression (n=110), controlling for weekday: each extra €1 a day buys +4.6 impressions, about 0 clicks (+0.02) and about 0 conversions.
  - The reviewer re-ran it with trend and demand controls and got the same result: 0.14–0.18 extra clicks per € in each period, against 3.7 at the average CPC.
  - Spend and CPC move together (correlation 0.46): CPC is €0.31 on days above €155, against €0.26 on other days.
- **"huel" exact is already almost fully covered.** It takes about 73% of spend and has 93% IS and 84% absolute-top IS at €0.29 (QS 10). The campaign-level "11% lost to budget" sits mainly in Huel (Broad), which has 52% IS, 26% absolute-top, a €0.33 CPC and an 8% conversion rate (12% on exact).
- **The real gain is control, not a big CPC saving.** A manual cap stops Google inflating CPCs, and the budget can rise as a ceiling for Black Friday demand without paying more per click. Expect CPC to stay about flat. No account data supports a 10–20% saving.
- **No ad-schedule adjustment.** Absolute-top IS is flat across the day (0.57–0.62 from 6h to 23h). The evening conversion rate is higher (15.8% at 19h against 10.0% at 9h), but that reflects who is searching then, not ad position.
- **Why switch now:** Manual CPC has no learning period, and switching today gives a 7-day baseline before Black Friday.
- **Retracted:** the v3 budget raise under Max Conversions (€175/€200) would mostly have inflated CPC. The "€6 marginal CPA" from 13–14 Nov was confounded by 24% lower demand on those days.

**Actions**
- [ ] Before switching, add exact-match keywords at €0.35 for "huel black friday", "huel de" and "huel rabattcode". They currently run through broad (74 clicks / 8 conversions on "huel de").
- [ ] Switch the bidding to Manual CPC. Max CPC: "huel" exact **€0.35** (only 8 of 110 days averaged above it); product exacts **€0.50** (black edition already averages €0.38; daily greens has only 20% absolute-top at €0.35); Huel (Broad) **€0.30**.
- [ ] Budget ceiling: €180, then €250 for 24 Nov–1 Dec.
- [ ] Check daily (twice a day 26 Nov–1 Dec): absolute-top IS on "huel" exact ≥ 80%, and on "huel black friday". If it falls, raise bids by €0.03. Check auction insights in the UI for competitor conquesting. IS data arrives about a day late.

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
| Brand bidding | Max Conversions + budget €175/€200 | **Manual CPC (€0.35 / €0.50 / €0.30) + budget ceiling €180/€250** | The user's view, tested. With weekday controls, extra spend buys 0 clicks and 0 conversions |

## Open decision for Huel
Volume or CAC for the rest of November? Germany is 252 new customers behind target, and CPA is 107% of target. Each recommendation above improves one and costs some of the other. The brand switch is the exception: it costs about nothing either way.
