# Conversion tracking check: Google Ads tag vs GA4 (19 Nov 2026)

Account Huel EU (8046071519). Reviewed with a second Opus reviewer working from the same data.

## Findings
1. **The gap is real, and it started in August 2026.**
   - DE tag/GA4 was 1.01–1.25 through July, then about 0.75 from August. PL went from 0.94–1.08 to about 0.84.
   - In 2–15 Nov the gap is the same for DE generic and brand Shopping (0.80 and 0.82).
2. **The likely cause is a change on the GA4 side, not the tag losing purchases.**
   - From July to August, GA4 rose in all four markets in the same month: DE +32%, PL +24%, SE +37%, ROE +36%.
   - The Ads tags stayed flat or rose: DE +1%, PL +8%, SE +26%, ROE +8%.
   - Four separate GA4 properties moving together points to a GA4-side change.
   - AOV is the same in both (DE €77.7 tag vs €79.2 GA4). ROE runs the other way (tag 1.3–2.4× GA4).
   - The windows also differ: the Ads tags credit purchases up to 7 days after a click, and the GA4 imports allow 30.
3. **The bidding signal hasn't changed.** The tag Smart Bidding uses did not drop in August, so bids are calibrated as before. My earlier claim that the account had become "about 81–86% effective tROAS" was wrong; I had the maths backwards too.
4. **The 16–18 Nov generic Shopping drop is real and isn't a tracking fault.**
   - GA4 shows it independently: PL 9.2 → 2.7 purchases a day, DE 10.2 → 2.7 (by conversion date).
   - On the same days, brand Shopping is normal in PL, and account-level new-customer purchases show no collapse (86, 62, 67 a day against 63–112 over 9–15 Nov).

## Deciding test: result (Fospha Channel Monthly, DE, received 19 Nov)
- **Fospha DE new customers, Jul → Aug:** total 4,278 → 4,442 (+4%). Paid Search 1,697 → 1,757 (+3.5%). Paid Search visits 33K → 32K.
- **Same period:** Ads tag 3,198 → 3,223 (+1%). GA4 import 3,171 → 4,199 (+32%).
- **Conclusion:** actual orders didn't rise about 30%, so the tag didn't start missing purchases. Since August, GA4 credits more purchases to Google Ads. It counts each order once but attributes more of them to Google Ads, perhaps through a window, attribution or channel-credit change.
- **Keep optimising to the Ads tag.**
- **Caveat:** Fospha counts new customers only. A roughly 30% jump in existing-customer purchases would be needed to change this conclusion, and the tag, which also fires on existing-customer purchases, shows no such jump.

## Revised reading (after the user's challenge, reviewed again)
GA4 isn't inventing orders. The Fospha test above only rules out real order growth. It doesn't show which system is right.

**What the data shows**
- The DE jump from Jul to Aug is in same-day purchases: GA4's "<1 day" bucket went from 2,605 to 3,645. The 7–30 day buckets are flat, so the 30-day window doesn't explain it.
- It's uniform across campaigns, roughly +25–36% for GA4 against a flat tag:
  - Brand Search: GA4 2,035→2,767, tag 2,034→2,134.
  - Generic Shopping: GA4 331→445, tag 353→351.
- It's uniform across devices: GA4÷tag went from 1.17 to 1.54 on desktop and from 0.94 to 1.24 on mobile. So it isn't a Safari or iOS issue.
- DE Google clicks fell 4%.

**Two explanations remain**
- **(a) GA4 now *sees* Google-driven purchases the tag misses.** This could follow a consent or measurement change, or GA4 could be double-firing. If GA4 is right, the tag has under-counted since August.
- **(b) GA4 now *credits* Google Ads with orders it used to give organic or direct.** This could come from a conversion-credit or attribution setting change. In that case the tag is the better count.

Google Ads data alone can't separate (a) from (b).

## Actions
1. **Deciding test, in GA4 itself:** compare DE all-channel purchases with backend orders for July against August.
   - If GA4's total rose by about 1,000 while backend orders rose only about 4%, it's (a) or double-firing.
   - If GA4's total is flat and only the Google Ads share rose, with organic or direct down by about 1,000, it's (b), and the tag is the better count.
   - Also check GA4 Admin change history on all four EU properties for early August: attribution settings, conversion-credit channels and consent settings. Check for any consent-banner change on the sites too.
2. **Find out what changed in GA4 in early August**, for example attribution or channel credit settings, or modelling.
3. **Do NOT switch the primary conversion to GA4 before Black Friday.** Adding GA4 as a second primary would double-count, and swapping it in would loosen bidding abruptly, 8 days before Black Friday.
4. **Remove "Transactions DK (All Web Site Data)", a dead Universal Analytics action, from the primary conversions.**
5. **Check how many purchases fall back to the default conversion value** (DE €62, PL €265, SE €50, EU €1).

## Later, after Black Friday
**"New customer Purchases"** (since Oct, 7-day window) covers about 43% of tag purchases. New and existing customer purchases add up to only about 76% of tag purchases, so audit that action before using it, or Google's new-customer goal, for bidding.
