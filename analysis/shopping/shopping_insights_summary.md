# Huel UK - Google Shopping: everything we found

Internal working summary, not client-facing. It collects every Shopping finding from the audit work (23 Sep – 7 Oct 2026), plus the 21 Sep and 19 Oct performance reviews, so nothing gets lost before the Shopping section is written.

Account: Huel UK (345-592-4316), GBP. Windows vary by finding and are stated each time. "CAC" from the Google Ads account means cost per conversion across all purchases, new and returning, unless it says Fospha.

**Already in the audit doc:** 1.3 (single target, LTV question), section 2 (Brand Shopping), the 4.1 negatives table (healf and elderly on Shopping; discount codes Search-only with a note to revisit Shopping), and the 4.5 line on Target ROAS allocating between products the way it does in Shopping.

**Not in the doc yet:** everything else below. The doc has no Shopping section.

---

## 1. Structure

- **Generic Shopping is one campaign with one ad group.** `UK_SHOPPING_GENERIC_CORE` (£447k over 90 days, Target ROAS 0.8) covers every product family.
- **A second campaign, `UK_SHOPPING_GENERIC_RESTRICT`** (£8.9k over 90 days, target 0.8), holds bars, Daily A-Z, Essential and Greens RTD.
- **Brand Shopping (`UK_SHOPPING_STANDARD_BRAND`) is split into ad groups by family**, on Manual CPC.
- **Labels are clean, unlike Sunday Citizen.** Every product has a product type and custom labels. Custom label 0 is a product-family label (Complete Protein, Black Edition Powder, Diet Powder, Hot & Savoury Meal Packs, Daily Greens, Bundles and so on), and 0% of spend is unlabelled. On Sunday Citizen, 38% of spend had no label. The structure doesn't use the labels yet.
- **Paused leftovers from the 2025 structure:** 4 Generic Shopping campaigns (`GENERIC_HIGH`, `HERO`, `LOW`, `MEAL`) and 3 paused Brand Shopping ad groups (Low, High, Powder Professional). Clutter, not a risk.
- **Brand terms are kept out of Generic Shopping.** "huel" terms cost £13.4k in Brand Shopping and effectively £0 in Generic Shopping over 90 days, so the brand exclusions work.

## 2. Target vs delivery: limited by the target, not budget

90 days to 3 Oct, leaving out the last 3 days for conversion lag:

| Campaign | Target | 90d ROAS | Last 30d ROAS | Budget used (30d) | Impr. share | Lost to budget | Lost to rank |
|---|---|---|---|---|---|---|---|
| Shopping Generic Core | 0.80 | **0.80** | 0.77 | 71% | 62% | 0% | 38% |
| Shopping Restrict | 0.80 | 0.81 | 0.69 | 100% | 37% | 20% | 43% |

- **Core hits its target exactly.** It spends about 70% of its £6.2k daily budget and loses no impression share to budget. Spend is controlled by the target, which is where we want to be.
- **Restrict is the opposite.** It spends its whole budget, loses 20% of impression share to budget, and the last 30 days fell to 0.69. It's small (£8.9k over 90 days).
- **The in-platform 0.8 isn't the real test.** It shows Google doing what it was told, not whether the spend is worth it. Judging the target needs Fospha CAC or a backend-adjusted ratio (section 11).

## 3. Product level vs family level: do results repeat?

Same test as Sunday Citizen: does a product's ROAS in Mar–Jun predict its ROAS in Jun–Sep?

| Level | Huel | Sunday Citizen |
|---|---|---|
| Individual products (£200+ spend) | r = 0.18 | r = 0.04 |
| Product family | r = 0.44 | r = 0.72 |

- **Product-level winners don't repeat**, the same as on Sunday Citizen. Don't pick winners by SKU.
- **Family level holds up better, but not as well as Sunday Citizen.** The reason is the single target: it pushes every family towards about 0.8, so they barely differ. Most sit at 0.75–0.90. The outliers were Hot & Savoury Pots (1.10), Daily A-Z (1.21) and Bundles (0.67).
- **Spend is very concentrated.** One product, Complete Protein Chocolate Fudge Brownie (`ptn-cfb-20`), takes **27% of Generic Shopping spend** (£122k over 90 days). The top 5 products take 55%.

## 4. Shopping Core by product family

180 days to 3 Oct 2026, £845.6k spend. All conversions, not only new customers. Conversion value is the whole basket, credited to the product clicked.

