# Paid apps abroad → gaps in the Swiss App Store

*Research date: 30 October 2026*

**Question:** Which apps that earn money from a subscription or one-time purchase in the US or Asia are missing (or useless) in Switzerland, and which one is most worth adapting for CH by a two-person team (you plus an AI coding partner)?

**Short answer:** Build a **Speak-style AI speaking coach for the Swiss *fide* language test** (German first, then French and Italian). Runner-up: a **Taxfix-style mobile tax return** for Switzerland (bigger market, much harder). The Rocket Money / Copilot idea is real, but Swiss start-ups launched into that gap in late 2025.

---

## 1. Method and limits

1. I listed paid apps from the US, Japan and Korea that are commercially proven (revenue, paying users or valuation on record).
2. For each one I checked whether it **works in Switzerland**. That means more than being downloadable: it has to support Swiss banks, Swiss tax law, Swiss languages and Swiss exams.
3. I scored the apps that have a Swiss gap on market size, willingness to pay, competition, build effort for two people, and regulatory risk.

**Limitation:** this cloud session could not reach Apple's lookup API (`itunes.apple.com`), the Swiss App Store pages (`apps.apple.com`), `fide-info.ch` or `forum.mustachianpost.com`. So the Swiss-availability verdicts below come from the providers' own help pages, third-party sources and Swiss App Store listings that showed up in search. They are **inferred, not confirmed with Apple's data**. Before committing, run the check in section 7.

---

## 2. Candidate apps and Swiss availability

| App (origin) | Business model | Proof it works | Usable in CH? | Swiss alternatives found |
|---|---|---|---|---|
| **Rocket Money** (US) | Subscription: budgeting, subscription cancelling, bill negotiation | Large US PFM app | **No.** US users and US banks only | **Liquid** (CHF 7/mo or CHF 70/yr, launched Nov 2025, bLink bank sync and subscription check), **BlueBudget**, BudgetCH (free) |
| **Copilot Money** / **Monarch** (US) | Subscription PFM | Popular US budgeting apps | **No.** Copilot's FAQ says US-based accounts only, and Monarch is US-centric | Same as above |
| **Money Forward ME** (JP) | Freemium plus premium subscription (household budget, account aggregation) | 18.1M users, **640k paying** subscribers | **No.** Japan only (Japanese banks) | Liquid, BlueBudget, banks' own e-banking (UBS, ZKB, PostFinance, LUKB now show other banks via bLink) |
| **Taxfix** (DE, also IT/ES) | Pay-per-return mobile tax filing | Market leader in Germany | **Downloadable but useless.** Covers German tax only, and Swiss users ask for CH in reviews | TaxWize (CHF 39, ZH and AG only), Taxea (from CHF 99), Steuermacher (CHF 99, human-assisted), free cantonal software. Taxly (CHF 49) reportedly **ceased operations** |
| **Speak** (US/KR) | AI speaking tutor, about USD 20/month | **USD 100M+ annualised revenue**, USD 1B valuation | **Available, but no German.** It teaches English, Korean, Spanish, Japanese, French and Italian, and has no Swiss exam focus | FidePrep (web: free exercises, mock exams), Praktika (generic AI German), Pimsleur Swiss German. **No AI speaking coach for fide found** |
| **Asken** (JP) | Diet app with dietitian-style AI feedback, premium subscription | 14M members, #1 diet app in Japan (company figures) | **Japan-focused.** Its US/Canada launch did not scale | Yazio, MyFitnessPal, Cal AI are all available. **No gap** |
| **Pawp** (US) | Pet telehealth subscription | US, all 50 states, Walmart+ partner | **No.** US only | Unclear. It needs Swiss-licensed vets and has veterinary-law questions |
| **Huckleberry** (US) | Baby-sleep subscription (USD 9.99–14.99/mo) | 5M+ families, 179 countries | **Available, but English only** | Localisation gap only, not a market gap |

---

## 3. Shortlist scoring (1 = poor, 5 = great)

