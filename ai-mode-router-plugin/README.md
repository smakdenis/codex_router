# AI Mode Router

AI Mode Router recommends the most economical ChatGPT Work or Codex model, reasoning effort, and speed that can still produce an acceptable result. Version 3 optimizes expected total cost: a cheap first answer is not economical if it predictably needs a costly rewrite.

## What it returns

For a new task it recommends one model, one effort level, and one speed setting, along with a qualitative cost tier, confidence, and a quality check when needed. The user switches the settings and replies `выполняй` to start the task.

## Limits

The plugin cannot inspect an unsent prompt, change model settings automatically, or keep a reliable personal learning history across chats. It never claims otherwise. Persistent calibration and true multi-stage automation belong to the optional API companion described in [docs/API-ROADMAP.md](docs/API-ROADMAP.md).

## Updating model data

The maintained routing roles, supported effort levels, qualitative cost tiers, and `validAsOf` date live in [routing-config.json](skills/recommend-ai-mode/references/routing-config.json). Update that file only from official product information, then run the checks below.

## Validation

```bash
python3 scripts/validate_router_resources.py
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/recommend-ai-mode
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

The evaluation corpus in [tests/evaluation-cases.json](tests/evaluation-cases.json) is a manual regression suite: test each prompt in a fresh chat and judge the recommendation against its stated acceptance criteria.

## License

MIT. See [LICENSE](LICENSE).
