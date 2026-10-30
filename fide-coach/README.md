# Passbereit: German practice for Swiss citizenship (prototype)

A working prototype of the app recommended in [`market-analysis/swiss-app-opportunities.md`](../market-analysis/swiss-app-opportunities.md). An AI examiner helps people prepare the German needed for Swiss naturalisation (Einbürgerung), in the format of the **fide** test.

- Live prototype (private until shared): https://claude.ai/artifact/VoQCf6zm6DGuaRFw1p3Cz6
- App file: `sprechprobe.html` (the early working name, kept so the live link stays the same)
- Logo / app icon: `logo.svg`

## What it does

- **Goals:** Citizenship (B1 speaking, A2 writing; the federal minimum), C permit (A2 speaking, A1 writing) and Starting out (A1). Citizenship is the default.
- **Speaking test:** the AI examiner holds a fide-style conversation of up to 6 answers on an everyday Swiss topic, including a short role-play. The candidate types or dictates answers and can play the examiner's lines aloud.
- **Writing task:** a short message task at the goal's writing level, with three content points.
- **Feedback:** an estimated level against the target, 4 criteria scored out of 4, corrections with the changed words highlighted, useful phrases and a next step. Explanations come in 11 languages.
- **Canton picker:** all 26 cantons. For now every canton gets the Canton of Zürich civics questions, with a note that its own questions are coming; federal questions apply everywhere.
- **Civics quiz (Grundkenntnisse):** 10 random multiple-choice questions per round from a bank of 49 (federal, Canton of Zürich, municipality and daily life). Each answer comes with an explanation, and the AI can explain it again in the user's language. This works without the AI.
- **Mock naturalisation interview:** the AI plays a member of a Zurich municipality's naturalisation committee. It asks a personal question, civics questions drawn from the bank, and a question about local life, then grades each civics answer against the bank's facts along with the applicant's German.
- **History:** past sessions are saved on the device.

### Civics question bank

The questions are written for Passbereit, not copied from the canton's official list. They cover the topics of the Canton of Zürich knowledge test (Grundkenntnistest: 50 questions drawn from an official list of 350). Facts were checked against the federal and cantonal constitutions and zh.ch. Examples: Zurich has a 180-member Kantonsrat, 7 Regierungsrat members elected by the people, 6,000 signatures for a cantonal initiative and 3,000 for a referendum, and 12 districts. The interview AI may only ask about facts in the bank, so it cannot invent questions. Before launch, have a Zurich naturalisation officer or civics teacher review the bank, and add a "last checked" date.

## Name and logo

**Passbereit** means "passport-ready" in German. *Pass* is also the English "pass", as in passing the test. The name says what the user wants (the Swiss passport) without pretending to be an authority.

The logo is a white speech bubble with a check mark on a Swiss-red rounded square: speak, then pass. It uses Swiss red as a colour but **no Swiss cross, coat of arms or federal design**, for these reasons:

- The Swiss coat of arms (the cross in a shield) may not be used commercially, and the protection law (SR 232.21) forbids public signs used in a way that suggests a link with the Confederation. A citizenship app with a cross and an official look is exactly that case.
- The federal corporate design (the "Schweizerische Eidgenossenschaft" style) is reserved for the federal administration.
- Looking official while not being official is misleading advertising under the Unfair Competition Act (UWG). It is also how scam sites aimed at applicants look, and that destroys trust and store reviews.

The app states plainly that it is independent and not affiliated with the SEM, the fide programme or any canton.

## Store listing draft (App Store limits in brackets)

| Field | Text |
|---|---|
| App name (30) | `Passbereit: Einbürgerung CH` (27) |
| Subtitle (30) | `Deutsch B1 & fide Test üben` (27) |
| Keywords (100) | `einbürgerungstest,schweiz,sprachtest,staatsbürgerschaft,citizenship,swiss,passport,prüfung,mündlich` (99) |
| Promotional text | Bereit für die Einbürgerung? Üben Sie Sprechen (B1) und Schreiben (A2) mit einem KI-Prüfer – mit Niveau-Einschätzung und Korrekturen. |

Words that are already in the name and subtitle are left out of the keyword field, because Apple indexes them anyway.

**Website / Google**
- Title tag: `Einbürgerung Schweiz: Deutsch B1 & fide Test üben | Passbereit`
- Meta description: `Üben Sie für die Einbürgerung in der Schweiz: mündlich B1 und schriftlich A2 im Format des fide-Tests. KI-Prüfer, Niveau-Einschätzung und Korrekturen in Ihrer Sprache.`

Keyword sources: competitor app names ("Einbürgerungstest Code Schweiz", "Einbürgerung Schweiz – Pro", "Einbürgerungtest Schweiz 2026") and fide course pages. These are not measured search volumes. Before launch, check them with Google Keyword Planner / Google Trends (region: Switzerland) and with App Store search suggestions (type "Einbürgerung" and "fide" in the App Store on an iPhone).

**Gap to close:** searches for "Einbürgerungstest" mostly mean the **civics knowledge test**, not the language test. To win that traffic, add a civics module (Swiss, cantonal and municipal knowledge, by canton). Otherwise users who arrive from that keyword will be disappointed.

## How it runs

`sprechprobe.html` is a single-file page published as a Claude artifact. It reaches the model through the artifact runtime (`claude.use("sample")`). That means:

- there is no backend and no API key, and each viewer's own Claude account pays for the AI calls;
- it only works inside the Claude app or on claude.ai, and viewers must be signed in and allow the page to use Claude.

## Path to a store app

1. Validate with 10 to 20 real candidates: does the estimated level match their actual fide result?
2. Move the prompts to a small backend using the Claude API, adding real speech-to-text and text-to-speech and Swiss/EU hosting.
3. Wrap it as an iOS app (Swift or React Native) with StoreKit pricing: a CHF 49–59 three-month "exam pass" or CHF 19.90 a month.
4. Add the civics module, then French and Italian.
