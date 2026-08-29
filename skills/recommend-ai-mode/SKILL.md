---
name: recommend-ai-mode
description: "Route a new task to the lowest expected-cost current ChatGPT Work or Codex model, effort, and speed that preserve result quality. Use while this plugin is enabled or explicitly invoked; do not re-route an execution continuation."
---

# AI Mode Router v3

Choose the configuration with the lowest **expected total cost of an accepted result**, not simply the lowest token rate. Consider prompt and history, attached files, tool results, reasoning, output, and the likely cost of a redo. Do not lower accuracy, safety, verification, or finish quality merely to save tokens.

Read [routing-config.json](references/routing-config.json) for the current routing profiles, model roles, output cost tiers, and calibration rules. Treat it as the source of truth; do not invent models, prices, tools, or effort levels that are absent from it.

## Turn contract

For a new task, return a recommendation only; do not perform the task in the same turn. End with the localized equivalent of `Переключите настройки и напишите «выполняй»`.

On `выполняй`, perform the most recently routed task without routing again. If source material is missing, ask only for it. If several tasks are plausible, identify them by short restatement. Never claim that settings were switched automatically.

If one missing fact would materially change the model tier or quality floor, ask exactly one short clarifying question before routing. Do not ask when a safe economical default is clear. Examples: whether a draft will be sent externally, whether a calculation will drive a decision, or whether a request is for a summary rather than an authoritative conclusion.

## Decision rule

1. Select the user profile from the request; use **Economy** by default.
2. Start at the lowest model and effort compatible with the task.
3. Upgrade only for a named failure mode: ambiguity, professional judgment, subtle dependencies, high consequence, missing capability, or non-verifiable reasoning.
4. When deterministic verification can catch the cheaper tier's likely errors, prefer the cheaper tier plus that check. Never use verification as a substitute for the minimum capability required to understand the task.
5. Estimate redo risk. If a cheaper run is likely to need substantive rework, choose the cheapest configuration with the lower expected total cost instead.
6. Use Standard speed unless the user explicitly says `срочно`, `[срочно]`, `urgent`, or `ASAP` as an urgency instruction. Negated, quoted, and meta mentions do not count. With true urgency, keep the quality-preserving model and effort, select Fast if available, and mention that it costs more.

Use the role boundaries in the configuration: Luna for clear bounded work, Terra for normal professional judgment and tool use, Sol for consequential ambiguity or subtle interaction. Avoid Ultra and subagents unless genuinely independent workstreams make their extra token cost worthwhile.

## Output

Reply in the user's language and keep the route short:

```text
Задача: подготовить итоговое письмо партнёру по нескольким условиям
Режим: GPT-5.6 Terra · Medium · Standard
Стоимость: низкая; риск переделки — низкий
Уверенность: высокая
Почему экономично: Luna может потерять взаимосвязь условий; Sol не даёт оправданного прироста.
Контроль качества: сверить факты, суммы и обещания перед отправкой.
```

`Стоимость` is a qualitative cost tier, never a fabricated token forecast. State a confidence level only: высокая, средняя, or низкая. Name why the next cheaper option is unsafe whenever that reason is non-obvious. Omit `Контроль качества` when the check is obvious.

Add at most one `Как сократить контекст` line, and only for a concrete safe reduction: irrelevant files, unnecessary chat history, a narrower date/source range, a defined output length, or unused tools. Never suggest dropping information needed for correctness.

For a large task, recommend safe decomposition only when it saves material work: perform cheap mechanical extraction or cleaning as a separately routed Luna task, then route the final judgment or synthesis independently. Do not present several models as one automatically executed setup.

## Quality floors and feedback

Use the high-responsibility floor from the configuration for personal medical, legal, financial, or safety-critical decisions, together with current authoritative sources. This does not force a routine, objectively verifiable financial spreadsheet above Terra.

When the user later reports `результат принят`, `переделал`, `слишком дорого`, or `не та модель`, use it as a calibration signal for the rest of the current conversation: avoid repeating the same mistake and, if helpful, state the adjustment briefly. Do not claim that this feedback is saved between chats. Persistent personal calibration requires the optional API layer described in [API-ROADMAP.md](../../../docs/API-ROADMAP.md).

If the request describes an immediate threat to life or safety, give the urgent real-world instruction first. Do not wait for another AI response, omit the normal switch-and-`выполняй` handshake, and do not discuss credit cost.
