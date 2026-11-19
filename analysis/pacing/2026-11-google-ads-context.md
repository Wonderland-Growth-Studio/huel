# Huel EU + UK Google Ads: working context (as of 19 Nov 2026)

**Status: nothing here is signed off.** These are notes on how we work, what we've learned, and what's under discussion. Every account change listed is a proposal, unless it's marked as the user's own position. Nothing has been changed in any account: the API connection is read-only.

This file replaces the separate per-market "plan" files. They are still in git history.

---

## 1. How Huel makes performance decisions

1. Start from Fospha's **Actuals vs Target** view for each market: new-customer (NC) pacing against target, and CPA pacing against target.
2. Classify each market:
   - NC behind, CPA on target: chase NC.
   - NC on track, CPA over: save budget, trim.
   - NC behind and CPA over: reallocate to efficient channels rather than scale.
3. Use channel efficiency (Fospha DDA+ CAC) to decide what happens per channel and per campaign.
4. Regions are UK, US and Europe (DE, PL, SE, Rest of Europe). The user owns Google Ads for Europe and the UK.

Huel's channel teams don't have a clear Google picture, so working it out is our job.

## 2. Standing instructions from the user

**Measurement**
- **The KPI is Fospha DDA+ (click-based).** FA isn't trusted. The aim isn't for DDA+ CAC to match blended CAC; it's to find the right efficiency level.
- **Use Google's "New Customer Purchase" conversion** for all analyses (EU: "New customer Purchases"). Use purchases only where NC doesn't fire (PL).
- **Report volumes,** not only cost per NC.
- **Base everything on real account and Fospha data,** not Google's projections or simulators.

**How recommendations are made**
- Every recommendation needs a why, with the data behind it.
- Develop conviction; don't get swayed too easily.
- Stress-test every recommendation with a second Opus agent. One side pulls the data and makes the recommendation; the other reviews the same data, then the recommendation (connect inputs to outputs).
- Act as a performance marketer, not a doc-writer: actions first, numbered lists, less wording. When the user is on a call, cover only what we do.

**Bidding and budgets**
- **No Max Conversions or other conversion-based bidding on brand.** Manual CPC gets the same IS at a lower CPC.
- **Pause only when Smart Bidding will move the spend somewhere more efficient,** i.e. in budget-capped campaigns, or where an item is hurting another bucket. In an uncapped tROAS or tCPA campaign, leave weak items to Smart Bidding.
- **Don't tinker with budget ceilings;** a change either works or it doesn't. Change a budget only when it's actually binding: budget-lost IS, or the monthly limit.
- **"Move budget" means move actual spend,** not the nominal budget in Google.
- **Germany:** Google non-brand Search plus Shopping spend stays constant, with spend shifted toward Shopping.
- **Germany Shopping:** decide on what keeps the funnel big.
- **Automate monitoring** (rules and alerts) rather than relying on manual checks.

## 3. Facts about the business and accounts

- **BFCM:** Huel runs BFCM on exactly **27–30 Nov**, not extended.
- **UK Demand Gen budget is protected** and is run separately; it isn't cut.
- **The user has no Merchant Center access yet.**
- **Fospha's Halo tab is irrelevant:** it measures non-DTC.
- **Accounts:**
  - Huel EU (8046071519) is in EUR.
  - Huel UK (3455924316) is in GBP.
  - Fospha reports in GBP (EUR × ≈0.87).
- **Monthly spend limit:**
  - Google caps a month at 30.4 × the daily budget.
  - A mid-month budget change resets the limit to spend so far + new budget × days left.
  - Campaigns that over-deliver can get throttled late in the month. The check script is in `.claude/skills/google-ads-budget-pacing/`.
- **Conversion actions:**
  - EU primary actions: DE/PL/SE Google Ads Purchase and EU Adwords Tracking Purchases, all 7-day click.
  - EU new-customer action: "New customer Purchases", live since about 5 Oct.
    - Fires in DE, SE and ROE; **not in PL** (5 NC against 1,590 purchases).
    - In ROE, **DK shows conversions but 0 NC.**
  - UK: "Google Ads Purchase" is primary, alongside "New Customer Purchase".
  - GA4 imports use 30-day windows.
