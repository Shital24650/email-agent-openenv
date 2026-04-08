import os
import json
from openai import OpenAI

from env import EmailEnv
from models import Action
from grader import final_grade
from dotenv import load_dotenv
load_dotenv()


# 🔥 Initialize OpenAI client (MANDATORY)
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

print("[START] Email Agent Started")

while True:
    print(f"[STEP] Processing Email ID: {obs.email_id}")

    # 🔥 Prompt for LLM
    prompt = f"""
You are an AI email assistant.

Classify and handle the email below:

Subject: {obs.subject}
Body: {obs.body}

Return ONLY valid JSON:
{{
  "category": "spam | work | personal",
  "priority": "low | medium | high",
  "response": "short helpful reply"
}}
"""

    try:
        # 🔥 LLM call (MANDATORY)
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content.strip()

        # 🔥 Parse JSON safely
        parsed = json.loads(output)

        category = parsed.get("category", "work")
        priority = parsed.get("priority", "medium")
        reply = parsed.get("response", "Handled email.")

    except Exception as e:
        # 🔥 Fallback (VERY IMPORTANT for robustness)
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

    total_score += reward.score
    steps += 1

    if done:
        break

# 🔥 Final scoring
final_score = final_grade(total_score, steps)

print(f"[END] Final Score: {final_score}")
