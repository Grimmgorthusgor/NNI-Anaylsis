# Sprechprobe: fide test practice (prototype)

A working prototype of the app recommended in [`market-analysis/swiss-app-opportunities.md`](../market-analysis/swiss-app-opportunities.md): an AI examiner for practising the Swiss **fide** German test.

Live prototype (private until shared): https://claude.ai/artifact/VoQCf6zm6DGuaRFw1p3Cz6

## What it does

- **Speaking test:** the AI examiner holds a fide-style conversation of up to 6 answers on an everyday Swiss topic (housing, work, health, children & school, local authorities, shopping, getting around, free time). It includes a short role-play. The candidate answers by typing or with iPhone keyboard dictation, and can play the examiner's lines aloud.
- **Writing task:** generates a short A1/A2/B1 message task with three content points and checks the candidate's text.
- **Feedback:** gives an estimated level (below A1 / A1 / A2 / B1) against the target, 4 criteria scored out of 4, corrections with the changed words highlighted, useful phrases and a next step. Explanations come in 11 languages.
- **History:** past sessions are saved on the device (`localStorage`).

## How it runs

`sprechprobe.html` is a single-file page published as a Claude artifact. It reaches the model through the artifact runtime (`claude.use("sample")`). That means:

- there is no backend and no API key, and each viewer's own Claude account pays for the AI calls;
- it only works inside the Claude app or on claude.ai, and viewers must be signed in and allow the page to use Claude.

## Path to a store app

1. Validate with 10 to 20 real candidates using this prototype: does the estimated level match their actual fide result?
2. Move the prompts to a small backend using the Claude API, adding real speech-to-text and text-to-speech and Swiss/EU hosting.
3. Wrap it as an iOS app (Swift or React Native) with StoreKit pricing: a CHF 49–59 three-month "exam pass" or CHF 19.90 a month.
4. Add French and Italian (same engine, new prompts).

The name "fide" belongs to the SEM programme, so the app is branded *Sprechprobe* and describes itself as practice *for* the fide test, with no pass guarantee.
