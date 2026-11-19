# Germany Google Ads action plan, v2 (19 Nov 2026), stress-tested

Account: Huel EU (8046071519), EUR. A second reviewer (Opus) challenged v1; the changes from v1 are marked.

## 1. DE_SHOPPING_STANDARD_GENERIC: fix the product mix first, then a small tROAS step

**What's behind the drop**
- **Two products collapsed:**
  - Scharfe Chick'n Nudeln (savs7-fcn-10-edp): CVR 2.9% → 1.2%, CPA €53 → €106, 28% of spend.
  - Daily Greens (gre-ori-20r-edp): €234 spent and 0 conversions in 10 days, after 9.7 conversions in the 14 days before.
- **The 16-pack trial pack is fine.** Its CPA *improved* from €102 to €80. It is probably a strong source of new customers. Keep it. *(v1 called it weak; that was wrong.)*
- **CPA is not flat.** It was €70 for 9–15 Nov but €81 for 12–16 Nov, and €95 if you include the lagging 17–18 Nov. *(v1 said flat.)*

**Actions**
- [ ] Today: check Merchant Center for price, stock, promotion or disapproval changes on both products around 8–10 Nov.
- [ ] Today: exclude Daily Greens from this campaign.
- [ ] Today: exclude Scharfe Chick'n Nudeln, unless Merchant Center shows a fixable cause. In that case fix it and keep the product.
- [ ] Today: lower tROAS from 108% to **100%**. *(v1 said 95%.)*
  - The simulator puts the marginal new customer at about £170–215, roughly 5× the £37 target. With the exclusions in place, a smaller step holds spend roughly flat and improves the mix.
  - Go to 95% only if Huel explicitly prefers volume over CAC for the rest of November.
- [ ] Before 26 Nov: if Germany has a Black Friday discount, apply tROAS × (BF AOV ÷ normal AOV) for 27 Nov–1 Dec. A lower AOV will otherwise throttle the campaign automatically.

**Guardrail** *(v1 used a £100 Fospha trigger, but that was the same as the expected result)*
- Daily: Google CPA over 7 days, read only on data at least 3 days old, ≤ **€80**.
- Weekly (Mon 23 Nov and 30 Nov): extra Fospha new customers compared with extra spend.

## 2. DE_SEARCH_GENERIC: hold tROAS at 100% and the budget at €700

- **The competitor structure works. v1's campaign-level negatives are withdrawn.**
  - There are three competitor ad groups. Each non-competitor ad group carries about 325 negatives.
  - The prepmymeal leak into Ready Meals (€668, 1.3 conversions) stopped after the negatives added on 11 Nov.
- **Most of those negatives are exact match** (about 242 exact, 35 phrase, 48 broad per ad group), while the keywords are broad. New competitor variants will keep leaking.

**Actions**
- [ ] Add "frosta" as a **phrase** negative to the non-competitor ad groups (€57 spent, 0 conversions, not negated anywhere).
- [ ] Ready Meals: add [every] exact. Review "meal prep" (€107, 0.3 conversions).
- [ ] Monthly: scan non-competitor ad groups for competitor names and add phrase negatives.
- [ ] Competitor ad groups: no pausing yet (youcook €77, jimmy joy €102: under 1–2 CPAs of spend).
- [ ] Watch "Competitors – Meal Replacement & Delivery" (CPA €114, the weakest group). If anything gets trimmed, trim here first.

## 3. DE_SEARCH_BRAND: keep Maximise Conversions and raise the budget

*v1's switch to Target Impression Share is withdrawn.*

**Why v1 was wrong**
- Budget is what limits the campaign, not the bidding strategy. Target Impression Share raises CPCs, which loses more impressions to budget.
- Max Conversions also already shifts spend to the evening hours, which convert about twice as well.
- The proposed €0.45 cap would bind. Daily CPC already reached €0.43 on 7 and 15 Nov.

**Actions**
- [ ] Today: raise the budget from €140 to **€180**.
- [ ] Pre-schedule **€280** for 26 Nov–1 Dec. Go back to €140 on 2 Dec.
  - In 2025, brand conversions rose about 50% in Black Friday week. The total extra cost is about €1.2k.
- [ ] Check auction insights in the UI. If no competitors appear on brand terms, organic probably catches most of the lost clicks. Keep the budget lift small in that case.
- [ ] Check change history for 13–14 Nov: spend was €99 a day with 17–18% lost to budget. Something capped it.

## Open decisions for Huel
- **Volume or efficiency for the rest of November?** Closing the 252-customer gap and hitting £37 pull in opposite directions. Every extra Google new customer costs about 5× the target at the margin.
- **Is there a Black Friday discount in Germany?** It decides the tROAS adjustment for 27 Nov–1 Dec.
- **Not yet reviewed:** DE_SHOPPING_STANDARD_BRAND (manual CPC, €140).
