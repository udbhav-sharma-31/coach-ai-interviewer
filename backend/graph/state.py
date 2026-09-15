from typing import TypedDict


class InterviewGraphState(TypedDict):

    # ---------------------------------------------------------
    # Candidate information
    # ---------------------------------------------------------

    candidate: dict

    # Explicit target role selected by the candidate.
    target_role: str

    # Grounded information extracted from the resume.
    resume_profile: dict
    resume_path: str
    # ---------------------------------------------------------
    # Resume / RAG
    # ---------------------------------------------------------

    resume_available: bool
    resume_context: str

    # ---------------------------------------------------------
    # Interview planning
    # ---------------------------------------------------------

    covered_topics: list[str]

    current_question: str
    current_topic: str
    evaluation_mode: str

    # ---------------------------------------------------------
    # Current answer
    # ---------------------------------------------------------

    current_answer: str
    evaluation: dict | None

    # ---------------------------------------------------------
    # Interview history
    # ---------------------------------------------------------

    answers: list[str]
    evaluations: list[dict]

    questions: list[str]

    # ---------------------------------------------------------
    # Interview control
    # ---------------------------------------------------------

    question_number: int
    difficulty: str
    max_questions: int
    final_report: dict | None