| Opportunity | Demand / willingness to pay | Competition in CH | Build effort for 2 people | Regulatory / liability risk | Time to first revenue | **Total** |
|---|---|---|---|---|---|---|
| **A. fide AI speaking coach** (Speak model) | 4 (mandatory, high-stakes exam) | 5 (no AI speaking product found) | 4 (LLM + speech APIs) | 5 (education, no licence) | 5 (weeks) | **23** |
| **B. Swiss mobile tax return** (Taxfix model) | 5 (millions of returns, fiduciaries charge CHF 280–400) | 3 (fragmented small players, free cantonal tools) | 2 (26 cantonal rule sets, e-filing formats) | 2 (errors cost users money) | 2 (seasonal, one canton at a time) | **14** |
| **C. Swiss PFM / subscription killer** (Rocket Money model) | 3 | 2 (Liquid and BlueBudget already live on bLink, banks adding multibanking) | 2 (bLink onboarding, security audits) | 2 (bank data, FINMA/FADP questions) | 2 | **11** |
| D. Pet telehealth (Pawp model) | 3 | 4 | 2 (needs vets) | 2 | 2 | 13 |
| E. Localised baby app (Huckleberry model) | 3 | 3 | 3 | 3 (health claims) | 3 | 15 |

---

## 4. Recommendation: "fide Coach", an AI speaking examiner for Switzerland

### Why this one
- **Proven model abroad.** Speak shows that people pay about USD 20/month to *talk* to an AI tutor (USD 100M+ annualised revenue). It does not offer German, and no app targets the Swiss fide format.
- **Demand is forced, dated and high-stakes.** Swiss naturalisation requires proof of the local language (generally **B1 spoken, A2 written**; some cantons, such as Zurich, run their own test). Permit applications such as the C permit also have language requirements. People must pass by a deadline, so they pay.
- **Steady flow of customers.** About **41,000 people were naturalised in 2025**, and Zurich alone issued 11,100 passports. Native speakers of German, French or Italian, and people who went to school in a national language for 5+ years, are exempt. That still leaves many thousands of test-takers each year, plus permit applicants. The fide statistical reports show participants from 65 nationalities in 2024, with **76% taking the test in German**.
- **Small competitive set.** FidePrep offers static web exercises. Generic apps (Duolingo, Praktika) don't simulate the fide oral exam, its everyday Swiss scenarios (Gemeinde, landlord, doctor, school) or its scoring.
- **Ideal for two people plus AI.** No licence, no bank integration, no tax liability. The core is an LLM examiner plus speech-to-text and text-to-speech, which can be prototyped in days.

### Honest size check
This is a solid niche business, not a unicorn. **Illustrative assumption, not data:** 15,000–30,000 relevant learners a year × 10–15% paying × CHF 49–79 comes to roughly **CHF 75k–350k a year B2C**. Upside comes from:
- **B2B licences** for language schools, cantonal integration offices and employers with migrant workforces.
- **French and Italian versions** (the same engine with new content).
- **Swiss German listening module** for everyday life, as a natural upsell.
- **Civics knowledge prep.** Naturalisation also tests local and Swiss knowledge, and "Einbürgerung Schweiz" quiz apps already show demand.

### Monetisation
- **"Exam Pass": CHF 49–59 one-time purchase for 3 months.** This matches how people prepare and avoids subscription fatigue.
- **Monthly CHF 19.90** for longer learners.
- **School/organisation seats** billed per learner.

### MVP (about 4–6 weeks)
1. **Oral mock exam.** The AI plays the examiner on fide-style everyday topics (housing, work, health, school, authorities), with voice in and voice out.
2. **Feedback.** An estimated level (A1 / A2 / B1) per criterion, corrected sentences and useful phrases.
3. **Written mini-tasks.** Short A2 texts such as a message to a landlord or a form, with instant correction.
4. **Interface languages:** English, Portuguese, Albanian, Turkish, Ukrainian, Arabic, Tigrinya and Spanish (the largest non-exempt groups).
5. **Stack:** React Native or Swift app; a hosted LLM API for the examiner; speech-to-text and text-to-speech APIs; RevenueCat or StoreKit for payments; data hosted in CH or the EU for FADP compliance.

