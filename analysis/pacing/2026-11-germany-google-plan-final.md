# Germany Google Ads: final plan (19 Nov 2026)

Account Huel EU (8046071519), EUR; Fospha figures in GBP. Every action is tied to the account's own history. Each one was drafted from the data and then challenged by a second reviewer working from the same data.

**Context**
- Germany is 252 new customers behind target (88%), and CPA is 107% of target.
- The Google changes below recover a modest part of that gap. The gap is mainly a Meta question (75% of German spend, at £119 per Fospha new customer over the last 7 days).

## Actions we are taking

1. **DE_SHOPPING_STANDARD_GENERIC: lower tROAS from 108% to 95%. On hold until 21 Nov** (update 19 Nov, from the Poland review).
   - **Why the hold:** by conversion date, DE generic Shopping fell from 8.8 to 3.6 conversions a day on 16–18 Nov (conversion rate 1.9% → 1.0%). PL shows the same drop, while brand Shopping is normal. Lowering the target now would buy clicks at that conversion rate.
   - Diagnose first: Merchant Center, Black Week pre-announcement, product pages. If conversion rate is back to normal by 21 Nov, apply 95% so it's in place before Black Friday.
   - **Why:** in the week of 9 Nov, value per click fell 35%. Conversion rate went from 2.25% to 1.71%, and AOV fell from €73 to €62, a 13-month low against a median of €71. ROAS dropped from 1.07 to 0.89, under target, so Google cut CPC 23%. Spend fell 41% and conversions 42%.
   - **CPA held at €69–70**, below the 58-week median of €72.5. Fospha Shopping new customers fell from 55 to 40 a week, while CAC went from £102 to £82.
   - **Expect a modest lift, not a return to €900 a day.** The ROE Shopping cut from 108% to 102% (30 Oct) produced no measurable spend increase.

2. **Shopping guardrail. Revert to 108% if any of these happens:**
   - 2 consecutive weeks of CPA above €80.
   - 1 week of CPA above €90.
   - Fospha Shopping CAC above £105.

   Read from the week of 23 Nov, on data at least 3 days old.
   - **Why:** €80 alone is breached in 11 of 58 normal weeks. €90 happened in only 3 of 58. £105 caps the marginal Fospha CAC at about £210.

3. **Merchant Center: check stock, price and disapprovals on Daily Greens (`gre-ori-20r-edp`).**
   - **Why:** it got 0 conversions on 89 clicks in 2 weeks. At its usual 5.3% conversion rate, that has about a 1% chance.

4. **Investigate the Shopping conversion-rate drop.** Check landing pages, prices and stock on the top 4 SKUs around 8–10 Nov.
   - **Why:** conversion rate fell 24%. Lowering tROAS restores bids but doesn't fix conversion rate.

5. **DE_SEARCH_BRAND: add exact-match keywords "huel black friday", "huel de" and "huel rabattcode" at €0.35, before step 6.**
   - **Why:** they currently match through the broad ad group. "huel de" had 74 clicks and 8 conversions. Exact match gives them a controlled bid over Black Friday.

6. **DE_SEARCH_BRAND: switch from Max Conversions to Manual CPC, with enhanced CPC off.** Max CPC: "huel" exact **€0.35**, product exacts **€0.50**, Huel (Broad) **€0.30**.
   - **Why:** controlling for weekday, each extra €1 a day bought about 0 extra clicks and about 0 extra conversions. Higher spend only raised CPC: €0.31 on days above €155, against €0.26 on other days.
   - **"huel" exact already has** 93% IS and 84% absolute-top IS at €0.29.
   - **Why these bid levels:** only 8 of 110 days averaged above €0.35 on "huel". Black edition already averages €0.38, so products need €0.50.
   - **Expect CPC about flat.** The gain is control.

7. **Brand budget becomes a ceiling: €180 now, €250 for 24 Nov–1 Dec, €180 from 2 Dec.**
   - **Why:** manual bidding doesn't spend budget it doesn't need. In Black Friday week 2025, brand conversions rose 55% while 17% of IS was lost to budget. The ceiling makes room for that demand without CPC inflation.

8. **Brand monitoring: daily, and twice a day from 26 Nov to 1 Dec.**
   - Keep absolute-top IS on "huel" exact (and "huel black friday") at 80% or above. If it drops, raise the bid by €0.03.
   - Check auction insights in the UI.
   - **Why:** under manual bidding nothing reacts automatically if a competitor starts bidding on "huel". IS data arrives about a day late.

9. **Find out what capped brand spend at exactly €99 on 13–14 Nov.**
   - **Why:** change history shows no budget change, and an unexplained cap would also limit the new setup.

10. **Search generic: scan the non-competitor ad groups monthly for competitor names, and add phrase-match negatives.**
    - **Why:** the 19 negatives added on 11 Nov are exact match, and the keywords are broad. The prepmymeal leak into Ready Meals cost €668 for 1.3 conversions before they were added.

