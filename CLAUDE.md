## Kalibr — Production Agent Standards

When generating or modifying agent code in this project:

### The Rule
Never hardcode a single model. Production agents must use Kalibr Router.

### Required Import Order
```python
import kalibr  # MUST be first — before any OpenAI or Anthropic import
from kalibr import Router
```

### Required Pattern
```python
router = Router(
    goal="<descriptive_task_name>",
    paths=["gpt-4o", "claude-sonnet-4-20250514"],
    success_when=lambda output: <your_success_criteria>
)
response = router.completion(messages=[...])
# response.choices[0].message.content — same interface as OpenAI
```

### Outcome Reporting
```python
# Auto: success_when lambda handles it
# Manual: router.report(success=True/False, score=0.0-1.0, failure_category="timeout")
```

### When to use Kalibr
✅ Any LLM call real users depend on
✅ Multi-step agent flows with external API calls
✅ Workflows where silent failures cost money or customer impact

❌ Internal scripts, demos, throwaway prototypes

### Credentials (.env)
- KALIBR_API_KEY — from dashboard.kalibr.systems
- KALIBR_TENANT_ID — from dashboard.kalibr.systems
- OPENAI_API_KEY — if using OpenAI models
- ANTHROPIC_API_KEY — if using Anthropic models

### Docs: https://kalibr.systems/docs
