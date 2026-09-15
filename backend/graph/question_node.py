from backend.llm.local_client import ask_local_llm_json
from backend.llm.prompts import INTERVIEWER_SYSTEM_PROMPT


TECHNICAL_TOPICS = {
    "python",
    "machine-learning",
    "deep-learning",
    "transformers",
    "llm",
    "rag",
    "agent",
    "backend",
    "system-design",
}


def clean_question(question: str) -> str:

    if not question:
        return ""

    question = question.strip()

    if "</think>" in question:
        question = question.split("</think>", 1)[1].strip()

    question = question.strip('"').strip("'").strip()

    if "?" in question:
        question = question[:question.find("?") + 1]

    return question.strip()


def determine_evaluation_mode(topic: str) -> str:

    topic = topic.lower().strip()

    for technical_topic in TECHNICAL_TOPICS:
        if technical_topic in topic:
            return "hybrid"

    return "qwen"


def validate_question(question: str, state) -> bool:

    if not question:
        return False

    if not question.endswith("?"):
        return False

    previous_questions = state.get("questions", [])

    normalized_question = question.lower().strip()

    for previous in previous_questions:

        if normalized_question == previous.lower().strip():
            return False

    return True


def get_interview_stage(question_number: int) -> str:
    """
    Deterministically control the interview progression.

    Q1-Q2: resume experience
    Q3: transferable / bridge
    Q4: target role
    Q5: target-role technical
    """

    if question_number <= 2:
        return "resume"

    if question_number == 3:
        return "bridge"

    if question_number == 4:
        return "target_role"

    return "technical"