## Actions we are not taking

11. **No change to DE_SEARCH_GENERIC tROAS (100%) or budget (€700).**
    - **Why:** Search costs £128 per Fospha new customer against £97 for Shopping, so Shopping is the better home for extra money. The budget isn't limiting spend (0% lost to budget). If the Shopping increase needs to be CAC-neutral, trim Search first.

12. **No campaign-level competitor negatives.**
    - **Why:** the competitor ad groups and ad-group negatives work. The leak stopped on 11 Nov.

13. **No negatives for the remaining stray terms** (frosta, every, meal prep, tactical).
    - **Why:** each has spent less than 1.5 CPAs. That's not enough data to justify a decision.

14. **No pausing of competitor keywords** (youcook €77, jimmy joy €102).
    - **Why:** each has spent less than 1–2 CPAs.

15. **No Shopping product exclusions.**
    - **Why, Spicy Chick'n noodles:** its €89 CPA is inside its 10-week range of €40–89.
    - **Why, trial pack:** its CPA improved from €102 to €80, and it is likely a key product for new customers.
    - **Why, Daily Greens:** Google has already cut it to about €10 a day while the Merchant Center check runs.

16. **No smaller tROAS step (100%).**
    - **Why:** it doesn't offset the 15% AOV fall that caused the throttle.

17. **No Black Friday tROAS cut on Shopping.**
    - **Why:** AOV in Black Friday week 2025 was €69.5, in line with the weeks around it. Revisit only if Germany runs a deeper discount this year.

18. **No Shopping budget change.**
    - **Why:** 0% IS lost to budget, so the budget isn't what's limiting spend.

19. **No Target Impression Share on brand.**
    - **Why:** the budget was the limit, not the bid strategy, and Target IS pushes CPC up.

20. **No brand budget raise under Max Conversions.** This withdraws an earlier recommendation.
    - **Why:** extra spend under Max Conversions bought about 0 extra clicks.

21. **No ad-schedule bid adjustments on brand.**
    - **Why:** absolute-top IS is flat across the day (0.57–0.62 from 6h to 23h). The higher evening conversion rate comes from who is searching, not ad position.

22. **No Black Friday seasonality adjustment on the generic campaigns.**
    - **Why:** the generic conversion rate barely moved in Black Friday week 2025.

23. **No restoring Search generic budget to €1,000.**
    - **Why:** the budget isn't limiting spend.

## Open decision for Huel
Volume or CAC for the rest of November? Most of these changes improve one at the expense of the other. The brand switch costs about nothing either way.

---

## v4 update (19 Nov, late): replaces items 1–9 above where they conflict

1. **Why generic Shopping stopped converting:** most likely pre-Black Friday deal-waiting, not a fault.
   - **Evidence:** shoppers still start checkout but don't finish. PL generic Shopping purchase/checkout fell from 37% to 18%, but PL brand Shopping, on the same checkout, was normal (33–38%). DE brand Search was also normal (60% → 58%).
   - **Precedent:** PL had the same pre-Black Friday dip in 2025, when the Shopping conversion rate in the week of 10 Nov 2025 was about half the week before, then recovered.
   - **Action:** ask ecom whether a Black Week teaser, banner or price communication went live on DE/PL on 15–16 Nov.
2. **DE Shopping tROAS: 108% → 95% on Wed 26 Nov.** That lands the extra bids on Black Friday demand, not deal-waiting week.
   - **Kill-switch:** revert to 108% if CPA, using purchases by conversion date, is above €90 on 2 consecutive days.
   - **Review:** 3 Dec.
3. **Brand: Manual CPC** (huel exact €0.35, products €0.50, broad €0.30). Add exact-match keywords "huel black friday", "huel de" and "huel rabattcode" at €0.35.
4. **Brand budget: fixed at €250 as a safety ceiling, not touched again.**
   - **Why €250:** about 540 clicks a day, ×1.18 for the 2025 Black Friday click lift, at ~€0.30 CPC, comes to about €190, which leaves headroom.
5. **Brand automated rules:**
   - **A (daily, yesterday):** exact keywords with impressions > 20 and abs-top IS < 80%: raise max CPC by €0.03, capped at €0.50.
   - **B (daily, last 3 days):** abs-top IS > 95% and average CPC > €0.30: lower max CPC by €0.02, floor €0.25.
   - **C:** email if yesterday's cost > €220 or average CPC > €0.45.
6. **€99 on 13–14 Nov: answered.** There were no changes in the account, spend was spread across every hour, impressions were lower all day, and 15 Nov then spent €188. That's Google's pacing under Max Conversions, and it becomes moot once the campaign is on Manual CPC.
7. **Search generic:** run a monthly scan for competitor names and add them as phrase negatives.
8. **Merchant Center (Daily Greens):** dropped for now; no access yet.
