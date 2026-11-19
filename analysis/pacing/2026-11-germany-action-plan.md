# Germany Google Ads action plan (19 Nov 2026)

Account: Huel EU (8046071519). Amounts are in EUR unless shown in £ (Fospha).

## 1. DE_SHOPPING_STANDARD_GENERIC: lower tROAS from 108% to 95%

**What's behind the drop**
- **It's product-level.** The search-term view gets *better* after 9 Nov (CPA on captured terms €89 → €69).
- **Scharfe Chick'n Nudeln (savs7-fcn-10-edp), the top product, collapsed.** Conversion rate fell from 2.9% to 1.2%, CPA doubled from €53 to €106, and ROAS fell from 1.45 to 0.63. It is a quarter of the campaign's spend.
- **The 16-pack shake trial pack** (blks16-mx1-01-edp) was already weak (ROAS 0.67). Google halved its spend, from €238 to €108 a day.
- **Daily Greens** (gre-ori-20r-edp): €234 spent since 9 Nov, 0 conversions.

**What to expect from 95%**, based on Google's bid simulator for 10 to 16 Nov:

| tROAS | Spend per week | Conversions per week | Average CPA |
|---|---:|---:|---:|
| 108% (now) | €3,530 | 54 | €65 |
| 95% | ~€4,580 (+30%) | ~62 (+14%) | ~€74 |

- The extra spend buys conversions at a marginal CPA of about €140, which is roughly £190 in Fospha DDA+ terms.
- Average Shopping DDA+ CAC should move from about £85–90 to **about £100**, right at the guardrail.
- Expect about +5 DDA+ new customers a week.
- Results will be noisy for 5–7 days. Judge them on a full week, not day by day.

**How to defend the change**
- DE Shopping hasn't been touched in at least 30 days. 108% is its only target in the API's change history.
- The team already tunes targets by market: ROE Shopping went from 108% to 102% (30 Oct), and SE and PL were adjusted on 16 Nov.
- The change is 12%, inside the 15–20% step that avoids resetting Smart Bidding.
- CPA was stable. The order value mix is what moved.

**Actions**
- [ ] Today: set tROAS to 95%. Leave the budget (€1,225) alone; it isn't limiting spend.
- [ ] Today: in Merchant Center, check whether the price, stock or promotion on Scharfe Chick'n Nudeln changed around 8–10 Nov.
- [ ] Mon 23 Nov and Mon 30 Nov: read Shopping DDA+ CAC in Fospha. If it's above £100 for a full week, go back to 108%.

## 2. DE_SEARCH_GENERIC: hold bids, add negatives

Hold tROAS at 100% and the budget at €700.

Search terms from 26 Oct to 18 Nov cover €10.0k of spend and 91 conversions (CPA €110). Add these as campaign phrase negatives:

| Negative | Spend | Conversions | CPA | Why |
|---|---:|---:|---:|---|
| prepmymeal, prep my meal | €831 | 5.0 | €166 | Competitor; ROAS 0.37 |
| löwenanteil, loewenanteil | €478 | 3.0 | €159 | Competitor; ROAS 0.34 |
| weight gainer, gainer | €262 | 1.0 | €262 | Wrong product |
| esn | €203 | 1.3 | €159 | Competitor (protein brand) |
| trek n eat | €181 | 1.4 | €132 | Outdoor food |
| jimmy joy, plenny | €127 | 0.3 | €467 | Competitor |
| frosta, foodspring, saturo, more nutrition | €118 | 0 | – | Competitors |
| meal prep, lieferdienst | €111 | 0.3 | €401 | Delivery / cook-at-home intent |
| youcook, every foods, [every] | €130 | 0 | – | Competitors |
| notfall, notvorrat, survival, tactical | €74 | 0 | – | Emergency food |

- Total: about €2.5k (25% of spend) for 12 conversions (13%). Removing them takes captured CPA from about €110 to about €95.
- **Keep:** ag1 (CPA €72), yfood (€72) and protein powder terms (€66). They convert at or below the campaign average.
- **Don't negate:** trinkmahlzeit. It's a core category term, even though its CPA is €200+. Review its match type and landing page instead.
- **Caveat:** competitor searchers are likely new customers. If Huel wants to conquest competitors, run a separate campaign with its own target (2025 had DE_SEARCH_COMPETITORS_ACQ) rather than leaving it in generic.

**Actions**
- [ ] Today: add the negatives above at campaign level. Check them against the shared negative lists first.
- [ ] Separately: review trinkmahlzeit.

## 3. DE_SEARCH_BRAND: bidding strategy

**Current setup**
- Bidding is Maximise Conversions with no target CPA, on a €140 daily budget.
- It has been budget-limited every week since at least September, losing 9–14% of impression share to budget.
- Absolute-top impression share is 56–66%.
- CPC rose from €0.24 in September to €0.32 in November.
- The search terms are clean: everything is a "huel" variant.

**The problem**
- Maximise Conversions on a capped budget spends the whole budget chasing conversions, most of which would come through organic anyway. It isn't built for the brand objective, which is coverage at the lowest CPC.
- Other markets already do this differently: PL brand uses Target Impression Share and ROE brand uses Manual CPC.

**Actions**
- [ ] Today: check auction insights for the campaign in the UI (the API can't pull them). Are competitors or resellers appearing on brand terms?
- [ ] Today, so it settles before Black Friday: switch to **Target Impression Share, absolute top of page, 90%, max CPC cap €0.45**, keeping the €140 budget.
- [ ] Mon 23 Nov: check absolute-top impression share and CPC. If budget-lost impression share is still above 5%, raise the budget to cover 26 Nov–1 Dec only.
