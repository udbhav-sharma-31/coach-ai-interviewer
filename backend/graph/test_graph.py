from langgraph.types import Command

from backend.graph.graph import interview_graph


candidate = {
    "name": "Udbhav",
    "role": "Python Developer",
    "experience_level": "Beginner",
    "skills": ["Python", "Machine Learning", "Generative AI"],
}


initial_state = {
    "candidate": candidate,

    "target_role": candidate["role"],

    "resume_profile": {
        "education": [],
        "experience": [],
        "skills": [],
        "domains": [],
        "projects": [],
        "certifications": [],
    },

    "resume_available": True,
    "resume_context": "",

    "covered_topics": [],

    "current_question": "",
    "current_topic": "",
    "evaluation_mode": "",

    "current_answer": "",
    "evaluation": None,

    "answers": [],
    "evaluations": [],
    "questions": [],

    "question_number": 0,
    "difficulty": "beginner",
    "max_questions": 5,
}


config = {
    "configurable": {
        "thread_id": "test-interview-loop-1"
    }
}


print("\nStarting interview...\n")


result = interview_graph.invoke(
    initial_state,
    config=config,
)


while "__interrupt__" in result:

    question = result["current_question"]

    print(f"\nQuestion {result['question_number']}:")
    print(question)

    print("\nCandidate's answer:")
    answer = input("> ")

    result = interview_graph.invoke(
        Command(resume=answer),
        config=config,
    )


print("\n" + "=" * 50)
print("INTERVIEW FINISHED")
print("=" * 50)

print("\nFinal difficulty:")
print(result["difficulty"])

print("\nFinal interview results:")

evaluations = result["evaluations"]

total_score = sum(
    evaluation["score"]
    for evaluation in evaluations
)

overall_score = total_score / len(evaluations)

correct = sum(
    1
    for evaluation in evaluations
    if evaluation["correctness"] == "correct"
)

partially_correct = sum(
    1
    for evaluation in evaluations
    if evaluation["correctness"] == "partially_correct"
)

incorrect = sum(
    1
    for evaluation in evaluations
    if evaluation["correctness"] == "incorrect"
)

print(f"Overall Score: {overall_score:.1f}/10")
print(f"Correct: {correct}")
print(f"Partially Correct: {partially_correct}")
print(f"Incorrect: {incorrect}")

print("\nQuestion-by-question results:")

for i, evaluation in enumerate(evaluations, start=1):
    print(
        f"Q{i}: "
        f"{evaluation['score']}/10 - "
        f"{evaluation['correctness']} - "
        f"{evaluation['feedback']}"
    )

print("\nFinal difficulty:")
print(result["difficulty"])

print("\nTotal questions:")
print(result["question_number"])