| Family | Spend | Share | ROAS | Cost / Conv | Avg order | Max Cost / Conv at 0.8 | CPC | Conv rate | 90d ROAS | 90d Cost / Conv |
|---|---|---|---|---|---|---|---|---|---|---|
| Complete Protein | £249.5k | 30% | 0.78 | £58 | £45 | £56 | £2.59 | 4.4% | 0.73 | £62 |
| Black Edition powder | £171.2k | 20% | 0.80 | £69 | £56 | £70 | £1.91 | 2.8% | 0.81 | £69 |
| Diet powder | £134.0k | 16% | 0.82 | £68 | £56 | £70 | £2.54 | 3.8% | 0.78 | £71 |
| Hot & Savoury meal packs | £70.0k | 8% | 0.91 | £64 | £58 | £73 | £1.24 | 1.9% | 0.90 | £65 |
| Powder (v3.0) | £54.8k | 6% | 0.78 | £66 | £52 | £65 | £1.72 | 2.6% | 0.77 | £66 |
| Bundles | £40.4k | 5% | 0.78 | £79 | £62 | £78 | £1.74 | 2.2% | **0.69** | £84 |
| Hot & Savoury pots | £36.5k | 4% | 1.06 | £55 | £58 | £73 | £1.13 | 2.1% | 1.09 | £50 |
| Daily Greens | £27.2k | 3% | 0.81 | £72 | £59 | £74 | £2.20 | 3.0% | 0.85 | £71 |
| Lite RTD | £19.5k | 2% | 0.74 | £82 | £61 | £76 | £2.12 | 2.6% | **0.69** | £89 |
| RTD (standard) | £11.8k | 1% | 0.81 | £72 | £58 | £73 | £1.22 | 1.7% | 0.84 | £69 |
| Powder gluten-free | £10.8k | 1% | 0.90 | £55 | £49 | £61 | £1.86 | 3.4% | 0.87 | £56 |
| Black Edition RTD | £8.7k | 1% | 0.77 | £80 | £61 | £76 | £1.62 | 2.0% | 0.77 | £74 |
| Lite Ramen | £7.8k | 1% | 1.01 | £57 | £58 | £73 | £1.15–1.36 | 2.1–2.4% | 1.02 | £58 |
| Black Edition Ramen | £3.4k | 0.4% | 1.01 | £54 | £55 | £69 | (with Lite) | (with Lite) | 1.01 | £54 |
| **Core total** | **£845.6k** | | **0.82** | **£64** | **£53** | | | | **0.80** | |

"Max Cost / Conv at 0.8" = average order ÷ 0.8, the most Google can pay per conversion and still hit the target.

What the table shows:
- **ROAS is bunched together, while CPA varies a lot.** Most families sit at 0.77–0.91, which is the single 0.8 target doing its job. CPA runs from £54 to £82, so the most expensive families cost 1.5x the cheapest.
- **A ROAS target favours bigger orders.** At 0.8, Google will pay about £80 for a bundle or RTD customer (£61–62 orders) and holds Complete Protein to about £58 (£45 orders).
- **CPC alone points the wrong way.** Complete Protein has the highest CPC in Core (£2.59) but also the highest conversion rate (4.4%), so its CPA is still among the lowest.
- **The top 3 families (Complete Protein, Black Edition powder, Diet powder) are 65% of Core spend.** That's where a different target would matter.
- **Hot & Savoury runs above target** at 1.0–1.1 across pots and ramen. Google isn't putting more money there at the current target, most likely because demand is limited. Check impression share by product before promising volume.
- **Bundles and Lite RTD are getting worse,** at 0.69 over the last 90 days. About £26k is at stake there.

## 5. What the current setup is doing

- With Target ROAS, Google bids on conversion likelihood × predicted order value. So the most it pays per conversion is roughly order value ÷ target.
- **A single 0.8 target pays more for bigger baskets.** It works as a rough stand-in for LTV if value grows with the basket, while still keeping a lid on CAC. It's a middle ground between CAC and LTV that doesn't pick a lane. CAC still ranges from £54 to £82.
- **It's also a campaign average, so families above target carry the ones below it.** Over 90 days Core hit 0.80, but:

  | | 90d spend | 90d ROAS |
  |---|---|---|
  | Complete Protein | £148k (34% of Core) | **0.73** |
  | Everything else in Core | £290k | **0.83** |

  - Above target: Hot & Savoury pots 1.09, ramen 1.01–1.02, H&S meal packs 0.90, gluten-free powder 0.87.
  - Below target: Complete Protein 0.73, Bundles 0.69, Lite RTD 0.69.

## 6. Complete Protein

