from backend.evaluation.evaluator import evaluate_answer
from backend.evaluation.qwen_evaluator import evaluate_answer_qwen


TECHNICAL_SIGNALS = {
    "python",
    "python script",
    "python function",
    "python class",
    "python code",
    "exception handling",
    "try-except",
    "try except",
    "input validation",
    "data validation",
    "decorator",
    "decorators",
    "generator",
    "generators",
    "module",
    "modules",
    "object oriented",
    "object-oriented",
    "inheritance",
    "polymorphism",
    "garbage collection",
    "context manager",
    "rest api",
    "restful api",
    "backend development",
    "sql query",
    "sql database",
    "authentication",
    "authorization",
    "machine learning",
    "machine-learning",
    "deep learning",
    "deep-learning",
    "transformer",
    "transformers",
    "llm",
    "large language model",
    "rag",
    "retrieval augmented generation",
    "ai agent",
    "system design",
}


def is_technical_question(
    question: str,
    topic: str,
) -> bool:
    """
    Deterministically decide whether the question belongs
    to the technical domain supported by our Transformer.

    We do NOT ask Qwen to make this decision.
    """

    question_text = question.lower().strip()
    topic_text = topic.lower().strip()

    combined_text = f"{question_text} {topic_text}"

    for signal in TECHNICAL_SIGNALS:

        if signal in combined_text:
            return True

    return False


def evaluate_node(state):

    question = state["current_question"]
    answer = state["current_answer"]
    topic = state["current_topic"]

    # ---------------------------------------------------------
    # Deterministic evaluation routing
    # ---------------------------------------------------------

    technical = is_technical_question(
        question,
        topic,
    )

    if technical:

        evaluation_mode = "hybrid"

    else:

        evaluation_mode = "qwen"

    print("\n" + "=" * 60)
    print("EVALUATION ROUTER")
    print("=" * 60)

    print(f"\nQuestion: {question}")
    print(f"Topic: {topic}")
    print(f"Technical: {technical}")
    print(f"Evaluation Mode: {evaluation_mode}")

    # ---------------------------------------------------------
    # Evaluate
    # ---------------------------------------------------------

    if evaluation_mode == "hybrid":

        print("\nUsing Transformer + Qwen")

        evaluation = evaluate_answer(
            question,
            answer,
        )

    else:

        print("\nUsing Qwen only")

        evaluation = evaluate_answer_qwen(
            question,
            answer,
        )

    evaluation_data = {
        "score": evaluation.score,
        "correctness": evaluation.correctness,
        "feedback": evaluation.feedback,
    }

    # ---------------------------------------------------------
    # Interview history
    # ---------------------------------------------------------

    answers = state["answers"] + [
        answer
    ]

    evaluations = state["evaluations"] + [
        evaluation_data
    ]

    return {
        "evaluation": evaluation_data,
        "answers": answers,
        "evaluations": evaluations,
        "evaluation_mode": evaluation_mode,
    }