# Validation notes

Checked on 24 November 2026 against the original Claude source pinned in provenance/source.json.

## Source and package checks

Passed:

- The saved original matches Git blob 78c1f67985c4fa9763bf832b3d1ad078235b305a and its recorded SHA-256.
- All 20 cards and the complete source registry match the original sections, apart from a final newline.
- The operating principles, S1–S4, Step 1, Steps 3–6, all design moves and playbooks, Quick mode, stress-test, delivery, staffing maths, UDL and reviewer notes retain their original substantive text.
- The original opening and conditional output-credit strings are present verbatim. The requested basis/adaptation/licence notices appear in the instructions, README and licence file.
- The URL-fetch restriction is removed; plain questions replace multiple-choice tools; mandatory card/source lookup and the dated browsing fallback are explicit.
- JSON and YAML parse correctly; references resolve; manifest metadata and prompt limits are valid.
- The ZIP contains exactly the intended seven runtime files. Every packaged byte matches the corresponding repository file. SHA256SUMS matches the archive.
- The saved ChatGPT plugin was read back: the executing instructions and both appendices were retained. ChatGPT normalises account/publisher metadata; it does not change the required attribution text in the instructions.

## Behaviour checks

Two fresh consultations were run against the final instructions with web access:

| Scenario | Observed result |
| --- | --- |
| Quick mode: 120 accounting students; Apply/Analyse/Evaluate; lecture/seminar rooms; one lecturer; ordinary laptops | Retrieved card/source files; selected cards 7, 5 and 9 with full cohort/provision/Bloom matches; made S1 conditional on controlled paper conditions; treated unrestricted laptops as S3; included UDL and the original opening, card and workflow credits verbatim. |
| Opening consultation: 90 programming students; take-home project; uncontrolled IT lab; one lecturer; six hours | Ran source checks; invited clarification with four plain questions; identified the staffing constraint; treated open-device observation as S3; waited for agreement on the capability target before recommending designs; reproduced the original opening and workflow credits verbatim. |

The earlier draft shortened the credits during these checks. The final instructions therefore include an explicit verbatim-output check; both fresh runs reproduced the required lines correctly.

These are instruction-level behaviour checks, not a guarantee of identical model responses. The complete multi-turn design, document export and a genuinely browsing-unavailable host session were not exercised end to end. The corresponding instructions are present and checked structurally.

## Trying the saved plugin

Open the plugin in ChatGPT and select it in a fresh conversation. Use either scenario above, or one of the supplied starters. Check that it retrieves references and runs Step 0; asks only for information that changes the advice; obtains agreement before recommending; and labels assurance honestly.

For a complete design, continue through the target agreement, option choice, stress-test and final plan. If the session has no web tools, it must disclose that fact and name the baseline date as 24 November 2026. A failed PDF fetch must never become a claim that the full PDF was read.
