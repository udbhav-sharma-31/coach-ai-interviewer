from backend.llm.client import ask_llm
from backend.llm.prompts import (
    INTERVIEWER_SYSTEM_PROMPT,
    build_candidate_context,
)
from backend.interview.candidate import Candidate


candidate = Candidate(
    name="Udbhav",
    role="Python Developer",
    experience_level="Beginner",
    skills=["Python", "Machine Learning", "Generative AI"],
)


candidate_context = build_candidate_context(candidate)


response = ask_llm(
    candidate_context
    + "\nStart the interview by asking me one appropriate question.",
    system_prompt=INTERVIEWER_SYSTEM_PROMPT,
)


print("\nAI Interviewer:")
print(response)