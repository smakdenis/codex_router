# AI Mode Router

<p align="center">
  <img src="assets/icon-ai-pencil.png" width="180" alt="AI Mode Router — magical AI pencil icon">
</p>

<p align="center"><strong>Choose the lowest-cost AI mode that is still likely to deliver an accepted result.</strong></p>

AI Mode Router is a skills-only plugin for ChatGPT and Codex. It recommends the most economical
available model, reasoning effort, and speed for each new task—without pretending that the cheapest
first answer is always the cheapest outcome. It accounts for ambiguity, verification, context size,
and the risk of paying for a redo.

The plugin does not call external services, send data anywhere, or change your model settings. It
gives a short recommendation; you choose the settings and then reply `выполняй` to start the task.

## What it does

- Starts with the least expensive suitable model and effort.
- Raises the tier only for a concrete failure risk: professional judgement, ambiguity, subtle
  dependencies, high consequence, or a required capability.
- Prefers a cheaper model plus a reliable check—tests, recalculation, source cross-checking, or
  render review—when that preserves quality.
- Uses **Fast** only when the request explicitly says `срочно`, `urgent`, or `ASAP`.
- Returns a qualitative cost tier, confidence level, and the reason the next cheaper option is unsafe.
- Asks one focused clarification when it can materially reduce cost or prevent overkill.

## Example

**Prompt**

> Prepare a calm reply to a bank about a temporary cash-flow gap; the facts are attached.

**Recommendation**

```text
Задача: подготовить письмо банку по временному кассовому разрыву
Режим: GPT-5.6 Terra · Medium · Standard
Стоимость: низкая; риск переделки — низкий
Уверенность: высокая
Почему экономично: Luna может потерять деловой нюанс; Sol не даёт оправданного прироста.
Контроль качества: сверить факты, суммы и обещания перед отправкой.
```

Switch to the recommended settings, then write `выполняй`.

## Install

This repository is a ready-to-import GitHub marketplace. It supports two installation paths.

### Workspace or team installation

For a ChatGPT workspace, an administrator can import this repository as a marketplace:

1. Open **Admin → Plugins → Add → Import marketplace**.
2. Set **Source** to `https://github.com/smakdenis/codex_router`.
3. Leave **Path** empty and keep the `main` branch.
4. Import the marketplace, enable **AI Mode Router** for the required roles, and ask users to start a new chat.

### Personal installation

Create this file on your computer:

- macOS: `~/.agents/plugins/marketplace.json`
- Windows: `%USERPROFILE%\\.agents\\plugins\\marketplace.json`

Use the following content (merge the `plugins` entry if you already have a personal marketplace):

```json
{
  "name": "personal",
  "interface": {
    "displayName": "Personal"
  },
  "plugins": [
    {
      "name": "ai-mode-router",
      "source": {
        "source": "url",
        "url": "https://github.com/smakdenis/codex_router.git",
        "ref": "main"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Restart the ChatGPT desktop app, open **Plugins → Personal**, install **AI Mode Router**, and start a new chat. In Codex CLI, open the plugin browser with `/plugins`, install it from the configured marketplace, then start a new session.

GitHub marketplaces are suitable for team or self-managed distribution. Listing a plugin in the universal public Plugins Directory requires OpenAI’s separate plugin-review process.

## Use

After installation, write a normal task and let ChatGPT select the router when appropriate, or invoke it explicitly with `@AI Mode Router`.

```text
@AI Mode Router
Срочно: найди причину редкого production-бага в нескольких сервисах.
```

The router recommends the mode first. Reply `выполняй` only after switching the settings yourself.

## Limits and privacy

- It cannot see text before you send it.
- It cannot switch the model, reasoning effort, or speed automatically.
- It can use outcome feedback within the current chat, but does not store personal feedback between chats.
- It is guidance, not medical, legal, financial, or safety advice. High-consequence requests are routed to a stronger configuration with authoritative-source checks.

See the [privacy note](docs/PRIVACY.md) and the [API roadmap](docs/API-ROADMAP.md) for the optional future layer that could offer opt-in persistent calibration.

## Support

For installation questions, bug reports, and feature requests, use the
[GitHub issue tracker](https://github.com/smakdenis/codex_router/issues).

## Development

```bash
python3 scripts/validate_router_resources.py
```

The manual regression corpus lives in [tests/evaluation-cases.json](tests/evaluation-cases.json).
The public-review scenarios are in [tests/submission-test-cases.md](tests/submission-test-cases.md).

## License

[MIT](LICENSE) © Denis