### Risks and mitigations
| Risk | Mitigation |
|---|---|
| Overclaiming ("guaranteed pass"), or trademark issues with the name "fide" (SEM-run programme) | Describe it as practice "for the fide test" without a pass guarantee. Avoid official logos. Check naming before launch |
| LLM grading errors | Calibrate against official fide sample tasks and level descriptors. Have a certified fide trainer review the prompts |
| Small market | Add B2B seats, then FR/IT, then Swiss German |
| Voice data privacy | Don't store audio by default. Swiss or EU hosting. Clear FADP privacy notice |

---

## 5. Runner-up: Taxfix-style Swiss tax return

Bigger prize (every adult files, and fiduciaries charge CHF 280–400), with proven willingness to pay CHF 39–99 per return. But it requires canton-by-canton rules and formats, carries real liability, and earns most of its revenue in a short season. **Taxly**, backed by Helvetia, launched at CHF 49 in four cantons and reportedly ceased operations. **TaxWize** covers only ZH and AG. Viable later, starting with one canton (Zurich) and simple employee returns. It is too heavy as a first project.

## 6. Why not Rocket Money for CH (yet)

The enabler arrived on **25 Nov 2025**: SIX bLink **multibanking for private customers**, with 8 banks and 2 fintechs at launch and 30+ banks providing interfaces. But **Liquid** (21 banks connected, CHF 7/month) and **BlueBudget** took that slot immediately, and the banks are adding multibanking to their own e-banking. Becoming a bLink third-party provider also takes contracts and security reviews.

---

## 7. Next steps

1. **Confirm Swiss availability** with Apple data once `itunes.apple.com` is allowed (or on a laptop):
   `https://itunes.apple.com/search?term=fide&country=ch&entity=software`
   and search the Swiss App Store for "fide", "Einbürgerung" and "Deutsch Prüfung".
2. **Get real volumes** from the fide statistical report 2024 (fide-admin.ch) and SEM permit statistics. Replace the size assumption in section 4.
3. **Validate demand in a week.** A landing page plus posts in Swiss expat groups (r/Switzerland, English Forum, Facebook groups) offering a free AI mock exam, measuring sign-ups.
4. **Build the oral mock-exam prototype** (German, A2/B1) and test it with 10 real candidates.

---

## Sources