- **Lowest CPA in Generic Shopping every month, but the lowest order value:**

  | Generic Shopping, Apr–Sep (monthly range) | CPA | Avg order | ROAS |
  |---|---|---|---|
  | Complete Protein | **£52–64** | **£45–47** | 0.70–0.88 |
  | Black Edition powder | £67–73 | £54–58 | 0.73–0.84 |
  | Diet powder | £61–76 | £54–60 | 0.72–0.88 |

  It looks no better on ROAS only because its orders are smaller.
- **It has already scaled, and the extra spend costs more.** Spend went from £22k in April to about £50k a month. CPA rose from £52 to £64 over the same period. ROAS went 0.87–0.88 (Apr–May) → 0.80 (Jun–Jul) → 0.70–0.72 (Aug–Sep). Its last few pounds are the least efficient in Core.
- **It has around 800 conversions a month**, so it easily has the volume to run as its own campaign.
- **What happens if it's split out depends entirely on the target:**
  - **Same 0.8 target:** it has to earn 0.8 on its own. It held 0.81–0.88 at £22–40k a month and slipped to 0.70–0.72 at about £50k, so it would likely settle at about **£40k a month instead of £50k**, at about £55 per conversion instead of £62. The rest of Core (averaging 0.83) gets pushed slightly harder to hit its own 0.8. Measured on first-order value, the total is the same or slightly worse. Splitting at the same target only adds a constraint.
  - **Lower target (e.g. 0.70):** it keeps or gains volume, and its cost per conversion goes above £62.
  - **Higher target:** it shrinks further and gets cheaper per customer.
- **Which way the target should move can't be answered from ad data.** It depends on what a Complete Protein customer is worth (section 9).
- **Watch-out:** Complete Protein could be skewed towards existing customers adding protein to an order. If so, its new-customer CAC is worse than £58. Check with Fospha or backend new-customer share by product.
- **It ties to Search.** Every Protein Search ad sends "protein powder" searches to Black Edition, not Complete Protein. That's an LTV call made in Search, and it's the only place LTV shows up in the account. The audit's 4.5 handles the Search side with a duplicate ad to the Complete Protein page.

## 7. Two readings of "equal retention"

They give opposite answers, which is the main argument for getting LTV data first.

**A. Every new customer is worth the same over 12 months, whatever they buy first (CAC is the right measure).**
- The current setup is getting it wrong. It overpays for RTD and bundle customers and underpays for Complete Protein and Hot & Savoury.
- What I'd do:
  - Split Core by CPA. A low-CPA campaign (Complete Protein, Hot & Savoury, ramen, gluten-free powder) gets a lower target. A high-CPA campaign (RTDs, bundles, Daily Greens) gets a higher target or a lower budget.
  - Or give every conversion the same value and bid on target CPA, so Google buys the most customers.
- Rough size of the prize: the high-CPA families spent about £108k over 180 days at about £77 per conversion. The same money at the low-CPA tier's recent £62 would buy up to about 25% more customers. It would be less in practice, because returns diminish (Complete Protein's CPA already went from £52 to £64 as spend doubled).
- This is the likelier situation for a subscription brand, where what matters is whether the customer subscribes, not what was in the first basket.

**B. Repeat rates are equal, so a customer's value rises with their first order (ROAS is the right measure).** This is the reading Michael confirmed he meant.
- The single 0.8 target is right in principle. The problem is that it's an average, so Complete Protein runs at 0.73 carried by the rest at 0.83.
- What I'd do:
  1. Move Complete Protein into its own campaign at 0.8. Google then has to earn 0.8 on it, which pulls back the spend running at about 0.70. It's one change, so the effect is easy to read.
  2. The rest of Core, at its own 0.8, has room to bid up the families above target, Hot & Savoury especially. Blended ROAS stays at 0.8, but spend moves from Complete Protein's least efficient spend to families with room to grow. Check whether Hot & Savoury is demand-limited first.
  3. Bundles and Lite RTD get pulled up to target by the same change.
- **The line for the doc:** the right call on Complete Protein flips with retention. If every customer is worth the same, it's the cheapest customer in Shopping and should be pushed. If repeat rates are equal, it's overfunded at 0.73. The same campaign split serves both; only the target changes.

## 8. If we leaned 100% on CAC

