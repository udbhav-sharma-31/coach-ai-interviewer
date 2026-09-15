def difficulty_node(state):
    evaluations = state["evaluations"]
    current_difficulty = state["difficulty"]

    # Calculate average performance across all answered questions.
    scores = [
        evaluation["score"]
        for evaluation in evaluations
    ]

    average_score = sum(scores) / len(scores)

    # Move only one difficulty level at a time.
    if average_score >= 8:
        if current_difficulty == "beginner":
            difficulty = "intermediate"
        else:
            difficulty = "advanced"

    elif average_score >= 5:
        if current_difficulty == "advanced":
            difficulty = "intermediate"
        else:
            difficulty = "intermediate"

    else:
        if current_difficulty == "advanced":
            difficulty = "intermediate"
        elif current_difficulty == "intermediate":
            difficulty = "beginner"
        else:
            difficulty = "beginner"

    return {
        "difficulty": difficulty,
    }