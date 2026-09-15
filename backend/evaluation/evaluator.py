from backend.evaluation.predictor import InterviewEvaluator
from backend.interview.state import InterviewEvaluation
from backend.llm.local_client import ask_local_llm_json


# Load the custom Transformer once when the backend starts.
_transformer_evaluator = InterviewEvaluator()


HYBRID_SYSTEM_PROMPT = """
You are a strict technical interview evaluator.

Evaluate the candidate's answer against the question.

You receive a signal from a custom Transformer model.
Use it as supporting evidence, but make your own semantic judgment.

Return ONLY valid JSON. No reasoning. No explanation.

Evaluate these three dimensions separately:

1. technical_correctness:
   How technically correct is the answer?
   Score from 0 to 10.

2. completeness:
   How completely does the answer address the question?
   Score from 0 to 10.

3. relevance:
   How directly does the answer address the question?
   Score from 0 to 10.

Scoring guidance:

Technical correctness:
- 0-2: Fundamentally incorrect
- 3-4: Mostly incorrect with limited understanding
- 5-6: Some correct understanding but important errors
- 7-8: Technically correct with minor issues
- 9-10: Fully accurate and precise

Completeness:
- 0-2: Does not address the question meaningfully
- 3-4: Addresses only a small part
- 5-6: Addresses the main idea but misses important details
- 7-8: Covers most important points
- 9-10: Thoroughly addresses the question

Relevance:
- 0-2: Irrelevant
- 3-4: Mostly unrelated
- 5-6: Partially relevant
- 7-8: Directly relevant
- 9-10: Completely focused on the question

Important:
- A short basic definition should NOT automatically receive a high
  completeness score.
- A technically correct answer can still have low completeness.
- Do not give high scores simply because the answer contains relevant keywords.
- Judge what the candidate actually explained.
- If the answer is fundamentally wrong, technical correctness must be low.
- If the answer does not answer the question, relevance must be low.

Also provide:
- correctness: exactly "correct", "partially_correct", or "incorrect"
- feedback: one short sentence explaining the main strength or weakness

Return this exact structure:

{
    "technical_correctness": 8,
    "completeness": 6,
    "relevance": 9,
    "correctness": "partially_correct",
    "feedback": "The answer is technically correct but misses important details."
}
"""


