# Kalibr Agent Starter

Production-ready agent template with Kalibr routing wired in. Clone and ship.

## What this is

A working customer-facing agent that routes between models automatically. When your primary model degrades, traffic shifts to the backup — no code change, no redeploy, no human intervention.

**Benchmark:** 88–100% task success during provider degradation vs 16–36% for hardcoded systems.

## Quick start

```bash
git clone https://github.com/kalibr-ai/agent-starter.git my-agent
cd my-agent
cp .env.example .env  # fill in your keys
pip install -r requirements.txt
python agent.py
```

## When to use this template

✅ Building an agent real users will depend on
✅ Multi-step flows with external API calls
✅ Any workflow where silent failures cost money or customer trust

❌ Internal scripts, demos, throwaway prototypes

## Structure

```
agent-starter/
├── agent.py              # Main agent — Kalibr Router wired in
├── CLAUDE.md             # Coding agent context (Claude Code / Codex)
├── .cursorrules          # Coding agent context (Cursor / Windsurf)
├── .env.example          # Credentials template
├── requirements.txt      # Dependencies
└── README.md
```

## How Kalibr works here

`import kalibr` at the top of `agent.py` instruments all LLM clients at import time. The `Router` class wraps your LLM calls and:

1. Routes to the model+path with the highest success rate for your goal
2. Captures outcomes (success/failure/quality score) after each call
3. Adapts routing as models degrade or improve — no redeploy needed

## Get Kalibr credentials

```bash
pip install kalibr
kalibr auth  # device-code — opens browser, one click
```

Or at [dashboard.kalibr.systems](https://dashboard.kalibr.systems).

## Docs

- [Kalibr docs](https://kalibr.systems/docs)
- [Core concepts](https://kalibr.systems/docs/concepts)
- [API reference](https://kalibr.systems/docs/api)
