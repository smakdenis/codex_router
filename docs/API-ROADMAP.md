# API roadmap: adaptive routing

The native plugin recommends settings but cannot read an unsent prompt, switch the active model, or retain reliable feedback across chats. Those boundaries are intentional platform limits, not features promised by this repository.

An optional API companion can add the following without changing the native plugin's safe default:

1. Store only explicit feedback: task category, selected configuration, outcome, redo reason, and an optional cost band. Do not store prompt text or attachments by default.
2. Estimate expected total cost as execution cost plus expected redo cost. Use aggregate outcomes, not fabricated per-request token predictions.
3. Split eligible jobs into independently approved stages: inexpensive extraction or cleaning first, then final synthesis or judgment with the appropriate model.
4. Refresh model capabilities and price data from official sources on an explicit schedule, with a visible `validAsOf` date and a rollbackable snapshot.
5. Require the user to approve every proposed model change and every external API request.

Success metrics: accepted-result cost, redo rate, routing accuracy against the evaluation corpus, and calibration of the confidence label. Do not optimize for the lowest initial token count alone.