1. **Bid Core on target CPA, or give every conversion the same value.** Spend shifts towards Complete Protein, Hot & Savoury, ramen and gluten-free powder (£54–58 CAC) and away from RTDs and bundles.
2. **Put the low-CAC families in their own campaign.**

   | Family | 180d spend | 180d Cost / Conv | 90d Cost / Conv | Avg order |
   |---|---|---|---|---|
   | Hot & Savoury pots | £36.5k | £55 | £50 | £58 |
   | Lite Ramen / BE Ramen | £11.1k | £54–57 | £54–58 | £55–58 |
   | Powder gluten-free | £10.8k | £55 | £56 | £49 |
   | Complete Protein | £249.5k | £58 | £62 | £45 |
   | **Low-CAC group** | **£308k (36% of Core)** | **£58** | | |
   | Rest of Core | £538k | £69 | | |

   - Set it on target CPA, or target ROAS with every conversion given the same value, starting around today's £58–62, with its own budget so it can't swallow Core.
   - H&S meal packs (£64) sit exactly on the Core average, so they stay in the main campaign.
   - In practice this is a Complete Protein campaign: Complete Protein is 81% of the group's spend, and the other three are small.
3. **Cap the high-CAC families.** Lite RTD, BE RTD, bundles, Daily Greens and standard RTD: £108k, 13% of Core, at £77. Put them in a campaign with a CAC ceiling, or pull back hardest on Lite RTD (£82) and BE RTD (£80).

**Our position:** we give this as the one example of a split that brings CAC down, and say we won't do it yet. It buys the cheapest customer, not the most valuable one. If Complete Protein buyers turn out to be one-off tub buyers, it's exactly the wrong move. To optimise for LTV, we need 12-month LTV by first-order product.

## 9. LTV by first-order product: the deciding data

**Steps:**
1. Get 12-month LTV (revenue) per new customer, split by the product in their first order. "First order" already means first order with Huel, so the backend's new-customer flag gives the split.
2. Check whether first-order ROAS **ranks** products the same way as 12-month ROAS. The absolute numbers don't need to match. If the ranking holds, first-order data is a good enough guide, and Black Edition and Complete Protein can run side by side in Search and let performance decide. If it flips, make the call on the highest-LTV product.
3. Use it to set Shopping targets by family, and to decide which other products are worth testing in Search.

**The CAC vs LTV call is Huel's.** The targets should follow whichever one the business is judged on. Either way we judge Search and Shopping on CAC against LTV, not on first-order ROAS. ROAS stays the setting we give Google, not the yardstick.

**Turning LTV into a target:**
> Target ROAS = average first order value ÷ the most you'll pay per customer
> The most you'll pay = 12-month LTV ÷ the LTV:CAC ratio you want

Illustrative only. These LTV figures are made up; they're what we need from Huel. Assumes a 2.5x LTV:CAC requirement.

| Scenario | Product | 12m LTV | Max CAC | Avg first order | Target ROAS |
|---|---|---|---|---|---|
| Every customer worth the same | Complete Protein | £150 | £60 | £45 | **0.75 (lower)** |
| | Black Edition powder | £150 | £60 | £56 | 0.93 |
| | Bundles | £150 | £60 | £62 | 1.03 |
| Complete Protein buyers churn faster | Complete Protein | £90 | £36 | £45 | **1.25 (higher)** |
| | Black Edition powder | £200 | £80 | £56 | 0.70 |

**What else we'd need from Huel:**
- The share of each product's buyers who are new customers.
- Margin by product, if it differs much.
- (We can pull ourselves) product-level impression share for Complete Protein, to see whether there's room to spend more.

## 10. Black Edition vs Complete Protein: the two blind spots

The single 0.8 target already pays more for a Black Edition customer (£69) than a Complete Protein one (£58), because the first basket is bigger. That's the right direction, but it's sized on basket value alone:

1. **No 12-month LTV, so Black Edition is probably underbid.** Huel already sends protein searches to Black Edition because it believes those customers are worth more. If that's right, Black Edition's lead should be bigger than basket size gives it. So the account says one thing in Search and another in Shopping.
2. **Every purchase counts, new or returning, which could mean Black Edition is overbid.** Returning customers reordering are more likely to buy the core product than try Complete Protein. If more of Black Edition's conversions are returning customers, its real cost per new customer is above £69.

They pull in opposite directions, so we can't tell from inside the account which way it nets out. 12-month LTV by first-order product and the New Customer Purchase event (audit 1.5) settle it. New Customer Purchase would also give cost per new customer by family directly in Google.

## 11. When to split (general rule, any account)

**Only split when you'd give the new campaign a different target, and judge that target on CAC against LTV, not ROAS.**