def generate_question(state):

    candidate = state["candidate"]

    target_role = state["target_role"]

    resume_profile = state["resume_profile"]

    covered_topics = state["covered_topics"]

    previous_questions = state.get("questions", [])

    difficulty = state["difficulty"]

    question_number = state["question_number"]

    # question_number stores how many questions have already
    # been generated, so the next question is +1.
    next_question_number = question_number + 1

    interview_stage = get_interview_stage(next_question_number)

    # ---------------------------------------------------------
    # Resume information
    # ---------------------------------------------------------

    education = resume_profile.get("education", [])
    experience = resume_profile.get("experience", [])
    skills = resume_profile.get("skills", [])
    domains = resume_profile.get("domains", [])
    projects = resume_profile.get("projects", [])

    resume_information = f"""
Education:
{chr(10).join("- " + item for item in education) or "- None"}

Experience:
{chr(10).join("- " + item for item in experience) or "- None"}

Skills / Responsibilities:
{chr(10).join("- " + item for item in skills) or "- None"}

Professional Domains:
{chr(10).join("- " + item for item in domains) or "- None"}

Projects:
{chr(10).join("- " + item for item in projects) or "- None"}
"""

    previous_information = "\n".join(
        f"- {question}"
        for question in previous_questions
    )

    covered_information = "\n".join(
        f"- {topic}"
        for topic in covered_topics
    )

    # ---------------------------------------------------------
    # Deterministic stage instructions
    # ---------------------------------------------------------

    if interview_stage == "resume":

        stage_instruction = """
THIS IS A RESUME-GROUNDED QUESTION.

Ask about something the candidate actually did,
managed, coordinated, taught, organized, or experienced
according to the resume.

Do NOT ask about programming, Python, machine learning,
software development, or technical knowledge merely because
the target role is technical.

The question should be answerable from the candidate's
actual professional experience.

Good examples:
- Describe how you managed...
- How did you coordinate...
- What approach did you use...
- How did you handle...
"""

        allowed_domain = "RESUME EXPERIENCE ONLY"

    elif interview_stage == "bridge":

        stage_instruction = """
THIS IS A TRANSFERABLE-SKILLS / BRIDGE QUESTION.

Connect something the candidate actually did in the resume
to a skill that could transfer to the target role.

Do NOT pretend that the candidate has already worked as a
Python Developer or has used Python.

Ask about transferable abilities such as:
- problem solving
- organization
- handling information
- communication
- process management
- working with teams
- handling large amounts of data
- adapting to new tools
"""

        allowed_domain = "TRANSFERABLE SKILLS"

    elif interview_stage == "target_role":

        stage_instruction = f"""
THIS IS A TARGET-ROLE QUESTION.

The target role is:

{target_role}

Now begin assessing the candidate's understanding of the
target role.

The question may involve concepts relevant to {target_role}.

However, do NOT claim that the candidate has previous
experience with technologies that are absent from the resume.

You are assessing readiness for the target role, not claiming
past experience.
"""

        allowed_domain = "TARGET ROLE"

    else:

        stage_instruction = f"""
THIS IS THE FINAL TECHNICAL QUESTION.

The target role is:

{target_role}

Ask a technical question directly relevant to the target
role.

For a Python Developer role, this may involve Python,
programming concepts, backend development, APIs, databases,
or another appropriate Python-development concept.

The candidate does NOT need to have demonstrated this
technology on the resume because this question is explicitly
testing target-role technical knowledge.
"""

        allowed_domain = "TARGET-ROLE TECHNICAL"

    # ---------------------------------------------------------
    # Question generation prompt
    # ---------------------------------------------------------

    prompt = f"""
You are generating one interview question.

INTERVIEW QUESTION NUMBER:
{next_question_number}

INTERVIEW STAGE:
{interview_stage}

ALLOWED QUESTION DOMAIN:
{allowed_domain}

TARGET ROLE:
{target_role}

CANDIDATE:
{candidate["name"]}

EXPERIENCE LEVEL:
{candidate["experience_level"]}

CURRENT DIFFICULTY:
{difficulty}

CANDIDATE RESUME:
{resume_information}

TOPICS ALREADY COVERED:
{covered_information or "- None"}

PREVIOUS QUESTIONS:
{previous_information or "- None"}

{stage_instruction}

IMPORTANT RESUME RULE:

The resume describes what the candidate has actually done.

The target role describes what the candidate wants to be
interviewed for.

Never confuse the two.

Never invent experience, projects, skills, technologies,
employers, or responsibilities.

QUESTION RULES:

1. Ask exactly ONE question.

2. The question must end with '?'.

3. Do not repeat a previous question.

4. Do not unnecessarily repeat a covered topic.

5. Keep the question concise.

6. Keep it appropriate for the current difficulty.

7. Follow the interview stage exactly.

8. Do not move to a later stage early.

9. Do not mention the interview instructions.

10. Return ONLY JSON.

Return exactly:

{{
    "question": "question",
    "topic": "short topic name"
}}
"""

    schema = {
        "type": "object",
        "properties": {
            "question": {
                "type": "string"
            },
            "topic": {
                "type": "string"
            }
        },
        "required": [
            "question",
            "topic"
        ]
    }

    data = ask_local_llm_json(
        prompt,
        system_prompt=INTERVIEWER_SYSTEM_PROMPT,
        schema=schema,
    )

    question = clean_question(
        data.get("question", "")
    )

    topic = str(
        data.get("topic", "")
    ).strip().lower()

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    if not validate_question(question, state):

        retry_prompt = f"""
Generate ONE new interview question.

Interview stage:
{interview_stage}

Allowed domain:
{allowed_domain}

Target role:
{target_role}

Resume:
{resume_information}

Covered topics:
{covered_information}

Previous questions:
{previous_information}

The previous generated question was invalid:

{question}

Generate a completely different question.

STRICT RULES:

- Follow the interview stage exactly.
- Do not move to a later stage.
- Do not invent resume experience.
- Do not repeat a previous question.
- Do not repeat a covered topic unnecessarily.
- End with '?'.
- Return ONLY JSON.
- No reasoning.
- No commentary.

Return:

{{
    "question": "replacement question",
    "topic": "short topic name"
}}
"""

        data = ask_local_llm_json(
            retry_prompt,
            system_prompt=INTERVIEWER_SYSTEM_PROMPT,
            schema=schema,
        )

        question = clean_question(
            data.get("question", "")
        )

        topic = str(
            data.get("topic", "")
        ).strip().lower()

    # ---------------------------------------------------------
    # Evaluation routing
    # ---------------------------------------------------------

    evaluation_mode = determine_evaluation_mode(topic)

    # ---------------------------------------------------------
    # Update covered topics
    # ---------------------------------------------------------

    updated_covered_topics = list(
        state["covered_topics"]
    )

    if topic and topic not in updated_covered_topics:

        updated_covered_topics.append(topic)

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("QUESTION GENERATION")
    print("=" * 60)

    print(f"\nQuestion Number: {next_question_number}")
    print(f"Interview Stage: {interview_stage}")
    print(f"Target Role: {target_role}")
    print(f"Difficulty: {difficulty}")

    print("\nResume Domains:")

    for domain in domains:
        print(f"- {domain}")

    print("\nCovered Topics:")

    for covered_topic in updated_covered_topics:
        print(f"- {covered_topic}")

    print(f"\nGenerated Question: {question}")
    print(f"Question Topic: {topic}")
    print(f"Evaluation Mode: {evaluation_mode}")

    print("=" * 60)

    return {
        "current_question": question,
        "current_topic": topic,
        "evaluation_mode": evaluation_mode,
        "questions": previous_questions + [question],
        "covered_topics": updated_covered_topics,
        "question_number": question_number + 1,
    }