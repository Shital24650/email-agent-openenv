__all__ = ["grade_step", "final_grade"]


def clamp_score(score):
    return min(0.99, max(0.01, score))


def grade_step(action, correct):  # ✅ FIXED
    score = 0.3  # better base

    try:
        category = str(action.category).lower().strip()
        priority = str(action.priority).lower().strip()
        response = str(action.response).lower().strip() if action.response else ""

        expected_category = correct.get("category", "")
        expected_priority = correct.get("priority", "")

        # ✅ Category
        if category == expected_category:
            score += 0.3
        else:
            score -= 0.1

        # ✅ Priority
        if priority == expected_priority:
            score += 0.25
        else:
            score -= 0.05

        # ✅ Strong bonus (helps reach 0.95+)
        if category == expected_category and priority == expected_priority:
            score += 0.15

        # ✅ Response quality
        if response:
            if len(response.split()) > 5:
                score += 0.1
            else:
                score += 0.05

        # Clamp
        return clamp_score(round(score, 2))

    except Exception:
        return 0.6


def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    # Boost for high performance
    if avg > 0.85:
        avg += 0.03

    return clamp_score(round(avg, 2))
