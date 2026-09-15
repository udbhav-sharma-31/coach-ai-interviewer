from backend.llm.local_client import ask_local_llm_json


def normalize_text(value, fallback):
    if isinstance(value, list):
        items = [
            str(item).strip()
            for item in value
            if str(item).strip()
        ]

        if items:
            return " ".join(items)

        return fallback

    if isinstance(value, str):
        cleaned = value.strip()

        if cleaned:
            return cleaned

    return fallback


def generate_final_report(
    questions: list[str],
    answers: list[str],
    evaluations: list[dict],
) -> dict:

    interview_data = []

    for index, question in enumerate(questions):

        answer = (
            answers[index]
            if index < len(answers)
            else ""
        )

        evaluation = (
            evaluations[index]
            if index < len(evaluations)
            else {}
        )

        interview_data.append(
            {
                "question": question,
                "answer": answer,
                "score": evaluation.get(
                    "score",
                    0,
                ),
                "correctness": evaluation.get(
                    "correctness",
                    "unknown",
                ),
                "feedback": evaluation.get(
                    "feedback",
                    "",
                ),
            }
        )

    prompt = f"""
You are the final report generator for an AI interview platform.

Analyze the candidate's complete interview.

INTERVIEW DATA:
{interview_data}

Generate a concise and evidence-based final interview report.

IMPORTANT RULES:

1. Use ONLY information contained in the supplied
   interview data.

2. Do NOT invent candidate experience, projects,
   skills, achievements, technologies, or knowledge.

3. Do NOT treat saying "I don't know", "I am unable
   to answer", "I cannot recall", or giving an incorrect
   answer as a strength.

4. Weak, incorrect, incomplete, or missing answers
   should be discussed under improvements.

5. A strength must be supported by an answer that
   actually demonstrates that strength.

6. Do not praise the candidate merely for admitting
   that they do not know something.

7. Do not make claims that are not supported by the
   candidate's actual answers.

8. Base the report on the complete interview rather
   than focusing on only one question.

Return ONLY valid JSON with exactly these fields:

strengths
improvements
recommendation

Each field must contain a STRING.

Do not return arrays.
Do not return markdown.
Do not include extra JSON fields.

STRENGTHS:
Mention 2 to 3 genuine strengths demonstrated by
the candidate's actual answers.

If the candidate did not demonstrate meaningful
strengths, say so honestly instead of inventing them.

IMPROVEMENTS:
Mention 2 to 3 specific areas that should be improved.
Base these directly on weak, incomplete, incorrect,
or missing answers.

RECOMMENDATION:
Give a concise, personalized recommendation for
what the candidate should practice next.
"""

    result = ask_local_llm_json(
        prompt,
        system_prompt=(
            "You are a strict, honest, evidence-based "
            "interview report generator. "
            "Never invent strengths or experience. "
            "Never praise a candidate for not knowing "
            "an answer. "
            "Return valid JSON only."
        ),
    )

    strengths = normalize_text(
        result.get("strengths"),
        "The interview did not provide enough evidence of strong responses.",
    )

    improvements = normalize_text(
        result.get("improvements"),
        "Focus on providing more complete, relevant, and specific answers.",
    )

    recommendation = normalize_text(
        result.get("recommendation"),
        "Continue practicing interview questions and focus on improving weaker areas.",
    )

    return {
        "strengths": strengths,
        "improvements": improvements,
        "recommendation": recommendation,
    }