- **How Google NC compares with Fospha:**
  - DE: about 1.3× Fospha (brand matches: 857 vs 862).
  - UK Shopping: about 1.8× Fospha.
  - ROE generic: roughly in line.
- **Demand Gen NC is inflated by engaged-view and view-through conversions.** Of UK Demand Gen TEST's 652 NC, only 83 are clicks, at £768 each, against Fospha's £1,110.

### Tracking: Google Ads tag vs GA4
- **Since Aug 2026, GA4 reports about 30% more Google purchases than the Ads tag.** The tag stayed flat.
  - The jump is in same-day purchases.
  - It's uniform across campaigns and devices.
  - All four EU GA4 properties moved in the same month.
- **Fospha DE NC rose only 4% from Jul to Aug,** so real orders didn't jump.
- **Two explanations remain:**
  - (a) GA4 now sees purchases the tag misses.
  - (b) GA4 now credits Google with orders it used to give to organic or direct.
  - GA4 isn't fabricating orders.
- **Deciding test (in GA4):** compare DE all-channel purchases with backend orders for July against August, and check GA4 Admin change history for early August.
- **Working assumption until then:** keep bidding on the tag. Don't swap or add GA4 as a primary conversion before BFCM.
- **Housekeeping:**
  - "Transactions DK (All Web Site Data)" is a dead UA action that's still a primary conversion.
  - Default conversion values are worth checking: DE €62, PL €265, SE €50, EU €1.

## 4. Market snapshot (Fospha, Nov MTD to about 17 Nov)

| Market | Spend | NC | NC vs target | CPA vs target | User's read |
|---|---:|---:|---:|---:|---|
| DE | £72.7k | 1,830 | 87.9% | 107.4% | Needs help |
| PL | £31.6k | 1,284 | 89.8% | 114.5% | Needs help |
| SE | £29.8k | 847 | 90.1% | 130.6% | Needs help |
| ROE | £147.2k (later screenshot) | 3,830 | 108.3% | 113.5% | Best of the bunch; slight trimming |
| UK | – | – | 88% | 113% (£37.34 vs £33) | – |

---

## 5. Germany

**What the data shows**
- **Shopping generic (tROAS 108%):**
  - Spend fell about 41% from the week of 9 Nov.
  - AOV dropped to a 13-month low (€62 against a €71 median), so ROAS fell below target and Google cut CPC 23%. IS went from 39% to 33%.
  - Cost per NC held flat at €83–89 a week while spend swung from €3.8k to €6.5k. The cut spend was buying NC at about the average rate.
  - Fospha Shopping is £82–102.
- **16–18 Nov drop in generic Shopping:**
  - Generic Shopping fell from 7.4 to 3.5 NC a day, confirmed in GA4.
  - Brand Search and brand Shopping were normal over the same days.
  - Cause is unexplained; it isn't a checkout fault. Flag to ecom/CRO.
- **Search generic (tROAS 100%, €700 budget):**
  - About €113 per Google NC; Fospha £115–128.
  - Not budget-limited: 0% budget-lost IS, and it spends €220–620 a day. Lowering the nominal budget only cuts spend if it's set below actual spend.
- **Competitor terms** are already funnelled into competitor ad groups, with ad-group negatives (added 11 Nov). The prepmymeal leak stopped.
- **Brand (Max Conversions):**
  - Controlling for weekday, extra spend bought about 0 extra clicks. Spend and CPC moved together (€0.31 vs €0.26).
  - "huel" exact has 93% IS and 84% absolute-top IS at about €0.29.
  - The €99 days on 13–14 Nov were Google pacing, not a cap.
- **Channel mix:** Meta is about 75% of DE spend at £109–119. The NC gap is mainly a Meta question.

**Where the discussion stands** (none of this is signed off)
- **Shopping tROAS from 108% to 95%.** The user agreed with the direction ("keep the funnel big"); the timing was debated.
  - Proposed guardrail: revert if cost per NC is above about €110–120 on a 3-day read.
