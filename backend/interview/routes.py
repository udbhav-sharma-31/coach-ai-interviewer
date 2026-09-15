import uuid

from fastapi import APIRouter, File, Form, UploadFile
from pydantic import BaseModel
from langgraph.types import Command

from backend.graph.graph import interview_graph


router = APIRouter(
    prefix="/interview",
    tags=["Interview"],
)



class AnswerRequest(BaseModel):
    session_id: str
    answer: str


# Store the LangGraph thread configuration for each API session.
interview_sessions: dict[str, dict] = {}


@router.post("/start")
async def start_interview(
    name: str = Form(...),
    role: str = Form(...),
    experience_level: str = Form(...),
    skills: str = Form(""),
    resume: UploadFile = File(...),
):

    session_id = str(uuid.uuid4())

    candidate = {
        "name": name,
        "role": role,
        "experience_level": experience_level,
        "skills": [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ],
    }
    resume_path = f"data/resumes/{session_id}.pdf"

    import os

    os.makedirs("data/resumes", exist_ok=True)

    resume_contents = await resume.read()

    with open(resume_path, "wb") as f:
        f.write(resume_contents)

    initial_state = {
        "candidate": candidate,

        "target_role": role,
        "resume_path": resume_path,
        "resume_profile": {
            "education": [],
            "experience": [],
            "skills": [],
            "domains": [],
            "projects": [],
            "certifications": [],
        },

        "resume_available": True,
        "resume_context": "",

        "covered_topics": [],

        "current_question": "",
        "current_topic": "",
        "evaluation_mode": "",

        "current_answer": "",
        "evaluation": None,

        "answers": [],
        "evaluations": [],
        "questions": [],

        "question_number": 0,
        "difficulty": "beginner",
        "max_questions": 5,
    }

    config = {
        "configurable": {
            "thread_id": session_id
        }
    }

    result = interview_graph.invoke(
        initial_state,
        config=config,
    )

    interview_sessions[session_id] = config

    return {
        "session_id": session_id,
        "candidate": candidate,
        "question": result["current_question"],
        "question_number": result["question_number"],
        "difficulty": result["difficulty"],
    }


@router.post("/answer")
def submit_answer(request: AnswerRequest):

    if request.session_id not in interview_sessions:
        return {
            "error": "Interview session not found."
        }

    config = interview_sessions[request.session_id]

    result = interview_graph.invoke(
        Command(resume=request.answer),
        config=config,
    )

    # Interview is still running
    if "__interrupt__" in result:

        return {
            "session_id": request.session_id,
            "evaluation": result["evaluation"],
            "next_question": result["current_question"],
            "question_number": result["question_number"],
            "difficulty": result["difficulty"],
            "finished": False,
        }

    # Interview has finished
    evaluations = result["evaluations"]

    scores = [
        evaluation["score"]
        for evaluation in evaluations
    ]

    overall_score = (
        sum(scores) / len(scores)
        if scores
        else 0.0
    )

    return {
    "session_id": request.session_id,
    "finished": True,
    "evaluation": result["evaluation"],
    "questions": result["questions"],
    "answers": result["answers"],
    "evaluations": result["evaluations"],
    "difficulty": result["difficulty"],
    "question_number": result["question_number"],
    "overall_score": round(overall_score, 1),
    "final_report": result.get("final_report"),
    "next_question": None,
}

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF resumes are supported."
        }

    contents = await file.read()

    if not contents:
        return {
            "error": "Uploaded resume is empty."
        }

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "message": "Resume uploaded successfully."
    }