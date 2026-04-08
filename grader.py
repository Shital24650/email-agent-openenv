__all__ = ["grade_step", "final_grade"]

def safe_score(score):
    if score >= 1.0:
        return 0.99
    elif score <= 0.0:
        return 0.01
    return score


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

        if category == expected_category:
            score += 0.45
        else:
            score -= 0.1

        if priority == expected_priority:
            score += 0.25
        else:
            score -= 0.05

        if expected_action:
            if action_type == expected_action:
                score += 0.15
            else:
                score -= 0.05

        if response:
            if len(response.split()) > 5:
                score += 0.2
            else:
                score += 0.1
        else:
            score -= 0.05

        if category == "spam" and action_type == "ignore":
            score += 0.05

        if category == "work" and priority == "high":
            score += 0.05

        if category in ["work", "spam", "personal"]:
            score += 0.05

        score = safe_score(score)
        return round(score, 2)

    except:
        return 0.5


def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    if avg > 0.85:
        avg += 0.03

    avg = safe_score(avg)
    return round(avg, 2)
