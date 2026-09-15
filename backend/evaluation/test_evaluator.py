from backend.evaluation.evaluator import evaluate_answer


question = "What is a Python context manager?"


excellent_answer = """
A context manager manages resources using the __enter__ and __exit__
methods. The with statement calls __enter__ when entering the block
and __exit__ when leaving it. This ensures cleanup happens even if
an exception occurs.
"""


partial_answer = """
A context manager is used with the with statement to manage resources
and automatically clean them up.
"""


weak_answer = """
It is something Python uses to open and close files.
"""


incorrect_answer = """
A context manager is a Python variable that stores data in memory.
"""


answers = [
    ("EXCELLENT", excellent_answer),
    ("PARTIAL", partial_answer),
    ("WEAK", weak_answer),
    ("INCORRECT", incorrect_answer),
]


print("\n" + "=" * 60)
print("HYBRID EVALUATOR TEST")
print("=" * 60)

for name, answer in answers:

    result = evaluate_answer(
        question=question,
        answer=answer,
    )

    print(f"\n{name} ANSWER")
    print("-" * 40)
    print(f"Score: {result.score}/10")
    print(f"Correctness: {result.correctness}")
    print(f"Feedback: {result.feedback}")

print("\n" + "=" * 60)