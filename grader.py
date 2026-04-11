__all__ = ["grade_step", "final_grade"]

def clamp_score(score):
    # Ensures score is STRICTLY between (0,1)
    return min(0.99, max(0.01, score))


def grade_step(observation, action, correct):
    score = 0.3

    try:
        category = str(action.category).lower().strip()
        priority = str(action.priority).lower().strip()
        response = str(action.response).lower().strip() if action.response else ""
        action_type = str(getattr(action, "action", "")).lower().strip()

        expected_category = correct.get("category", "")
        expected_priority = correct.get("priority", "")
        expected_action = correct.get("action_type", "")

        # Category scoring
        if category == expected_category:
            score += 0.45
        else:
            score -= 0.1

        # Priority scoring
        if priority == expected_priority:
            score += 0.25
        else:
            score -= 0.05

        # Action type scoring
        if expected_action:
            if action_type == expected_action:
                score += 0.15
            else:
                score -= 0.05

        # Response scoring
        if response:
            if len(response.split()) > 5:
                score += 0.2
            else:
                score += 0.1
        else:
            score -= 0.05

        # Bonus rules
        if category == "spam" and action_type == "ignore":
            score += 0.05

        if category == "work" and priority == "high":
            score += 0.05

        if category in ["work", "spam", "personal"]:
            score += 0.05

        # ✅ FIX: round FIRST, then clamp
        score = round(score, 2)
        score = clamp_score(score)

        return score

    except Exception:
        # Keep fallback safe as well
        return 0.5


def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    if avg > 0.85:
        avg += 0.03

    # ✅ FIX: round FIRST, then clamp
    avg = round(avg, 2)
    avg = clamp_score(avg)

    return avg