- Rocket Money US-only: [Truebill help center](https://help.truebill.com/articles/79778-does-truebill-support-international-banks), [Mustachian Post forum thread](https://forum.mustachianpost.com/t/something-like-rocket-money-in-switzerland/10395)
- Copilot / Monarch coverage: [Copilot FAQ](https://www.copilot.money/faq), [Freenance comparison](https://freenance.io/comparisons/freenance-vs-monarch-money-2026-comparison-eu-pl-features-pricing-which-pfm/)
- Money Forward ME paying users: [Money Forward news (2026)](https://aeo.washinmura.jp/ai/corp-moneyforward-com/en/news/2026-04-24-money-forward-me-premium-members-prime-c), [Techleap profile](https://finder.techleap.nl/companies/money_forward)
- Speak revenue, valuation and languages: [Benzinga](https://www.benzinga.com/news/topics/25/11/48975908/this-1-billion-ai-startup-backed-by-openai-khosla-ventures-just-hit-100m-revenue-racing-to-beat-duolingo), [TechCrunch](https://techcrunch.com/2024/06/20/language-learning-app-speak-nets-20m-doubles-valuation/), [Dataconomy](https://dataconomy.com/2024/12/10/speak-raises-78m-at-a-1b-valuation)
- Asken: [Company news (2026)](https://aeo.washinmura.jp/ai/asken-inc/en/news/2026-06-15-%E3%81%82%E3%81%99%E3%81%91%E3%82%93-%E9%A3%9F%E4%BA%8B%E7%9B%B8%E8%AB%87%E3%83%81%E3%83%A3%E3%83%83%E3%83%88%E6%A9%9F%E8%83%BD-ai%E3%81%93%E3%82%93%E3%81%A0%E3%81%A6%E6%8F%90%E6%A1%88-%CE%B2%E7%89%88-%E3%81%AE%E5%85%88%E8%A1%8C%E4%BD%93%E9%A8%93%E3%82%92%E9%96%8B%E5%A7%8B-%E6%9C%AA%E6%9D%A5%E3%81%95), [Business Wire (Canada launch)](https://www.businesswire.com/news/home/20161202005182/en/Asken-Diet-Launches-in-Canada-After-Reaching-1-Million-Users-in-Japan), [Statista](https://statista.com/statistics/1227947/japan-leading-weight-control-applications-by-revenue)
- Pawp: [NerdWallet review](https://nerdwallet.com/p/reviews/insurance/pawp-pet-insurance), [Walmart press release](https://corporate.walmart.com/news/2024/05/22/walmart-plus-and-pawp-team-up-to-unleash-24-7-pet-telehealth-benefit)
- Huckleberry: [US App Store listing](https://apps.apple.com/us/app/huckleberry-baby-child/id1169136078), [Series A release](https://www.vcaonline.com/news/2021110411/huckleberry-raises-12-5-million-series-a-to-bring-customized-data-driven-pediatric-expertise-to-every-family)
- Swiss multibanking (bLink): [SIX media release](https://www.six-group.com/en/newsroom/media-releases/2025/20251125-multibanking-launch.html), [SIX multibanking page](https://blink.six-group.com/en/multibanking), [PostFinance](https://www.postfinance.ch/en/about-us/media/newsroom/postfinance-launches-multibanking-for-private-customers.html), [blue News](https://www.bluewin.ch/en/news/banks-introduce-multibanking-for-private-clients-via-six-platform-2980031.html)
- Liquid and BlueBudget: [Liquid on the Swiss App Store](https://apps.apple.com/ch/app/liquid-app/id6742995389), [Liquid on bLink](https://blink.six-group.com/en/about/customer-stories/liquid), [Netzwoche](https://www.netzwoche.ch/news/2026-08-26/liquid), [GRS foundation](https://www.grstiftung.ch/en/funding/portfolio~grs-007-25~.html), [BlueBudget on bLink](https://blink.six-group.com/en/about/customer-stories/bluebudget)
- Swiss tax market: [TaxWize](https://taxwize.ch/), [Taxea](https://www.taxea.ch/en/faq-taxes/can-i-file-my-tax-return-online-in-switzerland), [Steuermacher](https://steuermacher.ch/en), [Helvetia on Taxly](https://www.helvetia.com/ch/web/en/about-us/news/media-releases/2021/20210209.html), [Dealroom on Taxly](https://app.dealroom.co/companies/taxly), [Suter Treuhand price list](https://sutertreuhand.ch/files/formulare/preisesteuern.pdf), [Taxfix reviews from Swiss users](https://apptail.io/de/app/taxfix-online-steuererklarung-fsk/switzerland)
- fide and naturalisation: [iamexpat: 2025 naturalisations](https://www.iamexpat.ch/expat-info/swiss-news/which-internationals-got-swiss-passport-2025), [Le News: language requirements](https://lenews.ch/2023/05/27/language-requirements-for-swiss-citizenship-and-visas-what-you-need-to-know/), [fide statistical report 2024](https://fide-admin.ch/doc/4657/FR_Statistischer_Bericht_Sprachnachweisverfahren_2024.pdf), [Graubünden language proof page](https://hallo.gr.ch/en/sprache_integration/nachweise/Seiten/nachweise.aspx?isdlg=1), [FidePrep](https://www.expat.com/en/business/140108_fide-prep-ch.html), [Berlitz fide page](https://www.berlitz.com/en-ch/preparation-exams/fide)
- Swiss German apps: [Pimsleur Swiss German](https://www.pimsleur.com/learn-swiss-german), [LanguageFast Swiss German](https://apps.apple.com/us/app/-/id6754994883)
- Market context: [RevenueCat State of Subscription Apps](https://revenuecat.com/state-of-subscription-apps/), [App Radar US top grossing](https://appradar.com/blog/top-grossing-apps-app-store)
