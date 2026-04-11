from models import Observation, Action, Reward
from grader import grade_step
import random


class EmailEnv:
    def __init__(self):
        # 🔥 Emails with difficulty + ground truth
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

    # 🔹 RESET ENV
    def reset(self):
        self.index = 0
        self.done = False
        random.shuffle(self.emails)
        return self._get_obs()

    # 🔹 STEP FUNCTION
    def step(self, action: Action):
        current_email = self.emails[self.index]

        # 🔥 Create observation for grader
        observation = Observation(
            email_id=current_email["id"],
            subject=current_email["subject"],
            body=current_email["body"],
            sender=current_email["sender"]
        )

        # 🔥 Correct answer
        correct = {
            "category": current_email["category"],
            "priority": current_email["priority"]
        }

        # 🔥 Score from grader
        try:
            score = grade_step(observation, action, correct)
        except:
            score = 0.5  # safe fallback

        # 🔥 HARD task: enforce better response
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

        # 🔥 FINAL CLAMP (STRICTLY BETWEEN 0 AND 1)
        score = max(0.01, min(0.99, score))

        # 🔥 Feedback
        if score > 0.8:
            feedback = "correct"
        elif score > 0.5:
            feedback = "partial"
        else:
            feedback = "wrong"

        reward = Reward(score=round(score, 2), feedback=feedback)

        # 🔥 Move to next email
        self.index += 1
        if self.index >= len(self.emails):
            self.done = True

        return self._get_obs(), reward, self.done, {}

    # 🔹 STATE
    def state(self):
        return {"current_index": self.index}

    # 🔹 OBSERVATION
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

TASKS = [
    {
        "name": "easy_classification",
        "description": "Classify email category",
        "grader": grade_step
    },
    {
        "name": "medium_priority",
        "description": "Assign correct priority",
        "grader": grade_step
    },
    {
        "name": "hard_full_action",
        "description": "Full email handling",
        "grader": grade_step
    }
]
