# Assured Assessment Design — ChatGPT Plugin

A consultative assessment-design plugin for educators. **This ChatGPT version is an adaptation of the Claude skill.** It preserves the complete workflow and assessment content of the [Claude version](https://github.com/sirmarlfox/assured-assessment-design-claude-skill), with the platform changes recorded in [ADAPTATION.md](ADAPTATION.md).

It begins by checking current guidance, invites the educator's account of their situation, agrees what learning must be assured, then develops inclusive and workable options. It combines supervised, in-person and interactive assessment with open preparation or take-home work where appropriate.

## What it does

- Preserves the opening credit line and conditional card/workflow output credits.
- Runs Steps 0–6: currency check; story; situation model; agreed target; options; stress-test; delivery.
- Retains eight operating principles, S1–S4 assurance ratings, all ten design moves and all twelve scenario playbooks, including open-device IT labs and take-home work with an in-person endpoint.
- Offers Light, Medium and Structural options; Quick mode; staffing calculations; student-facing wording; an inclusion layer using UDL; and all seven reviewer cautions.
- Retrieves the relevant entries from the complete 20-card library and source registry before using them. Cards are starting points for design, not automatic prescriptions.
- Distinguishes regulator guidance, research/sector frameworks, practitioner designs, untested ideas and inference.

Institutional regulations, module approval rules and the educator's quality office determine which assessment changes can be made. This is not an AI detector or a ruling on an individual student's adjustments or misconduct.

## Set it up in ChatGPT

The main deliverable is a native plugin containing one instructional skill and its reference files. It requires no API key, external server or connected account.

1. Open [Assured Assessment Design in ChatGPT](https://chatgpt.com/plugins/plugins_6b05514dee7c8191bb1f4812722bc0d4) if you have access to this saved personal plugin. For another account, download [the installable plugin ZIP](dist/assured-assessment-design-chatgpt-plugin-1.0.1.zip).
2. To install a copy from the ZIP, use Plugin Creator in ChatGPT and ask it to install the attached plugin ZIP. Where your workspace exposes manual plugin uploads, its upload interface is another route.
3. Open the saved plugin and install/select it if ChatGPT prompts you. Start a conversation by mentioning **Assured Assessment Design**.
4. Use a session with **web search available**. The plugin requires search and page/PDF retrieval for Step 0; account and workspace controls determine whether those tools are available. Its manifest cannot turn on a session's built-in search setting.
5. Try one of the conversation starters below. The first consultation should open with the original credit line, give the currency-check result or baseline disclosure, and invite your story. It should seek agreement on the target before generating options.

The plugin uses the session's existing search tools; it does not include a separate search service. When browsing is unavailable it must say:

> Web browsing is unavailable in this session. I am using the baseline source registry dated 24 November 2026; I cannot verify whether newer guidance has been published.

It then continues using the baseline registry. A failed individual page or PDF retrieval must also be disclosed; a search snippet must not be presented as a full-document check.

Setup references, checked 24 November 2026: [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) and [GPTs in ChatGPT](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt). OpenAI currently restricts new custom GPT creation on personal accounts; use the native plugin. Existing GPT editing and managed-workspace availability depend on the account.

## Knowledge files and instructions

| File | Purpose |
| --- | --- |
| [SKILL.md](skills/assured-assessment-design/SKILL.md) | Complete, uncondensed executing instructions |
| [Appendix A — Card library](knowledge/Appendix-A-Card-Library.md) | All 20 cards, ready to upload as a knowledge file |
| [Appendix B — Source registry](knowledge/Appendix-B-Source-Registry.md) | Complete source registry, ready to upload as a knowledge file |
| [Description and conversation starters](chatgpt-description-and-starters.md) | Requested GPT description and four starter prompts |
| [Setup metadata](chatgpt-setup.json) | Human-readable configuration values; not a GPT import format |
| [Adaptation record](ADAPTATION.md) | Changes, limitations and a comparison with the original |
| [Validation notes](VALIDATION.md) | What was checked and what still requires a live conversation |

The plugin already bundles both knowledge files under its skill's references directory. The copies in `knowledge/` are identical standalone upload files. Instructions explicitly require retrieving relevant card and source entries instead of relying on memory.

No instruction condensation was necessary: the native plugin supports the complete instruction text. A legacy GPT editor with a smaller instruction limit cannot accept the full file unchanged. Do not truncate it or silently move behavioural rules into a knowledge file; use the native plugin to preserve the workflow.

The registry's **Read** and **Seen** labels record the **original Claude builder's** checks on 24 November 2026. They do not claim that this adaptation reverified every publication. Step 0 must perform current checks at the start of each consultation; newer verified guidance takes precedence.

## Conversation starters

1. Help me redesign a take-home assessment while keeping an in-person endpoint.
2. My students use an IT lab without locked-down computers. How can I assure their learning?
3. I have a large cohort and limited staff time. Help me find workable assessment options.
4. Quick mode: help me choose three assessment formats for my cohort, learning outcomes and available rooms.

The native manifest supports three launch prompts, so the first three appear there. All four are supplied in the description/starter file.

## Build and validate

Python 3 and the development dependency are needed only to validate or rebuild the package, not to use it in ChatGPT.

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/build.py
python3 scripts/validate.py
```

The builder creates a deterministic ZIP containing only the manifest, executing skill, its two reference files, agent metadata and credit/licence notices. It also refreshes the standalone knowledge copies. `dist/SHA256SUMS` records the release checksum. The ZIP is intentionally committed so the repository offers a directly downloadable plugin.

The validator checks the pinned source checksum; complete appendix preservation; unchanged substantive workflow sections; credits; steps, moves and scenarios; reference targets; manifest/YAML syntax; and every packaged file against its source. Rebuild after changing runtime files.

A small `.gitignore` excludes local environments, credentials and caches. It deliberately keeps the release ZIP and knowledge files.

## Credits and licence

Basis: the Assured Assessment "Grab Bag" by Dr Viktoria Mileva SFHEA, University of Stirling, CC BY-NC 4.0. Original: https://claude.ai/artifact/Ry33gaHyiuXqDC7SsATyoh

Adaptation (workflow, scenario playbooks, assurance scale, live source-checking): Dr Gerhard Kristandl, Associate Professor of Accounting and Technology-Enhanced Learning, University of Greenwich Business School, developed with Claude (Anthropic).

This ChatGPT version is an adaptation of the Claude skill.

Licence CC BY-NC 4.0, non-commercial use only. Do not present the cards as anyone's own work.

The licence notice and controlling legal-text link are in [LICENSE.md](LICENSE.md). Original card material remains credited to Dr Mileva. Neither author is represented as endorsing new designs generated in a consultation.

Original Claude repository: https://github.com/sirmarlfox/assured-assessment-design-claude-skill

The original source file is pinned to commit [256bf13b2c793fcea3a780ce6f73843659138045](https://github.com/sirmarlfox/assured-assessment-design-claude-skill/blob/256bf13b2c793fcea3a780ce6f73843659138045/assured-assessment-design/SKILL.md). See [provenance/source.json](provenance/source.json) for its blob and SHA-256 checksums.