- **Shift actual non-brand spend from Search to Shopping, keeping the total constant.** This is the user's requirement. The open question is the lever: Shopping tROAS to pull spend in, and a Search tROAS tightening or a budget below run rate to take it out.
- **Search generic:** the user's position is to hold, and the user withdrew loosening Search tROAS. Run a monthly scan for competitor names leaking into non-competitor ad groups, and add them as phrase negatives.
- **Brand: Manual CPC.** This is the user's view; it was tested on the data.
  - Proposed bids: "huel" exact €0.35, products €0.50, broad €0.30.
  - Proposed exact keywords: "huel de", "huel rabattcode", "huel black friday".
  - Proposed budget: a one-off ceiling of €220–300.
  - Proposed automated rules: raise bids when absolute-top IS is under 80%, lower them when it's over 95%, and send a cost alert.
- **Dropped or withdrawn:**
  - Campaign-level competitor negatives (the ad-group structure already works).
  - Target IS on brand.
  - A brand budget raise under Max Conversions.
  - Product exclusions.
  - Daily Greens Merchant Center check (no access).
  - CAC "par" of £100. It's circular; the honest range is £37–100.

## 6. Poland

**What the data shows**
- **There's no NC tag,** so channel calls use Fospha and keyword calls use purchases.
- **Fospha 4-week CAC:**
  - Shopping £119.
  - Meta £117 (£91–94 at lower spend, £140+ at higher spend).
  - Search generic £158.
  - Brand £2.68.
- **Generic Shopping conversion rate halved on 16–18 Nov** (1.24% → 0.54%). Brand Shopping was normal. PL had a similar pre-BF dip in 2025, which recovered.
- **PL_SEARCH_GENERIC:** tROAS 70% (raised from 60% by Huel on 16 Nov), €440 budget, **uncapped** (0% budget-lost, about 80% rank-lost).
- **Competitors ad group:**

  | | Aug | Sep | Oct | Nov 1–18 |
  |---|---|---|---|---|
  | Spend | €1,464 | €1,345 | €679 | €452 |
  | Conversions | 18.9 | 9.0 | 7.1 | 2.0 |
  | CPA | €77 | €149 | €96 | €226 |

  - Aug–Nov overall: €106 per conversion, the same as the campaign (€105).
  - Quality Score is 1 on every competitor-brand keyword, and 3 on the "liofilizowane" generics.
  - KFD exact is 61% of its spend, at €122 per conversion.
- **"posiłek w proszku" (broad):** €348 for 0 conversions.
- **"białko roślinne" (broad):** €103 CPA over 16 weeks. The broad expansions are its cheaper 85%.
- **Brand:**
  - On Target IS (75%, €0.50 cap). "huel" exact costs €0.02.
  - IS fell from 86% to 71–80% and rank-lost IS rose. That may mean a new competitor on brand; check auction insights in the UI.
  - The €46 budget would hit its monthly limit.

**Where the discussion stands**
- **Pause the Competitors ad group: the user's instruction** (CPA double the campaign, QS 1).
  - My counterpoint: the campaign is uncapped, so pausing removes about €750 and about 3 conversions a month rather than moving the spend.
  - If paused, move the "liofilizowane" generic keywords to Outdoor first.
- **Proposed:**
  - Pause "posiłek w proszku".
  - Keep tROAS at 70%.
  - Get the NC tag firing on pl.huel.com.
  - Raise the brand budget ceiling to about €80, because of the monthly limit.
- **The brand switch to Manual CPC wasn't proposed,** but it's open given the user's preference. The potential saving is small: about €60 a week at most.
- **Not proposed:** moving money to Meta (same CAC as Shopping; cheap only at low spend) or phrase match on "białko roślinne".

## 7. Sweden

- **Not analysed yet.** Needs Fospha screenshots: Channel Weekly, Google non-brand, and Google brand.
- **Platform signals only:**
  - SE Shopping loses about 23% of IS to budget (€300/day), and its tROAS was raised from 80% to 90% on 16 Nov.
  - SE brand loses about 14% to budget.
  - Non-brand CPA has risen every week, from €70 to €116.

## 8. Rest of Europe

**What the data shows**
- **Fospha 5-week CAC:**
  - PPC generic £168 (£197–200 in the last 2 weeks).
  - Shopping £104.
  - Brand £10.
  - Meta £159, 77% of spend.
  - TikTok £171.
