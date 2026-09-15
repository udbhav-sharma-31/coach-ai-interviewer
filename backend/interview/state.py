from dataclasses import dataclass, field


@dataclass
class InterviewEvaluation:
    score: float
    correctness: str
    feedback: str


@dataclass
class InterviewState:
    candidate: object
    current_question: str = ""
    answers: list[str] = field(default_factory=list)
    evaluations: list[InterviewEvaluation] = field(default_factory=list)
    question_number: int = 0
    score: float = 0.0
    difficulty: str = "beginner"