from backend.interview.state import InterviewEvaluation
from backend.llm.local_client import ask_local_llm_json


def is_no_answer(answer: str) -> bool:
    if not answer or not answer.strip():
        return True

    normalized = answer.lower().strip()

    no_answer_phrases = {
        "unable to answer",
        "i am unable to answer",
        "can't answer",
        "cannot answer",
        "i cannot answer",
        "don't know",
        "i don't know",
        "do not know",
        "no idea",
        "i have no idea",
        "not sure",
        "i'm not sure",
        "i am not sure",
        "unable to recall",
        "i can't recall",
        "i cannot recall",
    }

    return normalized in no_answer_phrases


def evaluate_answer_qwen(question: str, answer: str) -> InterviewEvaluation:

    if is_no_answer(answer):
        return InterviewEvaluation(
            score=0.0,
            correctness="incorrect",
            feedback="The candidate did not provide an answer to the question.",
        )

    prompt = f"""
Evaluate the candidate's answer to the interview question.

Question:
{question}

Candidate Answer:
{answer}

First determine the question type:

1. behavioral
   Questions about experience, teamwork, leadership, communication,
   problem solving, responsibilities, or situations.

2. resume_experience
   Questions asking the candidate to explain something from their
   resume or previous experience.

3. general_knowledge
   Questions asking for factual or conceptual knowledge.

For behavioral and resume_experience questions, evaluate:

- relevance: Does the answer address the question?
- completeness: Does it adequately explain the situation, action,
  and result or responsibility?
- specificity: Does it provide concrete details or examples?
- clarity: Is the answer understandable and well organized?

For general_knowledge questions, evaluate:

- correctness: Is the factual or conceptual information correct?
- completeness: Does the answer sufficiently explain the concept?
- relevance: Does the answer stay focused on the question?
- clarity: Is the explanation understandable?

Give REAL scores from 0 to 10 based on the candidate's actual answer.
Do not use placeholder values.

Score interpretation:

0-3 = poor
4-5 = weak
6-7 = partially correct
8 = good
9-10 = excellent

The final score must be consistent with correctness:

- incorrect: maximum 3.0
- partially_correct: maximum 7.9
- correct: minimum 8.0

Return ONLY valid JSON with exactly these fields:

question_type
relevance
completeness
specificity
clarity
correctness
feedback

The numeric fields must contain actual numbers from 0 to 10.

The correctness field must be exactly one of:
"incorrect"
"partially_correct"
"correct"

The feedback should briefly explain the strengths and weaknesses of the candidate's answer.
"""

    result = ask_local_llm_json(
        prompt,
        system_prompt=(
            "You are a strict but fair interview evaluator. "
            "Evaluate the candidate's actual answer. "
            "Return only valid JSON."
        ),
    )

    question_type = str(
        result.get("question_type", "general_knowledge")
    ).lower()

    relevance = float(result.get("relevance", 0))
    completeness = float(result.get("completeness", 0))
    specificity = float(result.get("specificity", 0))
    clarity = float(result.get("clarity", 0))

    correctness = str(
        result.get("correctness", "incorrect")
    ).lower()

    feedback = str(
        result.get(
            "feedback",
            "The answer was evaluated based on its relevance and quality.",
        )
    )

    if question_type in {"behavioral", "resume_experience"}:
        score = (
            relevance * 0.35
            + completeness * 0.25
            + specificity * 0.25
            + clarity * 0.15
        )
    else:
        if correctness == "correct":
            factual_score = 10.0
        elif correctness == "partially_correct":
            factual_score = 6.0
        else:
            factual_score = 0.0

        score = (
            factual_score * 0.50
            + completeness * 0.30
            + relevance * 0.20
        )

    if correctness == "incorrect":
        score = min(score, 3.0)
    elif correctness == "partially_correct":
        score = min(score, 7.9)
    elif correctness == "correct":
        score = max(score, 8.0)

    score = round(max(0.0, min(10.0, score)), 1)

    print("\n" + "=" * 60)
    print("QWEN EVALUATION")
    print("=" * 60)

    print(f"\nQuestion Type: {question_type}")
    print(f"Relevance: {relevance:.1f}/10")
    print(f"Completeness: {completeness:.1f}/10")
    print(f"Specificity: {specificity:.1f}/10")
    print(f"Clarity: {clarity:.1f}/10")
    print(f"Score: {score:.1f}/10")
    print(f"Correctness: {correctness}")
    print(f"Feedback: {feedback}")

    return InterviewEvaluation(
        score=score,
        correctness=correctness,
        feedback=feedback,
    )