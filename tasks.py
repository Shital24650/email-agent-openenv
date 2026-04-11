from grader import grade_step
TASKS = [
    {
        "name": "easy_classification",
        "description": "Classify email category correctly",
        "weight": 0.3,
        "grader": grade_step
    },
    {
        "name": "medium_priority",
        "description": "Assign correct priority",
        "weight": 0.3,
        "grader": grade_step
    },
    {
        "name": "hard_full_action",
        "description": "Full email handling (category + priority + response)",
        "weight": 0.4,
        "grader": grade_step
    }
]