- **Italy consolidation (3 Nov):**
  - IT_SEARCH_GENERIC (tCPA €110, €400, itself budget-capped) was paused. The ROE generic budget went from €750 to €1,150 the same day, then to €920 on 16 Nov.
  - ROE generic targets en/fr/es/nl only and has no Italian keywords.
  - Italy fell from about €2.7k for 13.6 NC a week to about €0.8k for 3.7 NC.
  - Combined Search went from €7.8k for 46 NC a week (€168 each) to €8.4k for 42 NC (€201 each).
  - Outside Italy, the raise bought +€2.3k a week for +5 NC: €325–446 per extra NC.
- **ROE_SEARCH_GENERIC** (Max Conversions, tCPA €100) **is budget-capped:** 11–58% budget-lost IS by week.
- **ROE generic ad groups, 5 Oct–18 Nov:**
  - Meal Replacement €161 per NC (61.9 NC).
  - Protein €164.
  - Competitors €258 (29.5 NC). Within it:
    - Bulk protein, ESN, Ag1, prepmymeal exact and factor meals: €2.75k for 4.5 NC.
    - jimmy joy: €1.3k for 9 NC.
    - yfood: €2.3k for 9 NC.
  - Greens €337.
  - Protein Bars €294.
- **Countries:**
  - Switzerland: 0 conversions in Oct–Nov.
  - Spain is volatile (Oct €151 per NC, Nov €335).
  - Ireland is best (€103).
- **ROE Shopping (tROAS 102%, uncapped):**
  - Realised ROAS has been 0.90–0.92, so CPC fell from €1.70 to €0.98 and spend fell from about €400 to about €200 a day.
  - Cost per NC was flat at €84–116 at every spend level.
  - CVR is intact, with no 16–18 Nov drop.
  - The earlier cut from 108% to 102% produced no lift, because realised ROAS stayed below it.
- **ROE brand (Manual CPC, €400):**
  - Spend has been pinned at €400 since 17 Nov (budget-lost IS 10/37/5%).
  - The monthly limit leaves €346 a day against €445 of demand, so it would stop serving around 28 Nov, during BFCM.
  - Brand brings in about 235–297 NC a week at about €12 each.

**Proposals, stress-tested with the reviewer, not signed off**
1. Raise the brand budget from €400 to €600, once. It's binding, and it would hit the monthly limit during BFCM.
2. Reactivate IT_SEARCH_GENERIC as it was, and exclude Italy from ROE generic.
3. Cut the ROE generic budget from €920 back to €750.
4. In ROE generic (capped), pause:
   - the 5 losing competitor keywords;
   - the Greens and Protein Bars ad groups;
   - Switzerland (exclude).
5. Lower ROE Shopping tROAS from 102% to 90%.
   - Kill-switch: 14-day cost per NC above €140 (by conversion date), or Fospha Shopping CAC above £130 for a week.
6. Fix the DK NC tag.

**Estimated effect:**
- Search plus Shopping: about +€0.6–1.4k a week for +12–20 NC.
- Brand: recovers about 40 NC a week.
- The remaining CPA overage sits with Meta.

## 9. UK

**What the data shows**
- **Fospha 4-week CAC:** Shopping £165, Search £175, Meta £161, Demand Gen £1,110. Without Demand Gen, non-brand CAC is about £170; with it, £215.
- **Capped campaigns:**
  - WEIGHT_LOSS (£1,343/day against £1,300).
  - GENERIC (£436 against £400).
- **Uncapped campaigns:** COMPETITORS and SHOPPING_GENERIC_CORE.
- **Weight Loss:**
  - After the 22 Oct loosening (82% → 75% tROAS), the extra NC cost about £115 each.
  - "Medical/trending" costs £180 per NC since 2 Nov, about 3.5 NC a week. The other ad groups run at £94–124.
- **Generic "Stockpiling":**
  - New on 2 Nov, and the largest NC source in the campaign since 9 Nov (20 NC in 10 days, £94–131 each).
  - Convenient Meals and Weight Gain run at £47–86.
- **Shopping core:**
  - £74–80 per NC at £16–21k a week, but £106 at £28k a week.
  - Huel's tightening (Shopping 85%, Search Generic 110%, Meal Replacement 80%) stays.
