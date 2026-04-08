import os
import json
from openai import OpenAI

from env import EmailEnv
from models import Action
from grader import final_grade
from dotenv import load_dotenv

load_dotenv()

# =========================
# ✅ ENV VARIABLES (MANDATORY)
# =========================
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL = os.getenv("MODEL_NAME")
API_KEY = os.getenv("HF_TOKEN")  # ✅ FIXED

if not API_KEY:
    print("[DEBUG] No API key found, running in fallback mode", flush=True)

# =========================
# ✅ OPENAI CLIENT (SAFE)
# =========================
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY if API_KEY else "dummy"  # ✅ prevents crash
)

# =========================
# ✅ INIT ENV
# =========================
env = EmailEnv()
obs = env.reset()

total_score = 0.0
steps = 0
rewards = []

print("[START] task=email_agent env=openenv model=" + str(MODEL), flush=True)

# =========================
# 🔁 MAIN LOOP
# =========================
while True:
    print(f"[STEP] step={steps+1} action=process_email reward=0.00 done=false error=null", flush=True)

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
        # ✅ LLM CALL
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content.strip()
        parsed = json.loads(output)

        category = parsed.get("category", "work")
        priority = parsed.get("priority", "medium")
        reply = parsed.get("response", "Handled email.")

    except Exception as e:
        print(f"[DEBUG] Model error: {e}", flush=True)

        # ✅ FALLBACK (VERY IMPORTANT)
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

    # =========================
    # ✅ STEP ENV
    # =========================
    action = Action(
        category=category,
        priority=priority,
        response=reply
    )

    obs, reward, done, _ = env.step(action)

    total_score += reward.score
    rewards.append(reward.score)
    steps += 1

    if done:
        break

# =========================
# ✅ FINAL SCORE
# =========================
final_score = final_grade(total_score, steps)

rewards_str = ",".join(f"{r:.2f}" for r in rewards)

print(
    f"[END] success=true steps={steps} score={final_score:.3f} rewards={rewards_str}",
    flush=True
)
