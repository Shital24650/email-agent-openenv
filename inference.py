import os
import json
from openai import OpenAI

from env import EmailEnv
from models import Action
from grader import final_grade
from dotenv import load_dotenv

load_dotenv()

# 🔥 Initialize OpenAI client
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

MODEL = os.getenv("MODEL_NAME")

# 🔥 Initialize environment
env = EmailEnv()
obs = env.reset()

total_score = 0
steps = 0
rewards_list = []

print(f"[START] task=email_agent env=email_env model={MODEL}")


def safe_parse_json(output: str):
    """Clean and parse model output safely"""
    try:
        output = output.strip()

        # Remove markdown ```json ```
        if output.startswith("```"):
            parts = output.split("```")
            if len(parts) >= 2:
                output = parts[1]
            if output.startswith("json"):
                output = output[4:]

        return json.loads(output.strip())

    except Exception:
        return None


while True:
    # 🔥 Strong prompt for better accuracy
    prompt = f"""
You are a STRICT email classification AI.

Rules:
- spam → ads, lottery, offers, promotions
- work → meetings, invoices, urgent issues, business
- personal → friends, casual, social

Priority:
- high → urgent, asap, server down
- medium → normal communication
- low → spam or non-important

Email:
Subject: {obs.subject}
Body: {obs.body}

Return ONLY valid JSON (no markdown):

{{
  "category": "spam | work | personal",
  "priority": "low | medium | high",
  "response": "short professional reply"
}}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw_output = response.choices[0].message.content
        parsed = safe_parse_json(raw_output)

        if parsed:
            category = parsed.get("category", "work").lower().strip()
            priority = parsed.get("priority", "medium").lower().strip()
            reply = parsed.get("response", "Handled email.")
        else:
            raise ValueError("Invalid JSON")

    except Exception:
        # 🔥 Strong fallback (rare now)
        text = (obs.subject + " " + obs.body).lower()

        if any(word in text for word in ["lottery", "click", "offer", "discount", "buy", "win"]):
            category = "spam"
            priority = "low"
        elif any(word in text for word in ["meeting", "invoice", "server", "urgent", "asap", "project"]):
            category = "work"
            priority = "high"
        elif any(word in text for word in ["dinner", "meet", "friend"]):
            category = "personal"
            priority = "medium"
        else:
            category = "work"
            priority = "medium"

        reply = f"Handled email about: {obs.subject}"

    # 🔥 Create action
    action = Action(
        category=category,
        priority=priority,
        response=reply
    )

    # 🔥 Step environment
    obs, reward, done, _ = env.step(action)

    steps += 1
    total_score += reward.score
    rewards_list.append(reward.score)

    print(
        f"[STEP] step={steps} action={category}|{priority} "
        f"reward={reward.score:.2f} done={str(done).lower()} error=null"
    )

    if done:
        break

# 🔥 Final scoring
final_score = final_grade(total_score, steps)
success = final_score > 0.5

print(
    f"[END] success={str(success).lower()} steps={steps} "
    f"score={final_score:.2f} rewards=" +
    ",".join(f"{r:.2f}" for r in rewards_list)
)
