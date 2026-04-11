__all__ = ["grade_step", "final_grade"]

def clamp_score(score):
    return min(0.99, max(0.01, score))


__all__ = ["grade_step", "final_grade"]

def clamp_score(score):
    return min(0.99, max(0.01, score))


def grade_step(action, correct):
    score = 0.4  # 🔥 higher base

    try:
        category = str(action.category).lower().strip()
        priority = str(action.priority).lower().strip()
        response = str(action.response).strip() if action.response else ""

        expected_category = correct.get("category", "")
        expected_priority = correct.get("priority", "")

        # ✅ Category (main signal)
        if category == expected_category:
            score += 0.3
        else:
            score -= 0.05

        # ✅ Priority
        if priority == expected_priority:
            score += 0.2
        else:
            score -= 0.05

        # ✅ Response (only bonus, no heavy penalty)
        if response and len(response.split()) >= 3:
            score += 0.1

        # 🔥 Strong bonus for perfect match
        if category == expected_category and priority == expected_priority:
            score += 0.1

        # 🔥 Light realism bonus
        if category in ["work", "spam", "personal"]:
            score += 0.05

        # 🔥 Final clamp
        score = clamp_score(round(score, 2))

        return score

    except Exception:
        return 0.6  # safer fallback


def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    # 🔥 Boost high performers
    if avg > 0.85:
        avg += 0.05

    return clamp_score(round(avg, 2))

def final_grade(total_score, steps):
    if steps <= 0:
        return 0.01

    avg = total_score / steps

    if avg > 0.85:
        avg += 0.03

    avg = round(avg, 2)
    avg = clamp_score(avg)

    
    return avg
