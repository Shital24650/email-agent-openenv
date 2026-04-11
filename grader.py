__all__ = ["grade_step", "final_grade"]

def clamp_score(score):
    return min(0.99, max(0.01, score))


def grade_step(observation, action, correct):
    score = 0.2  # ✅ reduced base score

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
            score += 0.35  # ✅ reduced
        else:
            score -= 0.1

        # Priority scoring
        if priority == expected_priority:
            score += 0.2  # ✅ reduced
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
                score += 0.15  # ✅ reduced
            else:
                score += 0.1
        else:
            score -= 0.05

        # Bonus rules (all reduced)
        if category == "spam" and action_type == "ignore":
            score += 0.02

        if category == "work" and priority == "high":
            score += 0.02

        if category in ["work", "spam", "personal"]:
            score += 0.02

        # Round then clamp
        score = round(score, 2)
        score = clamp_score(score)

        
        return score

    except Exception:
        return 0.5


def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    if avg > 0.85:
        avg += 0.03

    avg = round(avg, 2)
    avg = clamp_score(avg)

    
    return avg
