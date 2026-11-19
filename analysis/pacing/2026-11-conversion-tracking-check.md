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

## Actions
1. **Run the deciding test.** Did DE backend orders (Shopify or Fospha total new customers) rise about 32% from July to August?
   - If not, GA4 is over-crediting, and we keep optimising to the Ads tag.
   - If they did, the Ads tag is missing purchases and needs fixing before Black Friday.
2. **Find out what changed in GA4 in early August**, for example attribution or channel credit settings, or modelling.
3. **Do NOT switch the primary conversion to GA4 before Black Friday.** Adding GA4 as a second primary would double-count, and swapping it in would loosen bidding abruptly, 8 days before Black Friday.
4. **Remove "Transactions DK (All Web Site Data)", a dead Universal Analytics action, from the primary conversions.**
5. **Check how many purchases fall back to the default conversion value** (DE €62, PL €265, SE €50, EU €1).

## Later, after Black Friday
**"New customer Purchases"** (since Oct, 7-day window) covers about 43% of tag purchases. New and existing customer purchases add up to only about 76% of tag purchases, so audit that action before using it, or Google's new-customer goal, for bidding.
