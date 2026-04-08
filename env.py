from models import Observation, Action, Reward
from grader import grade_step
import random


class EmailEnv:
    def __init__(self):
        # 🔥 Emails with difficulty + ground truth
        self.emails = [
            # EASY (Spam detection)
            {
                "id": 1,
                "subject": "Win a lottery",
                "body": "Click now!!!",
                "sender": "spam@fake.com",
                "category": "spam",
                "priority": "low",
                "difficulty": "easy"
            },

            # EASY
            {
                "id": 2,
                "subject": "50% discount offer",
                "body": "Buy now",
                "sender": "ads@promo.com",
                "category": "spam",
                "priority": "low",
                "difficulty": "easy"
            },

            # MEDIUM (normal classification)
            {
                "id": 3,
                "subject": "Dinner tonight?",
                "body": "Let’s meet",
                "sender": "friend@gmail.com",
                "category": "personal",
                "priority": "medium",
                "difficulty": "medium"
            },

            # MEDIUM
            {
                "id": 4,
                "subject": "Meeting tomorrow",
                "body": "Project discussion",
                "sender": "boss@company.com",
                "category": "work",
                "priority": "high",
                "difficulty": "medium"
            },

            # HARD (needs good response)
            {
                "id": 5,
                "subject": "Urgent: server down",
                "body": "Fix ASAP",
                "sender": "devops@company.com",
                "category": "work",
                "priority": "high",
                "difficulty": "hard"
            },

            # HARD
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

    # 🔥 RESET ENV
    def reset(self):
        self.index = 0
        self.done = False
        random.shuffle(self.emails)  # 🔥 important for generalization
        return self._get_obs()

    # 🔥 STEP FUNCTION
    def step(self, action: Action):
        current_email = self.emails[self.index]

        # 🔥 Get correct answer dynamically
        correct = {
            "category": current_email["category"],
            "priority": current_email["priority"]
        }

        # 🔥 Base score from grader
        score = grade_step(action, correct)

        # 🔥 HARD TASK: enforce response quality
        if current_email["difficulty"] == "hard":
            if not action.response or len(action.response.strip()) < 15:
                score -= 0.2

        # 🔥 Normalize inputs
        action.category = str(action.category).lower().strip()
        action.priority = str(action.priority).lower().strip()

        if action.category not in ["work", "spam", "personal"]:
            score -= 0.05

        if action.priority not in ["high", "medium", "low"]:
            score -= 0.05

        # 🔥 Clamp score (VERY IMPORTANT)
        score = max(0.0, min(1.0, score))

        # 🔥 Feedback
        if score > 0.8:
            feedback = "correct"
        elif score > 0.5:
            feedback = "partial"
        else:
            feedback = "wrong"

        reward = Reward(score=round(score, 2), feedback=feedback)

        # 🔥 Move to next step
        self.index += 1
        if self.index >= len(self.emails):
            self.done = True

        return self._get_obs(), reward, self.done, {}

    # 🔥 STATE (required for OpenEnv)
    def state(self):
        return {"current_index": self.index}

    # 🔥 OBSERVATION
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
