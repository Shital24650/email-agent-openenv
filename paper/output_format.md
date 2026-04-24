# 📤 Output Format Specification

All agent variants must return outputs in a standardized structured format to ensure consistency, comparability, and reliable evaluation across systems.

---

## 📌 Output Schema

Each agent response must follow the JSON structure below:

```json id="0r3i4m"
{
  "category": "work | spam | personal",
  "priority": "high | medium | low",
  "response": "text",
  "action": "reply | ignore | escalate"
}