Split when all of these are true:
1. **You'd set a different target for it.** A £ of first-order revenue is worth materially more or less in that group (LTV multiple, margin or new-customer share).
2. **The difference holds over time.** Results repeat period to period at that level (family, not SKU).
3. **It has enough conversions of its own,** roughly 30–50+ a month. Complete Protein (~800) qualifies; the ramen lines don't.

Or when you need control rather than efficiency:
4. **Budget control:** one group is swallowing the campaign (Complete Protein is 30% of Core).
5. **A different objective:** one group on a CAC target, the rest on ROAS.
6. **Operational reasons:** stock, promos or launches that need their own on/off switch.

**Don't split just because a group's ROAS looks different under the same target.** That's usually Google moving spend until the last £1 earns the same everywhere: high-volume groups average lower, small ones higher. Splitting at the same target fragments the data and makes things worse.

**For Huel:** if LTV differs between the top 3 families (65% of Core), split those three out with LTV-based targets and keep everything else in one campaign. Until then, a single target is the right default.

## 12. Hot & Savoury pots almost stopped serving

- £9.6k in August, £0.4k in September.
- That looks like stock or a feed issue rather than bidding. It's in Key points to clarify.
- Until it's explained, pots can't be relied on for volume in a low-CAC campaign.

## 13. Feed health: very clean

- All 115 products are eligible, in stock and free of disapprovals. All 115 got impressions in the 90 days, so submitted equals serving.
- Flavours are separate products, and each one gets impressions.
- **Subscription pricing isn't in the feed.** Prices are the one-off price (e.g. Complete Protein £25), and "Free Shaker & T-shirt" is written into titles instead.
- One sloppy title: "Professional Protein Powder Vanilla -".

## 14. PMax: tested and paused, the right call

- `UK_PMAX_GENERIC` ran in Oct 2025, Dec 2025 and Mar–May 2026 (peak £60k in April). It has been paused since June.
- It reported 2.1–2.95x ROAS in Apr–May (April £60k at 2.09, May £37k at 2.95), against about 0.85x for Standard Generic Shopping in the same months.
- That gap is the classic sign of PMax claiming brand and existing-customer conversions. Going with Standard matches what we did on Sunday Citizen. A positive finding.
- Option for later: a controlled re-test with brand exclusions and new-customer reporting before writing it off for good.
- Correction: the 25 Sep pass said "the account has no PMax". That was true only for the 90-day window; the 6 Oct pass found the history above.

## 15. Search terms and negatives in Shopping

- **"elderly":** about 60% of this spend is Generic Shopping (Core). Search bidding had already mostly backed off it (−51% per day), but Shopping hadn't (£6.1 → £4.7 a day). Over 180 days: £1,434 total, £962 of it Shopping. Added as a phrase negative on Search **and** Shopping. These are clinical and care nutrition searches (Ensure/Fortisip-type, for a parent or patient).
- **"healf":** Search + Shopping. £45 of the 180-day £861 was Shopping.
- **Discount codes: Search only for now.** On Generic Shopping they spent £247 in the last 30 days and £1,376 over 180 days at about 0.40 ROAS. **Revisit Shopping in a month** (from 7 Oct, so early November). Competitor-code terms running in Shopping include "myprotein discount code" (£335 over 90 days, all Shopping), "yfood discount code" (£113 of £163 in Shopping) and "bulk discount code" (about £55 in Shopping).
- **"cancer": dropped.** About 60% Shopping as well (£2.0 → £1.4 a day), but only about £60 in the last 30 days across both channels.
- **"reviews": left off the list.** £1,407 of its £3,773 (90 days) was Shopping. It runs at 0.47 ROAS on full coverage, and the biggest terms (AG1, Slim Fast, "protein powder reviews") convert.
- An earlier suggestion, before the user's calls above, was for the Shopping negative lists to also carry discount code, reviews, over 50 and recipes (£8–13 a day in Shopping, with no bid learning to fall back on). Only "elderly" and "healf" went ahead. "Over 50" and "recipes" weren't revisited on Shopping specifically.
- Caveat: `search_term_view` includes Shopping, so Search-only figures had to be re-split by channel. The early pattern figures mixed the two.

## 16. Segments

