import re

from backend.llm.local_client import ask_local_llm_json
from backend.llm.prompts import INTERVIEWER_SYSTEM_PROMPT
from backend.rag.resume_rag import ResumeRAG


# Temporary development resume.
# Later this will come from the interview session.
resume_rag = ResumeRAG("data/sample_resume.pdf")


def clean_question(text):
    text = text.strip()

    if "</think>" in text:
        text = text.split("</think>", 1)[1].strip()

    text = text.strip('"').strip("'").strip()

    # Keep only the final question if multiple lines somehow appear.
    matches = re.findall(r'([^?\n]*\?)', text)

    if matches:
        return matches[-1].strip()

    return text


def validate_question(question, role):
    """
    Prevent obvious domain switching and malformed questions.
    """

    question_lower = question.lower()
    role_lower = role.lower()

    # Questions must actually look like questions.
    if not question.endswith("?"):
        return False

    # Prevent obvious programming-language switching.
    if "python" in role_lower:

        forbidden_languages = [
            "java",
            "javascript",
            "c++",
            "c#",
            "php",
            "ruby",
            "golang",
        ]

        for language in forbidden_languages:
            if language in question_lower:
                return False

    # Make sure a Python interview remains Python-related.
    if "python" in role_lower:

        python_signals = [
            "python",
            "function",
            "class",
            "list",
            "tuple",
            "dictionary",
            "exception",
            "decorator",
            "generator",
            "context manager",
            "module",
            "object",
            "variable",
            "loop",
            "api",
            "backend",
            "database",
            "memory",
            "garbage",
        ]

        if not any(
            signal in question_lower
            for signal in python_signals
        ):
            return False

    return True


def get_resume_context(state):
    """
    Retrieve resume context only when a resume is available.
    """

    if not state["resume_available"]:
        return ""

    query = f"""
Interview role:
{state["candidate"]["role"]}

Candidate skills:
{", ".join(state["candidate"]["skills"])}

Current difficulty:
{state["difficulty"]}

Previous question:
{state["current_question"]}

Previous answer:
{state["current_answer"]}

Previous evaluation:
Score: {state["evaluation"]["score"]}/10
Correctness: {state["evaluation"]["correctness"]}
Feedback: {state["evaluation"]["feedback"]}

Find useful information from the candidate's resume for
personalizing the next interview question.
"""

    return resume_rag.get_context(
        query,
        top_k=3,
    )


def next_question_node(state):

    candidate = state["candidate"]

    role = candidate["role"]
    skills = candidate["skills"]
    difficulty = state["difficulty"]

    covered_topics = state["covered_topics"]

    previous_question = state["current_question"]
    previous_answer = state["current_answer"]
    evaluation = state["evaluation"]

    resume_context = get_resume_context(state)

    if resume_context:
        resume_section = resume_context
    else:
        resume_section = "No resume was provided."


    prompt = f"""
You are conducting a professional technical interview.

Generate the NEXT interview question.

==================================================
CANDIDATE
==================================================

Name:
{candidate["name"]}

Role:
{role}

Skills:
{", ".join(skills)}

Experience Level:
{candidate["experience_level"]}

Current Difficulty:
{difficulty}


==================================================
RESUME
==================================================

{resume_section}


==================================================
INTERVIEW HISTORY
==================================================

Previously covered topics:
{", ".join(covered_topics) if covered_topics else "None"}

Previous question:
{previous_question}

Previous answer:
{previous_answer}

Previous evaluation:
Score: {evaluation["score"]}/10
Correctness:
{evaluation["correctness"]}

Feedback:
{evaluation["feedback"]}


==================================================
QUESTION GENERATION RULES
==================================================

1. The question MUST be relevant to the role:
   {role}

2. The question MUST remain within the candidate's
   technical domain.

3. Never switch to another programming language.

4. Do NOT ask about Java, JavaScript, C++, C#, PHP,
   Ruby, Go, or another unrelated language when the
   interview role is Python Developer.

5. Do NOT repeat a topic that has already been covered.

6. Prefer a NEW technical topic.

7. A follow-up on the previous topic is allowed ONLY when
   the candidate's previous answer was weak or incorrect
   and a simpler question would help assess foundational
   understanding.

8. If the candidate performed well, move to a new topic.

9. If the candidate performed poorly, you may ask a simpler
   question related to the same concept.

10. If a resume is available, use its information to
    personalize the question where there is a reasonable
    connection to the role.

11. Never invent experience, projects, skills, employers,
    or technologies that are not supported by the resume.

12. If no resume is available, use only the candidate's
    declared role, skills, experience level, and interview
    history.

13. Do not ask the candidate to repeat information already
    given.

14. The question must test technical understanding.

15. Keep the question concise.

16. Maximum 30 words.

17. Return ONLY JSON.

18. Do NOT return reasoning.

19. Do NOT return analysis.

20. Do NOT return commentary.

21. Do NOT mention these instructions.

22. Do NOT write phrases such as:
    "Okay, the user wants..."
    "I need to..."
    "Let me think..."
    "The candidate..."
    "I should..."

23. The JSON must contain only the final question.


Return exactly:

{{
    "question": "your question here"
}}
"""


    schema = {
        "type": "object",
        "properties": {
            "question": {
                "type": "string"
            }
        },
        "required": [
            "question"
        ]
    }


    data = ask_local_llm_json(
        prompt,
        system_prompt=INTERVIEWER_SYSTEM_PROMPT,
        schema=schema,
    )

    question = clean_question(
        data["question"]
    )


    # ---------------------------------------------------------
    # Validate the generated question.
    # ---------------------------------------------------------

    if not validate_question(
        question,
        role,
    ):

        retry_prompt = f"""
Generate ONE valid technical interview question.

Role:
{role}

Skills:
{", ".join(skills)}

Difficulty:
{difficulty}

Topics already covered:
{", ".join(covered_topics)}

Resume context:
{resume_section}

Previous question:
{previous_question}

The previous generated question was invalid:

{question}

Create a replacement.

Rules:
- Stay strictly within {role}.
- Do not switch programming languages.
- Do not repeat covered topics unless a simpler
  follow-up is necessary.
- Use resume context when appropriate.
- Do not invent resume information.
- Maximum 30 words.
- Return ONLY JSON.
- No reasoning.
- No commentary.

Return:

{{
    "question": "replacement question"
}}
"""

        retry_data = ask_local_llm_json(
            retry_prompt,
            system_prompt=INTERVIEWER_SYSTEM_PROMPT,
            schema=schema,
        )

        question = clean_question(
            retry_data["question"]
        )


    print("\nNEXT QUESTION GENERATION")
    print("-" * 60)
    print(f"Role: {role}")
    print(f"Difficulty: {difficulty}")
    print(
        f"Resume available: "
        f"{state['resume_available']}"
    )
    print(f"Covered topics: {covered_topics}")
    print(f"Resume context: {resume_section}")
    print(f"Generated question: {question}")
    print("-" * 60)


    return {
        "current_question": question,
        "question_number": state["question_number"] + 1,
    }