- **Brand Shopping (Manual CPC):** about 24% of spend goes on non-brand terms ("freeze dried meals", "foods to stockpile", "morrisons") at an £83 CPA, against £6 for "huel" terms. 41% of IS is lost to rank.
- **Demand Gen:**
  - Restructured on 5 Oct, which coincided with platform ROAS falling from about 1.9 to about 0.6 and a −28% drop in brand demand.
  - Only 83 click NC.
  - No customer-acquisition goal is set.
  - "Parents" and "Female Focused" spent £194 for 0 conversions.
- **Monthly limits:**
  - UK Generic would throttle around 28 Nov at £400.
  - Weight Loss would throttle around 29–30 Nov at its current rate.

**Where the discussion stands**
- **Keep Stockpiling.** My earlier pause was reversed after the volumes check.
- **Proposed:**
  - Raise the UK Generic budget from £400 to £450 (monthly limit).
  - Weight Loss: pause Medical/trending (small win, about +2–3 NC a week) and revert tROAS from 75% to 82%.
  - Brand Shopping: add non-brand negatives, then test +20% CPC on brand terms only.
  - Demand Gen:
    - Switch to new-customers-only (after BFCM, 2 Dec).
    - Remove the 2 dead ad groups.
    - Run a Conversion Lift study.
    - Get Huel and Fospha to report Demand Gen separately from non-brand.
- **Withdrawn:**
  - Pausing Competitors ad groups, Shopping product exclusions, and informational/GLP-1 negatives (all uncapped).
  - Extra generic spend (both campaigns are past their efficient level).

## 10. BFCM (27–30 Nov) context

- **2025 reference:**
  - DE brand conversions +55%, brand CVR +36%, Shopping CVR +21%.
  - DE generic CVR barely moved.
  - PL Shopping −16%.
  - DE BF-week AOV was normal (€69.5); DE brand AOV was +7%.
- **Ideas discussed:**
  - Promotion assets and countdowns scheduled for the 4 days.
  - Feed `sale_price` with `sale_price_effective_date`, so prices don't mismatch.
  - Re-add "huel black friday" exact on brand.
  - Set brand ceilings once.
  - On tROAS campaigns, scale the target by the BFCM AOV ratio (not the discount %), in two steps, and revert 1 Dec.
  - No CVR seasonality adjustment.
  - Pause CPA kill-switches during BFCM, but keep spend alerts and a daily tag-vs-GA4 check (normal ranges: DE 0.75–0.85, PL 0.84–0.90).
  - Read results on 7 Dec.
- **Missing input:** BFCM offer depth per market.

## 11. Open questions and data requests

1. BFCM offer depth per market (DE, PL, SE, ROE, UK).
2. Fospha Demand Gen DDA+ NC by month, Aug–Nov (UK).
3. GA4 deciding test: DE all-channel purchases vs backend orders, Jul vs Aug, plus GA4 change history.
4. Sweden screenshots: Channel Weekly, Google non-brand, Google brand.
5. Why IT_SEARCH_GENERIC was paused on 3 Nov: was there a reason beyond consolidation?
6. Cause of the 16–18 Nov generic Shopping CVR drop in DE and PL (ecom/CRO).
7. Auction insights (UI only) for DE and PL brand.
8. NC tag fixes: PL (not firing) and DK (0 NC).

## 12. Lessons from corrections in this thread

- **Check volumes, launch date and weekly trend before calling something a pause.** UK Stockpiling was a new ad group that became the top NC source.
- **A bad 4-week CPA can be noise.** Check the longer window (PL Competitors: €228 over 4 weeks, €106 over Aug–Nov).
- **Don't over-index on Black Friday.** Huel runs exactly 4 days.
- **Don't build targets from circular maths.** The DE £100 CAC par was circular.
- **Check that the platform's NC tag actually fires before using it** (PL, DK).
- **Reviewers make errors too. Verify disputed claims yourself.**
  - "DE funnel tags unusable" came from misreading PL rows.
  - "ROE generic also dropped" was false.
  - "No video in May" was wrong: £45k of YouTube Reach ran.