- **Device: no gap.** Generic Shopping returns 0.80 on desktop vs 0.81 on mobile. About 85% of spend is mobile. (Sunday Citizen was 3.4 vs 2.2.)
- **Geo: flat** across UK regions (0.70–0.83 ROAS, £62–77 CPA; this pull wasn't split by channel).
- **Time of day: a strong pattern, but not a setting to change.** Generic Shopping returns 0.60–0.70 between 7am and 4pm and 1.0–1.4 between 9pm and 1am.
  - Target ROAS bids each auction on its own expected value and already uses time of day. Manual ad-schedule bid adjustments are ignored under Target ROAS.
  - It's a talking point, plus one practical rule: budget-limited campaigns shouldn't run dry before the evening.

## 17. Audiences (Customer Match exclusions)

- Customer Match lists are excluded on **both Generic Shopping campaigns and Brand Shopping**, as well as on Search.
  - "UK_CM_MANUAL_20260731_12mo_purchasers": a manual upload on 31 Jul 2026, about 130k matched, 76% match rate.
  - "All customer purchases (last 12 months)": about 270k.
  - "Purchased – GA4": about 86k.
- **The automated daily-sync list shows a size of 0.** It's excluded on most campaigns and doing nothing.
- So exclusions rely on manual snapshots. Anyone who became a customer after 31 Jul isn't excluded from Shopping.
- This contradicts the line in audit 1.5, "existing customers can't go into a Customer Match file". The doc still has that wording. Suggested rewording: "the Customer Match lists rely on manual uploads and the automated sync is empty", unless the legal blocker is specifically about the sync. Check with Huel.

## 18. Incrementality and measurement

- **Natural experiments.** Days when Generic Shopping spend dropped 40%+ below its 7-day average:

  | Date | Shopping spend vs 7-day avg | Google-reported value vs 7-day avg |
  |---|---|---|
  | Fri 26 Sep 2025 | −48% | −5% |
  | 3–6 Dec 2025 | −49% to −53% | −23% to −40% (whole account also cut ~45%) |
  | Sat 28 Feb 2026 | −52% | −15% |
  | Sat 14 Mar 2026 | −42% | −15% |
  | Fri 21 Aug 2026 | −45% | −18% |

  - 26 Sep 2025 is the most interesting: spend halved and Google-reported value barely moved.
  - Can't be finished without Huel's daily store orders and revenue, split new vs returning, for these dates plus the 2 weeks around each. Compare Saturdays against Saturdays.
  - This was dropped from section 2 when it was renamed "Brand vs Non-Brand", so it's unused.
- **Fospha ratio for Shopping.** The Search work on 2 Oct built a Google-ROAS-to-Fospha-CAC ratio (£124) for non-brand Search only. Shopping isn't covered: Fospha's "Google Non-brand Total" also includes Shopping_Generic (£151k), and Shopping needs its own ratio from Google's Shopping ROAS against Fospha's Shopping_Generic CAC.
- **Geo test.** The Brand Shopping step test is cheap and fast. A Stella-style geo test (synthetic control, 30–35 days, backend new customers by region) is better kept for Generic Shopping and non-brand incrementality, where there's enough spend for a result that holds up statistically.
- **Attribution ladder.** The planned step of checking CPA against a backend-adjusted target needs Huel's backend last-click numbers or Fospha at campaign level.

## 19. Volume at better efficiency: where Shopping sits

Ranked by the difference each would make (7 Oct):
1. **Brand Shopping** (in the doc, section 2). Loses 52% of impression share to budget; Fospha CAC £23–28. The only big pot of spend where budget is what holds it back.
2. **Boost the value of new customers** (in the doc, 1.5). At the same 0.8, Google shifts spend towards new customers. The biggest efficiency lever, because it changes what the target buys.
3. Landing page relevance (Search).
4. A lower target as a step test (Search). Note: a lower target raises CAC by design. It's a volume lever, so it comes after the efficiency moves.
5. **Shopping: separate targets only where the data supports them.** Superseded by sections 7–11: split only with LTV in hand.
6. **A proper PMax re-test**, with brand exclusions and new-customer reporting.
7. Small budget wins (Search Weight Gain).

## 20. Brand Shopping: details not in the doc

Section 2 of the doc already covers: 69% of impression share lost to budget, the reseller argument, Fospha not discounting it, the July→August incremental CAC of £31 (147 more customers on £4.6k), the max CPC vs Target ROAS endgame, and the 1-2-3 test plan.

Not in the doc:
- **Budget-change history** (spend steps that line up with budget-limited periods; the API doesn't show past budget settings):

  | Change | Spend per week | Google conv per week | Cost per conversion |
  |---|---|---|---|
  | w/c 21 Jul 2025: up ~40% | £2.3–2.5k → £3.3–3.6k (4 weeks, then down w/c 18 Aug) | 360–410 → 475–570 | £6.1 → £6.3–7.2 |
  | w/c 29 Dec 2025: up ~100% | £1.3–1.7k → £2.6–3.3k | 155–215 → 340–410 | ~£7.5 |
  | w/c 8 Jun 2026: cut ~65% | ~£1.9k → ~£0.7k (5 weeks) | ~245 → 72–118 | – |
  | w/c 13 Jul 2026: restored ~3x | ~£0.7k → £2.0–2.2k | ~100 → 250–305 | £7–8 |
  | w/c 17 Aug 2026: up ~50% | £2.0–2.2k → £2.8–3.4k | ~273 → 333–383 | £7.8 → £8.7–9.4 |

  - Each increase brought more conversions, and cost per conversion barely moved. From August 2026, each extra conversion cost roughly £13.
  - The June–July 2026 cut and restore is the cleanest natural experiment. The January step overlaps the New Year peak, so it's the weakest evidence.
- **Fospha by month:**

  | Month | Spend | Spend per day | New customers | CAC |
  |---|---|---|---|---|
  | May | £9.9k | ~£320 | 529 | £18.78 |
  | Jun | £4.2k | | 223 | £18.79 |
  | Jul | £6.7k | ~£217 | 301 | £22.34 |
  | Aug | £11.3k | ~£366 | 448 | £25.30 |
  | Sep (to ~24th) | £11.2k | ~£465 | 402 | £27.86 |

  - New customers moved with spend when it was cut in June, at the same CAC.
  - 2,358 new customers since April at a £22.62 average CAC.
  - CAC creeps up as spend rises (diminishing returns), so doubling or tripling would probably put it at £30+.
  - April and May both show exactly £9,941 of spend in Fospha. Possibly an export quirk; worth a second look.
- **Between us, not for the doc:** blended CAC target is £32 including organic/unattributed; channel-level CAC is £80, so even a £40 Fospha DDA CAC on Brand Shopping pushes blended CAC down if it brings new customers.
- **Monitoring detail beyond the doc's 1-2-3:**
  - Incremental CAC = (test-week spend − baseline spend) ÷ (test-week new customers − baseline new customers), weekly and as a running total.
  - Measure on total brand new customers (Search + Shopping). Use Brand Search as a demand control for seasonality.
  - Google-side checks: impression share lost to budget should fall from ~55% towards 0–10%; average CPC should stay around £0.42; Google cost per conversion should stay at £8–13. If lost-to-budget reaches ~0% and spend stops rising, that's the ceiling.
  - Suggested decision rules: ≤£40 incremental CAC after 3 weeks → step up to 3x; £40–60 → hold at 2x; above £60, or Brand Search new customers drop by a similar amount → roll back.
  - Cleaner option: alternate weeks between 1x and 2x for 4–6 weeks.
  - Small inconsistency: the doc says hold the step-up for at least 4 weeks; the chat plan said 3.
- **Geo test (Stella approach) for Brand Shopping:** split the UK into postcode areas or ITV regions, run a 2x copy in treatment regions, and measure backend new customers by region over 4–5 weeks. Catches: only £7–8k of extra spend over 5 weeks (under Stella's typical $15–30k), few usable UK regions, and it needs new customers by postcode from Huel. Verdict: run the step test now.
- **Bigger budget numbers have moved since.** Brand Shopping lost 69% of impression share to budget over the audit's 90 days, and 50–55% after the August increase. MTD 1–20 Sep, Brand Shopping spend was up 46% on August at 5.73x ROAS.

## 21. Recent performance (after the audit)

**21 Sep review (week of 14–20 Sep):**
- Core: £32.1k for the week, 0.61x ROAS, £82 CPA. Conversions −23.5% on spend −7.2%.
- Non-brand Shopping was the one decline on the Shopping side that held up after matching for conversion lag: conversions −10.4% and ROAS −12.3% on spend +9.9%.
- Month to date (1–20 Sep vs August): non-brand Shopping £98.2k, 0.72x, £71 CPA. Restrict £695 for the week at 0.80x.

**19 Oct weekly review (12–18 Oct vs 5–11 Oct):**
- **Core is shrinking and getting less efficient.** Daily spend slid from £5.4k on 5 Oct to about £2.5k on 18 Oct, and cost per conversion rose from £69 to £81.
- Budget isn't the limit: about 40% of eligible impressions are lost to ad rank.
- The 15 Oct budget cut (£6,200 → £5,800 a day) has no effect while the campaign spends under £3k.
- **A product group was excluded on 15 Oct.** Confirm it was intended.
- Next step: check auction insights for a new competitor before touching the ROAS target.

## 22. Key points to clarify (Shopping)

1. Can Huel share 12-month LTV by first-order product, for new customers?
2. Are we prioritising CAC, LTV, or a CAC ceiling with LTV as the tiebreaker?
3. What share of each product's buyers are new customers? Margin by product?
4. Hot & Savoury pots: why did they almost stop serving in September (stock or feed)?
5. Was a target changed in early September? Change history through the API only covers 30 days.
6. Was the product-group exclusion on 15 Oct in Core intended?
7. Daily store orders (new vs returning) around the natural-experiment dates.
8. Is the Customer Match legal blocker about the automated sync specifically?

## 23. Corrections made along the way

So these don't get repeated:
- **"No PMax in the account"** was true only for the 90-day window. It ran Oct 2025 – May 2026 and has been paused since June.
- **Complete Protein's share.** 27% is the single top SKU's share of 90-day Generic Shopping spend. As a family it's 30% of 180-day Core spend, and 34% over 90 days.
- **Splitting Complete Protein out at the same target** was first put forward as "the clean move", then withdrawn: at the same target, it only adds a constraint.
- **Early search-pattern figures mixed Search and Shopping spend.** They were re-split by channel.

## Appendix: draft Shopping copy already written (7 Oct)

This was written into an earlier "Section 4 (to paste in)" doc, before the user narrowed section 4 to non-brand Search only. It still has "ifs" to remove before it goes client-facing.

> **4.1 LTV by first-order product**
>
> In Search, protein powder searches go to Black Edition rather than Complete Protein - a call made on LTV. That's a reasonable call, but it's the only place LTV shows up in the account. Shopping runs a single 0.8 target across every product, there's no LTV figure by first-order product to set targets against (see 1.3), and we're measured on CAC.
>
> **What needs to happen.**
> 1. **Get 12-month LTV by first-order product** - for new customers only.
> 2. **Check whether first-order ROAS predicts 12-month ROAS.** If products rank the same on both, first-order data is a good enough guide - we can run Black Edition and Complete Protein side by side in Search and let performance decide. If the ranking changes, we make the call on the highest-LTV product.
> 3. **Use it to set Shopping targets** (4.2) and decide which other products are worth testing in Search.
>
> Underneath this is a decision only you can make - whether we prioritise CAC or LTV. Either way, I'd judge Search and Shopping on CAC against LTV rather than on first-order ROAS. ROAS stays the setting we give Google, not the yardstick.
>
> **4.2 Shopping: one target, bids follow the first basket**
>
> Generic Shopping (Core) runs every product at a 0.8 target. With Target ROAS, Google bids on how likely a click is to convert multiplied by the predicted order value - so the most it will pay per conversion is roughly the order value divided by 0.8. That's exactly what the data shows: *[top 8 families table: Spend, Share, ROAS, Cost / Conv, Avg order]*
>
> The single target already pays more for a Black Edition customer (£69) than a Complete Protein one (£58), because the first basket is bigger. But it's sized on basket value alone, with two blind spots:
> - **No LTV.** If Black Edition customers are worth more over 12 months - the reason protein searches go to Black Edition in Search - a basket-based target is underbidding it.
> - **All purchases, not new customers.** If more of Black Edition's conversions are existing customers reordering, its real cost per new customer is higher than £69, and it may be overbid.
>
> They pull in opposite directions, so we can't tell which way it nets out from the account alone. 12-month LTV by first-order product and the New Customer Purchase event from 1.5 answer it.
>
> **How I'd split to bring CAC down.** If every new customer were worth the same, I'd move the four cheapest families - Complete Protein, Hot & Savoury pots, gluten-free powder and ramen - into their own campaign. That's £308k, 36% of Core, at £58 per conversion against £69 for the rest. It would be bid on CAC rather than basket value, with its own budget so it can't swallow Core.
>
> **I wouldn't do it yet.** It buys the cheapest customer, not the most valuable one - if Complete Protein buyers turn out to be one-off tub buyers, it's exactly the wrong move. Depending on LTV, the same family could need a lower target or a higher one, and the ad data alone can't tell us which.
>
> To optimise for LTV, we need 12-month LTV by first-order product. With it, each family's target becomes its order value divided by the most we'll pay for a customer - and that maximum comes from LTV. Until then, a single target is the right default: splitting at the same target only adds constraints and thins out the data.
>
> **When a split makes sense:** when we'd give the group a different target, the difference holds up over time, and it has enough conversions of its own for the bidding to learn from. The top three families are 65% of Core spend, so that's where different targets would matter.