def evaluate_answer(question: str, answer: str) -> InterviewEvaluation:

    # ---------------------------------------------------------
    # 1. EMPTY ANSWER
    # ---------------------------------------------------------

    if not answer or not answer.strip():
        return InterviewEvaluation(
            score=0.0,
            correctness="incorrect",
            feedback="No answer was provided.",
        )


    # ---------------------------------------------------------
    # 2. CUSTOM TRANSFORMER
    # ---------------------------------------------------------

    transformer_result = _transformer_evaluator.evaluate(
        question=question,
        answer=answer,
    )

    transformer_score = transformer_result["score"]
    transformer_label = transformer_result["label"]
    transformer_confidence = transformer_result["confidence"]


    # ---------------------------------------------------------
    # 3. QWEN SEMANTIC EVALUATION
    # ---------------------------------------------------------

    prompt = f"""
Question:
{question}

Candidate Answer:
{answer}

Custom Transformer Evaluation:
Quality: {transformer_result["quality"]}
Transformer Score: {transformer_score}/10
Transformer Confidence: {transformer_confidence}

Now independently evaluate the candidate's answer.

Use the Transformer result only as supporting evidence.

Pay particular attention to whether the answer actually answers
the question and whether its technical claims are correct.

Return:
- technical_correctness
- completeness
- relevance
- correctness
- feedback
"""

    schema = {
        "type": "object",
        "properties": {
            "technical_correctness": {
                "type": "integer",
                "minimum": 0,
                "maximum": 10
            },
            "completeness": {
                "type": "integer",
                "minimum": 0,
                "maximum": 10
            },
            "relevance": {
                "type": "integer",
                "minimum": 0,
                "maximum": 10
            },
            "correctness": {
                "type": "string",
                "enum": [
                    "correct",
                    "partially_correct",
                    "incorrect"
                ]
            },
            "feedback": {
                "type": "string"
            }
        },
        "required": [
            "technical_correctness",
            "completeness",
            "relevance",
            "correctness",
            "feedback"
        ]
    }

    data = ask_local_llm_json(
        prompt,
        system_prompt=HYBRID_SYSTEM_PROMPT,
        schema=schema,
    )


    # ---------------------------------------------------------
    # 4. QWEN SCORE
    # ---------------------------------------------------------

    qwen_score = (
        0.50 * data["technical_correctness"]
        + 0.30 * data["completeness"]
        + 0.20 * data["relevance"]
    )


    # ---------------------------------------------------------
    # 5. CONFIDENCE-AWARE HYBRID SCORE
    # ---------------------------------------------------------

    # High-confidence Transformer predictions receive more weight.
    #
    # Low-confidence predictions allow Qwen to contribute more.

    transformer_weight = 0.40 + (0.40 * transformer_confidence)

    qwen_weight = 1.0 - transformer_weight

    final_score = (
        transformer_weight * transformer_score
        + qwen_weight * qwen_score
    )


    # ---------------------------------------------------------
    # 6. SAFETY GUARDRAILS FOR SCORE
    # ---------------------------------------------------------

    # High-confidence "Incorrect" prediction.
    # Do not allow Qwen to pull the score into the passing range.

    if transformer_label == 0 and transformer_confidence >= 0.80:
        final_score = min(final_score, 2.9)


    # High-confidence "Weak" prediction.
    # Keep it below the "Good" range.

    elif transformer_label == 1 and transformer_confidence >= 0.85:
        final_score = min(final_score, 4.9)


    # Partially correct answers should normally remain below 8
    # unless both models strongly support a good answer.

    elif transformer_label == 2:
        if qwen_score < 8:
            final_score = min(final_score, 7.4)


    # Keep score inside 0-10.

    final_score = max(0.0, min(10.0, final_score))


    # ---------------------------------------------------------
    # 7. FINAL CORRECTNESS CATEGORY
    # ---------------------------------------------------------

    # A fundamentally technically incorrect answer must be incorrect,
    # even if the Transformer predicts "Weak" instead of "Incorrect".

    if data["technical_correctness"] <= 5:
        correctness = "incorrect"

    elif transformer_label == 0:
        correctness = "incorrect"

    elif data["correctness"] == "incorrect":
        correctness = "incorrect"

    elif transformer_label in (1, 2):
        correctness = "partially_correct"

    else:
        if (
            data["correctness"] == "correct"
            and data["technical_correctness"] >= 7
            and data["relevance"] >= 7
            and final_score >= 8.0
        ):
            correctness = "correct"
        else:
            correctness = "partially_correct"


    # ---------------------------------------------------------
    # 8. ALIGN SCORE WITH FINAL CATEGORY
    # ---------------------------------------------------------

    if correctness == "incorrect":

        final_score = min(final_score, 3.0)

    elif correctness == "partially_correct":

        final_score = min(final_score, 7.9)

    else:

        final_score = max(final_score, 8.0)


    # Keep score inside 0-10.
    final_score = max(0.0, min(10.0, final_score))

    # ---------------------------------------------------------
    # 9. DEBUG INFORMATION
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("HYBRID EVALUATION")
    print("=" * 60)

    print("\nTransformer:")
    print(f"Quality: {transformer_result['quality']}")
    print(f"Score: {transformer_score}/10")
    print(f"Confidence: {transformer_confidence}")

    print("\nQwen:")
    print(f"Technical Correctness: {data['technical_correctness']}/10")
    print(f"Completeness: {data['completeness']}/10")
    print(f"Relevance: {data['relevance']}/10")
    print(f"Qwen Score: {qwen_score:.1f}/10")

    print("\nHybrid:")
    print(f"Transformer Weight: {transformer_weight:.2f}")
    print(f"Qwen Weight: {qwen_weight:.2f}")
    print(f"Final Score: {final_score:.1f}/10")
    print(f"Final Correctness: {correctness}")

    print(f"\nFeedback: {data['feedback']}")

    print("=" * 60)


    return InterviewEvaluation(
        score=round(final_score, 1),
        correctness=correctness,
        feedback=data["feedback"],
    )