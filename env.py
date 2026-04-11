from models import Observation, Action, Reward
from grader import grade_step
import random


class EmailEnv:
    def __init__(self):
        self.emails = [
            {
                "id": 1,
                "subject": "Win a lottery",
                "body": "Click now!!!",
                "sender": "spam@fake.com",
                "category": "spam",
                "priority": "low",
                "difficulty": "easy"
            },
            {
                "id": 2,
                "subject": "50% discount offer",
                "body": "Buy now",
                "sender": "ads@promo.com",
                "category": "spam",
                "priority": "low",
                "difficulty": "easy"
            },
            {
                "id": 3,
                "subject": "Dinner tonight?",
                "body": "Let’s meet",
                "sender": "friend@gmail.com",
                "category": "personal",
                "priority": "medium",
                "difficulty": "medium"
            },
            {
                "id": 4,
                "subject": "Meeting tomorrow",
                "body": "Project discussion",
                "sender": "boss@company.com",
                "category": "work",
                "priority": "high",
                "difficulty": "medium"
            },
            {
                "id": 5,
                "subject": "Urgent: server down",
                "body": "Fix ASAP",
                "sender": "devops@company.com",
                "category": "work",
                "priority": "high",
                "difficulty": "hard"
            },
            {
                "id": 6,
                "subject": "Invoice pending",
                "body": "Please pay",
                "sender": "finance@company.com",
                "category": "work",
                "priority": "high",
                "difficulty": "hard"
            },
        ]

        self.index = 0
        self.done = False

    # ✅ RESET (FIXED: accepts input)
    def reset(self, input=None):
        self.index = 0
        self.done = False
        random.shuffle(self.emails)

        # Optional: inject task input into first email
        if input:
            self.emails[0].update(input)

        return self._get_obs()

    # ✅ STEP (FIXED grader call + safe execution)
    def step(self, action: Action):
        current_email = self.emails[self.index]

        observation = Observation(
            email_id=current_email["id"],
            subject=current_email["subject"],
            body=current_email["body"],
            sender=current_email["sender"]
        )

        correct = {
            "category": current_email["category"],
            "priority": current_email["priority"]
        }

        # ✅ FIXED grader call
        try:
            score = grade_step(action, correct)
        except Exception:
            score = 0.0  # safe fallback

        # Extra penalty for hard tasks
        if current_email["difficulty"] == "hard":
            if not action.response or len(action.response.strip()) < 15:
                score -= 0.2

        # Normalize action values
        action.category = str(action.category).lower().strip()
        action.priority = str(action.priority).lower().strip()

        if action.category not in ["work", "spam", "personal"]:
            score -= 0.05

        if action.priority not in ["high", "medium", "low"]:
            score -= 0.05

        # ✅ FIXED reward range (STRICT)
        score = max(0.0, min(1.0, score))

        # Feedback
        if score > 0.8:
            feedback = "correct"
        elif score > 0.5:
            feedback = "partial"
        else:
            feedback = "wrong"

        reward = Reward(score=round(score, 2), feedback=feedback)

        # Move forward
        self.index += 1
        if self.index >= len(self.emails):
            self.done = True

        return self._get_obs(), reward, self.done, {}

    # ✅ STATE
    def state(self):
        return {"current_index": self.index}

    # ✅ OBSERVATION
    def _get_obs(self):
        if self.index >= len(self.emails):
            return None

        e = self.emails[self.index]

        return Observation(
            email_id=e["id"],
            subject=e["subject"],
            body=e["body"],
            sender=e["sender"]
        )
